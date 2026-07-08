TYPE Review
|     |     |     |     |     |     |     |     | PUBLISHED | 13January2025 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------------- | --- |
10.3389/frai.2024.1472411
DOI
|     | The         | sociolinguistic |     |          |     | foundations |     |     |     |     |
| --- | ----------- | --------------- | --- | -------- | --- | ----------- | --- | --- | --- | --- |
|     | of language |                 |     | modeling |     |             |     |     |     |     |
OPENACCESS
EDITEDBY
MeishanZhang,
HarbinInstituteofTechnology,China JackGrieve*,SaraBartl,MatteoFuoli,JasonGrafmiller,
| REVIEWEDBY | WeihangHuang,AlejandroJawerbaum,AkiraMurakami, |     |     |     |     |     |     |     |     |     |
| ---------- | ---------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
CynthiaWhissell,
MarcusPerlman,DanaRoemlingandBodoWinter
LaurentianUniversity,Canada
KevinTang,
HeinrichHeineUniversityofDüsseldorf, DepartmentofLinguisticsandCommunication,UniversityofBirmingham,Birmingham,
| Germany | UnitedKingdom |     |     |     |     |     |     |     |     |     |
| ------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
LiweiYang,
NortheastNormalUniversity,China
Inthisarticle,weintroduceasociolinguisticperspectiveonlanguagemodeling.
*CORRESPONDENCE
JackGrieve We claim that language models in general are inherently modeling varieties of
j.grieve@bham.ac.uk
|     | language, | and we | consider | how | this | insight can | inform | the development |     | and |
| --- | --------- | ------ | -------- | --- | ---- | ----------- | ------ | --------------- | --- | --- |
RECEIVED29July2024 deploymentoflanguagemodels.Webeginbypresentingatechnicaldefinition
ACCEPTED30November2024
|     | of the concept | of  | a variety | of  | language | as developed |     | in sociolinguistics. |     | We  |
| --- | -------------- | --- | --------- | --- | -------- | ------------ | --- | -------------------- | --- | --- |
PUBLISHED13January2025
|     | then discuss | how | this perspective |     | could | help | us better | understand | five | basic |
| --- | ------------ | --- | ---------------- | --- | ----- | ---- | --------- | ---------- | ---- | ----- |
CITATION
|     | challenges | in language |     | modeling: | social | bias, | domain | adaptation, | alignment, |     |
| --- | ---------- | ----------- | --- | --------- | ------ | ----- | ------ | ----------- | ---------- | --- |
GrieveJ,BartlS,FuoliM,GrafmillerJ,
HuangW,JawerbaumA,MurakamiA, language change, and scale. We argue that to maximize the performance
PerlmanM,RoemlingDandWinterB(2025) and societal value of language models it is important to carefully compile
Thesociolinguisticfoundationsoflanguage
trainingcorporathataccuratelyrepresentthespecificvarietiesoflanguagebeing
modeling.Front.Artif.Intell.7:1472411.
doi:10.3389/frai.2024.1472411 modeled, drawing on theories, methods, and descriptions from the field of
sociolinguistics.
COPYRIGHT
©2025 Grieve,Bartl,Fuoli,Grafmiller,Huang,
Jawerbaum,Murakami,Perlman,Roemling
| andWinter.Thisisanopen-accessarticle | KEYWORDS |     |     |     |     |     |     |     |     |     |
| ------------------------------------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
distributedunderthetermsoftheCreative AIethics,artificialintelligence,computationalsociolinguistics,corpuslinguistics,large
CommonsAttributionLicense(CCBY).The languagemodels,naturallanguageprocessing,varietiesoflanguage
use,distributionorreproductioninother
forumsispermitted,providedtheoriginal
author(s)andthecopyrightowner(s)are
1 Introduction
creditedandthattheoriginalpublicationin
thisjournaliscited,inaccordancewith
acceptedacademicpractice.Nouse,
distributionorreproductionispermitted Theunderlyingtaskoflanguagemodelingistopredicttheprobabilityofwordtokens,
whichdoesnotcomplywiththeseterms. or other linguistic forms, in a text based on previously observed texts (Jurafsky and
|     | Martin, 2023). | Language | modeling     |     | is not        | new (Bengio | et      | al., 2003), | but when           | pursued |
| --- | -------------- | -------- | ------------ | --- | ------------- | ----------- | ------- | ----------- | ------------------ | ------- |
|     | through the    | analysis | of extremely |     | large corpora | of          | natural | language    | using transformer- |         |
basedarchitectures(Vaswanietal.,2017;Devlinetal.,2018),ithasproventobeauniquely
|     | effective approach |     | to natural | language | processing |     | (NLP) (Radford |     | et al., 2019). | These |
| --- | ------------------ | --- | ---------- | -------- | ---------- | --- | -------------- | --- | -------------- | ----- |
systems,whichhavecometobeknownasLargeLanguageModels(LLMs),arecurrently
revolutionizingArtificialIntelligence(AI),withespeciallypowerfulLLMssuchasGPT-
|     | 4(Achiametal.,2023),LLaMa(Touvronetal.,2023), |       |             |     |            |        | Mistral(Jiangetal.,2023)often |     |               |        |
| --- | --------------------------------------------- | ----- | ----------- | --- | ---------- | ------ | ----------------------------- | --- | ------------- | ------ |
|     | being referred                                | to as | base models | or  | foundation | models | (Bommasani                    |     | et al., 2021) | due to |
theirhighlevelsoffluencyandtheirabilitytohelpachievestate-of-the-artperformance
acrossawiderangeofdownstreamtasks,mostfamouslyinchatbotslikeChatGPT(Ray,
2023).DespiteincreasingconcernsabouttherisksofLLMs(Benderetal.,2021),experts
acrossmanyfieldsbelievetheywillhaveamajorimpactonsociety,includinginmedicine
(Thirunavukarasuetal.,2023;HuangY.etal.,2024),education(Kasnecietal.,2023;Yigci
etal.,2024),computerprogramming(Lietal.,2022;Wangetal.,2024),journalism(Pavlik,
2023;Lietal.,2024),economics(Horton,2023;GuoandYang,2024),andtechnicalwriting
(Lundetal.,2023;Cruz-Castroetal.,2024).
|     | Given | the growing | societal | importance |     | of LLMs, | language | modeling | has | provoked |
| --- | ----- | ----------- | -------- | ---------- | --- | -------- | -------- | -------- | --- | -------- |
criticaldiscussionfromawiderangeofperspectives,notonlyAIandNLP(e.g.,Bender
etal.,2021;Bommasanietal.,2021;Jiaoetal.,2024;Headetal.,2023),butinlinguistics
| FrontiersinArtificialIntelligence |     |     | 01  |     |     |     |     |     | frontiersin.org |     |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- |

| Grieveetal. |     |     |     |     |     |     |     |     |     |     |     |     | 10.3389/frai.2024.1472411 |     |     |
| ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- |
(e.g., Piantadosi, 2023; Dentella et al., 2023; Marcus et al., 2023), modelingthatwebelievethesociolinguisticperspectiveintroduced
cognitive science (e.g., Hardy et al., 2023; Demszky et al., 2023; inthispapercanhelpaddress.Werefertothesechallengesassocial
Michaelovetal.,2024),andethics(e.g.,Birhaneetal.,2023;Cabrera bias,domainadaptation,alignment,languagechange,andscale.
etal.,2023;Lietal.,2023;Stefanetal.,2023;HaqueandLi,2024). Ourprimarygoalinthispositionpaperisthereforetointroduce
Thereis,however,averybasicquestionaboutlanguagemodelsthat a sociolinguistic perspective on language modeling and to argue
hasreceivedremarkablylittleattentionintheliterature: foritsrelevancetoourgeneralunderstandingoflanguagemodels,
|     |     |     |     |     |     |     |     | as well as | their | development |     | and deployment |     | in the real | world. |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ----- | ----------- | --- | -------------- | --- | ----------- | ------ |
Whatisactuallybeingmodeledbylanguagemodels? Ourintentisnottoprovidesimpleorspecificsolutionstomajor
|     |     |     |     |     |     |     |     | challenges | in language |     | modeling. | Rather, | our | intent is | to offer |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ----------- | --- | --------- | ------- | --- | --------- | -------- |
Although the goal of language modeling is clear (i.e., token a new and general theoretical perspective from which to better
|              |     |         |          |       |         |     |          | understand | these | challenges, |     | arguing | for greater | engagement | in  |
| ------------ | --- | ------- | -------- | ----- | ------- | --- | -------- | ---------- | ----- | ----------- | --- | ------- | ----------- | ---------- | --- |
| prediction), | the | type of | language | being | modeled | by  | language |            |       |             |     |         |             |            |     |
models is usually only defined in the most general terms, for the field of language modeling with the field of sociolinguistics.
Ourcoreargumentisthat,whenpretrainingorfurtherpretraining
| example, | “a broad | swath | of internet | data” | (Brown | et  | al., 2020). |     |     |     |     |     |     |     |     |
| -------- | -------- | ----- | ----------- | ----- | ------ | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
Modelsareoftentrainedoncorporabasedatleastinpartonthe languagemodels,itisimportanttocarefullyconsiderthespecific
CommonCrawldatasetoralike(Radfordetal.,2019;Raffeletal., varieties of language being modeled and to compile corpora that
|     |     |     |     |     |     |     |     | accurately | represent | these | varieties | of  | language. | Furthermore, | we  |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --------- | ----- | --------- | --- | --------- | ------------ | --- |
2020;Baack,2024),butotherwise,inmostcases,thenatureofthe
languagebeingmodeledisnotdescribedatall(Benderetal.,2021). argue that corpus compilation should be firmly grounded in
theories,methods,andfindingsofsociolinguistics,whichhaslong
Inlargepart,thisisanaturalconsequenceoftheneedformassive
amountsofdatatotrainbasemodels,makingthesourcesofthese focused on understanding the nature of language variation and
corporaofsecondaryconcern.However,evenwhenthesemodels change. Our hope is that the proposals made in this paper will
inspirefutureempiricalresearchinlanguagemodeling,ultimately
| are adapted | for more | specific | contexts |     | (Gururangan | et  | al., 2020), |     |     |     |     |     |     |     |     |
| ----------- | -------- | -------- | -------- | --- | ----------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
the type of language used for further training is generally only leading to improvements inthe performance of languagemodels
|     |     |     |     |     |     |     |     | and the | societal | value | of the | NLP | systems | into which | they |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | -------- | ----- | ------ | --- | ------- | ---------- | ---- |
looselydefined.Forexample,ChatGPTwasdevelopedbyadapting
| aGPT-3.5basemodelfordialogue(OpenAI,2022),buttheform |          |       |         |     |         |     |           | areembedded. |     |     |     |     |     |     |     |
| ---------------------------------------------------- | -------- | ----- | ------- | --- | ------- | --- | --------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
| of dialogue                                          | actually | being | modeled | by  | ChatGPT | is  | something |              |     |     |     |     |     |     |     |
muchlessdiverseandmuchmoreartificialthaneverydayEnglish
|     |     |     |     |     |     |     |     | 2 Defining |     | varieties |     | of  | language |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --------- | --- | --- | -------- | --- | --- |
conversation,asanyonewhointeractswithChatGPTknows.
| Drawing | on  | modern | sociolinguistic |     | theory, | in this | paper, we |     |     |     |     |     |     |     |     |
| ------- | --- | ------ | --------------- | --- | ------- | ------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
thereforeprovideananswertothequestionwhatisbeingmodeled A variety of language, or more simply a variety, is a term
bylanguagemodels? commonlyusedacrosslinguisticstorefertoanytypeoflanguage
|     |     |     |     |     |     |     |     | (Crystal | and Davy, | 1969; | Hartmann | and | Stork, | 1972; Matthews, |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --------- | ----- | -------- | --- | ------ | --------------- | --- |
Languagemodelsaremodelsofvarietiesoflanguage. 1997; McEnery et al., 2006; Jackson, 2007; Crystal, 2011). The
termisespeciallycommoninfieldsthatstudylanguagevariation
Wearguethatanylanguagemodelisinherentlymodelingthe andchange—likesociolinguistics,dialectology,typology,historical
|     |     |     |     |     |     |     |     | linguistics, | discourse | analysis, |     | stylistics, | and corpus | linguistics— |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --------- | --------- | --- | ----------- | ---------- | ------------ | --- |
varietyoflanguagerepresentedbythecorpusonwhichitistrained,
evenifthatvarietyoflanguageisunknownandevenifthatcorpus whereitisgenerallyusedtoidentifythetypesoflanguagetargeted
fordescription,comparison,orotherformsoflinguisticanalysis.
| is a poor | representation |         | of that     | variety | of language.  | Our | view       | is  |        |           |             |     |         |            |         |
| --------- | -------------- | ------- | ----------- | ------- | ------------- | --- | ---------- | --- | ------ | --------- | ----------- | --- | ------- | ---------- | ------- |
|           |                |         |             |         |               |     |            | One | reason | a variety | of language |     | is such | a powerful | concept |
| that this | simple         | insight | can inform, | at      | a fundamental |     | level, how |     |        |           |             |     |         |            |         |
languagemodelsaredevelopedanddeployed.Givenrapidadvances is because it can be used to identify such a wide range of
|             |          |     |        |       |         |            |          | phenomena—from |     | very | broadly | defined | varieties | like the | entire |
| ----------- | -------- | --- | ------ | ----- | ------- | ---------- | -------- | -------------- | --- | ---- | ------- | ------- | --------- | -------- | ------ |
| in language | modeling | in  | recent | years | and the | increasing | societal |                |     |      |         |         |           |          |        |
impactandriskassociatedwithLLMs,webelievethesociolinguistic English language to very narrowly defined varieties like the
|     |     |     |     |     |     |     |     | speeches | of a | single | politician. | This | terminology | also | allows |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---- | ------ | ----------- | ---- | ----------- | ---- | ------ |
perspectiveweareproposinginthispaperisespeciallyimportant
linguiststosidestepdebates,whichareoftenunderlyinglypolitical
| at this time—not |     | only to | improve | the | performance, |     | evaluation, |     |     |     |     |     |     |     |     |
| ---------------- | --- | ------- | ------- | --- | ------------ | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
and applicability of LLMs, but to guide the creation of safe in nature, like whether a given variety qualifies as a dialect or a
|             |            |     |        |      |           |            |       | language | (Meyerhoff, | 2018). | For | example, | regardless | of  | whether |
| ----------- | ---------- | --- | ------ | ---- | --------- | ---------- | ----- | -------- | ----------- | ------ | --- | -------- | ---------- | --- | ------- |
| and ethical | AI systems |     | and to | help | us better | understand | their |          |             |        |     |          |            |     |         |
underlyingnature. ScotsisconsideredtobeadialectofEnglishoradistinctlanguage,
|             |            |             |     |          |            |       |              | Scots can | be considered |        | to be   | a variety, | as well  | as a sub-variety |          |
| ----------- | ---------- | ----------- | --- | -------- | ---------- | ----- | ------------ | --------- | ------------- | ------ | ------- | ---------- | -------- | ---------------- | -------- |
| In the      | rest of    | this paper, | we  | expand   | on our     | claim | that, in its |           |               |        |         |            |          |                  |          |
|             |            |             |     |          |            |       |              | of some   | larger        | Anglic | variety | that also  | includes | English          | (Aitken, |
| basic form, | a language | model       | of  | any type | represents | a     | variety of   |           |               |        |         |            |          |                  |          |
language, and we consider the implications of this claim for the 1985).Similarly,regardlessofwhetherChineseisconsideredtobe
afamilycomposedofmanylanguagesoralanguagecomposedof
| task of language |     | modeling. | We  | do this | primarily | by synthesizing |     |     |     |     |     |     |     |     |     |
| ---------------- | --- | --------- | --- | ------- | --------- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
recent research in NLP and sociolinguistics, especially research manydialects,allformsofChinesecanbeconsideredtobeboth
varietiesthemselvesandpartofsomelargerSiniticvariety(Huang
| from the | emerging | field | of computational |     | sociolinguistics, |     | which |     |     |     |     |     |     |     |     |
| -------- | -------- | ----- | ---------------- | --- | ----------------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
H.etal.,2024).
| sits at their | intersection |     | (Nguyen | et  | al., 2016; | Eisenstein, | 2017; |     |     |     |     |     |     |     |     |
| ------------- | ------------ | --- | ------- | --- | ---------- | ----------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
Grieveetal.,2023).Wefirstprovideatechnicaldefinitionofthe Although what are traditionally considered entire languages
|                 |         |     |              |     |          |     |            | like English | or  | Chinese | can | be referred | to  | as varieties, | the |
| --------------- | ------- | --- | ------------ | --- | -------- | --- | ---------- | ------------ | --- | ------- | --- | ----------- | --- | ------------- | --- |
| sociolinguistic | concept |     | of a variety | of  | language | and | argue that |              |     |         |     |             |     |               |     |
thisconceptinherentlyunderpinsthetaskoflanguagemodeling. term is most commonly used in linguistics to refer to more
narrowlydefinedsub-typesoftheselargerlanguages(Crystal,2011;
Wethenintroduceanddiscussfivegeneralchallengesinlanguage
| FrontiersinArtificialIntelligence |     |     |     |     |     |     |     | 02  |     |     |     |     |     | frontiersin.org |     |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- |

Grieveetal. 10.3389/frai.2024.1472411
Meyerhoff,2018;WardhaughandFuller,2021).Suchvarietiesare register variation in a corpus of English Twitter data through a
referred to by a wide range of technical and colloquial terms, multivariate analysis of grammatical features, identifying four
includingnotonlydialects,butaccents,sociolects,topolects,argots, generaldimensionsofstylisticvariation.
jargons,registers,genres,styles,slangs,standards,periods,anderas. Finally, periods are varieties defined by the time span over
We believe, however, that it is especially insightful to recognize whichlanguageisproduced(NevalainenandRaumolin-Brunberg,
three basic and distinct types of varieties—or, alternatively, three 2016). Like dialects and registers, linguistic variation over time
basicanddistinctsourcesoflinguisticvariation—whichwereferto is also systematic. The study of language change has been one of
asdialect,register,andperiod/time(seeFigure1). the oldest endeavors in linguistics (Bybee, 2015; Campbell, 2013;
Dialects are varieties defined by the social backgrounds Joseph et al., 2003; Lehmann, 2013). This research, which is also
of the people who produce language (Chambers and Trudgill, referredtoashistoricallinguistics,hasfocusedbothondetermining
1998; Meyerhoff, 2018; Wardhaugh and Fuller, 2021). Dialects howmutuallyunintelligiblevarietiesarehistoricallyrelatedtoeach
are often associated with language that originates from speakers other and on describing how individual varieties, like English,
from particular nations, regions, classes, or ethnicities. Empirical havechangedovertime.Notably,recentresearchincomputational
research in sociolinguistics and dialectology has long shown sociolinguisticshasstudiedhowlanguagechangesoververyshort
that the language use of people from different social groups time spans based on large corpora of timestamped social media
(Tagliamonte, 2006, 2011) and identities (Eckert, 2012, 2018; data,especiallytoanalyzelexicalinnovation(Eisensteinetal.,2014;
Ilbury, 2020) is characterized by systematic patterns of linguistic Grieve et al., 2017; Kershaw et al., 2016; Stewart and Eisenstein,
variation, especially variation in accent and vocabulary. For 2018) For example, Grieve et al. (2018) showed how new words
example,WilliamLabovandhiscolleagueshaveanalyzedvariation inAmericanEnglishtendedtooriginatefromfivehubsoflexical
in the pronunciation of American English in great detail (Bell innovation through a spatial analysis of a multi-billion-word
etal.,2016;Gordon,2017),fromvariationacrossclassandother corpusgeolocatedofTwitterdatafromacrosstheUS.
demographicvariablesinthepronunciationof/r/post-vocalically Takentogether,thesethreeextra-linguisticsourcesoflinguistic
in New York City (Labov, 1986, 1973) to mapping regional variation allow for varieties of language to be defined with great
variationinthepronunciationoftheentireEnglishvowelsystem flexibilityandprecision.ThisisillustratedinFigure1,whichshows
across North America (Labov et al., 2006). Lexical variation has how language use can be mapped across these three dimensions
also notably been the focus of considerable recent research in oflinguisticvariation,andhowavarietyoflanguagecandefined
computational linguistics, primarily based on large corpora of bytakingintoconsiderationthesocialbackgroundofpeoplewho
socialmedia(DonosoandSánchez,2017;Grieveetal.,2019;Huang producelanguage(dialect),thesocialcontextinwhichlanguageis
etal.,2016;Bammanetal.,2014).Forexample,Blodgettetal.(2016) produced(register),andtherangeoftimeoverwhichlanguageis
introducedamethodforidentifyinglexicalvariationcharacteristic produced(period).
ofAfricanAmericanEnglishonTwitter,whilealsoshowinghow AsFigure1illustrates,therelationshipsbetweenvarietiescan
NLPtoolsconsistentlyunderperformwhenappliedtothisdialect. be highly complex. Varieties can be defined at any scale and
Alternatively, registers are varieties defined by the aregenerallyhierarchicallystructured,beingdivisibleintosmaller
communicative contexts in which people, potentially from and smaller sub-varieties. For example, English is a variety, but
any social background, produce language (Biber and Conrad, it also contains many smaller sub-varieties. These include many
2019; Meyerhoff, 2018; Wardhaugh and Fuller, 2021). Registers dialects, including national varieties of English, like British and
areoftenassociatedwithlanguageproducedinspecificmodalities, AmericanEnglish,whicharethemselvescomposedofmanysmaller
media,settings,andtopics.Itisimportanttostressthatregisters regionaldialectslikeWestCountryEnglishintheUKorAfrican
and dialects are independent: dialects are defined by the social American English in the US (Chambers and Trudgill, 1998). At
backgrounds of language users, whereas registers are defined by themostnarrowlydefinedlevel,thelanguageofanindividualcan
the social contexts in which language users, regardless of their beconsideredadistinctdialect(i.e.,anidiolect).Similarly,English
socialbackgrounds,communicate.Likedialectvariation,therehas alsoincludesmanyregisters,includingspokenandwrittenEnglish,
been a long tradition of empirical research on register variation, which are themselves composed of many smaller registers, like
predominantly in corpus linguistics (Biber, 1991; Sardinha and conversations, telephone conversations, and personal telephone
Pinto, 2014; Biber and Conrad, 2005) and discourse analysis conversations(BiberandConrad,2019).
(Martin, 2001; Matthiessen, 2015; Halliday, 1989), which has Alongwithexhibitinghierarchicalstructure,varietiescanalso
shown that language use across contexts is characterized by be defined based on the overlap of larger varieties, as is also
systematic patterns of linguistic variation, especially grammatical illustrated in Figure1. For example, it is common to define a
variation (Biber and Conrad, 2019). For example, Douglas Biber varietyofinterestbyspecifyingadialect,register,andperiod,like
and his colleagues have studied register variation in English ContemporaryConversationalCanadianFrenchorScottishNovels
(Biber, 1991) and other languages (Biber, 1995) in great detail fromtheTwentiethCenturyWrittenbyWomen.Inotherwords,we
through the multivariate analysis of grammatical patterns across canthinkofavarietyasbeingdefinedbythespecificationofoneor
a range of corpora. Also, like dialect variation, recent research moreextra-linguisticfactorsrelatedtothecircumstancesinwhich
has focused on the analysis of large corpora of online language, languageisproduced.Inaddition,theboundariesbetweenvarieties
especially social media data (Biber and Egbert, 2018; Clarke and arenotnecessarilysharporfixed.Forexample,oneregionaldialect
Grieve, 2017; Liimatta, 2019; Pavalanathan and Eisenstein, 2015; orliteraryregistermighttransitiongraduallyintothenextandthis
Berber Sardinha, 2018). For example, Clarke (2022) described maychangeovertime.Forthisreasons,sociolinguistsoftentreat
FrontiersinArtificialIntelligence 03 frontiersin.org

Grieveetal. 10.3389/frai.2024.1472411
FIGURE1
Varietiesoflanguage.Thisfigureillustratestheconceptofavarietyoflanguage,showinghowtheinteractionbetweenthreedistinctextra-linguistic
factors—thesocialbackgroundofpeoplewhoproducelanguage(dialect),thesocialcontextinwhichlanguageisproduced(register),andtherange
oftimeoverwhichlanguageisproduce(period)—canbeusedtospecifyavarietyoflanguage.Italsoillustrateshowvarietiesoflanguageare
hierarchicallyorganized,composedofsmallerandsmallersub-varieties.
dialect, register, and time as dimensions of linguistic variation as extra-linguisticfactors,inparticular,byaspecificdialect,register,
opposedtohardcategories. and period (see Croft, 2000). Notably, in this case, a text
Although we have defined a variety of language as a type is broadly defined as the language (e.g., utterances, discourse)
of language, it is important to specify what exactly a variety produced during any communicative event, including language
of language consists of. In other words, when linguists study producedinanymodality(e.g.,speech,writing,signing)(Halliday
a variety of language, what are they actually studying? For and Hasan, 1976). For example, not only can an email or
many linguists, a variety of language is essentially a population an essay be considered a text, but so can a conversation
of texts (or utterances), as circumscribed by one or more or a speech. If we adopt what is known as an externalist
FrontiersinArtificialIntelligence 04 frontiersin.org

| Grieveetal. |     |     |     |     |     |     |     |     |     |     |     | 10.3389/frai.2024.1472411 |     |     |
| ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- |
approachtolinguistics(Scholzetal.,2024;Sampson,2002),where basiclevel,thisisbecausecertainwordsassociatedwithconcepts
language in general is defined as the population of all texts (or ofparticularimportancetothatgrouporcontextwillbefavored
utterances) that have ever been produced, a variety of language or will develop over time, although differences can generally be
can be defined as a sub-population of those texts that meets expectedtoemergeacrossalllevelsoflinguisticanalysis,depending
some external definition—i.e., the totality of language produced onthecommunicativeconstraintsandaffordancesassociatedwith
by people from a particular social background (dialect), in a the extra-linguistic factors that define that variety (see Grieve,
particularsocialcontext(register),andoveraparticularperiodof 2023). Although the number of possible varieties is therefore
time(period). innumerable, a general goal of linguistic analysis is to identify
For example, Contemporary Spoken French Canadian varietiesthataremaximallydistinctive,forexample,mappingthe
Conversation can be considered a variety of language, as it is a dialectregionsofacountry(WielingandNerbonne,2015;Grieve,
population of texts (i.e., conversations) produced by individuals 2016), defining the sub-types of a given register (Biber, 1989;
fromaspecificsocialbackground(i.e.,peoplewholiveinCanada), Grieve et al., 2010), or identifying the most distinct periods of a
in a specific social context (i.e., spoken interactions), during a language (Gries and Hilpert, 2008; Degaetano-Ortlieb and Teich,
| specificperiod(i.e.,now).Similarly,amorenarrowlydefinedtype |     |     |     |     |     |     |     | 2018). |     |     |     |     |     |     |
| ----------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- |
oflanguagelikeScottishNovelsfromtheTwentiethCenturyWritten Tosummarizethediscussionpresentedinthissection,weoffer
byWomencanalsobeconsideredavarietyoflanguage,asitisa thefollowingdefinitionofavarietyoflanguage(seeFigure1):
| population | of texts | (i.e., | books) | produced | by  | individuals | from | a   |     |     |     |     |     |     |
| ---------- | -------- | ------ | ------ | -------- | --- | ----------- | ---- | --- | --- | --- | --- | --- | --- | --- |
specificsocialbackground(i.e.,femaleauthorsfromScotland),ina Avarietyoflanguageisapopulationoftextsdefinedby
|     |     |     |     |     |     |     |     | one or | more | external | factors, | especially | related to | the social |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ---- | -------- | -------- | ---------- | ---------- | ---------- |
specificsocialcontext(i.e.,long-formfictionalnarratives),during
aspecifictimespan(i.e.,1900-1999). backgroundofthepeoplewhoproducethesetexts,thesocial
Thisconceptionofavarietyoflanguageisespeciallycommon context in which these texts are produced, and the period of
timeoverwhichthesetextsareproduced.
incorpuslinguistics,whereacorpusisoftenseenasrepresenting
| a variety     | of language: |        | a corpus    | consists | of             | a sample | of texts   |                 |         |              |          |             |                     |       |
| ------------- | ------------ | ------ | ----------- | -------- | -------------- | -------- | ---------- | --------------- | ------- | ------------ | -------- | ----------- | ------------------- | ----- |
|               |              |        |             |          |                |          |            | Furthermore,    |         | we define    | a corpus | as a sample | of texts            | drawn |
| drawn from    | the          | larger | population  | of       | texts targeted | for      | analysis   |                 |         |              |          |             |                     |       |
|               |              |        |             |          |                |          |            | from a specific | variety | of language, |          | i.e., from  | a larger population |       |
| (Biber, 1993; | McEnery      |        | and Wilson, | 2001;    | McEnery        | et       | al., 2006; |                 |         |              |          |             |                     |       |
Scholz et al., 2024). The goal of analyzing the structure of oftexts(seeFigure2).Inthissense,wesaythatacorpusrepresents
agivenvarietyoflanguage.Itisalsoimportanttostress,especially
languageobservedinacorpusisthereforetodrawgeneralizations
about the variety of language (i.e., the larger population of inthecontextoflanguagemodeling,thatanycorpus—anysample
oftexts—inherentlyrepresentssomevarietyoflanguage,namely,
| texts) represented |     | by that      | corpus. | Furthermore,     |     | the    | quality of |              |        |         |      |             |             |     |
| ------------------ | --- | ------------ | ------- | ---------------- | --- | ------ | ---------- | ------------ | ------ | ------- | ---- | ----------- | ----------- | --- |
|                    |     |              |         |                  |     |        |            | the smallest | common | variety | that | encompasses | that sample | of  |
| a corpus,          | and | by extension | the     | generalizability |     | of any | analyses   |              |        |         |      |             |             |     |
based on that corpus, depends directly on the representativeness texts. However, the representativeness of any corpus depends
|     |     |     |     |     |     |     |     | directly on | the quality | and | the size | of the sample, | as well | as the |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ----------- | --- | -------- | -------------- | ------- | ------ |
ofthissample,includingtheaccurateidentificationofitsprimary
constituentsub-varieties.Thisrelationshipbetweensociolinguistic accurate identification of the variety and its sub-varieties from
|     |     |     |     |     |     |     |     | which texts | are sampled. |     | For example, | a sample | consisting | of  |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------------ | --- | ------------ | -------- | ---------- | --- |
variationandcorpusdesignisillustratedinFigure2,whichshows
|              |     |        |         |                  |     |        |          | a few conversational |     | transcripts |     | and emails | collected | in Great |
| ------------ | --- | ------ | ------- | ---------------- | --- | ------ | -------- | -------------------- | --- | ----------- | --- | ---------- | --------- | -------- |
| how a corpus |     | can be | seen as | a representative |     | sample | of texts |                      |     |             |     |            |           |          |
taken from a larger population of texts delimited by relevant Britain could be taken as representing British English, just not
verywell.
| extra-linguistic |     | factors. | This figure | also | shows | how compiling |     | a   |     |     |     |     |     |     |
| ---------------- | --- | -------- | ----------- | ---- | ----- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
representative corpus in a principled manner generally requires Our primary contention in this paper is that, in general,
|           |     |            |       |     |              |     |           | language models, |     | which are | trained | on large | corpora of | natural |
| --------- | --- | ---------- | ----- | --- | ------------ | --- | --------- | ---------------- | --- | --------- | ------- | -------- | ---------- | ------- |
| access to | an  | underlying | model | of  | that variety | of  | language, |                  |     |           |         |          |            |         |
including its internal sub-varieties, so that the corpus can be language, are inherently modeling varieties of language. In
stratified so as to accurately represent internal variation in that other words, we conceive of language models as models of
|          |         |      |          |     |        |                  |     | language use—models |     | of  | how language | is used | to create | texts |
| -------- | ------- | ---- | -------- | --- | ------ | ---------------- | --- | ------------------- | --- | --- | ------------ | ------- | --------- | ----- |
| variety. | Without | such | a model, | a   | corpus | may misrepresent |     |                     |     |     |              |         |           |       |
the patterns of linguistic variation that characterize a variety in the variety of language that the corpus used to train the
|     |     |     |     |     |     |     |     | model represents. |     | Furthermore, |     | like all linguistic | models | that |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | ------------ | --- | ------------------- | ------ | ---- |
oflanguage.
Finally,ifavarietyoflanguageisdefinedasapopulationoftexts are based on corpora of natural language, we believe that the
delimitedbysomesetofexternalcriteria,thegeneralexpectation validity and value of a language model depends on the degree
is that this population of texts will differ from populations of to which the training corpus accurately represents the variety
textsdelimitedbyotherexternalcriteriaintermsofitslinguistic that is effectively being modeled, which we refer to as the
|                                                          |           |     |          |            |     |            |           | target variety—even |     | if that | variety | of language | is  | unknown |
| -------------------------------------------------------- | --------- | --- | -------- | ---------- | --- | ---------- | --------- | ------------------- | --- | ------- | ------- | ----------- | --- | ------- |
| structure,                                               | including | its | grammar, | phonology, |     | lexis, and | discourse |                     |     |         |         |             |     |         |
| (CrystalandDavy,1969;Jackson,2007).Forexample,amongother |           |     |          |            |     |            |           | orunder-specified.  |     |         |         |             |     |         |
features, a regional dialect may be characterized by the specific Consequently, our claim is that understanding how to define
pronunciation of certain vowels (Labov et al., 2006), whereas and represent varieties of language is of direct relevance to
a conversational register might be characterized by its rate of language modeling: we believe that many problems that arise in
|                |          |     |        |             |        |            |     | language modeling |     | result | from a | mismatch | between the | variety |
| -------------- | -------- | --- | ------ | ----------- | ------ | ---------- | --- | ----------------- | --- | ------ | ------ | -------- | ----------- | ------- |
| use of certain | pronouns |     | (Biber | and Conrad, | 2019). | Crucially, | we  |                   |     |        |        |          |             |         |
can expect that any social group or any social context that is of language that language models are effectively intended to
recognized within society will generally become associated with represent and the variety of language that is actually represented
distinct patterns of linguistic variation over time. At the most by the training corpora. We believe that this perspective is
| FrontiersinArtificialIntelligence |     |     |     |     |     |     |     | 05  |     |     |     |     | frontiersin.org |     |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- |

Grieveetal. 10.3389/frai.2024.1472411
FIGURE2
Representativecorpusdesign.Thisfigurepresentsacorpusasarepresentativesampleoftextstakenfromagivenvarietyoflanguage(i.e.,froma
largerpopulationoftextsdelimitedbyrelevantextra-linguisticfactors).Thisfigurealsoillustrateshowcompilingacorpusthataccuratelyrepresents
atargetvarietyrequiresaccesstoanunderlyingmodelofthatvarietyoflanguage,includingitsinternalsub-varieties,sothatthecorpuscanbe
stratifiedsoastocaptureinternalvariationinthatvariety.Naivecorpuscompilationstrategiesthatrelyonconveniencesamplingwillgenerallylead
tolessrepresentativesamples.
not only novel but fundamental to understanding the nature of 3 Challenges
| language modeling | and how               | to maximize | the societal          | value of  |            |      |     |     |
| ----------------- | --------------------- | ----------- | --------------------- | --------- | ---------- | ---- | --- | --- |
|                   |                       |             |                       |           | 3.1 Social | bias |     |     |
| LLMs. To          | support and exemplify | this        | claim, in the         | remainder |            |      |     |     |
| of this paper,    | we therefore          | consider    | specific implications | of        |            |      |     |     |
NLPsystemsgenerallysufferfromsocialbias:theirreal-world
| this sociolinguistic | conception | of language | modeling | for | a   |     |     |     |
| -------------------- | ---------- | ----------- | -------- | --- | --- | --- | --- | --- |
range of different challenges currently being faced in language applicationleadstooutcomesthatunfairlydisadvantageorharm
|          |                   |            |           |         | specific social | groups (Shah | et al., 2020; Blodgett | et al., 2020; |
| -------- | ----------------- | ---------- | --------- | ------- | --------------- | ------------ | ---------------------- | ------------- |
| modeling | primarily through | a critical | review of | the NLP |                 |              |                        |               |
literature from the sociolinguistic perspective introduced in Dev et al., 2022; Navigli et al., 2023; Luo et al., 2024). Social
thissection. biascanbeintroducedatvariouspointsduringthedevelopment
| FrontiersinArtificialIntelligence |     |     |     |     | 06  |     |     | frontiersin.org |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --------------- |

Grieveetal. 10.3389/frai.2024.1472411
and deployment of NLP systems (Hovy and Prabhumoye, 2021), like disparagement and dehumanization (Dev et al., 2022), where
butgiventheunsupervisednatureoflanguagemodeling,training negative viewpoints about specific social groups are propagated,
corpora are a key source of social bias in LLMs (Bender et al., as has been widely discussed in regards to LLMs (Bender et al.,
2021;Ferrara,2023).WhilebiasinNLPsystemscanharmpeople 2021). Once again, it is clear that this issue can be traced back,
invariousways(Blodgettetal.,2020),inthissection,weprimarily at least in part, to the data the language model was trained on.
focus on two common harmful outcomes of social bias. These If the training corpus contains relatively frequent expression of
two types of harms are most commonly discussed in terms of harmful or inaccurate ideas about certain social groups—as we
quality-of-service harms and stereotyping harms (e.g., Crawford, can safely assume any large, unconstrained sample of internet
2017; Blodgett, 2021; Dev et al., 2022; Weerts, 2021; Leidinger writings will—language models will inevitably reproduce those
andRogers,2024;Chehbounietal.,2024;Hofmannetal.,2024), biases (Bender et al., 2021; Ferrara, 2023; Hofmann et al., 2024).
althoughmanydifferentsystemshavebeenproposedforclassifying AsBenderetal.(2021,613)state,“large,uncurated,Internet-based
biases and harms in NLP, which define these terms in somewhat datasets encode the dominant/hegemonic view, which further
differentways,alongwithmanyadditionalandoftenoverlapping harmspeopleatthemargins.”Thesetypesofharmsaregenerally
categories(Blodgettetal.,2020).Bothofthesetypesofharmsare the product of semantic bias, as they result from the meaning
especiallyrelevanttoLLMs,andcruciallywebelievebothcanbe relationshipsbetweenwordsinferredbythelanguagemodelbased
betterunderstoodandaddressedinlanguagemodelingbyadopting on patterns of co-occurrence observed in the training corpus
asociolinguisticperspective(seeFigure3). (Shahetal.,2020).
First, social bias can be characterized by poor system From a sociolinguistic perspective, we believe social bias in
performance for certain social groups that are interacting with language models can be addressed at a basic level by pretraining
languagemodelsandapplicationsbasedonlanguagemodels:token on corpora that more accurately represent the target variety.
prediction will be more or less accurate depending on the social Imbalanceinpretrainingdataisarecognizedasageneralsource
origins of the language inputted into the system. For example, of social bias in language modeling (Yogarajan et al., 2023;
ChatGPT might have difficulty correctly understanding prompts Kocijan,2021;Hofmannetal.,2024).Althoughsocialbiascanbe
written by people from certain social groups due to their use of partiallydetectedorresolvedbymanipulatingtheembeddingspace
non-standard or socially restricted language patterns. This type (Caliskan et al., 2017), the probability table (Salazar et al., 2019),
of bias leads to what is known as quality-of-service harms, ortheoutputofthetextgenerationprocess(BordiaandBowman,
where the performance of these systems varies depending on the 2019),theseapproacheshavenumerouslimitations.Forexample,
social background of the user (Crawford, 2017; Dev et al., 2022; models that are de-toxified following pretraining will tend to
Chehbouni et al., 2024). These types of quality-of-service harms generatelesscontentaboutthesocialgroupthathadbeenthetarget
canoftenbetheproductofselectionbias,astheyresultfromhow oftoxicdiscourse,inadvertentlyleadingtotheerasureofthatsocial
training data is selected from across the society whose language group(Xuetal.,2021).Moregenerally,thesetypesofinterventions
is being modeled (Shah et al., 2020): in general, if language data all fall outside the basic language modeling task, focusing on
fromcertainsocialgroupsisunder-representedinthetrainingdata suppressingbias-relatedparameters(Liuetal.,2024),ratherthan
for a language model, we should expect that applications of that pretraining better underlying language models. To address bias
modelwillprocesslanguagestructuresproducedbythesegroups in language models at a fundamental level requires intervention
less accurately and consequently exhibit poorer performance for at the pretraining stage (Yogarajan et al., 2023; Hofmann et al.,
thesegroups(Blodgettetal.,2020;Lahotietal.,2023). 2024). Our claim is that this type of intervention can be pursed
Notably, quality-of-service harms, especially those resulting inaprincipledmannerbypretrainingoncorporathataccurately
from selection bias, have been one of the central concerns in represent the target variety of language, as identified through
computational sociolinguistics (Nguyen et al., 2016; Eisenstein, sociolinguisticanalysis.
2017; Grieve et al., 2023). Researchers in this emerging field Furthermore, we believe that it is especially important that
have stressed for the past decade that the performance of NLP the training corpus represents the internal structure of the target
systems generally varies for people from different social groups variety, in the sense that the sub-varieties of that variety of
andhavecalledforengagementwithdescriptionandtheoryfrom language, including most importantly the major dialects of that
sociolinguisticstohelpaddressthisbasicformofsocialbias(e.g., variety of language, are adequately represented in the training
Hovy and Søgaard, 2015; Jórgensen et al., 2015; Blodgett and corpus, reflecting both the size and distinctiveness of those
O’Connor, 2017; Jurgens et al., 2017; Schramowski et al., 2022; dialects. This challenge is illustrated in Figure3, which shows
Hofmannetal.,2024). how a language model for American English could be biased
Second,socialbiascanbecharacterizedbysystemsthatproduce toward one regional dialect or biased against another in various
outputs that directly harm or discriminate against certain social ways. For example, a corpus intended to represent American
groupsevenwhentheyarenotdirectlyengagingwiththesesystems English, but which is primarily composed of texts collected from
themselves.Forexample,whenprompted,ChatGPTmightbemore a specific dialect of American English (e.g., texts written by
likely to produce negative portrayals of certain ethnicities and highlyeducated,middle-class,whiteAmericansfrommajorcoastal
genders,nomatterwhoisdoingtheprompting(Bommasanietal., cities),cannotadequatelyrepresentthefulldiversityofAmerican
2021;Lahotietal.,2023).Mostnotably,thistypeofbiascanleadto English. Any language model trained on such a corpus should
whatisknownasstereotypingharms(Crawford,2017;Leidinger therefore be expected to be biased against social groups that are
andRogers,2024;Hofmannetal.,2024),aswellasrelatedharms underrepresented in the training data, such as African American
FrontiersinArtificialIntelligence 07 frontiersin.org

Grieveetal. 10.3389/frai.2024.1472411
FIGURE3
Sociolinguisticbiasinlanguagemodels.Thisfigureillustrateshowtraininglanguagemodelsoncorporathataccuratelyrepresentthetargetvarietyof
languageincludingitsinternalstructure,especiallyitsconstituentdialects,canpotentiallyhelpaddresssocialbias,includingbothquality-of-service
harmsandstereotyping.ThisisexemplifiedbycomparingtwohypotheticalmodelsofAmericanEnglish,whicharetrainedoncorporathat
inaccuratelyandaccuratelyrepresentregionaldialectvariation(basedonGrieve,2016)inthisvarietyoflanguage.
English from the Southern US, compared to a language model English: if a model were only trained on American English,
trained on a corpus that more accurately represents variation in it would be much more likely to misinterpret the meaning
AmericanEnglish. of words that tend to have different meanings in British
The link between corpus design and quality-of-service harms English, like boot (for trunk) or underground (for subway).
inLLMsisespeciallyclear:becauselanguagevariesinsystematic Consequently, the quality of service provided by applications
ways,toensurealanguagemodelcanaccuratelyprocesslanguage based on that model for speakers of British English would
from a wide range of social groups, it should be trained on bedegraded.
corpora that represent the language used by a wide range of Stereotypingandrelatedformsofdiscriminationgeneratedby
social groups, i.e., their dialects, as illustrated in Figure3. For LLMshavealsooftenbeentracedbacktoissueswithdatacollection
example, consider lexical variation in British and American and curation (Bender et al., 2021). A sociolinguistic perspective
FrontiersinArtificialIntelligence 08 frontiersin.org

Grieveetal. 10.3389/frai.2024.1472411
potentially provides a principled solution to this problem: in This approach is often referred to as further pretraining
general, stereotyping harms could be addressed by training on because it involves extending the basic form of unsupervised
data that better represents the language produced by a wider languagemodelingusedtotrainthebasemodeltonewdatafrom
range of social groups. One reason that certain social groups are the more specific target domain (Gururangan et al., 2020). The
negativelyportrayedbyLLMsisthattheyarenotallowedtoportray goalissimplytoimprovetheaccuracyoftokenpredictioninthe
themselves, in their own words, in the data used for training. targetdomain,whilepreservingtheunderlyingfluencyofthebase
By training on corpora that equitably and deliberately represent model. For example, a base model trained on huge amounts of
the internal varietal structure of the target variety, especially unrestrictedonlinelanguagedatacouldbeadaptedtothespecific
the range of dialects of which it is composed, we believe that domainofcustomerservice:basedonacorpusofcustomerservice
stereotypingandotherformsofsemanticbiascanbemitigated(see transcripts, the parameters of the base model would be adjusted
Figure3). In other words, modeling data from a wider range of to improve the ability of the model to predict word tokens in
dialects—and,byextension,fromawiderrangeofsocialgroups— texts from that domain given the topics of discussion and the
would help ensure that a wider range of viewpoints would be specifictypesofinteractionsthatcharacterizethatdomain(Chen
representedbyalanguagemodel.Stratifiedcorporathataccurately et al., 2024). In practice, further pretraining has been proven
representthesociolinguisticstructureofthetargetvariety(i.e.,its to be an effective way of improving the performance of LLMs
constituentsub-varieties)couldalsopotentiallybeusedtoevaluate across a wide range of downstream tasks, including medical text
and probe a model, allowing for social bias to be identified and processing(Lehmanetal.,2023;NaziandPeng,2024),cross-lingual
interpreteddirectly. transfer (Aggarwal et al., 2024), and named-entity recognition in
Thesociolinguisticapproachtolanguagemodelingadvocated low-resourcesdomains(Mahapatraetal.,2022).
for in this paper therefore provides a simple yet theoretically Althoughtheimportanceofdomainadaptationhaslongbeen
grounded basis for understanding the general source of social appreciated in language modeling (Rudnicky, 1995; Chen et al.,
biasinlanguagemodeling,includingforaddressingbothquality- 2024), we believe that this process can be reframed directly and
of-service and stereotyping harms, as well as other related types insightfullyinsociolinguisticterms,wheredomainisunderstood
of harms. In addition, a sociolinguistic approach offers a clear as a variety of language. If the goal of the base model is seen
pathway for both interpreting and addressing these different asaccuratelypredictingwordtokensinabroadlydefinedvariety
forms of social bias during pretraining through careful corpus of language, like the English language, then the goal of domain
compilationinformedbyscientificunderstandingofthenatureof adaptation can be seen as the process of fine-tuning the base
linguisticvariationwithinthatspecifictargetvariety,basedeither model to allow it to predict word tokens more accurately in
onexistingornewsociolinguisticresearch.Crucially,however,such a more narrowly defined variety of that language—the sub-
sociolinguistic interventions need not necessarily occur during variety associated with the target domain. Crucially, the adapted
the initial pretraining of the base model, but can be pursued model should be expected to be more accurate because more
throughthefurtherpretrainingofbasemodels,aswediscussinthe narrowly defined varieties of language must be characterized
nextsection. by less variation than any larger variety that encompasses it.
This process can also potentially be carried out in an iterative
manner, where a base model is repeatedly adapted on corpora
representing more narrowly defined varieties of language, as
showninFigure4,whichillustratesasociolinguisticallyinformed
3.2 Domain adaptation approach to domain adaption, where a model is iteratively fine-
tuned on corpora representing increasingly narrowly defined
Despite their remarkable fluency and general applicability, varietiesofcomputer-mediatedcommunication.
LLMs generally benefit from some form of domain adaptation A sociolinguistic perspective on domain adaptation therefore
before deployment (Radford et al., 2019; Gururangan et al., sees the target domain as a variety of language. This means
2020). In NLP, domain adaptation is the task of improving the that the process of domain adaptation can be informed by
performance of a system that was developed using language linguistic analysis that rigorously identifies maximally distinctive
data collected in one domain for a different and often more varieties of language. This can include both existing research in
specific domain where the system is to be applied—the real— sociolinguistics, dialectology, and related fields, as well as new
world context where the system is used, such as texts about researchconducteddirectlytosupportmodeltrainingforspecified
a particular topic or from a particular genre (Daumé, 2007). domains. For example, if a base model is adapted for a specific
Althoughtherearemanyapproachesforadaptinglanguagemodels, regionoftheUS,empiricalresearchinAmericandialectgeography
includingfordifferentdownstreamtasks—includingreinforcement (e.g., Grieve, 2016) should be consulted to precisely define the
learning from human feedback (Ouyang et al., 2022), low- sub-region that is being targeted for adaptation (see Figure3).
rank adaptation (Hu et al., 2021), and low-tensor rank weight Similarly, if a base model is adapted for a specific type of blog
adaptation (Bershatsky et al., 2024)—we focus on the process of writing, empirical research on register variation in blogs (e.g.,
fine-tuning a base model by extending unsupervised language Grieveetal.,2010)shouldbeconsultedtopreciselydefinethesub-
modeling on a corpus of texts sampled from a specific target typeofblogwritingthatisbeingtargetedforadaptation.Notably,
domain (Gururangan et al., 2020; Hu et al., 2021; Hou et al., recentresearchinNLPhasbeguntoofferempiricalevidencefor
2022). the value of this approach in downstream tasks. For example, in
FrontiersinArtificialIntelligence 09 frontiersin.org

Grieveetal. 10.3389/frai.2024.1472411
FIGURE4
Sociolinguisticadaptationoflanguagemodels.Thisfigureillustrateshowanunderstandingofthesociolinguisticstructureofvarietiesoflanguages
caninformtheadaptationoflanguagemodels.Languagemodeladaptationcanbeseenastheprocessoffine-tuningabasemodel,potentiallyinan
iterativemanner,topredictwordtokensinamorenarrowlydefinedvarietyoflanguagethatissubsumedbythelargervarietyoflanguage
representedbythebasemodel.
hatespeechdetection,adaptingtheunderlyinglanguagemodelsto from that variety, drawn without taking into account its internal
whatareeffectivelytargetdialects(Pérezetal.,2024)andregisters structure,mightseverelyunder-representsub-varietiesofinterest.
(Nirmal, 2024) has been found to lead to improvements in the Forexample,asocialmediacorpusmaybedominatedbycertain
overallperformanceofthesesystems. sub-registers(e.g.,abusiveorpromotionalposts)thatarenotthe
Crucially, sociolinguistics does not only provide a basis for intendedtargetofadaptation,whilethesub-registersthatarethe
identifying valid targets for domain adaptation but for mapping intended target of adaptation (e.g., interactive or informational
andmodelingtheinternalstructureofthesetargetvarieties.Thisis posts)maybelimited.Similarly,peoplefromcertainsocialgroups
especiallyimportantbecausetargetvarietiesfordomainadaptation may be underrepresented in specific domains, resulting in social
are often well-defined by default. For example, if a fine-tuning biasbeinginadvertentlyexacerbatedbynaivedomainadaptation.
corpus is collected by sampling data from a particular social Inmanycases,thetargetvarietycannotevenbeaccuratelydefined
mediaplatform,arelativelyhomogeneousvarietyoflanguagewill until the overall structure of the larger variety in which it is
have naturally been targeted; however, a random sample of texts subsumedisunderstoodthroughcarefulsociolinguisticanalysis.
FrontiersinArtificialIntelligence 10 frontiersin.org

Grieveetal. 10.3389/frai.2024.1472411
A sociolinguistic perspective also highlights a more general Christian, 2021; Ngo et al., 2022; Dung, 2023). Misalignment
problem with domain adaptation: the success of this process arises not simply when AI systems fail to achieve their intended
dependsontherelationshipbetweenthelargervarietyrepresented goals,butwhentheypursuethesegoals,evensuccessfully,inways
by the base model and the smaller target variety toward which thathavenegativeorunforeseenconsequencesorthatarenotin
the base model is being adapted. Ideally the variety of language accordancewithsocietalvalues,forexample,inwayssocietyfinds
represented by the base model would completely subsume the tobeinappropriate,unethical,immoral,ordishonest.Alignment
target variety: the target variety would be a sub-variety of the is therefore the general process of guiding AI systems to behave
base variety, regardless of whether it was represented directly in in ways that are consistent with the broader expectations of
the base training data. However, the target variety may not be society, while discouraging them from behaving in ways that are
adequately represented in the data sampled for training the base inconsistentwiththeseexpectations,especiallytoavoidunintended
model.Forexample,thetargetvarietycouldbeassociatedwitha risksandharms(RussellandNorvig,2016).Crucially,thechallenge
social group or a social context that is severely underrepresented is not only how to guide AI systems but where to guide them
in the base training corpus. In such situations, fine-tuning (Gabriel,2020).
regimesinformedbysociolinguistictheoryanddescriptionwould Althoughalignmentisalong-standingconcerninAI(Wiener,
likely be beneficial by providing a basis for identifying these 1960), attention has grown in recent years due to the growing
varieties and sampling language directly from these contexts complexity and ubiquity of real-world AI systems, especially
andcommunities. systems based on language models (Shen et al., 2023; Liu et al.,
Understandingthesociolinguisticstructureofthelargervariety 2022,2023;Wangetal.,2023;Wolfetal.,2023),whichpotentially
of language could also allow models to be adapted to represent allowformisalignmenttoemergeonmanydifferentlevels(Gabriel,
targetvarietieswithmissingdata.Ifempiricalresearchinlinguistics 2020; Dung, 2023). For example, consider a generative language
has found that a target dialect or register for which data is modelthatautomaticallyproducesreviewsofscientificliteratureon
lackingfallsbetweenmultipledialectsorregistersforwhichdata aspecifiedtopic.Anobviouslymisalignedsystemmightproduce
is available, a model could be adapted for the target variety reviews that are clearly wrong—incoherent or incorrect—while a
by training on a combination of the available corpora. Overlap less obviously misaligned system might produce fluent reviews,
between varieties could also be exploited in a similar way: for completing the task successfully in a superficial way, but getting
example, if data is lacking for a target variety defined in terms factswrong,forexample,referencingpublicationsthatdonotexist.
of a specific register and a specific dialect, a model could be Thistypeofahallucination—thepresentationoffalseinformation
adapted for the target variety by fine-tuning on a combination asifitistrue—isacommonformofmisalignmentinLLMs(Evans
of corpora that represent that specific register and that specific et al., 2021; Tonmoy et al., 2024). A more insidiouslymisaligned
dialect. These types of techniques could even be used to create system, however, might produce perfectly accurate and fluent
a model of a variety of language that does not yet exist— synthesesthatciterelevantliterature,butexhibitotherproblematic
engineeredbytrainingoncorporarepresentingdifferentregisters behaviors,suchaslimitingreferencestocertainideasorresearchers
anddialects. incertainfields,therebyeffectivelysuppressingcertainviewpoints
Finally,itisimportanttostressthatourproposalisnotmeant (Benderetal.,2021).
to be a simple solution to the problem of domain adaptation A basic approach for aligning language models involves
that can be applied mechanically or without sociolinguistic pretrainingorfurtherpretrainingoncorporathatareconsidered
expertise. Given the complexity of language variation and to be more aligned with the values and expectations of society
change, we do not believe such an approach is possible. A (Solaiman and Dennison, 2021). How such corpora can best be
sociolinguistic approach to domain adaptation must draw upon compiled,however,isfarfromclear.Aswehavearguedthroughout
detailed empirical research on that specific variety of language this paper, sociolinguistic theory provides a basis for compiling
and its constituent sub-varieties to direct the compilation of bettertrainingcorpora.Inthegeneralcaseofalignment,webelieve
representative training corpora. If this empirical research has languagemodelscanbealignedwiththevaluesandexpectations
already been conducted by sociolinguists, it can be consulted of society, crucially without pre-specifying what exactly these
directly, but if no such research exists, new sociolinguistic valuesandexpectationsare,bytrainingoncorporathataccurately
research would need to be conducted. Although this research representtherangeofvarietiesfoundinthatsociety.Asdiscussed
would be grounded in general methods for sociolinguistic in terms of social bias, language models can be trained to better
analysis, the results would necessarily be specific to that variety alignwiththegeneralvaluesofasociety,asopposedtothevalues
oflanguage. of some particular social group within that society, by balancing
training data originating from different dialects. Similarly, as
discussedintermsofdomainadaptation,languagemodelscanbe
trained to better align with expectations that they will perform
3.3 Alignment adequately across the range of communicative contexts found in
that society by balancing training data originating from different
The challenges of social bias and domain adaptation can be register.Thisisbecausethevaluesandexpectationsofasocietyare
seen as forms of the more general alignment problem—how to instantiatedintheirpatternsoflanguageuse.
ensure that the behavior of AI systems aligns with the values In addition to addressing specific alignment issues related to
andexpectationsofsociety(Gabriel,2020;Hendrycksetal.,2020; social bias and domain adaptation, we believe a sociolinguistic
FrontiersinArtificialIntelligence 11 frontiersin.org

Grieveetal. 10.3389/frai.2024.1472411
approach can potentially help us train models that are less A related issue that has caused growing concern in language
susceptibletounethicalanddishonestbehaviorsingeneral (Huang modeling is that over time more and more real-world language
C.etal.,2024).Thisisbecauserespectingsociolinguisticdiversity will presumably be produced with the assistance of LLMs, which
entailstrainingmodelsondatathatrepresentsagreaterdiversity willmakeitincreasinglydifficulttocompilecontemporarycorpora
ofviewpoints,experiences,andopinions.AsLLMsaremodelsof of real human language for training new models or updating
varietiesoflanguage,theywillbebettermodels,morealignedwith existingones(Shumailovetal.,2023).Proposedsolutionstothese
theneeds,expectations,andvaluesofsociety,whentheyaccount problems of data contamination (Balloccu et al., 2024) and task
for the full range of sub-varieties, and hence the full range of contamination (Li and Flanigan, 2024) generally involve finding
perspectives, found within that society. In general, we therefore waystoexcludemachine-generatedlanguagefromfuturetraining
believe that a major source of LLM misalignment comes from data,includingthroughwatermarkingsystems(Kirchenbaueretal.,
what we call varietal misalignment and that LLM misalignment 2023; Dathathri et al., 2024). These types of solutions, however,
canthereforebeaddressed,atleastinpart,bycompilingtraining wouldseemeasytoconfound,ifonlybecausetheydonotgenerally
corporatoaccuratelyrepresentthevarietalstructureofthetarget allow texts written collaboratively by human and machine to be
variety,asidentifiedthroughsociolinguisticanalysis. identified, which is likely to become increasingly common and
Finally, it is important to acknowledge that while a diversifiedineverydaylife.
sociolinguistic perspective can provide a basis for aligning DespiterealconcernsaboutLLMdetectionincertaincontexts
language models for the society that it is intended to serve, this (Bommasani et al., 2021; Bian et al., 2023), the rising use of
approachdoesnotensurethattheresultantlanguagemodelswill LLMs to generate language is not difficult to reconcile with
be aligned with the ethical and moral aspirations of that society. sociolinguistic theory and practice. Over time, AI systems based
For example, a generative language model trained on a socially on language models will undoubtedly start to change how we
balanced corpus of the English language will still potentially use language. Texts generated with the help of language models
produce texts that express racist viewpoints because a portion of willincreasinglyenterintotherealworld.Atthispoint,froman
English texts expresses racist viewpoints. There might be greater externalistperspective(Scholzetal.,2024),thesetextswillbepart
equity in the types of stereotypes it spreads, but such behavior oflanguage—produced,transmitted,andunderstoodbyhumansas
can still be seen as a form of misalignment. A sociolinguistic language,oftenindistinguishablefromhuman-generatedlanguage
perspective, however, also provides a possible solution to this in the regular flow of real-world language use. Ultimately, the
problem—by deliberately weighting the varieties of language distinctionbetweenhuman-andmachine-generatedlanguagecan
represented in the training corpus. For example, if a particular thereforebeseenassimplyanotheraspectofregisterthatdefines
social group has been broadly disadvantaged or has a worldview variationwithinvarietiesoflanguage,justlikeallcommunicative
that society wishes to encourage, the portion of the corpus technologies that have come before, including the invention of
representingtherelevantvarietiesoflanguagecanbemoreheavily writinganddigitalcommunication.
weightedduringpretrainingorfurtherpretraining.Inthisway,a Taking a sociolinguistic perspective, it is also important to
sociolinguisticperspectivecanprovideatheoreticalbasisnotonly acknowledge that the rise of language models is creating new
forbalancingbutforcontrollingthealignmentoflanguagemodels. varietiesoflanguage,includingthosecharacterizedbythelinguistic
interaction between humans and machines, such as dialogues
with ChatGPT (Mavrodieva, 2023). These new varieties, which
will only continue to diversify over time, will also need to be
3.4 Language change
accounted for, like all varieties of language, both by theories of
sociolinguistic variation and by the evolving language models
Thus far, our discussion has focused on how a series of designed to represent contemporary language use. If language
challenges in language modeling related to bias, adaptation, and models are to be kept up-to-date, machine-generated language
alignment more generally can be addressed, in principle, by cannot be excluded, as its production will become a significant
building training corpora that better represent the dialects and driveroflanguagechange.
registersofthetargetvariety.Anotherformofthisbasicproblem
involvesensuringthatlanguagemodelsandapplicationsbasedon
language models are responsive to language change and cultural
change more generally (Bender et al., 2021; Bommasani et al., 3.5 Scale
2021).Allvarietiesoflanguagechangeovertime,ofteninwaysthat
aredifficult,ifnotimpossible,topredict(Lass,1997).Iflanguage In addition to more specific insights into the development
modelsaretomaintaintheirfluencyandnotbecomeobsolete,they and deployment of language models, we believe a sociolinguistic
mustthereforebecontinuouslyupdatedusingtrainingcorporathat perspective can also help to explain the remarkable success of
consistofexamplesofcontemporarylanguageuse.Inprinciple,this LLMs, which has been attributed both to the development of
problemcanberesolvedbycompilingnewcorporaovertimethat new deep learning architectures and the use of extremely large
consistently represent the target variety and its evolving internal corpora of natural language for pretraining (Kaplan et al., 2020;
varietalstructure.Thechallengeisthereforetounderstandhowthe Bender et al., 2021; Bommasani et al., 2021). Although there is a
sociolinguisticlandscapeofregistersanddialectswithinthatvariety clear relationship between the scale of the training data and the
oflanguagehaschangedovertime,whichcanonlybeaccomplished success of these systems (Sardana and Frankle, 2023; Hoffmann
accuratelythroughdetailedandongoingsociolinguisticanalysis. et al., 2022; Bahri et al., 2024), it is unclear why increasing
FrontiersinArtificialIntelligence 12 frontiersin.org

Grieveetal. 10.3389/frai.2024.1472411
the amount of training data results in such great increases in considerableresearchonquantifyingtheoveralldegreeoflinguistic
performance. Is there a limit to how much performance can be diversityandcomplexityincorporainbothdialectology(Wieling
gained simply by increasing the scale of the training data? How and Nerbonne, 2015; Röthlisberger and Szmrecsanyi, 2020) and
canmorepowerfulmodelsbedevelopedwithlessdata?Theseare registeranalysis(Ehret,2021;Biberetal.,2021).
fundamental questions for LLM development (Bommasani et al., This sociolinguistic perspective also provides an answer to
2021),especiallybecauseofthesignificantcostsandenvironmental questionsaboutthelimitsofincreasingthescaleoftrainingdata
impacts associated with increases in scale (Bender et al., 2021). (Bommasanietal.,2021).Atwhatpointshouldincreasingthesize
Webelievethesearequestionsthatcanbeuniquelyinformedby ofthetrainingcorpusnolongerleadtosubstantialimprovements
asociolinguisticperspective. in model performance? Our hypothesis is that increasing the
Theobviousreasonwhyincreasingtheamountoftrainingdata scale of training data will continue to increase the performance
providedtoalanguagemodelimprovesitsperformanceisthatthis of language models so long as it also results in an increase in
provides the model access to a wider range of language patterns thesociolinguisticdiversityinthetrainingcorpus.Crucially,this
(Shumailovetal.,2023).ThisispresumablywhyLLMsbenefitfrom impliesthatattemptstoempiricallyassessthelimitsofscalesimply
being pretrained on such large corpora of natural language: the bycomparingmodelperformanceastheamountoftrainingdata
same levels of performance could not be achieved by pretraining increaseswillnotbeaccurate,unlessthesociolinguisticdiversityof
twiceaslongonhalfthedata.Scaleisthereforenotsufficienton thecorpusisalsocontrolledforandmeasuredalongsidecorpussize
itsown.Whatmattersisnotsimplythescaleofthetrainingdata (Hoffmannetal.,2022).
butthediversityofthetrainingdata.Althoughtheimportanceof Thisinsightisdirectlyrelevanttodefiningscalinglaws(Bahri
the diversity of training data has often been stressed in critical etal.,2024)forlanguagemodels(Bommasanietal.,2021),which
discussions of LLMs (Brown et al., 2020; Bender et al., 2021), are attempts to specify how much data is needed to train a
the sociolinguistic perspective advocated in this paper provides a languagemodelwithagivennumberofparameters.Thisissuehas
theoretical basis for understanding this relationship with greater most famously been discussed in terms of what is known as the
precision: diversity in the training corpus, in terms of both its ChinchillaLaw,whichstatesthat,foreachparameterinanLLM,20
linguisticstructureanditssemanticcontent,canbeseenasdirectly tokensoftrainingdataisoptimal(Hoffmannetal.,2022).Bythis
reflectingthediversityofthevarietiesoflanguagerepresentedby standard,GPT-3,forexample,ismuchtoolargegiventheamount
thatcorpus.Tomaximizetheperformanceoflanguagemodelsand oftrainingdata.Fromasociolinguisticperspective,however,any
theefficiencywithwhichtheseimprovementscanbeobtained,we suchcalculationsseemoverlysimplistic,astheyignorethediversity
therefore believe it is more important to prioritize the amount of the training data. This issue has not been entirely missed in
of varietal diversity in the training data over scale. This can be languagemodeling.Forexample,theChinchillaLawassumesthe
achieved by carefully representing a wider range of varieties in trainingdataisof"highquality",althoughexactlywhatthismeans
thetrainingdata,includingbothdialectsandregisters,grounded andhowthiscanbeassessedisalargelyunexploredtopic(Sardana
on empirical sociolinguistic analysis of the target variety and its andFrankle,2023).Measuringtheoveralldegreeofsociolinguistic
internalpatternsoflinguisticvariation. diversityintrainingdatacanprovideabasisformakingthesetypes
Notably,empiricalevidenceforprioritizingdiversityintraining ofassessments.
data in language modeling is building. In addition to research Finally,asociolinguisticperspectivealsoofferscleardirection
on debiasing (Hofmann et al., 2024) and domain adaptation fortrainingmodelsusinglimitedamountsofdata.Thisisespecially
(Gururangan et al., 2020) that has stressed the importance of important issue when the goal is to build language models for
further pretraining on diverse data, the superior performance under-resourcedvarietiesoflanguage,whereobtainingsufficiently
of GPT-3 over GPT-J—both of which share the same base largecorporafortrainingmodelsisamajorchallenge(Benderetal.,
model architecture—provides an especially clear evidence of the 2021; Ramesh et al., 2023). Specifically, if the value of training
importanceofdiversityoverscale(WangandKomatsuzaki,2021; data is largely determined by the diversity of training data, great
Brownetal.,2020).GPT-3isgenerallyconsideredtohavebenefited care should be taken to maximize the amount of sociolinguistic
from OpenAI’s carefully curated, even if largely undocumented, diversity,bothintermsofdialectandregistervariation,inthedata
training dataset, whereas GPT-J was pretrained on an open data usedtotrainlanguagemodelsforunder-resourcedvarieties.
set called the Pile (Gao et al., 2020), which is presumably far less
carefullycurated. Anothersource ofevidencefortheimportance
4 Conclusion
of diversity in training data is the rapid degradation of model
performance and breaks in information integrity that have been
foundtooccurwhenLLMsaretrainedondatageneratedbyother In this paper, we have proposed that, in general, language
LLMs,whichisinherentlyfarlessdiversethanlanguageproduced models inherently represent varieties of language. Our claim is
by humans (Shumailov et al., 2023), as has been demonstrated that whenever tokens are predicted based on the observation of
repeatedlyinrecentresearchonLLMdetection(Bevendorffetal., linguistic patterns in corpora of natural language, the resultant
2024;HuangandGrieve,2024). language model is necessarily a model of the variety of language
Asociolinguisticperspectiveprovidesabasisforassessingthe representedbythatcorpus.Byextension,wehavearguedthatthe
diversityoftrainingdataandtheeffectofvaryingthediversityof performance,utility,andethicalapplicationoflanguagemodels,as
training data along multiple dimensions on the performance of wellasanyNLPsystemsintowhichtheareembedded,depends
the resultant models in a meaningful way. For example, there is onhowwellthecorporaonwhichtheyaretrainedrepresentthe
FrontiersinArtificialIntelligence 13 frontiersin.org

Grieveetal. 10.3389/frai.2024.1472411
varietiesbeingmodeled,includingtheirinternalvarietalstructure. sociolinguistics.Thisperspectiveisalsonotablyquitedifferentfrom
In other words, we believe that the performance and societal discussionsoflanguagemodelinginlinguistics,whichhavefocused
value of language models is determined not only by the amount onthestatusofLLMsasmodelsoflanguagecognition(Piantadosi,
of language data used for training but by the sociolinguistic 2023; Dentella et al., 2023; Marcus et al., 2023; Tsvilodub et al.,
diversity and representativeness of these corpora. Crucially, the 2024). In this article, we have attempted to shift this discussion,
arguments we have presented in this paper are intended to be focusing instead on understanding language models as models of
relevant to any form of language modeling—not only current languageuse,whichwebelievehasfarmoredirectandimmediate
transformer-basedmodels,butsimplertraditionalmodels,aswell consequences for the development and deployment of language
as future approaches to language modeling that have not yet modelsintherealworld.
beendeveloped. Our basic claim is therefore that language models can
For these reasons, we believe that drawing on insights from be improved in many ways by training on datasets that
sociolinguistics to direct the design, compilation, and curation endeavor to accurately represent the varieties of language
of training corpora will be critical to the future of language being modeled. We therefore believe that there is a clear
modeling, with widespread implications for their development and urgent need for engagement with sociolinguistic research
and deployment. Specifically, we have identified and discussed in language model design and evaluation. At the most basic
several challenges in language modeling—social bias, domain level, language models are models of how language is used
adaptation,alignment,languagechange,andscale—thatwebelieve for communication within society. Understanding the structure
a sociolinguistic perspective could help address in a principled of society, and how this structure is reflected in patterns of
and unified manner. Although our goal in this paper has language use, is therefore critical to maximizing the benefits of
been to introduce this new perspective on language modeling language models for the societies in which they are increasingly
through a theoretical discussion grounded in existing research beingembedded.
in sociolinguistics and NLP, we hope our proposal will act as a Finally, in this paper, we have focused exclusively on
foundation and inspiration for future empirical research in this the basic task of language modeling (i.e., pretraining and
area, not only in NLP but in linguistics (Huang W. et al., 2024; fine tuning via further pretraining). Our goal has been to
HuangandGrieve,2024). explain how and why a sociolinguistically informed approach
Itisalsoimportanttoacknowledgethattherealreadyhasbeen to the curation of training data can improve the societal
considerable discussion of these types of challenges in language value of language models in general. Nevertheless, we believe
modelingandNLPmoregenerally,withproposalstoaddressthese sociolinguistic insight, and linguistic insight more generally, can
issues often emphasizing the need for more careful curation of inform the broader development and application of modern
training data (Bender et al., 2021; Hovy and Prabhumoye, 2021) LLMs,includingimprovingapproachestoreinforcementlearning
and for incorporating social and even sociolinguistic insight into (Ouyang et al., 2022), prompt engineering, and in-context
these models (Hovy, 2018; Hovy and Yang, 2021; Nguyen et al., learning (Chen et al., 2023), all of which are ultimately
2021; Yang et al., 2024), especially within the emerging field of grounded in patterns of language use. Moving forward, we
computational sociolinguistics (Nguyen et al., 2016; Grieve et al., therefore believe that research on language use—not only in
2023).Forexample,toaddressrisksrelatedtosocialbiasinLLMs, sociolinguistics, but in corpus linguistics, discourse analysis,
Bender et al. (2021, p. 610) recommend that resources must be pragmatics,cognitivelinguistics,andotherfieldsoflinguisticsthat
invested for “curating and carefully documenting datasets rather focusonunderstandinghowlanguageisusedforcommunication
than ingesting everything on the web,” while Yang et al. (2024, in the real world—will increasingly become central to advancing
p. 1) argue that issues with LLM performance are related to “a the field of language modeling, as well as NLP and AI
lack of awareness of the factors, context, and implications of moregenerally.
the social environment in which NLP operates, which we call
socialawareness”.
Author contributions
Whatwebelieveislackinginthesediscussions,however,isthe
identification of a general linguistic framework for solving these
typesofproblemswithinthebasicparadigmoflanguagemodeling, JGri: Conceptualization, Project administration, Writing –
especially one that is theoretically grounded in our scientific originaldraft,Writing–review&editing.SB:Conceptualization,
understandingoflanguagevariationandchange.Althoughthelack Writing – original draft, Writing – review & editing. MF:
of social diversity in training data has been repeatedly identified Conceptualization, Writing – original draft, Writing – review &
asaproblemforLLMs,whatexactlythismeansandhowexactly editing.JGra:Conceptualization,Writing–originaldraft,Writing
this can be measured and addressed in a principled manner – review & editing. WH: Conceptualization, Writing – original
has not been articulated. Given this emerging discourse, the draft,Writing–review&editing.AJ:Conceptualization,Writing–
primarycontributionofthispaperistoproposeatheoreticaland originaldraft,Writing–review&editing.AM:Conceptualization,
empiricalfoundationforaddressingawiderangeofchallengesin Writing – original draft, Writing – review & editing. MP:
languagemodelingthatisbaseddirectlyonsociolinguistictheory, Conceptualization, Writing – original draft, Writing – review &
specifically the concept of a variety of language—a topic that, editing.DR:Conceptualization,Writing–originaldraft,Writing–
to the best of our knowledge, has been absent from discussions review&editing.BW:Conceptualization,Writing–originaldraft,
of language modeling up until now, even within computational Writing–review&editing.
FrontiersinArtificialIntelligence 14 frontiersin.org

Grieveetal. 10.3389/frai.2024.1472411
Funding Conflict of interest
The author(s) declare financial support was received for the The authors declare that the research was conducted in the
research,authorship,and/orpublicationofthisarticle.SaraBartl, absenceofanycommercialorfinancialrelationshipsthatcouldbe
Alejandro Jawerbaum, and Dana Roemling were supported by construedasapotentialconflictofinterest.
the UKRI ESRC Midlands Graduate School Doctoral Training The author(s) declared that they were an editorial board
Partnership ES/P000711/1. Bodo Winter was supported by the memberofFrontiers,atthetimeofsubmission.Thishadnoimpact
UKRIFutureLeadersFellowshipMR/T040505/1. onthepeerreviewprocessandthefinaldecision.
Acknowledgments Publisher’s note
We would especially like to thank Dong Nguyen for her All claims expressed in this article are solely those of the
comments on this article, as well as Meike Latz for creating authors and do not necessarily represent those of their affiliated
the artwork presented in this article. This article also benefited organizations, or those of the publisher, the editors and the
from discussions with Su Lin Blodgett, Dirk Hovy, Huang He, reviewers. Any product that may be evaluated in this article, or
David Jurgens, Taylor Jones, and Emily Waibel, as well as claimthatmaybemadebyitsmanufacturer,isnotguaranteedor
threereviewers. endorsedbythepublisher.
References
Achiam, J., Adler, S., Agarwal, S., Ahmad, L., Akkaya, I., Aleman, F. Biber,D.(1993).Representativenessincorpusdesign.LiteraryLinguist.Comp.8,
L., et al. (2023). Gpt-4 technical report. arXiv [preprint] arXiv:2303.08774. 243–257.doi:10.1093/llc/8.4.243
doi:10.48550/arXiv.2303.08774
Biber,D.(1995).DimensionsofRegisterVariation:ACross-LinguisticComparison.
Aggarwal,D.,Sathe,A.,andSitaram,S.(2024).Exploringpretrainingviaactive Cambridge:CambridgeUniversityPress.doi:10.1017/CBO9780511519871
forgettingforimprovingcrosslingualtransferfordecoderlanguagemodels.arXiv
Biber,D.,andConrad,S.(2005).“Registervariation:acorpusapproach,”inThe
[preprint]arXiv:2410.16168.doi:10.48550/arXiv.2410.16168
HandbookofDiscourseAnalysis,eds.D.Tannen,H.E.Hamilton,andD.Schiffrin
Aitken, A. J. (1985). Is scots a language? English Today 1, 41–45. (Oxford:JohnWiley&Sons),175–196.
doi:10.1017/S0266078400001292
Biber,D.,andConrad,S.(2019).Register,Genre,andStyle.Cambridge:Cambridge
Baack,S.(2024).“Acriticalanalysisofthelargestsourceforgenerativeaitraining UniversityPress.
data:Commoncrawl,”inThe2024ACMConferenceonFairness,Accountability,and
Biber,D.,andEgbert,J.(2018).RegisterVariationOnline.Cambridge:Cambridge
Transparency(RiodeJaneiro:AssociationforComputingMachinery),2199–2208.
UniversityPress.
Bahri,Y.,Dyer,E.,Kaplan,J.,Lee,J.,andSharma,U.(2024).Explainingneural
Biber, D., Gray, B., Staples, S., and Egbert, J. (2021). The Register-Functional
scalinglaws.Proc.Nat.Acad.Sci.121:e2311878121.doi:10.1073/pnas.2311878121
ApproachtoGrammaticalComplexity:TheoreticalFoundation,DescriptiveResearch
Balloccu, S., Schmidtová, P., Lango, M., and Duvsek, O. (2024). Leak, cheat, Findings,Application.London:Routledge.
repeat:Datacontaminationandevaluationmalpracticesinclosed-sourceLLMs.arXiv
Birhane,A.,Kasirzadeh,A.,Leslie,D.,andWachter,S.(2023).Scienceintheageof
[preprint]arXiv:2402.03927.doi:10.48550/arXiv.2402.03927
largelanguagemodels.Nat.Rev.Phys.5,277–280.doi:10.1038/s42254-023-00581-4
Bamman,D.,Eisenstein,J.,andSchnoebelen,T.(2014).Genderidentityandlexical
Blodgett,S.L.(2021).SociolinguisticallyDrivenApproachesforJustnaturallanguage
variationinsocialmedia.J.Sociolinguist.18,135–160.doi:10.1111/josl.12080
Processing(PhDthesis).Amherst,MA:UniversityofMassachusettsAmherst.
Bell, A., Sharma, D., and Britain, D. (2016). Labov in sociolinguistics: an
Blodgett,S.L.,Barocas,S.,andDauméIII,H.,andWallach,H.(2020).“Language
introduction.J.Sociolinguist.20,399–408.doi:10.1111/josl.12199
(Technology)isPower: A Critical Survey of “Bias” inNLP,”inProceedings of the
Bender,E.M.,Gebru,T.,McMillan-Major,A.,andShmitchell,S.(2021).“Onthe 58thAnnualMeetingoftheAssociationforComputationalLinguistics(Associationfor
dangersofstochasticparrots:canlanguagemodelsbetoobig?,”inProceedingsofthe ComputationalLinguistics).
2021ACMConferenceonFairness,Accountability,andTransparency(Associationfor
Blodgett, S. L., Green, L., and O’Connor, B. (2016). Demographic dialectal
ComputingMachinery),610–623.
variationinsocialmedia:acasestudyofafrican-americanenglish.arXiv[preprint]
Bengio,Y.,Ducharme,R.,Vincent,P.,andJauvin,C.(2003).Aneuralprobabilistic arXiv:1608.08868.doi:10.18653/v1/D16-1120
languagemodel.J.Mach.Learn.Res.3,1137–1155.doi:10.1162/153244303322533223
Blodgett, S. L., and O’Connor, B. (2017). Racial disparity in natural language
BerberSardinha,T.(2018).Dimensionsofvariationacrossinternetregisters.Int.J. processing:acasestudyofsocialmediaafrican-americanenglish.arXiv[preprint]
CorpusLinguist.23,125–157.doi:10.1075/ijcl.15026.ber arXiv:1707.00061.doi:10.48550/arXiv.1707.00061
Bershatsky, D., Cherniuk, D., Daulbaev, T., Mikhalev, A., and Oseledets, I. Bommasani, R., Hudson, D. A., Adeli, E., Altman, R., Arora, S., von
(2024).LoTR:lowtensorrankweightadaptation.arXiv[preprint]arXiv:2402.01376. Arx, S., et al. (2021). On the opportunities and risks of foundation
doi:10.48550/arXiv.2402.01376 models. arXiv [preprint] arXiv:2108.07258. doi: 10.48550/arXiv.2108.
07258
Bevendorff,J.,Casals,X.B.,Chulvi,B.,Dementieva,D.,Elnagar,A.,Freitag,D.,
etal.(2024).“Overviewofpan2024:Multi-authorwritingstyleanalysis,multilingual Bordia,S.,andBowman,S.R.(2019).Identifyingandreducinggenderbiasinword-
text detoxification, oppositional thinking analysis, and generative ai authorship levellanguagemodels.arXiv[preprint]arXiv:1904.03035.doi:10.18653/v1/N19-3002
verification,”inAdvancesinInformationRetrieval,eds.N.Goharian,N.Tonellotto,
Brown,T.B.,Mann,B.,Ryder,N.,Subbiah,M.,Kaplan,J.,Dhariwal,P.,etal.
Y.He,A.Lipani,G.McDonald,C.Macdonald,etal.(Cham:SpringerNature),3–10.
(2020).Languagemodelsarefew-shotlearners.arXiv[preprint]arXiv:2005.14165.
Bian,N.,Liu,P.,Han,X.,Lin,H.,Lu,Y.,He,B.,etal.(2023).Adropofinkmakesa doi:10.48550/arXiv.2005.14165
millionthink:thespreadoffalseinformationinlargelanguagemodels.arXiv[preprint]
Bybee,J.(2015).LanguageChange.Cambridge:CambridgeUniversityPress.
arXiv:2305.04812.doi:10.48550/arXiv.2305.04812
Cabrera,J.,Loyola,M.S.,Magaña,I.,andRojas,R.(2023).“Ethicaldilemmas,
Biber, D. (1989). A typology of english texts. Linguistics 27, 3–44.
mentalhealth,artificialintelligence,andllm-basedchatbots,”inBioinformaticsand
doi:10.1515/ling.1989.27.1.3
BiomedicalEngineering,IWBBIO2023.LectureNotesinComputerScience,vol13920,
Biber, D. (1991). Variation Across Speech and Writing. Cambridge: Cambridge eds. I. Rojas, O. Valenzuela, F. Rojas Ruiz, L. J. Herrera, and F. Ortuño (Cham:
UniversityPress. Springer).doi:10.1007/978-3-031-34960-7_22
FrontiersinArtificialIntelligence 15 frontiersin.org

Grieveetal. 10.3389/frai.2024.1472411
Caliskan, A., Bryson, J. J., and Narayanan, A. (2017). Semantics derived Evans,O.,Cotton-Barratt,O.,Finnveden,L.,Bales,A.,Balwit,A.,Wills,P.,etal.
automaticallyfromlanguagecorporacontainhuman-likebiases.Science356,183–186. (2021).TruthfulAI:developingandgoverningAIthatdoesnotlie.arXiv[preprint]
doi:10.1126/science.aal4230 arXiv.2110.06674.doi:10.48550/arXiv.2110.06674
Campbell,L.(2013).HistoricalLinguistics.Edinburgh:EdinburghUniversityPress. Ferrara,E.(2023).ShouldChatGPTbebiased?challengesandrisksofbiasinlarge
languagemodels.FirstMonday28:13346.doi:10.5210/fm.v28i11.13346
Chambers, J. K., and Trudgill, P. (1998). Dialectology. Cambridge: Cambridge
UniversityPress. Gabriel,I.(2020).Artificialintelligence,values,andalignment.MindsMach.30,
411–437.doi:10.1007/s11023-020-09539-2
Chehbouni,K.,Roshan,M.,Ma,E.,Wei,F.A.,Taïk,A.,Cheung,J.C.,etal.(2024).
Fromrepresentationalharmstoquality-of-serviceharms:acasestudyonllama2 Gao,L.,Biderman,S.,Black,S.,Golding,L.,Hoppe,T.,Foster,C.,etal.(2020).
safetysafeguards.arXiv[preprint]arXiv:2403.13213.doi:10.18653/v1/2024.findings-a Thepile:an800gbdatasetofdiversetextforlanguagemodeling.arXiv[preprint]
cl.927 arXiv:2101.00027.doi:10.48550/arXiv.2101.00027
Chen,B.,Zhang,Z.,Langrené,N.,andZhu,S.(2023).Unleashingthepotential Gordon, M. J. (2017). “William labov,” in Oxford Research Encyclopedia of
of prompt engineering in large language models: a comprehensive review. arXiv Linguistics.
[preprint]arXiv:2310.14735.doi:10.48550/arXiv.2310.14735
Gries, S. T., and Hilpert, M. (2008). The identification of stages in
Chen,Z.,Lin,M.,Wang,Z.,Zang,M.,andBai,Y.(2024).“PreparedLLM:effective diachronic data: variability-based neighbour clustering. Corpora 3, 59–81.
pre-pretrainingframeworkfordomain-specificlargelanguagemodels,”inBigEarth doi:10.3366/E1749503208000075
Data(Abingdon,UK:Taylor&Francis),1–24.
Grieve, J. (2016). Regional Variation in Written American English. Cambridge:
Christian,B.(2021).TheAlignmentProblem:HowCanMachinesLearnHuman CambridgeUniversityPress.
Values?London:AtlanticBooks.
Grieve,J.(2023).Situationaldiversityandlinguisticcomplexity.Linguist.Vanguard
Clarke,I.(2022).Amulti-dimensionalanalysisofenglishtweets.Lang.Literat.31, 9,73–81.doi:10.1515/lingvan-2021-0070
124–149.doi:10.1177/09639470221090369
Grieve,J.,Biber,D.,Friginal,E.,andNekrasova,T.(2010).“Variationamongblogs:a
Clarke,I.,andGrieve,J.(2017).“DimensionsofabusivelanguageonTwitter,” multi-dimensionalanalysis,”inGenresontheWeb,A.Mehler,S.Sharoff,andM.Santini
inProceedingsoftheFirstWorkshoponAbusiveLanguageOnline(Vancouver,BC: (Amsterdam:SpringerNetherlands),303–322.
AssociationforComputationalLinguistics),1–10.
Grieve,J.,Hovy,D.,Jurgens,D.,Kendall,T.,Nguyen,D.,Stanford,J.,etal.(2023).
Crawford,K.(2017).“Thetroublewithbias,”inKeynoteatNeurips(LongBeach, Computationalsociolinguistics.Front.AIRes.Topic.doi:10.3389/978-2-8325-1760-4
CA).
Grieve,J.,Montgomery,C.,Nini,A.,Murakami,A.,andGuo,D.(2019).Mapping
Croft,W.(2000).ExplainingLanguageChange:AnEvolutionaryApproach.London: lexical dialect variation in british english using twitter. Front. Artif. Intellig. 2:11.
PearsonEducation. doi:10.3389/frai.2019.00011
Cruz-Castro,L.,Castelblanco,G.,andAntonenko,P.(2024).“LLM-basedsystem Grieve, J., Nini, A., and Guo, D. (2017). Analyzing lexical emergence
for technical writing real-time review in urban construction and technology,” in in modern American english online. English Lang. Linguist. 21, 99–127.
Proceedingsof60thAnnualAssociatedSchoolsofConstructionInternationalConference doi:10.1017/S1360674316000113
(Auburn,AL:AssociatedSchoolsofConstruction),130–138.
Grieve,J.,Nini,A.,andGuo,D.(2018).Mappinglexicalinnovationonamerican
Crystal,D.(2011).ADictionaryofLinguisticsandPhonetics.Hoboken,NJ:John socialmedia.J.Engl.Linguist.46,293–319.doi:10.1177/0075424218793191
Wiley&Sons.
Guo, Y., and Yang, Y. (2024). Econnli: evaluating large language
Crystal,D.,andDavy,D.(1969).InvestigatingEnglishStyle.Harlow:Longman. models on economics reasoning. arXiv [preprint] arXiv:2407.01212.
doi:10.18653/v1/2024.findings-acl.58
Dathathri, S., See, A., Ghaisas, S., Huang, P.-S., McAdam, R., Welbl, J., et al.
(2024).Scalablewatermarkingforidentifyinglargelanguagemodeloutputs.Nature Gururangan,S.,Marasovic´,A.,Swayamdipta,S.,Lo,K.,Beltagy,I.,Downey,D.,
634,818–823.doi:10.1038/s41586-024-08025-4 etal.(2020).Don’tstoppretraining:Adaptlanguagemodelstodomainsandtasks.
arXiv[preprint]arXiv:2004.10964.doi:10.48550/arXiv.2004.10964
DauméIII,H.(2007).“Frustratinglyeasydomainadaptation,”inProceedingsof
the 45th Annual Meeting of the Association of Computational Linguistics (Prague: Halliday,M.A.(1989).Language,Context,andText:AspectsofLanguageina
AssociationforComputationalLinguistics),256–263. Social-SemioticPerspective.Oxford:OxfordUniversityPress.
Degaetano-Ortlieb,S.,andTeich,E.(2018).“Usingrelativeentropyfordetection Halliday,M.A.K.,andHasan,R.(1976).CohesioninEnglish.London:Longman.
andanalysisofperiodsofdiachroniclinguisticchange,”inProceedingsoftheSecond
Haque,M.A.,andLi,S.(2024).ExploringChatGPTanditsimpactonsociety.AI
JointSIGHUMWorkshoponComputationalLinguisticsforCulturalHeritage,Social
Ethics2024,1–13.doi:10.1007/s43681-024-00435-4
Sciences,HumanitiesandLiterature,22–33.
Hardy, M., Sucholutsky, I., Thompson, B., and Griffiths, T. (2023). “Large
Demszky,D.,Yang,D.,Yeager,D.S.,Bryan,C.J.,Clapper,M.,Chandhok,S.,etal.
languagemodelsmeetcognitivescience:LLMsastools,models,andparticipants,”in
(2023).Usinglargelanguagemodelsinpsychology.Nat.Rev.Psychol.2,688–701.
Proceedingsofthe45thAnnualConferenceoftheCognitiveScienceSociety,eds.M.
doi:10.1038/s44159-023-00241-5
Goldwater,F.K.Anggoro,B.K.Hayes,andD.C.Ong(CognitiveScienceSociety),
Dentella, V., Günther, F., and Leivada, E. (2023). Systematic testing of three 14–15.
languagemodelsrevealslowlanguageaccuracy,absenceofresponsestability,andayes-
Hartmann,R.R.K.,andStork,F.C.(1972).DictionaryofLanguageandLinguistics.
responsebias.Proc.Nat.Acad.Sci.120:e2309583120.doi:10.1073/pnas.2309583120
Basel:AppliedSciencePublisher.
Dev, S., Sheng, E., Zhao, J., Amstutz, A., Sun, J., Hou, Y., et al. (2022). “On
Head,C.B.,Jasper,P.,McConnachie,M.,Raftree,L.,andHigdon,G.(2023).Large
measuresofbiasesandharmsinNLP,”inFindingsoftheAssociationforComputational
languagemodelapplicationsforevaluation:opportunitiesandethicalimplications.
Linguistics:AACL-IJCNLP2022(AssociationforComputationalLinguistics),246–267.
NewDirect.Evaluat.2023,33–46.doi:10.1002/ev.20556
Devlin,J.,Chang,M.W.,Lee,K.,andToutanova,K.(2018).BERT:Pre-training
Hendrycks, D., Burns, C., Basart, S., Critch, A., Li, J., Song, D., et al.
of deep bidirectional transformers for language understanding. arXiv [preprint]
(2020).AligningAIwithsharedhumanvalues.arXiv[preprint]arXiv.2008.02275.
arXiv:1810.04805.doi:10.48550/arXiv.1810.04805
doi:10.48550/arXiv.2008.02275
Donoso,G.,andSánchez,D.(2017).Dialectometricanalysisoflanguagevariation
intwitter.arXiv[preprint]arXiv:1702.06777.doi:10.18653/v1/W17-1202 Hoffmann,J.,Borgeaud,S.,Mensch,A.,Buchatskaya,E.,Cai,T.,Rutherford,E.,
etal.(2022).“TrainingCompute-OptimalLargeLanguageModels,”Proceedingsofthe
Dung,L.(2023).Currentcasesofaimisalignmentandtheirimplicationsforfuture 36thInternationalConferenceonNeuralInformationProcessingSystems(NewOrleans,
risks.Synthese202:138.doi:10.1007/s11229-023-04367-0 LA:Neurips).
Eckert, P. (2012). Three waves of variation study: the emergence of meaning Hofmann, V., Kalluri, P. R., Jurafsky, D., and King, S. (2024). AI generates
in the study of sociolinguistic variation. Annu. Rev. Anthropol. 41, 87–100. covertlyracistdecisionsaboutpeoplebasedontheirdialect.Nature633,147–154.
doi:10.1146/annurev-anthro-092611-145828 doi:10.1038/s41586-024-07856-5
Eckert, P. (2018). Meaning and Linguistic Variation: The Third Wave in Horton,J.J.(2023).LargeLanguageModelsasSimulatedEconomicAgents:What
Sociolinguistics.Cambridge:CambridgeUniversityPress. CanweLearnfromHomosilicus?Cambridge,MA:NationalBureauofEconomic
Ehret, K. (2021). An information-theoretic view on language complexity and Research.doi:10.3386/w31122
register variation: Compressing naturalistic corpus data. Corpus Linguist. Linguist.
Hou,Z.,Salazar,J.,andPolovets,G.(2022).Meta-learningthedifference:preparing
Theory17,383–410.doi:10.1515/cllt-2018-0033
largelanguagemodelsforefficientadaptation.Trans.Assoc.Comput.Linguist.10,
Eisenstein,J.(2017).“IdentifyingRegionalDialectsinOn-LineSocialMedia,”in 1249–1265.doi:10.1162/tacl_a_00517
TheHandbookofDialectology,eds.C.Boberg,J.Nerbonne,D.Watt(Hoboken,NJ:
Hovy, D. (2018). “The social and the neural network: How to make natural
JohnWiley&Sons),368–383.doi:10.1002/9781118827628.ch21
languageprocessingaboutpeopleagain,”inProceedingsoftheSecondWorkshopon
Eisenstein,J.,O’Connor,B.,Smith,N.A.,andXing,E.P.(2014).Diffusionoflexical Computational Modeling of People’s Opinions, Personality, and Emotions in Social
changeinsocialmedia.PLoSONE9:e113114.doi:10.1371/journal.pone.0113114 Media(NewOrleans,LA:AssociationforComputationalLinguistics),42–49.
FrontiersinArtificialIntelligence 16 frontiersin.org

Grieveetal. 10.3389/frai.2024.1472411
Hovy,D.,andPrabhumoye,S.(2021).Fivesourcesofbiasinnaturallanguage MethodsinNaturalLanguageProcessing(Singapore:AssociationforComputational
processing.Lang.Linguist.Compass15:e12432.doi:10.1111/lnc3.12432 Linguistics),10383–10405.
Hovy,D.,andSøgaard,A.(2015).“Taggingperformancecorrelateswithauthor Lass,R.(1997).HistoricalLinguisticsandLanguageChange,Volume81.Cambridge:
age,”inProceedingsofthe53rdannualmeetingoftheAssociationforComputational CambridgeUniversityPress.
Linguisticsandthe7thInternationalJointConferenceonNaturalLanguageProcessing
Lehman,E.,Hernandez,E.,Mahajan,D.,Wulff,J.,Smith,M.J.,Ziegler,Z.,etal.
(volume2:Shortpapers)(Beijing:AssociationforComputationalLinguistics),483–488.
(2023).“Dowestillneedclinicallanguagemodels?”inConferenceonHealth,Inference,
Hovy,D.,andYang,D.(2021).“Theimportanceofmodelingsocialfactorsof andLearning(NewYork:PMLR),578–597.
language:Theoryandpractice,”inProceedingsofthe2021ConferenceoftheNorth
Lehmann,W.P.(2013).HistoricalLinguistics:AnIntroduction.London:Routledge.
AmericanChapteroftheAssociationforComputationalLinguistics:HumanLanguage
Technologies(AssociationforComputationalLinguistics),588–602. Leidinger,A.,andRogers,R.(2024).HowareLLMsmitigatingstereotypingharms?
Learningfromsearchenginestudies.Proc.AAAI/ACMConf.AI,Ethics,andSoc.7,
Hu,E.J.,Shen,Y.,Wallis,P.,Allen-Zhu,Z.,Li,Y.,Wang,S.,etal.(2021).LoRA:
839–854.doi:10.1609/aies.v7i1.31684
low-rank adaptation of large language models. arXiv [preprint] arXiv:2106.09685.
doi:10.48550/arXiv.2106.09685 Li, C., and Flanigan, J. (2024). Task contamination: Language models
may not be few-shot anymore. Proc. AAAI Conf. AI. 38, 18471–18480.
Huang,C.,Zhao,W.,Zheng,R.,Lv,H.,Dou,S.,Li,S.,etal.(2024).Safealigner:
doi:10.1609/aaai.v38i16.29808
Safety alignment against jailbreak attacks via response disparity guidance. arXiv
[preprint]arXiv:2406.18118.doi:10.48550/arXiv.2406.18118 Li,H.,Moon,J.T.,Purkayastha,S.,Celi,L.A.,Trivedi,H.,andGichoya,J.W.
(2023).Ethicsoflargelanguagemodelsinmedicineandmedicalresearch.Lancet
Huang, H., Grieve, J., Jiao, L., and Cai, Z. (2024). Geographic structure of
DigitalHealth5,e333–e335.doi:10.1016/S2589-7500(23)00083-3
Chinesedialects:acomputationaldialectometricapproach.Linguistics.62,937–976.
doi:10.1515/ling-2021-0138 Li,M.,Chen,M.-B.,Tang,B.,ShengbinHou,S.,Wang,P.,Deng,H.,etal.(2024).
“NewsBench:asystematicevaluationframeworkforassessingeditorialcapabilities
Huang,W.,andGrieve,J.(2024).“AuthoriallanguagemodelsforAIauthorship
oflargelanguagemodelsinchinesejournalism,”inProceedingsofthe62ndAnnual
verification,”inWorkingNotesofCLEF(Grenoble:CEUR).
MeetingoftheAssociationforComputationalLinguistics(Volume1:LongPapers),eds.
Huang, W., Murakami, A., and Grieve, J. (2024). ALMs: Authorial Ku,L.-W.,Martins,A.,andSrikumar,V.(Bangkok:AssociationforComputational
language models for authorship attribution. arXiv [preprint] arXiv:2401.12005. Linguistics),9993–10014.
doi:10.48550/arXiv.2401.12005
Li, Y., Choi, D., Chung, J., Kushman, N., Schrittwieser, J., Leblond, R., et al.
Huang,Y.,Guo,D.,Kasakoff,A.,andGrieve,J.(2016).Understandingusregional (2022).Competition-levelcodegenerationwithalphacode.Science378,1092–1097.
linguistic variation with twitter data analysis. Comput. Environ. Urban Syst. 59, doi:10.1126/science.abq1158
244–255.doi:10.1016/j.compenvurbsys.2015.12.003
Liimatta,A.(2019).Exploringregistervariationonreddit:amulti-dimensional
Huang,Y.,Tang,K.,Chen,M.,andWang,B.(2024).Acomprehensivesurveyon study of language use on a social media website. Register Stud. 1, 269–295.
evaluatinglargelanguagemodelapplicationsinthemedicalindustry.arXiv[preprint] doi:10.1075/rs.18005.lii
arXiv:2404.15777.doi:10.48550/arXiv.2404.15777
Liu,R.,Yang,R.,Jia,C.,Zhang,G.,Zhou,D.,Dai,A.M.,etal.(2023).Training
Ilbury,C.(2020).“sassyqueens:”Stylisticorthographicvariationintwitterandthe socially aligned language models in simulated human society. arXiv [preprint]
enregistermentofaave.J.sociolinguist.24,245–264.doi:10.1111/josl.12366 arXiv.2305.16960.doi:10.48550/arXiv.2305.16960
Jackson,H.(2007).KeyTermsinLinguistics.London:Continuum. Liu,R.,Zhang,G.,Feng,X.,andVosoughi,S.(2022).Aligninggenerativelanguage
models with human values. Find. Assoc. Comp. Linguist.: NAACL 2022, 241–252.
Jiang, A. Q., Sablayrolles, A., Mensch, A., Bamford, C., Chaplot, D.
doi:10.18653/v1/2022.findings-naacl.18
S., Casas, D., et al. (2023). Mistral 7B. arXiv [preprint] arXiv:2310.06825.
doi:10.48550/arXiv.2310.06825 Liu,Y.,Liu,Y.,Chen,X.,Chen,P.-Y.,Zan,D.,Kan,M.-Y.,etal.(2024).Thedevil
isintheneurons:Interpretingandmitigatingsocialbiasesinpre-trainedlanguage
Jiao, J., Afroogh, S., Xu, Y., and Phillips, C. (2024). Navigating llm ethics:
models.arXiv[preprint]arXiv:2406.10130.doi:10.48550/arXiv.2406.10130
advancements,challenges,andfuturedirections.arXiv[preprint]arXiv:2406.18841.
doi:10.48550/arXiv.2406.18841 Lund,B.D.,Wang,T.,Mannuru,N.R.,Nie,B.,Shimray,S.,andWang,Z.(2023).
ChatGPTandanewacademicreality:artificialintelligence-writtenresearchpapersand
Jórgensen, J. N., Karrebáek, M. S., Madsen, L. M., and Móller, J. S. (2015).
theethicsofthelargelanguagemodelsinscholarlypublishing.J.Assoc.Inform.Sci.
“Polylanguaging in superdiversity,” in Language and Superdiversity (Milton Park:
Technol.74,570–581.doi:10.1002/asi.24750
Routledge),147–164.
Luo,H.,Huang,H.,Deng,Z.,Liu,X.,Chen,R.,andLiu,Z.(2024).Bigbench:
Joseph,B.D.,Janda,R.D.,andVance,B.S.(2003).TheHandbookofHistorical
a unified benchmark for social bias in text-to-image generative models based
Linguistics.Hoboken,NJ:WileyOnlineLibrary.
onmulti-modalLLM.arXiv[preprint]arXiv:2407.15240.doi:10.48550/arXiv.2407.
Jurafsky,D.,andMartin,J.H.(2023).SpeechandLanguageProcessing,3rdEdition. 15240
Availableat:https://web.stanford.edu/~jurafsky/slp3/
Mahapatra,A.,Nangi,S.R.,andGarimella,A..(2022).“Entityextractioninlow
Jurgens,D.,Tsvetkov,Y.,andJurafsky,D.(2017).“Incorporatingdialectalvariability resourcedomainswithselectivepre-trainingoflargelanguagemodels,”inProceedings
forsociallyequitablelanguageidentification,”inProceedingsofthe55thAnnualMeeting ofthe2022ConferenceonEmpiricalMethodsinNaturalLanguageProcessing,eds.Y.
oftheAssociationforComputationalLinguistics(Volume2:ShortPapers),51–57. Goldberg,Z.Kozareva,andY.Zhang(AbuDhabi,UnitedArabEmirates:Association
forComputationalLinguistics),942–951.
Kaplan,J.,McCandlish,S.,Henighan,T.,Brown,T.B.,Chess,B.,Child,R.,etal.
(2020).Scalinglawsforneurallanguagemodels.arXiv[preprint]arXiv.2001.08361. Marcus,G.,Leivada,E.,andMurphy,E.(2023).Asentenceisworthathousand
doi:10.48550/arXiv.2001.08361 pictures:Canlargelanguagemodelsunderstandhumanlanguage?arXiv[preprint]
Kasneci, E., Se´ssler, K., Küchemann, S., Bannert, M., Dementieva, D., arXiv.2308.00109.doi:10.48550/arXiv.2308.00109
Fischer, F., et al. (2023). Chatgpt for good? on opportunities and challenges Martin,J.R.(2001).“Language,registerandgenre,”inAnalysingEnglishinaGlobal
of large language models for education. Learn. Individ. Differ. 103:102274. Context:AReader(London:Routledge),149–166.
doi:10.1016/j.lindif.2023.102274
Matthews,P.H.(1997).OxfordConciseDictionaryofLinguistics.Oxford:University
Kershaw, D., Rowe, M., and Stacey, P. (2016). “Towards modelling language ofOxford.
innovationacceptanceinonlinesocialnetworks,”inProceedingsoftheNinthACM
InternationalConferenceonWebSearchandDataMining,553–562. Matthiessen,C.M.(2015).Registerintheround:Registerialcartography.Funct.
Linguist.2,1–48.doi:10.1186/s40554-015-0015-8
Kirchenbauer,J.,Geiping,J.,Wen,Y.,Katz,J.,Miers,I.,andGoldstein,T.(2023).
“Awatermarkforlargelanguagemodels,”inInternationalConferenceonMachine Mavrodieva, I. (2023). Linguistic and rhetorical features of dialogue on
Learning(Honolulu,HI:PMLR),17061–17084. rhetoricaltopicsbetweenahumanandchatbotgpt.RhetoricCommun.56,22–45.
doi:10.55206/CIKP7841
Kocijan,V.(2021).ImpactofPre-TrainingonBackgroundKnowledgeandSocietal
Bias(PhDthesis).Oxford:UniversityofOxford. McEnery,T.,andWilson,A.(2001).CorpusLinguistics.Edinburgh:Edinburgh
UniversityPress.
Labov,W.(1973).SociolinguisticPatterns.Philadelphia:UniversityofPennsylvania
Press. McEnery,T.,Xiao,R.,andTono,Y.(2006).Corpus-basedLanguageStudies:An
AdvancedResourceBook.London:Routledge.
Labov,W.(1986).“Thesocialstratificationof(r)innewyorkcitydepartment
stores,”inDialectandLanguageVariation(London:Elsevier),304–329. Meyerhoff,M.(2018).IntroducingSociolinguistics.London:Routledge.
Labov,W.,Ash,S.,andBoberg,C.(2006).TheAtlasofNorthAmericanEnglish: Michaelov,J.A.,Bardolph,M.D.,VanPetten,C.K.,Bergen,B.K.,andCoulson,
Phonetics,PhonologyandSoundChange.Berlin:MoutondeGruyter. S.(2024).Strongprediction:languagemodelsurprisalexplainsmultiplen400effects.
Neurobiol.Lang.2024,1–29.doi:10.1162/nol_a_00105
Lahoti,P.,Blumm,N.,Ma,X.,Kotikalapudi,R.,Potluri,S.,Tan,Q.,etal.(2023).
“Improving diversity of demographic representation in large language models via Navigli,R.,Conia,S.,andRoss,B.(2023).Biasesinlargelanguagemodels:origins,
collective-critiquesandself-voting,”inProceedingsofthe2023ConferenceonEmpirical inventory,anddiscussion.J.DataInform.Quality15,1–10.doi:10.1145/3597307
FrontiersinArtificialIntelligence 17 frontiersin.org

Grieveetal. 10.3389/frai.2024.1472411
Nazi,Z.A.,andPeng,W.(2024).Largelanguagemodelsinhealthcareandmedical Shen, T., Jin, R., Huang, Y., Liu, C., Dong, W., Guo, Z., et al. (2023).
domain:Areview.Informatics11,57.doi:10.3390/informatics11030057 Large language model alignment: A survey. arXiv [preprint] arXiv.2309.15025.
doi:10.48550/arXiv.2309.15025
Nevalainen, T., and Raumolin-Brunberg, H. (2016). Historical Sociolinguistics:
LanguageChangeinTudorandStuartEngland.London:Routledge. Shumailov,I.,Shumaylov,Z.,Zhao,Y.,Gal,Y.,Papernot,N.,andAnderson,R.
(2023).Thecurseofrecursion:Trainingongenerateddatamakesmodelsforget.arXiv
Ngo, R., Chan, L., and Mindermann, S. (2022). The alignment problem
[preprint]arXiv.2305.17493.doi:10.48550/arXiv.2305.17493
from a deep learning perspective. arXiv [preprint] arXiv.2209.00626.
doi:10.48550/arXiv.2209.00626 Solaiman, I., and Dennison, C. (2021). Process for adapting language models
tosociety(palms)withvalues-targeteddatasets.Adv.NeuralInf.Process.Syst.34,
Nguyen,D.,Doäÿruöz,A.S.,Rosé,C.P.,andDeJong,F.(2016).Computational
5861–5873.doi:10.48550/arXiv.2106.10328
sociolinguistics:asurvey.Comput.Linguist.42,537–593.doi:10.1162/COLI_a_00258
Stefan, R., Carutasu, G., and Mocan, M. (2023).“Ethical considerations in the
Nguyen,D.,Rosseel,L.,andGrieve,J.(2021).“Onlearningandrepresentingsocial
implementation and usage of large language models,” in The 17th International
meaninginnlp:asociolinguisticperspective,”inProceedingsofthe2021Conferenceof
ConferenceInterdisciplinarityinEngineering,edsL.MoldovanandA.Gligor(Cham:
theNorthAmericanChapteroftheAssociationforComputationalLinguistics:Human
Springer),131–144.
LanguageTechnologies(AssociationforComputationalLinguistics),603–612.
Stewart,I.,andEisenstein,J.(2018).“Makingfetch?happen:theinfluenceofsocial
Nirmal,A.(2024).InterpretableHateSpeechDetectionviaLargeLanguageModel-
andlinguisticcontextonthesuccessoflexicalinnovations,”inProceedingsofthe2018
ExtractedRationales.Tempe,AZ:ArizonaStateUniversity.
ConferenceonEmpiricalMethodsinNaturalLanguageProcessing(EMNLP)(Brussels:
OpenAI.(2022).Chatgpt. AssociationforComputationalLinguistics),4360–4370.
Ouyang,L.,Wu,J.,Jiang,X.,Almeida,D.,Wainwright,C.L.,Mishkin,P.,etal. Tagliamonte, S. A. (2006). Analysing Sociolinguistic Variation. Cambridge:
(2022).Traininglanguagemodelstofollowinstructionswithhumanfeedback.arXiv CambridgeUniversityPress.
[preprint]arXiv:2203.02155[cs].doi:10.48550/arXiv.2203.02155
Tagliamonte, S. A. (2011). Variationist Sociolinguistics: Change, Observation,
Pavalanathan,U.,andEisenstein,J.(2015).Audience-modulatedvariationinonline Interpretation.Hoboken:JohnWiley&Sons.
socialmedia.Am.Speech90,187–213.doi:10.1215/00031283-3130324
Thirunavukarasu,A.J.,Ting,D.S.J.,Elangovan,K.,Gutierrez,L.,Tan,T.F.,and
Pavlik,J.V.(2023).Collaboratingwithchatgpt:Consideringtheimplicationsof Ting,D.S.W.(2023).Largelanguagemodelsinmedicine.Nat.Med.29,1930–1940.
generativeartificialintelligenceforjournalismandmediaeducation.Journalism&mass doi:10.1038/s41591-023-02448-8
communicationeducator78:84–93.doi:10.1177/10776958221149577
Tonmoy,S.M.,Zaman,S.M.,Jain,V.,Rani,A.,Rawte,V.,Chadha,A.,etal.(2024).
Pérez,J.M.,Miguel,P.,andCotik,V.(2024).Exploringlargelanguagemodels A comprehensive survey of hallucination mitigation techniques in large language
forhatespeechdetectioninrioplatenseSpanish.arXiv[preprint]arXiv:2410.12174. models.arXiv[preprint]arXiv.2401.01313.doi:10.48550/arXiv.2401.01313
doi:10.48550/arXiv.2410.12174
Touvron, H., Martin, L., Stone, K., Albert, P., Almahairi, A., Babaei, Y., et al.
Piantadosi, S. (2023). “Modern language models refute chomsky’s approach to (2023). Llama 2: Open foundation and fine-tuned chat models. arXiv [preprint]
language,”inTechnicalReport,LingbuzzPreprint.Troms:UniversityofTroms. arXiv.2307.09288.doi:10.48550/arXiv.2307.09288
Radford,A.,Wu,J.,Child,R.,Luan,D.,Amodei,D.,andSutskever,I.(2019). Tsvilodub, P., Carcassi, F., and Franke, M. (2024). Towards neuro-symbolic
Languagemodelsareunsupervisedmultitasklearners.OpenAIBlog(OpenAI),1:9. models of language cognition: Llms as proposers and evaluators. arXiv [preprint]
arXiv.2401.09334.doi:10.48550/arXiv.2401.09334
Raffel,C.,Shazeer,N.,Roberts,A.,Lee,K.,Narang,S.,Matena,M.,etal.(2020).
Exploringthelimitsoftransferlearningwithaunifiedtext-to-texttransformer.J.Mach. Vaswani,A.,Shazeer,N.,Parmar,N.,Uszkoreit,J.,Jones,L.,Gomez,A.N.,etal.
Learn.Res.21:1–67. (2017).Attentionisallyouneed.Adv.NeuralInf.Process.Syst.2017:30.
Ramesh,K.,Sitaram,S.,andChoudhury,M.(2023).Fairnessinlanguagemodels Wang, B., and Komatsuzaki, A. (2021). GPT-J-6B: A 6 Billion Parameter
beyond english: Gaps and challenges. Find. Assoc. Comp. Linguist.: EACL 2023, Autoregressive Language Model. Long Beach, CA. Available at: https://github.com/
2106–2119.doi:10.18653/v1/2023.findings-eacl.157 kingoflolz/mesh-transformer-jax(accessedDecember10,2024).
Ray,P.P.(2023).Chatgpt:acomprehensivereviewonbackground,applications, Wang, T., Zhou, N., and Chen, Z. (2024). Enhancing computer programming
keychallenges,bias,ethics,limitationsandfuturescope.Intern.ThingsCyber-PhysSyst. education with LLMs: a study on effective prompt engineering for Python
3,121–154.doi:10.1016/j.iotcps.2023.04.003 code generation. arXiv [preprint] arXiv:2407.05437. doi: 10.48550/arXiv.2407.
05437
Röthlisberger,M.,andSzmrecsanyi,B.(2020).“Dialecttypology:recentadvances,”
in Handbook of the Changing World Language Map (New York, NY: Springer), Wang,Y.,Zhong,W.,Li,L.,Mi,F.,Zeng,X.,Huang,W.,etal.(2023).Aligning
131–156. large language models with human: A survey. arXiv [preprint] arXiv.2307.12966.
doi:10.48550/arXiv.2307.12966
Rudnicky,A.(1995).“LanguageModelingwithLimitedDomainData,”inProc.
ARPASpokenLanguageSystemsTechnologyWorkshop(Austin,TX;SanFrancisco,CA: Wardhaugh, R., and Fuller, J. M. (2021). An Introduction to Sociolinguistics.
MorganKaufmanPublishers),66–69. Hoboken:JohnWiley&Sons.
Russell,S.J.,andNorvig,P.(2016).ArtificialIntelligence:AModernApproach. Weerts, H. J. (2021). An introduction to algorithmic fairness. arXiv [preprint]
London:Pearson. arXiv.2105.05595.doi:10.48550/arXiv.2105.05595
Salazar,J.,Liang,D.,Nguyen,T.Q.,andKirchhoff,K.(2019).Maskedlanguage Wieling,M.,andNerbonne,J.(2015).Advancesindialectometry.AnnualRev.
modelscoring.arXiv[preprint]arXiv:1910.14659.doi:10.18653/v1/2020.acl-main.240 Linguist.1,243–264.doi:10.1146/annurev-linguist-030514-124930
Sampson,G.(2002).EmpiricalLinguistics.London:A&CBlack. Wiener, N. (1960). Some moral and technical consequences of automation: as
machines learn they may develop unforeseen strategies at rates that baffle their
Sardana, N., and Frankle, J. (2023). Beyond chinchilla-optimal: accounting
programmers.Science131,1355–1358.doi:10.1126/science.131.3410.1355
for inference in language model scaling laws. arXiv [preprint] arXiv.2401.00448.
doi:10.48550/arXiv.2401.00448 Wolf,Y.,Wies,N.,Levine,Y.,andShashua,A.(2023).Fundamentallimitations
of alignment in large language models. arXiv [preprint] arXiv.2304.11082.
Sardinha,T.B.,andPinto,M.V.(2014).Multi-DimensionalAnalysis,25Years
doi:10.48550/arXiv.2304.11082
On:ATributetoDouglasBiber,volume60.Amsterdam:JohnBenjaminsPublishing
Company. Xu,A.,Pathak,E.,Wallace,E.,Gururangan,S.,Sap,M.,andKlein,D.(2021).
Detoxifying language models risks marginalizingminority voices. arXiv [preprint]
Scholz, B.C.,Pelletier, F. J.,Pullum, G.K.,and Nefdt,R. (2024).“Philosophy
arXiv:2104.06390.doi:10.48550/arXiv.2104.06390
of linguistics. In of Philosophy (Spring Edition),” in The Stanford Encyclopedia of
Philosophy(SpringEdition),eds.N.Edward,T.S.E.Zalta,andU.Nodelman(Stanford, Yang, D., Hovy, D., Jurgens, D., and Plank, B. (2024). The call for
CA:StanfordUniversity). socially aware language technologies. arXiv [preprint] arXiv.2405.02411.
doi:10.48550/arXiv.2405.02411
Schramowski,P.,Turan,C.,Andersen,N.,Rothkopf,C.A.,andKersting,K.(2022).
Largepre-trainedlanguagemodelscontainhuman-likebiasesofwhatisrightand Yigci,D.,Eryilmaz,M.,Yetisen,A.K.,Tasoglu,S.,andOzcan,A.(2024).Large
wrongtodo.Nat.Mach.Intellig.4,258-268.doi:10.1038/s42256-022-00458-8 languagemodel-basedchatbotsinhighereducation.Adv.Intellig.Syst.2024:2400429.
doi:10.1002/aisy.202400429
Shah, D. S., Schwartz, H. A., and Hovy, D. (2020). “Predictive biases in
natural language processing models,” in Proceedings of the 58th Annual Meeting Yogarajan,V.,Dobbie,G.,Keegan,T.T.,andNeuwirth,R.J.(2023).Tacklingbias
of the Association for Computational Linguistics (Stroudsburg, PA: Association for inpre-trainedlanguagemodels:Currenttrendsandunder-representedsocieties.arXiv
ComputationalLinguistics),5248–5264. [preprint]arXiv:2312.01509.doi:10.48550/arXiv.2312.01509
FrontiersinArtificialIntelligence 18 frontiersin.org
