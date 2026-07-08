Ecological Informatics 94 (2026) 103669
Contents lists available at ScienceDirect
Ecological Informatics
journal homepage: www.elsevier.com/locate/ecolinf
AI-assisted multi-target classification for research-policy alignment in
conservation science
Chris McCarthya,*, Cassandra Brooksb,c, Troy Sternbergd,e, Kyle Shaneya,f, Buho Hoshinog
aAmerican Association for the Advancement of Science (AAAS) Science & Technology Policy Fellow (STPF), Washington, DC 20005, USA
bDepartment of Environmental Studies, University of Colorado Boulder, Boulder, CO 80303, USA
cInstitute of Arctic and Alpine Research, University of Colorado Boulder, Boulder, CO 80303, USA
dSchool of Geography, University of Oxford, Oxford OX2 6HY, UK
eCEI Centre for International Studies ISCTE – University Institute Lisbon, Avenida das Forças Armadas, 1649 Lisbon, Portugal
fDepartment of Biology, Health, and the Environment, The University of Texas at San Antonio, San Antonio, TX 78249, USA
gLab of Environmental Remote Sensing, Department of Environmental Sciences, College of Agriculture, Food and Environment Sciences, Rakuno Gakuen University,
Hokkaido 069-8501, Japan
A R T I C L E I N F O A B S T R A C T
Keywords: Scientific research underpins effective conservation policy, yet current approaches for assessing whether sci-
Artificial intelligence entific outputs meaningfully support defined management objectives rely primarily on manual expert review.
Automated classification This limitation constrains scalability, is time intensive and introduces potential bias in identifying knowledge
Conservation science
gaps. We present a framework combining AI-assisted multi-target classification with systematic coverage analysis
Evidence-based management
for automated evaluation of research alignment with conservation objectives. We compare traditional machine
Multi-target learning
learning (TF-IDF +logistic regression), a generic BERT baseline, and an enhanced SciBERT approach incorpo-
Natural language processing
Research coverage analysis rating domain-specific adaptations including multi-target architecture, balanced loss functions, and target
SciBERT weighting optimized for conservation science. The framework classifies research topics and conservation
objective alignment, two dimensions requiring comprehension of scientific content and policy implications. We
demonstrate the approach using 295 expert-annotated peer-reviewed studies from the Ross Sea region Marine
Protected Area in Antarctica. Our enhanced multi-target SciBERT model achieved 70.0% macro F1, out-
performing TF-IDF (59.5%) and BERT (52.0%) baselines, with per-target improvements of 21% on research
topics and 14.5% on conservation objectives. The framework achieved 78% agreement with expert annotations,
with particularly strong performance on conservation objective alignment (87.7% F1, 94% agreement). The
integrated system successfully identified and quantified descriptive patterns in research coverage across thematic
and policy dimensions, enabling systematic assessment for research prioritization and automated coverage
analysis. While demonstrated in the Antarctic context, the framework architecture is broadly transferable,
though successful adaptation requires retraining with domain-specific expert annotations and fine-tuning to
match local management frameworks.
1. Introduction (Sabo et al., 2024). This disconnect, often termed the “knowledge-
–action” or “science–policy” gap, limits the impact of conservation in-
Conservation science increasingly grapples with the challenge of vestments, hampers adaptive management, and contributes to
translating growing volumes of research into real-world outcomes. inefficiencies in research funding and planning (Cook et al., 2013; Cvi-
Despite widespread recognition that evidence-based decision-making is tanovic et al., 2016; Toomey et al., 2017). While open-access publishing
critical to addressing biodiversity loss, climate adaptation, and sus- and data-sharing initiatives have expanded the availability of scientific
tainability goals (Lemos et al., 2018; Sutherland et al., 2004), the link knowledge (Piwowar et al., 2018), accessibility alone does not ensure
between scientific knowledge and conservation policy remains weak that research outputs meaningfully support defined management
* Corresponding author.
E-mail addresses: cmccar27@jh.edu(C. McCarthy), cassandra.brooks@colorado.edu(C. Brooks), troy.sternberg@geog.ox.ac.uk(T. Sternberg), kjshaney@gmail.
com(K. Shaney), aosier@rakuno.ac.jp(B. Hoshino).
https://doi.org/10.1016/j.ecoinf.2026.103669
Received 6 August 2025; Received in revised form 17 February 2026; Accepted 18 February 2026
Available online 19 February 2026
1574-9541/© 2026 The Authors. Published by Elsevier B.V. This is an open access article under the CC BY license ( http://creativecommons.org/licenses/by/4.0/) .

C. McCarthy et al. E c o l o g i c a l I n f o r m a t i c s 94 (2026) 103669
objectives. What is needed are scalable systems that can systematically The Ross Sea region Marine Protected Area (RSRMPA) provides an
evaluate whether scientific outputs align with conservation goals and ideal demonstration case due to its well-defined conservation structure
provide automated tools for systematic research coverage assessment. consisting of clearly articulated conservation objectives, structured
Marine Protected Areas (MPAs) offer an instructive lens for management zones, and substantial research corpus that enables
addressing this challenge. Although global MPA coverage has grown comprehensive validation of automated classification approaches. As
rapidly (UNEP-WCMC, IUCN, 2021), many remain “paper parks” lack- the world's largest MPA, covering approximately 2 million km2 (Marine
ing the scientific insight required to monitor performance or guide Conservation Institute, 2024) and established in 2016 under the Com-
adaptive management (Gill et al., 2017; Jones et al., 2018; Pike et al., mission for the Conservation of Antarctic Marine Living Resources
2024). Ensuring that research activities align with conservation objec- (CCAMLR), the RSRMPA incorporates a zone-based management
tives and monitoring priorities is critical for MPA effectiveness, yet framework with three distinct management zones (General Protection
synthesizing whether existing studies support these priorities remains Zone, Special Research Zone, and Krill Research Zone) and eleven spe-
time-consuming, inconsistent, and largely manual. Traditional biblio- cific conservation objectives outlined in CCAMLR Conservation Measure
metric approaches focus primarily on citation patterns and publication 91–05 (CCAMLR, 2016). This well-defined conservation structure, with
metrics rather than content alignment with specific conservation goals explicit policy frameworks, geographic boundaries, and conservation
(Aria and Cuccurullo, 2017). Manual expert review, while thorough, targets, combined with the availability of expert-curated research
cannot scale to assess the rapidly growing volume of scientific literature datasets, provides the classification targets necessary to validate auto-
or provide consistent, unbiased evaluation across research domains and mated assessment approaches. These objectives include protecting
management contexts. ecological structure and function, maintaining reference areas for
Recent advances in artificial intelligence, particularly natural lan- monitoring natural variability, and preserving important habitats for
guage processing (NLP), offer promising solutions for automated sci- key species. We trained and validated our approach using a dataset of
entific literature analysis. Transformer-based language models, such as 295 expertly annotated studies compiled by Brooks & Ainley (Brooks
BERT and its domain-specific variants, have demonstrated strong ca- and Ainley, 2022), achieved robust multi-target classification perfor-
pabilities in understanding scientific text and performing complex mance, and applied the framework to demonstrate systematic coverage
classification tasks (Rogers et al., 2020). SciBERT, specifically pre- assessment capabilities.
trained on scientific literature, has shown superior performance in Our approach directly responds to the unique challenges that con-
biomedical and scientific text classification compared to general- servation domains present for automated text analysis. While the vol-
purpose models (Beltagy et al., 2019). However, most applications ume of relevant literature varies across conservation contexts, the need
focus on single-target classification tasks, while comprehensive research for expert annotation across multiple dimensions, including thematic
assessment requires simultaneous evaluation across multiple di- content and policy alignment, makes comprehensive manual classifi-
mensions including research topics, policy alignment, geographic scope, cation resource-intensive at any scale. Expert reviewers must possess
and methodological approaches (Chalkidis et al., 2020). Furthermore, deep domain knowledge to accurately assess research alignment with
robust, scalable automated approaches to identify research coverage specific conservation objectives and thematic priorities. This assessment
gaps and inform strategic planning are still lacking (Westgate et al., process typically requires considerable time and effort per paper when
2015). evaluating multiple classification dimensions. These demands create
Multi-target learning approaches, where models simultaneously significant bottlenecks for grant program managers evaluating research
predict multiple related outcomes, have shown promise in various do- portfolios, funding agencies assessing proposal alignment with prior-
mains by leveraging shared representations and improving classification ities, conservation organizations conducting literature reviews, and
performance (Ruder, 2017; Zhang and Yang, 2017). In the context of policy makers requiring evidence synthesis for decision-making, a
scientific literature analysis, such approaches could enable compre- challenge increasingly recognized in recent literature (Gil-Clavel and
hensive assessment of research alignment across multiple conservation Filatova, 2023; Kopperud et al., 2022). The resource intensity limits the
dimensions simultaneously while reducing computational requirements scope and frequency of comprehensive research assessments, often
compared to separate single-target models. The challenge extends resulting in ad hoc rather than structured evaluation of research
beyond classification to systematic assessment of research coverage coverage and gaps.
patterns and evaluation of how research portfolios align with existing By combining advanced NLP techniques with research coverage
conservation priorities. This requires frameworks that can systemati- assessment within a scalable AI framework, this study provides a
cally analyze research distribution across comprehensive literature transferable solution for evidence-based research assessment. The
corpora to assess coverage patterns across defined conservation prior- framework's ability to assess thematic content and policy alignment
ities, ultimately enabling evidence-based research prioritization and makes it particularly valuable for protected area management, where
resource allocation. research must support diverse conservation objectives across defined
This study addresses these challenges by introducing an AI-assisted spatial boundaries. While demonstrated using CCAMLR's conservation
framework that combines enhanced multi-target SciBERT classifica- framework, the multi-target architecture applies broadly to diverse
tion with research coverage assessment for evaluating research align- conservation contexts requiring simultaneous assessment across multi-
ment with conservation objectives. The enhanced SciBERT architecture ple dimensions, including terrestrial protected areas, marine conserva-
incorporates domain-specific adaptations including multi-target archi- tion networks, and ecosystem-based management initiatives globally.
tecture, balanced loss functions, and target weighting optimized for
conservation science. Through a unified model that leverages shared 2. Methodology
representations, the system classifies research topics and conservation
objective alignment, two dimensions that require comprehension of 2.1. Study area and dataset
scientific content and policy implications. While geographic dimensions
(management zones and monitoring areas) were initially evaluated, This study focuses on the Ross Sea region Marine Protected Area
these proved to be information extraction tasks rather than classification (RSRMPA) in Antarctica, located between approximately 67◦S to 78◦S
challenges requiring content understanding. The framework enables and 160◦E to 160◦W (spanning the International Date Line) (Fig. 1).
comprehensive evaluation across thematic and policy dimensions while Established in 2016 under CCAMLR Conservation Measure 91–05, the
revealing research coverage patterns and imbalances. The integrated RSRMPA covers approximately 2 million km2 of the Southern Ocean
framework enables systematic research assessment at scale, addressing when including areas beneath the Ross Ice Shelf, making it the world's
the limitations of traditional manual review approaches. largest MPA (Marine Conservation Institute, 2024). The area is
2

C. McCarthy et al. E c o l o g i c a l I n f o r m a t i c s 94 (2026) 103669
Fig. 1. Ross sea region marine protected area study region. Map showing the RSRMPA boundaries and management zones that comprise the conservation framework
from which our research dataset was derived.
delineated into three primary management zones: the General Protec- and monitoring areas (geographic entity recognition) to be information
tion Zone (GPZ), Special Research Zone (SRZ), and Krill Research Zone extraction rather than classification tasks. Therefore, our model ad-
(KRZ), each with specific regulations governing activities such as fishing dresses the two targets requiring content understanding, detailed in
and scientific research. Table 1, with the complete research topics from the RSRMPA Research
To ensure comprehensive coverage and policy relevance, we utilized and Monitoring Plan detailed in Supplementary Table S1 and the full list
the expert-curated dataset compiled by Brooks and Ainley (2022), of CCAMLR conservation objectives provided in Supplementary
consisting of 295 peer-reviewed articles published between 2010 and Table S2.
2021. While 295 papers may seem modest by general ML standards, this
represents a substantial portion of Ross Sea research literature and re-
flects the reality of specialized conservation domains where expert 2.2. Multi-target SciBERT architecture
annotation is resource-intensive. This dataset reflects a systematic
collection of research relevant to the RSRMPA and its conservation and 2.2.1. Foundation model
monitoring priorities. Each paper was manually annotated by domain We compare two approaches to demonstrate the combined value of
experts with comprehensive labels including research and monitoring domain-specific pretraining and architectural innovations. The baseline
topics (1–38 based on the RSRMPA Research and Monitoring Plan; model consists of standard BERT-base with simple multi-label classifi-
(Dunn et al., 2017)), CCAMLR conservation objectives (I-XI; (CCAMLR, cation heads using binary cross-entropy loss. The enhanced model em-
2016)), management zones (GPZ, SRZ, KRZ), and monitoring areas. All ploys SciBERT (Beltagy et al., 2019) with architectural adaptations
included studies fall within CCAMLR Statistical Subareas 88.1 and 88.2 including: (1) multi-target architecture with shared projection layer, (2)
(the Ross Sea management unit). We initially evaluated all four anno- focal loss with class-specific weights, (3) label smoothing regularization,
tation types but found management zones (94% single-class dominance) and (4) optimized target weighting. This comparison isolates the com-
bined contribution of domain-specific pretraining (SciBERT's scientific
Table 1
Multi-target classification schema. Details of the two classification targets addressed by the enhanced multi-target SciBERT framework, both requiring content un-
derstanding. Class distribution metrics reveal extreme imbalance ratios (comparing most frequent to least frequent class within each target).
Target Classes Classes Class Imbalance Pattern Description Examples
Total Present
45:1 imbalance ratio, Semantic classification of research focus Bioregionalization and biodiversity mapping, Physical and
Research 38 27 59% of classes in <15 areas from RSRMPA Research and biological habitat changes, Functional ecology processes,
Topics
papers Monitoring Plan Krill population dynamics
30:1 imbalance ratio, Policy alignment classification based on Conserve natural ecological structure, Promote research,
CCAMLR
11 9 Dominant: “promote conservation objectives in CCAMLR Large scale ecosystem processes, Key top predator foraging
Objectives
research” Conservation Measure 91–05 distributions
3

C. McCarthy et al. E c o l o g i c a l I n f o r m a t i c s 94 (2026) 103669
corpus) and architectural enhancements designed for imbalanced multi- focus, abstracts summarize methods, findings, and study locations,
target classification, representing our complete methodological contri- while keywords explicitly identify key species, geographic areas, and
bution rather than isolating individual components. research themes. This metadata-based approach also offers practical
advantages for real-world deployment, as title, abstract, and keywords
2.2.2. Multi-target learning framework are readily available from research databases, grant proposals, and
The Multi-Target SciBERT architecture consists of three main com- systematic review workflows, making the model immediately applicable
ponents: (1) the pre-trained SciBERT base model for feature extraction, for research assessment tasks without requiring access to full
(2) a shared projection layer (768 → 256 dimensions) for learning manuscripts.
common representations across targets, and (3) target-specific classifi- The concatenated text was tokenized using SciBERT's tokenizer with
cation heads for each prediction task. The shared projection layer en- a maximum sequence length of 512 tokens. We extended the tokenizer
ables the model to learn representations that benefit all classification vocabulary with a small set of Antarctic-specific terms (e.g., “dis-
targets while reducing computational complexity compared to separate sostichus-mawsoni”, “euphausia-superba”, “ross-sea-polynya”) to
single-target models. Target-specific classification heads consist of two- reduce tokenization of domain-specific compound terms. For new paper
layer feedforward networks with ReLU (Rectified Linear Unit) activation classification, the same input format should ideally be maintained,
and dropout regularization, allowing simultaneous prediction across which our implementation supports through automated extraction of
both tasks while leveraging shared semantic understanding of research these fields from PDF documents or structured metadata. This standard
content. Fig. 2illustrates the complete enhanced multi-target SciBERT approach for document classification leverages SciBERT's pre-training
architecture. on scientific literature while working within real-world data constraints.
2.2.3. Classification targets and schema 2.3. Training strategy and optimization
Our framework addresses two classification targets that require un-
derstanding of scientific content and policy implications (Table 1). 2.3.1. Data splitting and cross-validation
Research topics (38 total, 27 present in dataset) provide classification of The dataset was partitioned using iterative stratification to maintain
research focus areas, including bioregionalization and biodiversity label distribution across all targets, with 70% for training, 15% for
mapping, physical and biological habitat changes, functional ecology validation, and 15% for testing. The final data splits consisted of 204
processes, and krill population dynamics. CCAMLR objectives (11 total, papers for training, 43 papers for validation, and 48 papers for testing.
9 present in dataset) provide policy alignment classification based on the Based on preliminary experiments with multiple configurations, we
conservation objectives outlined in CCAMLR Conservation Measure selected a configuration optimized for the two content understanding
91–05 and require inference of how research contributes to specific targets. This configuration uses differentiated target weights (topics:
conservation goals. 3.0, objectives: 2.5) to balance the complexity difference between
research topic classification and policy alignment, combined with
2.2.4. Text processing gradient accumulation for effective batch size of 30, and label smooth-
Input texts for each paper consisted of concatenated title, abstract, ing (0.08) for regularization.
and keywords from the Brooks and Ainley (2022) dataset. While this
constraint limits access to methodological details that may appear only 2.3.2. Final model training
in full text, this approach was necessitated by the available data, as the For the final model reported in this paper, we employed an enhanced
expert-curated dataset contained only these metadata fields rather than training strategy to maximize data utilization. Following cross-
full text. Despite this constraint, these fields provide high information validation for configuration selection, we combined the training and
density for classification purposes: titles capture the primary research validation sets (247 papers total) and trained for 34 epochs using the
Fig. 2. Enhanced multi-target SciBERT architecture. Schematic diagram showing the workflow from paper metadata (title, abstract, keywords) through the SciBERT
base model (110 M parameters) to multi-target predictions. The architecture employs a shared projection layer (768 → 256 dimensions) that learns common rep-
resentations across both targets, followed by target-specific classification heads for research topics (27 classes) and CCAMLR objectives (9 classes). The configuration
uses differentiated target weights (topics: 3.0, objectives: 2.5) with multi-rate optimization using differential learning rates for the base model (5e-6) and classifi-
cation heads (1.2e-4).
4

C. McCarthy et al. E c o l o g i c a l I n f o r m a t i c s 94 (2026) 103669
optimized configuration. This approach maximizes the use of available prediction quality. Final performance is reported on the held-out test
annotated data while the held-out test set (48 papers) provides unbiased set of 48 papers.
performance evaluation. To ensure robust performance estimates and
enable statistical analysis, we trained an ensemble of five models with 2.4.2. Decision thresholds
different random seeds (42, 123, 456, 789, 321). We report the perfor- Classification thresholds were tuned on the validation split (43 pa-
mance of the ensemble using majority voting (3/5 agreement required pers) before any final training or test-set evaluation. A single shared
for positive classification). threshold of 0.42, applied to both research topics and conservation ob-
jectives, was selected to maximize macro F1. A shared value was
2.3.3. Multi-target loss function and class balancing adopted because both targets use the same sigmoid output range and
The framework employs Focal Loss (Lin et al., 2017) enhanced with because per-target tuning on a 43-paper validation set risks overfitting
class-specific weights and label smoothing to address severe label to split-specific label noise. After threshold selection, the model was
imbalance across targets. Class weights were calculated as the inverse retrained on the combined training +validation set (247 papers) for 34
frequency of each class in the training set. The multi-target loss com- epochs. The fixed 0.42 threshold was then held constant across all five
bines weighted focal losses across both targets, with target-specific ensemble models during evaluation on the held-out test set (48 papers),
weights (w_target) applied to balance task complexity, label smooth- ensuring no information leakage from test data into any model selection
ing (α =0.08) for regularization, and gradient accumulation for stable or calibration decision. For the TF-IDF baseline, a default threshold of
training. This approach effectively handles the extreme class imbalance 0.5 was applied to all targets.
while maintaining focus on research topic and conservation objective
classification. Multi-rate optimization employed different learning rates 2.4.3. Agreement with expert annotations
for the pre-trained base model (5e-6) versus classification heads (1.2e- We conducted post-hoc expert validation using our test set of 48
4), determined through validation set tuning following standard prac- papers containing both expert-assigned labels (from the Brooks & Ainley
tices for transformer fine-tuning, to prevent catastrophic forgetting dataset) and model predictions. This approach treats the original dataset
while enabling task-specific adaptation. annotations as single-expert ground truth, comparing model predictions
against expert classifications using Jaccard similarity for multi-label
2.3.4. Training implementation tasks.
All model development and training was conducted using Google Throughout the evaluation, overall scores are reported as weighted
Colab with NVIDIA A100 GPU acceleration, implemented using PyTorch averages across the two classification targets, assigning 60% weight to
2.0.1 and Hugging Face Transformers 4.35.0. The final model was research topics and 40% to conservation objectives. This weighting re-
trained with the following key hyperparameters: batch size 10 with flects three considerations: (1) research topics present substantially
gradient accumulation steps of 3 (effective batch size 30), dropout rate greater classification complexity (38 classes vs. 11, with 45:1 imbalance
0.12, weight decay 0.012, and focal loss gamma 2.0. Decision threshold vs. 30:1), meaning that overall metrics dominated by the easier target
selection is described in Section 2.4.2. The complete model architecture would overstate practical system performance; (2) the same weighting
contains 110,254,136 parameters, dominated by the pre-trained Sci- was applied during training loss computation, so evaluation-time
BERT base (110 M parameters) with a small number of additional pa- weighting mirrors the optimization objective; and (3) from a manage-
rameters from the projection and classification heads. ment perspective, thematic coverage assessment across 38 research
priorities represents the primary use case driving this framework's
2.3.5. TF-IDF baseline implementation development. This weighting scheme is applied consistently to all
To provide a non-neural baseline comparison, we implemented a TF- overall metrics reported in Tables 2 and 3, as well as the overall
IDF +Logistic Regression approach using scikit-learn 1.3.0. Text pre- agreement scores in Section 3.3.
processing included lowercase conversion and basic tokenization using
the same concatenated title-abstract-keywords input as neural models. 2.4.4. Statistical testing
We configured TfidfVectorizer with max_features =5000, ngram_range To evaluate improvements over baseline approaches, we compared
= (1,2) to capture unigram and bigram features, and sublinear term the enhanced multi-target SciBERT with a standard BERT model and a
frequency scaling (sublinear_tf = True) to reduce the impact of term TF-IDF +Logistic Regression baseline, all trained on the same dataset.
frequency differences. Statistical significance was assessed using paired t-tests comparing the
For multi-label classification across both targets (themes and objec- five ensemble models from each approach. Effect sizes were calculated
tives), we employed MultiOutputClassifier wrapping LogisticRegression using Cohen's d to quantify the magnitude of improvements. Perfor-
with balanced class weights. mance differences were assessed using the ensemble predictions with
(class_weight =‘balanced’) to address class imbalance, L2 regulari- majority voting (3/5 agreement required for positive classification),
zation (C = 1.0), and lbfgs solver (max_iter = 1000). The model was with improvement percentages calculated for each target. All statistical
trained on the same 247-paper combined training and validation set and tests used α =0.05 with Bonferroni correction for multiple comparisons
evaluated on the identical 48-paper held-out test set used for neural across targets.
baselines, ensuring fair comparison. Classification thresholds were set to
0.5 for all targets. This traditional machine learning baseline represents 2.4.5. Research coverage analysis
what conservation organizations might deploy without deep learning Research coverage analysis quantifies the distribution of classified
infrastructure or domain-specific language models. papers across themes and objectives to identify descriptive patterns in
research coverage. We define research gaps normatively based on
2.4. Model evaluation and validation framework CCAMLR's policy framework: all 38 research topics in the RSRMPA
Research and Monitoring Plan represent priorities that warrant scientific
2.4.1. Performance metrics attention for effective MPA management. A gap exists when research
Model performance was evaluated using macro F1 score as the pri- activity (measured by paper count) is substantially lower for policy-
mary metric for imbalanced multi-label data, complemented by micro designated priorities compared to others, descriptively indicating po-
F1 score, weighted F1 score, precision, recall, and Hamming loss (Zhang tential underinvestment in areas deemed important by management
and Zhou, 2014). Additionally, we calculated Jaccard similarity (inter- frameworks. The extreme class imbalances revealed in Table 1directly
section over union) between predicted and true label sets to quantify indicate such gaps, with some themes appearing in fewer than 5 papers
expert agreement, providing a more intuitive measure of multi-label despite their designation as management priorities. This normative
5

C. McCarthy et al. E c o l o g i c a l I n f o r m a t i c s 94 (2026) 103669
Table 2
Enhanced multi-target SciBERT test set performance (5-model ensemble).
Target Macro F1 Micro F1 Weighted F1 Jaccard Hamming Loss Precision Recall
Research Topics 0.583 0.759 0.749 0.672 0.062 0.575 0.591
CCAMLR Objectives 0.877 0.932 0.933 0.941 0.034 0.883 0.871
Overall Weighted 0.700 – – 0.780 – – –
Note: Dashes ((cid:0) ) indicate metrics where individual aggregation is not applicable. Overall weighted scores use the 60/40 target weighting described in Section 2.4.3.
Jaccard similarity (0.780) is lower than Macro F1 (Topics: 0.583, Objectives: 0.877) because Jaccard uses intersection-over-union for multi-label sets, penalizing both
false positives and false negatives simultaneously, while F1 separately considers precision and recall before harmonizing them.
Table 3
Performance comparison: enhanced SciBERT vs BERT baseline.
Target TF-IDF +LR BERT Baseline Enhanced SciBERT Improvement vs TF-IDF p-value Cohen's d
Research Topics 0.482 0.401 0.583 +21.0% 0.009** 3.01
CCAMLR Objectives 0.766 0.749 0.877 +14.5% 0.007** 3.24
Overall 0.595 0.520 0.700 +17.6% <0.001*** 5.20
*p <0.05, **p <0.01, ***p <0.001.
Note: TF-IDF +LR =TF-IDF vectorization with Logistic Regression (5000 features, unigrams +bigrams, balanced class weights). Overall scores use the 60/40 target
weighting described in Section 2.4.3. Improvement percentages and statistical tests compare Enhanced SciBERT against TF-IDF baseline. All models evaluated on
identical 48-paper test set.
approach reflects conservation practice where policy frameworks define 3.2. Comparison with baseline approaches
what should be researched; our tool reveals what actually is being
researched, with the delta indicating potential gaps for management The enhanced multi-target SciBERT demonstrated statistically sig-
consideration. nificant improvements over both traditional and neural baselines, as
shown in Table 3. We compare three approaches representing different
2.5. Code and data availability methodological paradigms: (1) TF-IDF + Logistic Regression repre-
senting traditional machine learning with domain-appropriate feature
The complete implementation of the Multi-Target SciBERT frame- engineering, (2) BERT baseline representing generic neural language
work, including model training scripts, evaluation pipelines, ensemble models without domain adaptation, and (3) Enhanced SciBERT repre-
training methodology, and classification analysis methodology, is senting domain-adapted transformers with architectural optimizations
available under an open-source license at https://github.com/mccarth for imbalanced multi-label classification.
y-conservation-ai/multitarget-scibert-ross-sea. The repository includes The TF-IDF baseline achieved overall performance of 0.595 (macro
detailed documentation, example notebooks, and configuration files to F1), demonstrating that conservation research classification is tractable
enable reproduction of all results. Complete technical specifications and with traditional machine learning methods. Notably, TF-IDF substan-
hyperparameter details are provided in Supplementary Table S3. The tially outperformed the BERT baseline (0.595 vs 0.520, +14.4%
modular architecture separates domain-specific components (conser- improvement), highlighting that domain-appropriate feature engineer-
vation objectives, Antarctic text preprocessing) from core methodology, ing can match or exceed generic neural architectures without domain-
facilitating adaptation to other research domains. Trained model specific pretraining.
weights for all ensemble models and preprocessing pipelines are pro- Enhanced SciBERT achieved 0.700 overall macro F1, representing a
vided to support immediate deployment. Access to the training dataset is 17.6% improvement over TF-IDF (p <0.001, Cohen's d =5.20), a sub-
freely available in the GitHub repository for testing and development stantial gain for practical deployment. This improvement is particularly
purposes. meaningful because TF-IDF itself substantially outperformed generic
BERT (0.595 vs 0.520, +14.4%), establishing it as a strong baseline that
3. Results captures domain-specific keywords effectively. The per-target im-
provements are even more substantial and consistent: research topics
3.1. Multi-target classification performance improved 21.0% (0.583 vs 0.482, p = 0.009, Cohen's d = 3.01) and
conservation objectives improved 14.5% (0.877 vs 0.766, p = 0.007,
The enhanced multi-target SciBERT framework achieved a weighted Cohen's d =3.24). The substantial improvements on both classification
F1 score of 0.700 ±0.021 on the held-out test set of 48 papers, repre- targets demonstrate the value of combining domain-specific pretraining
senting a 35% improvement over the BERT baseline (0.520). Perfor- (SciBERT's scientific corpus) with architectural enhancements designed
mance across the five ensemble models showed high consistency with F1 for imbalanced multi-label classification (focal loss, target weighting,
scores of 0.674, 0.680, 0.720, 0.714, and 0.713, demonstrating robust multi-rate optimization).
model behavior despite stochastic training variation. We do not include keyword-based or rule-based baselines, as these
Performance reflected the distinct characteristics of the two classi- approaches are impractical for multi-label classification across 49
fication tasks (Table 2). Research topics classification (F1 = 0.583) conservation-specific classes (38 topics +11 objectives). Such baselines
required understanding complex scientific themes despite severe class would require: (1) extensive expert curation of keyword lists for each
imbalance, with papers averaging 2.56 topics each and 59% of topic class, (2) disambiguation rules for overlapping terminology (e.g.,
classes appearing in fewer than 15 papers. CCAMLR objectives classifi- “ecosystem” appears in multiple topics), and (3) multi-label decision
cation (F1 =0.877) achieved higher performance due to clearer policy logic for papers addressing multiple themes simultaneously (papers
definitions and more balanced class distribution. average 2.56 topics and 2.3 objectives). More fundamentally, many
classification targets are defined by conceptual rather than lexical pat-
terns—distinguishing between CCAMLR objectives like “conserve
ecological structure” versus “promote research” requires understanding
6

C. McCarthy et al.                                                                                                                                                                                                E  c  o l o  g  i c a  l   I n  f o r  m  a  t i c s 94 (2026) 103669
policy intent and research contribution, not keyword matching. The TF-  for the robustness of the approach. The consistency across random ini-
IDF baseline provides a more meaningful comparison as it uses the same  tializations suggests the improvements derive from architectural and
multi-label framework and captures semantic relationships through n-  training  strategy  enhancements  rather  than  fortunate  random
| gram features.                              |     |     |          | initialization. |     |     |
| ------------------------------------------- | --- | --- | -------- | --------------- | --- | --- |
| The performance ranking (Enhanced SciBERT > |     |     | TF-IDF > |                 |     |     |
BERT)
validates our methodological approach: domain-specific pretraining  3.6. Research distribution analysis
provides measurable benefits over generic models, while the substantial
improvement over TF-IDF (which already captures domain keywords)  The classification results reveal descriptive patterns in research dis-
demonstrates the value of semantic understanding and architectural  tribution across the RSRMPA research portfolio. Among the 27 research
optimizations  for  imbalanced  multi-label  classification.  TF-IDF's  topics present in the dataset, 16 topics (59%) appear in fewer than 15
competitive performance (0.595) establishes feasibility for resource-  papers,  descriptively  indicating  substantial  underrepresentation.
constrained organizations, while our enhanced approach provides sub- Descriptive gaps include evolutionary biology processes (4 papers),
stantial accuracy gains (17.6% improvement, 26% error reduction) and  seamount benthic communities (3 papers), and Balleny Islands endemic
strong agreement with expert annotations (78% overall, 94% on ob- benthos  (1  paper).  For  conservation  objectives,  while  “promote
research” dominates with high frequency, several specific objectives
jectives) that justify infrastructure investment for high-stakes conser-
vation decision-making. receive notably limited attention. The class imbalance data shows a 30:1
ratio between the most and least represented objectives. Particularly
3.3. Expert agreement analysis underrepresented are objectives related to spatial protection (objective
iii - “protection of representative areas”), monitoring baseline areas
Expert validation demonstrated 78.0% overall agreement (Jaccard  (objective iv), and specific habitat protection objectives. The implica-
similarity) between model predictions and expert annotations across  tions of these coverage patterns for research prioritization are discussed
| both classification targets. The five ensemble models showed consistent  |     |     |     | in Section 4.1. |     |     |
| ------------------------------------------------------------------------ | --- | --- | --- | --------------- | --- | --- |
expert agreement with individual weighted Jaccard scores of 0.745,
0.804, 0.768, 0.754, and 0.752, indicating stable performance across  3.7. Practical deployment examples
| different  random  | initializations.  | Target-specific  | agreement  rates  |     |     |     |
| ------------------ | ----------------- | ---------------- | ----------------- | --- | --- | --- |
revealed strong alignment with human judgment: CCAMLR objectives  To demonstrate real-world applicability, Table 4 presents classifi-
achieved 94.1% agreement while research topics showed 67.2% agree- cation results for three representative papers from recent Ross Sea
ment. The higher agreement on conservation objectives reflects their  research, showing how the framework provides comprehensive classi-
well-defined nature in the CCAMLR framework, while moderate agree- fication for research assessment. Researchers and program managers can
ment on topics reflects the inherent ambiguity in scientific thematic  test their own papers using the pre-trained models and classification tool
classification and severe class imbalance. available at https://github.com/mccarthy-conservation-ai/multitarget
-scibert-ross-sea, which includes detailed documentation and example
3.4. Class imbalance analysis notebooks for immediate deployment.
These examples illustrate the framework's ability to provide multi-
Analysis of the Ross Sea research corpus reveals substantial class  label classification with confidence scores that enable assessment of
prediction reliability. The consistently high confidence for conservation
| imbalance  | that  reflects  actual  | research  priorities.  | Research  topics  |     |     |     |
| ---------- | ----------------------- | ---------------------- | ----------------- | --- | --- | --- |
objectives (0.795–0.971) indicates reliable policy alignment assessment,
showed severe imbalance with class frequencies ranging from 1 to 45
papers per topic (median: 8 papers). The most common topics included  while varying confidence levels for research topics reflect the inherent
“Physical & biological habitat changes” (45 papers) and “Functional  classification challenges across different themes. The framework's abil-
ecology processes” (41 papers), while specialized topics like “Toothfish  ity to identify papers addressing multiple research priorities simulta-
spawning migrations” and “Balleny Islands endemic benthos” appeared  neously supports evidence-based research portfolio assessment and
in only 1–2 papers. This imbalance presents significant challenges for  systematic coverage assessment.
classification, particularly for underrepresented themes critical to con-
servation objectives.
CCAMLR objectives showed less severe but still notable imbalance,
with “promote research” appearing most frequently while specific
habitat protection objectives appeared less often. This distribution re-
Table 4
flects the dual nature of the RSRMPA as both a conservation area and a  Representative multi-target classification examples.
scientific reference zone.
|     |     |     |     | Paper | Research Topics  | CCAMLR Objectives  |
| --- | --- | --- | --- | ----- | ---------------- | ------------------ |
|     |     |     |     |       | (confidence)     | (confidence)       |
3.5. Model robustness
Functional ecology
|     |     |     |     |     | processes (0.522); Prey  | Promote research (0.948);  |
| --- | --- | --- | --- | --- | ------------------------ | -------------------------- |
To ensure reliability, we trained five models with different random  Deep-sea skate nursery
|     |     |     |     |     | availability effects on  | Conserve natural  |
| --- | --- | --- | --- | --- | ------------------------ | ----------------- |
seeds (42, 123, 456, 789, 321), achieving consistent performance with a  habitats; Finucci et al.
|     |     |     |     |     | predators (0.518);  | ecological structure  |
| --- | --- | --- | --- | --- | ------------------- | --------------------- |
coefficient of variation of only 2.7% for overall F1 score. The variation  (2024) Physical & biological  (0.795)
across ensemble models (F1 range: 0.674–0.720, mean ±SD: 0.700 ± habitat changes (0.431)
|                                                                         |     |     |     |                         | Functional ecology  | Promote research (0.971);  |
| ----------------------------------------------------------------------- | --- | --- | --- | ----------------------- | ------------------- | -------------------------- |
| 0.021) provides empirical confidence intervals through bootstrap-style  |     |     |     | Mesozooplankton         |                     |                            |
|                                                                         |     |     |     | distribution patterns;  | processes (0.514);  | Conserve natural           |
resampling with different random initializations. This 95% empirical  Physical & biological  ecological structure
confidence interval (approximately 0.658–0.742, assuming normality)  Minutoli et al. (2024)
|     |     |     |     |     | habitat changes (0.471) | (0.850) |
| --- | --- | --- | --- | --- | ----------------------- | ------- |
demonstrates robust performance relatively insensitive to stochastic  Functional ecology  Conserve natural
|     |     |     |     |     | processes (0.840); Prey  | ecological structure  |
| --- | --- | --- | --- | --- | ------------------------ | --------------------- |
training factors, indicating that performance gains are reliable and
|     |     |     |     |     | availability effects on  | (0.957); Promote research  |
| --- | --- | --- | --- | --- | ------------------------ | -------------------------- |
reproducible rather than artifacts of fortunate initialization. Statistical  Predator-prey dynamics
|     |     |     |     |     | predators (0.719);  | (0.950); Key top predator  |
| --- | --- | --- | --- | --- | ------------------- | -------------------------- |
significance testing comparing enhanced multi-target SciBERT with  in McMurdo Sound;  Toothfish & predator
|     |     |     |     | Ainley et al. (2024) |     | foraging distributions  |
| --- | --- | --- | --- | -------------------- | --- | ----------------------- |
BERT baseline was performed using paired t-tests across these five  distributions (0.429);  (0.853); Coastal/localized
ensemble models. All improvements showed statistical significance (p < Dependence on coastal  areas of ecosystem
0.05) and large effect sizes (Cohen's d >2.8), providing strong evidence  habitats (0.383) importance (0.657)
7

C. McCarthy et al. E c o l o g i c a l I n f o r m a t i c s 94 (2026) 103669
4. Discussion validates the framework's role as a decision-support tool that comple-
ments expert judgment. This performance aligns with recent research
4.1. Implications for evidence-based conservation science showing that SciBERT-based models benefit from domain-specific ad-
aptations (Gupta et al., 2022; Likhareva et al., 2024), validating our
This work demonstrates that automated multi-target classification approach of combining multi-target optimization with conservation-
can transform how conservation organizations evaluate research align- specific strategies. This capability is particularly valuable for funding
ment with policy objectives. By achieving 78% agreement with expert agencies and policy makers who must rapidly assess large research
annotations (noting that this reflects comparison with a single annotator portfolios to ensure strategic alignment with conservation goals while
rather than a consensus panel), the framework addresses a critical maintaining evaluation consistency across reviewers and time periods.
bottleneck in evidence-based conservation planning: the resource-
intensive nature of manual research evaluation across multiple 4.2. Multi-target applications and deployment
dimensions.
This 78% expert agreement should be interpreted in the context of The enhanced multi-target SciBERT framework's ability to classify
multi-label classification challenges. Unlike single-label classification research papers across thematic and policy dimensions provides im-
where only one correct answer exists, multi-label classification requires mediate applications for systematic research portfolio evaluation across
correctly identifying all applicable labels - a paper with three themes diverse stakeholder communities. While our implementation focuses on
needs all three identified for perfect agreement. Given the severe class peer-reviewed research papers, the core multi-target architecture and
imbalance (45:1 ratio with 59% of classes appearing in fewer than 15 methodology can be adapted for different document types through
papers), achieving 67.2% agreement on research topics is particularly appropriate retraining on domain-specific corpora. Grant proposals,
noteworthy, though direct comparison with human inter-annotator technical reports, and policy documents would require customized
agreement is not possible from a single-annotator dataset and remains training datasets that reflect their distinct writing styles, structural el-
an important direction for future validation. The higher 94.1% agree- ements, and evaluation criteria.
ment on conservation objectives reflects their clearer definition in the It's important to note that our initial evaluation revealed geographic
CCAMLR framework, objectives like “key top predator foraging distri- dimensions (management zones and monitoring areas) to be informa-
butions” or “coastal/localized areas of particular ecosystem importance” tion extraction tasks rather than classification challenges. Management
have explicit policy language that makes classification more straight- zones showed 94% single-class dominance, while monitoring areas
forward than the nuanced thematic categories. required only geographic entity recognition. This distinction informs
The 17.6% overall improvement of Enhanced SciBERT over the TF- deployment strategies: content understanding tasks like thematic clas-
IDF baseline (0.700 vs 0.595, p <0.001, Cohen's d =5.20) represents sification benefit from the full SciBERT architecture, while geographic
a substantial gain for practical deployment. This improvement is information can be extracted through simpler pattern matching tech-
particularly meaningful because TF-IDF itself substantially out- niques, allowing organizations to optimize computational resources.
performed generic BERT (0.595 vs 0.520, +14.4%), establishing it as a The following applications demonstrate how the fundamental multi-
strong baseline that captures domain-specific keywords effectively. target approach could be deployed across different organizational con-
Beating this strong baseline by 17.6% demonstrates the value of domain- texts and conservation scales, recognizing that each implementation
specific pretraining combined with architectural optimizations for would need domain-appropriate training data and potentially modified
imbalanced multi-label classification. In practical terms, this 17.6% classification targets.
improvement translates to a 26% reduction in classification errors. For a
corpus of 1000 conservation papers, SciBERT would prevent approxi- 4.2.1. CCAMLR research portfolio assessment
mately 105 misclassifications compared to TF-IDF, directly improving CCAMLR and its Scientific Committee can use the framework to
research prioritization decisions. The per-target improvements are even assess new research papers across research topics and conservation ob-
more substantial: research topics improved 21.0% (0.583 vs 0.482, p = jectives. When processing incoming research proposals or publications,
0.009) and conservation objectives improved 14.5% (0.877 vs 0.766, p managers can quickly identify thematic gaps where certain research
=0.007), with both targets showing consistent gains that validate the topics remain underrepresented and ensure policy alignment with
framework's robustness across different classification challenges. CCAMLR objectives. The multi-target architecture enables identification
For organizations evaluating automated classification approaches, of papers that address multiple conservation objectives through inte-
the choice depends on operational context. TF-IDF provides competitive grated thematic analysis. For example, a single paper might simulta-
performance (0.595) with minimal infrastructure requirements, making neously address “Krill population dynamics” (topic) and “Large-scale
it suitable for pilot deployments or resource-constrained settings. ecosystem processes” (objective).
However, the 17.6% accuracy gain and strong agreement with expert Our framework enables rapid thematic assessment reports for new
annotations (78% overall, 94% on objectives) achieved by Enhanced literature, allowing research coordinators to guide future research pri-
SciBERT justify the additional infrastructure investment for organiza- orities and helping program managers make evidence-based decisions
tions managing large research portfolios or making high-stakes funding about research needs and funding directions. This real-time capability
decisions where classification accuracy directly impacts conservation addresses a critical need, as traditional manual assessment methods are
outcomes. often too slow for policy windows and adaptive management re-
The framework's practical significance extends beyond efficiency quirements (Atalay et al., 2025; Kaymaz Mühling, 2023). This may
gains. Conservation programs often struggle to identify research that provide a useful tool for the five year reports and 10 year reviews
simultaneously addresses multiple objectives within their thematic required of the RSRMPA under Conservation Measure 91–05 (CCAMLR,
scope. Our multi-target approach reveals these high-impact research 2016). Notably, the RSRMPA comes under its formal review in 2027,
opportunities that might be overlooked in traditional single-dimension thus this tool is particularly timely to support this policy process,
assessments. For instance, the framework can instantly identify papers especially given that AI-powered species recognition and monitoring
that combine underrepresented research topics (like evolutionary tools are increasingly seen as essential for uncovering ‘dark diversity’
biology) with critical conservation objectives. These are connections and addressing gaps in conservation knowledge (Reynolds et al., 2025).
that manual review might miss due to time constraints or reviewer It is important to emphasize that this framework identifies thematic
expertise limitations. coverage patterns and policy-relevant topics but does not evaluate
Furthermore, the consistent performance across diverse research research quality, methodological rigor, or whether a policy issue has
contexts (from novel species discoveries to functional ecology studies) been adequately addressed. A high number of papers on a topic does not
8

C. McCarthy et al. E c o l o g i c a l I n f o r m a t i c s 94 (2026) 103669
necessarily indicate sufficient policy analysis, and conversely, a small conservation, where machine learning has shown potential to revolu-
number of high-quality studies may adequately address certain objec- tionize how we process and synthesize conservation data (Reynolds
tives. The framework serves as a screening and mapping tool to identify et al., 2025). Our framework contributes to this movement by providing
what topics are being researched, not to evaluate how well those topics automated classification that can significantly reduce the time required
are being addressed. This distinction is fundamental to appropriate for evidence synthesis, a critical bottleneck given that traditional sys-
deployment of automated classification in conservation decision- tematic reviews are often too slow for policy windows (Cheng et al.,
making. 2018). The framework helps organizations prioritize research themes,
justify conservation investments, and track research progress across
4.2.2. Research funding portfolio optimization conservation priorities with evidence-based assessments.
Grant managers can leverage the framework's multi-target capability
to evaluate incoming proposals for thematic coverage across research 4.2.5. Corporate environmental research portfolio analysis
topics and conservation priorities within a single assessment. When Private sector sustainability managers can use the framework's multi-
reviewing funding applications, users can rapidly identify portfolio target architecture to assess R&D investments across environmental
imbalances and ensure thematic diversity across research investments. themes and business applications in one integrated evaluation. When
This integrated analysis reveals funding applications that optimize reviewing research portfolios, managers can quickly identify sustain-
multiple criteria simultaneously and can identify proposals that address ability gaps and ensure alignment with corporate environmental goals.
underrepresented topics while aligning with conservation objectives. This simultaneous classification reveals projects that optimize multiple
For instance, managers can instantly identify proposals that combine business criteria while addressing environmental priorities. For
evolutionary biology research (underrepresented theme) with specific example, a sustainability project can be instantly classified as carbon
conservation objectives. The framework can help agencies generate reduction research (environmental theme) and supply chain application
portfolio diversity reports, make real-time funding allocation decisions, (business unit). The system enables companies to generate ESG
and justify strategic research investments with quantitative evidence compliance reports, make data-driven research investment decisions,
rather than subjective assessments. and demonstrate environmental commitment to stakeholders with
comprehensive portfolio analysis.
4.2.3. UN sustainable development goals assessment
International organizations can deploy the framework to simulta- 4.3. Limitations and future directions
neously assess research thematic alignment with multiple United Na-
tions Sustainable Development Goals (SDGs) targets and research Several limitations warrant consideration. The framework's perfor-
methodologies in one integrated analysis (United Nations, 2015). When mance depends on training annotation quality, requiring ongoing vali-
evaluating research contributions, users can quickly identify SDG dation and potential retraining as conservation priorities evolve. While
coverage gaps and ensure alignment with priority development goals. our 295-paper dataset represents substantial expert-annotated coverage
The multi-target approach enables identification of research that con- for the specialized Ross Sea domain, successful application to other
tributes to multiple SDGs simultaneously, which is critical given that AI conservation contexts requires: (1) development of domain-specific
can enable the accomplishment of 134 SDG targets across all goals while classification taxonomies aligned with local management objectives,
potentially inhibiting 59 targets (Vinuesa et al., 2020). For example, (2) expert annotation of comparable training datasets, (3) fine-tuning to
using adapted classification targets, a marine conservation study can be capture domain-specific terminology and research patterns, and (4)
automatically classified as addressing SDG 14.2 (sustainable manage- validation against local expert judgment. The architectural approach is
ment of marine ecosystems) and SDG 14.3 (ocean acidification), along transferable; each application requires substantial domain-specific
with methodological approaches, all within a single integrated classifi- development rather than direct model deployment. Periodic model up-
cation, enabling comprehensive impact assessment impossible with dates may be necessary to maintain optimal performance as scientific
sequential single-target approaches. This integrated approach aligns vocabulary and methodological approaches evolve. Most importantly,
with recent bibliometric analyses demonstrating the need for systematic automated classification complements rather than replaces expert
methods to map research contributions across multiple SDGs, with judgment, and integration with human expertise remains essential for
studies showing that AI/ML techniques hold promise for SDG achieve- comprehensive research assessment, aligning with emerging frame-
ment but require regulatory oversight to ensure transparency and works for human-AI collaboration in scientific domains (Wang et al.,
adherence to ethical standards (Meitei et al., 2023). The framework's 2020).
ability to simultaneously assess multiple dimensions supports evidence- Furthermore, because the training corpus was annotated by a single
based approaches to SDG implementation, addressing the sociotechnical domain expert, our reported agreement levels reflect model-versus-one-
challenges of AI deployment while maintaining trust and transparency annotator concordance rather than comparison with a community
(Sachs et al., 2019; Visvizi, 2022). Program managers can generate consensus. A doubly coded subset with independent annotators would
comprehensive SDG alignment reports, track progress toward develop- be needed to benchmark the model against human inter-annotator
ment targets, and guide strategic research investments toward under- agreement and to determine whether the observed 78% Jaccard simi-
represented goals with evidence-based decision making. larity falls within or below the range of expert disagreement on these
multi-label tasks.
4.2.4. Species conservation action planning Neural network training involves inherent randomness from weight
Conservation organizations and wildlife agencies can use the initialization, data shuffling, and stochastic optimization processes that
framework to automatically categorize incoming research by thematic can produce different predictions across model instances trained with
content across conservation strategies and threat assessments in a single identical configurations and datasets. While our ensemble approach
multi-target analysis. When evaluating new research, users can rapidly with five models and majority voting demonstrates consistent overall
assess whether studies address priority conservation actions and identify performance metrics, individual predictions may vary between training
thematic gaps in species research coverage. The integrated classification runs, particularly for borderline classifications near decision thresholds.
approach reveals research that simultaneously addresses multiple con- This variability is most pronounced for papers with ambiguous thematic
servation needs. For example, in endangered species research, wildlife content, where different model instances might produce different clas-
managers might discover that new papers simultaneously address sifications for the same research paper. Conservation managers should
habitat protection (conservation action) and disease threats (threat consider this prediction uncertainty when interpreting individual paper
category). This capability aligns with growing efforts to leverage AI for classifications, especially for critical decision-making scenarios, and
9

C. McCarthy et al. E c o l o g i c a l I n f o r m a t i c s 94 (2026) 103669
may benefit from expert review validation for high-stakes assessments. 5. Conclusion
The current implementation focuses on English-language peer-
reviewed literature, potentially overlooking research published in other This paper presents an enhanced multi-target SciBERT framework
languages or formats. The framework's classification targets are inher- that addresses the critical need for scalable, systematic assessment of
ently constrained by CCAMLR's conservation-focused taxonomy, which research across thematic and policy dimensions. The framework ach-
emphasizes biological and ecological research topics rather than ieved 70.0% macro F1, representing a 17.6% improvement over tradi-
geological or geophysical studies. While our model successfully iden- tional machine learning approaches and demonstrating that domain-
tifies and processes geological papers (preventing systematic exclusion), specific pretraining combined with architectural optimizations pro-
such studies are necessarily classified using biological conservation vides measurable benefits for conservation text classification. The sys-
themes due to the absence of geological categories in the CCAMLR tem successfully identified and quantified descriptive patterns in
framework. For example, geological studies of mud volcanoes or seismic research coverage across thematic and policy dimensions, with 59% of
processes receive classifications such as “Benthic community structure & research topics appearing in fewer than 15 papers, providing quantita-
function” or “Physical & biological habitat changes,” which represent tive foundations for evidence-based conservation planning through
reasonable approximations within the conservation context but may not validated multi-target classification. Expert validation confirmed the
fully capture the geological research scope. This limitation reflects the framework's reliability with 78% agreement across both conservation
framework's design for conservation research assessment rather than dimensions and particularly strong performance on policy alignment
comprehensive scientific literature analysis, and adaptation to broader (94% agreement), demonstrating automated classification with sub-
research domains would require expansion of classification taxonomies stantial agreement with single-expert annotations while enabling scal-
beyond CCAMLR's conservation-specific structure. able deployment for systematic literature analysis. This transferable
Several directions could enhance model performance and applica- approach offers conservation organizations, funding agencies, and re-
bility. The reliance on title, abstract, and keywords rather than full text searchers a systematic tool to transform ad hoc research prioritization
represents a meaningful constraint that may bias results toward papers into strategic, evidence-based planning through automated coverage
with explicit topic statements in metadata while underrepresenting analysis methodology, ultimately strengthening the science-policy
complex interdisciplinary studies where key themes emerge only in interface in conservation practice and complementing expert judgment
detailed methods or discussion sections. This limitation particularly af- in comprehensive research evaluation. As AI-assisted frameworks
fects classification of papers with nuanced or emergent research con- continue to mature, they have the potential to become standard tools
tributions not clearly signaled in abstracts. Incorporating full-text integrated into conservation planning workflows, enabling evidence-
analysis could capture additional conceptual depth, though this must be based decision-making at unprecedented scale while maintaining
balanced against practical accessibility advantages for real-world essential human oversight.
deployment. Training on larger, more diverse conservation corpora
could improve generalization to other protected areas. Active learning CRediT authorship contribution statement
approaches could prioritize the most informative papers for expert
annotation, making dataset expansion more efficient. Integration with Chris McCarthy: Writing – review & editing, Writing – original
citation networks and research impact metrics could add another draft, Visualization, Validation, Software, Project administration,
dimension to research assessment. Finally, developing confidence cali- Methodology, Investigation, Formal analysis, Data curation, Conceptu-
bration techniques could provide more reliable uncertainty estimates for alization. Cassandra Brooks: Writing – review & editing, Writing –
individual predictions, helping users identify when expert review is original draft, Supervision, Resources, Methodology, Data curation,
most needed. Conceptualization. Troy Sternberg: Writing – review & editing, Writing
Additional developments should consider multilingual capabilities, – original draft, Supervision, Formal analysis, Conceptualization. Kyle
integration of grey literature and technical reports, ensemble methods Shaney: Writing – review & editing, Writing – original draft, Investi-
and uncertainty quantification approaches to enhance prediction reli- gation, Formal analysis, Conceptualization. Buho Hoshino: Writing –
ability, and expanded taxonomies for interdisciplinary research do- review & editing, Writing – original draft, Resources, Methodology,
mains. While transformer-based models excel at content understanding Funding acquisition, Conceptualization.
and pattern recognition, they cannot assess research quality, methodo-
logical rigor, or actual conservation impact, fundamental limitations Declaration of competing interest
arising from their reliance on distributional patterns rather than genuine
comprehension (Bender et al., 2021). These models effectively classify The authors declare the following financial interests/personal re-
research content based on textual patterns but cannot evaluate whether lationships which may be considered as potential competing interests:
research findings are scientifically sound, practically implementable, or Dr. Andrew Titmus reports a relationship with National Science
cost-effective. However, emerging approaches in AI development, Foundation that includes: employment. If there are other authors, they
including retrieval-augmented generation, multi-modal learning, and declare that they have no known competing financial interests or per-
improved reasoning capabilities, may eventually enable more sophisti- sonal relationships that could have appeared to influence the work re-
cated research assessment that goes beyond surface-level classification ported in this paper.
to evaluate methodological soundness and potential conservation
impact. Our focus on the Ross Sea region Marine Protected Area pro- Acknowledgments
vides proof-of-concept for the multi-target approach. The framework's
demonstrated success in this domain establishes technical feasibility, The authors thank Dr. Andrew Titmus (Office of Polar Programs,
though validation across diverse protected areas and conservation do- National Science Foundation) for his valuable contributions to the
mains with varying management frameworks and research priorities conceptualization and development of this research. This work was
would be necessary to support broader generalizability claims. The supported by JSPS KAKENHI Project Number 25K03325 “Verification of
modular design enables continual learning capabilities where newly abandoned oil well plugging effects for carbon offset credits by precise
classified papers can be incorporated into the training dataset to create a measurement of methane emissions”.
self-improving system, potentially mitigating temporal degradation
while reducing long-term annotation costs through active learning ap- Appendix A. Supplementary data
proaches that prioritize the most informative papers for expert review.
Supplementary data to this article can be found online at https://doi.
10

C. McCarthy et al. E c o l o g i c a l I n f o r m a t i c s 94 (2026) 103669
org/10.1016/j.ecoinf.2026.103669. Kaymaz Mühling, S¸.M., 2023. Utilizing artificial intelligence (AI) for the identification
and management of marine protected areas (MPAs): a review. GEP 11, 118–132.
https://doi.org/10.4236/gep.2023.119008.
Data availability Kopperud, B.T., Lidgard, S., Liow, L.H., 2022. Enhancing georeferenced biodiversity
inventories: automated information extraction from literature records reveal the
The complete implementation of the Multi-Target SciBERT frame- gaps. PeerJ 10, e13921. https://doi.org/10.7717/peerj.13921.
Lemos, M.C., Arnott, J.C., Ardoin, N.M., Baja, K., Bednarek, A.T., Dewulf, A., Fieseler, C.,
work, including model training scripts, evaluation pipelines, TF-IDF
Goodrich, K.A., Jagannathan, K., Klenk, N., Mach, K.J., Meadow, A.M., Meyer, R.,
baseline implementation, ensemble training methodology, and trained Moss, R., Nichols, L., Sjostrom, K.D., Stults, M., Turnhout, E., Vaughan, C., Wong-
model weights, is available under an open-source license at Parodi, G., Wyborn, C., 2018. To co-produce or not to co-produce. Nat. Sustainability
1, 722–724. https://doi.org/10.1038/s41893-018-0191-0.
https://github.
Likhareva, D., Sankaran, H., Thiyagarajan, S., 2024. Empowering Interdisciplinary
com/mccarthy-conservation-ai/multitarget-scibert-ross-sea. The expert- Research with BERT-Based Models: An Approach through SciBERT-CNN with Topic
annotated dataset of 295 Ross Sea region research papers used for Modeling. https://doi.org/10.48550/ARXIV.2404.13078.
Lin, T.-Y., Goyal, P., Girshick, R., He, K., Dollar, P., 2017. Focal loss for dense object
training and evaluation is freely available in the same repository. All
detection. In: 2017 IEEE International Conference on Computer Vision (ICCV).
code and data necessary to reproduce the results reported in this paper Presented at the 2017 IEEE International Conference on Computer Vision (ICCV).
are provided. IEEE, Venice, pp. 2999–3007. https://doi.org/10.1109/ICCV.2017.324.
Marine Conservation Institute, 2024. MPAtlas – Marine Protected Areas Atlas.
Meitei, A.J., Rai, P., Rajkishan, S.S., 2023. Application of AI/ML techniques in achieving
References SDGs: a bibliometric study. Environ. Dev. Sustain. 27, 281–317. https://doi.org/
10.1007/s10668-023-03935-1.
Ainley, D.G., Morandini, V., Salas, L., Nur, N., Rotella, J., Barton, K., Lyver, P.O., Minutoli, R., Bonanno, A., Guglielmo, L., Bergamasco, Alessandro, Grillo, M.,
Goetz, K.T., Larue, M., Foster-Dyer, R., Parkinson, C.L., Arrigo, K.R., Van Dijken, G., Schiaparelli, S., Barra, M., Bergamasco, Andrea, Remirens, A., Genovese, S.,
Beltran, R.S., Kim, S., Brooks, C., Kooyman, G., Ponganis, P.J., Shanhun, F., Granata, A., 2024. Biodiversity and functioning of mesozooplankton in a changing
Anderson, D.P., 2024. Response of indicator species to changes in food web and Ross Sea. Deep Sea Research Part II. Topical Studies Oceanogra 217, 105401.
ocean dynamics of the Ross Sea, Antarctica. Antarctic Sci 36, 290–318. https://doi. https://doi.org/10.1016/j.dsr2.2024.105401.
org/10.1017/s0954102024000191. Pike, E.P., MacCarthy, J.M.C., Hameed, S.O., Harasta, N., Grorud-Colvert, K., Sullivan-
Aria, M., Cuccurullo, C., 2017. Bibliometrix: an R-tool for comprehensive science Stack, J., Claudet, J., Horta E Costa, B., Gonçalves, E.J., Villagomez, A., Morgan, L.,
mapping analysis. J. Inf. Secur. 11, 959–975. https://doi.org/10.1016/j. 2024. Ocean protection quality is lagging behind quantity: applying a scientific
joi.2017.08.007. framework to assess real marine protected area progress against the 30 by 30 target.
Atalay, A., Perkumiene˙, D., Safaa, L., S ˇ ke˙ma, M., Aleinikovas, M., 2025. Artificial Conserv. Lett. 17, e13020. https://doi.org/10.1111/conl.13020.
intelligence technologies as smart solutions for sustainable protected areas Piwowar, H., Priem, J., Larivi`ere, V., Alperin, J.P., Matthias, L., Norlander, B., Farley, A.,
management. Sustainability 17, 5006. https://doi.org/10.3390/su17115006. West, J., Haustein, S., 2018. The state of OA: a large-scale analysis of the prevalence
Beltagy, I., Lo, K., Cohan, A., 2019. SciBERT: A Pretrained Language Model for Scientific and impact of open access articles. PeerJ 6, e4375. https://doi.org/10.7717/
Text. https://doi.org/10.48550/ARXIV.1903.10676. peerj.4375.
Bender, E.M., Gebru, T., McMillan-Major, A., Shmitchell, S., 2021. On the dangers of Reynolds, S.A., Beery, S., Burgess, N., Burgman, M., Butchart, S.H.M., Cooke, S.J.,
stochastic parrots: can language models be too big?. In: Proceedings of the 2021 Coomes, D., Danielsen, F., Di Minin, E., Dur´an, A.P., Gassert, F., Hinsley, A.,
ACM Conference on Fairness, Accountability, and Transparency. Presented at the Jaffer, S., Jones, J.P.G., Li, B.V., Mac Aodha, O., Madhavapeddy, A., O’Donnell, S.A.
FAccT ‘21: 2021 ACM Conference on Fairness, Accountability, and Transparency. L., Oxbury, W.M., Peck, L., Pettorelli, N., Rodríguez, J.P., Shuckburgh, E.,
ACM, Virtual Event Canada, pp. 610–623. https://doi.org/10.1145/ Strassburg, B., Yamashita, H., Miao, Z., Sutherland, W.J., 2025. The potential for AI
3442188.3445922. to revolutionize conservation: a horizon scan. Trends Ecol. Evol. 40, 191–207.
Brooks, C.M., Ainley, D.G., 2022. A summary of United States research and monitoring in https://doi.org/10.1016/j.tree.2024.11.013.
support of the Ross Sea region marine protected area. Diversity 14, 447. https://doi. Rogers, A., Kovaleva, O., Rumshisky, A., 2020. A primer in BERTology: what we know
org/10.3390/d14060447. about how BERT works. Trans. Assoc. Comp. Ling. 8, 842–866. https://doi.org/
CCAMLR, 2016. Conservation measure 91-05: Ross Sea region marine protected area 10.1162/tacl_a_00349.
(conservation measure No. 91–05). In: Commission for the Conservation of Antarctic Ruder, S., 2017. An Overview of Multi-task Learning in Deep Neural Networks. https://
Marine Living Resources, Hobart, Australia. doi.org/10.48550/ARXIV.1706.05098.
Chalkidis, I., Fergadiotis, M., Kotitsas, S., Malakasiotis, P., Aletras, N., Sabo, A.N., Berger-Tal, O., Blumstein, D.T., Greggor, A.L., Swaddle, J.P., 2024.
Androutsopoulos, I.. An Empirical Study on Large-Scale Multi-Label Text Conservation practitioners’ and researchers’ needs for bridging the
Classification Including Few and Zero-Shot Labels. https://doi.org/10.18653/v1/20 knowledge–action gap. Front. Conserv. Sci. 5, 1415127. https://doi.org/10.3389/
20.emnlp-main.607. fcosc.2024.1415127.
Cheng, S.H., Augustin, C., Bethel, A., Gill, D., Anzaroot, S., Brun, J., DeWilde, B., Sachs, J.D., Schmidt-Traub, G., Mazzucato, M., Messner, D., Nakicenovic, N.,
Minnich, R.C., Garside, R., Masuda, Y.J., Miller, D.C., Wilkie, D., Rockstro¨m, J., 2019. Six transformations to achieve the sustainable development
Wongbusarakum, S., McKinnon, M.C., 2018. Using machine learning to advance goals. Nat. Sustainability 2, 805–814. https://doi.org/10.1038/s41893-019-0352-9.
synthesis and use of conservation and environmental evidence. Conserv. Biol. 32, Sutherland, W.J., Pullin, A.S., Dolman, P.M., Knight, T.M., 2004. The need for evidence-
762–764. https://doi.org/10.1111/cobi.13117. based conservation. Trends Ecol. Evol. 19, 305–308. https://doi.org/10.1016/j.
Cook, C.N., Mascia, M.B., Schwartz, M.W., Possingham, H.P., Fuller, R.A., 2013. tree.2004.03.018.
Achieving conservation science that bridges the knowledge–action boundary. Toomey, A.H., Knight, A.T., Barlow, J., 2017. Navigating the space between research and
Conserv. Biol. 27, 669–678. https://doi.org/10.1111/cobi.12050. implementation in conservation. Conserv. Lett. 10, 619–625. https://doi.org/
Cvitanovic, C., McDonald, J., Hobday, A.J., 2016. From science to action: principles for 10.1111/conl.12315.
undertaking environmental research that enables knowledge exchange and UNEP-WCMC, IUCN, 2021. Protected Planet Report 2020.
evidence-based decision-making. J. Environ. Manag. 183, 864–874. https://doi.org/ United Nations, 2015. Transforming Our World: The 2030 Agenda for Sustainable
10.1016/j.jenvman.2016.09.038. Development (Resolution No. A/RES/70/1). United Nations General Assembly.
Dunn, A., Vacchi, M., Watters, G., 2017. The Ross Sea region Marine Protected Area Vinuesa, R., Azizpour, H., Leite, I., Balaam, M., Dignum, V., Domisch, S., Fell¨ander, A.,
Research and Monitoring Plan (CCAMLR Document No. SC-CAMLR-XXXVI/20). Langhans, S.D., Tegmark, M., Fuso Nerini, F., 2020. The role of artificial intelligence
Commission for the Conservation of Antarctic Marine Living Resources (CCAMLR), in achieving the sustainable development goals. Nat. Commun. 11. https://doi.org/
Hobart, Australia. 10.1038/s41467-019-14108-y.
Finucci, B., Chin, C., O’Neill, H.L., White, W.T., Pinkerton, M.H., 2024. First observation Visvizi, A., 2022. Artificial intelligence (AI) and sustainable development goals (SDGs):
of a skate egg case nursery in the Ross Sea. J. Fish Bio. 104, 1645–1650. https://doi. exploring the impact of AI on politics and society. Sustainability 14, 1730. https://
org/10.1111/jfb.15688. doi.org/10.3390/su14031730.
Gil-Clavel, S., Filatova, T., 2023. Using Natural Language Processing and Networks to Wang, D., Churchill, E., Maes, P., Fan, X., Shneiderman, B., Shi, Y., Wang, Q., 2020. From
Automate Structured Literature Reviews: An Application to Farmers Climate Change human-human collaboration to human-AI collaboration: designing AI systems that
Adaptation. https://doi.org/10.48550/ARXIV.2306.09737. can work together with people. In: Extended Abstracts of the 2020 CHI Conference
Gill, D.A., Mascia, M.B., Ahmadia, G.N., Glew, L., Lester, S.E., Barnes, M., Craigie, I., on Human Factors in Computing Systems. Presented at the CHI ‘20: CHI Conference
Darling, E.S., Free, C.M., Geldmann, J., Holst, S., Jensen, O.P., White, A.T., on Human Factors in Computing Systems. ACM, Honolulu HI USA, pp. 1–6. https://
Basurto, X., Coad, L., Gates, R.D., Guannel, G., Mumby, P.J., Thomas, H., doi.org/10.1145/3334480.3381069.
Whitmee, S., Woodley, S., Fox, H.E., 2017. Capacity shortfalls hinder the Westgate, M.J., Barton, P.S., Pierson, J.C., Lindenmayer, D.B., 2015. Text analysis tools
performance of marine protected areas globally. Nature 543, 665–669. https://doi. for identification of emerging topics and research gaps in conservation science.
org/10.1038/nature21708. Conserv. Biol. 29, 1606–1614. https://doi.org/10.1111/cobi.12605.
Gupta, T., Zaki, M., Krishnan, N.M.A., Mausam, 2022. MatSciBERT: a materials domain Zhang, Y., Yang, Q., 2017. A Survey on Multi-task Learning. https://doi.org/10.48550/
language model for text mining and information extraction. NPJ Comput. Mater. 8. ARXIV.1707.08114.
https://doi.org/10.1038/s41524-022-00784-w. Zhang, M.-L., Zhou, Z.-H., 2014. A review on multi-label learning algorithms. IEEE Trans.
Jones, K.R., Venter, O., Fuller, R.A., Allan, J.R., Maxwell, S.L., Negret, P.J., Watson, J.E. Knowl. Data Eng. 26, 1819–1837. https://doi.org/10.1109/TKDE.2013.39.
M., 2018. One-third of global protected land is under intense human pressure.
Science 360, 788–791. https://doi.org/10.1126/science.aap9565.
11
