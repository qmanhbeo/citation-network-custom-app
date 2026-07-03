SemEval-2014 Task 1: Evaluation of Compositional Distributional
Semantic Models on Full Sentences through Semantic Relatedness and
Textual Entailment
MarcoMarelli(1) LuisaBentivogli(2) MarcoBaroni(1)
RaffaellaBernardi(1) StefanoMenini(1,2) RobertoZamparelli(1)
(1) UniversityofTrento,Italy
(2) FBK-FondazioneBrunoKessler,Trento,Italy
{name.surname}@unitn.it,{bentivo,menini}@fbk.eu
Abstract data sets have been developed for various com-
putational semantics tasks, such as Semantic Text
This paper presents the task on the evalu- Similarity(STS)(Agirreetal.,2012)orRecogniz-
ation of Compositional Distributional Se- ingTextualEntailment(RTE)(Daganetal.,2006).
mantics Models on full sentences orga- Working with such data sets, however, requires
nized for the first time within SemEval- dealingwithissues,suchasidentifyingmultiword
2014. Participation was open to systems expressions,recognizingnamedentitiesoraccess-
basedonanyapproach. Systemswerepre- ing encyclopedic knowledge, which have little to
sented with pairs of sentences and were do with compositionality per se. CDSMs should
evaluated on their ability to predict hu- instead be evaluated on data that are challenging
manjudgmentson(i)semanticrelatedness forreasonsduetosemanticcompositionality(e.g.
and (ii) entailment. The task attracted 21 context-cued synonymy resolution and other lexi-
teams, most of which participated in both cal variation phenomena, active/passive and other
subtasks. We received 17 submissions in syntactic alternations, impact of negation at vari-
the relatedness subtask (for a total of 66 ouslevels,operatorscope,andothereffectslinked
runs)and18intheentailmentsubtask(65 tothefunctionallexicon). Theseissuesdonotoc-
runs). curfrequentlyin,e.g.,theSTSandRTEdatasets.
With these considerations in mind, we devel-
1 Introduction oped SICK (Sentences Involving Compositional
Knowledge), a data set aimed at filling the void,
Distributional Semantic Models (DSMs) approx-
including a large number of sentence pairs that
imate the meaning of words with vectors sum-
arerichinthelexical,syntacticandsemanticphe-
marizing their patterns of co-occurrence in cor-
nomena that CDSMs are expected to account for,
pora. Recently, several compositional extensions
but do not require dealing with other aspects of
of DSMs (CDSMs) have been proposed, with the
existing sentential data sets that are not within
purpose of representing the meaning of phrases
the scope of compositional distributional seman-
andsentencesbycomposingthedistributionalrep-
tics. Moreover, wedistinguishedbetweengeneric
resentationsofthewordstheycontain(Baroniand
semantic knowledge about general concept cate-
Zamparelli, 2010; Grefenstette and Sadrzadeh,
gories(suchasknowledgethatacoupleisformed
2011; Mitchell and Lapata, 2010; Socher et al.,
byabrideandagroom)andencyclopedicknowl-
2012). Despite the ever increasing interest in the
edge about specific instances of concepts (e.g.,
field,thedevelopmentofadequatebenchmarksfor
knowing the fact that the current president of the
CDSMs, especially at the sentence level, is still
USisBarackObama). TheSICKdatasetcontains
lagging. Existing data sets, such as those intro-
manyexamplesoftheformer, butnoneofthelat-
ducedbyMitchellandLapata(2008)andGrefen-
ter.
stette and Sadrzadeh (2011), are limited to a few
hundred instances of very short sentences with a 2 TheTask
fixed structure. In the last ten years, several large
The Task involved two subtasks. (i) Relatedness:
This work is licensed under a Creative Commons At- predicting the degree of semantic similarity be-
tribution 4.0 International Licence. Page numbers and pro-
tween two sentences, and (ii) Entailment: detect-
ceedingsfooterareaddedbytheorganisers. Licencedetails:
http://creativecommons.org/licenses/by/4.0/ ing the entailment relation holding between them
1
Proceedingsofthe8thInternationalWorkshoponSemanticEvaluation(SemEval2014),pages1–8,
Dublin,Ireland,August23-24,2014.

(see below for the exact definition). Sentence re- 3.1 DataSetCreation
latedness scores provide a direct way to evalu-
SICK was built starting from two existing data
ate CDSMs, insofar as their outputs are able to
sets: the 8K ImageFlickr data set1 and the
quantifythedegreeofsemanticsimilaritybetween
SemEval-2012STSMSR-VideoDescriptionsdata
sentences. On the other hand, starting from the
set.2 The 8K ImageFlickr dataset is a dataset of
assumption that understanding a sentence means
images, where each image is associated with five
knowing when it is true, being able to verify
descriptions. To derive SICK sentence pairs we
whether an entailment is valid is a crucial chal-
randomly chose 750 images and we sampled two
lengeforsemanticsystems.
descriptions from each of them. The SemEval-
In the semantic relatedness subtask, given two 2012 STS MSR-Video Descriptions data set is a
sentences, systems were required to produce a re- collectionofsentencepairssampledfromtheshort
latedness score (on a continuous scale) indicating video snippets which compose the Microsoft Re-
theextenttowhichthesentenceswereexpressing searchVideoDescriptionCorpus. Asubsetof750
arelatedmeaning. Table1showsexamplesofsen- sentence pairs were randomly chosen from this
tence pairs with different degrees of semantic re- datasettobeusedinSICK.
latedness;goldrelatednessscoresareexpressedon In order to generate SICK data from the 1,500
a5-pointratingscale. sentencepairstakenfromthesourcedatasets,a3-
stepprocesswasappliedtoeachsentencecompos-
In the entailment subtask, given two sentences
ing the pair, namely (i) normalization, (ii) expan-
A and B, systems had to determine whether the
sionand(iii)pairing. Table3presentsanexample
meaningofBwasentailedbyA.Inparticular,sys-
oftheoutputofeachstepintheprocess.
tems were required to assign to each pair either
The normalization step was carried out on the
the ENTAILMENT label (when A entails B, viz.,
original sentences (S0) to exclude or simplify in-
B cannot be false when A is true), the CONTRA-
stancesthatcontainedlexical,syntacticorseman-
DICTIONlabel(whenAcontradictedB,viz. Bis
tic phenomena (e.g., named entities, dates, num-
falsewheneverAistrue),ortheNEUTRALlabel
bers,multiwordexpressions)thatCDSMsarecur-
(when the truth of B could not be determined on
rentlynotexpectedtoaccountfor.
the basis of A). Table 2 shows examples of sen-
tencepairsholdingdifferententailmentrelations. The expansion step was applied to each of the
normalizedsentences(S1)inordertocreateupto
Participants were invited to submit up to five
three new sentences with specific characteristics
system runs for one or both subtasks. Developers
suitable to CDSM evaluation. In this step syntac-
of CDSMs were especially encouraged to partic-
ticandlexicaltransformationswithpredictableef-
ipate, but developers of other systems that could
fectswereappliedtoeachnormalizedsentence,in
tackle sentence relatedness or entailment tasks
ordertoobtain(i)asentencewithasimilarmean-
were also welcome. Besides being of intrinsic in-
ing(S2),(ii)asentencewithalogicallycontradic-
terest, the latter systems’ performance will serve
tory or at least highly contrasting meaning (S3),
to situate CDSM performance within the broader
and(iii)asentencethatcontainsmostofthesame
landscapeofcomputationalsemantics.
lexicalitems,buthasadifferentmeaning(S4)(this
laststepwascarriedoutonlywhereitcouldyield
ameaningfulsentence;asaresult,notallnormal-
3 TheSICKDataSet
izedsentenceshavean(S4)expansion).
Finally, in the pairing step each normalized
TheSICKdataset,consistingofabout10,000En- sentence in the pair was combined with all the
glish sentence pairs annotated for relatedness in sentences resulting from the expansion phase and
meaning and entailment, was used to evaluate the with the other normalized sentence in the pair.
systems participating in the task. The data set Considering the example in Table 3, S1a and S1b
creation methodology is outlined in the following were paired. Then, S1a and S1b were each com-
subsections, while all the details about data gen- binedwithS2a,S2b,S3a,S3b,S4a,andS4b,lead-
eration and annotation, quality control, and inter-
1http://nlp.cs.illinois.edu/HockenmaierGroup/data.html
annotatoragreementcanbefoundinMarellietal.
2http://www.cs.york.ac.uk/semeval-
(2014). 2012/task6/index.php?id=data
2

Relatednessscore Example
A:“Amanisjumpingintoanemptypool”
1.6
B:“Thereisnobikerjumpingintheair”
A:“Twochildrenarelyinginthesnowandaremakingsnowangels”
2.9
B:“Twoangelsaremakingsnowonthelyingchildren”
A:“Theyoungboysareplayingoutdoorsandthemanissmilingnearby”
3.6
B:“Thereisnoboyplayingoutdoorsandthereisnomansmiling”
A:“Apersoninablackjacketisdoingtricksonamotorbike”
4.9
B:“Amaninablackjacketisdoingtricksonamotorbike”
Table1: Examplesofsentencepairswiththeirgoldrelatednessscores(ona5-pointratingscale).
Entailmentlabel Example
A:“Twoteamsarecompetinginafootballmatch”
ENTAILMENT
B:“Twogroupsofpeopleareplayingfootball”
A:“Thebrownhorseisneararedbarrelattherodeo”
CONTRADICTION
B:“Thebrownhorseisfarfromaredbarrelattherodeo”
A:“Amaninablackjacketisdoingtricksonamotorbike”
NEUTRAL
B:“Apersonisridingthebicycleononewheel”
Table2: Examplesofsentencepairswiththeirgoldentailmentlabels.
ingtoatotalof13differentsentencepairs. sidering both directions). The ratings were col-
Furthermore, a number of pairs composed of lectedthroughalargecrowdsourcingstudy,where
completely unrelated sentences were added to the each pair was evaluated by 10 different subjects,
data set by randomly taking two sentences from andtheorderofpresentationofthesentenceswas
twodifferentpairs. counterbalanced (i.e., 5 judgments were collected
The result is a set of about 10,000 new sen- for each presentation order). Swapping the order
tence pairs, in which each sentence is contrasted of the sentences within each pair served a two-
with either a (near) paraphrase, a contradictory or fold purpose: (i) evaluating the entailment rela-
strongly contrasting statement, another sentence tion in both directions and (ii) controlling pos-
withveryhighlexicaloverlapbutdifferentmean- sible bias due to priming effects in the related-
ing, or a completely unrelated sentence. The ra- nesstask. Oncealltheannotationswerecollected,
tionale behind this approach was that of building the relatedness gold score was computed for each
a data set which encouraged the use of a com- pair as the average of the ten ratings assigned by
positional semantics step in understanding when participants, whereas a majority vote scheme was
two sentences have close meanings or entail each adoptedfortheentailmentgoldlabels.
other, hindering methods based on individual lex-
3.3 DataSetStatistics
ical items, on the syntactic complexity of the two
sentencesoronpureworldknowledge. For the purpose of the task, the data set was ran-
domly split into training and test set (50% and
3.2 RelatednessandEntailmentAnnotation
50%),ensuringthateachrelatednessrangeanden-
Each pair in the SICK dataset was annotated to tailment categorywas equally representedin both
mark (i) the degree to which the two sentence sets. Table 4 shows the distribution of sentence
meanings are related (on a 5-point scale), and (ii) pairs considering the combination of relatedness
whether one entails or contradicts the other (con- ranges and entailment labels. The “total” column
3

Originalpair
S0a: Aseaturtleishuntingforfish S0b: Theturtlefollowedthefish
Normalizedpair
S1a: Aseaturtleishuntingforfish S1b: Theturtleisfollowingthefish
Expandedpairs
S2a: Aseaturtleishuntingforfood S2b: Theturtleisfollowingtheredfish
S3a: Aseaturtleisnothuntingforfish S3b: Theturtleisn’tfollowingthefish
S4a: Afishishuntingforaturtleinthesea S4b: Thefishisfollowingtheturtle
|           |           |           | Table3:  | Datasetcreationprocess. |          |     |             |     |            |     |     |
| --------- | --------- | --------- | -------- | ----------------------- | -------- | --- | ----------- | --- | ---------- | --- | --- |
|           |           |           |          |                         | Baseline |     | Relatedness |     | Entailment |     |     |
| indicates | the total | number of | pairs in | each range              |          |     |             |     |            |     |     |
of relatedness, while the “total” row contains the Chance 0 33.3%
| totalnumberofpairsineachentailmentclass. |     |     |     |     | Majority    |     |     | NA   | 56.7% |     |     |
| ---------------------------------------- | --- | --- | --- | --- | ----------- | --- | --- | ---- | ----- | --- | --- |
|                                          |     |     |     |     | Probability |     |     | NA   | 41.8% |     |     |
|                                          |     |     |     |     | Overlap     |     |     | 0.63 | 56.2% |     |     |
SICKTrainingSet
| relatedness | CONTRADICT | ENTAIL | NEUTRAL  | TOTAL |         |                         |     |     |               |     |     |
| ----------- | ---------- | ------ | -------- | ----- | ------- | ----------------------- | --- | --- | ------------- | --- | --- |
| 1-2range    | 0(0%)      | 0(0%)  | 471(10%) | 471   |         |                         |     |     |               |     |     |
|             |            |        |          |       | Table5: | Performanceofbaselines. |     |     | Figureofmerit |     |     |
| 2-3range    | 59(1%)     | 2(0%)  | 638(13%) | 699   |         |                         |     |     |               |     |     |
isPearsoncorrelationforrelatednessandaccuracy
| 3-4range | 498(10%) | 71(1%)    | 1344(27%) | 1913 |                |     |                  |     |     |     |     |
| -------- | -------- | --------- | --------- | ---- | -------------- | --- | ---------------- | --- | --- | --- | --- |
|          |          |           |           |      | forentailment. |     | NA=NotApplicable |     |     |     |     |
| 4-5range | 155(3%)  | 1344(27%) | 352(7%)   | 1851 |                |     |                  |     |     |     |     |
| TOTAL    | 712      | 1417      | 2805      | 4934 |                |     |                  |     |     |     |     |
SICKTestSet
5 SubmittedRunsandResults
| relatedness | CONTRADICT | ENTAIL | NEUTRAL  | TOTAL |                                       |     |     |     |     |          |     |
| ----------- | ---------- | ------ | -------- | ----- | ------------------------------------- | --- | --- | --- | --- | -------- | --- |
| 1-2range    | 0(0%)      | 1(0%)  | 451(9%)  | 452   |                                       |     |     |     |     |          |     |
|             |            |        |          |       | Overall,21teamsparticipatedinthetask. |     |     |     |     | Partici- |     |
| 2-3range    | 59(1%)     | 0(0%)  | 615(13%) | 674   |                                       |     |     |     |     |          |     |
3-4range 496(10%) 65(1%) 1398(28%) 1959 pantswereallowedtosubmitupto5runsforeach
subtaskandhadtochoosetheprimaryruntobein-
| 4-5range | 157(3%) | 1338(27%) | 326(7%) | 1821 |     |     |     |     |     |     |     |
| -------- | ------- | --------- | ------- | ---- | --- | --- | --- | --- | --- | --- | --- |
TOTAL 712 1404 2790 4906 cludedinthecomparativeevaluation. Wereceived
|          |              |             |       |            | 17 submissions |     | to the | relatedness | subtask | (for | a   |
| -------- | ------------ | ----------- | ----- | ---------- | -------------- | --- | ------ | ----------- | ------- | ---- | --- |
| Table 4: | Distribution | of sentence | pairs | across the |                |     |        |             |         |      |     |
totalof66runs)and18fortheentailmentsubtask
TrainingandTestSets.
(65runs).
|     |     |     |     |     | We asked | participants |           | to  | pre-specify | a   | pri- |
| --- | --- | --- | --- | --- | -------- | ------------ | --------- | --- | ----------- | --- | ---- |
|     |     |     |     |     | mary run | to           | encourage |     | commitment  |     | to a |
4 EvaluationMetricsandBaselines
|     |     |     |     |     | theoretically-motivated |     |     | approach, | rather |     | than |
| --- | --- | --- | --- | --- | ----------------------- | --- | --- | --------- | ------ | --- | ---- |
Bothsubtaskswereevaluatedusingstandardmet- post-hoc performance-based assessment. Inter-
rics. In particular, the results on entailment were estingly, some participants used the non-primary
evaluated using accuracy, whereas the outputs on runs to explore the performance one could reach
relatedness were evaluated using Pearson correla- by exploiting weaknesses in the data that are not
tion,Spearmancorrelation,andMeanSquaredEr- likely to hold in future tasks of the same kind
ror (MSE). Pearson correlation was chosen as the (for instance, run 3 submitted by The Meaning
officialmeasuretoranktheparticipatingsystems. Factory exploited sentence ID ordering informa-
Table 5 presents the performance of 4 base- tion, but it was not presented as a primary run).
lines. The Majority baseline always assigns Participants could also use non-primary runs to
the most common label in the training data test smart baselines. In the relatedness subtask
(NEUTRAL), whereas the Probability baseline six non-primary runs slightly outperformed the
assigns labels randomly according to their rela- official winning primary entry,3 while in the
tive frequency in the training set. The Overlap entailment task all ECNU’s runs but run 4 were
baseline measures word overlap, again with better than ECNU’s primary run. Interestingly,
parameters (number of stop words and EN- the differences between the ECNU’s runs were
TAILMENT/NEUTRAL/CONTRADICTION
|             |           |        |          |             | 3They | were: | The Meaning | Factory’s | run3 | (Pearson |     |
| ----------- | --------- | ------ | -------- | ----------- | ----- | ----- | ----------- | --------- | ---- | -------- | --- |
| thresholds) | estimated | on the | training | part of the |       |       |             |           |      |          |     |
0.84170)ECNU’sruns2(0.83893)run5(0.83500)andStan-
data.
fordNLP’srun4(0.83462)andrun2(0.83103).
4

| duetothelearningmethodsused. |     |     |     |     |     |     | ID  |     |     | Compose |     | ACCURACY |     |
| ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | -------- | --- |
Wepresenttheresultsachievedbyprimaryruns
|     |     |     |     |     |     |     | Illinois-LH | run1 |     | P/S |     | 84.6 |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ---- | --- | --- | --- | ---- | --- |
againsttheEntailmentandRelatednesssubtasksin
|              |           |              | respectively.4 |           |         |            | ECNU        | run1    |      | S   |     | 83.6 |     |
| ------------ | --------- | ------------ | -------------- | --------- | ------- | ---------- | ----------- | ------- | ---- | --- | --- | ---- | --- |
| Table 6      | and Table | 7,           |                |           | We      | witnessed  |             |         |      |     |     |      |     |
| a very close | finish    | in           | both           | subtasks, | with    | 4 more     |             |         |      |     |     |      |     |
|              |           |              |                |           |         |            | UNAL-NLP    | run1    |      |     |     | 83.1 |     |
| systems      | within    | 3 percentage |                | points    | of      | the winner |             |         |      |     |     |      |     |
|              |           |              |                |           |         |            | SemantiKLUE |         | run1 |     |     | 82.3 |     |
| in both      | cases.    | 4 of         | these          | 5 top     | systems | were the   |             |         |      |     |     |      |     |
|              |           |              |                |           |         |            | The Meaning | Factory | run1 | S   |     | 81.6 |     |
| same across  | the       | two          | subtasks.      | Most      | systems | per-       |             |         |      |     |     |      |     |
formed well above the best baselines from Table CECL ALL run1 80.0
5.
|               |     |             |      |            |          |           | BUAP | run1 |     | P   |     | 79.7 |     |
| ------------- | --- | ----------- | ---- | ---------- | -------- | --------- | ---- | ---- | --- | --- | --- | ---- | --- |
| The overall   |     | performance |      | pattern    | suggests | that,     |      |      |     |     |     |      |     |
|               |     |             |      |            |          |           | UoW  | run1 |     |     |     | 78.5 |     |
| owing perhaps |     | to the      | more | controlled |          | nature of |      |      |     |     |     |      |     |
the sentences, as well as to the purely linguistic Uedinburgh run1 S 77.1
nature of the challenges it presents, SICK entail- UIO-Lien run1 77.0
| ment is    | “easier”    | than       | RTE.         | Considering |          | the first  |             |      |     |     |     |      |     |
| ---------- | ----------- | ---------- | ------------ | ----------- | -------- | ---------- | ----------- | ---- | --- | --- | --- | ---- | --- |
|            |             |            |              |             |          |            | FBK-TR      | run3 |     | P   |     | 75.4 |     |
| five RTE   | challenges  |            | (Bentivogli  |             | et al.,  | 2009), the |             |      |     |     |     |      |     |
|            |             |            |              |             |          |            | StanfordNLP | run5 |     | S   |     | 74.5 |     |
| median     | values      | ranged     | from         | 56.20%      |          | to 61.75%, |             |      |     |     |     |      |     |
|            |             |            |              |             |          |            | UTexas      | run1 |     | P/S |     | 73.2 |     |
| whereas    | the average |            | values       | ranged      | from     | 56.45%     |             |      |     |     |     |      |     |
| to 61.97%. | The         | entailment |              | scores      | obtained | on         |             |      |     |     |     |      |     |
|            |             |            |              |             |          |            | Yamraj      | run1 |     |     |     | 70.7 |     |
| the SICK   | data        | set are    | considerably |             | higher,  | being      |             |      |     |     |     |      |     |
|            |             |            |              |             |          |            | asjai run5  |      |     | S   |     | 69.8 |     |
| 77.06%     | for the     | median     | system       |             | and      | 75.36% for |             |      |     |     |     |      |     |
the average system. On the other hand, the re- haLF run2 S 69.4
latedness task is more challenging than the one RTM-DCU run1 67.2
| run on MSRvid |     | (one | of our  | data        | sources) | at STS   |             |     |      |     |     |      |     |
| ------------- | --- | ---- | ------- | ----------- | -------- | -------- | ----------- | --- | ---- | --- | --- | ---- | --- |
|               |     |      |         |             |          |          | UANLPCourse |     | run2 | S   |     | 48.7 |     |
| 2012, where   | the | top  | Pearson | correlation |          | was 0.88 |             |     |      |     |     |      |     |
(Agirreetal.,2012). Table 6: Primary run results for the entailment
|     |     |     |     |     |     |     | subtask. | The | table | also shows | whether | a   | sys- |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | ----- | ---------- | ------- | --- | ---- |
6 Approaches
temexploitscompositioninformationateitherthe
phrase(P)orsentence(S)level.
| A summary     | of        | the | approaches |           | used  | by the sys- |           |                 |     |          |     |             |     |
| ------------- | --------- | --- | ---------- | --------- | ----- | ----------- | --------- | --------------- | --- | -------- | --- | ----------- | --- |
| tems to       | address   | the | task is    | presented |       | in Table 8. |           |                 |     |          |     |             |     |
| In the table, | systems   |     | in bold    | are       | those | for which   |           |                 |     |          |     |             |     |
|               |           |     |            |           |       |             | tems that | compositionally |     | computed |     | the meaning |     |
| the authors   | submitted |     | a paper    | (Ferrone  |       | and Zan-    |           |                 |     |          |     |             |     |
ofthefullsentences,thoughnotnecessarilybyas-
| zotto, 2014; | Bjerva     |              | et al.,  | 2014;   | Beltagy | et al.,    |                  |                 |                           |                |           |              |      |
| ------------ | ---------- | ------------ | -------- | ------- | ------- | ---------- | ---------------- | --------------- | ------------------------- | -------------- | --------- | ------------ | ---- |
|              |            |              |          |         |         |            | signing          | meanings        | to                        | intermediate   | syntactic |              | con- |
| 2014; Lai    | and        | Hockenmaier, |          | 2014;   | Alves   | et al.,    |                  |                 |                           |                |           |              |      |
|              |            |              |          |         |         |            | stituents)       | and             | ‘partially                | compositional’ |           | (systems     |      |
| 2014; Leo´n  | et         | al., 2014;   | Bestgen, |         | 2014;   | Zhao et    |                  |                 |                           |                |           |              |      |
|              |            |              |          |         |         |            | that stop        | the composition |                           | at the         | level     | of phrases). |      |
| al., 2014;   | Vo         | et al.,      | 2014;    | Bic¸ici | and     | Way, 2014; |                  |                 |                           |                |           |              |      |
|              |            |              |          |         |         |            | Asthetableshows, |                 | thirteensystemsusedcompo- |                |           |              |      |
| Lien and     | Kouylekov, |              | 2014;    | Jimenez | et      | al., 2014; |                  |                 |                           |                |           |              |      |
sitioninatleastoneofthetasks;tenusedcompo-
| ProislandEvert,2014;Guptaetal.,2014). |     |     |     |     |     | Forthe |            |                |     |         |     |          |       |
| ------------------------------------- | --- | --- | --- | --- | --- | ------ | ---------- | -------------- | --- | ------- | --- | -------- | ----- |
|                                       |     |     |     |     |     |        | sition for | full sentences |     | and six | for | phrases, | only. |
others,weusedthebriefdescriptionsentwiththe
|                  |     |                               |     |     |     |     | The best | systems | are | among | these | thirteen | sys- |
| ---------------- | --- | ----------------------------- | --- | --- | --- | --- | -------- | ------- | --- | ----- | ----- | -------- | ---- |
| system’sresults, |     | double-checkingtheinformation |     |     |     |     |          |         |     |       |       |          |      |
tems.
| with the | authors. | In  | the table, | “E” | and | “R” refer |        |       |         |               |     |          |     |
| -------- | -------- | --- | ---------- | --- | --- | --------- | ------ | ----- | ------- | ------------- | --- | -------- | --- |
|          |          |     |            |     |     |           | Let us | focus | on such | compositional |     | methods. |     |
totheentailmentandrelatednesstaskrespectively,
|     |     |     |     |     |     |     | Concerning | the | relatedness | task, | the | fine-grained |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ----------- | ----- | --- | ------------ | --- |
and“B”toboth.
|        |     |         |         |     |         |          | analyses | reported | for | several | systems | (Illinois- |     |
| ------ | --- | ------- | ------- | --- | ------- | -------- | -------- | -------- | --- | ------- | ------- | ---------- | --- |
| Almost | all | systems | combine |     | several | kinds of |          |          |     |         |         |            |     |
LH,TheMeaningFactoryandECNU)showsthat
| features. | To  | highlight | the | role | played | by com- |     |     |     |     |     |     |     |
| --------- | --- | --------- | --- | ---- | ------ | ------- | --- | --- | --- | --- | --- | --- | --- |
purelycompositionalsystemscurrentlyreachper-
| position, | we draw               | a    | distinction |                | between   | compo-  |               |             |         |             |             |             |     |
| --------- | --------------------- | ---- | ----------- | -------------- | --------- | ------- | ------------- | ----------- | ------- | ----------- | ----------- | ----------- | --- |
|           |                       |      |             |                |           |         | formance      | above       | 0.7     | r. In       | particular, | ECNU’s      |     |
| sitional  | and non-compositional |      |             |                | features, | and di- |               |             |         |             |             |             |     |
|           |                       |      |             |                |           |         | compositional |             | feature | gives 0.75  | r,          | The Meaning |     |
| vide the  | former                | into | ‘fully      | compositional’ |           | (sys-   |               |             |         |             |             |             |     |
|           |                       |      |             |                |           |         | Factory’s     | logic-based |         | composition |             | model 0.73  | r,  |
4ITTK’sprimaryruncouldnotbeevaluatedduetotech- and Illinois-LH compositional features combined
| nical problems | with | the | submission. | The | best | ITTK’s non- |           |         |      |     |       |              |     |
| -------------- | ---- | --- | ----------- | --- | ---- | ----------- | --------- | ------- | ---- | --- | ----- | ------------ | --- |
|                |      |     |             |     |      |             | with Word | Overlap | 0.75 | r.  | While | competitive, |     |
primaryrunscored78,2%accuracyintheentailmenttaskand
|     |     |     |     |     |     |     | these scores | are | lower | than the | one | of the | best |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ----- | -------- | --- | ------ | ---- |
0.76rintherelatednesstask.
5

ID Compose r ρ MSE els’, ‘Topic Models’ and ‘Neural Language Mod-
els’. Duetotheimpactshownbylearningmethods
| ECNUrun1        |     | S   |     | 0.828 0.769 | 0.325 |             |     |           |         |        |     |           |
| --------------- | --- | --- | --- | ----------- | ----- | ----------- | --- | --------- | ------- | ------ | --- | --------- |
|                 |     |     |     |             |       | (see ECNU’s |     | results), | we also | report | the | different |
| StanfordNLPrun5 |     | S   |     | 0.827 0.756 | 0.323 |             |     |           |         |        |     |           |
learningapproachesused.
| TheMeaningFactoryrun1 |     | S   |     | 0.827 0.772 | 0.322 |         |               |     |         |     |              |     |
| --------------------- | --- | --- | --- | ----------- | ----- | ------- | ------------- | --- | ------- | --- | ------------ | --- |
|                       |     |     |     |             |       | Several | participating |     | systems |     | deliberately | ex- |
| UNAL-NLPrun1          |     |     |     | 0.804 0.746 | 0.359 |         |               |     |         |     |              |     |
ploitad-hocfeaturesthat,whilenothelpingatrue
| Illinois-LHrun1 |     | P/S |     | 0.799 0.754 | 0.369 |                |                 |             |             |          |          |           |
| --------------- | --- | --- | --- | ----------- | ----- | -------------- | --------------- | ----------- | ----------- | -------- | -------- | --------- |
|                 |     |     |     |             |       | understanding  |                 | of sentence |             | meaning, | exploit  | some      |
| CECLALLrun1     |     |     |     | 0.780 0.732 | 0.398 |                |                 |             |             |          |          |           |
|                 |     |     |     |             |       | systematic     | characteristics |             | of          | SICK     | that     | should be |
|                 |     |     |     |             |       | controlled     | for             | in future   | releases    |          | of the   | data set. |
| SemantiKLUErun1 |     |     |     | 0.780 0.736 | 0.403 |                |                 |             |             |          |          |           |
|                 |     |     |     |             |       | In particular, |                 | the Textual | Entailment  |          | subtask  | has       |
| RTM-DCUrun1     |     |     |     | 0.764 0.688 | 0.429 |                |                 |             |             |          |          |           |
|                 |     |     |     |             |       | been shown     | to              | rely        | too much    | on       | negative | words     |
| UTexasrun1      |     | P/S |     | 0.714 0.674 | 0.499 |                |                 |             |             |          |          |           |
|                 |     |     |     |             |       | and antonyms.  |                 | The         | Illinois-LH | team     | reports  | that,     |
| UoWrun1         |     |     |     | 0.711 0.679 | 0.511 |                |                 |             |             |          |          |           |
|                 |     |     |     |             |       | just by        | checking        | the         | presence    | of       | negative | words     |
| FBK-TRrun3      |     | P   |     | 0.709 0.644 | 0.591 |                |                 |             |             |          |          |           |
(theNegationFeatureinthetable),onecandetect
| BUAPrun1 |     | P   |     | 0.697 0.645 | 0.528 |          |     |               |     |        |        |         |
| -------- | --- | --- | --- | ----------- | ----- | -------- | --- | ------------- | --- | ------ | ------ | ------- |
|          |     |     |     |             |       | 86.4% of | the | contradiction |     | pairs, | and by | combin- |
UANLPCourserun2 S 0.693 0.603 0.542 ing Word Overlap and antonyms one can detect
UQeResearchrun1 0.642 0.626 0.822 83.6% of neutral pairs and 82.6% of entailment
ASAPrun1 P 0.628 0.597 0.662 pairs. This approach, however, is obviously very
Yamrajrun1 0.535 0.536 2.665 brittle (it would not have been successful, for in-
|                  |     |         |     |             |             | stance,               | if negation | had | been   | optionally |     | combined |
| ---------------- | --- | ------- | --- | ----------- | ----------- | --------------------- | ----------- | --- | ------ | ---------- | --- | -------- |
| asjairun5        |     | S       |     | 0.479 0.461 | 1.104       |                       |             |     |        |            |     |          |
|                  |     |         |     |             |             | with word-rearranging |             |     | in the | creation   | of  | S4 sen-  |
| Table 7: Primary | run | results | for | the         | relatedness |                       |             |     |        |            |     |          |
tences,seeSection3.1above).
| subtask (r | for Pearson | and | ρ for | Spearman | corre- |     |     |     |     |     |     |     |
| ---------- | ----------- | --- | ----- | -------- | ------ | --- | --- | --- | --- | --- | --- | --- |
Finally,Table8reportsabouttheuseofexternal
lation). Thetablealsoshowswhetherasystemex-
|     |     |     |     |     |     | resources | in the | task. | One | of the | reasons | we cre- |
| --- | --- | --- | --- | --- | --- | --------- | ------ | ----- | --- | ------ | ------- | ------- |
ploitscompositioninformationateitherthephrase
atedSICKwastohaveacompositionalsemantics
(P)orsentence(S)level.
|                          |     |     |        |            |     | benchmark    | that         | would     | not          | require      | too        | many ex- |
| ------------------------ | --- | --- | ------ | ---------- | --- | ------------ | ------------ | --------- | ------------ | ------------ | ---------- | -------- |
|                          |     |     |        |            |     | ternal tools | and          | resources | (e.g.,       | named-entity |            | rec-     |
|                          |     |     |        |            |     | ognizers,    | gazetteers,  |           | ontologies). |              | By looking | at       |
| purely non-compositional |     |     | system | (UNAL-NLP) |     |              |              |           |              |              |            |          |
|                          |     |     |        |            |     | what the     | participants |           | chose        | to use,      | we         | think we |
whichreachesthe4thposition(0.80rUNAL-NLP
|            |          |        |      |          |       | succeeded, | as  | only | standard | NLP | pre-processing |     |
| ---------- | -------- | ------ | ---- | -------- | ----- | ---------- | --- | ---- | -------- | --- | -------------- | --- |
| vs. 0.82 r | obtained | by the | best | system). | UNAL- |            |     |      |          |     |                |     |
tools(tokenizers,PoStaggersandparsers)andrel-
| NLP however | exploits | an  | ad-hoc | “negation” | fea- |         |               |     |           |     |          |       |
| ----------- | -------- | --- | ------ | ---------- | ---- | ------- | ------------- | --- | --------- | --- | -------- | ----- |
|             |          |     |        |            |      | atively | few knowledge |     | resources |     | (mostly, | Word- |
turediscussedbelow.
Netandparaphrasecorpora)wereused.
| In the        | entailment | task, |        | the       | best non- |     |     |     |     |     |     |     |
| ------------- | ---------- | ----- | ------ | --------- | --------- | --- | --- | --- | --- | --- | --- | --- |
| compositional | model      |       | (again | UNAL-NLP) |           |     |     |     |     |     |     |     |
7 Conclusion
reachesthe3rdposition,withinclosereachofthe
bestsystem(83%UNAL-NLPvs.84.5%obtained We presented the results of the first task on the
by the best system). Again, purely compositional evaluation of compositional distributional seman-
models have lower performance. haLF CDSM ticmodelsandothersemanticsystemsonfullsen-
reaches 69.42% accuracy, Illinois-LH Word tences,organizedwithinSemEval-2014. Twosub-
| Overlap combined |     | with a | compositional |     | feature |                   |     |     |                             |     |     |     |
| ---------------- | --- | ------ | ------------- | --- | ------- | ----------------- | --- | --- | --------------------------- | --- | --- | --- |
|                  |     |        |               |     |         | taskswereoffered: |     |     | (i)predictingthedegreeofre- |     |     |     |
reaches71.8%. Thefine-grainedanalysisreported latedness between two sentences, and (ii) detect-
by Illinois-LH (Lai and Hockenmaier, 2014) ingtheentailmentrelationholdingbetweenthem.
shows that a full compositional system (based The task has raised noticeable attention in the
on point-wise multiplication) fails to capture community: 17 and 18 submissions for the relat-
contradiction. Itisbetterthanpartialphrase-based ednessandentailmentsubtasks,respectively,fora
compositional models in recognizing entailment total of 21 participating teams. Participation was
| pairs, but worse | than | them | on recognizing |     | neutral |     |     |     |     |     |     |     |
| ---------------- | ---- | ---- | -------------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
notlimitedtocompositionalmodelsbutthemajor-
| pairs. |     |     |     |     |     | ityofsystems(13/21)usedcompositioninatleast |     |     |     |     |     |     |
| ------ | --- | --- | --- | --- | --- | ------------------------------------------- | --- | --- | --- | --- | --- | --- |
Given our more general interest in the distri- one of the subtasks. Moreover, the top-ranking
butional approaches, in Table 8 we also classify systems in both tasks use compositional features.
the different DSMs used as ‘Vector Space Mod- However,itmustbenotedthatallsystemsalsoex-
6

Comp
Participant ID Non composition features Learning Methods External Resources
features
ledoM scitnameS
rotceV
ledoM
cipoT
ledoM egaugnaL
larueN
ledoM lanoitatoneD palrevO
droW
ytiralimiS
droW
serutaeF
citcatnyS
ecnereffid
ecnetneS
serutaeF
noitageN
noitisopmoC
ecnetneS
noitisopmoc
esarhP
sdohtem lenreK
dna
MVS
sruobhgieN
tseraeN-K
noitanibmoC
reifissalC
tseroF
modnaR
LoF citsilibaborP/LoF gninrael desab
mulucirruC
rehtO teNdroW BD sesarhparaP aroproC
rehtO
rekcilFegamI oediV-RSM
STS
noitpircseD
ASAP R R R R R R R R R
ASJAI B B B B B B B B E B R B
BUAP B B B B E B E B
UEdinburgh B B B B B E R B
CECL B B B B B B
ECNU B B B B B B B B B B B B B
FBK-TR R R R E B E E B R E R R E
haLF E E E E
IITK B B B B B B B B B
Illinois-LH B B B B B B B B B B B B
RTM-DCU B B B B B
SemantiKLUE B B B B B B B B
StandfordNLP B B R R R B E
The Meaning Factory R R R R R R B E R E B B R
UANLPCourse B B B B B
UIO-Lien E E
UNAL-NLP B B B B R B B
UoW B B B B B B
UQeRsearch R R R R R R R
UTexas B B B B B B B
Yamarj B B B B
Table8: SummaryofthemaincharacteristicsoftheparticipatingsystemsonR(elatedness),E(ntailment)
orB(oth)
ploitnon-compositionalfeaturesandmostofthem References
use external resources, especially WordNet. Al-
Eneko Agirre, Daniel Cer, Mona Diab, and Aitor
most all the participating systems outperformed Gonzalez-Agirre. 2012. Semeval-2012task6:Api-
theproposedbaselinesinbothtasks. Furtheranal- lotonsemantictextualsimilarity. InProceedingsof
yses carried out by some participants in the task theSixthInternationalWorkshoponSemanticEval-
uation(SemEval2012),volume2.
show that purely compositional approaches reach
accuracy above 70% in entailment and 0.70 r for Ana O. Alves, Adirana Ferrugento, Mariana Lorenc¸o,
relatedness. Thesescoresarecomparablewiththe andFilipeRodrigues. 2014. ASAP:Automaticase-
manticalignmentforphrases. InProceedingsofSe-
averageresultsobtainedinthetask.
mEval 2014: International Workshop on Semantic
Evaluation.
Acknowledgments Marco Baroni and Roberto Zamparelli. 2010. Nouns
are vectors, adjectives are matrices: Representing
adjective-noun constructions in semantic space. In
We thank the creators of the ImageFlickr, MSR- ProceedingsofEMNLP,pages1183–1193,Boston,
MA.
Video,andSemEval-2012STSdatasetsforgrant-
inguspermissiontousetheirdataforthetask. The IslamBeltagy,StephenRoller,GemmaBoleda,Katrin
University of Trento authors were supported by Erk, and Raymon J. Mooney. 2014. UTexas: Nat-
ERC 2011 Starting Independent Research Grant urallanguagesemanticsusingdistributionalseman-
tics and probablisitc logic. In Proceedings of Se-
n.283554(COMPOSES).
mEval 2014: International Workshop on Semantic
Evaluation.
7

LuisaBentivogli,IdoDagan,HoaT.Dang,DaniloGi- Elisabeth Lien and Milen Kouylekov. 2014. UIO-
ampiccolo,andBernardoMagnini. 2009. Thefifth Lien: Entailment recognition using minimal recur-
PASCAL recognizing textual entailment challenge. sion semantics. In Proceedings of SemEval 2014:
InTheTextAnalysisConference(TAC2009). InternationalWorkshoponSemanticEvaluation.
YvesBestgen. 2014. CECL:anewbaselineandanon- Marco Marelli, Stefano Menini, Marco Baroni, Luisa
compositionalapproachfortheSickbenchmark. In Bentivogli, Raffaella Bernardi, and Roberto Zam-
ProceedingsofSemEval2014: InternationalWork- parelli. 2014. A SICK cure for the evaluation of
shoponSemanticEvaluation. compositional distributional semantic models. In
ProceedingsofLREC,Reykjavik.
| Ergun Bic¸ici | and | Andy Way. | 2014. | RTM-DCU: |     | Ref- |     |     |     |     |     |     |
| ------------- | --- | --------- | ----- | -------- | --- | ---- | --- | --- | --- | --- | --- | --- |
erential translation machines for semantic similar- JeffMitchellandMirellaLapata. 2008. Vector-based
|                                  |     |     |     |     |               |     | modelsofsemanticcomposition. |     |     |     | InProceedingsof |     |
| -------------------------------- | --- | --- | --- | --- | ------------- | --- | ---------------------------- | --- | --- | --- | --------------- | --- |
| ity. InProceedingsofSemEval2014: |     |     |     |     | International |     |                              |     |     |     |                 |     |
ACL,pages236–244,Columbus,OH.
WorkshoponSemanticEvaluation.
|          |         |            |     |     |           |     | Jeff Mitchell | and | Mirella | Lapata. | 2010. | Composition |
| -------- | ------- | ---------- | --- | --- | --------- | --- | ------------- | --- | ------- | ------- | ----- | ----------- |
| Johannes | Bjerva, | Johan Bos, | Rob | van | der Goot, | and |               |     |         |         |       |             |
MalvinaNissim. 2014. TheMeaningFactory: For- indistributionalmodelsofsemantics. CognitiveSci-
mal Semantics for Recognizing Textual Entailment ence,34(8):1388–1429.
| and Determining |            | Semantic | Similarity.   |     | In       | Proceed- |        |        |            |            |             |           |
| --------------- | ---------- | -------- | ------------- | --- | -------- | -------- | ------ | ------ | ---------- | ---------- | ----------- | --------- |
|                 |            |          |               |     |          |          | Thomas | Proisl | and Stefan | Evert.     | 2014.       | SemantiK- |
| ings            | of SemEval | 2014:    | International |     | Workshop | on       |        |        |            |            |             |           |
|                 |            |          |               |     |          |          | LUE:   | Robust | semantic   | similarity | at multiple | levels    |
SemanticEvaluation.
|     |     |     |     |     |     |     | usingmaximumweightmatching. |     |     |     | InProceedingsof |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------------- | --- | --- | --- | --------------- | --- |
SemEval2014:InternationalWorkshoponSemantic
| Ido Dagan, | Oren                                  | Glickman, | and      | Bernardo    |     | Magnini. |             |         |              |             |     |          |
| ---------- | ------------------------------------- | --------- | -------- | ----------- | --- | -------- | ----------- | ------- | ------------ | ----------- | --- | -------- |
| 2006.      | ThePASCALrecognisingtextualentailment |           |          |             |     |          | Evaluation. |         |              |             |     |          |
| challenge. | In                                    | Machine   | learning | challenges. |     | Evalu-   |             |         |              |             |     |          |
|            |                                       |           |          |             |     |          | Richard     | Socher, | Brody Huval, | Christopher |     | Manning, |
atingpredictiveuncertainty,visualobjectclassifica-
|     |     |     |     |     |     |     | and Andrew |     | Ng. 2012. | Semantic | compositionality |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --------- | -------- | ---------------- | --- |
tion,andrecognisingtextualentailment,pages177–
|     |     |     |     |     |     |     | throughrecursivematrix-vectorspaces. |     |     |     |     | InProceed- |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------ | --- | --- | --- | --- | ---------- |
190.Springer.
ingsofEMNLP,pages1201–1211,JejuIsland,Ko-
rea.
| Lorenzo | Ferrone | and Fabio | Massimo | Zanzotto. |     | 2014. |     |     |     |     |     |     |
| ------- | ------- | --------- | ------- | --------- | --- | ----- | --- | --- | --- | --- | --- | --- |
haLF:comparingapureCDSMapproachandastan-
AnN.P.Vo,OctavianPopescu,andTommasoCaselli.
| dard | ML system | for RTE. |     | In Proceedings |     | of Se- |     |     |     |     |     |     |
| ---- | --------- | -------- | --- | -------------- | --- | ------ | --- | --- | --- | --- | --- | --- |
2014. FBK-TR:SVMforSemanticRelatednessand
| mEval | 2014: | International | Workshop |     | on  | Semantic |        |          |          |     |             |        |
| ----- | ----- | ------------- | -------- | --- | --- | -------- | ------ | -------- | -------- | --- | ----------- | ------ |
|       |       |               |          |     |     |          | Corpus | Patterns | for RTE. | In  | Proceedings | of Se- |
Evaluation.
|     |     |     |     |     |     |     | mEval | 2014: | International | Workshop |     | on Semantic |
| --- | --- | --- | --- | --- | --- | --- | ----- | ----- | ------------- | -------- | --- | ----------- |
Evaluation.
| EdwardGrefenstetteandMehrnooshSadrzadeh. |     |         |       |             |            | 2011.    |             |      |           |        |          |            |
| ---------------------------------------- | --- | ------- | ----- | ----------- | ---------- | -------- | ----------- | ---- | --------- | ------ | -------- | ---------- |
| Experimental                             |     | support | for a | categorical |            | composi- |             |      |           |        |          |            |
|                                          |     |         |       |             |            |          | Jiang Zhao, | Tian | Tian Zhu, | and    | Man      | Lan. 2014. |
| tionaldistributionalmodelofmeaning.      |     |         |       |             | InProceed- |          |             |      |           |        |          |            |
|                                          |     |         |       |             |            |          | ECNU:       | One  | Stone Two | Birds: | Ensemble | of Het-    |
ingsofEMNLP,pages1394–1404,Edinburgh,UK. erogenous Measures for Semantic Relatedness and
|                   |                               |       |                      |     |     |     | Textual | Entailment.   | In       | Proceedings |             | of SemEval |
| ----------------- | ----------------------------- | ----- | -------------------- | --- | --- | --- | ------- | ------------- | -------- | ----------- | ----------- | ---------- |
| RohitGupta,       | IsmailElMaaroufHannahBechara, |       |                      |     |     | and |         |               |          |             |             |            |
|                   |                               |       |                      |     |     |     | 2014:   | International | Workshop |             | on Semantic | Evalu-     |
| CostantinOrasaˇn. |                               | 2014. | UoW:NLPtechniquesde- |     |     |     |         |               |          |             |             |            |
ation.
velopedattheUniversityofWolverhamptonforSe-
| mantic                 | Similarity | and | Textual               | Entailment. |     | In Pro- |     |     |     |     |     |     |
| ---------------------- | ---------- | --- | --------------------- | ----------- | --- | ------- | --- | --- | --- | --- | --- | --- |
| ceedingsofSemEval2014: |            |     | InternationalWorkshop |             |     |         |     |     |     |     |     |     |
onSemanticEvaluation.
| Sergio Jimenez, |          | George | Duenas,   | Julia | Baquero, | and     |     |     |     |     |     |     |
| --------------- | -------- | ------ | --------- | ----- | -------- | ------- | --- | --- | --- | --- | --- | --- |
| Alexander       | Gelbukh. | 2014.  | UNAL-NLP: |       |          | Combin- |     |     |     |     |     |     |
ingsoftcardinalityfeaturesforsemantictextualsim-
| ilarity,   | relatedness | and                 | entailment. |          | In Proceedings |        |     |     |     |     |     |     |
| ---------- | ----------- | ------------------- | ----------- | -------- | -------------- | ------ | --- | --- | --- | --- | --- | --- |
| of SemEval |             | 2014: International |             | Workshop |                | on Se- |     |     |     |     |     |     |
manticEvaluation.
| AliceLaiandJuliaHockenmaier. |     |                    |     | 2014.    | Illinois-lh: | A      |     |     |     |     |     |     |
| ---------------------------- | --- | ------------------ | --- | -------- | ------------ | ------ | --- | --- | --- | --- | --- | --- |
| denotational                 |     | and distributional |     | approach | to           | seman- |     |     |     |     |     |     |
tics. InProceedingsofSemEval2014:International
WorkshoponSemanticEvaluation.
| Sau´l Leo´n, | Darnes   | Vilarino, | David | Pinto,          | Mireya | To- |     |     |     |     |     |     |
| ------------ | -------- | --------- | ----- | --------------- | ------ | --- | --- | --- | --- | --- | --- | --- |
| var, and     | Beatrice | Beltra´n. | 2014. | BUAP:evaluating |        |     |     |     |     |     |     |     |
compositionaldistributionalsemanticmodelsonfull
| sentences   | through                     | semantic | relatedness |     | and | textual |     |     |     |     |     |     |
| ----------- | --------------------------- | -------- | ----------- | --- | --- | ------- | --- | --- | --- | --- | --- | --- |
| entailment. | InProceedingsofSemEval2014: |          |             |     |     | Inter-  |     |     |     |     |     |     |
nationalWorkshoponSemanticEvaluation.
8
