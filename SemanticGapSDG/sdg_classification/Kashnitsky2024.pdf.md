RESEARCH ARTICLE
Evaluating approaches to identifying research
supporting the United Nations Sustainable
Development Goals
YuryKashnitsky1 ,GuillaumeRoberge2 ,JingwenMu3 ,KevinKang3 ,WeiweiWang3 ,
MauriceVanderfeesten4 ,MaximeRivest2,5 ,SavvasChamezopoulos1 ,RobertJaworek6 ,
an open access journal Maéva Vignes7 , BaminiJayabalasingham1,8 ,Finne Boonen1 , ChrisJames1 ,
Marius Doornenbal1 , andIsabelle Labrosse2
1ElsevierBV,Amsterdam,Netherlands
2ElsevierBV,Montreal,Canada
3TheUniversityofAucklandFacultyofScience,Auckland,NewZealand
4VrijeUniversiteitAmsterdam,Amsterdam,Netherlands
5McGillUniversity,Montreal,Canada
Citation:Kashnitsky,Y.,Roberge,G., 6PalackyUniversityOlomouc,Olomouc,CzechRepublic
Mu,J.,Kang,K.,Wang,W.,
Vanderfeesten,M.,Rivest,M., 7UniversityofSouthernDenmark,Odense,Denmark
Chamezopoulos,S.,Jaworek,R., 8ElsevierBV,NewYork,NY,USA
Vignes,M.,Jayabalasingham,B.,
Boonen,F.,James,C.,Doornenbal,M.,
&Labrosse,I.(2024).Evaluating
approachestoidentifyingresearch Keywords: benchmarking, bibliometrics, machine learning, scientometrics, sustainability,
supportingtheUnitedNations
SustainableDevelopmentGoals. SustainableDevelopment Goals
QuantitativeScienceStudies,5(2),
408–425.https://doi.org/10.1162
/qss_a_00304
ABSTRACT
DOI:
https://doi.org/10.1162/qss_a_00304
The United Nations (UN) Sustainable Development Goals (SDGs) challenge the global
PeerReview: community to build a world where no one is left behind. Recognizing that research plays a
https://www.webofscience.com/api
/gateway/wos/peer-review/10.1162 fundamental part in supporting these goals, attempts have been made to classify research
/qss_a_00304 publicationsaccordingtotheirrelevanceinsupportingeachoftheUN’sSDGs.Inthispaper,
SupportingInformation: we outline the methodology that we followed when mapping research articles to SDGs and
https://doi.org/10.1162/qss_a_00304
which is adopted by Times Higher Education in its Social Impact rankings. We compare our
Received:1May2023 solution with other existing queries and models mapping research papers to SDGs. We also
Accepted:28January2024
discussvariousaspectsinwhichthemethodologycanbeimprovedandgeneralizedtoother
types of content apart from research articles. The results presented in this paper are the
CorrespondingAuthor:
YuryKashnitsky outcome of the SDG Research Mapping Initiative, which was established as a partnership y.kashnitskiy@elsevier.com
between the University of Southern Denmark, the Aurora European Universities Alliance
HandlingEditor: (represented by Vrije Universiteit Amsterdam), the University of Auckland, and Elsevier to
VincentLarivière
bringtogetherbroadexpertiseandsharebestpracticesonidentifyingresearchcontributionsto
UN’s Sustainable Development Goals.
Copyright:©2024YuryKashnitsky,
GuillaumeRoberge,JingwenMu,Kevin
Kang,WeiweiWang,Maurice 1. INTRODUCTION
Vanderfeesten,MaximeRivest,Savvas
Chamezopoulos,RobertJaworek, NumerousapproachestomappingresearchtotheUnitedNations(UN)SustainableDevelop-
MaévaVignes,Bamini
Jayabalasingham,FinneBoonen,Chris ment Goals (SDGs)1 have been documented (Armitage, Lorenz, & Mikki, 2020b; Bordignon,
James,MariusDoornenbal,and
2021; Confraria, Ciarli, & Noyons, 2022; Jayabalasingham, Boverhof et al., 2019; LaFleur,
IsabelleLabrosse.Publishedundera
CreativeCommonsAttribution4.0 2019). These approaches vary with regard to the framework used to define inclusion and
International(CCBY4.0)license.
1 https://metadata.un.org/sdg/.
TheMITPress
Downloaded
from
http://direct.mit.edu/qss/article-pdf/5/2/408/2376617/qss_a_00304.pdf
by
guest
on
07
June
2026

Identifying research supporting the United Nations Sustainable Development Goals
exclusion criteria, the methodology employed to retrieve publications, and the publication
database used. For example, the approach to defining inclusion and exclusion criteria may
be set conservatively to limit publications to those documenting actions made to achieve
the SDG targets, or conversely, may be set using a more liberal approach, thereby including
any papers that increase knowledge on the overall topic. With regard to the methodology
employed to retrieve publications, publication sets for a specific SDG can use a Boolean
approach only or be complemented by machine learning algorithms.
Thesourceofpublicationsthatthemethodologyisappliedtocanalsointroducevariability,
giventheavailabilityofmanydatasources,rangingfromopenaccess,subscription-based,ora
mixture of both.
To date, there is no broadly agreed-upon methodology for mapping research to the SDGs
and existing methods produce quite different results (Armitage et al., 2020b). A common
approach to identifying research related to a topic is to use Boolean search expressions.
The Boolean method involves the use of keywords, either alone or in combination, using
conditional functions and applied to specified text sections (title, abstracts, keywords, etc.)
of scientific publications, and results in the exclusive retrieval of articles within which the
definedsearchexpressionswerefound.Armitageetal.(2020b)appliedtheBooleanmethod,
taking an approach to limit their SDG publication sets to publications with a direct contri-
butiontotargetsand/or indicators,witheffortsmadetoreducetheimpactofissuesraisedon
the Boolean technique, resulting in a more restrictive publication set. Bordignon’s strategy
(Bordignon, 2021) aimed at reducing the polysemy of terms by limiting keywords from
Elsevier 2020 queries (Jayabalasingham et al., 2019) to relevant subject areas using the
All-Science Journal Classification (ASJC). A text-mining tool (CorTexT) was then used to
enrich those selected publications. The Aurora European Universities Alliance (Schmidt &
Vanderfeesten,2021)developedandreleasedtheir169target-levelSDGqueries(Vanderfeesten,
Otten, & Spielberg, 2020) also using keyword combinations and Boolean- and proximity
operators. The University of Auckland (Jingwen & Weiwei, 2022) developed queries
informed by the researchers within their network, resulting in a localized version that takes
into account more papers that are specific to Australian and New Zealand research topics.
Confrariaetal.(2021)employedatwo-stepapproach,involvingbuildingSDG-specificterms
obtained from many sources (policy reports, publications, forums, etc.), applying a selection
processtotheterms,andthenusingthetermstoidentifycitation-basedcommunitiesofpub-
lications.However,asdescribedbyArmitageetal.(2020b),suchakeyword-basedapproach
involves challenges related to the interpretation of the themes and concepts of the SDGs,
decisions around which publications to designate as a “contribution” to the chosen interpre-
tation of the SDG, and the translation of concepts into a search query that will accurately
identify publications.
An alternative or complementary approach to query-based methods involves using
machine learning to map research articles to SDGs: either in a supervised manner (i.e., per-
forming classification) or an unsupervised manner (i.e., performing clustering). Supervised
methods typically resort to the same SDG queries to obtain a labeled data set to train the
model(SouthAfricanSDGHub,2023;Zhang,Vignesetal.,2020).Clusteringistypicallydone
withpapertextrepresentationsorcitationgraphswheretheresultingclustersarelatermapped
toSDGseitherdirectlyorviaintermediateclusters(e.g.,“topics”;Nakamura,Pendleburyetal.,
2019; Wastl, Porter et al., 2020). Refer to Pukelis, Puig et al. (2020) for an overview of some
more methods of classifying documents into SDGs. However, they all face the same chal-
lenges noted above, and machine learning further introduces the problem of interpretability
of the model predictions or the clusters attained.
Quantitative Science Studies 409
Downloaded
from
http://direct.mit.edu/qss/article-pdf/5/2/408/2376617/qss_a_00304.pdf
by
guest
on
07
June
2026

Identifying research supporting the United Nations Sustainable Development Goals
Since2018,ElsevierhasendeavoredtomapresearchtotheSDGs,releasingpubliclyavail-
able queries to facilitate transparency and reproducibility (Jayabalasingham et al., 2019).
Herein, we describe the approach taken to improve former attempts to map research to the
SDGs,takingfeedbackintoaccount,resultinginthecreationofamorecomprehensivequery
setwithsubqueriesaddressingtargetsandindicatorsandtheapplicationofamachinelearning
modeltoincreaserecall.Thismethodology(“Elsevier2021SDGmapping”:Rivest,Kashnitsky
et al. (2021)) captures on average twice as many articles as the 2020 version, while keeping
precisionabove80%.TimesHigherEducation(THE)isusingElsevierSDGmappingaspartof
itsSocialImpactrankings(Ross,2022).“Elsevier2023SDGmapping”(Bedard-Vallee,James,
&Roberge,2023)isthemostup-to-datesimplifiedversionofthequeries&MLmodel,differing
fromthe2021versioninCOVID-relatedenhancementtoSDG3queriesandqueriesdesigned
for SDG 17: “Partnerships for the goals.”
To evaluate the approach, the output generated using the developed methodology was
compared to the results generated by Aurora European Universities Alliance (Vanderfeesten
& Jaworek, 2022), the University of Auckland (Jingwen & Weiwei, 2022), the University of
Bergen(Armitageetal.,2020b),SIRISAcademic(Duran-Silva,Fusteretal.,2019),Bordignon
queries(Bordignon,2021),andtheMLclassifierbytheSouth-AfricanSDGHub(SouthAfrican
SDG Hub, 2023).
We have not seen much research aimed at doing similar benchmarking of different SDG
mappingapproacheswithhand-labeleddatasets.Wulff,Meier,andMata(2023)istheclosest
investigationtoours:Apartfrombenchmarking,theauthorsexploretheextenttowhichSDG
queries produce false positives by marking non-SDG-related content with SDG labels. They
also investigate the bias in SDG labeling systems defined as the normalized difference in the
number of predicted and observed (i.e., put by human experts) SDG labels.
The novel contributions of this paper can be summarized as follows:
(cid:129) Wesolvetheproblemofrecallassessmentforkeywordqueriesmappingresearcharticles
toSustainableDevelopmentGoals,whileotherapproachestypicallyfocusonprecision.
(cid:129) We are among the first to quantitively evaluate existing sets of such keyword queries
against several validation data sets.
2. METHODOLOGY
2.1. DevelopingSDGQueries
The SDGs are goals to achieve rather than research topics, each SDG encompassing many
targets. Using Boolean search expressions to build SDG-specific publication sets presents
many challenges. Elsevier implemented a bottom-up approach to the construction of each
SDG-relevant publication set, whereby several subqueries were first constructed for each
SDG target, and then aggregated at the SDG level.
2.1.1. BuildingaqueryforeachtargetwithinanSDG
ThecriteriafordelineatingthepublicationsetsrelevanttoeachSDGweredesignedbyateam
consisting of a minimum of four analysts and were based on an extensive literature review
done by the team to gain an understanding of the SDG. As a first step, the SDG was further
subdividedintothemestofacilitatethecreationofspecificcriterialinkedtospecificSDGtar-
gets. The criteria defined for each theme aimed to specify topics of focus as well as any
requirements for “action terms” in association with the topics (Armitage et al., 2020b). For
Quantitative Science Studies 410
Downloaded
from
http://direct.mit.edu/qss/article-pdf/5/2/408/2376617/qss_a_00304.pdf
by
guest
on
07
June
2026

Identifying research supporting the United Nations Sustainable Development Goals
example, for the topic of “poverty” the action term “alleviate,” or other action terms holding
similarmeaningmightbedeemedarequirement.Toensurehomogeneityintheapproach,the
criteriadevelopedbytheteamofanalystsweresubmittedtoareviewcommitteeconsistingof
both those on the SDG team and those external to the team. The review committee was
responsible for reviewing the criteria, recommending changes, and final approval of the cri-
teria.Table1presentsthecriteriaforSDG1overall(SDG1-Main)andsubcategoriesrelatedto
|     |     |     |     | SDG1. | These criteria | were | defined | for each SDG and theme | related to | the SDG. |     |
| --- | --- | --- | --- | ----- | -------------- | ---- | ------- | ---------------------- | ---------- | -------- | --- |
Followingtheestablishmentofcriteriadefiningtheresearchareasoffocusrelevantforeach
SDG (overall and per SDG-Theme), these criteria were used to guide the development of Downloaded from http://direct.mit.edu/qss/article-pdf/5/2/408/2376617/qss_a_00304.pdf by guest on 07 June 2026
queries to retrieve publication sets. Where possible, the analyst responsible for query devel-
opment wasselected due to subject matter expertise in the field. Otherwise, the process was
informed by a literature review. An iterative approach was taken to assess the precision with
which individual keywords and sets of keywords identified publications that met the criteria.
KeywordsfromtheElsevier2020(Jayabalasinghametal.,2019)andAuroraEuropeanUniver-
sities Alliance (Schmidt & Vanderfeesten, 2021) queries were assessed first. Additional
keywords were identified using term-frequency and inverse-document frequency (TF-IDF)
analysesoftextfromtitles,abstracts,andauthorkeywordsfrompublicationsmeetingthecri-
teria.Additionaleffortsweretakentoidentifypublicationsthatmayhavebeenexcludedbased
on the developed query. Specifically, the query results were analyzed to identify specialized
journals that would be expected to include a high percentage of publications that fit the
|             |     |     | Table | 1. Anexample | of  | SDG 1subtopicsand |     | associated SDGtargets |            |        |     |
| ----------- | --- | --- | ----- | ------------ | --- | ----------------- | --- | --------------------- | ---------- | ------ | --- |
| Subset code |     |     |       | Criteria     |     |                   |     |                       | Associated | target |     |
SDG1-Main Researchfocusedonpovertyandresearchasdefinedfor Target 1.1: Eradicate extreme poverty
any SDG1-subset below. “Action term” specified: The Target 1.2: Reduce poverty by half All Targets
actionterm,“alleviate”wasappliedtomakethetopic associated with SDG1-Subsets
|     |     | term | “poverty” | more specific. |     |     |     |     |     |     |     |
| --- | --- | ---- | --------- | -------------- | --- | --- | --- | --- | --- | --- | --- |
SDG1-Theme1 Research focused on social programs, including all Target 1.3: Implement nationally appropriate
articles discussing social security systems related to social protection systems
|     |     |          |          |           | “action | terms”        |      |     |     |     |     |
| --- | --- | -------- | -------- | --------- | ------- | ------------- | ---- | --- | --- | --- | --- |
|     |     | health,  | finance, | and work. | No      |               | were |     |     |     |     |
|     |     | required | for the  | inclusion | of the  | topics above. |      |     |     |     |     |
SDG1-Theme2 Research focused on microfinance, access to the Target 1.4: Equal rights to economic resources
|     |     | property,    | inheritance, | natural     | resources,       | and   | new        | and basic | services |     |     |
| --- | --- | ------------ | ------------ | ----------- | ---------------- | ----- | ---------- | --------- | -------- | --- | --- |
|     |     | technologies | as           | they relate | to facilitating  |       | access,    |           |          |     |     |
|     |     | equality,    | and human    | rights.     | “Action          | term” | specified: |           |          |     |     |
|     |     | the action   | term         | “access     | to” was applied. |       |            |           |          |     |     |
SDG1-Theme3 Research focused on resilience, exposure, and Target 1.5: Build the resilience of the poor
|     |     | vulnerability | to                 | disasters | (financial,   | climate-related, |     |     |     |     |     |
| --- | --- | ------------- | ------------------ | --------- | ------------- | ---------------- | --- | --- | --- | --- | --- |
|     |     | social        | ...), particularly | on        | understanding | poor             | and |     |     |     |     |
“action
|     |     | vulnerable | people        | and | communities.  | No  |            |     |     |     |     |
| --- | --- | ---------- | ------------- | --- | ------------- | --- | ---------- | --- | --- | --- | --- |
|     |     | terms”     | were required | for | the inclusion | of  | the topics |     |     |     |     |
above.
SDG1-Theme4 Research focused on financial aid, policies, government Target 1A: Ensure significant mobilization of
support (such as food banks, and support distribution resources from a variety of sources
strategies), and strategies to eradicate poverty. No Target 1B: Create sound policy frameworks
|              |         | “action | terms” |               |     |               |        |     |     |     |     |
| ------------ | ------- | ------- | ------ | ------------- | --- | ------------- | ------ | --- | --- | --- | --- |
|              |         |         |        | were required | for | the inclusion | of the |     |     |     |     |
|              |         | topics  | above. |               |     |               |        |     |     |     |     |
| Quantitative | Science | Studies |        |               |     |               |        |     |     |     | 411 |

Identifying research supporting the United Nations Sustainable Development Goals
criteria,andthecitationnetworkofthepublicationsretrievedusingthequerywasassessedto
identifypublicationswithinthecitationnetworkoftheresults(i.e.,publicationscitingorcited
bythe publications retrieved by the query) that were not retrieved by the query. Publications
from these specialized journals or the citation network that were not being retrieved by the
querywereassessedtoidentifyadditionalkeywordstoincludeinthequerytoincreaserecall.
Relevant exclusions were built into the queries to increase precision and could result in the
exclusion of specific terms using Boolean operators or the exclusion of fields of science
deemed to be outside the scope of the criteria.
Tofacilitate thecontinuous evaluation ofthequery,publications weremanually reviewed
toassesstheir fitagainstthecriteria shownabove (seeTable1forSDG1).Anevaluation ofa
minimum of 100 random publications by two independent analysts was done to support the
calculation of precision metrics for each query and a minimum precision threshold of 90%
was required for a query to be considered acceptable. The recall was assessed against inde-
pendentpublicationsetsdeveloped byananalystconsistingofpublicationsfromspecialized
journalsidentifiedtofitthecriteria.Asmostspecializedjournalsdonotexclusivelyfocustheir
contentonasingleSDG,aminimumrecallof60%wasrequiredforaquerytobeconsidered
acceptable. In cases where no single journal was specific enough for all publications within
thatjournaltofitthecriteriasetforanSDGorSDG-Theme,apublicationsetwasconstructed
by manually selecting publications from a journal with high relevance to the SDG (or SDG-
Theme), and recall was assessed against this set.
2.1.2. Precisionassessment
As described earlier, queries were composed gradually, starting from the seed queries devel-
oped at first by analysts. These queries were developed by concatenating queries together
withBooleanOR’expressionsafterevaluatingthekeywordssuggestedbytheTF-IDFanalysis
on the seed data set. Before adding a new search expression to the global SDG data set,
analysts were encouraged to sample at least 10 documents to ensure that high precision
was maintained throughout most queries and not simply for the global SDG data set. This
isquiteimportant,asotherwisesomekeywordsbringingasmallnumberofnewpublications,
but covering mostly content not relevant to the SDG, could be included in the data set, and
while their impact on global precision would be relatively small, it would still mean that
analystswouldbeforcingbadcontentwithsuchterms.Thesamplingwasperformeddirectly
in the exploration window which could be used to quickly draw random samples of publi-
cationscontainingtheselectedkeywords.Thisenabledanalyststovetnewkeywordsquickly,
whichwasnecessarygiventhecomplexityofthequeriesneededtodelineatetheSDGsprop-
erly. As a target, a 90% precision level was required to commit the tentative search expres-
sion;otherwise,alowerlevelwouldleadtodiminishedprecisionfortheglobaldatasetatthe
end of the iterative process. This was especially critical for keywords adding a lot of new
documents to the global data set, as lower precision for these would more greatly influence
the global precision.
Although precision was assessed throughout the whole process, a more formal precision
estimatewasperformedattheendofthewholeprocesstoprovideafinalassessment,which
would guide analysts as to whether they could stop their work or if an additional effort was
needed to remove content that was deemed too broad and resulted in lowered precision. A
largesampleof100publicationswaspulledfromtheglobaldatasetandanalystsperformeda
manual inspection of these, the tool enabling us to tag publications as good, bad, and in-
between for cases where the analyst was unsure whether documents should be included or
not. This feature presented the advantage that final precision assessments were stored in the
Quantitative Science Studies 412
Downloaded
from
http://direct.mit.edu/qss/article-pdf/5/2/408/2376617/qss_a_00304.pdf
by
guest
on
07
June
2026

Identifying research supporting the United Nations Sustainable Development Goals
toolandcouldbeconsultedatanytimeinthefuture.Thiswasespeciallyhelpfulwhenaddi-
tionalvalidationstepswereperformedbytheQAanalyst,whichwasabletovalidatethepre-
cisionassessmentbyassessingthesamesample.Iffinalprecisionwasinthe90–95%rangeor
above, precision was deemed sufficient.
As a final step, a final QAwas performed by an expert bibliometrician with more than a
decade of experience in the field and in building data sets. Each query was analyzed by this
expert, and tested again for its precision, reusing the samples pulled from each analyst, but
often pulling new samples as well to further solidify confidence. This additional layer of
validation helped cement the process, ensuring a unified view over all SDGs, in a similar
way to what was accomplished when defining definitions as groups at the beginning of the
process. The QA round led to multiple modifications, removals, and additions across most
SDGs,oftenresultinginrelativelyminorchangesinpublicationcounts,butfurtherincreasing
therobustnessofthealignmentbetweenthedefinitionsandthefinalcontentretrievedbythe
queries.
2.1.3. Recallassessment
To determine the recall of the queries developed by analysts, a selection of specialized jour-
nals was identified for each SDG to serve as a stand-in for a gold standard, representing the
subjects at hand. This pragmatic “proxy” for recall measurement was developed in the
absence of a true gold standard for testing the recall of the queries. The absence of a gold
standard is unsurprising; should such a gold standard exist, it would imply that perfectly
delineated document sets for SDGs would already exist, thus rendering the current exercise
irrelevant.ForeachSDG,setsofhighlyrelevantjournalswereidentifiedusingacombination
of keyword searches in journal names and percentages of journal content covered by the
keyword queries. This dual approach ensured that no relevant journals would be missed
simply because their name was not declarative enough to be captured. After these journals
wereidentified,analystsaimedtomaximizerecallacrosseachofthesejournals,whilemain-
taininghigh precision. Recall levels of60–70%were set asthe original minimal level forthe
current exercise based on two decades of expertise building such data sets. Increasing recall
for some categories without comprising precision is sometimes easy in subjects relying on
highly declarative vocabulary, while it can become quite tricky in others, especially those
mixingmultipledimensionsastheircoreconcepts.InthecaseofthetargetsoftheSDGs,this
notion is especially relevant, as SDGs often mix basic research with economic and social
concepts.
During the process, recall against the selected gold standard of journals was tested fre-
quently to determine if more investigation was needed to add new keywords to the queries.
Analysts performed recurring analyses of the content of these journals not captured by the
queries to detect any research subject not covered. TF-IDF analyses on these documents
notretrievedwereperformedtoobtainlistsofsuggestedtermsforinclusiontofurtherincrease
recall. At the end of the process, if recall remained low, corrected recalls were computed by
sampling amongst the publications not retrieved with the keyword queries, estimating which
partwastrulyrelevanttothesubjectathand.Indeed,specializedjournals,whileusuallyhav-
ing targetedscopes, are not always fully relevant to the topic at stake. By sampling about 50
publications,analystswereabletocomputecorrectedrecallscoresbyestimatingthefraction
of the content not covered that was indeed relevant to subjects.
As a final step, a final QAwas again performed by the expert bibliometrician. Each query
was analyzed by this expert and tested for recall, investigating whether areas of each target
Quantitative Science Studies 413
Downloaded
from
http://direct.mit.edu/qss/article-pdf/5/2/408/2376617/qss_a_00304.pdf
by
guest
on
07
June
2026

Identifying research supporting the United Nations Sustainable Development Goals
mighthavebeenmissedorleftoutbytheanalyst.TheQAroundledtomultiplemodifications,
removals,andadditionsacrossmostSDGs,oftenresultinginrelativelyminorchangesinpub-
licationcounts,butfurtherincreasingtherobustnessofthealignmentbetweenthedefinitions
|     |     | and | the final | content | retrieved | by the | queries. |     |     |     |
| --- | --- | --- | --------- | ------- | --------- | ------ | -------- | --- | --- | --- |
BelowwerefertothementionedrecallevaluationdatasetastotheElsevierrecalldataset.
2.2. MachineLearningAppliedtoSDGClassification
On top of the mapping produced by the queries described above, additional articles are Downloaded from http://direct.mit.edu/qss/article-pdf/5/2/408/2376617/qss_a_00304.pdf by guest on 07 June 2026
|     |     | mapped | to  | the SDGs | by a | machine | learning | model. |     |     |
| --- | --- | ------ | --- | -------- | ---- | ------- | -------- | ------ | --- | --- |
Inanutshell,themodelisalogisticregressiontrainedwithTF-IDFrepresentationsoftitles,
keywords,abstracts,andtwomoreoptionaltextfields—maintermsextractedfromthefulltext
and subject areas of the journal that published the paper. Thus, the model learns similar key
phrasesforeachSDGandhelpstoimprovetherecallofthequeries.Tokeepprecisionhigh,
wekeeponlythosepapersthatareclassifiedbythemodelwith95%orhigherpredictedprob-
|     |     | ability | for some | SDG. |     |     |     |     |     |     |
| --- | --- | ------- | -------- | ---- | --- | --- | --- | --- | --- | --- |
IntheElsevier2021SDGmappingrelease(Rivestetal.,2021),theElsevierteamspecifies
the input data for the model, the targets with which it is trained, the technical details of the
modelitself, andmodel performance. Also, toease the interpretation ofthe modelclassifica-
tionoutcomes,wesharetheSDG-specifickeyphraseslearnedbythemodel,aswellassample
articlesclassifiedbythemodel.Refertothementioneddocumentationformoredetailsonthe
|     |     | machine | learning | component |     | of our | approach. |     |     |     |
| --- | --- | ------- | -------- | --------- | --- | ------ | --------- | --- | --- | --- |
2.3. CombiningtheQueriesandtheModel
|     |     | The | end-to-end       | approach    |     | to mapping | scholarly | records to SDGs       | is two-staged: |     |
| --- | --- | --- | ---------------- | ----------- | --- | ---------- | --------- | --------------------- | -------------- | --- |
|     |     |     | (cid:129) First, | the keyword | SDG | queries    | are       | run (orange in Figure | 1).            |     |
(cid:129)
Then, the ML model adds about 3.5% of papers (blue in Figure 1) on top of what is
classifiedbythekeywordqueries.Weonlykeepthemostconfidentmodelpredictions
|     |     |     | by  | thresholding | predicted | scores | at  | 0.95. |     |     |
| --- | --- | --- | --- | ------------ | --------- | ------ | --- | ----- | --- | --- |
Figure 1. Distribution of the number of papers mapped by the queries (SM, orange) and by the
|              |                 | model(ML, |     | blue), bySDG | (ignoringSDG |     | 17). |     |     |     |
| ------------ | --------------- | --------- | --- | ------------ | ------------ | --- | ---- | --- | --- | --- |
| Quantitative | Science Studies |           |     |              |              |     |      |     |     | 414 |

Identifying research supporting the United Nations Sustainable Development Goals
NotethattheapproachislimitedtotheScopusdatabase,asthequeriesarewritteninScopus
search syntax.
3. RESULTS
3.1. ComparisonBetweentheSDGQueries
BelowwedescribetheSDGqueriesandvalidationdatasetsthatweusedforthecomparison
|     |     | in  | terms of precision, |     | recall, and | F1 scores. |     |     |     |     |     |
| --- | --- | --- | ------------------- | --- | ----------- | ---------- | --- | --- | --- | --- | --- |
Downloaded from http://direct.mit.edu/qss/article-pdf/5/2/408/2376617/qss_a_00304.pdf by guest on 07 June 2026
3.1.1. Querymodels
Table 2 describes the different classification methods that we compared. These can be either
|     |     |         |         | (“Elsevier |         | 2020,” | “Aurora |         | v5,” “Auckland |         | v2,” |
| --- | --- | ------- | ------- | ---------- | ------- | ------ | ------- | ------- | -------------- | ------- | ---- |
|     |     | keyword | queries |            | queries |        |         | queries |                | queries | and  |
“Bergen SDG queries”) or machine learning models (“Aurora ML v0.2”) or both (“Elsevier
|     |     |         |      | 2021,” | “Elsevier |         | 2022”). |     |     |     |     |
| --- | --- | ------- | ---- | ------ | --------- | ------- | ------- | --- | --- | --- | --- |
|     |     | queries | + ML |        |           | queries | + ML    |     |     |     |     |
3.1.2. Validationssets:Collectionmethod,sizes,andquality
Table3providesdetailsonthevalidationdatasetsusedinthecomparison.Italsomentionsthe
associatedlimitationsandbiases.Itisimportanttomentionthatthereisnosinglebestvalida-
|     |     | tion | data set | to evaluate | the output | of  | SDG classification. |     |     |     |     |
| --- | --- | ---- | -------- | ----------- | ---------- | --- | ------------------- | --- | --- | --- | --- |
3.1.3. Performance;querymodelsmeasuredagainstvalidationsets
Table4providestheevaluationresultsfortheSDGclassificationmethodsoutlinedinTable2
and evaluation data sets described in Table 3. Each cell shows two values: microaverage
F1-score and macroaverage F1-score (the microaverage F1-score aggregates performance
metricsacrossallclassesbytreatingeachinstanceequally,whilethemacroaverageF1-score
computestheF1-scoreforeachclassindependentlyandthentakestheaverage,givingequal
weighttoallclasses regardless oftheir sizes),in percent(%).Bothprecisionandrecallwere
calculated with respect to the validation sets (i.e., all predictions beyond the validation sets
were ignored):
(cid:129)
Precision is calculated as the number of correctly predicted SDG IDs divided by the
|     |     |     | number | of Scopus | IDs tagged | with | the | same SDG | ID in the given | validation | set. |
| --- | --- | --- | ------ | --------- | ---------- | ---- | --- | -------- | --------------- | ---------- | ---- |
(cid:129)
RecalliscalculatedastheproportionofcorrectlypredictedSDGIDswithinthegiven
|     |     |     | validation | set. |     |     |     |     |     |     |     |
| --- | --- | --- | ---------- | ---- | --- | --- | --- | --- | --- | --- | --- |
TocomparewithBergenqueries,Table5providessimilarmetricsonlyconsideringasubsetof
10SDGs,namely,SDG1(Nopoverty),SDG2(Zerohunger),SDG3(Goodhealthandwell-
being),SDG4(Qualityeducation),SDG7(Affordableandcleanenergy),SDG11(Sustainable
cities and communities), SDG 12 (Responsible consumption and production), SDG 13
|     |     | (Climate | action), | and | SDG 14 | (Life below | water), | and | SDG 15 (Life on | land). |     |
| --- | --- | -------- | -------- | --- | ------ | ----------- | ------- | --- | --------------- | ------ | --- |
The same comparisons for precision and recall are found in the Supplementary material
|     |     | (see | Tables S1–S4). |     |     |     |     |     |     |     |     |
| --- | --- | ---- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Notethatmicroaveragingfavorswell-represented,frequentclasses(likeSDG3inourcase)
while high macroaveraged scores mean that the method works fairly well across all SDGs
because bad results for a single SDG affect macroaveraged metrics much more than
microaveraged ones. By attending to both micro- and macroaveraged F1-scores we try to
assessbothaspects:howgoodthemethodisatclassifyingpapersintofrequentorrareclasses.
| Quantitative | Science Studies |     |     |     |     |     |     |     |     |     | 415 |
| ------------ | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Identifying research supporting the United Nations Sustainable Development Goals
Table2. SDG classification methods (bothkeyword queries andMLmodels) usedin theevaluation (Armitage, Lorenz, &Mikki, 2020a)
| Classification | method |     |     |     | Description |     |     | Web location |     |
| -------------- | ------ | --- | --- | --- | ----------- | --- | --- | ------------ | --- |
Auckland queries v2 Togainabetterunderstandingofourresearchcontribution,theUniversityof https://www.sdgmapping
(Auckland_v2) Auckland SDG Keywords Dictionary Project seeks to build on the .auckland.ac.nz/
processesdevelopedbytheUnitedNationsandTHEinordertocreatean
|     |     | expanded | list of keywords | that | can be used | to identify | SDG-relevant |     |     |
| --- | --- | -------- | ---------------- | ---- | ----------- | ----------- | ------------ | --- | --- |
research.
Aurora ML v0.2 “AI for mapping multi-lingual academic papers to the United Nations’ https://doi.org/10.5281
SustainableDevelopmentGoals(SDGs)”(Vanderfeesten&Jaworek,2022).
(Aurora_ml) /zenodo.5603019 Downloaded from http://direct.mit.edu/qss/article-pdf/5/2/408/2376617/qss_a_00304.pdf by guest on 07 June 2026
Aurora queries v5 “Mapping Research Output to the Sustainable Development Goals (SDGs)” https://zenodo.org/records
| (Aurora_v5) |     | (Vanderfeesten | et al., | 2020). |     |     |     | /4883250 |     |
| ----------- | --- | -------------- | ------- | ------ | --- | --- | --- | -------- | --- |
Bergen SDG queries The Bergen approach created queries for Web of Science to retrieve SDG- https://zenodo.org/records
(Bergen_2023_baa relatedpublicationsforalimitednumberofSDGs.Thequerieshavebeen /7711561
and translatedforScopusandasampleoftheresultshasbeentakenaspositive
Bergen_2023_bta) examples.Thesehavebeensupplementedbyotherpublicationswhichdid
|     |     | not appear | in the queries | as negative | examples. | Two | data sets were |     |     |
| --- | --- | ---------- | -------------- | ----------- | --------- | --- | -------------- | --- | --- |
created,onebasedontheActionApproachqueriesandonebasedonthe
queries—referred
|     |     | Topic Approach |           |                 | to as | Bergen BAA | and Bergen BTA |     |     |
| --- | --- | -------------- | --------- | --------------- | ----- | ---------- | -------------- | --- | --- |
|     |     | respectively   | (Armitage | et al., 2020b). |       |            |                |     |     |
“Identifying
Elsevier queries 2020 research supporting the United Nations Sustainable https://elsevier
Goals”
(Els_2020) Development (Jayabalasingham et al., 2019). .digitalcommonsdata
.com/datasets
/87txkw7khs/1
Elsevier queries + ML “ImprovingtheScopusandAuroraqueries toidentifyresearchthat supports https://elsevier
2021 (Els_2021) the United Nations Sustainable Development Goals (SDGs) 2021” (Rivest .digitalcommonsdata
|     |     | et al., 2021). |     |     |     |     |     | .com/datasets |     |
| --- | --- | -------------- | --- | --- | --- | --- | --- | ------------- | --- |
/9sxdykm8s4/4
Elsevier queries + ML A simplified version of “Elsevier queries + ML 2021” with Covid-related https://elsevier
2022 (Els_2022) addendum to SDG 3 (Roberge, Kashnitsky, & James, 2022). .digitalcommonsdata
.com/datasets
/6bjy52jkm9/1
Elsevier queries + ML For2023,theSDGsusetheexactsamesearchqueryandMLalgorithmasthe https://elsevier
2023 (Els_2023) Elsevier2022SDGmappings,withonlyminormodificationstofiveSDGs, .digitalcommonsdata
namelySDG1,4,5,7,and14.Inthesecases,thequerieswereshortened .com/datasets
by removing exclusion lists based on journal identifiers. These exclusion /y2zyy9vwzy/1
listsoftencontainedthousandsofitemstofilteroutcontentinjournalsthat
|     |     | were not | core to the | SDGs (Bedard-Vallee |     | et al., 2023). |     |     |     |
| --- | --- | -------- | ----------- | ------------------- | --- | -------------- | --- | --- | --- |
South African SDG A machine learning model mapping text to SDGs. https://sasdghub.up.ac.za
| hub (South_africa) |     |     |     |     |     |     |     | /home/ |     |
| ------------------ | --- | --- | --- | --- | --- | --- | --- | ------ | --- |
SIRIS queries (SIRIS) The SIRIS queries were developed by extracting key terms from the UN https://zenodo.org/records
official list of goals, targets, and indicators as well as from relevant /4118028
|     |     | literature       | around SDGs.       | The query       | system | has subsequently | been           |     |     |
| --- | --- | ---------------- | ------------------ | --------------- | ------ | ---------------- | -------------- | --- | --- |
|     |     | expanded         | with a pre-trained | word2vec        |        | model and an     | algorithm that |     |     |
|     |     | selects related  | words              | from Wikipedia. | There  | are multiple     | queries per    |     |     |
|     |     | SDG (Duran-Silva | et                 | al., 2019).     |        |                  |                |     |     |
Bordignon SDG Thesequeriesaimedatreducingthepolysemyoftermsbylimitingkeywords https://data.mendeley
queries (Bordignon) from Elsevier 2020 queries (Jayabalasingham et al., 2019) to relevant .com/datasets
subject areas using the All-Science Journal Classification (ASJC) /xrx7ddbbb4/1
|              |                 | (Bordignon, | 2021). |     |     |     |     |     |     |
| ------------ | --------------- | ----------- | ------ | --- | --- | --- | --- | --- | --- |
| Quantitative | Science Studies |             |        |     |     |     |     |     | 416 |

Identifying research supporting the United Nations Sustainable Development Goals
|     |     | Table3. | SDG validation datasets | usedin theevaluation |     |     |
| --- | --- | ------- | ----------------------- | -------------------- | --- | --- |
Validation set Description and method of collection Web location Size Remarks on quality
Elsevier recall See Section 2.1.1 SharedviaICSRLab; 465k The data set is noisy in the
| dataset           |     |     |     | see Section 4.3 | sense that  | not all papers  |
| ----------------- | --- | --- | --- | --------------- | ----------- | --------------- |
| (Elsevier_recall) |     |     |     |                 | from an     | SDG-specific    |
|                   |     |     |     |                 | journal are | relevant to the |
|                   |     |     |     |                 | same SDGs.  | Hence, we do    |
|                   |     |     |     |                 | not aim     | for 100% recall |
withrespecttothisdataset
Downloaded from http://direct.mit.edu/qss/article-pdf/5/2/408/2376617/qss_a_00304.pdf by guest on 07 June 2026
|     | “Survey | of‘MappingResearch |     |     |     |     |
| --- | ------- | ------------------ | --- | --- | --- | --- |
Aurora Survey data outputto https://zenodo.org 6,741 Bias: the researchers are
(Aurora1) theSDGs’ by AuroraEuropean Universities /records/3813230 located at western
Alliance (AUR)”: 244seniorresearchers #.YyG93uxBxYw European universities.
fromdifferentuniversitiesinEuropeandthe
|     | UnitedStates | filled in | a survey. Theywere |     |     |     |
| --- | ------------ | --------- | ------------------ | --- | --- | --- |
onlyallowedtoenterthesurveyiftheywere
|     | familiarwith | the SDG | they hadselectedto |     |     |     |
| --- | ------------ | ------- | ------------------ | --- | --- | --- |
evaluate.Thefirstquestionwastoprovidea
|     | list of researchpapers |                   | they believe are |     |     |     |
| --- | ---------------------- | ----------------- | ---------------- | --- | --- | --- |
|     | relevant               | tothatselected    | SDG. Thesecond   |     |     |     |
|     | questionwas            | to handpick,froma | given set        |     |     |     |
of100randomlydrawnpapersintheAurora
queryresultset,thepapersthattheybelieve
|     | (based on | readingthe     | title, abstract, journal |     |     |     |
| --- | --------- | -------------- | ------------------------ | --- | --- | --- |
|     | name,and  | authors)belong | to the selected          |     |     |     |
SDG.Thesuggestedpapersandtheselected
papers are includedinthevalidationset.
Aurora Suggested The papers suggested by researchers; see https://zenodo.org 3,964 Theresearchersinvolvedinthe
Papers(Aurora2) “Survey data of ‘Mapping Research output /records/3813230 surveyidentifiedthemselves
|     | to the SDGs’.” |     |     | #.YyG93uxBxYw | ashavingexpertiseina |     |
| --- | -------------- | --- | --- | ------------- | -------------------- | --- |
specificSDG.Theymight
alsohavetheincentiveto
citetheirownresearch
Elsevier multilabel The data set consists of 6,000 papers SharedviaICSRLab; 6,000 Annotators are not as versed
SDG data set annotated by three experts each. These see Section 4.3 in SDGs as the analysts
(Els_multilabel) paperscomefromfivedatasourcestospan who developed Elsevier
as diverse as possible set of SDG-related queries and the Elsevier
|     | papers.Thirtypercentofthepapersarenot |     |     |     | recall data | set |
| --- | ------------------------------------- | --- | --- | --- | ----------- | --- |
mapped to any of SDGs.
Chilean multilabel The data set is provided by Pontificia https://repositorio.uc 1,200 Biases: self-assessment, only
(Chile) Universidad Católica (PUC) based in Chile .cl/handle/11534 Chilean researchers
|     | and consists | of about               | 1,200 papers self- | /61951 |     |     |
| --- | ------------ | ---------------------- | ------------------ | ------ | --- | --- |
|     | assessed     | by PUC researchers     | and labeled        |        |     |     |
|     | with 0,      | 1, or 2SDGs(Rodríguez, | Delpiano           |        |     |     |
et al., 2021).
OSDG A public data set of thousands of text https://zenodo.org 32,431 Crowd-sourced data set; the
Community excerpts, which were validated by /records/6831287 annotatorsarenotversedin
Dataset (OSDG) approximately 1,000 OSDG Community #.YyMF5OxBxYy SDGs. In our benchmarks,
Platform (OSDG-CP) citizen scientists from we only kept the records
over 110 countries, with respect to the with a difference between
|     | Sustainable | Development | Goals. |     | positive     | and negative votes |
| --- | ----------- | ----------- | ------ | --- | ------------ | ------------------ |
|     |             |             |        |     | greater than | or equal to 2,     |
|     |             |             |        |     | thus leaving | only 26,217        |
records.
| Quantitative | Science Studies |     |     |     |     | 417 |
| ------------ | --------------- | --- | --- | --- | --- | --- |

Identifying research supporting the United Nations Sustainable Development Goals
Table4. F1scores withmicro/macro averaging (percentages) for 10classification methods and
fivevalidation datasets.Bold figures indicate thebest result in thecolumn;asterisks indicate
“winners”dependingon
|     |     | multiple |     | micro- ormacroaveraging |     |     |     |
| --- | --- | -------- | --- | ----------------------- | --- | --- | --- |
Data set
|     |     | Method      | Aurora1 | Aurora2 | Els_multilabel | Chile | OSDG  |
| --- | --- | ----------- | ------- | ------- | -------------- | ----- | ----- |
|     |     | Auckland_v2 | 49/40   | 46/33   | 69/62          | 60/37 | 47/40 |
|     |     | Aurora_ml   | 53/44*  | 39/32   | 64/57          | 55/38 | 53/46 |
Aurora_v5 55/42* 15/18 37/38 12/14 26/20 Downloaded from http://direct.mit.edu/qss/article-pdf/5/2/408/2376617/qss_a_00304.pdf by guest on 07 June 2026
|     |     | Els_2020     | 47/35 | 46/28  | 63/47 | 55/25 | 33/27 |
| --- | --- | ------------ | ----- | ------ | ----- | ----- | ----- |
|     |     | Els_2021     | 46/39 | 38/32  | 73/67 | 46/34 | 41/35 |
|     |     | Els_2022     | 46/39 | 38/32  | 73/67 | 46/34 | 41/35 |
|     |     | Els_2023     | 45/38 | 37/30  | 72/66 | 46/31 | 42/36 |
|     |     | South_africa | 51/40 | 45/35* | 72/60 | 65/41 | N/A   |
|     |     | SIRIS        | 36/33 | 29/25  | 49/45 | 37/30 | 37/37 |
|     |     | Bordignon    | 45/34 | 50/30* | 60/48 | 61/32 | N/A   |
The code reproducing the experiments presented in this subsection is found on GitHub2.
RefertotheDataavailabilitysectionforinstructionsonobtainingthedatashouldyouwishto
|     |     | reproduce the | presented experiments. |     |     |     |     |
| --- | --- | ------------- | ---------------------- | --- | --- | --- | --- |
We conclude that there is no single best approach performing well across all validation
data sets: Some approaches are on average better at precision (e.g., Elsevier 2020 and South
African SDG ML model; see Tables S1 and S2), others shine at recall (e.g., Auckland queries
Q8andAuroraMLmodel;see TablesS3and S4).Thisfindingsupportsthegeneralcriticism
thatSDGclassificationfaces:Differentmappingmethodstypicallykickoffwiththesamekey-
wordsbutthenresultinpoorlyoverlappingmappings(Armitageetal.,2020b;Purnell,2022).
Apartfromthese“qualitative”problemswithSDGmappingswenowestablishthe“quantita-
tive” problem: When evaluated against several hand-labeled SDG data sets, different
|     |     | approaches | fail to select a clear | winner. |     |     |     |
| --- | --- | ---------- | ---------------------- | ------- | --- | --- | --- |
We notice a clear “overfitting” phenomenon: Elsevier queries + ML 2022 are best when
validated against Elsevier’s multilabeled data set while the Aurora queries v.5 and Aurora
MLmodelsachievethehighestF1-scoresagainsttheAurorasurveydataset.Aprobableexpla-
nationisthatthedatasetswerecraftedforaspecificdefinition/operationalizationofSDGsand
|     |     | these definitions | are undoubtedly | different from | one project | to another. |     |
| --- | --- | ----------------- | --------------- | -------------- | ----------- | ----------- | --- |
It is important to conclude that there is no single “golden” SDG validation data set; each
oneconsideredinourexperimentscomeswithitsownshortcomings(seeTable3,remarkson
quality), and each data set used in query development reflects some certain interpretation of
SDGsbythequerydevelopers.SimilarlytohowArmitageetal.(2020b)concludedthatthere
isapooroverlapinpublicationsfoundbydifferentsetsofqueries,weconcludethatthereisno
clear winner among SDG classification methods when those are validated with available
|     |     | human-annotated | SDG data | sets. |     |     |     |
| --- | --- | --------------- | -------- | ----- | --- | --- | --- |
2 https://github.com/Yorko/sdg_mapping_queries_n_ml_benchmarks.
| Quantitative | Science Studies |     |     |     |     |     | 418 |
| ------------ | --------------- | --- | --- | --- | --- | --- | --- |

Identifying research supporting the United Nations Sustainable Development Goals
Table5. F1scores withmicro/macro averaging (percentages) for 12classification methods and
fivevalidationdatasets.HerethevalidationisperformedonlyagainstasubsetofSDGsforwhich
|     |     | wehave Bergen2023queries: | 1,  | 2, 3,4, 5, 11, 12,13,14, | and15 |     |     |
| --- | --- | ------------------------- | --- | ------------------------ | ----- | --- | --- |
Data set
|     |     | Method      | Aurora1 | Aurora2 | Els_multilabel | Chile | OSDG  |
| --- | --- | ----------- | ------- | ------- | -------------- | ----- | ----- |
|     |     | Auckland_v2 | 59/47   | 60/42*  | 78/70          | 69/46 | 59/57 |
|     |     | Aurora_ml   | 61/48   | 47/37   | 72/63          | 66/48 | 65/62 |
Aurora_v5 64/50 17/23 40/46 13/18 29/27 Downloaded from http://direct.mit.edu/qss/article-pdf/5/2/408/2376617/qss_a_00304.pdf by guest on 07 June 2026
|     |     | Bergen_2023_baa | 15/11 | 15/11  | 15/13 | 14/12 | N/A   |
| --- | --- | --------------- | ----- | ------ | ----- | ----- | ----- |
|     |     | Bergen_2023_bta | 17/16 | 17/15  | 22/25 | 16/14 | N/A   |
|     |     | Els_2020        | 54/39 | 61/37  | 71/52 | 63/33 | 39/37 |
|     |     | Els_2021        | 55/45 | 46/38  | 80/74 | 53/42 | 47/44 |
|     |     | Els_2022        | 55/45 | 46/38  | 80/74 | 53/42 | 48/45 |
|     |     | Els_2023        | 54/43 | 46/37  | 80/73 | 52/38 | 48/46 |
|     |     | South_africa    | 60/50 | 58/45  | 80/72 | 74/56 | N/A   |
|     |     | SIRIS           | 48/40 | 42/33  | 62/54 | 48/39 | 51/49 |
|     |     | Bordignon       | 53/34 | 67/40* | 68/52 | 72/40 | N/A   |
3.2. TrackingtheProgressofElsevierQueries
TheprogresswithSDGqueriesdevelopmentatElsevierwastrackedbothintermsofrecall,as
described in Section 2.1.3 and in terms of precision/recall/F1 when validated with the inde-
pendentlylabelledElseviermultilabeldataset.Table6showsrecallscoresfordifferentElsevier
queriesasmeasuredagainsttheElsevierrecalldatasetdescribedindetailinSection2.Table7
shows precision, recall, and F1 scores for different Elsevier queries as measured against the
Elsevier multilabel SDG data set described in Table 3. Note that due to the specifics of the
SDG query creation methodology, it makes sense to report only recall for the first data set.
The reason is that it is labeled in a noisy way (the assumption that all papers from an
SDG-specificjournalcontributetothesameGoalisfarfromperfect);thus,lookingatprecision
sense—it
(and hence F1) is not meaningful. However, reporting recall makes perfect shows
|     |     | how many SDG-related | papers from | this large data | set the queries | can detect. |     |
| --- | --- | -------------------- | ----------- | --------------- | --------------- | ----------- | --- |
Table6. ElsevierqueriesvalidatedagainsttheElsevierrecalldataset(seeSection2).Micro-and
|     |     | macroaveragedvaluesfor | recall arereported |     |     |     |     |
| --- | --- | ---------------------- | ------------------ | --- | --- | --- | --- |
Elsevier recall
|              |                 | Method   |     |     |     | data | set, recall |
| ------------ | --------------- | -------- | --- | --- | --- | ---- | ----------- |
|              |                 | Els_2020 |     |     |     |      | 54/38       |
|              |                 | Els_2021 |     |     |     |      | 78/72       |
|              |                 | Els_2022 |     |     |     |      | 78/72       |
|              |                 | Els_2023 |     |     |     |      | 73/68       |
| Quantitative | Science Studies |          |     |     |     |      | 419         |

Identifying research supporting the United Nations Sustainable Development Goals
Table7. Elsevier queries validated against the Elsevier multilabel SDG data set (see Table 3).
P stands for precision, R for recall, and F1 for F1 score. Micro- and macroaveraged values are
reported
|     |     |          |     | Elsevier | multilabel data | set |       |
| --- | --- | -------- | --- | -------- | --------------- | --- | ----- |
|     |     | Method   |     | P        | R               |     | F1    |
|     |     | Els_2020 |     | 72/62    | 57/42           |     | 63/45 |
|     |     | Els_2021 |     | 69/63    | 78/75           |     | 73/63 |
Els_2022 69/63 78/75 73/63 Downloaded from http://direct.mit.edu/qss/article-pdf/5/2/408/2376617/qss_a_00304.pdf by guest on 07 June 2026
|     |     | Els_2023 |     | 68/62 | 76/73 |     | 72/62 |
| --- | --- | -------- | --- | ----- | ----- | --- | ----- |
FromTables6and7,weseethatall oftheElsevier2021–2023queriesperform aboutthe
same in terms of metrics and provide a considerable improvement in recall (and hence F1)
|     |     | over the earlier | 2020 version | of the queries. |     |     |     |
| --- | --- | ---------------- | ------------ | --------------- | --- | --- | --- |
Themetricsarecloseforthe2021–2023versionsofthequeriesbecausethe2022and2023
updateswerenotasconsiderableastheonein2021.Namely,the2022version(Robergeetal.,
2022) introduced only COVID-related changes to SDG 3. The 2023 version of the queries
(Bedard-Vallee et al., 2023) introduced changes to SDGs 1, 4, 5, and 14, removing long lists
|     |     | of journal    | identifiers and  | replacing them with keywords. |     |     |     |
| --- | --- | ------------- | ---------------- | ----------------------------- | --- | --- | --- |
|     |     | 4. DISCUSSION | AND PERSPECTIVES |                               |     |     |     |
In previous sections, we described the methodology and evaluation results. Below, we out-
line possible improvements to the SDG mapping approach, including localization of the
SDG queries, query generalization to non-English languages and extending the approach to
|     |     | nonarticle | content. |     |     |     |     |
| --- | --- | ---------- | -------- | --- | --- | --- | --- |
4.1. Localization
Researchactivitiesdonotstandalone;theyareanintegralpartofthegeographicalplacethey
were initiated and the communities they serve. An attempt to measure SDG-related research
activities can be improved by infusing the local context within which the research activities
take place. A localization approach can further foster understanding of, for example, the
degree to which the prevailing SDG mapping approaches capture SDG research in the geo-
graphicalregionthatmayormaynothavebeendescribedbykeywordsandkeyphraseswith
close semantic relatedness to the keyword-based queries (e.g., Elsevier 2020 queries).
TheUniversityofAuckland’sapproach(Wang,Kang,&Mu,2023)isonesuchlocalization
attemptbasedonElsevier’searlier2020queries,amixtureoftheUNofficialtargetsandindi-
cators, and the suggested search terms by the Sustainable Development Solutions Network
(SDSN). The n-gram model was applied to two samples of Scopus publication metadata: a
global publication sample and a University of Auckland publication sample. The n-gram
tokens were scored by a range of factors, including counts and measures of frequency, and
were then ranked by those scores. Keywords with a high rank were then evaluated in more
detailandmanuallyreviewedandimprovedforSDGalignments.Table8showsthenumberof
University’s
|              |                 | University       | of Auckland publications | between 2009         | and 2020 captured | by the |     |
| ------------ | --------------- | ---------------- | ------------------------ | -------------------- | ----------------- | ------ | --- |
|              |                 | queries compared | with those               | captured by Elsevier | 2020 queries.     |        |     |
| Quantitative | Science Studies |                  |                          |                      |                   |        | 420 |

Identifying research supporting the United Nations Sustainable Development Goals
|     |     |        | Table8.  | Comparison       | of Aucklandv2 |          | queriesand    | Elsevier | 2021queries |               |     |
| --- | --- | ------ | -------- | ---------------- | ------------- | -------- | ------------- | -------- | ----------- | ------------- | --- |
|     |     |        | Auckland | queries          |               | Elsevier | 2020          | queries  |             | Intersection  |     |
|     |     |        |          | output (number   |               | output   | (number       |          | of          | (number       | of  |
|     |     | SDG Id |          | of publications) |               |          | publications) |          |             | publications) |     |
|     |     | 1      |          | 522              |               |          |               | 229      |             |               | 125 |
|     |     | 2      |          | 1,975            |               |          |               | 420      |             |               | 264 |
|     |     | 3      |          | 16,894           |               |          | 7,966         |          |             | 6,894         |     |
Downloaded from http://direct.mit.edu/qss/article-pdf/5/2/408/2376617/qss_a_00304.pdf by guest on 07 June 2026
|     |     | 4   |     | 2,484 |     |     | 1,043 |     |     |     | 745 |
| --- | --- | --- | --- | ----- | --- | --- | ----- | --- | --- | --- | --- |
|     |     | 5   |     | 611   |     |     |       | 609 |     |     | 360 |
|     |     | 6   |     | 684   |     |     |       | 486 |     |     | 362 |
|     |     | 7   |     | 1,152 |     |     | 1,187 |     |     |     | 799 |
|     |     | 8   |     | 428   |     |     |       | 440 |     |     | 154 |
|     |     | 9   |     | 1,044 |     |     | 1,139 |     |     |     | 519 |
|     |     | 10  |     | 1,528 |     |     |       | 977 |     |     | 500 |
|     |     | 11  |     | 1,886 |     |     | 1,462 |     |     |     | 779 |
|     |     | 12  |     | 921   |     |     |       | 438 |     |     | 158 |
|     |     | 13  |     | 1,032 |     |     |       | 577 |     |     | 466 |
|     |     | 14  |     | 1,390 |     |     |       | 744 |     |     | 552 |
|     |     | 15  |     | 1,641 |     |     |       | 769 |     |     | 473 |
|     |     | 16  |     | 891   |     |     |       | 779 |     |     | 409 |
For 13 of the 16 SDGs documented in Table 8, the Auckland queries capture more
SDG-relatedpublications.Insomecases,thenumberofpublicationscapturedbytheAuckland
queries doubled that captured by the Elsevier 2021 approach. A significant proportion of the
additionalpublicationsarecapturedthroughlocalizedkeywordsandsearchterms.Forexample,
“Te Whāriki”—the New Zealand national curriculum document for early childhood
education—was
|     |     |     |     | used as an SDG4 | key phrase | under | the | Auckland | approach, | as it pinpoints |     |
| --- | --- | --- | --- | --------------- | ---------- | ----- | --- | -------- | --------- | --------------- | --- |
what makes a quality early childhood education curriculum with an indigenous Māori lens. It
retrieved 19 SDG4 papers published by the University of Auckland, of which only six were
Whāriki
counted by the Elsevier 2020 approach. A manual inspection of these 19 Te papers
unsurprisinglysuggeststhehighrelevanceofall19paperstoSDG4Target4.2onensuringqual-
ity early childhood development, care, and pre-primary education. In some other cases, the
Aucklandqueriesalsogaverisetoadditionalkeywordspotentiallyfittingfortheglobalsettings.
Forexample,“marinebiodiversity”asanAucklandkeyphraseretrieved24SDG14paperspub-
lishedbytheUniversityofAuckland,ofwhich19werecountedbytheElsevier2020approach.
AsshowninFigure2,applyingtheAucklandapproachtotheAurora(survey&suggested),
Elsevier(multilabel),Chilean,andOSDGdatasetsgeneratesF1scoresthatarebetterforsome
SDGs(e.g.,SDG3,4,7,and14)thanothers.TheF1scoresarenotablylowforSDGssuchas
SDG1,2,10,and12.Thissuggeststhat,whilethelocalizedapproachaddsusefulkeywords
and themes in some contexts, further work is required to examine each keyword and key
phrase independently to understand their impact on precision and recall and to refine the
| Quantitative | Science Studies |     |     |     |     |     |     |     |     |     | 421 |
| ------------ | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Identifying research supporting the United Nations Sustainable Development Goals
Figure2. F1-scores for theAucklandapproach applied to theAurora, Elsevier, Chilean,and OSDG datasets.
searchconditionsuponwhichtheyshouldbeapplied. Infuturework,itwouldalsobeinter-
esting to develop a contextualized SDG-label set that aligns with the contextualized SDG
mapping approach (e.g., an Auckland SDG validation set) to better test out the performance
of the contextualized approach against more generic, global approaches.
4.2. MultilingualQueries
In CRIS systems3 and repositories there are many more publications that are not included in
Scopusandarewritteninthelocallanguageofthecountrytoserveadifferentaudience.We
foundthatwecouldnotsimplyreplacethekeywordsinthequeriesandhavethesearchwork
thesameinotherlanguages,becauseofthesyntaxandmorphologyrules.ThatiswhyAurora
chose to train mBERT models to classify SDGs. Due to the lack of non-English SDG-labeled
data, we used only English training data, specifically paper abstracts.
Duringtheevaluation,themodelsforSDGs1–5and11wereappliedtoclassify888German
papertitles.Tohaveaqualitativebenchmark,weperformedamanualSDGclassificationonly
on titlesaswell.Indoingthe latter,wetendedto takea strict approachand triedto stick very
closetotherespectiveSDGindicators(e.g.,nonassignmentofSDG4topublicationsonteacher
training inGermany, asthe SDG indicatorsonlyrefer to teachertraininginthe Global South).
The manual classification resulted in 43 SDG-related publications, while the ML models
resulted in 58 SDG-related publications. The total overlap between these two methods was
eight publications. This was mainly for SDG3—Good Health and Wellbeing (5/8) and can
most likely be explained by great similarities in terminology between English and German
forissuessuchasmultiplesclerosis,psychotherapy,suicide,alcohol,andillegaldrugs(inGer-
man: Multiple Sklerose, Psychotherapie, Suizid, Alkohol, illegale Drogen).
At the current phase of evaluation, the multilingual ability of the ML models for research
output in German cannot be positively assessed. However, further analysis, including the
abstracts of publications for the classification of the ML models, may offer improvements in
classification quality.
4.3. GeneralizationtoOtherTypesofContent
In addition to SDG-related research outputs, higher education institutions have a strong
interest in understanding SDG-related educational activities, as done in the Aurora SDG
CourseCatalogue4.TheseSDGlabelshavebeenaddedmanuallybythecoursecoordinators,
3 https://en.wikipedia.org/wiki/Current_research_information_system.
4 https://bit.ly/aurora-sdg-courses.
Quantitative Science Studies 422
Downloaded
from
http://direct.mit.edu/qss/article-pdf/5/2/408/2376617/qss_a_00304.pdf
by
guest
on
07
June
2026

Identifying research supporting the United Nations Sustainable Development Goals
but such a process is labor-intensive and not sustainable, as this needs to be done year
after year.
Similartopublicationmetadata(e.g.,title,abstract,keywords),manycoursecataloguesand
curriculum management systems capture metadata in a similar way (e.g., title, course short
description, course long description). Whether the SDG research mapping techniques can
be translated and applied to SDG course mapping represents an interesting topic to many.
A study was conducted by the University of Auckland to apply the Auckland queries to
classify courses taught by the university. The mapping results identified 792 SDG courses
out of 2,441 courses in total offered to students in the academic year 2020. Compared with
the frequency and distribution of keywords in research mapping, course mapping demon-
strated a higher concentration of keywords used to convey the SDG topics. For example,
the24UniversityofAucklandcoursesrelatedtoSDG14arefullycapturedbythetop10key-
words in the Auckland queries by frequency (i.e., marine; fisheries; coastal management;
pollut*; aquaculture; marine environment; fisheries management; eutrophical*; aquatic
ecosystem; alga*).
5. CONCLUSION
In this paper, we outlined the methodology behind research mapping to the United Nations
(UN)SustainableDevelopmentGoals(SDGs),howitcomparestootherexistingmethods,and
how well it performs with existing SDG validation data sets. We conclude that there is no
singlebestapproachperformingwellacrossallvalidationdatasets,althoughElsevierqueries
areslightlymorestable.Wealsoconcludethatthereisnosingle“golden”SDGvalidationdata
set.Eachoneconsideredinourexperimentscomeswithitsownshortcomings,andeachdata
setusedinquerydevelopmentbearstheintrinsicbiasoftheSDGinterpretationsbythequery
developers. We observed that Elsevier’s queries have seen a measurable improvement from
the original 2020 version to the 2021/2022/2023 versions. Finally, we discussed possible
improvementstotheexistingapproach:localizationofthequeriesandgeneralizationtoother
languages and data types.
ACKNOWLEDGMENTS
ThisworkispartlyanoutcomeoftheSDGResearchMappingInitiative5thatElsevierinitiated
withtheAuroraEuropeanUniversitiesAlliance,theUniversityofAuckland,andtheUniversity
of Southern Denmark. We are also grateful to Scopus for providing data for the analysis.
AUTHOR CONTRIBUTIONS
Yury Kashnitsky: Conceptualization, Investigation, Methodology, Software, Supervision, Vali-
dation, Writing—original draft, Writing—review & editing. Guillaume Roberge: Conceptuali-
zation, Methodology, Writing—review & editing. Jingwen Mu: Investigation, Methodology,
Resources. Kevin Kang: Software, Validation. Weiwei Wang: Investigation, Methodology.
MauriceVanderfeesten:Formalanalysis,Methodology,Resources.MaximeRivest:Concep-
tualization, Methodology, Validation, Writing—review & editing. Savvas Chamezopoulos:
Software,Validation.RobertJaworek:Formalanalysis.MaévaVignes:Investigation,Method-
ology, Resources. Bamini Jayabalasingham: Methodology, Validation. Finne Boonen: Meth-
odology,Visualization.ChrisJames:Project administration.Marius Doornenbal:Resources,
Supervision. Isabelle Labrosse: Methodology, Visualization.
5 https://www.elsevier.com/about/sustainability/sdg-research-mapping-initiative.
Quantitative Science Studies 423
Downloaded
from
http://direct.mit.edu/qss/article-pdf/5/2/408/2376617/qss_a_00304.pdf
by
guest
on
07
June
2026

Identifying research supporting the United Nations Sustainable Development Goals
COMPETING INTERESTS
The authors have no competing interests.
FUNDINGINFORMATION
No funding has been received for this research.
DATAAVAILABILITY
Thedataunderlyingtheresultspresentedinthestudy(includingtheprocessedversionofpub-
licly available data sets listed in Table 3) are available, partially via GitHub6 and partially
(upon application) from Elsevier BVon the ICSR Lab7. ICSR Lab is intended for scholarly
researchonlyandisacloud-basedcomputationalplatformthatenablesresearcherstoanalyze
largestructureddatasets,includingaggregateddatafromScopusauthorprofiles,PlumXMet-
rics, SciVal Topics, and Peer Review Workbench.
REFERENCES
Armitage,C.,Lorenz,M.,&Mikki,S.(2020a).Replicationdatafor: goals (3rd) [Web page]. Retrieved March 4, 2024, from https://
MappingscholarlypublicationsrelatedtotheSustainableDevel- clarivate.com/g/sustainable-development-goals/.
opment Goals: Do independent bibliometric approaches get the Pukelis, L., Puig, N. B., Skrynik, M., & Stanciauskas, V. (2020).
same results? [Data set]. https://doi.org/10.18710/98CMDR OSDG—Open-source approach to classify text data by UN Sus-
Armitage,C.S.,Lorenz,M.,&Mikki,S.(2020b).Mappingscholarly tainable Development Goals [Data set]. arXiv. https://doi.org/10
publications related to the Sustainable Development Goals: Do .48550/arXiv.2005.14569
independent bibliometric approaches get the same results? Purnell,P.J.(2022). Acomparisonofdifferentmethodsof identi-
Quantitative Science Studies, 1(3), 1092–1108. https://doi.org fying publications related to the United Nations Sustainable
/10.1162/qss_a_00071 Development Goals: Case study of SDG 13—Climate action.
Bedard-Vallee, A., James, C., & Roberge, G. (2023). Elsevier 2023 Quantitative Science Studies, 3(4), 976–1002. https://doi.org
SustainableDevelopmentGoals(SDGs)mapping[Dataset].Else- /10.1162/qss_a_00215
vier Data Repository. https://doi.org/10.17632/y2zyy9vwzy.1 Rivest,M.,Kashnitsky,Y.,Bédard-Vallée,A.,Campbell,D.,Khayat,
Bordignon, F. (2021). Dataset of search queries to map scientific P.,...James,C.(2021).ImprovingtheScopusandAuroraqueries
publications to the UN sustainable development goals. Data in toidentifyresearchthatsupportstheUnitedNationsSustainable
Brief, 34, 106731. https://doi.org/10.1016/j.dib.2021.106731, Development Goals (SDGs) 2021 (Version 3.0) [Data set].
PubMed: 33537369 Mendeley. https://doi.org/10.17632/9sxdykm8s4.1
Confraria, H., Ciarli, T., & Noyons, E. (2022). Countries’ research Roberge, G., Kashnitsky, Y., & James, C. (2022). Elsevier 2022
priorities in relation to the Sustainable Development Goals. Sustainable Development Goals (SDG) Mapping (Version 1.0)
MERIT Working Papers 2022-030, United Nations University— [Data set]. Digital Commons Data. https://doi.org/10.17632
MaastrichtEconomicandSocialResearchInstituteonInnovation /6bjy52jkm9.1
andTechnology(MERIT).[Webpage].RetrievedMarch4,2024, Rodríguez, P. C., Delpiano, R. R., Meneses, P. S., & Vargas, R. V.
from https://ideas.repec.org/p/unm/unumer/2022030.html. (2021). Conjunto de datos: Categorization of articles 2017 with
Duran-Silva,N.,Fuster,E.,Massucci,F.A.,&Quinquillà,A.(2019). authorship of Pontificia Universidad Católica de Chile, through
AcontrolledvocabularydefiningthesemanticperimeterofSus- the SDGS [Data set]. https://bibliotecadigital.oducal.com
tainableDevelopmentGoals(1.2)[Dataset].Zenodo.https://doi /Record/ir-11534-69668/Details
.org/10.5281/zenodo.3567769 Ross, D. (2022). Impact rankings 2022: Methodology [Web page].
Jayabalasingham, B., Boverhof, R., Agnew, K., & Klein, L. (2019). Retrieved March 4, 2024, from https://www.timeshighereducation
Identifying research supporting the United Nations Sustainable .com/world-university-rankings/impact-rankings-2022-methodology.
Development Goals (Version 1.0) [Data set]. Mendeley. https:// Schmidt,F.,&Vanderfeesten,M.(2021).Evaluationonaccuracyof
doi.org/10.17632/87txkw7khs.1 mapping science to the United Nations’ Sustainable Develop-
Jingwen, M., & Weiwei, W. (2022). The University of Auckland ment Goals (SDGs) of the Aurora SDG queries. Zenodo. https://
SDG keywords mapping [Web page]. Retrieved March 4, 2024, doi.org/10.5281/zenodo.4917171
from https://www.sdgmapping.auckland.ac.nz/. SouthAfricanSDGHub.(2023).SouthAfricanSDGHub[Webpage].
LaFleur, M. (2019). Art is long, life is short: An SDG Classification RetrievedMarch4,2024,fromhttps://sasdghub.up.ac.za/home/.
System for DESA Publications. DESAWorking Paper 159. Avail- Vanderfeesten, M., & Jaworek, R. (2022). AI for mapping multi-
able atSSRN: https://dx.doi.org/10.2139/ssrn.3400135. lingual academic papers to the United Nations’ Sustainable
Nakamura, M.,Pendlebury,J., Schnell, J., &Szomszor, M.(2019). Development Goals (SDGs). Zenodo. https://doi.org/10.5281
Navigating thestructure of researchon sustainable development /zenodo.6487606
6 https://github.com/Yorko/sdg_mapping_queries_n_ml_benchmarks.
7 https://www.elsevier.com/insights/icsr/lab.
Quantitative Science Studies 424
Downloaded
from
http://direct.mit.edu/qss/article-pdf/5/2/408/2376617/qss_a_00304.pdf
by
guest
on
07
June
2026

Identifying research supporting the United Nations Sustainable Development Goals
Vanderfeesten,M.,Otten,R.,&Spielberg,E.(2020).Searchqueries Wulff,D.U.,Meier,D.S.,&Mata,R.(2023).Usingnoveldataand
for "Mapping Research Output to the Sustainable Development ensemble models to improve automated labeling of Sustainable
Goals (SDGs)" v5.0.2 (Version 5.0.2) [Data set]. Zenodo. Development Goals. arXiv. https://doi.org/10.48550/arXiv.2301
https://doi.org/10.5281/zenodo.4883250 .11353
Wang,W.,Kang,W.,&Mu,J.(2023).MappingresearchtotheSus- Zhang, R., Vignes, M., Steiner, U., & Zimek, A. (2020). Matching
tainable Development Goals (SDGs), PREPRINT (Version 2). research publications to the United Nations’ Sustainable Devel-
ResearchSquare. https://doi.org/10.21203/rs.3.rs-2544385/v2 opment Goals by multi-label-learning with hierarchical catego-
Wastl, J., Porter, S., Draux, H., Fane, B., & Hook, D. (2020). Con- ries. In IEEE 7th International Conference on Data Science and
textualizing sustainable development research. https://doi.org/10 Advanced Analytics (DSAA) (pp. 516–525). Sydney, NSW,
.6084/m9.figshare.12200081.v2 Australia. https://doi.org/10.1109/DSAA49011.2020.00066
Quantitative Science Studies 425
Downloaded
from
http://direct.mit.edu/qss/article-pdf/5/2/408/2376617/qss_a_00304.pdf
by
guest
on
07
June
2026
