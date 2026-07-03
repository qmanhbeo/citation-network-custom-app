# AGENTS.md — citation-network

Multi-collection bibliographic knowledge graph. Currently one collection:
**EnergyBurden** (38 in-collection papers + 1,953 stubs).

---

## PID Convention (critical — be consistent)

PIDs are the primary key across collections. Every entity must follow these rules.

### Pattern

| Authors | Pattern | Example |
|---|---|---|
| 1 | `LastName+Initials_Year` | `BoardmanB_1991` |
| 2 | `LastName1+Initials1_LastName2+Initials2_Year` | `LiddellC_MorrisC_2010` |
| 3+ | `LastName1+Initials1_etal_Year` | `DrehoblA_etal_2020` |
| Institutional | `ABBREV_Year` | `DOE_2014`, `WHO_2007` |

### Rules

- **First-name initials**: take ALL given-name initials (tighter dedup).
  - `SmithJR` for "John Robert Smith", not `SmithJ`.
- **Hyphenated last names**: join parts.
  - `SmithJonesJ` for "Alice Smith-Jones".
- **Multi-word last names**: camelCase join.
  - `daVinciL` for "Leonardo da Vinci".
  - `vanderWaalsJ` for "Jan van der Waals".
- **Apostrophes**: strip.
  - `OBrienJ` for "O'Brien".
  - `DAmatoM` for "D'Amato".
- **Diacritics**: strip to ASCII.
  - `MendezR` for "Méndez".
- **Same-year dupes**: suffix `a`, `b`, `c`…
  - `WilkinsonP_etal_2007a`, `WilkinsonP_etal_2007b`.
- **No date**: `_ND`.
  - `PalmerG_ND`.
- **Institutional**: use the standard abbreviation, not full name.
  - `WHO_2007`, `CensusBureau_2019`, not `WorldHealthOrganization_2007`.
- **Collision detection**: if a generated PID already exists for a *different* paper (not same-year-dup), append a suffix just like dupes.
- **Filename must match PID exactly**: `{PID}.meta.yaml`.

### Examples

| Authors | Year | PID |
|---|---|---|
| Boardman, B. | 1991 | `BoardmanB_1991` |
| Liddell, C., Morris, C. | 2010 | `LiddellC_MorrisC_2010` |
| Drehobl, A., Ross, L., Ayala, R. | 2020 | `DrehoblA_etal_2020` |
| U.S. Dept. of Energy | 2014 | `DOE_2014` |
| Centers for Disease Control | 2013 | `CDC_2013` |
| World Health Organization | 2007 | `WHO_2007` |

---

## Directory layout

```
~/citation-network/
├── lit.py                     # CLI tool
├── AGENTS.md
├── citation_network.html      # all-collections viz
├── checklist.md
├── checklist_bibliography.md
├── {CollectionName}/           # cited in-collection papers
│   ├── PID.meta.yaml
│   ├── PID.pdf
│   └── vocabulary.yaml         # per-collection concept vocab
├── {CollectionName}_uncited/   # uncited in-collection papers
│   └── PID.meta.yaml
└── {CollectionName}_stubs/     # external references
    └── PID.meta.yaml
```

**Current collections:** `EnergyBurden`.

### Adding a new collection

1. Register in `lit.py`: `register_collection("Name", "DirName")`
2. Create `DirName/`, `DirName_uncited/`, `DirName_stubs/`
3. Create `DirName/vocabulary.yaml` (or leave empty)
4. Place paper meta files in the appropriate subdirectory

---

## Meta file fields

| Field | Required | Notes |
|---|---|---|
| `pid` | yes | Auto-derived from authors + year (see above) |
| `in_collection` | yes | `true` for collection papers, `false` for stubs |
| `title` | yes | |
| `authors` | yes | List of strings |
| `year` | yes | Use `~` (null) for unknown |
| `type` | no | article, report, book, legislation, dataset, webpage… |
| `region` | no | List of region tags |
| `concepts` | no | List of concept tags (should align with vocabulary.yaml) |
| `references` | no | List of PID strings this paper cites |
| `refs_status` | no | `none` (no bibliography in source), `unavailable` (has refs, no PDF) |
| `key_finding` | no | One-sentence summary |
| `file` | no | PDF filename (just the basename) |

---

## CLI reference

```bash
lit stats                           # summary across all collections
lit stats --collection=EnergyBurden # single collection

lit missing                              # papers missing refs
lit missing --in-collection              # only in-collection papers
lit missing --collection=EnergyBurden

lit paper <PID>                     # paper details + refs + citations

lit graph <PID>                     # citation neighbors

lit papers                          # list all papers
lit papers --in-collection
lit papers --external

lit search <term>                   # search titles, concepts, findings

lit list --concept=energy_poverty   # filter by concept/region/type

lit concepts                        # all concepts with counts

lit viz                             # generate vis.js HTML (all collections)
lit viz --collection=EnergyBurden   # generates EnergyBurden_network.html
lit viz --pid=DrehoblA_etal_2020    # ego network
```

---

## Key behaviors

- **Load order**: stubs → uncited → cited *(later overrides earlier on PID collision)*
- **`--collection=NAME`** can appear anywhere in argv: `lit --collection=EB stats` or `lit stats --collection=EB`
- **Vocabulary is per-collection** at `{Collection}/vocabulary.yaml`
- **`refs_status`** distinguishes deliberate absence (`none`, `unavailable`) from unprocessed (no field)
- **Viz colors**: cited=blue, uncited=teal, stubs=gray

---

## Adding a paper's references

1. Read the paper's meta from `{Collection}/<PID>.meta.yaml`
2. For each reference, generate a PID per convention
3. Check `{Collection}_stubs/` and `{Collection}/` for existing entries
4. Create new stub `{Collection}_stubs/<PID>.meta.yaml` (bare minimum fields)
5. Write PID list into the paper's `references: []` field
6. Verify with `lit paper <PID>` and `lit missing --in-collection`

---

## Portability

`lit.py` uses `os.path.dirname(__file__)` for all paths — move the whole
`citation-network/` directory anywhere. Viz loads vis.js from CDN. Only
system dependency is `PyYAML` (`pip install pyyaml`).
