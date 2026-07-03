#!/usr/bin/env python3
"""
lit — multi-collection literature graph CLI.

usage:
    lit papers [--in-collection] [--external] [--uncited] [--no-uncited]  list papers
    lit paper ID                   show paper details + citation neighbors
    lit concepts                   list all concepts with paper counts
    lit search TERM                search titles, concepts, key_finding
    lit list [--concept C] [--region R] [--type T] [--in-collection] [--external]  filter
    lit graph ID                   show citation graph (cites + cited-by)
    lit neighbors ID               papers sharing concepts
    lit missing                    papers with empty references
    lit stats                      summary counts
    lit viz                        citation network (opens in browser)
        [--pid=ID]  [--in-collection]  [--concept=C]  [--output=FILE]
        [--collection=NAME]

    All commands accept --collection=NAME to scope to a single collection.
    Without it, every registered collection is loaded.
"""

import sys, os, yaml, re, glob
from collections import defaultdict

LIT_DIR = os.path.dirname(os.path.abspath(__file__))

COLLECTIONS = {}

def register_collection(name, base_dirname):
    COLLECTIONS[name] = {
        "dir": os.path.join(LIT_DIR, base_dirname),
        "uncited_dir": os.path.join(LIT_DIR, f"{base_dirname}_uncited"),
        "stubs_dir": os.path.join(LIT_DIR, f"{base_dirname}_stubs"),
        "vocab_path": os.path.join(LIT_DIR, base_dirname, "vocabulary.yaml"),
    }

register_collection("EnergyBurden", "EnergyBurden")
register_collection("SemanticGapSDG", "SemanticGapSDG")

def load_vocab(collection=None):
    vocab = {}
    names = [collection] if collection else list(COLLECTIONS.keys())
    for name in names:
        vp = COLLECTIONS[name]["vocab_path"]
        try:
            with open(vp) as f:
                data = yaml.safe_load(f)
        except:
            continue
        if not isinstance(data, dict):
            continue
        for group, concepts in data.items():
            if isinstance(concepts, dict):
                for cid, cinfo in concepts.items():
                    if isinstance(cinfo, dict):
                        vocab[cid] = f"{cinfo.get('label','')} {cinfo.get('desc','')}"
    return vocab

def load(collection=None):
    """Load all .meta.yaml files from every registered collection (or one)."""
    papers = {}
    names = [collection] if collection else list(COLLECTIONS.keys())
    for name in names:
        c = COLLECTIONS[name]
        for meta_dir in [c["stubs_dir"], c["uncited_dir"], c["dir"]]:
            if not os.path.isdir(meta_dir):
                continue
            for fpath in glob.glob(os.path.join(meta_dir, "*.meta.yaml")):
                with open(fpath) as f:
                    entry = yaml.safe_load(f)
                if entry and "pid" in entry:
                    pid = entry["pid"]
                    entry.pop("pid")
                    entry["_uncited"] = (meta_dir == c["uncited_dir"])
                    entry["_collection"] = name
                    papers[pid] = entry
    return papers

def save(pid, p):
    """Write a single .meta.yaml file for a paper entry."""
    collection = p.get("_collection", "EnergyBurden")
    c = COLLECTIONS[collection]
    entry = {"pid": pid}
    entry.update(p)
    entry.pop("_uncited", None)
    entry.pop("_collection", None)
    if p.get("_uncited"):
        meta_dir = c["uncited_dir"]
    elif p.get("in_collection", True):
        meta_dir = c["dir"]
    else:
        meta_dir = c["stubs_dir"]
    path = os.path.join(meta_dir, f"{pid}.meta.yaml")
    with open(path, "w") as f:
        yaml.dump(entry, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

def paper_id(pid):
    return pid.replace(" ", "_").replace("-", "_").replace(".pdf", "")

def in_collection(p):
    return p.get("in_collection", True)

def is_uncited(p):
    return p.get("_uncited", False)

def color(s, c):
    colors = {"green": "\033[92m", "yellow": "\033[93m", "blue": "\033[94m", "cyan": "\033[96m", "bold": "\033[1m", "dim": "\033[2m", "reset": "\033[0m"}
    return f"{colors.get(c, '')}{s}{colors['reset']}"

def badge(p):
    if not in_collection(p):
        return color(" [ext]", "dim")
    if is_uncited(p):
        return color(" [uncited]", "blue")
    return ""

def filter_collection(papers, incl=None, ext=None, uncited=None, no_uncited=None):
    if incl and ext:
        return papers
    if ext:
        return {pid: p for pid, p in papers.items() if not in_collection(p)}
    if uncited:
        return {pid: p for pid, p in papers.items() if is_uncited(p)}
    if no_uncited:
        return {pid: p for pid, p in papers.items() if in_collection(p) and not is_uncited(p)}
    if incl:
        return {pid: p for pid, p in papers.items() if in_collection(p)}
    return papers

def cmd_papers(papers, incl=False, ext=False, uncited=False, no_uncited=False):
    papers = filter_collection(papers, incl, ext, uncited, no_uncited)
    print(f"{color('ID', 'bold'):30s} {color('Year', 'bold'):6s} {color('Type', 'bold'):14s} {color('Region', 'bold'):20s} {color('Title', 'bold')}")
    print("-" * 120)
    for pid, p in sorted(papers.items()):
        region = ", ".join(p.get("region", []))
        title = p.get("title", "")[:60]
        print(f"{pid:30s}{badge(p)}  {p.get('year', ''):<6} {p.get('type', ''):14s} {region:20s} {title}")

def cmd_paper(papers, pid):
    pid = paper_id(pid)
    p = papers.get(pid)
    if not p:
        print(f"Paper '{pid}' not found.")
        return
    print(f"{color('='*60, 'cyan')}")
    print(f"{color(p['title'], 'bold')}")
    print(f"{color('='*60, 'cyan')}")
    print(f"  ID:        {pid}{badge(p)}")
    print(f"  Authors:   {', '.join(p.get('authors', []))}")
    print(f"  Year:      {p.get('year', '')}")
    print(f"  Type:      {p.get('type', '')}")
    print(f"  Region:    {', '.join(p.get('region', []))}")
    print(f"  Concepts:  {', '.join(p.get('concepts', []))}")
    print(f"  File:      {p.get('file', '')}")
    print(f"  Finding:   {p.get('key_finding', '')}")
    refs_status = p.get("refs_status", "")
    refs = p.get("references", [])
    if refs_status == "none":
        print(f"\n  {color('Cites:', 'yellow')}")
        print(f"    {color('[no references in source]', 'dim')}")
    elif refs_status == "unavailable":
        print(f"\n  {color('Cites:', 'yellow')}")
        print(f"    {color('[references unavailable]', 'dim')}")
    elif refs:
        print(f"\n  {color('Cites:', 'yellow')}")
        for r in refs:
            rp = papers.get(r)
            yr = f"({rp.get('year','?')})" if rp else ""
            print(f"    → {r} {yr}")
    cited_by = [pid2 for pid2, p2 in papers.items() if pid in p2.get("references", [])]
    if cited_by:
        print(f"\n  {color('Cited by:', 'yellow')}")
        for c in sorted(cited_by):
            cp = papers.get(c)
            yr = f"({cp.get('year','?')})" if cp else ""
            print(f"    ← {c} {yr}")
    neighbors = []
    my_concepts = set(p.get("concepts", []))
    for pid2, p2 in papers.items():
        if pid2 == pid:
            continue
        shared = my_concepts & set(p2.get("concepts", []))
        if shared:
            neighbors.append((pid2, shared))
    if neighbors:
        print(f"\n  {color('Concept neighbors (shared concepts):', 'cyan')}")
        for nid, shared in sorted(neighbors, key=lambda x: -len(x[1]))[:10]:
            np = papers.get(nid)
            yr = f"({np.get('year','?')})" if np else ""
            print(f"    ~ {nid} {yr}  [{', '.join(sorted(shared))}]")

def cmd_concepts(papers):
    internal = {pid: p for pid, p in papers.items() if in_collection(p)}
    concept_counts = defaultdict(list)
    for pid, p in internal.items():
        for c in p.get("concepts", []):
            concept_counts[c].append(pid)
    print(f"{color('Concept', 'bold'):35s} {color('Count', 'bold'):8s} {color('Papers', 'bold')}")
    print("-" * 80)
    for c in sorted(concept_counts.keys()):
        print(f"{c:35s} {len(concept_counts[c]):<8} {', '.join(sorted(concept_counts[c]))}")

def cmd_search(papers, term):
    term = term.lower()
    vocab = load_vocab()
    results = []
    for pid, p in papers.items():
        haystack = f"{pid} {p.get('title','')} {' '.join(p.get('concepts',[]))} {p.get('key_finding','')} {' '.join(p.get('authors',[]))}".lower()
        for c in p.get("concepts", []):
            if c in vocab:
                haystack += " " + vocab[c].lower()
        if term in haystack:
            results.append(pid)
    if not results:
        print(f"No matches for '{term}'.")
        return
    header = f'Search results for "{term}":'
    print(f"{color(header, 'bold')}\n")
    for pid in sorted(results):
        p = papers[pid]
        print(f"  {color(pid, 'green'):30s}{badge(p)}  ({p.get('year','?')}) {p.get('title','')[:70]}")

def cmd_list(papers, concept=None, region=None, ptype=None, incl=None, ext=None):
    papers = filter_collection(papers, incl, ext)
    results = []
    for pid, p in papers.items():
        if concept and concept not in p.get("concepts", []):
            continue
        if region and region not in p.get("region", []):
            continue
        if ptype and p.get("type") != ptype:
            continue
        results.append(pid)
    if not results:
        print("No matching papers.")
        return
    print(f"{color(f'{len(results)} papers:', 'bold')}\n")
    for pid in sorted(results):
        p = papers[pid]
        concepts = ", ".join(p.get("concepts", [])[:4])
        print(f"  {color(pid, 'green'):30s}{badge(p)}  ({p.get('year','?')})  [{concepts}{'...' if len(p.get('concepts',[]))>4 else ''}]")

def cmd_graph(papers, pid):
    pid = paper_id(pid)
    p = papers.get(pid)
    if not p:
        print(f"Paper '{pid}' not found.")
        return
    print(f"\n{color('Citation graph for:', 'bold')} {color(pid, 'green')}{badge(p)} ({p.get('year','')}) — {p.get('title','')[:60]}\n")
    refs = p.get("references", [])
    cited_by = sorted([pid2 for pid2, p2 in papers.items() if pid in p2.get("references", [])])
    my_concepts = set(p.get("concepts", []))
    neighbors = []
    for pid2, p2 in papers.items():
        if pid2 == pid:
            continue
        shared = my_concepts & set(p2.get("concepts", []))
        if shared:
            neighbors.append((pid2, shared))
    if refs:
        print(f"  {color('┌─ Cites (references)', 'yellow')}")
        for r in refs:
            rp = papers.get(r)
            line = f"  │  ← {r}"
            if rp:
                line += f" ({rp.get('year','?')}){badge(rp)}"
            print(line)
    else:
        print(f"  {color('┌─ Cites: (none filled)', 'dim')}")
    if cited_by:
        print(f"  {color('├─ Cited by', 'cyan')}")
        for c in cited_by:
            cp = papers.get(c)
            line = f"  │  → {c}"
            if cp:
                line += f" ({cp.get('year','?')}){badge(cp)}"
            print(line)
    if neighbors:
        print(f"  {color('└─ Concept neighbors (top 5)', 'magenta')}")
        for nid, shared in sorted(neighbors, key=lambda x: -len(x[1]))[:5]:
            np = papers.get(nid)
            line = f"     ~ {nid}"
            if np:
                line += f" ({np.get('year','?')})"
            line += f"  [{', '.join(sorted(shared))}]"
            print(line)

def cmd_neighbors(papers, pid):
    pid = paper_id(pid)
    p = papers.get(pid)
    if not p:
        print(f"Paper '{pid}' not found.")
        return
    my_concepts = set(p.get("concepts", []))
    neighbors = []
    for pid2, p2 in papers.items():
        if pid2 == pid:
            continue
        shared = my_concepts & set(p2.get("concepts", []))
        if shared:
            neighbors.append((pid2, shared))
    if not neighbors:
        print(f"No concept neighbors for {pid}.")
        return
    print(f"{color(f'Papers sharing concepts with {pid}:', 'bold')}\n")
    for nid, shared in sorted(neighbors, key=lambda x: -len(x[1])):
        np = papers.get(nid)
        yr = f"({np.get('year','?')})" if np else ""
        print(f"  {color(nid, 'green'):30s}{badge(np) if np else ''} {yr:12s} {', '.join(sorted(shared))}")

def cmd_missing(papers, incl=None, ext=None, uncited=None, no_uncited=None):
    papers = filter_collection(papers, incl, ext, uncited, no_uncited)
    missing = [pid for pid, p in papers.items() if not p.get("references") and not p.get("refs_status")]
    if not missing:
        print("All papers have references filled.")
        return
    print(f"{color(f'{len(missing)} papers missing references:', 'yellow')}\n")
    for pid in sorted(missing):
        p = papers[pid]
        print(f"  {pid:30s}{badge(p)}  ({p.get('year', '?')}) — {p.get('title', '')[:60]}")

def cmd_stats(papers):
    internal = {pid: p for pid, p in papers.items() if in_collection(p)}
    external = {pid: p for pid, p in papers.items() if not in_collection(p)}
    uncited_p = {pid: p for pid, p in papers.items() if is_uncited(p)}
    types = defaultdict(int)
    regions = defaultdict(int)
    concepts = defaultdict(int)
    refs_filled = 0
    refs_none = 0
    refs_unavail = 0
    for pid, p in internal.items():
        types[p.get("type", "unknown")] += 1
        for r in p.get("region", []):
            regions[r] += 1
        for c in p.get("concepts", []):
            concepts[c] += 1
        if p.get("references"):
            refs_filled += 1
        elif p.get("refs_status") == "none":
            refs_none += 1
        elif p.get("refs_status") == "unavailable":
            refs_unavail += 1
    print(f"{color('Literature Stats', 'bold')}\n")
    print(f"  In collection:  {len(internal)} ({len(internal) - len(uncited_p)} cited + {len(uncited_p)} uncited)")
    print(f"  External stubs: {len(external)}")
    print(f"  Total entries:  {len(papers)}")
    print(f"  Refs filled:    {refs_filled}/{len(internal) - refs_none - refs_unavail}")
    if refs_none:
        print(f"  No refs in source: {refs_none}")
    if refs_unavail:
        print(f"  Refs unavailable:  {refs_unavail}")
    print(f"\n  {color('By type (in-collection):', 'bold')}")
    for t, n in sorted(types.items()):
        print(f"    {t:20s} {n}")
    print(f"\n  {color('By region (in-collection):', 'bold')}")
    for r, n in sorted(regions.items(), key=lambda x: -x[1]):
        print(f"    {r:20s} {n}")
    print(f"\n  {color('Top concepts (in-collection):', 'bold')}")
    for c, n in sorted(concepts.items(), key=lambda x: -x[1])[:15]:
        print(f"    {c:35s} {n}")


def cmd_viz(papers, pid=None, collection_only=False, concept=None, output=None, collection=None):
    if output is None:
        if collection:
            output = os.path.join(LIT_DIR, f"{collection}_network.html")
        else:
            output = os.path.join(LIT_DIR, "citation_network.html")

    # filter nodes
    nodes = {}
    for pid0, p in papers.items():
        if collection_only and not in_collection(p):
            continue
        if concept and concept not in p.get("concepts", []):
            continue
        if pid and pid0 != pid:
            continue
        nodes[pid0] = p

    # if ego, include references and cited-by
    if pid and pid in papers:
        p = papers[pid]
        for r in p.get("references", []):
            if r not in nodes and r in papers:
                nodes[r] = papers[r]
        for pid2, p2 in papers.items():
            if pid in p2.get("references", []):
                if pid2 not in nodes:
                    nodes[pid2] = p2

    if not nodes:
        print("No nodes match the filter.")
        return

    # compute citation counts
    cit_count = defaultdict(int)
    cited_by_map = defaultdict(list)
    for pid0, p in papers.items():
        for r in p.get("references", []):
            cit_count[r] += 1
            cited_by_map[r].append(pid0)

    # build JSON-serializable node/edge data
    node_list = []
    concept_set = set()
    region_set = set()
    min_year, max_year = 9999, 0
    for nid, p in nodes.items():
        in_coll = in_collection(p)
        uncited_flag = is_uncited(p)
        deg = cit_count.get(nid, 0)
        size = max(10, min(50, 3 + deg * 2)) if in_coll else 8
        if uncited_flag:
            color_hex = "#00897B"
        elif in_coll:
            color_hex = "#2196F3"
        else:
            color_hex = "#B0BEC5"
        cs = p.get("concepts", [])
        if isinstance(cs, str):
            cs = [cs]
        concept_set.update(cs)
        rr = p.get("region", [])
        if isinstance(rr, str):
            rr = [rr]
        for reg in rr:
            region_set.add(reg)
        y = p.get("year")
        if y:
            try:
                yi = int(y)
                min_year = min(min_year, yi)
                max_year = max(max_year, yi)
            except:
                pass
        authors = p.get("authors", [])
        if isinstance(authors, str):
            authors = [authors]
        node_list.append({
            "id": nid,
            "label": nid,
            "size": size,
            "color": color_hex,
            "in_collection": in_coll,
            "uncited": uncited_flag,
            "title": p.get("title", ""),
            "year": y or "",
            "type": p.get("type", ""),
            "concepts": cs,
            "cit_count": deg,
            "authors": authors,
            "region": rr,
            "key_finding": p.get("key_finding", ""),
            "references": [r for r in p.get("references", [])],
            "cited_by": cited_by_map.get(nid, [])
        })

    node_ids = {n["id"] for n in node_list}
    # trim refs/cited_by to only present nodes
    for n in node_list:
        n["references"] = [r for r in n["references"] if r in node_ids]
        n["cited_by"] = [c for c in n["cited_by"] if c in node_ids]

    edge_list = []
    for sid, p in nodes.items():
        for t in p.get("references", []):
            if t in node_ids:
                edge_list.append({"from": sid, "to": t})

    all_concepts = sorted(concept_set)
    all_regions = sorted(region_set)
    min_year = 1990 if min_year == 9999 else min_year
    max_year = 2025 if max_year == 0 else max_year

    import json
    data_json = json.dumps({"nodes": node_list, "edges": edge_list,
                            "concepts": all_concepts, "regions": all_regions,
                            "minYear": min_year, "maxYear": max_year})
    # count prefixes for toggle labels
    ic_count = sum(1 for n in node_list if n["in_collection"] and not n["uncited"])
    uncited_count = sum(1 for n in node_list if n["uncited"])
    stub_count = len(node_list) - ic_count - uncited_count

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Citation Network</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/vis-network/9.1.9/standalone/umd/vis-network.min.js"></script>
<link href="https://cdnjs.cloudflare.com/ajax/libs/vis-network/9.1.9/styles/vis-network.min.css" rel="stylesheet">
<style>
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{ font-family:'Segoe UI',system-ui,sans-serif; display:flex; height:100vh; overflow:hidden; }}
#sidebar {{
  width:300px; min-width:300px; background:#f5f7fa; border-right:1px solid #cfd8dc;
  display:flex; flex-direction:column; overflow-y:auto;
}}
#sidebar h1 {{ font-size:16px; padding:16px 14px 8px; color:#37474f; }}
#sidebar .sub {{ font-size:12px; color:#78909c; padding:0 14px 12px; border-bottom:1px solid #e0e0e0; }}
.ctrl {{ padding:10px 14px; border-bottom:1px solid #eceff1; }}
.ctrl label {{ display:block; font-size:12px; font-weight:600; color:#546e7a; margin-bottom:4px; }}
.tgl {{ display:flex; align-items:center; gap:8px; margin-bottom:4px; cursor:pointer; font-size:13px; color:#37474f; }}
.tgl input {{ accent-color:#2196F3; }}
#search {{ width:100%; padding:6px 8px; border:1px solid #cfd8dc; border-radius:4px; font-size:13px; outline:none; }}
#search:focus {{ border-color:#2196F3; }}
#concept, #region {{ width:100%; padding:6px 8px; border:1px solid #cfd8dc; border-radius:4px; font-size:13px; }}
#types .type-tgl {{ display:flex; align-items:center; gap:6px; margin-bottom:2px; cursor:pointer; font-size:12px; color:#37474f; }}
#types .type-tgl input {{ accent-color:#2196F3; }}
.year-row {{ display:flex; gap:8px; align-items:center; font-size:12px; color:#546e7a; }}
.year-row input[type=range] {{ flex:1; }}
.btn-row {{ display:flex; gap:6px; padding:10px 14px; flex-wrap:wrap; }}
.btn {{
  padding:6px 12px; border:1px solid #cfd8dc; border-radius:4px; background:#fff;
  font-size:12px; cursor:pointer; color:#37474f;
}}
.btn:hover {{ background:#e3f2fd; border-color:#2196F3; }}
.btn:active {{ background:#bbdefb; }}
#stats {{ font-size:11px; color:#78909c; padding:10px 14px; margin-top:auto; border-top:1px solid #e0e0e0; }}
#network {{ flex:1; }}
#overlay {{
  display:none; position:fixed; top:0; left:0; width:100%; height:100%;
  background:rgba(0,0,0,0.35); z-index:1000; justify-content:center; align-items:center;
}}
#modal {{
  background:#fff; border-radius:8px; max-width:580px; width:90%;
  max-height:80vh; overflow-y:auto; box-shadow:0 8px 32px rgba(0,0,0,0.25);
  padding:24px 28px; font-size:13px; line-height:1.6; position:relative;
}}
#modal h2 {{ font-size:15px; color:#1565C0; margin-bottom:10px; padding-right:28px; }}
#modal .close, #modal .back {{
  position:absolute; top:12px; font-size:18px; cursor:pointer;
  color:#90a4ae; line-height:1; border:none; background:none; padding:2px 4px;
}}
#modal .close {{ right:16px; font-size:20px; }}
#modal .back {{ right:44px; }}
#modal .close:hover, #modal .back:hover {{ color:#37474f; }}
#modal .hl {{ font-weight:600; color:#546e7a; display:inline; }}
#modal .tag {{
  display:inline-block; background:#e3f2fd; color:#1565C0; padding:1px 8px;
  border-radius:10px; font-size:11px; margin:1px 3px 1px 0;
}}
#modal .section {{ margin:8px 0 4px; font-weight:600; color:#78909c; font-size:11px; text-transform:uppercase; letter-spacing:0.5px; }}
#modal .ref-link {{ cursor:pointer; color:#1565C0; }}
#modal .ref-link:hover {{ text-decoration:underline; }}
#modal .finding {{ background:#f5f7fa; padding:8px 12px; border-radius:4px; color:#455a64; font-style:italic; margin-top:4px; }}
</style>
</head>
<body>
<div id="sidebar">
  <h1>🔬 Citation Explorer</h1>
  <div class="sub">{len(node_list)} papers · {len(edge_list)} citations</div>
    <div class="ctrl">
      <label>VISIBILITY</label>
      <label class="tgl"><input type="checkbox" id="chkColl" checked onchange="filter()"><span>Cited <b>({ic_count})</b></span></label>
      <label class="tgl"><input type="checkbox" id="chkUncited" checked onchange="filter()"><span>Uncited <b>({uncited_count})</b></span></label>
      <label class="tgl"><input type="checkbox" id="chkStub" checked onchange="filter()"><span>Stubs <b>({stub_count})</b></span></label>
    </div>
  <div class="ctrl">
    <label for="search">SEARCH</label>
    <input type="text" id="search" placeholder="PID, title, author..." oninput="filter()">
  </div>
  <div class="ctrl">
    <label for="concept">CONCEPT</label>
    <select id="concept" onchange="filter()">
      <option value="">All concepts</option>
    </select>
  </div>
  <div class="ctrl">
    <label>YEAR RANGE</label>
    <div class="year-row">
      <span>From</span>
      <input type="number" id="yearLo" min="1960" max="2026" value="{min_year}" style="width:70px;padding:4px 6px;border:1px solid #cfd8dc;border-radius:4px;font-size:13px;" onchange="filter()">
      <span>To</span>
      <input type="number" id="yearHi" min="1960" max="2026" value="{max_year}" style="width:70px;padding:4px 6px;border:1px solid #cfd8dc;border-radius:4px;font-size:13px;" onchange="filter()">
    </div>
  </div>
  <div class="ctrl">
    <label for="region">REGION</label>
    <select id="region" onchange="filter()">
      <option value="">All regions</option>
    </select>
  </div>
  <div class="ctrl" id="types-ctrl">
    <label>TYPE</label>
    <div id="types"></div>
  </div>
  <div class="ctrl">
    <label>MIN CITATIONS</label>
    <input type="number" id="minCit" min="0" value="0" style="width:80px;padding:4px 6px;border:1px solid #cfd8dc;border-radius:4px;font-size:13px;" onchange="filter()">
  </div>
  <div class="btn-row">
    <button class="btn" onclick="resetView()">Reset View</button>
    <button class="btn" onclick="fitCanvas()">Fit Canvas</button>
  </div>
  <div id="stats"></div>
</div>
<div id="network"></div>
<div id="overlay">
  <div id="modal"></div>
</div>
<script>
const DATA = {data_json};
const container = document.getElementById('network');
const allNodes = new vis.DataSet(DATA.nodes);
const allEdges = new vis.DataSet(DATA.edges);
let network, selectedNodeId = null, historyStack = [], overlayOpen = false;

// populate dropdowns
const selC = document.getElementById('concept');
DATA.concepts.forEach(c => {{ const o=document.createElement('option'); o.value=c; o.textContent=c; selC.appendChild(o); }});
const selR = document.getElementById('region');
DATA.regions.forEach(r => {{ const o=document.createElement('option'); o.value=r; o.textContent=r; selR.appendChild(o); }});

// build type checkboxes with counts
const typeCounts = {{}};
DATA.nodes.forEach(n => {{ const t = n.type || 'unknown'; typeCounts[t] = (typeCounts[t] || 0) + 1; }});
const typesDiv = document.getElementById('types');
Object.keys(typeCounts).sort().forEach(t => {{
  const label = document.createElement('label');
  label.className = 'type-tgl';
  label.innerHTML = `<input type="checkbox" checked onchange="filter()"> <span>${{t}} <b>(${{typeCounts[t]}})</b></span>`;
  label.querySelector('input').dataset.type = t;
  typesDiv.appendChild(label);
}});

const options = {{
  nodes: {{ shape:'dot', font: {{ size:12, color:'#37474f' }}, borderWidth:0, borderWidthSelected:2 }},
  edges: {{
    arrows: {{ to: {{ enabled:true, scaleFactor:0.5 }} }},
    color: {{ color:'#90A4AE', opacity:0.35 }},
    smooth: {{ type:'continuous' }}
  }},
  physics: {{
    barnesHut: {{ gravitationalConstant:-8000, centralGravity:0.3, springLength:200, springConstant:0.04, damping:0.09 }},
    stabilization: {{ iterations:100 }},
    minVelocity: 0.75, solver: 'barnesHut'
  }},
  interaction: {{ tooltipDelay:200, hover:true }}
}};

network = new vis.Network(container, {{ nodes:allNodes, edges:allEdges }}, options);

function renderModal(id) {{
  selectedNodeId = id;
  const n = DATA.nodes.find(x => x.id === id);
  if (!n) return;
  const modal = document.getElementById('modal');
  const refsHtml = n.references.length
    ? n.references.map(r => `<span class="ref-link" onclick="goToNode('${{r}}')">${{r}}</span>`).join(', ')
    : '<span style="color:#b0bec5">none</span>';
  const citedHtml = n.cited_by.length
    ? n.cited_by.map(c => `<span class="ref-link" onclick="goToNode('${{c}}')">${{c}}</span>`).join(', ')
    : '<span style="color:#b0bec5">none</span>';
  const tags = n.concepts.map(c => `<span class="tag">${{c}}</span>`).join('');
  const authors = n.authors.length ? n.authors.join(', ') : '<span style="color:#b0bec5">—</span>';
  const region = n.region.length ? n.region.join(', ') : '<span style="color:#b0bec5">—</span>';
  const finding = n.key_finding ? `<div class="finding">${{n.key_finding}}</div>` : '';
  const backBtn = historyStack.length
    ? `<button class="back" onclick="goBack()">←</button>`
    : '';
  modal.innerHTML = `
    ${{backBtn}}
    <button class="close" onclick="hideModal()">✕</button>
    <h2>${{n.id}}</h2>
    <div><span class="hl">Title:</span> ${{n.title || '—'}}</div>
    <div><span class="hl">Authors:</span> ${{authors}}</div>
    <div><span class="hl">Year:</span> ${{n.year}} &nbsp;|&nbsp; <span class="hl">Type:</span> ${{n.type || '—'}} &nbsp;|&nbsp; <span class="hl">Region:</span> ${{region}}</div>
    <div><span class="hl">Cited by:</span> ${{n.cit_count}} paper(s)</div>
    <div class="section">Concepts</div>
    <div>${{tags || '<span style="color:#b0bec5">—</span>'}}</div>
    <div class="section">References (${{n.references.length}})</div>
    <div>${{refsHtml}}</div>
    <div class="section">Cited by (${{n.cited_by.length}})</div>
    <div>${{citedHtml}}</div>
    ${{finding}}
  `;
  document.getElementById('overlay').style.display = 'flex';
  overlayOpen = true;
}}

function showModal(id) {{
  if (selectedNodeId && selectedNodeId !== id) {{
    historyStack.push(selectedNodeId);
  }}
  renderModal(id);
}}

function goToNode(id) {{
  network.selectNodes([id]);
  showModal(id);
  network.focus(id, {{ scale:1.5, animation:true }});
}}

function goBack() {{
  if (historyStack.length) {{
    const id = historyStack.pop();
    renderModal(id);
    network.selectNodes([id]);
    network.focus(id, {{ scale:1.5, animation:true }});
  }}
}}

function hideModal() {{
  document.getElementById('overlay').style.display = 'none';
  network.selectNodes([]);
  selectedNodeId = null;
  historyStack = [];
  overlayOpen = false;
}}

network.on('click', function(params) {{
  if (overlayOpen) return;
  if (params.nodes.length) {{
    showModal(params.nodes[0]);
  }}
}});

document.addEventListener('keydown', function(e) {{ if (e.key === 'Escape' && overlayOpen) hideModal(); }});

function filter() {{
  const showColl = document.getElementById('chkColl').checked;
  const showUncited = document.getElementById('chkUncited').checked;
  const showStub = document.getElementById('chkStub').checked;
  const q = document.getElementById('search').value.toLowerCase().trim();
  const concept = document.getElementById('concept').value;
  const region = document.getElementById('region').value;
  const yrLo = parseInt(document.getElementById('yearLo').value);
  const yrHi = parseInt(document.getElementById('yearHi').value);
  const minCit = parseInt(document.getElementById('minCit').value) || 0;
  const activeTypes = new Set();
  document.querySelectorAll('#types input[type=checkbox]').forEach(cb => {{
    if (cb.checked) activeTypes.add(cb.dataset.type);
  }});

  const idsToShow = new Set();
  DATA.nodes.forEach(n => {{
    if (n.uncited) {{
      if (!showUncited) return;
    }} else if (n.in_collection) {{
      if (!showColl) return;
    }} else {{
      if (!showStub) return;
    }}
    if (q) {{
      const haystack = (n.id+' '+n.title+' '+n.concepts.join(' ')+' '+n.authors.join(' ')).toLowerCase();
      if (!haystack.includes(q)) return;
    }}
    if (concept && !n.concepts.includes(concept)) return;
    if (region && !n.region.includes(region)) return;
    const t = n.type || 'unknown';
    if (!activeTypes.has(t)) return;
    if (n.cit_count < minCit) return;
    const y = parseInt(n.year) || 0;
    if (y && (y < yrLo || y > yrHi)) return;
    idsToShow.add(n.id);
  }});

  // highlight matched, dim others; hide unmatched
  const updates = [];
  DATA.nodes.forEach(n => {{
    const vis = idsToShow.has(n.id);
    let color = n.color;
    if (vis && q) {{
      if (n.uncited) color = '#00695C'; else if (n.in_collection) color = '#1565C0'; else color = '#78909C';
    }} else if (!vis) {{
      color = '#f0f0f0'; // nearly invisible
    }}
    updates.push({{ id: n.id, color: color, hidden: !vis }});
  }});
  allNodes.update(updates);

  // update edges visibility
  const edgeUpdates = [];
  DATA.edges.forEach(e => {{
    edgeUpdates.push({{ id: e.from+'→'+e.to, hidden: !(idsToShow.has(e.from) && idsToShow.has(e.to)) }});
  }});
  allEdges.update(edgeUpdates);

  document.getElementById('stats').textContent = `Showing ${{idsToShow.size}} / ${{DATA.nodes.length}} papers, ${{DATA.edges.filter(e => idsToShow.has(e.from) && idsToShow.has(e.to)).length}} edges`;
}}

function resetView() {{
  document.getElementById('search').value = '';
  document.getElementById('concept').value = '';
  document.getElementById('region').value = '';
  document.getElementById('minCit').value = 0;
  document.getElementById('chkColl').checked = true;
  document.getElementById('chkUncited').checked = true;
  document.getElementById('chkStub').checked = true;
  document.getElementById('yearLo').value = DATA.minYear;
  document.getElementById('yearHi').value = DATA.maxYear;
  document.querySelectorAll('#types input[type=checkbox]').forEach(cb => cb.checked = true);
  filter();
}}

function fitCanvas() {{ network.fit({{ animation:true }}); }}

// year range sync
document.getElementById('yearLo').addEventListener('change', function() {{
  const hi = document.getElementById('yearHi');
  if (parseInt(this.value) > parseInt(hi.value)) hi.value = this.value;
  filter();
}});
document.getElementById('yearHi').addEventListener('change', function() {{
  const lo = document.getElementById('yearLo');
  if (parseInt(this.value) < parseInt(lo.value)) lo.value = this.value;
  filter();
}});

// initial edge ids
DATA.edges.forEach(e => {{ e.id = e.from+'→'+e.to; }});

// initial filter
filter();
</script>
</body>
</html>"""

    with open(output, "w") as f:
        f.write(html)
    print(f"Saved citation network: {output}")


def main():
    # extract --collection=NAME before dispatching
    collection = None
    for i, arg in enumerate(sys.argv):
        if arg.startswith("--collection="):
            collection = arg.split("=", 1)[1]
            del sys.argv[i]
            break

    if collection and collection not in COLLECTIONS:
        print(f"Unknown collection '{collection}'. Available: {', '.join(COLLECTIONS)}")
        sys.exit(1)

    papers = load(collection)
    if not papers:
        print("No papers found. Run 'lit rebuild' or check .meta.yaml files.")
        sys.exit(1)
    if len(sys.argv) < 2:
        print(__doc__)
        return
    cmd = sys.argv[1]
    if cmd == "viz":
        args = sys.argv[2:]
        kwargs = {"output": None, "pid": None, "collection_only": False, "concept": None}
        for a in args:
            if a == "--in-collection":
                kwargs["collection_only"] = True
            elif a.startswith("--pid="):
                kwargs["pid"] = a.split("=", 1)[1]
            elif a.startswith("--concept="):
                kwargs["concept"] = a.split("=", 1)[1]
            elif a.startswith("--output="):
                kwargs["output"] = a.split("=", 1)[1]
        cmd_viz(papers, **kwargs, collection=collection)
    elif cmd == "papers":
        args = sys.argv[2:]
        incl = "--in-collection" in args
        ext = "--external" in args
        uncited = "--uncited" in args
        no_uncited = "--no-uncited" in args
        cmd_papers(papers, incl, ext, uncited, no_uncited)
    elif cmd == "paper" and len(sys.argv) > 2:
        cmd_paper(papers, sys.argv[2])
    elif cmd == "concepts":
        cmd_concepts(papers)
    elif cmd == "search" and len(sys.argv) > 2:
        cmd_search(papers, " ".join(sys.argv[2:]))
    elif cmd == "list":
        kwargs = {}
        for i, arg in enumerate(sys.argv[2:]):
            if arg == "--concept" and i+1 < len(sys.argv[2:]):
                kwargs["concept"] = sys.argv[2:][i+1]
            elif arg == "--region" and i+1 < len(sys.argv[2:]):
                kwargs["region"] = sys.argv[2:][i+1]
            elif arg == "--type" and i+1 < len(sys.argv[2:]):
                kwargs["ptype"] = sys.argv[2:][i+1]
            elif arg == "--in-collection":
                kwargs["incl"] = True
            elif arg == "--external":
                kwargs["ext"] = True
        cmd_list(papers, **kwargs)
    elif cmd == "graph" and len(sys.argv) > 2:
        cmd_graph(papers, sys.argv[2])
    elif cmd == "neighbors" and len(sys.argv) > 2:
        cmd_neighbors(papers, sys.argv[2])
    elif cmd == "missing":
        args = sys.argv[2:]
        incl = "--in-collection" in args
        ext = "--external" in args
        uncited = "--uncited" in args
        no_uncited = "--no-uncited" in args
        cmd_missing(papers, incl, ext, uncited, no_uncited)
    elif cmd == "stats":
        cmd_stats(papers)
    else:
        print(__doc__)

if __name__ == "__main__":
    main()
