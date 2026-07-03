This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2025.3595894
Dateofpublicationxxxx00,0000,dateofcurrentversionxxxx00,0000.
DigitalObjectIdentifier10.1109/ACCESS.2024.0429000
Benchmarking Sentence Encoders in Associating
Indicators with Sustainable Development Goals
and Targets
ANAGJORGJEVIKJ1,2,KOSTADINMISHEV1,DIMITARTRAJANOV1,3,(MEMBER,IEEE),AND
LJUPCOKOCAREV1,4,(FELLOW,IEEE)
1FacultyofComputerScienceandEngineering,Ss.CyrilandMethodiusUniversityinSkopje,1000Skopje,NorthMacedonia(e-mail:
kostadin.mishev@finki.ukim.mk,dimitar.trajanov@finki.ukim.mk)
2ComputerSystemsDepartment,JožefStefanInstitute,1000Ljubljana,Slovenia(e-mail:ana.gjorgjevikj@ijs.si)
3DepartmentofComputerScience,MetropolitanCollege,BostonUniversity,Boston,MA02215,USA
4MacedonianAcademyofSciencesandArts,1000Skopje,NorthMacedonia(e-mail:lkocarev@manu.edu.mk)
Correspondingauthor:AnaGjorgjevikj(e-mail:ana.gjorgjevikj@ijs.si).
ThisworkwassupportedinpartbytheSlovenianResearchAgencythroughprogramgrantNo.P2-0098andprojectgrantNo.GC-0001,
andtheEuropeanUnionthroughGrantAgreement101211695(HorizonEuropeMSCA-PFAutoLLMSelect).
ABSTRACT The United Nations’ 2030 Agenda for Sustainable Development balances the economic,
environmental, and social dimension of sustainable development in 17 Sustainable Development Goals
(SDGs), monitored through a well-defined set of targets and global indicators. Although essential for
humanity’sfuturewell-being,thismonitoringisstillchallengingduetothevariablequalityofthestatistical
data of global indicators compiled at the national level and the diversity of indicators used to monitor
sustainabledevelopmentatthesubnationallevel.Associatingindicatorsotherthantheglobaloneswiththe
SDGs/targetsmayhelpnotonlytoexpandthestatisticaldata,buttobetteraligntheeffortstowardsustainable
developmenttakenat(sub)nationallevel.Thisarticlepresentsamodel-agnosticframeworkforassociating
suchindicatorswiththeSDGsandtargetsbycomparingtheirtextualdescriptionsinacommonrepresentation
space.Whileremovingthedependenceonthequantityandqualityofthestatisticaldataoftheindicators,it
provideshumanexpertswithdata-drivensuggestionsonthecomplexandnotalwaysobviousassociations
betweentheindicatorsandtheSDGs/targets.Acomprehensivedomain-specificbenchmarkingofadiverse
sentenceencoderportfoliowasperformedfirst,followedbyfine-tuningofthebestonesonanewlycreated
dataset.Fivesetsofindicatorsusedatthe(sub)nationallevelofgovernance(around800indicatorsintotal)
wereusedfortheevaluation.Finally,theinfluenceof40factorsontheresultswasanalyzedusingexplainable
artificial intelligence (xAI) methods. The results show that (1) certain sentence encoders are better suited
tosolvingthetaskthanothers(potentiallyduetotheirdiversepre-trainingdatasets),(2)thefine-tuningnot
onlyimprovesthepredictiveperformanceoverthebaselinesbutalsoreducesthesensitivitytochangesin
indicatordescriptionlength(performancedropsevenbyupto17%forbaselinemodelsaslengthincreases,
butremainscomparableforfine-tunedmodels),and(3)betterselectedtraininginstanceshavethepenitential
toimprovetheperformanceevenfurther(takingintoaccountthelimitedfine-tuningdatasetcurrentlyused
andtheinsightsfromthexAIanalysis).Mostimportantly,thisarticlecontributestofillingtheexistinggap
incomprehensivebenchmarkingofAImodelsinsolvingtheproblem.
INDEXTERMSMachinelearning,naturallanguageprocessing,representationlearning,sustainabledevel-
opment
I. INTRODUCTION a plan to take action in the most crucial areas for the well-
being of the planet and humanity. The Agenda consists of
The 2030 Agenda for Sustainable Development [1] of the
17SustainableDevelopmentGoals(SDGs)and169targets,
UnitedNations(UN),adoptedinSeptember2015,represents
VOLUME11,2023 1
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2025.3595894
Gjorgjevikjetal.:BenchmarkingSentenceEncodersinAssociatingIndicatorswithSustainableDevelopmentGoalsandTargets
whichdescribewhatneedstobeachievedby2030toensure theregionalorlocallevelsofgovernance[7]–[11].Atthose
asustainablefuture.Forexample,SDG1isdevotedtoend- levels, the selection of an appropriate indicator framework
ing poverty in all its forms everywhere, while its target 1.1 formonitoringsustainabilitymaybeburdenedbycompeting
specifically requires eradicating extreme poverty, measured objectives of the process, e.g., the need for context-specific
as people living on less than $1.25 a day, by 2030 [1] (for indicators that are better suited to local needs vs. indicators
detailsontheSDGs,seetheAppendixA).Progressismon- frominternationalframeworksthatallowcomparabilityona
itoredthroughtheGlobalindicatorframeworkfortheSDGs globallevel[9].Therefore,itisnotuncommontouselocally
andtargetsoftheAgenda[2],adoptedinJuly2017,refined relevantindicatorsetstomonitorsustainabilityatthoselevels.
annually, and including 231 unique indicators at the time Forexample,aresearcharticle[9]identified67initiativesde-
of writing1. The Agenda defines the SDGs and their targets velopingindicatorsetsforurbanareas.Ontheotherhand,not
asintegratedandindivisible,balancingthethreedimensions allavailableindicatorsetsformonitoringurbansustainability
of sustainable development, i.e., the economic, social, and are aligned with the 2030 Agenda [8]. Harmonization and
environmental dimension [1]. Therefore, trying to achieve homogeneityofthedataarepointedaskeychallengeswhen
the SDGs and targets in isolation can lead to unintended analyzing the SDGs at the regional level in the European
outcomes [3]. The interactions between the SDGs may be Union(EU),assuchdatacanbescarceorcomefrommultiple
positivewhencoordinatedactionsleadtobeneficialoutcomes sources [11]. In such circumstances, many initiatives aim at
at a lower cost or with a higher impact, or negative when “localizing” the SDGs and assisting in their integration into
actions lead to trade-offs [4]. Consequently, achieving the local policies, as further described in Section II-A. Local-
Agenda as a whole requires knowledge of the SDG depen- ization is the process of defining/implementing/monitoring
dencies,thestrengthofthedependencies,thedirectionofin- strategies for achieving SDGs at the local level, i.e., trans-
fluence,thereversibilityoftheeffectsandthecertaintyofthe latingtheAgendaintolocalresults[12].
perceivedoutcomesintheregionalcontext[3].However,the
|     |     |     |     |     |     |     |     | From our | literature | review, | several | key | challenges | that |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---------- | ------- | ------- | --- | ---------- | ---- |
interactionsbetweentheSDGsarenotdefinedintheAgenda motivatedthisarticlewereidentified:
itselfandmaydependonthecontext(e.g.,geographicregion,
Varietyofindicatorframeworksusedatdifferentlevels
•
time,levelofgovernance).Asmostoftheactionssupporting
ofgovernanceandgeographicregions.
| the Agenda     | take place | at               | local,   | regional, | and national |        | levels |                                                        |      |     |              |     |             |          |
| -------------- | ---------- | ---------------- | -------- | --------- | ------------ | ------ | ------ | ------------------------------------------------------ | ---- | --- | ------------ | --- | ----------- | -------- |
|                |            |                  |          |           |              |        |        | • Necessitytoproperlyassociatelocallyrelevantindicator |      |     |              |     |             |          |
| [5], achieving | the        | Agenda           | requires | accurate  | monitoring   |        | of     |                                                        |      |     |              |     |             |          |
|                |            |                  |          |           |              |        |        | frameworks                                             | with | the | SDGs/targets |     | in order to | properly |
| the effects    | that the   | policies/actions |          | taken     | at those     | levels | of     |                                                        |      |     |              |     |             |          |
monitortheeffectsthatlocalpolicieshaveonthe2030
| governance | have on | progress. | Although |     | the role | of regional |     |     |     |     |     |     |     |     |
| ---------- | ------- | --------- | -------- | --- | -------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
Agenda.
| and local       | governments | was     | recognized |        | in the        | Agenda       | itself  |             |                 |           |            |                      |                   |     |
| --------------- | ----------- | ------- | ---------- | ------ | ------------- | ------------ | ------- | ----------- | --------------- | --------- | ---------- | -------------------- | ----------------- | --- |
|                 |             |         |            |        |               |              |         | • Necessity | to              | find even | the        | less obvious         | associations      |     |
| [1], the latest | SDG         | Reports | pointed    | to     | their central |              | role in |             |                 |           |            |                      |                   |     |
|                 |             |         |            |        |               |              |         | between     | locally         | relevant  | indicators |                      | and SDGs/targets, |     |
| achieving       | the Agenda  | since   | 65%        | of the | targets       | are actually |         |             |                 |           |            |                      |                   |     |
|                 |             |         |            |        |               |              |         | which       | is a nontrivial |           | task due   | to context-dependent |                   | in- |
linkedtotheirwork[6].
teractionsbetweentheSDGs/targets.
However,thereareseveralchallengesrelatedtoSDGmon-
|     |     |     |     |     |     |     |     | Necessity | to  | complement/facilitate |     |     | the nontrivial | and |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --------------------- | --- | --- | -------------- | --- |
•
itoringthroughindicatorsfromtheGlobalframeworkorother time-consuming manual mapping process done by hu-
locallyrelevantindicatorsreportedtodate.Forexample,the
|             |             |        |           |            |     |           |     | man experts | through |     | thoroughly | evaluated | data-driven |     |
| ----------- | ----------- | ------ | --------- | ---------- | --- | --------- | --- | ----------- | ------- | --- | ---------- | --------- | ----------- | --- |
| statistical | data of the | Global | indicator | framework, |     | collected |     |             |         |     |            |           |             |     |
methods,capableofinferringsuchlessobviousassoci-
andcompiledatthenationallevel,stillhasgapswithrespect
ationsinatransparentmanner.
toitstimelines,geographiccoverage,anddisaggregationby
|     |     |     |     |     |     |     |     | • Variable | statistical | data | quality | and | quantity | in certain |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ----------- | ---- | ------- | --- | -------- | ---------- |
required dimensions as a result of the uneven statistical ca- geographic regions, even for the indicators from the
pacityofthecountries[6],[7].Forexample,theSDGReport
|     |     |     |     |     |     |     |     | Global | framework, | which | requires |     | consideration | of al- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ---------- | ----- | -------- | --- | ------------- | ------ |
2023[6]highlightsthatmorethan50%ofthelatestavailable
|     |     |     |     |     |     |     |     | ternative | types | of data | available | in  | large volumes | but |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ----- | ------- | --------- | --- | ------------- | --- |
datacomefrom2020and2021,whilethelackofinternation-
|                 |      |                 |     |            |     |          |     | underutilized |     | for the | purpose. | An  | example | is textual |
| --------------- | ---- | --------------- | --- | ---------- | --- | -------- | --- | ------------- | --- | ------- | -------- | --- | ------- | ---------- |
| ally comparable | data | is particularly |     | noticeable |     | for SDGs | 5,  |               |     |         |          |     |         |            |
dataavailableintheformofSDG-relatedscientificpub-
13,and16,forwhichmorethanhalfofthe193countrieslack lications, Voluntary National/Local Reviews, progress
| such data. | This makes | progress |     | monitoring | challenging |     | and |     |     |     |     |     |     |     |
| ---------- | ---------- | -------- | --- | ---------- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
reports,newsarticles,andsimilar(seeSectionII-B).
| was especially | emphasized |     | during | the COVID-19 |     | pandemic |     |     |     |     |     |     |     |     |
| -------------- | ---------- | --- | ------ | ------------ | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
Lackofcomprehensivebenchmarksofthestrengthsand
•
whenevenwell-establishedmethodsfordatacollection(e.g.,
|            |        |             |      |     |          |            |     | weaknesses | of             | the | various | artificial    | intelligence | (AI) |
| ---------- | ------ | ----------- | ---- | --- | -------- | ---------- | --- | ---------- | -------------- | --- | ------- | ------------- | ------------ | ---- |
| in-person) | became | unavailable | [7]. | The | need for | innovative |     |            |                |     |         |               |              |      |
|            |        |             |      |     |          |            |     | models     | for processing |     | text,   | e.g., (large) | language     | mod- |
datacollectionmethods,non-standarddatasources,anddata els or sentence encoders, in associating indicators to
integrationfrommultiplesourcesisevident,butonlythrough
SDGs/targets(seeSectionII-B).
| careful design | and | evaluation | [6], | [7]. Furthermore, |     | the | use |     |     |     |     |     |     |     |
| -------------- | --- | ---------- | ---- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Ourcontributionstotacklethechallengesmentionedabove
| of the Global | indicator | framework |     | in  | measuring | progress |     |     |     |     |     |     |     |     |
| ------------- | --------- | --------- | --- | --- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
consistofthefollowing:
| toward the | SDGs | is not | always | a straightforward |     | task | at  |            |     |             |     |                |           |     |
| ---------- | ---- | ------ | ------ | ----------------- | --- | ---- | --- | ---------- | --- | ----------- | --- | -------------- | --------- | --- |
|            |      |        |        |                   |     |      |     | Developing | a   | text-driven |     | model-agnostic | framework |     |
•
1https://unstats.un.org/sdgs/indicators/indicators-list Embed4SD,tofindassociationsbetweenindicatorsand
| 2   |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME11,2023 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2025.3595894
Gjorgjevikjetal.:BenchmarkingSentenceEncodersinAssociatingIndicatorswithSustainableDevelopmentGoalsandTargets
the(1)17SDGsand(2)169targets. by aligning different indicator sets with the SDGs, targets,
• Comprehensive benchmarking of the potential of a di- orglobalindicatorsfromthe2030Agenda.Theinteractions
verseportfolioofpubliclyavailablepre-trainedgeneral- between the SDGs, targets, indicators, and policies have al-
purposesentenceencodersinsolvingtheproblem. ready been studied by the research community, and several
• Evaluating the fine-tuned sentence encoders on two secondary studies [5], [14] have summarized the primary
"main" tasks, i.e., multi-class classification of an indi- fromdifferentaspects.Inthesecondsubsection,wefocuson
catortooneofthe(1)17SDGsand(2)169targets,as thoseusingtextualdataforthosepurposes.
well as two "auxiliary" (zero-shot classification) tasks,
unseenduringfine-tuningandvalidation. A. FACILITATINGTHESDGMONITORINGAT
• Evaluating the fine-tuned sentence encoders using five (SUB)NATIONALLEVEL
indicatorsetsusedatnational,regional,andlocallevels The 2030 Agenda encourages UN member states to con-
of governance (with around 800 indicators in total), duct reviews of their progress in implementing the Agenda
whichdifferintheirpurposeandcharacteristics. on national and subnational levels on a regular basis [1]
• Creating a new domain-specific dataset to enable sen- and share experiences through Voluntary National Reviews
tenceencoderfine-tuning. (VNRs) of the High-level Political Forum for Sustainable
• Post-hoc analyses using methods from explainable ar- Development. In addition to the indicators from the Global
tificial intelligence (xAI) to better understand the fac- framework,intheirVNRs,thememberstatescanreportthe
tors influencing the results and gain insight for future useofadditionalnationalorsubnationalindicatorstomeasure
improvements. the progress in achieving the SDGs and are encouraged to
• Complementingandpotentiallyfacilitatingthenontriv- include an annex with data [15]. Voluntary Local Reviews
ialandtime-consumingmanualindicatormappingpro- (VLRs)aresubnationalreviewsonprogressinachievingthe
cess done by human experts by providing them with SDGsproducedbyregionalorlocalgovernments.According
data-drivensuggestionsonindicatorsassociationstothe totheGuidelinesforVLRsfrom2020[16],thereviewshould
SDGs/targets. provideinformationontheindicatorsetsused,i.e.,ifthoseare
• Publicavailabilityoftheframeworktoallowforrepro- already available indicator sets or newly developed ones. In
ducibility,criticalassessment,andimprovement. thelatercase,detailsonthemethodologyshouldbeprovided.
Through the proposed framework and experiments, the TheEuropeanUnion(EU)SDGindicatorsetwasadopted
followingresearchquestionswereaddressed: in2017andconsistsof100indicators,ofwhich33monitor
1) How can textual data and general-purpose pre-trained multiple SDGs, and 68 are aligned with indicators from the
sentence encoders be used to automate the process of Globalframework[17].Itallowsmonitoringoftheprogress
associatingnational,regional,andlocalindicatorswith in achieving the SDGs in the context of EU policies, and
theSDGsandtargetsfromtheUN2030Agenda? its development was led by the statistical office of the EU
2) What improvement does domain-specific fine-tuning –EUROSTATincooperationwithotherrelevantinstitutions
ofgeneral-purposepre-trainedsentenceencodersbring [17]. The project URBAN2030, supported by the European
totheirperformanceinsolvingthemainandauxiliary Commission Directorate General for Urban and Regional
tasks? PoliciesandrealizedbytheJointResearchCentre,aimedto
3) Whatkindoftextualdatashouldbeusedtodescribethe offerEUcitiesaframeworkfordevelopingVLRsandtohelp
SDGs,targets,andindicatorswhenusingtheproposed achievingtheSDGsatthelocalorregionallevel[18].Output
framework? oftheprojectwasthefirsteditionoftheEuropeanHandbook
Therestofthearticleisorganizedasfollows.Itstartswith forSDGVoluntaryLocalReviewsin2020[19].Theproject
a brief overview of different initiatives that facilitate SDG URBAN2030-IIresultedinasecondeditionoftheHandbook
monitoringatnationalandsubnationallevelsofgovernance, in2022[10].The72exampleindicatorsinthesecondedition,
as well as the related scientific literature studying the text comingfrominternationalinstitutions,Europeaninstitutions,
classificationtoSDGs/targets.Itisfollowedbytwosections research institutes, and regional governments, help regional
describing the dataset creation process, the pre-trained sen- and local governments in monitoring progress towards the
tence encoders benchmarking, fine-tuning, validation, and SDGsand54targets[10].TheprojectREGIONS2030,sup-
testing,aswellasthepost-hocanalysisofthefactorsinfluenc- portedbytheEuropeanParliamentandrealizedbytheJoint
ingthetestresults,bothintermsofthemethodologyitselfand Research Centre, aimed to identify indicators relevant for
in terms of the experimental choices. Finally, the validation monitoringtheSDGattheregionallevel[11],[20].Itstarted
andtestresultsarepresented,alongwithadiscussionofthe withasetof83indicators[20],testedinseveralpilotregions,
research questions. Embed4SD implementation is available and resulted in a final set of 116 indicators [11]. As part
onGitHub[13]. of the United for Smart Sustainable Cities (U4SSC) UN
initiative, coordinated by the International Telecommunica-
II. RELATEDWORK tionUnion(ITU),UnitedNationsEconomicCommissionfor
Thissectionbrieflydescribesinitiativesaimedatfacilitating Europe (UNECE), and United Nations Human Settlements
SDGmonitoringatthenationalorsubnationallevel,mainly Programme (UN-Habitat), a set of key performance indica-
VOLUME11,2023 3
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2025.3595894
Gjorgjevikjetal.:BenchmarkingSentenceEncodersinAssociatingIndicatorswithSustainableDevelopmentGoalsandTargets
tors2 wasdevelopedtoallowcitiestomeasuretheirprogress beddings,andpre-trainedUniversalSentenceEncodermod-
in becoming smart and sustainable through ICT, as well els were used. Meier et al. [28] presented an open-source R
as measure their progress in achieving the SDGs. The UN package detecting mentions of SDGs in text using existing
Sustainable Development Solutions Network (SDSN)3 aims labelingmethodsalreadypresentedintheresearchliterature.
tomobilizevariousinstitutionsworldwidetotakeactionsto Addition of new methods was also possible. The methods
achievetheSDGs.Amongthemanyinitiatives,someaimto recognizedmentionsofSDG-relatedkeywordsintext.Wulff
improvethemonitoringoftheSDGsattheurbanorregional etal.[29]extendedthepreviousresearchpaper[28]byshow-
levelbyaligninglocalindicatorswiththeSDGs. ing that an ensemble method combining different labeling
|     |     |     |     |     |     |     |     | methods | improved | the | performance |     | of a single | method. | In  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | -------- | --- | ----------- | --- | ----------- | ------- | --- |
B. METHODSFORTEXTCLASSIFICATIONTOSDGSOR addition,theauthorscomparedtheperformanceofthediffer-
entlabelingmethodsandconcludedthatfine-tuninglanguage
TARGETS
The latest advances in machine learning (ML) have huge modelsforthatpurposewasapromisingbutstillunexplored
potential to help solve sustainable development problems. researchdirection.HajikhaniandCole[30]comparedmodels
|          |      |        |           |          |             |     |         | specifically | developed |     | to detect | SDGs | in text | with | general- |
| -------- | ---- | ------ | --------- | -------- | ----------- | --- | ------- | ------------ | --------- | --- | --------- | ---- | ------- | ---- | -------- |
| However, | some | of the | obstacles | to their | application |     | are re- |              |           |     |           |      |         |      |          |
lated to the required domain-specific knowledge which ML purposelargelanguagemodels(LLMs)suchasGPT-3.5.The
modelsusedTF-IDFweighting,Word2Vecembeddings,and
| practitioners | usually | lack, | as  | well as | the unavailability |     | of  |     |     |     |     |     |     |     |     |
| ------------- | ------- | ----- | --- | ------- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
standardizedbenchmarksfortheproblems[21].Furthermore, theDoc2Vecmethod[31]incombinationwithMLclassifiers
the use of AI (in general) in achieving the SDGs requires trainedontextfromscientificpublications.Theauthorscon-
cludedthatspecializedmodelsweremorerobustandprecise
| awareness | of the | SDG | interactions | and | sufficient |     | oversight |     |     |     |     |     |     |     |     |
| --------- | ------ | --- | ------------ | --- | ---------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
since it can have both positive and negative impacts [22], but general-purpose LLMs were able to identify SDGs in a
broadersetoftexts.
[23].Whenitcomestotheuseofnaturallanguageprocessing
|     |     |     |     |     |     |     |     | The goal | of  | the Open | SDG | (OSDG) | project | [32] | was to |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | -------- | --- | ------ | ------- | ---- | ------ |
(NLP)advancesbasedondeeplearning(DL)insolvingSDG-
relatedproblems,ourliteraturereviewshowedthatitstarted integratevariousmethodsforclassifyingtexttoSDGsbased
onontologies,supervisedorunsupervisedML,bycreatingan
| attracting | attention | only | in the | last | few years. | The | use of |     |     |     |     |     |     |     |     |
| ---------- | --------- | ---- | ------ | ---- | ---------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
textual data to associate external indicators with the SDGs, ontologyofmorethan14,000relevantkeywordsandmapping
|     |     |     |     |     |     |     |     | them to | the themes | from | Microsoft |     | Academic | Graph. | Any |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ---------- | ---- | --------- | --- | -------- | ------ | --- |
targets,orglobalindicatorsfromthe2030Agenda(asdone
|                  |     |           |     |       |      |         |          | new text | was first | classified |     | against | those | themes | through |
| ---------------- | --- | --------- | --- | ----- | ---- | ------- | -------- | -------- | --------- | ---------- | --- | ------- | ----- | ------ | ------- |
| in this article) | is  | uncommon, | but | there | is a | growing | interest |          |           |            |     |         |       |        |         |
in ML-based classification of text to SDGs in general. This methods using TF-IDF weighting and then mapped to the
|     |     |     |     |     |     |     |     | OSDG ontology. |     | The | updated | framework, |     | OSDG | 2.0, was |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | ------- | ---------- | --- | ---- | -------- |
subsectionbrieflysummarizessuchresearcharticles.
Sorianoetal.[24]presentedanapproachtoclassifyshort presented in [33]. It combined keyword-based text classifi-
|            |           |              |     |         |       |         |      | cation to      | SDGs | with     | ML-based | classification |     | models.       | The |
| ---------- | --------- | ------------ | --- | ------- | ----- | ------- | ---- | -------------- | ---- | -------- | -------- | -------------- | --- | ------------- | --- |
| target and | indicator | descriptions |     | to SDGs | using | several | lan- |                |      |          |          |                |     |               |     |
|            |           |              |     |         |       |         |      | OSDG Community |      | Dataset, |          | consisting     | of  | text excerpts | la- |
guagemodelsbasedonBERT.Thedatasetconsistedof400
sentences that described global targets and indicators, and beled with the SDGs from 1 to 16, was made publicly
available.Anginetal.[34]fine-tunedpre-trainedBERTand
| were labeled | with | SDGs. | Two | types | of experiments |     | were |     |     |     |     |     |     |     |     |
| ------------ | ---- | ----- | --- | ----- | -------------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
conducted, the first encoding the descriptions in a common RoBERTa models on the OSDG Community Dataset for
multi-labeltextclassificationtoSDGs.Theyalsoconsidered
| vector space | and | classifying | them | based | on  | their | k nearest |                |     |     |          |         |           |     |        |
| ------------ | --- | ----------- | ---- | ----- | --- | ----- | --------- | -------------- | --- | --- | -------- | ------- | --------- | --- | ------ |
|              |     |             |      |       |     |       |           | a conventional |     | NLP | pipeline | (TF-IDF | weighting |     | and ML |
neighbors,whilethesecondfine-tuningthemodelsformulti-
classclassificationtoSDGs.ChatGPTwasevaluatedaswell. classifiers). The highest F1 score in the multi-label clas-
|     |     |     |     |     |     |     |     | sification | was | 0.91, achieved |     | with | a fine-tuned | RoBERTa |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | -------------- | --- | ---- | ------------ | ------- | --- |
Theaccuracyofthefine-tunedclassifiersdidnotexceed0.7,
andChatGPThadanaccuracyof0.84(±0.04).Matsuietal. model.Hsuetal.[35]classifiedtextagainsttheSDGsusinga
combinationofconventionalNLPmethods,i.e.,atopicmodel
[25]fine-tunedaBERTmodel(pre-trainedonJapanesetext)
|          |           |         |     |          |     |         |        | classifier | and a | semantic | link | classifier. | Fonseca | et  | al. [36] |
| -------- | --------- | ------- | --- | -------- | --- | ------- | ------ | ---------- | ----- | -------- | ---- | ----------- | ------- | --- | -------- |
| on 3,758 | sentences | related | to  | the SDGs | to  | perform | multi- |            |       |          |      |             |         |     |          |
labelclassificationofasentencetothe17SDGs.Theauthors presentedamethodformappingpatentdocumentstoSDGs.
|     |     |     |     |     |     |     |     | TF-IDF, | Word2Vec | embeddings, |     | and | Doc2Vec | were | used |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | -------- | ----------- | --- | --- | ------- | ---- | ---- |
thenusedthepredictionsforasetofindicatorstranslatedto
|          |          |     |                   |     |     |        |           | for text | representation |     | in combination |     | with | ML  | classifiers |
| -------- | -------- | --- | ----------------- | --- | --- | ------ | --------- | -------- | -------------- | --- | -------------- | --- | ---- | --- | ----------- |
| Japanese | to study | the | SDG co-occurrence |     |     | and to | visualize |          |                |     |                |     |      |     |             |
SDGinterlinks.Lietal.[26]presentedamethodformapping trained on text from scientific publications. Guisiano et al.
[37]presentedamethodformulti-labelclassificationoftext
texttoSDGsandtargetsthroughalexiconofsearchqueries
relevanttoeachSDG/target.TherelevanceofanSDG/target toSDGs.Thetraining/testdataconsistedof724textswithan
averageof374wordsandwasusedtofine-tuneapre-trained
foratextwasdeterminedusingthenumberofitsmentionsin
BERTmodelforthepurpose.Smithetal.[38]appliedNLP
thetext.Sovranoetal.[27]presentedamethodformulti-label
classification of UN Resolutions to SDGs at the paragraph methods,includingDoc2Vecandnetworkanalysis,toyearly
|     |     |     |     |     |     |     |     | UN SDG | Progress | and | Information |     | reports | to study | SDG |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | -------- | --- | ----------- | --- | ------- | -------- | --- |
level.TextrepresentationmethodssuchasTermFrequency–
InverseDocumentFrequency(TF-IDF),averageGloVeem- interactions. Fotopoulou et al. [39] presented a knowledge
graphthatfacilitatesthetrackingoftheprogressinachieving
theSDGsatnationalandregionallevel.SeveralexistingML
2https://u4ssc.itu.int/u4ssc-kpi/
3https://www.unsdsn.org/ approaches(e.g.,[25],[38])werementionedbytheauthorsas
| 4   |     |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME11,2023 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2025.3595894
Gjorgjevikjetal.:BenchmarkingSentenceEncodersinAssociatingIndicatorswithSustainableDevelopmentGoalsandTargets
applicableinpopulatingandanalyzingtheknowledgegraph. The analyses included term weighting using TF-IDF, topic
Mishra et al. [40] proposed a method that generates on- modelingwithLatentDirichletAllocation,andfine-tuninga
tologies from text data (e.g., Wikipedia, social media, blog pre-trained BERT model to classify tweets to SDGs which
posts, news articles) to anticipate the impact of policymak- achieves an overall F1 score of 0.82. The fine-tuning and
ers’ decisions on climate change (SDG 13). The process evaluationdatasetsweresampledfromadatasetconsistingof
consisted of entity extraction, relation extraction, and on- around57,843tweets.Morales-Hernández[50]comparedthe
tology formation. A fine-tuned RoBERTa model was used performanceofmulti-labelclassificationmodelsinclassify-
for entity extraction, while Graph Convolutional Networks ingresearcharticlestotheSDGs.TheDimensionsdatabaseof
and multi-head attention layers for relation extraction. Cho researcharticleslabeledwithSDGswasusedfortrainingand
and Ackom [41] evaluated national commitments to SDGs evaluation. For the period between 2015 and 2021, 180,852
and emissions reduction of 67 countries through compari- articles from organic agriculture were selected and repre-
son of their action plans reported in VNRs and Nationally sentedthroughtheirtitleandabstract.NaiveBayes,Logistic
Determined Contributions. TF-IDF weighting was used to Regression, Support Vector Machines, and Random Forest
representVNRsintovectorform,multidimensionalscalingto classifiers were compared. Nedungadi et al. [51] analyzed
reducethevectordimensionintoalowerone,andcosinedis- research articles between 2013 and 2024 using BERTopic
tancetoanalyzevectordistributioninspaceinrelationtoeco- modeling to detect the influence of big data and AI to the
nomic/geographical/environmentalfeatures.Koundourietal. SDGs.Thetitlesandabstractsof1,288articleslabeledwith
[42] analyzed if the SDGs are integrated into 74 European SDGs from the Dimensions database were used. The topics
Green Deal policy documents between 2019 and 2023. A andtheirrepresentativekeywordswereidentified.
custom dataset of 35,001 text excerpts describing the SDGs To visually present the topics prevalent in the related ar-
(comingfromOSDGCommunityDatasetandSDG-Tracker ticles, we analyzed the co-occurrence of keywords in their
among the rest) was used to fine-tune a pre-trained BERT abstracts with VOSviewer software [52] (configuration de-
modelinclassifyingpolicydocumentstotheirrelatedSDGs. tails given in Appendix B). The results are presented using
Benjiraetal.[43]studiedindicatorcomputationusingLLMs a keyword co-occurrence network (Figure 1) and keyword
and knowledge graphs. They used rule-based filtering and densityvisualization(Figure2).Figure1illustratesthekey-
LLMs for schema mapping, to find links between diverse word (node) clusters and keyword links. The clusters have
data sources and indicator metadata about their computa- different colors. The thickness of the link corresponds to
tion. They joined the mappings in a knowledge graph to the strength of the connection between the two keywords,
allowqueryingthegraphtopologyonindicatorcomputation. i.e., the frequency of their simultaneous appearance in the
Larosa et al. [44] used LLMs (ClimateBERT and Gemini abstracts. The size of the nodes reflects the number of ab-
1.0)andpromptengineeringmethodstoprocessclimateand stracts in which they appear. The most common keyword
sustainability policies to classify them into relevant SDGs is "SDG" (including all its synonyms), but other common
andtofindsynergiesandtrade-offsbetweentheSDGs.The keywords are "target", "research", "progress", "text", and
authors state that the 80% match with expert labels was "data". The green cluster (in general) refers to the areas
promising although the score was imbalanced among the of sustainable development covered by the articles, where
SDGs. Koundouri et al. [45] analyzed the relatedness of 44 in addition to keywords such as "progress", "integration",
Human Security reports to the SDGs using keyword-based and "gap", "climate action", "health", "clean energy", "wa-
matching, TF-IDF weighting, and Random Forestclassifier. ter" are also common, among the rest. The red and purple
The results were compared to those achieved by language clusters are mainly composed of methodology-related key-
modelssuchasBERT,DistilBERT,andELECTRA,forwhich words. The first contains common keywords such as "text",
theauthorsnotedthattheirperformancewashinderedbythe "document", "model", "task", "machine learning, "classifi-
small-sizeddomain-specifictrainingdataset.Themethodwas cation", as well as such specific to those fields like "per-
madeavailablethroughawebapplication.Lietal.[46]ana- formance","keyword","BERT",and"TF-IDF".Thesecond
lyzedChina’sattentiontowardstheSDGsintheGovernment containskey-phraseslike"largelanguagemodel","language
Work Reports between 2010 and 2020. To define different model"andtheirrelevantperformance-relatedattributes(e.g.,
explanatoryvariablesusedwitheconometricempiricalmod- "accuracy","capability").Keywordssuchas"transparency",
els,amongtherest,theauthorscombinedSDG-relatedword "cost",and"complexity"appearnear"largelanguagemodel"
and phrase frequency analysis, TF-IDF weighting, cosine- and "artificial intelligence" as well. While the generic key-
based text similarity. Strelkovskii and Komendantova [47] word"document"isthemostprevalent,specifictypesofdoc-
used the SDG Mapper tool [48] to find SDG mentions in umentsarealsomentioned(e.g.,"report"and"policy").Fig-
66 national hydrogen strategies, quantify the frequencies of ure2illustratesthedensityofdifferentpartsofthenetwork.It
SDG-related keywords, and visualize them. The SDG Map- bringsadditionalclarity,asitdisplayscertainkeywordsthat
per [48] relied on SDG and target-related keywords defined donotappearinFigure1duetospacelimitations.
by text mining and domain experts, followed by a keyword In the remainder of this section we discuss the identified
matchingproceduretoidentifythemintext.Ramanetal.[49] gapsintherelatedworkwhichourmethodtriestofillfrom
performedavarietyofSDG-relatedanalysesofTwitterposts. threeaspects,i.e.,(1)targetclassesinthetextclassification
VOLUME11,2023 5
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2025.3595894
Gjorgjevikjetal.:BenchmarkingSentenceEncodersinAssociatingIndicatorswithSustainableDevelopmentGoalsandTargets
|     |     |     |     |     | monitoring | user | actor |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ---------- | ---- | ----- | --- | --- | --- | --- | --- | --- | --- |
text source
variety
connection
|     |     |     |     |     |                |     | osdg journal |     |         |     |     |     |     |     |
| --- | --- | --- | --- | --- | -------------- | --- | ------------ | --- | ------- | --- | --- | --- | --- | --- |
|     |     |     |     |     | classification |     |              |     | keyword |     |     |     |     |     |
performance
|     |     |     |     |     | bert |     | machine learning |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ---- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- |
specific sdg
|     |     |     |     | relevance   |       | initiative   |             | project policymaker |              | recognition | land |       |     |     |
| --- | --- | --- | --- | ----------- | ----- | ------------ | ----------- | ------------------- | ------------ | ----------- | ---- | ----- | --- | --- |
|     |     |     |     |             | label | tf idf       |             |                     |              |             |      |       |     |     |
|     |     |     |     |             | text  |              | methodology |                     |              | foundation  |      |       |     |     |
|     |     |     |     | combination | task  |              |             |                     | agenda peace |             |      |       |     |     |
|     |     |     |     |             |       | article tool |             | document            |              |             |      | water |     |     |
limitation
|     |     |               |                      | sensitivity           |             |               | researcher |                     | machine                 |                 | education         |                                        |     |     |
| --- | --- | ------------- | -------------------- | --------------------- | ----------- | ------------- | ---------- | ------------------- | ----------------------- | --------------- | ----------------- | -------------------------------------- | --- | --- |
|     |     |               |                      | activity              |             |               |            | need available data |                         |                 |                   | trade off                              |     |     |
|     |     |               |                      |                       | model       | dataset       |            | lack                |                         |                 |                   | life                                   |     |     |
|     |     |               |                      |                       |             |               | s d g      | p r o g r e s s     |                         |                 | climat e   a c ti | o n re s p o n s ib l e  c o nsumption |     |     |
|     |     |               | a cc u r a           | c y                   |             |               |            | development         |                         |                 |                   |                                        |     |     |
|     |     | language mode | l                    |                       | application | field         |            | r e s e arch        |                         |                 |                   | c le a n   e n e r g y                 |     |     |
|     |     |               |                      |                       |             |               | a n a lys  | is                  |                         | future research |                   |                                        |     |     |
|     |     |               | s ig n               | i fic ant improvement | deep        |               |            | a p p r o a c h     |                         |                 | p r o d u         | c ti on                                |     |     |
|     |     |               |                      |                       |             | process       |            |                     | sustainable development |                 |                   | sdg12                                  |     |     |
|     |     | precision     | cost                 |                       |             | indicator     |            |                     |                         |                 |                   |                                        |     |     |
|     |     |               |                      |                       |             | united nation | study      | contrast            |                         | integration     |                   | decent work                            |     |     |
|     |     |               |                      | complexity            |             |               |            |                     | area                    |                 | health            |                                        |     |     |
|     |     |               |                      |                       | challenge   |               |            |                     | literature              |                 | pattern           |                                        |     |     |
|     |     |               | large language model |                       |             |               |            | country target      |                         | opportunity     |                   |                                        |     |     |
|     |     |               |                      |                       |             | order         | issue      |                     | alignment               |                 | gender equality   |                                        |     |     |
climate change
|     |     |     |            |            | mapp in g         |          |         | impact         |     | gap           |      |     |     |     |
| --- | --- | --- | ---------- | ---------- | ----------------- | -------- | ------- | -------------- | --- | ------------- | ---- | --- | --- | --- |
|     |     |     | capability |            | k n owledge graph | solution |         |                |     |               |      |     |     |     |
|     |     |     |            |            |                   | data     | insight | sustainability |     |               | sdg7 |     |     |     |
|     |     |     |            | data frame |                   |          |         |                |     | text analysis |      |     |     |     |
|     |     |     |            |            |                   |          |         | report policy  |     |               |      |     |     |     |
|     |     |     | definition |            | exploitation      |          |         |                |     |               |      |     |     |     |
artificial intelligence
|     |     |     |     |     | transparency |            |             | ai application | priority |     |     |     |     |     |
| --- | --- | --- | --- | --- | ------------ | ---------- | ----------- | -------------- | -------- | --- | --- | --- | --- | --- |
|     |     |     |     |     |              |            | corpus      |                | covid    |     |     |     |     |     |
|     |     |     |     |     |              | commitment | achievement |                |          |     |     |     |     |     |
|     |     |     |     |     |              |            |             | effect decade  |          |     |     |     |     |     |
VOSviewer
FIGURE1. Keywordco-occurrencenetworkcreatedfromtheabstractsofthearticlesreferencedinSectionII-B.CreatedwiththeVOSviewersoftware[52].
- SDGs and/or targets, (2) text on which the methods were theresults.Themethodpresentedby[25]doesnotallowin-
evaluated,and(3)comparisonofstate-of-the-artNLPmeth- dicatorclassificationtotargetsasourmethoddoes,islimited
ods.First,mostoftherelatedmethodsfortextclassification toJapaneseinputtext,andfocusesmainlyontheproblemof
toSDGsand/ortargets[24],[25],[27],[34]–[37],[42],[44], SDG interlink detection. Third, while several related papers
[45], [50] only allow classification to the 17 SDGs, not ad- use language models [24], [25], [29], [34], [37], [42], [45],
dressingthemorechallengingproblemoftextclassification largelanguagemodels[24],[30],[44]andsentenceencoders
tothe169targets,agapwetriedtofillwithourpaper(inthe [27]fortextclassificationtoSDGs/targets,acomprehensive
contextofindicatordescriptions).Onlyonerelatedpaper[26] benchmarkingofthestrengthsandweaknessesofsuchmod-
classifies text to both SDGs and targets, but it differs from elsinassociatingindicatorswithSDGsandtargetsislacking
our work methodologically (they use a more conventional and is more than required. In this paper, we contributed in
NLP approach) and in its objective (general text classifica- filling that gap in the context of sentence encoders. This
tion vs. classification of indicator descriptions). Therefore, paper further extends the work presented in [53] by adding
the performance of their method in multi-class and multi- preliminary similarity-based comparison of the fine-tuning
labelindicatordescriptionclassificationshouldbeevaluated and test datasets (described in Sections III-B and V-A) and
additionally. Second, while many related papers address the addingfournewreal-worldindicatortestdatasetsinthetest-
problem of general text classification to SDGs/targets, only ingphase(testdatasets2-5,describedinSectionIV-A2).Asa
few are specifically evaluated in classification of indicator result,thispapersignificantlyextendsthetestresultanalysis
descriptions [24], [25]. Compared to the work of [24], our (SectionV-C)andthediscussionofresearchquestions2and
method is mainly a representation learning method that can 3(SectionVI),comparedto[53].
| be used for | non-parametric |       | classification |           | of both | SDGs        | and |             |     |     |     |     |     |     |
| ----------- | -------------- | ----- | -------------- | --------- | ------- | ----------- | --- | ----------- | --- | --- | --- | --- | --- | --- |
| targets at  | the same       | time, | while          | capturing | the     | relatedness |     | III. METHOD |     |     |     |     |     |     |
betweentheSDGs.Additionally,ourworkwasevaluatedona A. OVERVIEW
largerindicatorset,offeredcomparisonofalargernumberof The model-agnostic Embed4SD framework for associating
sentence encoders of several categories, proposed a slightly indicators with SDGs and targets based on their textual de-
more complex fine-tuning dataset creation process (in our scriptionsisillustratedinFigure3.Itformulatesthesolution
|           |             |        |          |          |     |          |     | to the | problem | as            | text classification, |              | first by representing |        |
| --------- | ----------- | ------ | -------- | -------- | --- | -------- | --- | ------ | ------- | ------------- | -------------------- | ------------ | --------------------- | ------ |
| opinion), | and offered | a more | thorough | post-hoc |     | analysis | of  |        |         |               |                      |              |                       |        |
|           |             |        |          |          |     |          |     | SDG,   | target, | and indicator |                      | descriptions | in a common           | vector |
| 6         |             |        |          |          |     |          |     |        |         |               |                      |              | VOLUME11,2023         |        |
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2025.3595894
Gjorgjevikjetal.:BenchmarkingSentenceEncodersinAssociatingIndicatorswithSustainableDevelopmentGoalsandTargets
|     |     |     |     | monitoring | user | actor |     |     |     |     |     |
| --- | --- | --- | --- | ---------- | ---- | ----- | --- | --- | --- | --- | --- |
text source
variety
connection
|     |     |     |     |                |     | osdg journal |     |         |     |     |     |
| --- | --- | --- | --- | -------------- | --- | ------------ | --- | ------- | --- | --- | --- |
|     |     |     |     | classification |     |              |     | keyword |     |     |     |
performance
|     |     |     |     | bert |     | machine learning |     |     |     |     |     |
| --- | --- | --- | --- | ---- | --- | ---------------- | --- | --- | --- | --- | --- |
specific sdg
|     |     |     | relevance   |       | initiative   |             | project policymaker |              | recognition | land  |     |
| --- | --- | --- | ----------- | ----- | ------------ | ----------- | ------------------- | ------------ | ----------- | ----- | --- |
|     |     |     |             | label | tf idf       |             |                     |              |             |       |     |
|     |     |     |             | text  |              | methodology |                     |              | foundation  |       |     |
|     |     |     | combination | task  |              |             |                     | agenda peace |             |       |     |
|     |     |     |             |       | article tool |             | document            |              |             | water |     |
limitation
|     |               |                      | sensitivity           |             |               | researcher |                     | machine                 |         | education         |                                 |
| --- | ------------- | -------------------- | --------------------- | ----------- | ------------- | ---------- | ------------------- | ----------------------- | ------- | ----------------- | ------------------------------- |
|     |               |                      | activity              |             |               |            | need available data |                         |         |                   | trade off                       |
|     |               |                      |                       | model       | dataset       |            | lack                |                         |         | life              |                                 |
|     |               |                      |                       |             |               | s d g      | p r o g r e s s     |                         | climat  | e   a c ti o n re | s p o n s ib l e  c o nsumption |
|     |               | a cc u r a           | c y                   |             |               |            | development         |                         |         |                   |                                 |
|     | language mode | l                    |                       | application | field         |            | r e s e arch        |                         |         | c                 | le a n   e n e r g y            |
|     |               |                      |                       |             |               | a n a lys  | is                  | future research         |         |                   |                                 |
|     |               | s ig n               | i fic ant improvement | deep        |               |            | a p p r o a c h     |                         |         | p r o d u c ti on |                                 |
|     |               |                      |                       |             | process       |            |                     | sustainable development |         |                   | sdg12                           |
|     | precision     | cost                 |                       |             | indicator     |            |                     |                         |         |                   |                                 |
|     |               |                      |                       |             | united nation | study      | contrast            | integration             |         |                   | decent work                     |
|     |               |                      | complexity            |             |               |            |                     | area                    |         | health            |                                 |
|     |               |                      |                       | challenge   |               |            |                     | literature              | pattern |                   |                                 |
|     |               | large language model |                       |             |               |            | country target      | opportunity             |         |                   |                                 |
|     |               |                      |                       |             | order         | issue      |                     | alignment               |         | gender equality   |                                 |
climate change
|     |     |            |            | mapp in g         |          |         | impact         |     | gap           |     |     |
| --- | --- | ---------- | ---------- | ----------------- | -------- | ------- | -------------- | --- | ------------- | --- | --- |
|     |     | capability |            | k n owledge graph | solution |         |                |     |               |     |     |
|     |     |            |            |                   | data     | insight | sustainability |     | sdg7          |     |     |
|     |     |            | data frame |                   |          |         |                |     | text analysis |     |     |
|     |     |            |            |                   |          |         | report policy  |     |               |     |     |
|     |     | definition |            | exploitation      |          |         |                |     |               |     |     |
artificial intelligence
|     |     |     |     | transparency |            |             | ai application | priority |     |     |     |
| --- | --- | --- | --- | ------------ | ---------- | ----------- | -------------- | -------- | --- | --- | --- |
|     |     |     |     |              |            | corpus      |                | covid    |     |     |     |
|     |     |     |     |              | commitment | achievement |                |          |     |     |     |
|     |     |     |     |              |            |             | effect decade  |          |     |     |     |
VOSviewer
FIGURE2. KeyworddensityvisualizationcreatedfromtheabstractsofthearticlesreferencedinSectionII-B.CreatedwiththeVOSviewersoftware[52].
space using a shared sentence encoder, then by classifying auxiliarytasksformulatedas(1)multi-labelclassificationof
the indicator into one or multiple classes (SDGs or targets indicatorstoassociatedSDGs(ML-IND-SDG)and(2)multi-
depending on the task being solved) using a classification labelclassificationofeachSDGtorelatedSDGs(ML-SDG-
algorithm.Theframeworkdevelopmentinvolvedthreephases SDG).Theauxiliarytaskswerenotseenduringencoderfine-
brieflydescribedbelow. tuning and validation. Therefore, with a small modification
Thefirstphaseinvolvedcreationofcustomfine-tuning/test of the classifier to allow it to do multi-label classification,
datasets, preliminary analysis of those datasets, and bench- in a zero-shot learning manner, we evaluated if the fine-
marking pre-trained general-purpose sentence encoders on tunedencodershadlearnedthemutualrelationsbetweenthe
domain-specificvalidationtasksformulatedas(1)multi-class SDGsfromthetextualfine-tuningdata,eventhoughtheyhad
classificationofindicatordescriptionstooneofthe17SDGs notbeenexplicitlygivensuchinformationinthefine-tuning
they are the most associated with (abbreviated as MC-IND- process. In the testing, different indicator sets used at the
SDG)and(2)multi-classclassificationofindicatordescrip- national,regional,orlocallevelofgovernancewereusedwith
tions to one of the 169 targets they are the most associated eachtesttask,asapplicable.Tohaveabaselineagainstwhich
with (MC-IND-TRG), i.e., the two main tasks of interest. to measure the improvement after fine-tuning, the selected
Basedontheencoders’averageperformanceonthevalidation encoders were evaluated on the test tasks and indicator sets
tasks, those with the highest performance were selected for priortotheirfine-tuning.
furtherdomain-specificfine-tuning. The third phase involved post-hoc analysis of the test re-
In the second phase, the selected sentence encoders were sultswithxAImethods,tobetterunderstandthefactorsthat
fine-tuned on domain-specific tasks. The fine-tuning was influencedthemandgaininsightsforfutureimprovementsof
done on one task at a time, selected from a set of fine- the framework. The remainder of this section describes the
tuningtasksformulatedasamulti-classclassificationofshort genericaspectsoftheframework,whileSectionIVdescribes
textual descriptions to the SDGs (abbreviated as FT-SDG) thespecificexperimentalchoices.
| or targets (abbreviated | as FT-TRG) |     | they | describe. | The | fine- |     |     |     |     |     |
| ----------------------- | ---------- | --- | ---- | --------- | --- | ----- | --- | --- | --- | --- | --- |
tuningusedcontrastiverepresentationlearningwiththetriplet B. DATASETCREATIONPROCESS,PRELIMINARY
networkarchitecture[54].Thefine-tunedsentenceencoders ANALYSISANDENCODERBASELINEBENCHMARKING
(incombinationwithaclassifier)wereevaluatedontwomain Thedatasetsusedtofine-tunethesentenceencodersconsisted
test tasks similar to the validation tasks, as well as on two ofshorttextualexcerptsdescribingtheSDGsandtargetsfrom
VOLUME11,2023 7
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2025.3595894
Gjorgjevikjetal.:BenchmarkingSentenceEncodersinAssociatingIndicatorswithSustainableDevelopmentGoalsandTargets
| Sentence  |     |     |     |     |     | Sentence encoders fine-tuning on four domain- |     |     |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | --------------------------------------------- | --- | --- | --- | --- | --- | --- |
encoders Task 1    Task 2  …           Task  N specific tasks related to sustainable development
| pre-training |     |     | P   | P   | P   |     |     |     |     |     |     |     |
| ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
on general
NLP tasks
|     |     |     |                  |     |     | Fine-tuning on  |     |       |     |     |     | Domain-  |
| --- | --- | --- | ---------------- | --- | --- | --------------- | --- | ----- | --- | --- | --- | -------- |
|     |     |     |                  |     |     | tasks FT-SDG    |     |       |     |     |     | specific |
|     |     |     | Sentence encoder |     |     | and FT-TRG      |     | Task  | FT  |     |     |          |
knowledge
(word/phrase
relatedness in
Sentence encoder
the context of
sustainable
| Prior knowledge       |     |     |     | Prior knowledge        |     |                        |            |           |           |     |     | development) |
| --------------------- | --- | --- | --- | ---------------------- | --- | ---------------------- | ---------- | --------- | --------- | --- | --- | ------------ |
|                       |     |     |     |                        |     | Fine-tuning mini-batch |            |           | Parameter |     |     |              |
| (word/phrase          |     |     |     | (from best-performing  |     |                        | embeddings |           | update    |     |     |              |
| semantic relatedness  |     |     |     | sentence encoder on    |     |                        |            |           |           |     |     |              |
| in common English)    |     |     |     | validation tasks)      |     |                        |            |           |           |     |     |              |
|                       |     |     |     |                        |     | Distance               |            | Learning  |           |     |     |              |
|                       |     |     |     |                        |     | function               |            | algorithm |           |     |     |              |
Pre-trained sentence encoders benchmarking on  Validation on tasks  Validation
domain-specific validation tasks related to  MC-IND-SDG and  performance
sustainable development MC-IND-TRG Task  VL 1     …    Task  VL  6
(for early
stopping of
| Validation on tasks  |     |     |     |     |     |     |     |     |     |     |     | the |
| -------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Sentence encoder
| MC-IND-SDG and  |     |     | Task  | 1     …     Task  | 6   |     |     |     |     |     |     | fine-tuning |
| --------------- | --- | --- | ----- | ----------------- | --- | --- | --- | --- | --- | --- | --- | ----------- |
|                 |     |     |       | VL                | VL  |     |     |     |     |     |     | process)    |
MC-IND-TRG
Training and validation
set embeddings
Sentence encoder
|     |                         |     |     |     |     | Distance | Non-parametric |            |     | Performance |     |     |
| --- | ----------------------- | --- | --- | --- | --- | -------- | -------------- | ---------- | --- | ----------- | --- | --- |
|     | Training and validation |     |     |     |     | function |                | classifier |     | function    |     |     |
set embeddings
|     | Distance | Non-parametric |     | Performance |     |     |     |     |     |     |     |     |
| --- | -------- | -------------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | function | classifier     |     | function    |     |     |     |     |     |     |     |     |
Sentence encoders testing on domain-specific test
tasks related to sustainable development
Testing on tasks
MC-IND-SDG,
Validation
|     |     |     |     |     |     | MC-IND-TRG,  |     |     | Task  | TS 1     …     Task  | TS  14 |     |
| --- | --- | --- | --- | --- | --- | ------------ | --- | --- | ----- | -------------------- | ------ | --- |
performance
ML-IND-SDG, and
ML-SDG-SDG
Sentence encoder
Training and validation
set embeddings
|     |     |     |     |     |     | Distance | Non-parametric |            |     | Performance |     | Test        |
| --- | --- | --- | --- | --- | --- | -------- | -------------- | ---------- | --- | ----------- | --- | ----------- |
|     |     |     |     |     |     | function |                | classifier |     | function    |     | performance |
FIGURE3. ConceptualdiagramofthemaincomponentsandtheirinteractionsthroughdifferentdevelopmentphasesoftheEmbed4SDframework.
various aspects (e.g., their main aim, definitions of related The validation and test datasets consisted of indicators
concepts,statisticaldata,relatedchallenges,relatedorganiza- taken from indicator frameworks used at the national, re-
tions).AllexcerptswerelabeledwiththeSDGtheydescribe, gional,orlocallevelofgovernance,labeledwithoneormulti-
while those describing a particular target were labeled with pleSDGsandtargetstheywereassociatedwith(dependingon
both the SDG and the target label. The excerpts were also thegroundtruthlabelsavailableintheindicatorframeworks
labeled with the specific aspect of the SDG they described. themselves). Two variations of the test dataset were created
Aninitialdatasetwascreatedandusedtosampleseveralfine- from each indicator framework, differing in the length of
tuningdatasetsusingdifferentstratifiedsamplingstrategies. the text used to represent the indicators (experimental setup
The main idea was to analyze how the fine-tuning dataset described in Section IV-A2). The process of creating the
size and structure impacted the results (experimental setup validationandtestdatasetsisillustratedinFigure5.
describedinSectionIV-A1).Thefine-tuningdatasetcreation
|     |     |     |     |     |     | To  | get apriori | insights | in  | the content | of  | the datasets and |
| --- | --- | --- | --- | --- | --- | --- | ----------- | -------- | --- | ----------- | --- | ---------------- |
processisillustratedinFigure4.
|     |     |     |     |     |     | eliminate | potential |     | biases | of the proposed |     | method, prior to |
| --- | --- | --- | --- | --- | --- | --------- | --------- | --- | ------ | --------------- | --- | ---------------- |
| 8   |     |     |     |     |     |           |           |     |        |                 |     | VOLUME11,2023    |
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2025.3595894
Gjorgjevikjetal.:BenchmarkingSentenceEncodersinAssociatingIndicatorswithSustainableDevelopmentGoalsandTargets
Fine-tuning dataset creation Validation/test dataset creation
| XML files  |     |     |     | Start fine-tuning dataset  |     |     |     |     |     |     |     |     |     |     |
| ---------- | --- | --- | --- | -------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Start dataset creation
| with text of  |     |     |     |     | creation |     |     |     |     |     |     |     |     |     |
| ------------- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
18 Wikipedia
articles
Dataset={Set1,…,Set5}
Data pre-processing
Variation={Title, Def.}
Task = {FT-SDG, FT-TRG}
|     | Labeled textual  |     |     |     |                       |     |     |     |     |     |     | i = 0 |     |     |
| --- | ---------------- | --- | --- | --- | --------------------- | --- | --- | --- | --- | --- | --- | ----- | --- | --- |
|     | excerpts         |     |     |     | K = [[14, 22][6, 17]] |     |     |     |     |     |     |       |     |     |
i = 0
|     |     |     |     |     |     |     |     |     | Labeled  |     |     | j =0 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | ---- | --- | --- |
indicator
datasets in
|     |     |     |     |     |     | j =0 |     |     | predefined  |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---- | --- | --- | ----------- | --- | --- | --- | --- | --- |
Read indicator text/labels
|     |     |     |     |     |     |     |     |     | format |     |     | for Dataset[i], Variation[j] |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | ---------------------------- | --- | --- |
Stratified sampling for
|     |     |     |     |     | Task[i], K[i, j] |     |     |     |     |     |     |     | No  |     |
| --- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Sample
validation set?
Yes
j++
Validation set for
Validation set stratified
Dataset[i],
|                      |     |     |     |     |        | No  |     |     | Variation[j] |     |     | sampling |     |     |
| -------------------- | --- | --- | --- | --- | ------ | --- | --- | --- | ------------ | --- | --- | -------- | --- | --- |
| Fine-tuning dataset  |     |     |     |     | j > 1? |     |     |     |              |     |     |          |     |     |
for Task[i], K[i, j]
Yes
Test set for
Output remaining
|     |     |     |     |     |     | i++ |     |     | Dataset[i],  |     |     |                      |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | -------------------- | --- | --- |
|     |     |     |     |     |     |     |     |     | Variation[j] |     |     | examples as test set |     |     |
No
i > 1?
j++
Yes
End fine-tuning dataset
No
|     |     |     |     |     | creation |     |     |     |     |     |     | j > 1? |     |     |
| --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | ------ | --- | --- |
Yes
| FIGURE4. | Flowchartofthefine-tuningdatasetcreationprocess. |     |     |     |     |     |     |     |     |     |     |     |     |     |
| -------- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
i++
No
i > 1?
| their use,       | all test | set variations |                 | were | subjected | to  | similarity- |     |     |     |     |     |     |     |
| ---------------- | -------- | -------------- | --------------- | ---- | --------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
| based comparison |          | with           | the fine-tuning |      | examples  |     | in a com-   |     |     |     |     | Yes |     |     |
pletelydifferentvectorspacethantheonesproducedbythe
End dataset creation
| benchmarked |             | sentence | encoders. | All  | fine-tuning |     | examples   |     |     |     |     |     |     |     |
| ----------- | ----------- | -------- | --------- | ---- | ----------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
| from the    | fine-tuning |          | datasets  | were | represented |     | as vectors |     |     |     |     |     |     |     |
usingthebag-of-wordsmethodandTF-IDFweighting.Using FIGURE5. Flowchartofthevalidationandtestdatasetcreationprocess.
| the same | model | fitted | on the | fine-tuning |     | vocabulary, | all de- |     |     |     |     |     |     |     |
| -------- | ----- | ------ | ------ | ----------- | --- | ----------- | ------- | --- | --- | --- | --- | --- | --- | --- |
scriptionsoftestexampleswereembeddedinthesamevector
| space and | compared | with | all | fine-tuning |     | examples | through |     |     |     |     |     |     |     |
| --------- | -------- | ---- | --- | ----------- | --- | -------- | ------- | --- | --- | --- | --- | --- | --- | --- |
cosinesimilarity.Foreachdescriptionofatestindicator,only
|     |     |     |     |     |     |     |     | the concept |     | of transfer | learning), | such models | usually | do  |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ----------- | ---------- | ----------- | ------- | --- |
thehighestcosinesimilarityscorewasretained.Thesummary
|            |          |            |     |        |          |            |     | not output      | ready-to-use |              | sentence    | embeddings | but | require  |
| ---------- | -------- | ---------- | --- | ------ | -------- | ---------- | --- | --------------- | ------------ | ------------ | ----------- | ---------- | --- | -------- |
| statistics | of those | similarity |     | scores | was then | calculated | by  |                 |              |              |             |            |     |          |
|            |          |            |     |        |          |            |     | domain-specific |              | fine-tuning. | Pre-trained | sentence   |     | encoders |
testsettoseeiftherearetestexamplesthatareverysimilar
|                    |     |          |     |             |     |           |          | (e.g., | [58]–[60]) | usually | fine-tune | such language |     | models |
| ------------------ | --- | -------- | --- | ----------- | --- | --------- | -------- | ------ | ---------- | ------- | --------- | ------------- | --- | ------ |
| to the fine-tuning |     | examples |     | (indicating |     | that test | examples |        |            |         |           |               |     |        |
(mainlythroughcontrastiverepresentationlearning)tooutput
| appear in  | our | fine-tuning | sets).    | In     | our future | work,        | we plan |            |            |          |            |                     |            |      |
| ---------- | --- | ----------- | --------- | ------ | ---------- | ------------ | ------- | ---------- | ---------- | -------- | ---------- | ------------------- | ---------- | ---- |
|            |     |             |           |        |            |              |         | meaningful |            | sentence | embeddings | for straightforward |            | sen- |
| to compare | the | datasets    | in larger | number |            | of different | vector  |            |            |          |            |                     |            |      |
|            |     |             |           |        |            |              |         | tence      | comparison | using    | a distance | metric.             | Therefore, | such |
spaces,producedbyotherpre-trainedsentenceencoders.The
encodersallowfortheireasyclusteringorclassificationwith
similarity-basedcomparisonprocessisillustratedinFigure6.
|              |     |              |     |     |                 |     |          | non-parametric |     | algorithms, | which | was the | main reason | for |
| ------------ | --- | ------------ | --- | --- | --------------- | --- | -------- | -------------- | --- | ----------- | ----- | ------- | ----------- | --- |
| The baseline |     | benchmarking |     | of  | the pre-trained |     | general- |                |     |             |       |         |             |     |
ourexperimentationwiththattypeoflanguagemodels.Based
purpose sentence encoders (their pre-training is outside the ontheencoders’averageperformanceonthevalidationtasks,
| scope of | this | article) | was done | on  | the two | validation | tasks |     |     |     |     |     |     |     |
| -------- | ---- | -------- | -------- | --- | ------- | ---------- | ----- | --- | --- | --- | --- | --- | --- | --- |
thosewiththehighestperformancewereselectedforfurther
MC-IND-SDGandMC-IND-TRG.Althoughtheuseoflan- domain-specificfine-tuning.TheprocessisillustratedinFig-
guagemodelsbasedonDL,whichcapturegenerallanguage
ure7.
| characteristics |          | (e.g., [55]–[57]), |         | is  | a common |         | practice to- |     |     |     |     |     |     |     |
| --------------- | -------- | ------------------ | ------- | --- | -------- | ------- | ------------ | --- | --- | --- | --- | --- | --- | --- |
| day when        | it comes | to                 | solving | NLP | tasks    | (mainly | through      |     |     |     |     |     |     |     |
| VOLUME11,2023   |          |                    |         |     |          |         |              |     |     |     |     |     |     | 9   |
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2025.3595894
Gjorgjevikjetal.:BenchmarkingSentenceEncodersinAssociatingIndicatorswithSustainableDevelopmentGoalsandTargets
Similarity-based comparison Sentence encoder baseline benchmarking
XML files
|     |     | Start comparison |     |     |     | Start benchmarking |     |
| --- | --- | ---------------- | --- | --- | --- | ------------------ | --- |
with text of
18 Wikipedia
| articles |     |        |                      |     | L a b e l e d         |     |                             |
| -------- | --- | ------ | -------------------- | --- | --------------------- | --- | --------------------------- |
|          |     | Fine-t | u n i n g  d ataset  |     |                       |     | D a t a s e t = S e t 1     |
|          |     |        |                      |     | in d i c a t o r      |     | V ar i a t i o n = T i t le |
|          |     |        | c r e a t io n       |     | da t a s e t s   in   |     |                             |
predefined
|     |     |                          |     |     | format | Create validation set from  |     |
| --- | --- | ------------------------ | --- | --- | ------ | --------------------------- | --- |
|     |     | TF-IDF model fitting on  |     |     |        | specified Dataset/Variation |     |
all fine-tuning examples
Embed validation dataset
Dataset={Set1,…,Set5}
Variation={Title, Def.}
Task={MC-IND-SDG,
|     |     |     | i = 0 |     |     |     | MC-IND-TRG} |
| --- | --- | --- | ----- | --- | --- | --- | ----------- |
K = [[14 + n(Sl)*6,
|     | Test set for  |     |      |     |     | 14 + n(Sl)*17, 22 + n(Sl)*6,    |     |
| --- | ------------- | --- | ---- | --- | --- | ------------------------------- | --- |
|     |               |     | j =0 |     |     | 22 + n(Sl)*17][6, 17]], k={1,3} |     |
Dataset[i],
Variation[j]
Pre-trained
|     |     | Get indicator Dataset[i],  |     |     | sentence  |     | i = 0 |
| --- | --- | -------------------------- | --- | --- | --------- | --- | ----- |
|     |     | Variation[j]               |     |     | encoder   |     |       |
architecture
|     |     |                    |     |     | and        |     | j = 0 |
| --- | --- | ------------------ | --- | --- | ---------- | --- | ----- |
|     |     | Embed with TF-IDF  |     |     | parameters |     |       |
model
p = 0
Cosine similarity
Get fine-tuning dataset(s)
calculation
for Task[i], K[i, j]
Statistics over max
|     |     | similarity by test example |     |     |     | Embed fine-tuning dataset |     |
| --- | --- | -------------------------- | --- | --- | --- | ------------------------- | --- |
Statistics for
| Dataset[i],  |     |     | j++ |     |     |     |     |
| ------------ | --- | --- | --- | --- | --- | --- | --- |
Classify validation set with
Variation[j]
k[p] nearest neighbors
No
j > 1?
|     |     | Yes |     |     |     |     | p++ |
| --- | --- | --- | --- | --- | --- | --- | --- |
i++
No
p > 1?
|     |     |     | No  |     |     |     | Yes |
| --- | --- | --- | --- | --- | --- | --- | --- |
i > 1?
Accuracy for
|     |     |     |     |     | Task[i], K[i, j],  |     | j++ |
| --- | --- | --- | --- | --- | ------------------ | --- | --- |
Yes
k[p]
|     |     | End comparison |     |     |     | (i = 0 & j > 3) ||  | No  |
| --- | --- | -------------- | --- | --- | --- | ------------------- | --- |
(i = 1 & j > 1) ?
Yes
FIGURE6. Flowchartofthesimilarity-basedcomparisonoffine-tuning
andtestexamples.Thefine-tuningdatasetcreationisshowninFigure4. i++
No
i > 1?
C. SENTENCEENCODERFINE-TUNING,VALIDATION,AND
Yes
TESTING
Calculate average
Thegoalofthefine-tuningprocesswastheadjustmentofthe Average  validation accuracy
| pre-trainedsentenceencoderparameterstoachieveimproved |     |     |     |     | validation  |     |     |
| ----------------------------------------------------- | --- | --- | --- | --- | ----------- | --- | --- |
accuracy
| resultsonthemainandauxiliarytesttasksovertheirbaseline |     |     |     |     | for  |     |     |
| ------------------------------------------------------ | --- | --- | --- | --- | ---- | --- | --- |
End benchmarking
| results.  | In each domain-specific | fine-tuning       | task (either | FT- | encoder                                               |     |     |
| --------- | ----------------------- | ----------------- | ------------ | --- | ----------------------------------------------------- | --- | --- |
| SDG or    | FT-TRG), N represents   | the number        | of classes   | to  |                                                       |     |     |
|           |                         |                   |              |     | FIGURE7. Flowchartofasentenceencoderbenchmarkingonall |     |     |
| which the | examples were           | classified, while | K represents | the |                                                       |     |     |
validationtasks/configurations.Forvalidationsetcreation,seeFigure5.
approximatenumberofexamplesbyclassinthefine-tuning
| set (several | different values | were evaluated | in the | experi- |     |     |     |
| ------------ | ---------------- | -------------- | ------ | ------- | --- | --- | --- |
mentsdescribedinSectionIV-A1).Eachfine-tuningtaskwas sentenceencoderparameters,J(θ).Eachfine-tuningexample
(t(i),y(i))
representedthroughitsfine-tuningsetofmexamples,D FT , was a pair ∈ D FT , i = {1,...,m} of short text
its distance metric measuring the distance between the em- describinganSDGortarget,labeledwitheithertheSDGor
beddingsoftwoexamplesinthetargetrepresentationspace, the target it describes, depending on the task. The text t(i)
d(z(i),z(j)), hadaninitialrepresentationx(i)belongingtoarepresentation
|     | and its objective | function used | to optimize | the |     |     |     |
| --- | ----------------- | ------------- | ----------- | --- | --- | --- | --- |
10 VOLUME11,2023
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2025.3595894
Gjorgjevikjetal.:BenchmarkingSentenceEncodersinAssociatingIndicatorswithSustainableDevelopmentGoalsandTargets
spaceRs,whilethesentenceencoderimplementedafunction p(y(i),yˆ(i)).Withineachvalidationandtesttask(MC-IND-
| Rs  | Rv  |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
f : → parameterized by a parameter vector θ with SDG, MC-IND-TRG, ML-IND-SDG, and ML-SDG-SDG)
the purpose of projecting the initial representation x(i) to a different experimental settings were evaluated, differing in
newandmoredenserepresentationz(i) =f(x(i)),belonging the approximate number of training examples by class (ap-
to a representation space Rv, where usually v ≪ s. The proximateK),asdescribedinSectionIV-B.Thefine-tuning
learningprocessoptimizedtheparametervectorθsothatthe processofasinglesentenceencoderisillustratedinFigure8.
representationz(i)wasusefulforthevalidationandtesttasks.
| In this article | we use | a vector | notation | for | the label, | y(i), to |     |     |     |     |     |     |     |
| --------------- | ------ | -------- | -------- | --- | ---------- | -------- | --- | --- | --- | --- | --- | --- | --- |
64
| representits1-of-Nencoding. |     |     |     |     |     |     |     |       | (cid:88) |       | d(z(a),z(p)) |     |     |
| --------------------------- | --- | --- | --- | --- | --- | --- | --- | ----- | -------- | ----- | ------------ | --- | --- |
|                             |     |     |     |     |     |     |     | J(θ)= |          | [ max |              |     | (1) |
p=1..64
| We used | the triplet | network | architecture, |     | where | triplets |     |     | a=1 |     |     |     |     |
| ------- | ----------- | ------- | ------------- | --- | ----- | -------- | --- | --- | --- | --- | --- | --- | --- |
a̸=p
((t(a),y(a)),(t(p),y(p)),(t(n),y(n)))wereformedfromfine- y(a)=y(p)
tuning examples and used to optimize the parameter vector − min d(z(a),z(n))+α]
+
| θ.Eachtriplethadananchorexamplea,apositiveexample |     |     |     |     |     |     |     |     | n=1..64 |     |     |     |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- |
a̸=n
| p (p ̸= | a) that was | related | to the anchor |     | in some | human- |     |     |     |     |     |     |     |
| ------- | ----------- | ------- | ------------- | --- | ------- | ------ | --- | --- | --- | --- | --- | --- | --- |
y(a)̸=y(n)
| definedway(sharingthesameclassinthiscase,y(a) |     |     |     |     |     | =y(p)), |     |     |     |     |     |     |     |
| --------------------------------------------- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
and a negative example n (n ̸= a) that was unrelated to the z(a)z(p)
|     |     |     |     |     |     |     | d(z(a),z(p))=1− |     |     |     | ,d(z(a),z(p))∈[0,2] |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --- | --- | ------------------- | --- | --- |
(2)
anchor(havingadifferentclassthantheanchorinthiscase, ||z(a)||||z(p)||
y(a) ̸=y(n)).Therefore,theobjectiveofthelearningprocess
| was to | bring the projected |     | embeddings | of  | the anchor | and |     |     |     |     |     |     |     |
| ------ | ------------------- | --- | ---------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
D. POST-HOCANALYSIS
thepositiveexamplecloserinthetargetrepresentationspace
Rv for at least a margin α than the anchor and the negative Tobetterunderstandthefactorsthatinfluencedtheevaluation
example, i.e., (d(z(a), z(n)) − d(z(a), z(p))) > α. The results,wefirsttriedtoidentifyasmanyofthemaspossible
andthenanalyzedtheirinfluenceontheresultsusingmethods
threeembeddingswerecombinedinthetripletlossfunction
[61],withthepurposeofincreasingthedistancebetweenthe from xAI. These included the various decisions we made
|     |     |     |     |     |     |     | during the | fine-tuning |     | and testing | processes. | The | idea was |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ----------- | --- | ----------- | ---------- | --- | -------- |
anchorandthenegativeexampleforamarginα,comparedto
thedistancebetweentheanchorandthepositiveexample. simple, i.e., all factors of interest were represented as input
Inthetripletnetworkarchitecture,thesetofallvalidtriplets features to a meta-model, i.e., linear regression, which was
|     |     |     |     |     |     |     | then trained | to  | predict | the performance |     | by SDG | that was |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------- | --------------- | --- | ------ | -------- |
istask-dependent.Althoughthenumberofvalidtripletsmay
be very large, not all triplets contribute to parameter im- actually achieved by our fine-tuned sentence encoders and
|            |                  |        |               |       |       |             | classifier        | on the | test | sets. The | training  | set on     | which the |
| ---------- | ---------------- | ------ | ------------- | ----- | ----- | ----------- | ----------------- | ------ | ---- | --------- | --------- | ---------- | --------- |
| provements | during training  |        | [61]. Instead | of    | using | all valid   |                   |        |      |           |           |            |           |
|            |                  |        |               |       |       |             | linear regression |        | was  | trained   | consisted | of all the | different |
| triplets,  | the hard triplet | mining | strategy      | forms | a     | triplet for |                   |        |      |           |           |            |           |
ananchorbysearchingforitsmostdistantpositiveexample fine-tuningandtestingconfigurations,describedthroughthe
|     |     |     |     |     |     |     | mentioned | factors. | The | contribution |     | of each feature | to the |
| --- | --- | --- | --- | --- | --- | --- | --------- | -------- | --- | ------------ | --- | --------------- | ------ |
anditsclosestnegativeexample,butthesehardtripletsmay
sometimesleadtofastconvergencetolocalminima[61].In predictionmadebythelinearregressionmodelforeachindi-
vidualtrainingexamplewasthencalculatedwiththeShapley
| this work, | we used the | batch | hard triplet |     | loss [62], | which |          |              |     |        |        |           |           |
| ---------- | ----------- | ----- | ------------ | --- | ---------- | ----- | -------- | ------------ | --- | ------ | ------ | --------- | --------- |
|            |             |       |              |     |            |       | Additive | Explanations |     | (SHAP) | method | [63]. The | method is |
minesthehardestpositiveandhardestnegativeexamplesina
mini-batchforeachanchorbasedonapre-specifiedmarginα, basedonconceptsfromcoalitiongamestheoryandexplains
featureattributionstothepredictionsmadebyanMLmodel
asgiveninEq.1.Foraspecificanchora,thehardestpositive
examplepinamini-batch(p ̸= a)wastheonebelongingto for individual examples [64]. When calculating the SHAP
(y(a) = y(p)) values for each example, we wanted the algorithm to take
| the same | class as the | anchor |     |     | and having | the |     |     |     |     |     |     |     |
| -------- | ------------ | ------ | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
intoconsiderationthefeaturecorrelationandspreadthecredit
| largest distance | from | the anchor | (d(z(a),z(p))) |     | in  | the target |     |     |     |     |     |     |     |
| ---------------- | ---- | ---------- | -------------- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
vectorspace.Thehardestnegativeexampleninamini-batch betweencorrelatedfeatures,asexplainedin[64].Theprocess
isillustratedinFigure9.
| (n ̸= a) | was the one    | belonging  | to a | different | class    | than the |     |     |     |     |     |     |     |
| -------- | -------------- | ---------- | ---- | --------- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- |
| anchor   | (y(a) ̸= y(n)) | and having | the  | smallest  | distance | from     |     |     |     |     |     |     |     |
theanchor(d(z(a),z(n)))inthetargetvectorspace.Theloss IV. EXPERIMENTALDESIGN
functionincludedonlythoseanchorsforwhichthedifference A. DATASETCREATIONPROCESS,PRELIMINARYANALYSIS
betweenthetwodistancesexceededthepredefinedmarginα, ANDENCODERBASELINEBENCHMARKING
i.e.,resultedinapositivevalue.Thedistancemetricofchoice 1) Fine-TuningDatasetCreationProcess
was the angular distance, defined in Eq. 2 and based on the The datasets used to fine-tune the sentence encoders were
well-knowncosinesimilarity. sampled from a custom-created dataset consisting of 1,815
Duringvalidationandtesting,weusedthefine-tunedsen- text excerpts of similar length, extracted from 18 English-
tenceencodersasfeatureextractorsandcombinedthemwith language Wikipedia articles devoted to the SDGs. Each ex-
aclassificationalgorithm.Thevalidationandtesttaskswere cerptwaslabeledwiththeSDGandtarget(whereapplicable)
represented through a training set D , a validation D it described, based on the article section it was extracted
|     |     |     |     | TR  |     | VL  |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
or test D set, accordingly, a distance metric in the target from. Those articles were (1) the article titled “Sustainable
TS
d(z(i),z(j)),
representation space and a performance metric Development Goals”, providing a brief description of all
| VOLUME11,2023 |     |     |     |     |     |     |     |     |     |     |     |     | 11  |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2025.3595894
Gjorgjevikjetal.:BenchmarkingSentenceEncodersinAssociatingIndicatorswithSustainableDevelopmentGoalsandTargets
Sentence encoder domain-specific fine-tuning Post-hoc analysis
XML files
with text of Start encoder fine- Start post-hoc analysis Fine-tuning
18 Wikipedia tuning datasets
articles
Factor value (input features)
Task = FT-SDG,
K = 14, Iterations = 20 calculation for a test set Results by
fine-tuning /
test
Create fine-tuning dataset Training dataset configuration
for specified Task and K and test set
Linear regression (meta-
i = 0 model) fitting
Stratified sampling of SHAP value calculation by
examples in a mini-batch factor and example
SHAP
analysis and
visualizations
Embed mini-batch SHAP value analysis
examples
Last fine-
tuned
checkpoint
of a sentence Find valid triplets End post-hoc analysis
encoder
Calculate loss J(θ), adjust FIGURE9. Flowchartofthepost-hocanalysis.
encoder parameters θ
No
i % 5 = 0? oftheprocess,seeFigure4.
Yes Step1:TextExtraction.Aselectedsetofarticlesections
wasextractedfromtheXMLfilesandcleanedfromHTML
Calculate average
and Wikipedia-specific XML markup. From the general ar-
validation accuracy
ticle, the sections devoted to each SDG were extracted and
Average labeledwiththeSDGtheyreferredto.FromtheSDG-specific
i++
validation
articles,theleadsectionandthesectionswithtitlescontaining
accuracy for
a checkpoint No aselectedsetofphraseswereextracted(seetheGitHubrepos-
i > Iterations?
itory)andlabeledwiththeSDGthearticlereferredto.From
Yes
thesectiondevotedtothetargetsofanSDG,eachsubsection
Select checkpoint with devoted to a specific target was extracted and labeled with
highest average validation
accuracy boththeSDGandthetargetitreferredto.
Selected
fine-tuned Step2:TextCleaning.Thetextextractedintheprevious
checkpoint
phasewassubjectedtocleaningconsistingoffourstepsillus-
End encoder fine-tuning
tratedinFigure10.Thepurposeoftheindicatortitleremoval
step was to find all mentions of SDG indicator titles in the
FIGURE8. Flowchartofthefine-tuningprocessofasentenceencoderon
thetaskFT-SDG,K=14.Theprocessisthesameforallfine-tuningtasks. textandremovethem,asthesetitleswerepartofthetestset.
Thefine-tuningdatasetcreationisshowninFigure4.Thecalculationof It was done by searching for common patterns, determined
theaveragevalidationaccuracyfollowstheprocessshowninFigure7.
with prior text analysis, and their replacement with general
phrases,suchas“indicator”,“theindicator”andsimilar.The
secondstepremovedmentionsofSDG,target,andindicator
17 SDGs, and (2) the articles dedicated to each of the 17 labels from the text. Each mention of an SDG, a target, or
SDGs,thefirstcalled“general”articleandthesecond“SDG- an indicator label was replaced with a generic phrase, such
specific” articles in the sections that follow. For the exact as“thegoal”,“thetarget”,“theindicator”,ortheirvariation,
article URLs and revision IDs see Appendix C. The text depending on the sentence context. The general cleaning
of the 18 Wikipedia articles, downloaded in XML format, removedgeneralpatternssuchaslistitemlettersornumbers
was subjected to custom pre-processing consisting of four from the text. The common phrase removal step removed a
steps, i.e., (1) text extraction, (2) text cleaning, (3) sentence smallsetofverycommonphrasesfromthetext,whichdidnot
extraction, and (4) text excerpt extraction, as illustrated in appearasseparatesentencestobefilteredbythesentencefil-
Figure 10. The pre-processing was followed by a fifth step, teringinthenextphase.Theycouldhavenegativelyaffected
i.e.,aprocessofstratifiedsamplingofthefine-tuningdatasets the learning process by making the excerpts that contained
fromthe1,815similar-lengthtextexcerpts.Foranillustration themappearsimilar,evenwhenthiswasnotthecase.
12 VOLUME11,2023
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2025.3595894
Gjorgjevikjetal.:BenchmarkingSentenceEncodersinAssociatingIndicatorswithSustainableDevelopmentGoalsandTargets
Start fine-tuning dataset
creation
| Text extraction |     |     | Text cleaning |     |     |     |     |     |     |     | Sentence extraction |     |     |     |
| --------------- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | --- |
XML markup cleaning SDG, target, indicator  Sentence segmentation
|     |     |     |     | Indicator title removal |     |     | label replacement |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ----------------------- | --- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- |
Text extraction from
|     |     |     |     | General cleaning |     |     | Common phrase removal |     |     |     |     | Sentence filtering |     |     |
| --- | --- | --- | --- | ---------------- | --- | --- | --------------------- | --- | --- | --- | --- | ------------------ | --- | --- |
selected sections
Text excerpt extraction
XML files
with text of 18
|     | Wikipedia  |     |     |                        |     |     |                        |     |     |     | End fine-tuning dataset  |          |     |     |
| --- | ---------- | --- | --- | ---------------------- | --- | --- | ---------------------- | --- | --- | --- | ------------------------ | -------- | --- | --- |
|     |            |     |     | Sentence concatenation |     |     | Length-based filtering |     |     |     |                          |          |     |     |
|     | articles   |     |     |                        |     |     |                        |     |     |     |                          | creation |     |     |
Dataset in
CSV file
FIGURE10. Flowchartofthepre-processingof18Wikipediaarticlestoextractcandidateexamplesforfine-tuningdatasets.
Step 3: Sentence Extraction. In the sentence extraction was labeled with the SDG and target labels of the section it
phase,allparagraphsineachsectionweredividedintotheir wasextractedfrom(seeTextExtractionphase).
| constituting  | sentences. | The purpose    |     | was to            | remove | com- |                |               |             |          |     |              |     |           |
| ------------- | ---------- | -------------- | --- | ----------------- | ------ | ---- | -------------- | ------------- | ----------- | -------- | --- | ------------ | --- | --------- |
|               |            |                |     |                   |        |      | Step           | 5: Stratified |             | Sampling | of  | Fine-Tuning  |     | Datasets. |
| mon sentences | that did   | not contribute |     | to distinguishing |        | the  |                |               |             |          |     |              |     |           |
|               |            |                |     |                   |        |      | Four different |               | fine-tuning | datasets |     | were sampled |     | from the  |
SDGortargetdescriptionsfromeachother.Thesesentences
extracteddatasetusingstratifiedsamplingstrategies.Ineach
| shared common | terminology, |     | therefore, | a   | simple | bag-of- |     |     |     |     |     |     |     |     |
| ------------- | ------------ | --- | ---------- | --- | ------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
fine-tuningset,basedonthetask(FT-SDGorFT-TRG),the
wordsmethodwithTF-IDFweighingwasusedtorepresent
|     |     |     |     |     |     |     | number | of classes | N corresponded |     |     | to either | the | number of |
| --- | --- | --- | --- | --- | --- | --- | ------ | ---------- | -------------- | --- | --- | --------- | --- | --------- |
eachsentenceinacommonvectorspace.Theminimumdoc-
|     |     |     |     |     |     |     | SDGs (N=17) |     | or the number |     | of targets | (N=169). |     | We exper- |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------------- | --- | ---------- | -------- | --- | --------- |
ument(sentenceinthisparticularcase)frequencywassetto
|     |     |     |     |     |     |     | imented | with the | number | of  | examples | by  | class | K, to see |
| --- | --- | --- | --- | --- | --- | --- | ------- | -------- | ------ | --- | -------- | --- | ----- | --------- |
min_df=10documents.Onlysinglewordswereweightedby
|     |     |     |     |     |     |     | if a larger | number | of  | examples | by  | class in | the | fine-tuning |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------ | --- | -------- | --- | -------- | --- | ----------- |
themethodafterremovingthestopwords.Thevectorswere
|                |           |               |     |         |            |     | set improved | the          | performance |      | or, on     | the | contrary,    | made it |
| -------------- | --------- | ------------- | --- | ------- | ---------- | --- | ------------ | ------------ | ----------- | ---- | ---------- | --- | ------------ | ------- |
| then clustered | using the | Density-Based |     | Spatial | Clustering |     |              |              |             |      |            |     |              |         |
|                |           |               |     |         |            |     | worse. We    | hypothesized |             | that | in FT-SDG, |     | the examples | ex-     |
ofApplicationswithNoise(DBSCAN)algorithm[65],with
|         |                     |     |             |     |                |     | tracted from | the | more | general | article | sections, | e.g., | the sec- |
| ------- | ------------------- | --- | ----------- | --- | -------------- | --- | ------------ | --- | ---- | ------- | ------- | --------- | ----- | -------- |
| ϵ = 0.3 | and min_samples=10, |     | to identify |     | large clusters | of  |              |     |      |         |         |           |       |          |
tionsofthegeneralSDGarticleorleadsectionoftheSDG-
similarsentences.Thesentencesthatwereretainedforfurther
|            |             |              |             |                |               |          | specific   | articles, | would         | actually    | result   | in      | a less  | noisy fine- |
| ---------- | ----------- | ------------ | ----------- | -------------- | ------------- | -------- | ---------- | --------- | ------------- | ----------- | -------- | ------- | ------- | ----------- |
| processing | were those  | labeled      | as outliers | by             | the algorithm |          |            |           |               |             |          |         |         |             |
|            |             |              |             |                |               |          | tuning set | and,      | consequently, |             | sentence | encoder |         | that would  |
| (more than | 96% of the  | total number |             | of sentences). |               | Cosine   |            |           |               |             |          |         |         |             |
|            |             |              |             |                |               |          | perform    | better    | on the        | test tasks. | That     | also    | applied | to FT-      |
| similarity | was used as | a similarity | metric,     |                | and the       | cluster- |            |           |               |             |          |         |         |             |
TRG,wherewehypothesizedagainthatextractingexamples
inghyperparameterswereselectedexperimentally.Sincethe
|     |     |     |     |     |     |     | from the | first | sentences/paragraphs |     |     | describing |     | each target |
| --- | --- | --- | --- | --- | --- | --- | -------- | ----- | -------------------- | --- | --- | ---------- | --- | ----------- |
distributionofthenumberofretainedsentencesbySDGand
|            |                    |     |                  |     |            |     | was better. | Therefore, |     | in the   | two FT-SDG |         | datasets, | K was     |
| ---------- | ------------------ | --- | ---------------- | --- | ---------- | --- | ----------- | ---------- | --- | -------- | ---------- | ------- | --------- | --------- |
| target was | highly imbalanced, |     | with significant |     | variations | in  |             |            |     |          |            |         |           |           |
|            |                    |     |                  |     |            |     | selected    | according  | to  | the mean | and        | maximum |           | number of |
theirlength,combiningthemintotextexcerptsofcomparable
|     |     |     |     |     |     |     | excerpts | by SDG, | extracted | from | the | general | article | and the |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------- | --------- | ---- | --- | ------- | ------- | ------- |
lengthwasneeded.Forclarity,Algorithm1summarizesthe
SDG-specificarticleleadsections,i.e.,K=14inthefirstand
sentenceextractionprocessinasimplifiedform(lessrelevant
|     |     |     |     |     |     |     | K=22 in | the second. |     | The first | fine-tuning |     | set (K=14) | was |
| --- | --- | --- | --- | --- | --- | --- | ------- | ----------- | --- | --------- | ----------- | --- | ---------- | --- |
configurationparametersareomitted).
|     |     |     |     |     |     |     | composed | mainly | of textual |     | excerpts | extracted | from | (1) the |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------ | ---------- | --- | -------- | --------- | ---- | ------- |
Step 4: Text Excerpt Extraction. After the sentence ex- generalarticle,(2)theleadsection,and(3)the"background"
traction phase, the sentences were concatenated into short sectionoftheSDG-specificarticles.Thesecondfine-tuning
excerpts. The exact order in which the sentences appeared set(K=22)extendedthefirstwithexcerptsfromtheremain-
intheoriginaltextandtheparagraphbreakswerepreserved ing sections of the SDG-specific article. In FT-TRG, K was
duringconcatenation,whiletryingtoachieveanapproximate selected according to the mean and maximum number of
value of 30(±10) words per excerpt. Those excerpts with examples extracted by target, i.e., K=6 in the first task and
less than 5 and more than 55 words were filtered out. In K=17inthesecond.Theexampleswerethoseextractedfrom
such a way, sufficient context was captured in the excerpts the section that described the targets in the SDG-specific
while keeping their number of words similar. Each excerpt articles. The distribution of fine-tuning examples by SDG
| VOLUME11,2023 |     |     |     |     |     |     |     |     |     |     |     |     |     | 13  |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2025.3595894
Gjorgjevikjetal.:BenchmarkingSentenceEncodersinAssociatingIndicatorswithSustainableDevelopmentGoalsandTargets
Algorithm1SimplifiedversionoftheSentenceExtractionalgorithm(lessrelevantconfigurationparametersareomitted).The
implementationusestheScikit-Learnlibrary(abbreviatedassklearn)andPythonbuilt-inregularexpressionlibrary(re).The
variablesdgreferstotheSDGnumberdescribedintheparagraph,trgtothetargetnumber(ifany),secreferstothetitleofthe
sectionfromwhichtheparagraphwasextracted,andpartotheparagraphtext.Fortheexactimplementation,seetheGitHub
repository[13].
1: all_sentences←[]/*allsentencesindataset*/
2: paragraph_sentences←[]/*sentencesbyparagraph*/
3: filtered_paragraphs←[]/*OUTPUT:paragraphswithcommonsentencesfilteredout*/
4: paragraphs←[(sdg(1),trg(1),sec(1),par(1)),...,(sdg(k),trg(k),sec(k),par(k))],sdg∈{1,..,17},trg∈{1,..,169}
5: vectorizer←sklearn.TfidfVectorizer(ngram_range=(1,1),min_df=10,stop_words=’english’)
6: dbscan←sklearn.DBSCAN(eps=0.3,min_samples=10,metric=’cosine’)
7: for(sdg,trg,sect,paragraph)inparagraphsdo
8: sentences←re.split(r’.|?|!|;;’,paragraph)/*splitparagraphtosentences*/
9: all_sentences.add(sentences)
10: paragraph_sentences.add((sdg,trg,sect,paragraph,sentences))
11: tf_idf_vectors←vectorizer.fit_transform(all_sentences).toarray()/*vectorizesentences*/
12: clusters←dbscan.fit(tf_idf_vectors)/*clustersentencevectors*/
13: start_index←0
14: for(sdg,trg,sect,paragraph,sentences)inparagraph_sentencesdo
15: retained_sentences←[]
16: span←len(sentences)
17: end_index←start_index+span
18: current_clusters=clusters[start_index:end_index]/*getlabelsforsentencesincurrentparagraph*/
19: for(sentence,cluster)inzip(sentences,current_clusters)do
/*DBSCANoutliersarelabeledwith-1*/
20: ifcluster==-1then
21: retained_sentences.add(sentence)/*ifthesentenceisanoutlier,retainit*/
22: start_index←end_index
23: filtered_paragraphs.add((sdg,trg,sect,paragraph,retained_sentences))
andtargetineachofthefourfine-tuningsetsisillustratedin
Figure11andFigure12,whilethedistributionofexamplesby   
    
WikipediaarticlesectionandSDGinthetwoFT-SDGfine-
 7 H [ W  H [ F H U S W V  O D E H O H G  R Q O \  Z L W K  6 ' *
tuningsetsisillustratedinFigure13andFigure14.         ) L Q H  W X Q L Q J  V H W   .       
 ) L Q H  W X Q L Q J  V H W   .     
   
2) ValidationandTestDatasetCreationProcess
Duetothelackofready-to-usedatasetsforvalidation/testing        
  
oftheproposedframework,wehadtoadjustseveralexisting
indicatorframeworksfortheiruseinourmainandauxiliary   
validation/testtasks.Thevalidationsetconsistedofindicators        
sampled from the Global indicator framework of the 2030
Agenda, labeled with SDGs and targets. Five indicator test
sets were created from (1) the Global indicator framework     
of the 2030 Agenda (validation/test dataset 1), (2) the EU-
ROSTAT’sEUSDGindicators(testdataset2),(3)theWorld
Bank’s World Development Indicators (test dataset 3, also     
abbreviatedas"WDISDG"indicatorsintheremainingtext),
(4)indicatorspresentedintheEuropeanHandbookforSDG     
VLRs (test dataset 4, also abbreviated as "EU Local SDG"
   
indicators),and(5)theinitialsetofEuropeanregionalSDG
indicators (test dataset 5, also abbreviated as "EU Regional FIGURE11. DistributionbySDGofallextractedexcerptslabeledwith
SDG"indicators).WhiletheindicatorsfromtheGlobalindi- SDGlabelonlyandtheexamplessampledforeachofthetwoFT-SDG
fine-tuningsets.
catorframeworkofthe2030Agenda(validation/testdataset
1) and EU Regional SDG indicators were represented only
throughtheirtitles,twovariationswerecreatedfromtheother
14 VOLUME11,2023
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2025.3595894
Gjorgjevikjetal.:BenchmarkingSentenceEncodersinAssociatingIndicatorswithSustainableDevelopmentGoalsandTargets
|     |        D    E  F                                               |     |     |     |     |     |    |     |     |
| --- | -------------------------------------------------------------------------------- | --- | --- | --- | --- | --- | ---- | --- | --- |
|     |    D    E                              D   E        |     |     |     |     |     |      |     |     |
                                          
|             |                  |  D  |     |     |     |     |     |     |     |
| -------------------- | ------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
         7  H  [  W    H  [  F  H  U  S  W  V    O   D    E      H    O   E  H    G F     Z  L  W  K    W  D  U  J  H  W  *  H  Q  H  U  D  O
|          |     |           |     |     |     |     |     |     |     |
| -------------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- |
      E         )  L  Q  H    W  X  Q  L  Q  J    V  H  W      .                                /  H  D  G      V  H  F  W  L  R  Q
           D  )  L  Q  H    W  X  Q  L  Q  J    V  H  W      .                          %  D  F  N  J  U  R  X  Q  G
                          D  &  K  D  O  O  H  Q  J  H  V
|        E |    |            E |     |     |     |    |     |     |     |
| ----------- | ---- | ----------------- | --- | --- | --- | ---- | --- | --- | --- |
       D            F    2  U J  D  Q  L  ]  D  W  L  R  Q  V
|                |          |                       |      |      |     |    |     |     |     |
| -------------------- | ---------- | --------------------------- | ---- | ---- | --- | ---- | --- | --- | --- |
|                   |            |                        |      |    |     |      |     |     |    |
|                  |           |                       |      |      |     |     |     |     |     |
|        F         |            |                       |      |      |     |      |     |     |     |
|      E             |           |                         |      |      |     |      |    |     |     |
|          D       |            |              D        |      |      |     |      |     |     |     |
|                  |           |          E              |      |      |     |      |    |     |     |
|                   |            |        F                 |      |      |     |      |     |     |     |
|                  |           |                       |      |      |     |      |    |     |     |
|                 |            |                       |    |      |     |      |     |     |    |
|    F               |            |     D                    |      |      |     |      |     |     |     |
|    E               |            |     E                    |      |      |     |      |     |     |     |
|    D            |            |                     |      |      |     |      |     |     |     |
|                   |            |                         |      |      |     |      |     |     |     |
|                  |            |                        |      |      |     |      |     |     |     |
|                 |            |                      |      |      |     |      |     |     |     |
|                   |            |                         |      |    |     |      |     |     |    |
|        G          |            |            D           |      |      |     |      |     |     |     |
|          F       |            |        F    E           |      |      |     |      |     |     |     |
|      E   D        |            |                        |      |      |     |      |     |     |     |
|                  |            |                       |      |      |     |      |     |     |     |
|                 |            |                      |      |      |     |      |     |     |     |
|                  |            |                      |      |      |     |      |     |     |     |
|                 |            |                        |      |    |     |      |     |     |    |
|                 |            |                     |      |      |     |      |     |     |     |
|             F |            |            D           |      |      |     |      |     |     |     |
|    E    D        |            |                F  E |      |      |     |      |     |     |     |
|                |        |                       |      |      |     |      |     |     |     |
                                          
|     |                         E     D               |     |     |     |     |     |     |     |     |
| --- | ----------------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
                                                                              
|     |     |     |           |                                                  |     |    |    |     |     |
| --- | --- | --- | --------- | ------------------------------------------------ | --- | --- | --- | --- | --- |
|     |     |     | FIGURE14. | DistributionbySDGandWikipediaarticlesectionofthe |     |     |     |     |     |
FIGURE12. Distributionbytargetofallextractedexcerptslabeledwith
targetlabelandexamplesinthetwoFT-TRGfine-tuningsets.Theoverlap examplesintheFT-SDGfine-tuningsetN=17,K=22.
ofthetwolinesindicatesthatthesecondfine-tuningset(K=17)includes
allextractedexcerpts.
|     |     |     | main | or auxiliary | test | tasks. | A custom | sixth dataset | for the |
| --- | --- | --- | ---- | ------------ | ---- | ------ | -------- | ------------- | ------- |
   ML-SDG-SDG task was created as well. For an illustration
|     |      |     |     |     |     |     |     |     |     |
| --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
oftheprocess,seeFigure5.
|  * H Q H U D O               |    |     |     |     |     |     |     |     |     |
| ---------------------------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
|  /  H  D G  V H F W L R Q |      |    |     |     |     |     |     |     |     |
 % D F N J U R X Q G Validation/Test Dataset 1: Global Indicator Frame-
  
 & K D O O H Q J H V
 2 U J D Q L ] D W L R Q V   work of the 2030 Agenda. The validation and test set 1
weresampledfromtheglobalindicatorsofthe2030Agenda.
|    |    |    |     |            |          |      |     |                  |        |
| ---- | --- | --- | --- | ---------- | -------- | ---- | --- | ---------------- | ------ |
|      |     |     | The | refinement | in March | 2021 | was | used, consisting | of 247 |
 
|     |     |     | indicators, | including |     | the repeating | ones. | Each | indicator was |
| --- | --- | --- | ----------- | --------- | --- | ------------- | ----- | ---- | ------------- |
  represented by its title and labeled with the SDG and target
|    |     |    |     |     |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
itmonitored.Therepeatingindicatorswerelabeledwiththe
|      |     |     | multiple | SDGs           | and | targets            | they monitored. |                     | In the multi- |
| ---- | --- | --- | -------- | -------------- | --- | ------------------ | --------------- | ------------------- | ------------- |
|      |     |     | class    | classification |     | validation/testing |                 | tasks, a prediction | that          |
|    |     |    |          |                |     |                    |                 |                     |               |
matchedanyofthosemultiplelabelswasconsideredacorrect
|     |     |     | prediction. |     | The validation-test |     | set ratio | was | 25%-75%. To |
| --- | --- | --- | ----------- | --- | ------------------- | --- | --------- | --- | ----------- |
ensurerepresentativesets,twocriteriaweretakenintoconsid-
|    |     |    |     |     |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
erationinthestratifiedsampling,i.e.,(1)theSDGswhichthe
indicatorsmeasure,and(2)theirtitles’wordcount.Basedon
|    |     |    |     |     |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
wordcount,theindicatorsundereachSDGweredividedinto
|     |     |     | threecategories,i.e.,(1)lessthan10words,(2)between10 |     |     |     |     |     |     |
| --- | ----- | --- | ---------------------------------------------------- | --- | --- | --- | --- | --- | --- |
and20words,(3)morethan20words.Thisdivisionworked
FIGURE13. DistributionbySDGandWikipediaarticlesectionofthe
examplesintheFT-SDGfine-tuningsetN=17,K=14. fineformostoftheSDGs,butforseveralSDGs,oneofthe
|     |     |     | categories | contained       |     | only | one example, | so a           | representative |
| --- | --- | --- | ---------- | --------------- | --- | ---- | ------------ | -------------- | -------------- |
|     |     |     | split      | was impossible. |     | For  | those SDGs,  | the indicators | were           |
three test sets. In the first, the indicators were represented divided into two categories, i.e., (1) less than 15 words and
through their titles, and in the second, through the indicator (2)morethan15words.Finally,basedonthiscategorization,
title concatenated as a first sentence with an excerpt from the indicators in the validation and test set were sampled.
the indicator definition containing approximately 30(±10) Forthemulti-labelclassificationofanindicatortoSDGs,the
words.Thecontentandorderofthesentenceswaspreserved. test set examples were sampled in the same way, but only
TheindicatorswerelabeledwithoneSDG,multipleSDGs,or those indicators that belonged to multiple different classes
onetargetdependingontheinformationavailableinthedata (repeatingindicatorsthatmonitoredmultipledifferentSDGs)
source.Consequently,theywereusedonlyintheappropriate wereretained.
| VOLUME11,2023 |     |     |     |     |     |     |     |     | 15  |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2025.3595894
Gjorgjevikjetal.:BenchmarkingSentenceEncodersinAssociatingIndicatorswithSustainableDevelopmentGoalsandTargets
Test Dataset 2: EU SDG Indicator Set. As a second were variations of the Universal Sentence Encoder (USE),
sourceoftestindicators,theEUSDGindicatorsetconsisting i.e.,thestandardmodelbasedontheTransformerarchitecture
of100indicatorswasused(theversionfrom20234).Indicator [66] (USE-TRANSFORMER6, v = 512) and two multilin-
title and definition given in the Monitoring report on the gualmodels[67],ofwhichthefirstbasedonaconvolutional
progress towards the SDGs in an EU context, 2023 edition neural network (USE-MILTILINGUAL-CONVOLUTION7,
[17], were used. The single or multiple SDGs (for multi- v = 512) and the second on the Transformer architecture
purposeindicators),whichtheindicatorsmonitor,wereused (USE-MILTILINGUAL-TRANSFORMER8, v = 512). The
aslabelsinthetesttasks(1)MC-IND-SDGand(2)ML-IND- secondgroupincludedtheSentenceBERT(SBERT)models.
SDG. The original models [58] were based on pre-trained BERT
Test Dataset 3: WDI SDG Indicator Set. WDI are the andRoBERTamodels,fine-tunedthroughSiameseandtriplet
World Bank’s collection of indicators that monitor different network architectures. The sentence encoder based on the
economies on global development. A set of 408 indicators, BERT base architecture (SBERT-BERT-BASE9, v = 768)
classifiedunderanSDGandatarget,wasdownloadedfrom wasusedinthisarticle.OntheSBERTwebsite10,theauthors
theWorldBank’sdataportal5.Theindicatorsavailableunder pointed to a new set of fine-tuned sentence encoders that
license other than CC-BY, as well as those that were not had outperformed original SBERT encoders. Four that have
classifiedunderaspecificSDGandtargetinthedatasource, thehighestperformance,asreportedonthatwebsite11,were
were excluded from the dataset, which resulted in a set of used,(1)fine-tunedMiniLM[68]modelwith6hiddenlayers
368 indicators. The title and long description taken from (SBERT-MINILM-L612, v = 384), (2) fine-tuned MiniLM
the indicator metadata were used as a source of text. The model with 12 hidden layers (SBERT-MINILM-L1213, v =
indicatorswereusedinthetesttasks(1)MC-IND-SDGand 384), (3) fine-tuned DistilRoBERTa [69] model (SBERT-
(2)MC-IND-TRG. DISTILROBERTA14, v = 768), and (4) fine-tuned MP-
TestDataset4:EULocalSDGIndicatorSet.Testindi- NET [70] model (SBERT-MPNET-BASE15, v = 768). The
catorset4consistsof72indicatorspresentedintheEuropean third group of encoders included those based on the Simple
Handbook for SDG Voluntary Local Reviews, 2022 Edition contrastive sentence embedding framework (SimCSE) [59],
[10]. The title and definition of the indicators given in the which fine-tuned pre-trained BERT and RoBERTa models
documentwerepreparedasdescribedatthebeginningofthis throughcontrastivelearninginunsupervisedandsupervised
section.ThemultipleSDGandtargeteachindicatorbelongs settings. BERT base model fine-tuned in both settings was
to were used as labels, therefore, the two variations of this used (SIMCSE-UNSUP-BERT-BASE16 and SIMCSE-SUP-
testsetwereusedin(1)MC-IND-SDG,(2)MC-IND-TRG, BERT-BASE17,v = 768).ThefinalgroupincludedtheSen-
and (3) ML-IND-SDG (only those indicators labeled with tenceT5(ST5)models[60]-fine-tunedT5modelsthrough
multipleSDGs). contrastive learning, optimized for sentence encoding. Two
Test Dataset 5: EU Regional SDG Indicator Set. The models were used (ST5-BASE18 and ST5-LARGE19, v =
testindicatorset5consistsoftheinitial83Europeanregional 768). As new sentence encoders are constantly being pro-
SDGindicatorsoftheprojectREGIONS2030[20].Onlythe posedintheliterature,theselectedsetisnotexhaustiveand
title of the indicators was available in the document, so this willbeexpandedinourfuturework.
indicatorsethadonerepresentationonly.TheSDGandtarget
eachindicatorbelongedtowereusedaslabels,therefore,this B. SENTENCEENCODERFINE-TUNING,VALIDATION,AND
testsetwasusedin(1)MC-IND-SDGand(2)MC-IND-TRG. TESTING
TestDataset6:SDGRelatednessDataset.Forthemulti- At each fine-tuning iteration, the examples in a mini-batch
labelclassificationofanSDGtomultiplerelatedSDGs(ML- ofsize64weresampledusingastratifiedsamplingstrategy,
SDG-SDG), the test set consisted of the titles of SDGs 1 to which ensured a balanced distribution across the 17 SDGs
16,labeledwiththeSDGstheylinkto.Thatinformationwas in the mini-batch, i.e., 3-4 randomly selected examples by
extracted from the section ”Links to other SDGs” of each
SDG-specific Wikipedia article. All mentioned SDGs were 6https://tfhub.dev/google/universal-sentence-encoder-large/5
consideredaslinkedtotheSDGthearticlereferredto.SDG
7https://tfhub.dev/google/universal-sentence-encoder-multilingual/3
8https://tfhub.dev/google/universal-sentence-encoder-multilingual-
17wasnotincluded,asitwasrelatedtoallotherSDGs.
large/3
9https://huggingface.co/sentence-transformers/bert-base-nli-stsb-mean-
3) SentenceEncoderBaselineBenchmarking tokens
Twelvestate-of-the-artsentenceencodersatthetimeofwrit-
10https://www.sbert.net/
11https://www.sbert.net/docs/pretrained_models.html
ing, belonging to four diverse categories, were compared
12https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2
on the validation tasks, of which the ones with the highest 13https://huggingface.co/sentence-transformers/all-MiniLM-L12-v2
averageaccuracyoverallvalidationtaskexperimentalconfig- 14https://huggingface.co/sentence-transformers/all-distilroberta-v1
urationswereselectedforfurtherfine-tuning.Thefirstthree 15https://huggingface.co/sentence-transformers/all-mpnet-base-v2
16https://huggingface.co/princeton-nlp/unsup-simcse-bert-base-uncased
4https://ec.europa.eu/eurostat/web/sdi/information-data 17https://huggingface.co/princeton-nlp/sup-simcse-bert-base-uncased
5https://databank.worldbank.org/source/sustainable-development-goals- 18https://tfhub.dev/google/sentence-t5/st5-base/1
(sdgs) 19https://tfhub.dev/google/sentence-t5/st5-large/1
16 VOLUME11,2023
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2025.3595894
Gjorgjevikjetal.:BenchmarkingSentenceEncodersinAssociatingIndicatorswithSustainableDevelopmentGoalsandTargets
SDG.TheSDGsthathaveeither3or4exampleswerealso
| randomlysampled.Thesamestrategywasusedforbothfine- |     |     |     |     |     |     | k   |     |     |     |     |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(cid:88)
tuningtasks.TheAdamoptimizationalgorithmwasusedto yˆ(i) = [1−d(z(i),z(j))]y(j),(z(j),y(j))∈D(i) (3)
TR
| fine-tune | the network, with | a learning | rate | η = 2e | − 5, |     |     |     |     |     |     |
| --------- | ----------------- | ---------- | ---- | ------ | ---- | --- | --- | --- | --- | --- | --- |
j=1
| β = 0.9, | β = 0.999, | ϵ = 1e−8. | The margin | α   | was set |     |     |     |     |     |     |
| -------- | ---------- | --------- | ---------- | --- | ------- | --- | --- | --- | --- | --- | --- |
| 1        | 2          |           |            |     |         |     |     |     |     |     |     |
to0.4inthefirstfine-tuningtask(FT-SDG)while0.2inthe C. POST-HOCANALYSIS
|     |     |     |     |     |     | To better | understand | the | factors | that influenced | the test re- |
| --- | --- | --- | --- | --- | --- | --------- | ---------- | --- | ------- | --------------- | ------------ |
second(FT-TRG).
Foreachpre-trainedsentenceencoderselectedforfurther sults, all factors of interest were represented as input fea-
fine-tuning,therewasonebaselinecheckpoint,and20check- turestoameta-model,i.e.,linearregression,whichwasthen
trainedtopredicttheaccuracyorNDCGbySDGthatwasac-
pointsfine-tunedoneachofthefourfine-tuningdatasetsand
five random seeds. Early stopping was used as a regular- tuallyachievedbyourfine-tunedsentenceencodersandkNN
|                   |            |            |         |          |     | classifier | on the | test datasets | from | (1) the Global | indicator |
| ----------------- | ---------- | ---------- | ------- | -------- | --- | ---------- | ------ | ------------- | ---- | -------------- | --------- |
| ization strategy. | Validation | tasks were | used to | evaluate | the |            |        |               |      |                |           |
checkpoint parameters after each 5 consecutive fine-tuning frameworkofthe2030Agenda(taskMC-IND-SDG)and(2)
iterations,andtheaverageperformanceonallvalidationex- SDG relatedness (task ML-SDG-SDG). The training set on
|     |     |     |     |     |     | which the | linear | regression | was trained | consisted | of all dif- |
| --- | --- | --- | --- | --- | --- | --------- | ------ | ---------- | ----------- | --------- | ----------- |
perimentalsettings(describedinTable1)wascalculated.The
model was fine-tuned on each task for 20 iterations and the ferent fine-tuning and test experimental configurations. The
checkpointwiththehighestaveragevalidationaccuracywas sameprocesswasrepeatedtwice,onceforMC-IND-SDGand
| selected. |     |     |     |     |     | ML-SDG-SDG,resultinginatotalof5,440labeledexamples |     |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | -------------------------------------------------- | --- | --- | --- | --- | --- |
Duringthevalidationandtesting,wewereusingthefine- forthefirstand2,560forthesecond.Theinputfeaturesare
|                |          |                       |     |              |     | described | in Table | 2. Different | linear | regression | algorithms |
| -------------- | -------- | --------------------- | --- | ------------ | --- | --------- | -------- | ------------ | ------ | ---------- | ---------- |
| tuned sentence | encoders | as feature extractors |     | and combined |     |           |          |              |        |            |            |
them with a non-parametric learning algorithm k Nearest were compared, i.e., regular linear regression without reg-
Neighbors (kNN). Within tasks MC-IND-SDG, ML-IND- ularization, Ridge regression (varying regularization hyper-
SDG, and ML-SDG-SDG, four different experimental set- parameter α), Lasso regression (varying α), and ElasticNet
tings were defined, differing in the approximate number of (varyingαandr),whereα,r ∈{1e−6,5e−6,1e−5,5e−
5,1e−4,5e−4,1e−3,5e−3,1e−2,5e−2,0.1,0.5,1.0}.
trainingexamplesbyclass(approximateK).IntaskMC-IND-
TRG,twodifferentexperimentalsettingsweredefined,again Thecontributionofeachfeaturetothepredictionmadebythe
differing in the approximate K. Six validation experimental linearregressionmodelforeachindividualtrainingexample
settings in total were defined and 14 test experimental set- wasthencalculatedwiththeSHAPmethod.
tings.Table1givesthedetailsoneach.
| ThetrainingsetsD |     |                                 |     |     |     | V. RESULTS |     |     |     |     |     |
| ---------------- | --- | ------------------------------- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- |
|                  | TR  | ofthevalidationandtesttaskswere |     |     |     |            |     |     |     |     |     |
created from those used in fine-tuning. In tasks MC-IND- A. PRELIMINARYANALYSIS
SDG, ML-IND-SDG, and ML-SDG-SDG, combinations of For each indicator test set and two variations of the indi-
examples from the fine-tuning sets were created. If S, l l = cator descriptions (title or concatenated title with definition
{1,...,17},isthesetofalltargetsunderSDGl,withcardinal- excerpt), Table 3 first gives the average number of words
ityn(S),thentheapproximatenumberofexamplesforSDG in the specific indicator set and then the average similarity
l
l inthecombinedtrainingsetswouldbeK ∈ {14+n(S)∗ of all indicators to their most similar fine-tuning example.
l
6, 14+n(S)∗17, 22+n(S)∗6, 22+n(S)∗17}. In Theresultsindicatethatthisaveragesimilarityisratherlow
|     | l   | l   |     | l   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ML-SDG-SDG,whilethe“training”exampleswereinitially for most indicator sets, i.e., between 0.20 and 0.25. It is the
sampledinthesamemanner,theactualtrainingsetusedby highest for the test indicator set sampled from the Global
thekNNclassifierconsistedofthecentroidsofthe“training” indicator framework of the 2030 Agenda, i.e., 0.35. The re-
examplesbyclass,i.e.,onetrainingexamplebyclass.These sultsfurthershowthatthisaveragesimilarityisslightlyhigher
centroids,oneperclass,werethenusedtoclassifythetitles whentheindicatorsarerepresentedbytheirtitles(whichare
ofthefirst16SDGsin16classes,excludingSDG17. quiteshortinmostcases),comparedtotheaveragesimilarity
During validation and testing, the parameters of the sen- when they are represented through their concatenated title
tence encoder were fixed and it was only used to output withdefinitionexcerpt(whicharelonger–around30words).
embeddingsofthetrainingandvalidationD VL (testD TS )set Therefore,itcanbeconcludedthatthetestexamplesdonot
examples.Thetrainingsetembeddingsandlabelswereused show much similarity to the fine-tuning examples, i.e., test
examplesdonotappearamongthefine-tuningexamples.
bythekNNclassifiertopredictthevalidation(test)examples
classesbasedonaweightedsumoftheirknearestneighbors’
labels(subsetofkexamplesrepresentedasD(i) ⊂ D ),as B. SENTENCEENCODERBASELINEBENCHMARKING
|     |     |     |     | TR  | TR  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
given with Eq. 3. In MC-IND-SDG and MC-IND-TRG, the The validation accuracy of the twelve pre-trained sentence
performancemetricwastheaccuracy,whileinML-IND-SDG encoders averaged over the six validation experimental set-
and ML-SDG-SDG the Normalized Discounted Cumulative tings and two values of kNN k ∈ {1,3}, is summarized
Gain (NDCG) where the predictions given with Eq. 3 were in Table 4. The average accuracy varies between the dif-
ranked in descending order, and the five predicted classes ferent categories of sentence encoders and within the cat-
withthehighestscorewerecomparedtotheactuallabels. egories themselves. Two sentence encoders achieving the
| VOLUME11,2023 |     |     |     |     |     |     |     |     |     |     | 17  |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2025.3595894
Gjorgjevikjetal.:BenchmarkingSentenceEncodersinAssociatingIndicatorswithSustainableDevelopmentGoalsandTargets
TABLE1. Descriptionofthevalidationandtesttasks,togetherwithallexperimentalsettings.Note:InthetaskML-SDG-SDG,onecentroidbySDGis
calculatedfromthetrainingexamples(6thcolumn).
|       |      |            | DTRsettings |          |      | DVL/DTSsettings |     |     | kNNsettings |
| ----- | ---- | ---------- | ----------- | -------- | ---- | --------------- | --- | --- | ----------- |
| Phase | Task | Text Label | N           | Approx.K | Text | Label           | N K |     | k Metric    |
14+n(Sl)∗6
|            |            | Wiki.   |     | 14+n(Sl)∗17 | Indicator |     | Sec.  |     | 1,         |
| ---------- | ---------- | ------- | --- | ----------- | --------- | --- | ----- | --- | ---------- |
| Validation | MC-IND-SDG | SDG     | 17  | 22+n(Sl)∗6  |           | SDG | 17    |     | Accuracy@1 |
|            |            | excrpt. |     |             | title     |     | IV-A2 |     | 3          |
22+n(Sl)∗17
|            |            | Wiki.   |     | 6   | Indicator |        | Sec.  |     | 1,         |
| ---------- | ---------- | ------- | --- | --- | --------- | ------ | ----- | --- | ---------- |
| Validation | MC-IND-TRG | Target  | 169 |     |           | Target | 169   |     | Accuracy@1 |
|            |            | excrpt. |     | 17  | title     |        | IV-A2 |     | 3          |
14+n(Sl)∗6
|     |     | Wiki. |     | 14+n(Sl)∗17 | Indicator |     | Sec. |     |     |
| --- | --- | ----- | --- | ----------- | --------- | --- | ---- | --- | --- |
Test MC-IND-SDG excrpt. SDG 17 22+n(Sl)∗6 title/definition SDG 17 IV-A2 3 Accuracy@1
22+n(Sl)∗17
|      |            | Wiki.   |     | 6          | Indicator        |        | Sec.  |     |               |
| ---- | ---------- | ------- | --- | ---------- | ---------------- | ------ | ----- | --- | ------------- |
| Test | MC-IND-TRG | Target  | 169 |            |                  | Target | 169   |     | 20 Accuracy@5 |
|      |            | excrpt. |     | 17         | title/definition |        | IV-A2 |     |               |
| Test |            |         |     | 14+n(Sl)∗6 |                  |        |       |     |               |
(zero- ML-IND-SDG Wiki. SDG 17 14+n(Sl)∗17 Indicator SDGs 17 Sec. 20 NDCG@5
| shot      |            | excrpt. |     | 22+n(Sl)∗6  | title/definition |        | IV-A2 |     |           |
| --------- | ---------- | ------- | --- | ----------- | ---------------- | ------ | ----- | --- | --------- |
| learning) |            |         |     | 22+n(Sl)∗17 |                  |        |       |     |           |
| Test      |            |         |     | 14+n(Sl)∗6  |                  |        |       |     |           |
| (zero-    |            | Wiki.   |     | 14+n(Sl)∗17 |                  | Linked |       |     |           |
|           | ML-SDG-SDG | SDG     | 16  |             | SDGtitle         |        | 16 1  |     | 16 NDCG@5 |
| shot      |            | excrpt. |     | 22+n(Sl)∗6  |                  | SDGs   |       |     |           |
| learning) |            |         |     | 22+n(Sl)∗17 |                  |        |       |     |           |
TABLE2. Descriptionoftheinputfeaturesofthelinearregression."FTn"referstotheexamplesfromthefine-tuningsetofthefine-tuningtask
experimentalsetting,while"kNN"referstothetrainingsetofthetesttaskexperimentalsettingusedbythekNNclassifier.
| InputFeature |     |     | Description |     |     |     |     |     |     |
| ------------ | --- | --- | ----------- | --- | --- | --- | --- | --- | --- |
[Section]ExampleNum[FTn|kNN] Numberofexamplesinthe[fine-tuningset|kNNtrainingset]ofthe[fine-tuningtaskFT-SDG|testtask
experimentalsetting],byWikipediaarticlesectionandSDG.Thisappliestoallsectionsexceptthe"targets"
section,whichisaddressedseparatelyinthetwoinputfeaturesthatfollow.
TargetMeanExampleNum[FTn|kNN] Meanofthetotalnumberofexamplesbytargetinthe[fine-tuning|training]setof[fine-tuning|test]task
experimentalsetting(extractedfromtheSDG-specificWikipediaarticles’"targets"section),groupedbySDG.
TargetStdExampleNum[FTn|kNN] Standarddeviationofthetotalnumberofexamplesbytargetinthe[fine-tuning|training]setof[fine-tuning|
test]taskexperimentalsetting(extractedfromtheSDG-specificWikipediaarticles’"targets"section),grouped
bySDG.
[Section]MeanWordNum[FTn|kNN] Meannumberofwordsinthe[fine-tuning|training]examplestextof[fine-tuning|test]taskexperimental
settingbysectionandSDG.
[Section]StdWordNum[FTn|kNN] Standarddeviationofthenumberofwordsinthe[fine-tuning|training]examplestextof[fine-tuning|test]
taskexperimentalsettingbysectionandSDG.
TaskFTn Fine-tuningtask.Valueequals1fordatasetsoftaskFT-SDGexperimentalsettings,andvalueequals2for
datasetsoftaskFT-TRGexperimentalsettings.
NumNeighborskNN NumberofnearestneighborsusedbythekNNclassifierinthetesttaskexperimentalsetting.
TABLE3. Averagewordcountandsimilaritytoafine-tuningexample(maxvalue)ofthedifferentindicatorsetsandindicatorrepresentations,(1)through
theirtitleand(2)throughtheirtitleconcatenatedwithdefinitionexcerpt.
Testset 2030Agenda EUSDGIndicators WDISDGIndicators EULocalSDGIndicators EURegional
|     | Indicators |     |     |     |     |     |     |     | SDGIndica- |
| --- | ---------- | --- | --- | --- | --- | --- | --- | --- | ---------- |
tors
Indicator Title Title Title + Defi- Title Title + Defi- Title Title + Defi- Title
| representa- |     |     | nition |     | nition |     |     | nition |     |
| ----------- | --- | --- | ------ | --- | ------ | --- | --- | ------ | --- |
tion
Avgwords 15.86 6.01(±2.89) 31.28 9.32(±3.48) 31.28 4.21(±2.00) 31.79 5.48(±3.07)
|     | (±8.98) |     | (±10.85) |     | (±10.85) |     |     | (±11.33) |     |
| --- | ------- | --- | -------- | --- | -------- | --- | --- | -------- | --- |
Avgsim. 0.35(±0.16) 0.25(±0.11) 0.23(±0.09) 0.26(±0.11) 0.23(±0.09) 0.25(±0.09) 0.20(±0.06) 0.26(±0.11)
highest average accuracy were selected for further domain- by the encoders from the USE and SimCSE categories,
specific fine-tuning, i.e., SBERT-MINILM-L6 and SBERT- i.e., the USE-TRANSFORMER and SIMCSE-SUP-BERT-
MINILM-L12. In general, the encoders from the SBERT BASE. The ST5 encoders are among those with the lowest
category, i.e., SBERT-MINILM-L6, SBERT-MINILM-L12, averageaccuracy,butitiscomparabletothatofsomeofthe
SBERT-MPNET-BASE, SBERT-DISTILROBERTA, (with encoders from the USE and SimCSE categories, as well as
one exception – SBERT-BERT-BASE presented in a sep- to the SBERT-BERT-BASE encoder. We believe that such
arate research article [58], prior to the remaining four validation accuracy may be a result of the encoders’ pre-
encoders), have the highest average accuracy, followed training tasks/datasets and their similarity to the main tasks
| 18  |     |     |     |     |     |     |     |     | VOLUME11,2023 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- |
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2025.3595894
Gjorgjevikjetal.:BenchmarkingSentenceEncodersinAssociatingIndicatorswithSustainableDevelopmentGoalsandTargets
TABLE4. Averagevalidationaccuracyofthetwelvepre-trainedsentence theencoderfine-tuning.However,thefine-tuningmakesthe
encodersonthesixvalidationexperimentalsettingsandtwovaluesof
|     |     |     |     |     |     |     | classifier | accuracy | less | sensitive | to changes | in  | the indicator |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | ---- | --------- | ---------- | --- | ------------- | --- |
nearestneighborsk∈{1,3}.Thetwoselectedforfurtherfine-tuningare
giveninbold. descriptionlength.Adecreaseintheaccuracyofthebaseline
|     |     |     |     |     |     |     | classifiers | due | to an increase | in  | the length | of  | the indicator |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | -------------- | --- | ---------- | --- | ------------- | --- |
SentenceEncoder AverageValidationAccuracy descriptionispresentforalltestsets,rangingfrommorethan
| USE-TRANSFORMER |     |     |     |     |     | 0.63 |     |     |     |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
15%fortheEUSDGandEULocalSDGtestsetsto3%for
| USE-MULTILINGUAL- |     |     |     |     |     | 0.61 |     |     |     |     |     |     |     |     |
| ----------------- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
CONVOLUTION WDISDG.However,afterthesentenceencoderfine-tuning,
USE-MULTILINGUAL- 0.59 for the EU SDG and EU Local SDG test sets, the accuracy
TRANSFORMER decreases by 5% and 3% appropriately, which is much less
| ST5-BASE |     |     |     |     |     | 0.59 |     |     |     |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
ST5-LARGE 0.58 than its decrease with the baseline classifiers. For the WDI
| SBERT-BERT-BASE |     |     |     |     |     | 0.60 | SDGtestsets,thereisanincreaseof1%. |     |     |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | ---- | ---------------------------------- | --- | --- | --- | --- | --- | --- | --- |
| SBERT-MINILM-L6 |     |     |     |     |     | 0.73 |                                    |     |     |     |     |     |     |     |
InthesecondtesttaskMC-IND-TRG,whichrequiresdis-
| SBERT-MINILM-L12    |     |     |     |     |     | 0.69 |             |         |     |        |                |     |          |     |
| ------------------- | --- | --- | --- | --- | --- | ---- | ----------- | ------- | --- | ------ | -------------- | --- | -------- | --- |
|                     |     |     |     |     |     |      | tinguishing | between | 169 | highly | interconnected |     | targets, | the |
| SBERT-DISTILROBERTA |     |     |     |     |     | 0.66 |             |         |     |        |                |     |          |     |
kNNclassifieraccuracy@5(k=20)isaround80%orabovein
| SBERT-MPNET-BASE |     |     |     |     |     | 0.68 |     |     |     |     |     |     |     |     |
| ---------------- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
SIMCSE-UNSUP-BERT-BASE 0.61 most cases, as given in Table 6. Measuring the accuracy@1
SIMCSE-SUP-BERT-BASE 0.63 was a rather strict test criterion, considering the high level
|     |     |     |     |     |     |     | of inter-relatedness |     | between | the | targets | and our | aim to | find |
| --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | ------- | --- | ------- | ------- | ------ | ---- |
eventhenon-obviousassociationsoftheindicatorswiththe
solvedinthisarticle.Solvingthemaintasksrequiressentence
|     |     |     |     |     |     |     | targets. In | that | sense, we | expected | to  | have more | than | one |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ---- | --------- | -------- | --- | --------- | ---- | --- |
encodersthatcapturethedifferencesbetweenthetopicscov-
associatedtargetwiththetestindicators.Asinthefirsttask,
| ered by | the SDGs/targets | in  | a common | vector | space, | i.e., a |     |     |     |     |     |     |     |     |
| ------- | ---------------- | --- | -------- | ------ | ------ | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
thefine-tuningmakestheclassifierlesssensitivetochanges
verydiversesetoftopics.Thefourbest-performingencoders
inthedescriptionlength,particularlyfortheEULocalSDG
havebeenpre-trainedonalargeanddiversesetoftasksand
|              |                   |      |           | website20), |                 |       | testset.  |       |             |     |         |     |        |      |
| ------------ | ----------------- | ---- | --------- | ----------- | --------------- | ----- | --------- | ----- | ----------- | --- | ------- | --- | ------ | ---- |
| datasets     | (for more details | see  | the SBERT |             |                 | which |           |       |             |     |         |     |        |      |
|              |                   |      |           |             |                 |       | The third | task, | ML-IND-SDG, |     | appears | to  | be the | most |
| has probably | enabled           | them | to better | capture     | the differences |       |           |       |             |     |         |     |        |      |
betweentheSDGsandtargets.Itshouldbenotedthatallthe challenging for the EU Local SDG test set compared to the
restwhichhavearelativelyhighNDCG@5scorebothbefore
aforementionedconclusionsapplysolelytothetaskssolved
|     |     |     |     |     |     |     | and after | the fine-tuning. |     | Similarly | to the | previous | two | test |
| --- | --- | --- | --- | --- | --- | --- | --------- | ---------------- | --- | --------- | ------ | -------- | --- | ---- |
inthisarticleandshouldnotbegeneralized.
|     |     |     |     |     |     |     | tasks, there | is performance |     | degradation |     | as the | length | of the |
| --- | --- | --- | --- | --- | --- | --- | ------------ | -------------- | --- | ----------- | --- | ------ | ------ | ------ |
indicatordescriptionincreasesfortestsetsEUSDGandEU
C. SENTENCEENCODERTESTRESULTSAFTER
LocalSDG.However,suchperformancedegradationiseither
FINE-TUNING
notpresentormuchlowerwithafine-tunedencoder,asgiven
Thetestresultsofthetwoselectedsentenceencodersinthe14
inTable7.
testexperimentalsettings,(1)MC-IND-SDG(4settings),(2)
|            |               |     |                |     |     |            | The improvement |     | of  | the NDCG@5 | value | in  | the test | task |
| ---------- | ------------- | --- | -------------- | --- | --- | ---------- | --------------- | --- | --- | ---------- | ----- | --- | -------- | ---- |
| MC-IND-TRG | (2 settings), |     | (3) ML-IND-SDG |     | (4  | settings), |                 |     |     |            |       |     |          |      |
ML-SDG-SDGisaround7.9%afterfine-tuning,asgivenin
| and (4) | ML-SDG-SDG | (4 settings) |     | are presented |     | in Tables |     |     |     |     |     |     |     |     |
| ------- | ---------- | ------------ | --- | ------------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
Table8.TheimprovementsinML-IND-SDGandML-SDG-
5,6,7,and8,appropriately.Thetablesfirstgivethehighest
SDGindicatethatalthoughinformationonthemutualSDG
baselinetestresultsforanyofthetwoencoders(priortotheir
|     |     |     |     |     |     |     | relations | was not | explicitly | provided | during | fine-tuning, |     | it  |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------- | ---------- | -------- | ------ | ------------ | --- | --- |
fine-tuning)bytesttaskandtestdatasetcombination.Then,
wasstilllearnedfromthetextinthefine-tuningdatasets.
| they give | the highest          | average | result | over five       | random | seeds     |     |     |     |     |     |     |     |     |
| --------- | -------------------- | ------- | ------ | --------------- | ------ | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
| after the | encoders fine-tuning |         | with   | all fine-tuning |        | datasets, |     |     |     |     |     |     |     |     |
againbytesttaskandtestdatasetcombination.Theseaverage D. POST-HOCANALYSIS
IntaskMC-IND-SDG,thelowestmeansquarederror(MSE)
resultsareaccompaniedbythebesttestresultsofthatsame
of0.0073wasachievedwithRidgeregression(α=1e−6),
| fine-tuning/test | configuration |     | but with | one | specific | random |     |     |     |     |     |     |     |     |
| ---------------- | ------------- | --- | -------- | --- | -------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
asintaskML-SDG-SDG,wherethelowestMSEwas0.0059.
| seed. This | result is | given along | with | the improvement |     | over |     |     |     |     |     |     |     |     |
| ---------- | --------- | ----------- | ---- | --------------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
ThedistributionofSHAPvaluesbyfeatureintaskMC-IND-
thehighestbaselineresultforthesametesttaskanddataset
SDGisillustratedinFigure15,whileintaskML-SDG-SDG
combination.
|     |     |     |     |     |     |     | in Figure | 16. The | suffix | FTn or | kNN simply |     | indicates | that |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------- | ------ | ------ | ---------- | --- | --------- | ---- |
Inthefirsttesttask,MC-IND-SDG,thehighestkNNclas-
|     |     |     |     |     |     |     | the feature | refers | to the | examples | in the | fine-tuning |     | set of |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------ | ------ | -------- | ------ | ----------- | --- | ------ |
sifieraccuracy@1(k=3)onalldatasetsisabove80%orvery
thefine-tuningtasksortotheexamplesinthekNNtraining
closetoit(inthecaseofEURegionalSDGtestset),asgiven
|     |     |     |     |     |     |     | set of the | test tasks. | In  | both tasks, | the structure |     | of the | kNN |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ----------- | --- | ----------- | ------------- | --- | ------ | --- |
inTable5.Theaccuracy@1is90%forthetestsetsampled
trainingsethadalargerinfluence.InthetaskMC-IND-SDG,
fromtheGlobalindicatorframeworkfromthe2030Agenda.
thelargenumberofwordsinthetextexcerptsextractedfrom
| For the test | sets having | two | indicator | description |     | variations |     |     |     |     |     |     |     |     |
| ------------ | ----------- | --- | --------- | ----------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
thesectiondevotedtothetargets,the“background”section,
| (title and | concatenated | title | with definition |     | excerpt), | it is |     |     |     |     |     |     |     |     |
| ---------- | ------------ | ----- | --------------- | --- | --------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
visiblethattheclassifieraccuracyishigherwhentheindica- and the lead section had the largest positive influence, as
wellasthemeannumberofexamplesbytargetandthelow
torsarerepresentedthroughtheirtitle,bothbeforeandafter
standarddeviationofthenumberofwordsintheleadsection
20https://www.sbert.net/ excerpts.Duringfine-tuning,thelargemeannumberofexam-
| VOLUME11,2023 |     |     |     |     |     |     |     |     |     |     |     |     |     | 19  |
| ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2025.3595894
Gjorgjevikjetal.:BenchmarkingSentenceEncodersinAssociatingIndicatorswithSustainableDevelopmentGoalsandTargets
TABLE5. HighestbaselineresultintesttaskMC-IND-SDGandhighestaverageresultoverfiverandomseedsafterencodersfine-tuningbytestset.The
besttestresultsofthatsamefine-tuning/testconfigurationaregiven,alongwiththeimprovementoverthehighestbaselineresultforthattestset.
|     | Configuration |     |     | Accuracy@1(kNNk=3) |     |
| --- | ------------- | --- | --- | ------------------ | --- |
TestDataset IndicatorsRepresentation Fine-Tuning HighestAverageover5Random BestCheckpoint(Improvement
|                         |                  |     |              | Seeds(St.Dev.) | OverBaseline) |
| ----------------------- | ---------------- | --- | ------------ | -------------- | ------------- |
|                         |                  |     | No(Baseline) | /              | 0.84          |
| 2030AgendaIndicators    | Title            |     |              |                |               |
|                         |                  |     | Yes          | 0.89(0.006)    | 0.90(+0.061)  |
|                         |                  |     | No(Baseline) | /              | 0.82          |
| EUSDGIndicators         | Title            |     |              |                |               |
|                         |                  |     | Yes          | 0.86(0.009)    | 0.87(+0.050)  |
|                         |                  |     | No(Baseline) | /              | 0.65          |
| EUSDGIndicators         | Title+Definition |     |              |                |               |
|                         |                  |     | Yes          | 0.82(0.005)    | 0.82(+0.170)  |
|                         |                  |     | No(Baseline) | /              | 0.76          |
| WDISDGIndicators        | Title            |     |              |                |               |
|                         |                  |     | Yes          | 0.82(0.007)    | 0.83(+0.068)  |
|                         |                  |     | No(Baseline) | /              | 0.73          |
| WDISDGIndicators        | Title+Definition |     |              |                |               |
|                         |                  |     | Yes          | 0.82(0.016)    | 0.84(+0.106)  |
|                         |                  |     | No(Baseline) | /              | 0.83          |
| EULocalSDGIndicators    | Title            |     |              |                |               |
|                         |                  |     | Yes          | 0.87(0.015)    | 0.89(+0.056)  |
|                         |                  |     | No(Baseline) | /              | 0.68          |
| EULocalSDGIndicators    | Title+Definition |     |              |                |               |
|                         |                  |     | Yes          | 0.85(0.010)    | 0.86(+0.181)  |
|                         |                  |     | No(Baseline) | /              | 0.73          |
| EURegionalSDGIndicators | Title            |     |              |                |               |
|                         |                  |     | Yes          | 0.76(0.015)    | 0.77(+0.036)  |
TABLE6. HighestbaselineresultintesttaskMC-IND-TRGandhighestaverageresultoverfiverandomseedsafterencodersfine-tuningbytestset.The
besttestresultsofthatsamefine-tuning/testconfigurationisgiven,alongwiththeimprovementoverthehighestbaselineresultforthattestset.
|     | Configuration |     |     | Accuracy@5(kNNk=20) |     |
| --- | ------------- | --- | --- | ------------------- | --- |
TestDataset IndicatorsRepresentation Fine-Tuning HighestAverageover5Random BestCheckpoint(Improvement
|                      |       |     |              | Seeds(St.Dev.) | OverBaseline) |
| -------------------- | ----- | --- | ------------ | -------------- | ------------- |
|                      |       |     | No(Baseline) | /              | 0.84          |
| 2030AgendaIndicators | Title |     |              |                |               |
|                      |       |     | Yes          | 0.88(0.009)    | 0.89(+0.050)  |
|                      |       |     | No(Baseline) | /              | 0.73          |
| WDISDGIndicators     | Title |     |              |                |               |
|                      |       |     | Yes          | 0.78(0.009)    | 0.79(+0.057)  |
|                      |       |     | No(Baseline) | /              | 0.73          |
WDISDGIndicators Title+Definition Yes 0.77(0.007) 0.77(+0.041)
|                         |                  |     | No(Baseline) | /           | 0.78         |
| ----------------------- | ---------------- | --- | ------------ | ----------- | ------------ |
| EULocalSDGIndicators    | Title            |     |              |             |              |
|                         |                  |     | Yes          | 0.79(0.006) | 0.79(+0.014) |
|                         |                  |     | No(Baseline) | /           | 0.63         |
| EULocalSDGIndicators    | Title+Definition |     |              |             |              |
|                         |                  |     | Yes          | 0.78(0.014) | 0.79(+0.167) |
|                         |                  |     | No(Baseline) | /           | 0.78         |
| EURegionalSDGIndicators | Title            |     | Yes          | 0.83(0.009) | 0.84(+0.060) |
TABLE7. HighestbaselineresultintesttaskML-IND-SDGandhighestaverageresultoverfiverandomseedsafterencodersfine-tuningbytestset.The
besttestresultsofthatsamefine-tuning/testconfigurationaregiven,alongwiththeimprovementoverthehighestbaselineresultforthattestset.
|     | Configuration |     |     | NDCG@5(kNNk=20) |     |
| --- | ------------- | --- | --- | --------------- | --- |
TestDataset IndicatorsRepresentation Fine-Tuning HighestAverageover5Random Best Checkpoint (Improvement
|                      |                  |     |              | Seeds(St.Dev.) | OverBaseline) |
| -------------------- | ---------------- | --- | ------------ | -------------- | ------------- |
|                      |                  |     | No(Baseline) | /              | 0.97          |
| 2030AgendaIndicators | Title            |     | Yes          | 1.00(0.000)    | 1.00(+0.026)  |
|                      |                  |     | No(Baseline) | /              | 0.90          |
| EUSDGIndicators      | Title            |     |              |                |               |
|                      |                  |     | Yes          | 0.90(0.007)    | 0.91(+0.011)  |
|                      |                  |     | No(Baseline) | /              | 0.79          |
| EUSDGIndicators      | Title+Definition |     |              |                |               |
|                      |                  |     | Yes          | 0.86(0.001)    | 0.86(+0.073)  |
|                      |                  |     | No(Baseline) | /              | 0.70          |
| EULocalSDGIndicators | Title            |     | Yes          | 0.70(0.007)    | 0.71(+0.012)  |
|                      |                  |     | No(Baseline) | /              | 0.64          |
| EULocalSDGIndicators | Title+Definition |     |              |                |               |
|                      |                  |     | Yes          | 0.70(0.007)    | 0.71(+0.067)  |
TABLE8. HighestbaselineresultintesttaskML-SDG-SDGandhighestaverageresultoverfiverandomseedsafterencodersfine-tuningbytestset.The
besttestresultsofthatsamefine-tuning/testconfigurationaregiven,alongwiththeimprovementoverthehighestbaselineresultforthattestset.
Configuration NDCG@5(kNNk=16)
TestDataset IndicatorsRepresentation Fine-Tuning Highest Average over 5 Random BestCheckpoint(ImprovementOver
|                      |     |              | Seeds(St.Dev.) |     | Baseline)    |
| -------------------- | --- | ------------ | -------------- | --- | ------------ |
|                      |     | No(Baseline) | /              |     | 0.67         |
| SDGRelatedness Title |     |              |                |     |              |
|                      |     | Yes          | 0.75(0.005)    |     | 0.75(+0.079) |
20 VOLUME11,2023
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

Gjorgjevikjetal.:BenchmarkingSentenceEncodersinAssociatingIndicatorswithSustainableDevelopmentGoalsandTargets
 + L J K
 7 D U J H W  0 H D Q  : R U G  1 X P  N 1 1
 / H D G  V H F W L R Q  6 W G  : R U G  1 X P  N 1 1
 7 D U J H W  6 W G  : R U G  1 X P  N 1 1
 7 D U J H W  0 H D Q  ( [ D P S O H  1 X P  N 1 1
 / H D G  V H F W L R Q  0 H D Q  : R U G  1 X P  N 1 1
 1 X P  1 H L J K E R X U V  N 1 1
 % D F N J U R X Q G  0 H D Q  : R U G  1 X P  N 1 1
 % D F N J U R X Q G  6 W G  : R U G  1 X P  N 1 1
 * H Q H U D O  0 H D Q  : R U G  1 X P  N 1 1
 7 D U J H W  0 H D Q  ( [ D P S O H  1 X P  ) 7 Q
 % D F N J U R X Q G  0 H D Q  : R U G  1 X P  ) 7 Q
 7 D U J H W  6 W G  ( [ D P S O H  1 X P  N 1 1
 7 D U J H W  6 W G  : R U G  1 X P  ) 7 Q
 7 D U J H W  0 H D Q  : R U G  1 X P  ) 7 Q
 / H D G  V H F W L R Q  ( [ D P S O H  1 X P  N 1 1
 / H D G  V H F W L R Q  6 W G  : R U G  1 X P  ) 7 Q
 & K D O O H Q J H V  6 W G  : R U G  1 X P  N 1 1
 2 U J D Q L ] D W L R Q V  0 H D Q  : R U G  1 X P  N 1 1
 % D F N J U R X Q G  ( [ D P S O H  1 X P  N 1 1
 7 D U J H W  6 W G  ( [ D P S O H  1 X P  ) 7 Q
 % D F N J U R X Q G  6 W G  : R U G  1 X P  ) 7 Q
 & K D O O H Q J H V  ( [ D P S O H  1 X P  N 1 1
 / H D G  V H F W L R Q  0 H D Q  : R U G  1 X P  ) 7 Q
 / H D G  V H F W L R Q  ( [ D P S O H  1 X P  ) 7 Q
 7 D V N  ) 7 Q
 % D F N J U R X Q G  ( [ D P S O H  1 X P  ) 7 Q
 * H Q H U D O  ( [ D P S O H  1 X P  N 1 1
 2 U J D Q L ] D W L R Q V  ( [ D P S O H  1 X P  N 1 1
 * H Q H U D O  ( [ D P S O H  1 X P  ) 7 Q
 2 U J D Q L ] D W L R Q V  6 W G  : R U G  1 X P  N 1 1
 * H Q H U D O  6 W G  : R U G  1 X P  ) 7 Q
 & K D O O H Q J H V  0 H D Q  : R U G  1 X P  N 1 1
 & K D O O H Q J H V  6 W G  : R U G  1 X P  ) 7 Q
 * H Q H U D O  0 H D Q  : R U G  1 X P  ) 7 Q
 2 U J D Q L ] D W L R Q V  0 H D Q  : R U G  1 X P  ) 7 Q
 & K D O O H Q J H V  ( [ D P S O H  1 X P  ) 7 Q
 * H Q H U D O  6 W G  : R U G  1 X P  N 1 1
 2 U J D Q L ] D W L R Q V  ( [ D P S O H  1 X P  ) 7 Q
 2 U J D Q L ] D W L R Q V  6 W G  : R U G  1 X P  ) 7 Q
 & K D O O H Q J H V  0 H D Q  : R U G  1 X P  ) 7 Q
 / R Z
                                               
 6 + $ 3  Y D O X H   L P S D F W  R Q  P R G H O  R X W S X W 
 H X O D Y  H U X W D H )
 + L J K
 * H Q H U D O  ( [ D P S O H  1 X P  N 1 1
 * H Q H U D O  0 H D Q  : R U G  1 X P  N 1 1
 / H D G  V H F W L R Q  6 W G  : R U G  1 X P  N 1 1
 * H Q H U D O  6 W G  : R U G  1 X P  N 1 1
 / H D G  V H F W L R Q  0 H D Q  : R U G  1 X P  N 1 1
 7 D U J H W  6 W G  : R U G  1 X P  N 1 1
 % D F N J U R X Q G  6 W G  : R U G  1 X P  N 1 1
 % D F N J U R X Q G  0 H D Q  : R U G  1 X P  N 1 1
 * H Q H U D O  ( [ D P S O H  1 X P  ) 7 Q
 % D F N J U R X Q G  0 H D Q  : R U G  1 X P  ) 7 Q
 & K D O O H Q J H V  6 W G  : R U G  1 X P  N 1 1
 / H D G  V H F W L R Q  6 W G  : R U G  1 X P  ) 7 Q
 7 D U J H W  0 H D Q  : R U G  1 X P  ) 7 Q
 2 U J D Q L ] D W L R Q V  0 H D Q  : R U G  1 X P  N 1 1
 % D F N J U R X Q G  6 W G  : R U G  1 X P  ) 7 Q
 7 D U J H W  6 W G  ( [ D P S O H  1 X P  ) 7 Q
 & K D O O H Q J H V  ( [ D P S O H  1 X P  N 1 1
 / H D G  V H F W L R Q  ( [ D P S O H  1 X P  N 1 1
 * H Q H U D O  0 H D Q  : R U G  1 X P  ) 7 Q
 7 D U J H W  6 W G  ( [ D P S O H  1 X P  N 1 1
 * H Q H U D O  6 W G  : R U G  1 X P  ) 7 Q
 / H D G  V H F W L R Q  0 H D Q  : R U G  1 X P  ) 7 Q
 % D F N J U R X Q G  ( [ D P S O H  1 X P  N 1 1
 2 U J D Q L ] D W L R Q V  ( [ D P S O H  1 X P  N 1 1
 7 D U J H W  0 H D Q  : R U G  1 X P  N 1 1
 7 D U J H W  6 W G  : R U G  1 X P  ) 7 Q
 2 U J D Q L ] D W L R Q V  6 W G  : R U G  1 X P  N 1 1
 % D F N J U R X Q G  ( [ D P S O H  1 X P  ) 7 Q
 7 D V N  ) 7 Q
 / H D G  V H F W L R Q  ( [ D P S O H  1 X P  ) 7 Q
 & K D O O H Q J H V  0 H D Q  : R U G  1 X P  N 1 1
 & K D O O H Q J H V  6 W G  : R U G  1 X P  ) 7 Q
 7 D U J H W  0 H D Q  ( [ D P S O H  1 X P  ) 7 Q
 & K D O O H Q J H V  ( [ D P S O H  1 X P  ) 7 Q
 7 D U J H W  0 H D Q  ( [ D P S O H  1 X P  N 1 1
 2 U J D Q L ] D W L R Q V  0 H D Q  : R U G  1 X P  ) 7 Q
 & K D O O H Q J H V  0 H D Q  : R U G  1 X P  ) 7 Q
 2 U J D Q L ] D W L R Q V  ( [ D P S O H  1 X P  ) 7 Q
 2 U J D Q L ] D W L R Q V  6 W G  : R U G  1 X P  ) 7 Q
 1 X P  1 H L J K E R X U V  N 1 1
 / R Z
                                               
 6 + $ 3  Y D O X H   L P S D F W  R Q  P R G H O  R X W S X W 
FIGURE15. SHAPvaluedistributionbyinputfeature(testtask
MC-IND-SDG).
plesfortheSDGtargetsinthefine-tuningsethadthegreatest
positive influence, as well as the large number of words in
theexcerptsfromthe“background”section.Contrarytoour
expectations, the large number of excerpts from the general
Wikipediaarticleortheirlargenumberofwordsdidnothave
a positive influence on the accuracy by SDG. The presence
of excerpts extracted from sections such as “organizations”
or “challenges” did not affect accuracy positively, and this
observationalsoappliestothetaskML-SDG-SDG.However,
in this task the large number of examples from the general
articleinboththefine-tuningandkNNtrainingsethadneg-
ative influence, while the large mean number of words in
theexcerptsfromthe“background”sectioninboththefine-
tuning and kNN training set a positive one. The large mean
numberofwordsintheexcerptsfromtheleadsection,which
arepartofthekNNtrainingset,hadpositiveinfluenceaswell.
VI. DISCUSSION
Thisarticleproposedamodel-agnosticmethodforfindingas-
sociations between sustainable development indicators used
at the national or subnational level of governance with the
SDGs and targets from the UN 2030 Agenda. By relying
on textual descriptions of SDGs, targets, and indicators, the
 H X O D Y  H U X W D H )
This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2025.3595894
FIGURE16. SHAPvaluedistributionbyinputfeature(testtask
ML-SDG-SDG).
dependenceonindicatorstatisticaldataquantityandquality
wasremoved.Thearticleproposedanewformulationofthe
problem in the ML domain – text classification and splited
the problem into two main and two auxiliary tasks to make
the evaluation easier. The proposed method used (1) short
texttodescribetheSDGs,targets,andindicators,(2)general-
purposepre-trainedsentenceencoderstorepresentthosede-
scriptionsinacommonvectorspace,(3)contrastiverepresen-
tationlearninganddomain-specificdatasetstofine-tunetheir
parameters,and(4)kNNclassifierintheexperimentalsetting,
to“associate”indicatorswithSDGsandtargetsbycomparing
their embeddings outputted by the shared encoder with a
distancemetric.Themethodwasevaluatedonfivereal-world
indicator sets used at different levels of governance. This
sectionanalyzestheresultsinthecontextofthethreeresearch
questionsandsummarizesthelimitationsofthemethod.
Regardingthepotentialoftextualdataandgeneral-purpose
pre-trainedsentenceencodersinsolvingthemainandauxil-
iarytasks(RQ1),thetestresultsshowedthattextisapromis-
ing type of data for solving the tasks. The validation results
showed that certain sentence encoders are particularly well
suited to solving the tasks even before the domain-specific
fine-tuning,i.e.,theyhavealreadycapturedusefulknowledge
VOLUME11,2023 21
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2025.3595894
Gjorgjevikjetal.:BenchmarkingSentenceEncodersinAssociatingIndicatorswithSustainableDevelopmentGoalsandTargets
to solve the tasks even during their pre-training on general which the method had to learn to distinguish, (2) the lack
NLPtasks.ThisparticularlyreferstotheSBERTcategoryof ofready-to-usefine-tuningdatasetsfortheproblem,i.e.,the
sentenceencoders.Furthermore,inallofthetestconfigura- needtocreatethemourselves,and,finally,(3)thenon-trivial
tions,theirperformancewasfurtherimprovedbyfine-tuning representativetextextractionprocessfromtheWikipediaarti-
withdomain-specificdatasets,eventhoughthedatasetswere cles.Therefore,thelimitationsanddirectionsforovercoming
quite limited in size. That suggests the possibility of even theminfutureworkaregiveninTable9.
| greater  | performance | improvements |          | with | larger | fine-tuning |          |     |     |     |     |     |     |     |     |
| -------- | ----------- | ------------ | -------- | ---- | ------ | ----------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
| datasets | and better  | selected     | examples |      | based  | on the      | insights |     |     |     |     |     |     |     |     |
VII. CONCLUSION
fromSectionV-D.
|          |                |     |              |     |         |     |         | Monitoring | progress | toward | achieving |     | the 2030 | Agenda | for |
| -------- | -------------- | --- | ------------ | --- | ------- | --- | ------- | ---------- | -------- | ------ | --------- | --- | -------- | ------ | --- |
| In terms | of performance |     | improvements |     | through |     | domain- |            |          |        |           |     |          |        |     |
specific fine-tuning of the pre-trained encoders (RQ2), the Sustainable Development of the United Nations is of the
|     |     |     |     |     |     |     |     | utmost priority |     | in the | current | decade. | Sustainable |     | develop- |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | ------ | ------- | ------- | ----------- | --- | -------- |
presentedresultsbytesttaskcategoryanddatasetshowedthat
|     |     |     |     |     |     |     |     | ment policies/actions |     | are | taken | at different |     | levels | of gov- |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | ----- | ------------ | --- | ------ | ------- |
thedomain-specificfine-tuningimprovedthebaselineresults
in all test task categories for all test datasets. Although the ernance, and monitoring of their effects on the Sustainable
|     |     |     |     |     |     |     |     | Development | Goals | (SDGs) |     | and targets | is essential |     | due to |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ----- | ------ | --- | ----------- | ------------ | --- | ------ |
fine-tuningdatasetswerequitelimitedinsize,theirusewitha
contrastiverepresentationlearningmethodstillimprovedthe SDGs/targets complex and not always obvious interactions.
Indicatorsrelevanttoaspecificcontext(e.g.,levelofgover-
| baseline | results. | The best-performing |     |     | fine-tuning |     | and kNN |                   |     |         |     |          |      |     |           |
| -------- | -------- | ------------------- | --- | --- | ----------- | --- | ------- | ----------------- | --- | ------- | --- | -------- | ---- | --- | --------- |
|          |          |                     |     |     |             |     |         | nance, geographic |     | region) | are | commonly | used | for | this pur- |
configurationwasspecifictothetestindicatordataset,which
can be attributed to the different purposes of the datasets, pose, but the associations of such indicators with the SDGs
|           |              |         |         |     |      |           |        | may not | always | be easy | to determine. |     | This | article | presents |
| --------- | ------------ | ------- | ------- | --- | ---- | --------- | ------ | ------- | ------ | ------- | ------------- | --- | ---- | ------- | -------- |
| resulting | in different | writing | styles, | as  | well | as length | of the |         |        |         |               |     |      |         |          |
titlesanddefinitionsoftheirindicators.Amorediverseval- a model-agnostic framework (Embed4SD) to associate in-
idationsetsampledfromdifferentindicatorsetsmayhelpin dicators with SDGs and targets by comparing their textual
|     |     |     |     |     |     |     |     | descriptions. | In  | that way, | it removes |     | the dependence |     | on the |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --------- | ---------- | --- | -------------- | --- | ------ |
selectingamodelthatbetterfitsdiverseindicatorsets,apos-
sible research direction for future work. Furthermore, fine- variable indicator statistical data quantity/quality and facil-
|     |     |     |     |     |     |     |     | itates human | experts’ |     | manual | mapping | process | with | data- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | -------- | --- | ------ | ------- | ------- | ---- | ----- |
tuningwithothercontrastiverepresentationlearningmethods
|     |     |     |     |     |     |     |     | driven insights. |     | Our experiments |     | include | a   | comprehensive |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --------------- | --- | ------- | --- | ------------- | --- |
ispossibleaswellandshouldbeconsideredinfuturework.
The results also showed that the textual data used in de- domain-specificbenchmarkingof12sentenceencoders,fine-
|          |           |          |     |            |     |               |     | tuning of | the best | ones | on a | newly | created dataset, |     | evalua- |
| -------- | --------- | -------- | --- | ---------- | --- | ------------- | --- | --------- | -------- | ---- | ---- | ----- | ---------------- | --- | ------- |
| scribing | the SDGs, | targets, | and | indicators | has | a significant |     |           |          |      |      |       |                  |     |         |
influenceonthetestresultswhenusingtheproposedmethod tion with five real-world indicator sets consisting of around
|        |                 |     |         |        |           |     |           | 800 indicators | in  | total, | and measuring |     | the influence |     | of 40 |
| ------ | --------------- | --- | ------- | ------ | --------- | --- | --------- | -------------- | --- | ------ | ------------- | --- | ------------- | --- | ----- |
| (RQ3). | This especially |     | applies | to the | structure | of  | the fine- |                |     |        |               |     |               |     |       |
factorsontheresultsusingexplainableartificialintelligence
tuningandkNNtrainingset,asshownbytheSHAPanalysis
on the Global indicator framework test set in Section V-D. (xAI). The results show that certain sentence encoders are
|     |     |     |     |     |     |     |     | better suited | to  | solving | the task | than | others, | potentially | due |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------- | -------- | ---- | ------- | ----------- | --- |
Thoseresultsshowedthatthedifferencesbetweenthetopics
covered by the SDGs were better captured in the excerpts to the diversity of their pre-training datasets. Furthermore,
|     |     |     |     |     |     |     |     | not only | does fine-tuning |     | improve |     | predictive | performance |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---------------- | --- | ------- | --- | ---------- | ----------- | --- |
extractedfromtheabstractand“background”sectionofthe
|              |           |     |           |     |        |         |         | over baselines, |     | it also | reduces | the sensitivity |     | to changes | in  |
| ------------ | --------- | --- | --------- | --- | ------ | ------- | ------- | --------------- | --- | ------- | ------- | --------------- | --- | ---------- | --- |
| SDG-specific | Wikipedia |     | articles, | but | not so | well in | the ex- |                 |     |         |         |                 |     |            |     |
cerpts extracted from sections such as “challenges” or “or- indicatordescriptionlength,i.e.,whiletheperformancedrops
|     |     |     |     |     |     |     |     | even by | up to 17% | for | baseline | models | as length | increases, |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --------- | --- | -------- | ------ | --------- | ---------- | --- |
ganizations”.Onthecontrary,thesectionsofthearticlesde-
votedtothetargetsweremoreusefulinassociatingindicators it remains comparable for fine-tuned models. We believe
|          |               |          |            |     |                |     |          | that Embed4SD |     | makes        | a step | in filling | the    | current | gap of  |
| -------- | ------------- | -------- | ---------- | --- | -------------- | --- | -------- | ------------- | --- | ------------ | ------ | ---------- | ------ | ------- | ------- |
| with the | SDGs and      | targets, | compared   |     | to associating |     | SDGs     |               |     |              |        |            |        |         |         |
|          |               |          |            |     |                |     |          | comprehensive |     | benchmarking |        | of AI      | models | on the  | problem |
| to their | related SDGs. |          | The length | of  | the indicator  |     | descrip- |               |     |              |        |            |        |         |         |
tions also influenced the results, but that influence was less andopensapromisingresearchdirection,thatis,solvingthe
problemthroughtextualdata.
pronouncedwhenusingfine-tunedsentenceencoders.When
| using fine-tuned |       | encoders, | there        | was | either   | no performance |          |     |     |     |     |     |     |     |     |
| ---------------- | ----- | --------- | ------------ | --- | -------- | -------------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
| degradation      | or it | was       | much smaller |     | compared | to             | the case |     |     |     |     |     |     |     |     |
APPENDIXA
| of encoders | which | were | not | fine-tuned. | Therefore, |     | it can |     |     |     |     |     |     |     |     |
| ----------- | ----- | ---- | --- | ----------- | ---------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
SUSTAINABLEDEVELOPMENTGOALS
beconcludedthatthebenefitofdomain-specificfine-tuning
Eachofthefirst16SDGsisdevotedtoaspecificarea,while
| of the sentence | encoders    |     | was | twofold,      | i.e., | (1) it      | improved |        |            |     |           |     |                |     |        |
| --------------- | ----------- | --- | --- | ------------- | ----- | ----------- | -------- | ------ | ---------- | --- | --------- | --- | -------------- | --- | ------ |
|                 |             |     |     |               |       |             |          | SDG 17 | is devoted | to  | the means | of  | implementation |     | of the |
| the predictive  | performance |     | of  | the evaluated |       | classifiers | over     |        |            |     |           |     |                |     |        |
other16SDGsandglobalpartnership.ForeachSDG,there
| the baseline | and | (2) it | resulted | in classifiers |     | that | were less |             |      |          |      |       |                |     |          |
| ------------ | --- | ------ | -------- | -------------- | --- | ---- | --------- | ----------- | ---- | -------- | ---- | ----- | -------------- | --- | -------- |
|              |     |        |          |                |     |      |           | are targets | that | describe | what | needs | to be realized |     | by 2030, |
sensitivetochangesinindicatordescriptionlength.
|     |     |     |     |     |     |     |     | i.e., (1) | outcome | targets | and | (2) means | of implementation |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------- | ------- | --- | --------- | ----------------- | --- | --- |
Finally,mostofthelimitationsofthisstudyweremainlya
targets,bothtypesofequalimportance[1].Abriefdescription
resultoftheexperimentalchoiceswehadtomaketokeepthe
ofthe17SDGsintermsoftheirtitleandtargetsisgivenin
| study within | a reasonable |     | scope, | given | the many | challenges |     |     |     |     |     |     |     |     |     |
| ------------ | ------------ | --- | ------ | ----- | -------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Table10.Forfurtherdetails,seetheUN2030Agenda[1].
thathadtobeaddressed.Thesechallengesincluded(1)alarge
numberofSDGsandtargetswithcomplexmutualinterlinks
| 22  |     |     |     |     |     |     |     |     |     |     |     |     |     | VOLUME11,2023 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2025.3595894
Gjorgjevikjetal.:BenchmarkingSentenceEncodersinAssociatingIndicatorswithSustainableDevelopmentGoalsandTargets
TABLE9. Limitationsofthestudyanddirectionsforfuturework.
Limitation FutureWorkDirection
Benchmarkingsentenceencodersfromcategoriesthatwerestate-of-the-art Benchmarkinganextensivesetofnewlyproposedstate-of-the-artencoders
atthetimeofwriting,potentiallymissingnewlyproposedencoders. which are highly ranked in general benchmarks like the Massive Text
EmbeddingBenchmark(MTEB)[71].Benchmarkingstate-of-the-artopen-
source LLMs on the tasks, after proper adjustment of the tasks to LLM
context.
Usingasinglesourceoftextdataforthefine-tuningdatasets,i.e.,Wikipedia, Creating fine-tuning datasets with textual descriptions of the SDGs and
whichmaybeinsufficienttoattributethedifferentwritingstylesandti- targetsthatcomefromdiversepubliclyavailablesources.
tle/descriptionexpressivenesspertinenttodifferentreal-worldindicatorsets.
Hypothesizing a positive influence (1) of the sections from the general TheclassificationofindicatorstoSDGsgenerallyrequiresdescriptionsof
Wikipedia article and (2) of sections such as “organizations” and “chal- theSDGsthataremuchmoresimilartothoseoftheirtargets.
lenges”(usedtocompensatefortheshortergeneralsections).
Experimentationwithasinglecontrastiverepresentationlearningmethod, Evaluatingadditionalcontrastiverepresentationlearningmethodsandad-
i.e.,thetripletnetworkarchitecture. justingtheirfine-tuningprocesstothefindingsoutlinedinSectionsVand
VI.
No fine-tuning task that considers the mutual links between the ObtainingdatathatcapturescertainlinksbetweentheSDGs/targetsaspart
SDGs/targets. of an additional fine-tuning task, under the assumption that such a task
wouldimprovethetestresults.
TABLE10. Titlesofthe17SDGs[1].
Targets
Goal Title Outcome MeansofImplementation
1 Endpovertyinallitsformseverywhere 1.1-1.5 1.a,1.b
2 Endhunger,achievefoodsecurityandimprovednutritionandpromotesustainableagriculture 2.1-2.5 2.a-2.c
3 Ensurehealthylivesandpromotewell-beingforallatallages 3.1-3.9 3.a-3.d
4 Ensureinclusiveandequitablequalityeducationandpromotelifelonglearningopportunitiesfor 4.1-4.7 4.a-4.c
all
5 Achievegenderequalityandempowerallwomenandgirls 5.1-5.6 5.a-5.c
6 Ensureavailabilityandsustainablemanagementofwaterandsanitationforall 6.1-6.6 6.a,6.b
7 Ensureaccesstoaffordable,reliable,sustainableandmodernenergyforall 7.1-7.3 7.a,7.b
8 Promotesustained,inclusiveandsustainableeconomicgrowth,fullandproductiveemployment 8.1-8.10 8.a,8.b
anddecentworkforall
9 Buildresilientinfrastructure,promoteinclusiveandsustainableindustrializationandfosterinno- 9.1-9.5 9.a-9.c
vation
10 Reduceinequalitywithinandamongcountries 10.1-10.7 10.a-10.c
11 Makecitiesandhumansettlementsinclusive,safe,resilientandsustainable 11.1-11.7 11.a-11.c
12 Ensuresustainableconsumptionandproductionpatterns 12.1-12.8 12.a-12.c
13 Takeurgentactiontocombatclimatechangeanditsimpacts 13.1-13.3 13.a,13.b
14 Conserveandsustainablyusetheoceans,seasandmarineresourcesforsustainabledevelopment 14.1-14.7 14.a-14.c
15 Protect,restoreandpromotesustainableuseofterrestrialecosystems,sustainablymanageforests, 15.1-15.9 15.a-15.c
combatdesertification,andhaltandreverselanddegradationandhaltbiodiversityloss
16 Promotepeacefulandinclusivesocietiesforsustainabledevelopment,provideaccesstojusticefor 16.1-16.10 16.a,16.b
allandbuildeffective,accountableandinclusiveinstitutionsatalllevels
17 Strengthen the means of implementation and revitalize the global partnership for sustainable 17.1-17.19
development
APPENDIXB Theclusteringusedthedefaultparameterssuggestedbythe
KEYWORDCO-OCCURRENCENETWORK tool,resultinginsixclusters.Foramoredetaileddescription
The keyword co-occurrence analysis of abstracts of related oftheparameters,seetheVOSviewermanual22.
articles referenced in Section II-B was performed using the
VOSviewer software21, version 1.6.20. To construct the co- APPENDIXC
occurrence network, binary counting was used. It only con- WIKIPEDIAARTICLESPROVIDINGDATA
sidered whether a keyword appeared in an abstract, not the The18English-languageWikipediaarticlesusedasasource
numberoftimesthekeywordappearedthere.Keywordsthat of text for fine-tuning datasets are listed in Table 11. The
appearedinatleasttwoabstractswereincludedintheanaly- tablecontainsthearticleURLsandrevisionIDs23.Thetextof
sis.Toremoveirrelevantkeywordsfromthetext(e.g.,"use", thearticleswasdownloadedusingWikipedia’sexportpage24
"type", "number", "link") and map synonyms to one same which allows download of a specific set of articles in XML
keyword (e.g., "(UN) sustainable development goal(s)" or format.Thedateofthedownloadwas2021-12-28.Onlythe
"sdgs"weremappedto"sdg"),athesaurusfilewasused.The current revision (the most recent version) of the articles at
linkweightswerenormalizedusingtheco-occurrencecounts.
22https://www.vosviewer.com/getting-started
23https://en.wikipedia.org/wiki/Wikipedia:Revision_id
21https://www.vosviewer.com/ 24https://en.wikipedia.org/wiki/Special:Export
VOLUME11,2023 23
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2025.3595894
Gjorgjevikjetal.:BenchmarkingSentenceEncodersinAssociatingIndicatorswithSustainableDevelopmentGoalsandTargets
TABLE11. 18English-languageWikipediaarticlesandtheirrevisionIDsusedasdatasourceforthefine-tuningdatasets.
No. WikipediaarticleURL RevisionID
1 https://en.wikipedia.org/wiki/Sustainable_Development_Goal_1 1058009356
2 https://en.wikipedia.org/wiki/Sustainable_Development_Goal_2 1060913868
3 https://en.wikipedia.org/wiki/Sustainable_Development_Goal_3 1059877068
4 https://en.wikipedia.org/wiki/Sustainable_Development_Goal_4 1058007755
5 https://en.wikipedia.org/wiki/Sustainable_Development_Goal_5 1061200438
6 https://en.wikipedia.org/wiki/Sustainable_Development_Goal_6 1061708983
7 https://en.wikipedia.org/wiki/Sustainable_Development_Goal_7 1060845341
8 https://en.wikipedia.org/wiki/Sustainable_Development_Goal_8 1062437298
9 https://en.wikipedia.org/wiki/Sustainable_Development_Goal_9 1059594243
10 https://en.wikipedia.org/wiki/Sustainable_Development_Goal_10 1058008474
11 https://en.wikipedia.org/wiki/Sustainable_Development_Goal_11 1060946438
12 https://en.wikipedia.org/wiki/Sustainable_Development_Goal_12 1060940446
13 https://en.wikipedia.org/wiki/Sustainable_Development_Goal_13 1058011032
14 https://en.wikipedia.org/wiki/Sustainable_Development_Goal_14 1061877687
15 https://en.wikipedia.org/wiki/Sustainable_Development_Goal_15 1060901217
16 https://en.wikipedia.org/wiki/Sustainable_Development_Goal_16 1058009669
17 https://en.wikipedia.org/wiki/Sustainable_Development_Goal_17 1056725992
18 https://en.wikipedia.org/wiki/Sustainable_Development_Goals 1060949206
thespecifieddatewasdownloaded,withouttheirfullhistory [8] A. Huovila, P. Bosch, and M. Airaksinen, ‘‘Comparative analysis of
(all versions of the article). For details on Wikipedia article standardizedindicatorsforsmartsustainablecities:Whatindicatorsand
history,seeWikipediapagesonthetopic2526. standardstouseandwhen?’’Cities,vol.89,pp.141–153,2019.
[9] A. Merino-Saum, P. Halla, V. Superti, A. Boesch, and C. R. Binder,
‘‘Indicatorsforurbansustainability:Keylessonsfromasystematicanalysis
of67measurementinitiatives,’’EcologicalIndicators,vol.119,p.106879,
APPENDIXD
2020.
SELECTEDCHECKPOINTDETAILS
[10] A.Siragusa,I.Stamos,C.Bertozzi,andP.Proietti,‘‘Europeanhandbook
Thefine-tuningandtestconfigurationdetailsoftheselected forsdgvoluntarylocalreviews–2022edition.’’2022.
checkpointsreferencedinTables5,6,7,and8inSectionV-C [11] L.LellaandN.Oses-Eraso,‘‘Monitoringthesdgsatregionallevelineu.
regions2030pilotproject.finalreport.’’Stamos.I.,Manfredi,R.editor(s),
aregiveninTables12,13,14,and15,accordingly.Thefour
2023.
tablesgiveninthissectionareorganizedinthesamewayas
[12] UnitedNationsDevelopmentGroup,‘‘Localizingthepost-2015develop-
thetablesgiveninSectionV-C. mentagenda:Dialogsonimplementation.’’2014.
[13] A.Gjorgjevikj,K.Mishev,D.Trajanov,andL.Kocarev,‘‘Embed4sd,’’
https://github.com/gjorgjevik/embed4sd,2023.
ACKNOWLEDGMENT [14] A.Breuer,H.Janetschek,andD.Malerba,‘‘Translatingsustainabledevel-
TheworkofA.G.(inpart)wasdonewhenshewasPhDstu- opmentgoal(sdg)interdependenciesintopolicyadvice,’’Sustainability,
vol.11,no.7,p.2092,2019.
dentattheFacultyofComputerScienceandEngineering,Ss.
[15] UNDepartmentforSocialandEconomicAffairs(DESA),‘‘Handbookfor
CyrilandMethodiusUniversityinSkopje,NorthMacedonia.
thepreparationofvoluntarynationalreviews,2023edition,’’2022.
She is now with the Computer Systems Department, Jožef [16] United Cities and Local Governments (UCLG) and UN HABITAT,
StefanInstitute,Ljubljana,Slovenia. ‘‘Guidelinesforvoluntarylocalreviews,volume1,acomprehensiveanal-
ysisofexistingvlrs.’’2020.
[17] European Commission, ‘‘Sustainable development in european union.
REFERENCES monitoringreportontheprogresstowardsthesdgsinaneucontext.2023
edition.’’2023.
[1] United Nations General Assembly, ‘‘Transforming our world: the 2030
[18] A.Siragusa,P.Proietti,C.Bertozzi,E.CollAliaga,S.Foracchia,A.Irving,
agendaforsustainabledevelopment,’’A/RES/70/1,UnitedNations,2015.
S.Monni,M.PachecoOliveira,andR.Sisto,‘‘Buildingurbandatasetsfor
[2] ——, ‘‘Global indicator framework for the sustainable development
thesdgs.sixeuropeancitiesmonitoringthe2030agenda.’’Siragusa,A.
goals and targets of the 2030 agenda for sustainable development,’’
andProietti,P.andBertozzi,C.editor(s),2021.
A/RES/71/313,Annex,UnitedNations,2017.
[19] A. Siragusa, P. Vizcaino Maria, P. Proietti, and C. Lavalle, ‘‘European
[3] M. Nilsson, D. Griggs, and M. Visbeck, ‘‘Policy: map the interactions
handbookforsdgvoluntarylocalreviews,’’2020.
betweensustainabledevelopmentgoals,’’Nature,vol.534,no.7607,pp.
320–322,2016. [20] M.VegaRapun,I.Stamos,A.Siragusa,andP.Proietti,‘‘Regions2030–
europeanregionalsdgindicators.’’2022.
[4] M.Nilsson,E.Chisholm,D.Griggs,P.Howden-Chapman,D.McCollum,
P.Messerli,B.Neumann,A.-S.Stevance,M.Visbeck,andM.Stafford- [21] C.Yeh,C.Meng,S.Wang,A.Driscoll,E.Rozi,P.Liu,J.Lee,M.Burke,
Smith,‘‘Mappinginteractionsbetweenthesustainabledevelopmentgoals: D.B.Lobell,andS.Ermon,‘‘Sustainbench:Benchmarksformonitoring
lessonslearnedandwaysforward,’’Sustainabilityscience,vol.13,no.6, the sustainable development goals with machine learning,’’ in Thirty-
pp.1489–1503,2018. fifthConferenceonNeuralInformationProcessingSystemsDatasetsand
[5] T.Bennich,N.Weitz,andH.Carlsen,‘‘Decipheringthescientificliterature
BenchmarksTrack(Round2),2021.
onsdginteractions:Areviewandreadingguide,’’ScienceoftheTotal [22] R.Vinuesa,H.Azizpour,I.Leite,M.Balaam,V.Dignum,S.Domisch,
Environment,vol.728,p.138405,2020. A.Felländer,S.D.Langhans,M.Tegmark,andF.FusoNerini,‘‘Therole
[6] UnitedNations,‘‘Thesustainabledevelopmentgoalsreport2023,’’2023. ofartificialintelligenceinachievingthesustainabledevelopmentgoals,’’
[7] ——,‘‘Thesustainabledevelopmentgoalsreport2022,’’2022. Naturecommunications,vol.11,no.1,pp.1–10,2020.
[23] N.Tomašev,J.Cornebise,F.Hutter,S.Mohamed,A.Picciariello,B.Con-
nelly,D.C.Belgrave,D.Ezer,F.C.v.d.Haert,F.Mugishaetal.,‘‘Ai
25https://en.wikipedia.org/wiki/Help:Page_history forsocialgood:unlockingtheopportunityforpositiveimpact,’’Nature
26https://en.wikipedia.org/wiki/Help:Permanent_link Communications,vol.11,no.1,p.2468,2020.
24 VOLUME11,2023
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2025.3595894
Gjorgjevikjetal.:BenchmarkingSentenceEncodersinAssociatingIndicatorswithSustainableDevelopmentGoalsandTargets
TABLE12. Baselineandfine-tunedconfigurationsachievingthehighestresultintesttaskMC-IND-SDG(Table5).
|                      |     | TestDataset |               |              | Config.          | Fine-TuningConfig. | TestConfig. |
| -------------------- | --- | ----------- | ------------- | ------------ | ---------------- | ------------------ | ----------- |
| Dataset              |     |             | IndicatorRep. | Fine-Tuning  | Encoder          | Task K             | K           |
|                      |     |             |               | No(Baseline) | SBERT-MINILM-L12 | / /                | 14+n(Sl)∗6  |
| 2030AgendaIndicators |     |             | Title         |              |                  |                    |             |
|                      |     |             |               | Yes          | SBERT-MINILM-L12 | FT-SDG 22          | 22+n(Sl)∗17 |
|                      |     |             |               | No(Baseline) | SBERT-MINILM-L12 | / /                | 22+n(Sl)∗6  |
| EUSDGIndicators      |     |             | Title         |              |                  |                    |             |
|                      |     |             |               | Yes          | SBERT-MINILM-L12 | FT-SDG 22          | 14+n(Sl)∗6  |
EUSDGIndicators Title+Definition No(Baseline) SBERT-MINILM-L12 / / 22+n(Sl)∗6
|                  |     |     |                  | Yes          | SBERT-MINILM-L6  | FT-SDG 14 | 22+n(Sl)∗6 |
| ---------------- | --- | --- | ---------------- | ------------ | ---------------- | --------- | ---------- |
|                  |     |     |                  | No(Baseline) | SBERT-MINILM-L6  | / /       | 22+n(Sl)∗6 |
| WDISDGIndicators |     |     | Title            |              |                  |           |            |
|                  |     |     |                  | Yes          | SBERT-MINILM-L12 | FT-TRG 17 | 14+n(Sl)∗6 |
|                  |     |     |                  | No(Baseline) | SBERT-MINILM-L12 | / /       | 14+n(Sl)∗6 |
| WDISDGIndicators |     |     | Title+Definition |              |                  |           |            |
|                  |     |     |                  | Yes          | SBERT-MINILM-L6  | FT-SDG 14 | 14+n(Sl)∗6 |
EULocalSDGIndicators Title No(Baseline) SBERT-MINILM-L6 / / 22+n(Sl)∗6
|                         |     |     |                  | Yes          | SBERT-MINILM-L12 | FT-TRG 6  | 14+n(Sl)∗17 |
| ----------------------- | --- | --- | ---------------- | ------------ | ---------------- | --------- | ----------- |
|                         |     |     |                  | No(Baseline) | SBERT-MINILM-L12 | / /       | 14+n(Sl)∗17 |
| EULocalSDGIndicators    |     |     | Title+Definition |              |                  |           |             |
|                         |     |     |                  | Yes          | SBERT-MINILM-L12 | FT-SDG 14 | 22+n(Sl)∗17 |
|                         |     |     |                  | No(Baseline) | SBERT-MINILM-L6  | / /       | 14+n(Sl)∗6  |
| EURegionalSDGIndicators |     |     | Title            |              |                  |           |             |
|                         |     |     |                  | Yes          | SBERT-MINILM-L12 | FT-SDG 22 | 22+n(Sl)∗17 |
TABLE13. Baselineandfine-tunedconfigurationsachievingthehighestresultintesttaskMC-IND-TRG(Table6).
|                         |     | TestDataset |                  |              | Config.          | Fine-TuningConfig. | TestConfig. |
| ----------------------- | --- | ----------- | ---------------- | ------------ | ---------------- | ------------------ | ----------- |
| Dataset                 |     |             | IndicatorRep.    | Fine-Tuning  | Encoder          | Task K             | K           |
|                         |     |             |                  | No(Baseline) | SBERT-MINILM-L6  | / /                | 6           |
| 2030AgendaIndicators    |     |             | Title            |              |                  |                    |             |
|                         |     |             |                  | Yes          | SBERT-MINILM-L12 | FT-TRG 6           | 6           |
|                         |     |             |                  | No(Baseline) | SBERT-MINILM-L6  | / /                | 6           |
| WDISDGIndicators        |     |             | Title            |              |                  |                    |             |
|                         |     |             |                  | Yes          | SBERT-MINILM-L12 | FT-TRG 17          | 17          |
|                         |     |             |                  | No(Baseline) | SBERT-MINILM-L6  | / /                | 6           |
| WDISDGIndicators        |     |             | Title+Definition |              |                  |                    |             |
|                         |     |             |                  | Yes          | SBERT-MINILM-L6  | FT-TRG 6           | 6           |
|                         |     |             |                  | No(Baseline) | SBERT-MINILM-L12 | / /                | 17          |
| EULocalSDGIndicators    |     |             | Title            |              |                  |                    |             |
|                         |     |             |                  | Yes          | SBERT-MINILM-L12 | FT-SDG 14          | 6           |
|                         |     |             |                  | No(Baseline) | SBERT-MINILM-L6  | / /                | 6           |
| EULocalSDGIndicators    |     |             | Title+Definition |              |                  |                    |             |
|                         |     |             |                  | Yes          | SBERT-MINILM-L6  | FT-SDG 14          | 17          |
|                         |     |             |                  | No(Baseline) | SBERT-MINILM-L6  | / /                | 6           |
| EURegionalSDGIndicators |     |             | Title            |              |                  |                    |             |
|                         |     |             |                  | Yes          | SBERT-MINILM-L6  | FT-SDG 14          | 6           |
TABLE14. Baselineandfine-tunedconfigurationsachievingthehighestresultintesttaskML-IND-SDG(Table7).
|                      |     | TestDataset |               |              | Config.          | Fine-TuningConfig. | TestConfig. |
| -------------------- | --- | ----------- | ------------- | ------------ | ---------------- | ------------------ | ----------- |
| Dataset              |     |             | IndicatorRep. | Fine-Tuning  | Encoder          | Task K             | K           |
|                      |     |             |               | No(Baseline) | SBERT-MINILM-L12 | / /                | 14+n(Sl)∗6  |
| 2030AgendaIndicators |     |             | Title         |              |                  |                    |             |
|                      |     |             |               | Yes          | SBERT-MINILM-L12 | FT-SDG 22          | 14+n(Sl)∗6  |
|                      |     |             |               | No(Baseline) | SBERT-MINILM-L12 | / /                | 22+n(Sl)∗6  |
| EUSDGIndicators      |     |             | Title         |              |                  |                    |             |
|                      |     |             |               | Yes          | SBERT-MINILM-L12 | FT-SDG 14          | 14+n(Sl)∗6  |
|                      |     |             |               | No(Baseline) | SBERT-MINILM-L6  | / /                | 14+n(Sl)∗6  |
EUSDGIndicators Title+Definition Yes SBERT-MINILM-L12 FT-SDG 14 14+n(Sl)∗6
|                      |     |     |                  | No(Baseline) | SBERT-MINILM-L12 | / /       | 14+n(Sl)∗17 |
| -------------------- | --- | --- | ---------------- | ------------ | ---------------- | --------- | ----------- |
| EULocalSDGIndicators |     |     | Title            |              |                  |           |             |
|                      |     |     |                  | Yes          | SBERT-MINILM-L12 | FT-SDG 14 | 14+n(Sl)∗17 |
|                      |     |     |                  | No(Baseline) | SBERT-MINILM-L12 | / /       | 22+n(Sl)∗6  |
| EULocalSDGIndicators |     |     | Title+Definition |              |                  |           |             |
|                      |     |     |                  | Yes          | SBERT-MINILM-L6  | FT-SDG 14 | 22+n(Sl)∗17 |
TABLE15. Baselineandfine-tunedconfigurationsachievingthehighestresultintesttaskML-SDG-SDG(Table8).
|                |     | Dataset |               |              | Config.          | Fine-TuningConfig. | TestConfig. |
| -------------- | --- | ------- | ------------- | ------------ | ---------------- | ------------------ | ----------- |
| TestDataset    |     |         | IndicatorRep. | Fine-Tuning  | Encoder          | Task K             | K           |
|                |     |         |               | No(Baseline) | SBERT-MINILM-L12 | / /                | 14+n(Sl)∗6  |
| SDGRelatedness |     |         | Title         |              |                  |                    |             |
|                |     |         |               | Yes          | SBERT-MINILM-L12 | FT-SDG 22          | 14+n(Sl)∗6  |
[24] M.Soriano,R.Berlanga,andI.Lanza-Cruz,‘‘Ontheproblemofautomat- [26] Y.Li,V.F.Frans,Y.Song,M.Cai,Y.Zhang,andJ.Liu,‘‘Sdgdetector:
icallyaligningindicatorstosdgs,’’inEuropeanSemanticWebConference. an r-based text mining tool for quantifying efforts toward sustainable
Springer,2023,pp.138–142. developmentgoals,’’JournalofOpenSourceSoftware,vol.8,no.84,p.
5124,2023.
| [25] T. Matsui, | K. Suzuki, | K. Ando, Y. Kitai, | C. Haga, N. Masuhara, | and |     |     |     |
| --------------- | ---------- | ------------------ | --------------------- | --- | --- | --- | --- |
S.Kawakubo,‘‘Anaturallanguageprocessingmodelforsupportingsus- [27] F. Sovrano, M. Palmirani, and F. Vitali, ‘‘Deep learning based multi-
tainabledevelopmentgoals:translatingsemantics,visualizingnexus,and labeltextclassificationofungaresolutions,’’inProceedingsofthe13th
connectingstakeholders,’’SustainabilityScience,vol.17,no.3,pp.969– internationalconferenceontheoryandpracticeofelectronicgovernance,
| 985,2022. |     |     |     |     | 2020,pp.686–695. |     |     |
| --------- | --- | --- | --- | --- | ---------------- | --- | --- |
VOLUME11,2023 25
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2025.3595894
Gjorgjevikjetal.:BenchmarkingSentenceEncodersinAssociatingIndicatorswithSustainableDevelopmentGoalsandTargets
[28] D. S. Meier, R. Mata, and D. U. Wulff, ‘‘text2sdg: An r package [50] R.C.Morales-Hernández,J.G.Jagüey,andD.Becerra-Alonso,‘‘Acom-
to monitor sustainable development goals from text,’’ arXiv preprint parisonofmulti-labeltextclassificationmodelsinresearcharticleslabeled
arXiv:2110.05856,2021. withsustainabledevelopmentgoals,’’IEEEAccess,vol.10,pp.123534–
[29] D.U.Wulff,D.S.Meier,andR.Mata,‘‘Usingnoveldataandensemble 123548,2022.
modelstoimproveautomatedlabelingofsustainabledevelopmentgoals,’’ [51] P.Nedungadi,S.Surendran,K.-Y.Tang,andR.Raman,‘‘Bigdataandai
arXivpreprintarXiv:2301.11353,2023. algorithmsforsustainabledevelopmentgoals:Atopicmodelinganalysis,’’
[30] A. Hajikhani and C. Cole, ‘‘A critical review of large language mod- IEEEAccess,2024.
els:Sensitivity,bias,andthepathtowardspecializedai,’’arXivpreprint [52] N.VanEckandL.Waltman,‘‘Softwaresurvey:Vosviewer,acomputer
arXiv:2307.15425,2023. programforbibliometricmapping,’’Sientometrics,vol.84,no.2,pp.523–
[31] Q. Le and T. Mikolov, ‘‘Distributed representations of sentences and 538,2009.
documents,’’inInternationalConferenceonMachineLearning,2014,pp. [53] A. Gjorgjevikj, ‘‘Knowledge transfer in deep learning with small text
1188–1196. datasets,’’Ph.D.dissertation,FacultyofComputerScienceandEngineer-
[32] L.Pukelis,N.B.Puig,M.Skrynik,andV.Stanciauskas,‘‘Osdg–open- ing,Ss.CyrilandMethodiusUniversityinSkopje,Skopje,NorthMacedo-
sourceapproachtoclassifytextdatabyunsustainabledevelopmentgoals nia,2023.
(sdgs),’’arXivpreprintarXiv:2005.14569,2020. [54] E.HofferandN.Ailon,‘‘Deepmetriclearningusingtripletnetwork,’’in
[33] L. Pukelis, N. Bautista-Puig, G. Statulevičiu¯te˙, V. Stančiauskas, Internationalworkshoponsimilarity-basedpatternrecognition. Springer,
G. Dikmener, and D. Akylbekova, ‘‘Osdg 2.0: a multilingual tool 2015,pp.84–92.
for classifying text data by un sustainable development goals (sdgs),’’ [55] J.Devlin,M.-W.Chang,K.Lee,andK.Toutanova,‘‘Bert:Pre-training
arXivpreprintarXiv:2211.11252,2022. of deep bidirectional transformers for language understanding,’’ arXiv
[34] M.Angin,B.Taşdemir,C.A.Yılmaz,G.Demiralp,M.Atay,P.Angin, preprintarXiv:1810.04805,2018.
andG.Dikmener,‘‘Arobertaapproachforautomatedprocessingofsus- [56] Y.Liu,M.Ott,N.Goyal,J.Du,M.Joshi,D.Chen,O.Levy,M.Lewis,
tainabilityreports,’’Sustainability,vol.14,no.23,p.16139,2022. L. Zettlemoyer, and V. Stoyanov, ‘‘Roberta: A robustly optimized bert
[35] D.F.Hsu,M.T.LaFleur,andI.Orazbek,‘‘Improvingsdgclassification pretrainingapproach,’’arXivpreprintarXiv:1907.11692,2019.
precisionusingcombinatorialfusion,’’Sensors,vol.22,no.3,p.1067, [57] C.Raffel,N.Shazeer,A.Roberts,K.Lee,S.Narang,M.Matena,Y.Zhou,
2022. W.Li,P.J.Liuetal.,‘‘Exploringthelimitsoftransferlearningwitha
[36] L.M.Fonseca,J.P.Domingues,andA.M.Dima,‘‘Mappingthesustain- unifiedtext-to-texttransformer.’’J.Mach.Learn.Res.,vol.21,no.140,
abledevelopmentgoalsrelationships,’’Sustainability,vol.12,no.8,p. pp.1–67,2020.
3359,2020. [58] N.ReimersandI.Gurevych,‘‘Sentence-bert:Sentenceembeddingsusing
[37] J.E.Guisiano,R.Chiky,andJ.DeMello,‘‘Sdg-meter:Adeeplearning siamesebert-networks,’’arXivpreprintarXiv:1908.10084,2019.
basedtoolforautomatictextclassificationofthesustainabledevelopment [59] T.Gao,X.Yao,andD.Chen,‘‘Simcse:Simplecontrastivelearningof
goals,’’ in Asian Conference on Intelligent Information and Database sentenceembeddings,’’arXivpreprintarXiv:2104.08821,2021.
Systems. Springer,2022,pp.259–271. [60] J.Ni,G.H.Ábrego,N.Constant,J.Ma,K.B.Hall,D.Cer,andY.Yang,
[38] T.B.Smith,R.Vacca,L.Mantegazza,andI.Capua,‘‘Naturallanguage ‘‘Sentence-t5: Scalable sentence encoders from pre-trained text-to-text
processingandnetworkanalysisprovidenovelinsightsonpolicyandsci- models,’’arXivpreprintarXiv:2108.08877,2021.
entificdiscoursearoundsustainabledevelopmentgoals,’’Scientificreports, [61] F.Schroff,D.Kalenichenko,andJ.Philbin,‘‘Facenet:Aunifiedembed-
vol.11,no.1,pp.1–10,2021. ding for face recognition and clustering,’’ in Proceedings of the IEEE
[39] E.Fotopoulou,I.Mandilara,A.Zafeiropoulos,C.Laspidou,G.Adamos, conferenceoncomputervisionandpatternrecognition,2015,pp.815–823.
P.Koundouri,andS.Papavassiliou,‘‘Sustaingraph:Aknowledgegraphfor [62] A.Hermans,L.Beyer,andB.Leibe,‘‘Indefenseofthetripletlossfor
trackingtheprogressandtheinterlinkingamongthesustainabledevelop- personre-identification,’’arXivpreprintarXiv:1703.07737,2017.
mentgoals’targets,’’FrontiersinEnvironmentalScience,vol.10,p.2175, [63] S.M.LundbergandS.-I.Lee,‘‘Aunifiedapproachtointerpretingmodel
2022. predictions,’’Advancesinneuralinformationprocessingsystems,vol.30,
[40] P.Mishra,S.K.Narayanasamy,andK.Srinivasan,‘‘Context-awareembed- 2017.
dedlanguagetransformersforevaluatingclimatechangebasedsustainable [64] H.Chen,J.D.Janizek,S.Lundberg,andS.-I.Lee,‘‘Truetothemodelor
developmentgoals,’’IEEEAccess,2025. truetothedata?’’arXivpreprintarXiv:2006.16234,2020.
[41] H. Cho and E. Ackom, ‘‘Artificial intelligence (ai)-driven approach to [65] M.Ester,H.-P.Kriegel,J.Sander,X.Xuetal.,‘‘Adensity-basedalgorithm
climate action and sustainable development,’’ Nature Communications, for discovering clusters in large spatial databases with noise.’’ in Kdd,
vol.16,no.1,p.1228,2025. vol.96,no.34,1996,pp.226–231.
[42] P.Koundouri,A.Alamanos,A.Plataniotis,C.Stavridis,K.Perifanos,and [66] D.Cer,Y.Yang,S.-y.Kong,N.Hua,N.Limtiaco,R.S.John,N.Con-
S.Devves,‘‘Assessingthesustainabilityoftheeuropeangreendealandits stant,M.Guajardo-Cespedes,S.Yuan,C.Taretal.,‘‘Universalsentence
interlinkageswiththesdgs,’’NpjClimateAction,vol.3,no.1,p.23,2024. encoder,’’arXivpreprintarXiv:1803.11175,2018.
[43] W.Benjira,F.Atigui,B.Bucher,M.Grim-Yefsah,andN.Travers,‘‘Auto- [67] Y.Yang,D.Cer,A.Ahmad,M.Guo,J.Law,N.Constant,G.H.Abrego,
matedmappingbetweensdgindicatorsandopendata:Anllm-augmented S.Yuan,C.Tar,Y.-H.Sungetal.,‘‘Multilingualuniversalsentenceencoder
knowledgegraphapproach,’’Data&KnowledgeEngineering,vol.156,p. forsemanticretrieval,’’arXivpreprintarXiv:1907.04307,2019.
102405,2025. [68] W.Wang,F.Wei,L.Dong,H.Bao,N.Yang,andM.Zhou,‘‘Minilm:
[44] F.Larosa,S.Hoyas,H.A.Conejero,J.Garcia-Martinez,F.F.Nerini,and Deep self-attention distillation for task-agnostic compression of pre-
R.Vinuesa,‘‘Largelanguagemodelsinclimateandsustainabilitypolicy: trainedtransformers,’’AdvancesinNeuralInformationProcessingSys-
limitsandopportunities,’’arXivpreprintarXiv:2502.02191,2025. tems,vol.33,pp.5776–5788,2020.
[45] P.Koundouri,P.-S.Aslanidis,K.Dellis,A.Plataniotis,andG.Feretzakis, [69] V. Sanh, L. Debut, J. Chaumond, and T. Wolf, ‘‘Distilbert, a distilled
‘‘Mappinghumansecuritystrategiestosustainabledevelopmentgoals:a version of bert: smaller, faster, cheaper and lighter,’’ arXiv preprint
machinelearningapproach,’’DiscoverSustainability,vol.6,no.1,p.96, arXiv:1910.01108,2019.
2025. [70] K. Song, X. Tan, T. Qin, J. Lu, and T.-Y. Liu, ‘‘Mpnet: Masked and
[46] C. Li, Z. Chen, Q. Jiang, M. Yue, L. Wu, Y. Bao, B. Huang, A. B. permutedpre-trainingforlanguageunderstanding,’’AdvancesinNeural
Wang,Y.Tan,andZ.Xu,‘‘Impactsofgovernmentattentiononachieving InformationProcessingSystems,vol.33,pp.16857–16867,2020.
sustainable development goals: evidence from china,’’ Geography and [71] N.Muennighoff,N.Tazi,L.Magne,andN.Reimers,‘‘Mteb:Massivetext
Sustainability,vol.6,no.2,p.100233,2025. embeddingbenchmark,’’arXivpreprintarXiv:2210.07316,2022.
[47] N.StrelkovskiiandN.Komendantova,‘‘Integrationofunsustainablede-
velopmentgoalsinnationalhydrogenstrategies:Atextanalysisapproach,’’
InternationalJournalofHydrogenEnergy,vol.102,pp.1282–1294,2025.
[48] S.Borchardt,V.G.Barbero,D.Buscaglia,M.Maroni,L.Marellietal.,
‘‘Mappingeupolicieswiththe2030agendaandsdgs–fosteringpolicy
coherencethroughtext-basedsdgmapping,’’2023.
[49] R.Raman,P.Singh,V.K.Singh,R.Vinuesa,andP.Nedungadi,‘‘Under-
standingthebibliometricpatternsofpublicationsinieeeaccess,’’IEEE
Access,vol.10,pp.35561–35577,2022.
26 VOLUME11,2023
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2025.3595894
Gjorgjevikjetal.:BenchmarkingSentenceEncodersinAssociatingIndicatorswithSustainableDevelopmentGoalsandTargets
ANAGJORGJEVIKJreceivedthemaster’sdegree LJUPCO KOCAREV (Fellow,IEEE) iscurrently
incomputernetworksande-technologiesandthe a Member of the Macedonian Academy of Sci-
Ph.D. degree in computer science and engineer- encesandArts,aFullProfessorwiththeFaculty
ing from Ss. Cyril and Methodius University in of ComputerScience andEngineering, Ss. Cyril
Skopje,in2014and2023,respectively,withapar- andMethodiusUniversity,Skopje,Macedonia,the
ticularfocusonnaturallanguageprocessingand DirectoroftheResearchCenterforComputerSci-
machinelearning.Sheisapostdoctoralresearcher enceandInformationTechnologies,Macedonian
atJožefStefanInstituteinLjubljana,Sloveniaand Academy,andaResearchProfessorwiththeUni-
wasawardedaHorizonEuropeMSCAPostdoc- versityofCaliforniaatSanDiego.Hisworkhas
toral Fellowship in the 2024 call. She also has been supported by the Macedonian Ministry of
12 years of professional experience as a software engineer. Her research Education and Science, the Macedonian Academy of Sciences and Arts,
interestsincludedatascience,machinelearning,naturallanguageprocessing, NSF,AFOSR,DoE,ONR,ONRGlobal,NIH,STMicroelectronics,NATO,
representationlearning,multi-tasklearning,andmeta-learning. TEMPUS,FP6,FP7,Horizon2020,andagenciesfromSpain,Italy,Germany
(DAADandDFG),HongKong,andHungary.Hisresearchinterestsinclude
networks,nonlinearsystemsandcircuits,dynamicalsystemsandmathemat-
icalmodeling,machinelearning,andcomputationalbiology.
KOSTADINMISHEVreceivedthemaster’sdegree
incomputernetworksande-technologiesandthe
|     | Ph.D | degree   | in computer | science   | and        | engineer- |
| --- | ---- | -------- | ----------- | --------- | ---------- | --------- |
|     | ing  | from Ss. | Cyril and   | Methodius | University | in        |
Skopje,in2016and2023,respectively.Heisan
|     | Assistant | Professor | at  | the Faculty | of  | Computer |
| --- | --------- | --------- | --- | ----------- | --- | -------- |
ScienceandEngineering,Ss.CyrilandMethodius
UniversityinSkopje.Hisresearchinterestsinclude
datascience,semanticweb,naturallanguagepro-
cessing,enterpriseapplicationarchitectures,web
technologies,andcomputernetworks.
DIMITARTRAJANOV(Member,IEEE)received
thePh.D.degreeincomputerscience.FromMarch
|     | 2011         | to September | 2015,   | he          | was the | Founding    |
| --- | ------------ | ------------ | ------- | ----------- | ------- | ----------- |
|     | Dean         | of the       | Faculty | of Computer | Science | and         |
|     | Engineering, |              | and in  | his tenure, | the     | faculty be- |
camethelargesttechnicalfacultyinMacedonia.
HeiscurrentlyaFullProfessorwiththeFaculty
|     | of ComputerScience |     |     | and Engineering,Ss. |     | Cyril |
| --- | ------------------ | --- | --- | ------------------- | --- | ----- |
andMethodiusUniversityinSkopje,andaVisiting
ResearchProfessorwithBostonUniversity.Heis
| the Leader       | of the Regional Social | Innovation |             | Hub, established |                  | in 2013, |
| ---------------- | ---------------------- | ---------- | ----------- | ---------------- | ---------------- | -------- |
| as a cooperation | between UNDP           | and        | the Faculty | of               | Computer         | Science  |
| and Engineering. | He is the author       | of         | more than   | 200              | journal articles | and      |
conferencepapers,andsevenbooks.Hehasbeeninvolvedinmorethan70
researchandindustryprojects,ofwhichmorethan40projectsasaProject
Leader.Hisresearchinterestsincludedatascience,machinelearning,NLP,
FinTech,semanticweb,e-commerce,technologyfordevelopment,ESG,and
climatechange.
VOLUME11,2023 27
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/
