Received:7November2022 Revised:9May2023 Accepted:19July2023
DOI:10.1002/sd.2706
RESEARCH ARTICLE
Artificial intelligence for Sustainable Development Goals:
Bibliometric patterns and concept evolution trajectories
Aakash Singh1 | Anurag Kanaujia1 | Vivek Kumar Singh1 | Ricardo Vinuesa2
1DepartmentofComputerScience,Banaras
HinduUniversity,Varanasi,India Abstract
2FLOW,EngineeringMechanics,KTHRoyal The development of artificial intelligence (AI) as a field has impacted almost all
InstituteofTechnology,Stockholm,Sweden
aspectsofhumanlife.Morerecentlyithasfoundaroleinaddressingdevelopmental
Correspondence challenges, specifically the Sustainable Development Goals (SDGs). However, there
VivekKumarSingh,DepartmentofComputer
arenotenoughsystematicstudiesonanalysisoftheroleofAIresearchtowardsthe
Science,BanarasHinduUniversity,Varanasi
221005,India. SDGs.Therefore,thisarticleattemptstobridgethisgapbyidentifyingthemajorbib-
Email:vivek@bhu.ac.in
liometric trends and concept-evolutiontrajectories in the area of AI applications for
RicardoVinuesa,FLOW,Engineering
sustainable-developmentgoals.Theresearchpublicationdataforthelast20yearsin
Mechanics,KTHRoyalInstituteofTechnology,
StockholmSE-10044,Sweden. the areas of artificial intelligence, machine learning, deep learning, and so forth, is
Email:rvinuesa@mech.kth.se
obtained and computationally analysed using a framework comprising bibliometrics,
Fundinginformation pathanalysisandcontentanalysis.Thefindingsshowanincrementaltrendinoverall
HPEArubaCentreforResearchinInformation
publications on the application of AI for SDGs across the different regions of the
Systems,Grant/AwardNumber:M-22-69;
ScienceandEngineeringResearchBoard, world. SDGs 3 (good health & well-being) and 7 (affordable and clean energy) are
Grant/AwardNumber:MTR/2020/000625
found as the areas with the most applications of AI. In SDG3, the literature reflects
[Correctionaddedon3August2023,after application of AI techniques such as deep learning for precision and personalised
firstonlinepublication:Correspondingauthor's
medicine while in SDG7, a number of studies have employed AI techniques for the
e-mailaddresshasbeencorrectedinthis
version.] integration of systems for efficient generation of solar power and improving the
energyefficiencyofabuilding.Furthermore,SDG4(qualityeducation),SDG13(cli-
mateaction),SDG11(sustainablecitiesandcommunities)andSDG16(peace,justice
andstronginstitutions)aretheotherSDGswhereAIapproachesandtechniquesare
applied. The analytical results present a detailed insight of application of AI for
achievingtheSDGs.
KEYWORDS
artificialintelligence(AI),bibliometrics,pathanalysis,SustainableDevelopmentGoals(SDGs)
1 | INTRODUCTION AI broadly refers to the design of intelligent machines that enable
high-levelcognitiveprocesseslikethinking,perceiving,learning,prob-
The development of artificial intelligence (AI) as a field has been all lemsolvinganddecisionmaking.Thisfieldhasgainedbroaderatten-
encompassing.Ithasimpactedalmostallaspectsofhumanlife,made tion with significant advances in data collection and aggregation,
possible unprecedented developments in areas of communication, analytics and availability of suitable computer processing power
medicine,engineering,sustainability,andsoforth,(Allenetal.,2020). (National Stratregy for Artificial Intelligence, 2018). AI has not
ThisisanopenaccessarticleunderthetermsoftheCreativeCommonsAttributionLicense,whichpermitsuse,distributionandreproductioninanymedium,
providedtheoriginalworkisproperlycited.
©2023TheAuthors.SustainableDevelopmentpublishedbyERPEnvironmentandJohnWiley&SonsLtd.
724 wileyonlinelibrary.com/journal/sd SustainableDevelopment.2024;32:724–754.

SINGHETAL. 725
only attracted the attention of the academic research community etal.,2020).Inthisregard,theSDGsareanareawherepracticalappli-
but also has become a focus area for technology and service cations of AI technology have grown rapidly (Goralski & Tan, 2020;
companies, playing a major role in the Fourth Industrial Revolution Vinuesaetal.,2020).ThoughAIapplicationsinachievingSDGtargets
(Moavenzadeh,2015).AIsystemscanhelppeopleacquirenewskills, arenowbeingrecognised,notmuchisknownaboutthequantumof
democratiseservices,designanddeliverfasterproductiontimesand research on AI for SDGs, the major focus areas of AI for SDGs, the
quickeriterationcycles,reduceenergyusage,providereal-timeenvi- prominentAItechniquesandmethodsbeingappliedtoSDGs,andso
ronmentalmonitoringforpollutionandairquality,enhancecyberse- forth. Therefore, there exists a research gap in terms of in-depth
curitydefences,reducehealthcareinefficiencies,createnewkindsof knowledgeaboutapplicationsofAIforSDGs.Thishasmotivatedus
recreationalexperiences,andimprovereal-timetranslationservicesto toundertakethisstudy.Thisarticleattemptstoaddressthisresearch
connect people around the world. Looking at the wide applicability gapbyusinganalyticalmethodsfrombibliometricsandcontentanaly-
and impact of AI, several national governments have opted to pro- sis. More specifically the article attempts to answer the following
moteandregulateAIadoptioninvarioussectors(Baumetal.,2023), researchquestions.
through national plans and strategies. For instance, UK (National AI
Strategy1),Japan(AIStrategy2019&IntegratedInnovationStrategy RQ1. What quantum of AI research, and from which
20202), China (New Generation AI Development Plan for 20303), regionsoftheworld,isfocusedonSDGs?
India (National Strategy for Artificial Intelligence (NSAI)), UAE (UAE
Strategy for Artificial Intelligence (AI)4), South Korea (Toward AI RQ2. Whether different SDGs attract differential
World Leader beyond IT5), Canada (Pan-Canadian AI Strategy6), and attentionfromAIresearchers,asmeasuredintermsof
soforth.aresomeofthecountrieswhichhaveledtheefforttowards publicationandcitationactivity?
developmentofsystematicplansforthewideradoptionofAIingov-
ernanceandothersectors. RQ3. Whatarethemajorthematic evolutiontrajecto-
TheSustainableDevelopmentGoals(SDGs)areasetof17guiding riesinAIresearchforSDGs?
targets adopted by United Nation, each focusing on an aspect of
human development and sustainability of ecosystems. The constitu- RQ4. Which prominent AI methods and models have
tionandadoptionofthesegoalssignifiesauniversalcalltoactionto beenappliedtoachievedifferentSDGtargets?
address the urgent environmental, political and economic challenges
being faced by the world (UNGA, 20157; United Nations, 20208). Inordertoanswerthesequestions,theresearchpublicationsdata
TheseSDGshaveplayedanimportantroleinpromotingresearchand on AI for SDGs has been explored and analysed using Bibliometric
developmentinnoveltechnologiessincetheiradoptionbytheUnited analysis,PathanalysisandContentanalysis.BibliometricAnalysisisa
Nations in 2015. As an activity, sustainable development has been method, which is applied to explore large amount of literature and
definedas‘developmentthatmeetstheneedsofthepresentwithout present an all-encompassing review of the literature (Donthu
compromising the ability of future generations to meet their own etal.,2021).Itidentifiesmajorbibliometrictrendssuchasmostinflu-
needs’.Itcallsforconcertedeffortstowardsbuildinganinclusive,sus- ential publications, authors, subdomains, and so forth, (Farrukh
tainableandresilientfutureforthepeopleandtheplanet(Brundtland et al., 2020; Kumar et al., 2021). However, a major criticism of this
Commission, 19879). In order to make considerable progress in method is that it often ignores more detailed trends. Therefore, to
achievingthetargetsofSDGs,theroleofscienceandtechnologywill uncovermoremeaningfulinformationaboutresearchgrowthandthe-
becentral. matic structure of the research area, methods of Path Analysis and
AI hasemerged as a transformative technology that holds great Content Analysis have been used. Path Analysis involves exploring
promise in economic, social, medical, security, and environmental the major knowledge flow paths through tracing the citations of
applications, including some of the major important concerns of the importantpublications(Lathabaietal.,2018;Liu&Lu,2012).Content
currentcenturyincludedundertheSDGs.TheapplicationsofAIhave Analysis utilises the insights from the path analysis and involves in
helped in addressing developmental challenges, specifically sustain- depth review of most important publications identified during the
able development has received attention in recent times (Vinuesa path analysis. The methodology have been described further in
thedataandmethodssection.
1NationalAIStrategy–https://www.gov.uk/government/organisations/office-for-artificial-
intelligence.
2AIStrategy2019&IntegratedInnovationStrategy2020–https://www.meti.go.jp/press/ 1.1 | Majorcontributions
2020/01/20210115003/20210115003-3.pdf.
3NewGenerationAIDevelopmentPlanfor2030–https://www.theconstructsim.com/98-
chinas-ai-plan-for-2030/. This study attempts to address the research gap on more detailed
4UAEStrategyforArtificialIntelligence(AI)–https://ai.gov.ae/.
informationonAIapplicationsforSDGS.Thisstudyisamongthefirst
5TowardsAIWorldLeaderbeyondIT–https://oecd.ai/dashboards/countries/SouthKorea.
6Pan-CanadianAIStrategy–https://cifar.ca/ai/. ofitskindandmakesfollowingmajorcontributions.Itquantifiesthe
7https://upload.wikimedia.org/wikipedia/commons/d/d5/N1529189.pdf. total research activity on AI for SDGs from different parts of
8https://sdgs.un.org/publications/sustainable-development-goals-report-2020-24686.
9https://sustainabledevelopment.un.org/content/documents/5987our-common-future.pdf. theworld,howhasitchangedovertime,whichregionsoftheworld
10991719,
2024,
1, Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1002/sd.2706
by
NICE,
National
Institute
for
Health
and
Care
Excellence,
Wiley
Online
Library
on
[29/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

726 SINGHETAL.
areworkingtowardsAIapplicationstoSDGsandhowdotheycollab- TheyhavecomparedAItoadouble-edgedsword,whichmustbeused
orate with each other for this purpose. In addition, the knowledge carefully by the relevant stakeholders. This is particularly relevant
flows in AI research for SDGs has been explored to identify major whenusingAIforsustainabilityapplications,whichrequiresthedevel-
application areas along with AI methods and models applied to opment of interpretable models (Vinuesa & Sirmacek, 2021), or in
address different SDG targets. Thus, the study provides a detailed complex social contexts such as that of pandemics (Vinuesa
insight into applications of AI research for SDGs by underlining its et al., 2020b). Some region-specific study has looked at the
application areas, major themes, most important SDG targets, and relationship between AI and sustainable development in China
majormethodsandmodelsapplied. (Liengpunsakul,2021)andinIndia(Singhetal.,2022).Thesestudies
haveusedapproachesfavouringaqualitativeanalysisofavailablesub-
jectexpertiseandliterature,andwecouldfindonlyafewveryrecent
1.2 | Organisationofthepaper previousarticlesonquantitativeanalysis,namely,Wambaetal.,2021
and Liu et al., 2023. A new platform named AI4SDGs Think Tank10
Thisarticleisorganisedasfollows.TheexplanationofAI,itsimpacts, hasstartedwhichevaluatesAIprojectsfortheirpositiveornegative
SDGs, their connection with technology, and research questions for impactonSDGs.
this study are listed in the introduction section. Section 2 surveys Thereare,however,nosignificantaccountsofavailableliterature
some related work on the theme. The data and methodology are onthetopicofAIforSDGs,intermsofthequantumofresearchon
detailedinSection3.Section4withdescriptiveresultspresentsthe AIforSDGs,themajorfocusareasofAIforSDGs,theprominentAI
observations from bibliometric path analysis and content analysis. techniquesandmethodsbeingappliedtoSDGs,andsoforth.There-
Section5ofthearticlepresentsin-depthdiscussiononthemainfind- fore,thereexistsaresearchgapintermsofin-depthknowledgeabout
ingsincludingSDGwisesummariesofresearchtrendsinAIresearch applications of AI for SDGs. This article attempts to address this
for SDGs. The practical implications of study are highlighted in sec- research gap by using analytical methods from bibliometrics, path
tion6.Theconclusionsectionofthearticleunderlinestherelevance analysisandcontentanalysis.
of the findings and suggests possible future work related to this
study.
3 | DATA AND METHODOLOGY
2 | RELATED WORK The study is based upon the publication metadata catalogued in
Dimensions11databasefrom2001to2020.Dimensionsdatabasepro-
Theresearchcommunityhasrecentlystartedtoexploretheapplica- vides an automated classification of publications into various SDGs.
tions of AI in SDGs, and this new confluence of two areas has Thepublicationmetadatawasaccessedbythemeansofadedicated
emerged. Among these studies the common theme relates to: APIgrantedfromthedatabase.Thequerytoobtainthedatawasas
(a)evaluatingtheimpactofexistingtechniquesofAIonachievement follows:
of SDGs, and (b)regulating theapplicationof AIon SDGs. Early on,
Chuietal.(2018)lookedattheroleofAIforsocialgoodbycompiling 'search publications in title_abstract_only for
about160caseswhereAIhadmadeasocial-impact.Whiletheimpact "n"Artificialintelligencen"ORn"machinelearningn"OR
ofAIonindividualareasofsustainabilityhavebeenstudiedbyseveral n"Deep learningn"" where category_sdg in ["40001",
others, the other notable study covering all SDGs was reported by "40002", "40003", "40004", "40005", "40006",
Vinuesa et al. (2020). It used an expert-elicitation approach to esti- "40007", "40008", "40009", "40010", "40011",
matetheroleofAIinachievingtheSDGsandsuggestedthatAIcan "40012", "40013", "40014", "40015", "40016",
enable the accomplishment of 134 targets, while it may also inhibit "40017"] and year = '+year+' and type = "article"
theprogresson59targets.Incontrast,Yehetal.(2021),conducteda return publications [id + doi + title + abstract +
public perception survey about the connection between the two category_for + category_sdg + authors + authors_
areas. AnothersuchstudycategorisesSDGsinto five groupson the count+journal+year+type+issn+research_orgs
basisofthetypeofimpactofAIonthem(Sætra,2021).Itspecifically + research_org_countries + concepts + concepts_
brings forth the potential negative impacts of AI which could result scores + times_cited+ funders + funder_countries +
fromthedominanceoflargefirmsandselectednationsonthegver- referenced_pubs + publisher + researchers +date +
nancestructureofAIapplications.Guptaetal.(2021)haveconducted pages+open_access_categories_v2]'
amoredetailedstudyofAIapplicationsatanSDGindicatorlevel.
AnotherstudyhasexploredtheimpactofAIresearchondifferent Thisqueryyieldedatotalof20,511documentswhichwerethen
domains where AI applications can facilitate social good (Wamba importedtotheworkingdatabase.Dimensionsdatabasewaschosen
etal.,2021).GoralskiandTan(2020)havelookedatthreecasestud-
ies(water,agricultureandsanitation&health)ontheapplicationsof
10https://ai-for-sdgs.academy/about.
AI to improve the efficiency and efficacy of resource management. 11Dimensionsdatabaseisavailableatwww.dimensions.ai.
10991719,
2024,
1, Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1002/sd.2706
by
NICE,
National
Institute
for
Health
and
Care
Excellence,
Wiley
Online
Library
on
[29/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

SINGHETAL. 727
over otheravailable databases considering its widercoverage (Singh throughpublicationdetailsandcitedreferenceinformation.Thisnet-
etal.,2021)anditsautomatedclassificationofpublicationsintovari- work is further analysed using the approach described by Lathabai
ous SDGs. The metadata downloaded consisted of twenty-five etal.(2018).
(25) attributes for each publication, these include publication id Complex network analysis offers a multitude of methods and
(uniqueidentificationnumberassignedtoeachpublication),DOI,title tools for addressing wide range of problems in real-world systems
of the publication, abstract, disciplinary “category” assigned by thatcanbemodelledasnetworks.Scientificandtechnological(pat-
Dimensions,SDGcategory,thatis,theSDG(s)towhichthepublica- ent)literatureistwosuchsystemsthatconsistsofseveralrelation-
tionhasbeenassociatedbyDimensions'AIalgorithm,author(s)ofthe ship between entities such as works (papers or patents), authors/
publication,numberofauthors,nameofthejournalinwhichthepub- inventors, institutional affiliations/assignees, and so forth. One of
lication appeared, year of publication, type of publication, ISSN, themajorrelationshipsiscitations,whereforapairofworks,thelat-
author affiliation, country in which author's organisation is located, estworkcitespreviousrelatedwork.Thisresultsintheformationof
conceptsassociatedwiththepublication,conceptscoresfortheasso- scientificcitationsnetworkorcitationnetworkofscholarlypublica-
ciatedconcepts,numberofcitationsreceivedbythepublication,ref- tions/papers(DeSollaPrice,1965;Garfieldetal.,1964)andpatent
erencescited inthepapers,andso forth.Thisdata wasretrievedin citationnetworksorcitationnetworksofpatents.Amongthediffer-
August 2021 and analysed using methods of standard bibliometric entanalysespossibleinnetworks,thepathanalysishelpstoidentify
analysis,PathAnalysisandaContent-basedanalysis. the important evolutionary trajectories or connective threads of
knowledge(Hummon&Dereian,1989).Pathanalysishasbeenused
by many for determining important evolutionary paths that might
3.1 | Bibliometricanalysis have served as backbone of development of different fields. Few
examplesareevolutionarytrajectorystudyformedicaltechnologies
Bibliometric Analysis is a method which is applied to explore large (Mina et al., 2007), ‘Coronary angioplasty’ (Tampubolon &
amountofliteratureandcanidentifymajortrendssuchasmostinflu- Ramlogan,2007),humanresourcedevelopment(Joetal.,2009)and
entialpublications,authors,subdomains,collaborations,andsoforth, archaeology(Brughmans,2013),andsoforth.
(Donthuetal.,2021;Farrukhetal.,2020;Kumaretal.,2021).Forcar- Citationnetworksarebydefaultunweighted.Pathanalysiscon-
ryingoutbibliometricanalysis,astandardbibliometricsapproachwas sists of two major steps – (i) weight assignment or conversion of
used.Fromthepublicationmetadata,firstofall,thetotalnumberof unweighted network into weighted network and (ii) search or trace
publications in AI for SDGs were identified. Thereafter, major coun- through the weighted network to retrieve paths. Original Hummon
tries/regionscontributingtoAIforSDGsresearchwereidentifiedby andDereian (1989)frameworkusedtraversalasthebasisof weight
processing author affiliation field of the metadata. Country/ region assignment of arcs (directed citation links) for the creation of
levelcollaborationnetworkswerealsodrawntounderstandthescien- weighted network. A break-through in path analysis literature was
tificcollaborationstructureofAIforSDGsresearch.Themajorjour- brought-in by Batagelj (2003) when computationally efficient
nals publishing the AI for SDGs research are identified next by traversal-basedweightassignmentmethodnamelysearchpathcount
processing the publication source field of the publication metadata. (SPC) method was introduced. Generally, the traversal-based weight
Subsequently, the research output in each SDG is measured and a assignmentschemescanbetermedtogetherasSPXschemes.Amajor
map of contribution of different countries in different SDGs is development in search scheme happened with the introduction of
created. searchschemeslikebackwardsearch,key-routesearch,globalsearch,
After looking at the overall picture of the AI for SDGs research andsoforth,withaprovisionfortolerance.Theseschemes,especially
output,theSDGsinwhichmostresearchoutputisfoundareanalysed multiplekey-routesearch,empoweredtheabilityofpathanalysisto
indetail.ForeachsuchSDG,thesubjectareasfromwhichresearch retrieve more important evolutionary trajectories in scientific litera-
outputiscomingisidentified.Thekeyconceptsoccurringinpublica- ture.However,duetothedependencyonSPXmethodsontheglobal
tions for each SDG are identified and plotted in a density plot to structure of the network, in a connected component, highly (SPX)
understand the thematic structure of research publications in each weightedarcsseemtocluttertogether,therebylimitingtheeffective-
SDG.Themajorconceptevolutiontrajectoriesareidentifiedandana- nessofmultiplekeyroutesearchtoretrievemultiplepaths.Inorderto
lysednextbyfollowingthepathanalysismethodology. address this limitation, (Lathabai et al., 2018) introduced a novel
weightassignmentmethod,namelytheFlowVergence(FV)gradient
method for weight assignment and also upgrading the Liu-Lu
3.2 | Pathanalysis approach(Liu&Lu,2012).withstate-of-the-artintegratedframework
inpathanalysis.WiththeframeworkofLathabaietal.(2018),ifwe
This study also utilised the network scientometrics approach (path useSPXandFVgradientasweightassignmentmethods,andexisting
analysis)toobservethedevelopmentintheliteratureofAIforSDGs searchschemes,followingpathscanberetrieved:SPX-forwardpaths,
from2001 through 2020. For thispurpose, theextracted data was SPX-backward paths, SPX-keyroute paths, SPX-critical paths, FV-
cleaned to remove records that did not have corresponding values forwardpaths,FV-backwardpaths,FV-keyroutepathsandFV-critical
for ‘referenced_pubs’ and used to create the citation network paths.Inthiswork,weuseSPC(amongSPX)weightassignmentand
10991719,
2024,
1, Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1002/sd.2706
by
NICE,
National
Institute
for
Health
and
Care
Excellence,
Wiley
Online
Library
on
[29/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

728 SINGHETAL.
therefore the retrieved paths will be SPC-forward path, SPC-
backward path, SPC-keyroute path, SPC-critical path, FV-forward
path,FV-backwardpath,FV-keyroutepathandFV-criticalpath.
Brief description of SPC and FV gradient weight assignment
methodsandthesearchschemesaregiveninAppendixA.
3.3 | Contentanalysis
MostofthepublicationsthatappearinimportantpathsdealwithAI
techniques appliedto different problemsfrom various fields relating
toSDGs.Thesepublicationswereidentified,chronologicallyarranged
andtheirfulltextswereaccessedfromtheirrespectivesources.The
FIGURE 1 Theyear-wisetrendinpublicationcountforpapersin
specificselectedcharacteristicsofthesestudieswerebroughtoutby
AIapplicationsonSDGs.Asharpincreaseinthenumberof
diligentandrigorousanalysisofthecontentoftheseworksbymanu- publicationscanbeseenfrom2016onwards,aftertheadoptionof
ally going through the abstracts and overallcontentof these works. SDGsin2015.AI,artificialintelligence;SDGs,Sustainable
Thecharacteristicslookedatinthesestudieswerearea(s)ofapplica- DevelopmentGoals.
tion, theme, SDG target covered, AI method(s)/ models studied/used,
natureofthestudy,andtheInference/Conclusiondrawnbythestudies.
Althoughthisisatime-consumingandsubjectivemethod,itisadvan- ofcitationsreceivedbythepublicationsonAI4SDGsshowsacorre-
tageous if the requisite care is taken during the analysis. Useful spondingincreasefrom2012to2015.Itmaybenotedthatthistime
insightsaboutpopularareasofresearch,methodsused,andsoforth, frame is associated with the renaissance of artificial intelligence, in
canbedrawnbyutilisingtheresultsofpathanalysis.Forthepurpose termsoforiginofdeeplearningparadigminAIwhicharecapableof
ofthisstudy,articleswereassignedoneofthefivenature(Predictive superiorperformanceinawidevarietyofproblemdomains.AI-based
(model)Analysis,DescriptiveAnalysis,Review,ValidationStudy,Recom- models like “AlexNet” and “Alpha Go” had proved their potentialin
mendationAnalysis).AchartshowingtheAImethods/modelsusedin solvingreal-worldproblems(Haenlein&Kaplan,2019;Muthukrishnan
thesearticleswaspreparedandispresentedasapartofthesummary etal.,2020).Thesenewdevelopmentsmaybeseenasresponsibleto
of these qualitative findings. An alternativevisualisationof thefind- haveboughtbacktheresearchcommunity'sattentiontowardsAI.
ingsofthecontentanalysisisalsopresented.
4.2 | TopregionscontributingtoAIresearch
4 | DESCRIPTIVE RESULTS forSDGs
This section portrays the results obtained from the descriptive ana- The most active geographical regions/ countries around the world
lyses that were conducted on the data. These analyses not only focusing on AI4SDG research are the United States, Western
helpedtovisualisethedatainameaningfulwaybutalsotoformalise Europe, China, Japan, Australia, and India (Figure 2). Areas on the
the components that needed detailed attention. Four major aspects eastcoastofUnitedStates(NewYork,Washington,Hawaii),Canada
were focused upon including temporal, regional, collaborative, and (Montreal, Ottawa, Toronto, etc.), United Kingdom, Norway,
quantitative. The temporal analysis includes visualising the trend of Sweden, France, Germany, Italy, India (New Delhi, Bangalore),
publications and their citations over the 20years, for all the SDGs. Singapore, China (Beijing, Shanghai), Hong Kong, Japan, and
Theregionalanalysisrevolvesaroundidentifyingresearchhotspotsin Australia (Sydney, Melbourn) show the highest density in the map
theworldbasedongeotagsofeachpublication.Revellingthecollabo- and would have the greatest number of research publications on
rationpatternsthatexistinthedomainamongauthorsfromdifferent AI4SDG. On the other hand, South American countries Mexico,
regionswasthemotiveofcollaborativeanalysis.And,thelastanalysis Brazil,Argentina,AfricaandpartsofMiddleEasthadlowernumber
wasusedtoquantifytheresearchoutputwiththeavailablevariables, ofpublications.Inadditiontothis,thenumberofpublicationsindif-
thatis,individualSDGsandthemostactiveregions. ferentregionswerealsofoundtovarybydifferentSDGs.Forexam-
ples, it was observed that the African region has most of its
publicationsonSDG2(ZeroHunger)andSDG3(GoodHealthand
4.1 | TemporalpatternsinAIresearchforSDGs Wellbeing).InIndiaandChina,thelargerpercentageofpublications
wererelatedtoSDG3,SDG7,andSDG11.Whereas,theUSA,UK,
Thetotalnumberof publicationsonAIfor SDGs(hereafterreferred Europe,andJapanhadpublicationsrelatingtoallsixtop-performing
to as AI4SDG) shows an exponential growth post the adoption of SDGs. Among the South American countries, Brazil and Columbia
SDGsby theUnitedNationsin2015(Figure1).Theoverallnumber hadthelargestnumberofpublications.Theseweremostlyrelatedto
10991719,
2024,
1, Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1002/sd.2706
by
NICE,
National
Institute
for
Health
and
Care
Excellence,
Wiley
Online
Library
on
[29/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

SINGHETAL. 729
FIGURE 2 RegionaldistributionofresearchonAI4SDG.Plottedbyusingthe“location”fieldofthepublicationmetadata,thesizeofdot
showsthenumberofpublications.TheareaswithhighdensityofdotshadhighproductivityinAI4SDGresearch.GeoplotandGeoPandas
librariesofpythonwereusedtopreparethisplot.
FIGURE 3 Region-wise
publicationsandcollaborations
betweendifferentcountriesare
shownbyarcs,inAIforSDGs
research.AI,artificialintelligence;
SDGs,SustainableDevelopment
Goals.
SDG3andSDG7,whereasotherSDGsdidnothavemanypublica- infrastructure, environment, education, and health and the smaller
tionsrelatedtoAI4SDGfromthisregion.Itisobservedthatresearch and underprivileged countries target specifically SDGs relating to
giant countries have been focusing more on SDGs relating to health and hunger reflecting their societal needs. This is in
10991719,
2024,
1,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1002/sd.2706
by
NICE,
National
Institute
for
Health
and
Care
Excellence,
Wiley
Online
Library
on
[29/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

 10991719, 2024, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/sd.2706 by NICE, National Institute for Health and Care Excellence, Wiley Online Library on [29/06/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| 730 |     |     | SINGHETAL. |
| --- | --- | --- | ---------- |
TABLE 1 ThetopjournalspublishingpapersonapplicationsofartificialintelligenceforSustainableDevelopmentGoals.
|         |           | TP TC   | CPP |
| ------- | --------- | ------- | --- |
| Journal | Publisher | SDG SDG | SDG |
IEEEAccess InstituteofElectricalandElectronicsEngineers(IEEE) 619 8993 14.53
| JournalofPhysicsConferenceSeries | IOPPublishing                | 279 440  | 1.58  |
| -------------------------------- | ---------------------------- | -------- | ----- |
| Sensors                          | MDPI                         | 278 5133 | 18.46 |
| Energies                         | MDPI                         | 259 3736 | 14.42 |
| RemoteSensing                    | MDPI                         | 205 4021 | 19.61 |
| AppliedSciences                  | MDPI                         | 198 1933 | 9.76  |
| PLOSONE                          | PublicLibraryofScience(PLoS) | 189 4635 | 24.52 |
| ScientificReports                | SpringerNature               | 161 4502 | 27.96 |
| Sustainability                   | MDPI                         | 148 1589 | 10.74 |
| AppliedEnergy                    | Elsevier                     | 136 7124 | 52.38 |
IOPConferenceSeriesMaterialsScienceandEngineering IOPPublishing 134 145 1.08
InternationalJournalofInnovativeTechnologyand BlueEyesIntelligenceEngineeringandSciencesEngineering 128 53 0.41
andSciencesPublication–BEIESP
ExploringEngineering
| ProcediaComputerScience | Elsevier | 128 1228 | 9.59 |
| ----------------------- | -------- | -------- | ---- |
IEEEInternetofThingsJournal InstituteofElectricalandElectronicsEngineers(IEEE) 112 3268 29.18
InternationalJournalofRecentTechnologyand BlueEyesIntelligenceEngineeringandSciencesEngineering 101 69 0.68
| Engineering | andSciencesPublication–BEIESP |          |       |
| ----------- | ----------------------------- | -------- | ----- |
| Energy      | Elsevier                      | 100 2770 | 27.70 |
ISPRS–InternationalArchivesofthePhotogrammetry, CopernicusPublications 92 268 2.91
RemoteSensingandSpatialInformationSciences
IOPConferenceSeriesEarthandEnvironmentalScience IOPPublishing 84 90 1.07
IEEETransactionsonIntelligentTransportationSystems InstituteofElectricalandElectronicsEngineers(IEEE) 83 1919 23.12
InternationalJournalofEngineeringandAdvanced BlueEyesIntelligenceEngineeringandSciencesEngineering 81 43 0.53
| Technology | andSciencesPublication–BEIESP |     |     |
| ---------- | ----------------------------- | --- | --- |
conformitywiththeobservationsofChuietal.(2018),whichassoci- top 20 journals ranked by the number of publications were selected.
ated17SGDswithwidersocialandenvironmentalissues. These accounted for 17.13% (3515) of the total publications in
AI4SDG.ThetopjournalwiththemostpublicationswasIEEEAccess
(publishedbytheInstituteofElectricalandElectronicsEngineers),fol-
4.3 | Region-wisecollaborationnetworkofAI lowedbytheJournalofPhysicsConferenceSeries.Thetop3journals
researchforSDGs ranked byCitationsper paper (CPP) included Applied Energy (52.38),
IEEEInternetofThingsJournal(29.18),andScientificReports(27.96).
ThecollaborationsbetweendifferentregionswerevisualisedusingVoS ThetotalcitationsreceivedbypaperspublishedinAppliedEnergywere
viewer (Figure 3). The US, The UK, China, Canada, Australia, and thehighestfollowedbyIEEEAccessandSensors(Table1).Thejournals
Germany had the most publications in collaboration with international thatappearinthetoplistvaryinsubjectclassifications.Manyofthem
authors.TheUS,theUKandChinawerethetopthreeclosestpartners werefoundmultidisciplinary.Whiletheotherprominentsubjectshav-
followed by the US and Canada, The UK and Germany, Australia and ing publications in AI4SDGs include Computer Science, Electrical &
China,aswellasUKandChina.ItmayalsobenotedthatmostEuropean Electronics, Chemistry, Instruments & Instrumentation, Geosciences,
countrieshaveclosetieswitheachotherwhenitcomestoresearchcol- Civil engineering, Energy & Fuels, and Thermodynamics. This in turn
laborationinthedomain.Thesecollaborationpatternsnotonlyoutline portraysamultifacetedpenetrationofAIindifferentdomains.
thegeographicalandideationalproximitybutalsothetrendsthatpersist
inthetransferofknowledgeandtechnologyamongtheseregions.
4.5 | AIresearchoutputrelatedtovariousSDGs
4.4 | TopjournalspublishingAIresearchforSDGs SDGs 3 (Good Health and Well Being) and SDG 7 (Affordable and
CleanEnergy)showedasharpriseinthetotalnumberofpublications
The20,511articlespublishedweredistributedin360journals,show- from 2015 onwards with the number of publications doubling from
ing the widerapplications of AI in SDGs. Among these journals, the thepreviousyear(Figure4).SDG3hadthehighestnumberoftotal

SINGHETAL. 731
FIGURE 4 Thetrendinpublicationcountof
AIapplicationsonindividualSDGs.Threegroups
basedonthenumberofpublicationscanbeseen,
theseincludeSDGs7and3(High),4,13,
11,16(Moderate),andtherest11(Low).SDGs
7and3exhibitarapidincreasesince2012.
Before2012,thehighestnumberofpublications
was45(2011)forSDG4.Thelegendliststhe
SDGsbasedontheirtotalyearlypublications.AI,
artificialintelligence;SDGs,Sustainable
DevelopmentGoals.
publications (6829), followed by SDG 7 (6683), SDG 4 (2312), SDG thepublicationscountwasunevenlydistributedamongtheseSDGs,
13(1510),SDG11(1296),andSDG16(1059).Othergoalshowever only the goals having high publication counts (greater than 1000)
hadlessthan1000totalpublicationsonAI4SDG.Thenumberofpub- were chosen for this exploration, that is, (SDG3, SDG 7, SDG
lications in SDG 17 (Partnerships for the Goals) was the smallest. 4,SDG11,SDG13,SDG16).Thisfilteringwasadoptedconsidering
These patterns indicate that AI has a more involved role in certain an assumption that the SDG having higher research output in the
areasascomparedtoothers. domainiswellexploredandwouldrepresentabetterAIpenetration
inthesaidarea.Thefollowingsubsectionspresentadetailedanaly-
sisalongeachofthesixSDGsconsideredhere.ForeachSDG,the
4.6 | Region–AI4SDGpublicationsmap subjectareadistributionoftheresearchoutput,themostfrequent
concepts occurring in the research papers on that SDG, the major
ThehighestproportionofresearchpublicationsfromtheUnitedStates concept evolution paths, and some highly cited papers are dis-
as well as China corresponds to topics related to SDG 3 and SDG cussed.Figure6belowpresentsasummarydiagramofsubjectarea
7. Publications corresponding to topics related to SDG 1, and SDG distributionofresearchoutputinthesixSDGsconsidered.Thesub-
5correspondtoninecountriesandSDG17correspondstoonlytwo sectionsfor each SDG will discussthe relevant part of the subject
countries, namely, the United States and the United Kingdom. Both area distribution shown in the figure. Plots of frequency of occur-
region-wiseandSDG-wisedifferentialfocusinresearchrelatingtothe rence of the major concepts for each of the six SDGs is given in
applicationofAIinSDGcanbeinferredfromtheheatmap(Figure5). AppendixB.
5 | DETAILED ANALYSIS OF PROBLEM 5.1 | SDG3–Goodhealthandwell-being
DOMAINS ADDRESSED, AND AI TECHNIQUE
APPLIED FOR SDGS This goal aims to provide a healthy lifestyle and promote good
health for people of all ages. It is also one of the most researched
This section presents analysis of the major problem areas being goalsasobservedinthepublicationdata analysed with 6829 total
addressedwith thehelp ofAItechniquesamong various SDGs.As papers (comprising about 33.3% of the whole publications).
10991719,
2024,
1,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1002/sd.2706
by
NICE,
National
Institute
for
Health
and
Care
Excellence,
Wiley
Online
Library
on
[29/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

732 SINGHETAL.
FIGURE 5 Region-wiseresearchproductivityineachSDG.OnlyafewcountrieshavepublicationsinSDG17.
TheUnitedStateswasobservedtobethetopcontributingcountry paper compared the current models in practice with the Radiomics
inthedomainwith(n=2634)totalpublications.Themajorcontrib- modeltoproveitssignificanceandopportunitiesthatmayarriveinthe
uting subject areas to this SDG are found to be Medical & Health futureandalsotalkedabouttheneedforstandardisationindatacollec-
Science (37.83% papers) and Information & Computing Science tion, evaluation criteria, and reporting guidelines inthe field.Another
(31.17%papers)(seeFigure6).TheAI-relatedconceptthattopedin paperwithmorethan1000citationswasfromvanGriethuysenetal.
appearance was “convolutional neural network” with a total of (2017)titled“ComputationalRadiomicsSystemtoDecodetheRadio-
375publicationsdiscussingit.Thereisahighlevelofemployment graphic Phenotype”. They have developed an open-source platform
of techniques for Image processing and Computer vision in the “PyRadiomics”intendedtoextractalargepanelofengineeredfeatures
domain.Mostofthisiscentredaroundmedicaldiagnosis.Theother fromthemedicalimage.Anotherpublicationwithsignificantattention
conceptsthatappearedfrequentlyandweredirectlyrelatedtothe was titled “Artificial Intelligence Distinguishes COVID-19 from
domainwere“electronichealthrecords”and“clinicaldecisionsup- Community-AcquiredPneumoniaonChestCT”byLietal.(2020)and
portsystem”.Afrequencyofoccurrenceplotofthemajorconcepts proposedadeeplearning-basedmodeltoidentifyCOVID-19onchest
for SDG 3 is given in Figure A1 of the Appendix B. To get more CTexamsanddistinguishitfromcommunity-acquiredpneumonia.“An
detailed insight about the thematic attention of AI applications on immunogenicpersonalneoantigenvaccineforpatientswithmelanoma”
this SDG, some of the most cited papers are explored in more apaperfromRajkomaretal.(2018)criticisedtheuseofstandardstatis-
detailnext. ticalanalysisonEHRastheytendtomissmanyrelevantinferencesand
Themostcitedpublicationinthissub-domainwas“Radiomics:the proposedadeeplearning-basedmethodtohandlethesameefficiently.
bridgebetweenmedicalimagingandpersonalisedmedicine”byLambin Thus, AIapplicationsinmedicaldiagnostics,electronichealthrecords,
et al. (2017) published in “Nature Reviews Clinical Oncology” with personalisedmedicinearesomeofthefocusareasinthisSDG.
1366citations.ThepapertalkedabouttheimportanceofRadiomics,a Nowwemoveaheadtopresenttheknowledgeflowandcontent
field that describes the mining of quantitative features from medical analysisofpapersinAIapplicationstoSDG3throughthePathanaly-
images and coupling it with the clinical decision support system. The sisapproach.
10991719,
2024,
1,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1002/sd.2706
by
NICE,
National
Institute
for
Health
and
Care
Excellence,
Wiley
Online
Library
on
[29/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

SINGHETAL. 733
5.1.1 | TrendsofknowledgeflowinAI4SDG 5.2 | SDG7–Affordableandcleanenergy
researchrelatedtoSDG3
Thebiggerpictureofthisgoalistoensuremodern,clean,sustainable,
SDG3networkconsistsof5625nodesand5509links.Thereisasin- andaffordableenergyavailabletoall.With(n=6683)numberoftotal
gleprominentchainthatisfoundtobethemostrelevantforSDG3, publications,thisgoalissecondintermsofnumberofpublicationson
Xiong et al. (2014)–Lutz et al. (2020) (Figure 7). There is a point of theuseofAItechnologies.Themostoutputinthisareawasfoundto
knowledgeconvergenceatMenke(2018)anddivergenceatKessler be from China with 1838 total publications followed by US and
etal.(2019). UK.Figure6showsthesubjectareaswhichcontributetoresearchon
Personalisedmedicinewastheareainwhichthearticlesfeatured AIapplicationsinSDG7.Themajorcontributingsubjectareastothis
onthemostprominentpathweremostlyfocusedupon.Itsvariations SDGarefoundtobeEngineering(32.97%papers)andInformation&
from genetics, pharmaco-genomics, and pharmacotherapy are seen ComputingScience(31.92%papers).Next,themajorconceptsoccur-
amongtheapplicationareas(Table2). ring in the research publications are shown in Figure A2 in the
FIGURE 6 TopfieldsofresearchcontributingtopublicationsforthesixSDGsconsidered.Thepercentagecontributionofeachfiledisshown
along-withtheclassificationcodeforthefieldinDimensionsdata.
FIGURE 7 MostprominentpathofknowledgeflowinthecitationnetworkofpublicationsonSDG3.Inthisandthefollowingfigures,the
nodesrepresentthearticlesandthearrowsrepresentthecitationrelationshipbetweenthearticles.ThesizeofthearrowsindicatesFV
normalisedcountofsearchpathspassingthroughthepairofnodes.
10991719,
2024,
1,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1002/sd.2706
by
NICE,
National
Institute
for
Health
and
Care
Excellence,
Wiley
Online
Library
on
[29/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

 10991719, 2024, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/sd.2706 by NICE, National Institute for Health and Care Excellence, Wiley Online Library on [29/06/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
734 SINGHETAL.
TABLE 2 Year-wiselistingofmajorareasofapplicationandtargetsinSDG3,artificialintelligence(AI)methodsandmodelsused,natureof
thestudy,andresearchfindingsoftheavailableliteraturededucedusingpathanalysis.
|     |     |     |     |     | SDG3target |     | AImethod(s)/Models | Natureof |     |
| --- | --- | --- | --- | --- | ---------- | --- | ------------------ | -------- | --- |
Year Area(s)ofapplication Theme covered studied/used thestudy Inference/Conclusion
2014 GeneticsResearch PrecisionMedicine/ 3.D Bayesiandeeplearning Predictive Amodelforidentificationof
|     |     |     | GenomicMedicine |     |     |     | algorithm | Analysis | genescausingdisease |
| --- | --- | --- | --------------- | --- | --- | --- | --------- | -------- | ------------------- |
2015 GeneticsResearch Deeplearning,Recurrent Review ComputationalModelof
|     |     |     |     |     |     |     | NeuralNetworks |     | Protein-DNAandProtein- |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ---------------------- |
RNABinding
2017 Pharmaco-genomics Systemsgenomics Machinelearningand Review MLSGtools-basedpredictionof
|     | (Systemsgenomics) |     |     |     |     |     | systemsgenomics |     | diseasesandtreatments |
| --- | ----------------- | --- | --- | --- | --- | --- | --------------- | --- | --------------------- |
(MLSG)
2018 UseofGeneticBiomarkers Personalised Multilayerfeedforward Predictive DeepMFNNframework-based
forClinicalDecision Medicine/ neuralnetworks Analysis toolfordistinguishing
|     | Making |     | GenomicMedicine |     |     |     | (MFNNs) |     | treatmentresponders |
| --- | ------ | --- | --------------- | --- | --- | --- | ------- | --- | ------------------- |
Pharmacotherapy PrecisionMedicine/ Machinelearningand Review Stratificationofpatientsallows
|     |     |     | Personalised |     |     |     | Deeplearning |     | fortailoredtreatments,   |
| --- | --- | --- | ------------ | --- | --- | --- | ------------ | --- | ------------------------ |
|     |     |     | Medicine     |     |     |     |              |     | increasingresponserates, |
andreducemedicalerrors.
2019 Psychology PrecisionHealthcare 3.4. Descriptive Differentscenariosforuseof
|     |     |     |     |     |     |     |     | Analysis | MLmethodsinmental |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ----------------- |
healthcare
|     |     |     |     |     |     |     | EnsembleLearning | Predictive |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | ---------- | --- |
|     |     |     |     |     |     |     | ModelsusingSuper | Analysis   |     |
learner
| 2020 |     |     |     |     | 3.4.3.D |     |     | Descriptive | ContributionsofAIin   |
| ---- | --- | --- | --- | --- | ------- | --- | --- | ----------- | --------------------- |
|      |     |     |     |     |         |     |     | Analysis    | improvingmentalhealth |
services
|     |     |     |     |     |     |     |     | Descriptive | Developmentofmentalhealth |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------------------------- |
|     |     |     |     |     |     |     |     | Analysis    | servicesasawhole          |
AppendixB,intermsofafrequencyplotofthemajorconceptsoccur- forecasting of wind power generation” discussed various methods
|     |     |     |     | “Neural | networks” |     |     |     |     |
| --- | --- | --- | --- | ------- | --------- | --- | --- | --- | --- |
ring in the research papers on this SDG. was the andtechniquesavailabletopredictwindpowergenerationconsider-
mostiteratedtechnologicalconceptwith525appearancesfollowedby ingtheclimaticandotherfactorsintoconsideration, andgotsignifi-
“convolutional neural networks” with more than 300 appearances in cantattention.Anotherpublicationonasimilarthemewas“Machine
variouspublications.Frequentlyoccurringconceptsrelatedtotheprob- learningmethodsforsolarradiationforecasting:Areview”byVoyant
lemdomainwere“wirelesssensornetworks”,“smartgrids”and“elec- etal.(2017),publishedinthejournal“RenewableEnergy”anditcom-
tricvehicles”.
paredthevariouspopularmachinelearning-basedmethodsinpredict-
Now we look at some most cited papers on AI applications on ing the power output of the solar system. ANN and ARIMA-based
SDG7.Oneofthemostcitedpublications(morethan1200citations) methods were their major focusing area. AI applications in manage-
inthedomainwas“FogandIoT:AnOverviewofResearchOpportuni- mentofenergysystemsisamajorfocusareainthisSDG.
| ties”         | by Chiang and | Zhang (2016) | which       | is a survey | exploring | the |     |     |     |
| ------------- | ------------- | ------------ | ----------- | ----------- | --------- | --- | --- | --- | --- |
| opportunities | generated     | by the       | development | of Fog      | computing | and |     |     |     |
IoT in the areas such as car assembly plants, minimising the down- 5.2.1 | TrendsofknowledgeflowinAI4SDG
time of nuclear reactors, optimising electrical power generators in researchrelatedtoSDG7
smartenergygrids.Anotherpapertitled“Areviewontheprediction
of buildingenergy consumption” was by Zhao and Magoulès (2012) ThepathanalysisapproachshowsthattheSDG7networkconsistsof
“Journal
that appeared in the of Renewable and Sustainable Energy 6084nodesand7522links.Figure8showsthattheobtainednetwork
Reviews”surveyedtherecentworksthathaveexploredtheprobable pathhadvariouschainsandmultiplepointsofdivergence,indicating
solutions to the problem of predicting the energy consumption of a thehighlyinterdisciplinarynatureofresearchinSDG7.Threeofthe
buildingsconsideringvarioussub-factorslikeambientweathercondi- longest chains started from Ilagras (2008), Paris et al. (2011), and
tions, building structure, and so forth. Another survey paper from Chaouachietal.(2010)andterminatedatYoonetal.(2020),Vaisakh
“Current
Foley et al. (2012) titled methods and advances in the and Jayabarathi (2020), and Tovar et al. (2020) respectively.

SINGHETAL. 735
TherearetwopointsofknowledgeconvergenceMocanuetal.(2016) paradigmforeducationalsoftware”,publishedinthe“AppliedArtificial
andReynondsetal.(2018)whilethreepointsofdivergenceAhmad Intelligence” journal, discussed agent-based (Betty's brain) interactive
etal.(2018)a,Ghimireetal.(2019),andWangetal.(2020). moduleproposedbyBiswasetal.(2005).Anotherhighlycitedpublica-
Thedetailedcontentanalysisof thepapersshowsthatthearti- tion titled “Developing seriousgames for cultural heritage:a state-of-
clesfocusingonusingAIandtechnologytopromoteEnergyconser- the-artreview” by Anderson etal.(2010) discussedtheuse of virtual
vation,EnergyGeneration,Solarpowergeneration,andsoforth,are andaugmentedrealitygamestosupporthistoricalteachingandlearning.
foundtobepresentonthemostprominentpath(Table3). Onemorehighlycitedpaperinthisdomainwas“MachineLearningPar-
adigmsfor Speech Recognition: An Overview” by DengandLi (2013)
that discussed the challenges and opportunities that Artificial Intelli-
5.3 | SDG4–Qualityeducation genceposesinhighereducation.ApplicationsofAIineducationaltech-
nologiesandparadigmsisamajorfocusareainthisSDG.
This SDG targets to provide completely free, equitable, and quality
educationforbothboysandgirlsby 2030sotheytheacquireskills
andknowledgerequiredfortheirsustainabledevelopmentandelimi- 5.3.1 | TrendsofknowledgeflowinAI4SDG
nateanykindofgenderbiasesineducation.Itrankedthirdinourlist researchrelatedtoSDG4
with (n=2312) publications in total. Once again, United Nations
appearstobethecountrywithmostpublicationsfollowedbyChina ThepathanalysisofpapersinthisdomainshowthatSDG4network
andUK.ThemajorcontributingsubjectareastothisSDGarefound consists of 1590 nodes and 437 links. There is a single prominent
to be Education (33.48% papers) and Information & Computing Sci- chainthatisfoundtobethemostrelevantforSDG4(Figure9),Hus-
ence(30.78%papers)(seeFigure6).Themajorconceptsoccurringin sainetal.(2018)–ZhouandSong(2020).Thereisonepointofdiver-
the research papers in this domain are presented in Figure A3 genceNaseeretal.(2020)‘a’,whichlinkstoNaseeretal.(2020)and
in Appendix B. The technological concepts that dominated this area ZhouandSong(2020).
were“ArtificialIntelligence”and“NaturalLanguageProcessing”.Also InthemostprominentpathforSDG4,studiesusingMachineand
“Learning environment” and “Higher Education” were the most DeepLearningmethodsinpredictingperformanceofindividuals(stu-
repeated problem area concept depicting the creation of an aug- dents,employees,teams)arefound.Thesestudiesaimtoassistdeci-
mentedlearningapproachwiththehelpofAI. sionmakingandimprovetheefficiencyofmanagementandenhance
Nowwelookatsometopcitedpapersinthisdomain.Apublication learningforstudents(Table4).
withsignificantattentioninthedomainwas“AutoTutor:Atutorwith
dialogueinnaturallanguage”byGraesseretal.(2004)whichappeared
inthe“BehaviorResearchMethods”journal.Thispaperdescribed“Auto 5.4 | SDG13–Climateaction
Tutor”,aNaturalLanguageDialoguetutorwhichaimstoassisttheuser
tobetterframetheiranswersthroughaseriesofdialogueswithAuto Mitigating adverse effects caused by climate change and improving
Tutor. Another paper titled “Learning by Teaching: A new agent education and awareness regarding appropriate actions towards
FIGURE 8 MostprominentpathofknowledgeflowinthecitationnetworkofpublicationsonSDG7.
10991719,
2024,
1, Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1002/sd.2706
by
NICE,
National
Institute
for
Health
and
Care
Excellence,
Wiley
Online
Library
on
[29/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

 10991719, 2024, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/sd.2706 by NICE, National Institute for Health and Care Excellence, Wiley Online Library on [29/06/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
736 SINGHETAL.
TABLE 3 Year-wiselistingofmajorareasofapplicationandtargetsinSDG7,artificialintelligence(AI)methodsandmodelsused,natureof
thestudy,andresearchfindingsoftheavailableliteraturededucedusingpathanalysis.
SDG7
| Area(s)of |     | target | AImethod(s)/Models | Natureof |     |
| --------- | --- | ------ | ------------------ | -------- | --- |
Year application Themes covered studied/used thestudy Inference/Conclusion
2008 Energy EnergyEfficient 7.3 ComputationalIntelligence/ Descriptive SmartdeviceswithAI
Conservation/ Houses/Spaces SoftComputing Analysis aggregationsystemto
| Internetof |     |     |     |     | provideenergyefficient, |
| ---------- | --- | --- | --- | --- | ----------------------- |
| Things     |     |     |     |     | intelligent,adaptiveand |
convenientuser
experience
2010 ComputationalIntelligence/ Descriptive IntelligentAgentsand
|     |     |     | SoftComputing,        | Analysis | MultiagentSystemsin  |
| --- | --- | --- | --------------------- | -------- | -------------------- |
|     |     |     | DistributedAI/Ambient |          | energyconservationin |
|     |     |     | AI                    |          | Buildings            |
2016 Energy SmartGrids 7.A ArtificialNeuralNetwork, Predictive FCRBM'sadvantageover
| Conservation |     |     | Deeplearning,CRBM, | Model    | othermethodsfor       |
| ------------ | --- | --- | ------------------ | -------- | --------------------- |
|              |     |     | FRBM,SVM,RNN       | Analysis | predicationofbuilding |
energyconsumption
patterns
2018 EnergySystem EnergyGenerationand Deeplearning,AIfordistrict Review Proposalforamodelfuture
| Optimization | Optimisation |     | energyconversion |     | districtenergy     |
| ------------ | ------------ | --- | ---------------- | --- | ------------------ |
|              |              |     | technology       |     | managementsolution |
usingsemanticmodelling
2019 EnergySystem EnergyEfficient 7.3 DHN,Extremely Predictive AllDHN,ETandSVRare
Optimization Houses/Spaces RandomisedTree(ET), Model goodforpredictingHVAC
|     |     |     | SupportVector   | Analysis | hourlyenergy |
| --- | --- | --- | --------------- | -------- | ------------ |
|     |     |     | Regression(SVR) |          | consumption  |
2020 SolarPower EnergyGenerationand 7.2 ConvolutionalNeural Predictive Ahybriddeeplearning
Generation Optimisation Network(CNN),Long Model modeltoforecastglobal
|     |     |     | Short-TermMemory | Analysis | solarradiation |
| --- | --- | --- | ---------------- | -------- | -------------- |
Network(LSTM)
2020 SolarAssisted EnergyEfficient 7.3 LSTM,Attention-based Validation Superiorperformanceof
WaterHeating Houses/Spaces 7.A LSTM,ALSTM– Study ALSTM-Dinpredicting
|     |     |     | decomposeddata |     | energyuseover      |
| --- | --- | --- | -------------- | --- | ------------------ |
|     |     |     | (ALSTM-D)      |     | conventionalmodels |
2020 EnergyEfficiency BuildingEnergyUse 7.2 ANN,CNN,RNN,LSTM Predictive Higherpredictionaccuracy
|     |     | 7.A |     | Model    | ofbuildingenergyusage |
| --- | --- | --- | --- | -------- | --------------------- |
|     |     |     |     | Analysis | ofLSTMoverother       |
methods
2020 Solar/PVPower AIMethodsfor MultipleMethodsDescribed Review Taxonomyofexisting
| Generation | PredictionofSolar  |     |     |     | modelsforpredictionof  |
| ---------- | ------------------ | --- | --- | --- | ---------------------- |
|            | energyavailability |     |     |     | solarpoweravailability |
andtheirapplications
| 2020 | PVpowersystems/ |     | CNN,LSTM(RNN) | Review | HybridDeepLearning  |
| ---- | --------------- | --- | ------------- | ------ | ------------------- |
|      | SmartGrid       |     |               |        | approachforPVoutput |
powerforecasting
2020 PVpowersystems CNN,LSTM(RNN),Ridge Predictive HybridNeuralNetworkhas
|     |     |     | RegressionandLasso | Model    | betterpredictionofPV |
| --- | --- | --- | ------------------ | -------- | -------------------- |
|     |     |     | Regression         | Analysis | powergenerationfor   |
energysystems
Abbreviations:CNN,convolutionalneuralnetwork;CRBM,conditionalrestrictedBoltzmannmachine;DHN,deephighwaynetworks;ET,extremely
randomisedtree;FRBM,factoredconditionalrestrictedBoltzmannmachine;LSTM,longshort-termmemorynetwork;RNN,recurrentneuralnetworks;
SVR,supportvectorregression.
climateisthefocusareaofthisSDG.With(n=1510)publicationsin bepublishedafter2015.TheParisAgreement2015couldbeconsid-
the corpus, this ranked 4th in the use of AI to address consequent eredaprobablecatalystforthisincreaseinresearchinterest.TheUS,
problems.About86%ofthetotaloutputinthisareawasobservedto China, and the UK again appear to be the countries with higher

 10991719, 2024, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/sd.2706 by NICE, National Institute for Health and Care Excellence, Wiley Online Library on [29/06/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
SINGHETAL. 737
| publications | in the | domain. | The major | contributing | subject | areas | to  |     |     |     |
| ------------ | ------ | ------- | --------- | ------------ | ------- | ----- | --- | --- | --- | --- |
srotacudeesruocrofmetsysnoitadnemmoceR
this SDG are found to be Engineering (28.7% papers) and Informa- erutaefniagnoitamrofnifohcaorppadirbyha otdetcepxesmaetehttciderpotnoitceles
|     |     |     |     |     |     |     |     | nitnemegagnetnedutsetaulaveotsledoM | erawtfosniedargegareva-wolebaniatbo |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------- | ----------------------------------- | --- |
elbaliavaehtfosgnidnifhcraeserdna,ydutsehtfoerutan,desusledomdnasdohtem)IA(ecnegilletnilaicifitra,4GDSnistegratdnanoitacilppafosaerarojamfognitsilesiw-raeY
tion&ComputingScience(17.72%papers)(seeFigure6).Frequently tcejorpfosseccuSehttciderpotsledoM
fonoitciderprofstiklootdnaseigetartS
| appearing    | concept          | relating | to AI was        | observed | to be  | “Neural    | Net-  |     |     |     |
| ------------ | ---------------- | -------- | ---------------- | -------- | ------ | ---------- | ----- | --- | --- | --- |
| work”. While | “Climate         | Change”  | and “Renewable   |          | Energy | Resources” |       |     |     |     |
| were the     | problem-specific |          | popular concepts |          | (see   | Figure     | A4 in |     |     |     |
AppendixB).
ecnamrofreptneduts tnempolevedtcudorp
noisulcnoC/ecnerefnI
Nowwelookatsometopcitedpapersinthisdomain.Oneofthe
mostcitedpublicationsinthisarea“Recentdeclineinthegloballand
.sELVenilno
| evapotranspiration |           | trend due   | to limited | moisture  | supply” | by           | Jung |     |     |     |
| ------------------ | --------- | ----------- | ---------- | --------- | ------- | ------------ | ---- | --- | --- | --- |
| et al. (2010)      | published | in “Nature” | journal,   | suggested |         | an ensemble- |      |     |     |     |
smaet
basedmachinelearningmethodtoassessthechangeinEvapotranspi-
rationusinggeospatialdatafromsatelliteremotesensingandsurface
meteorologicaldata.AnotherpublicationbyKongetal.(2017)titled
|     |     |     |     |     |     |     |     | ledoMevitciderP |     | noitadnemmoceR |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --- | -------------- |
“Short-TermResidentialLoadForecastingBasedonLSTMRecurrent
| NeuralNetwork”talkedabouttheemploymentofLSTM-basedrecur- |     |     |     |     |     |     |     | ehtfoerutaN |     |     |
| -------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- |
sisylanA sisylanA
rentneuralnetworktoforecastelectricloadrequirementsatamicro
yduts
| level (single | energy | customer). | One more | popular | paper | in the | field |     |     |     |
| ------------- | ------ | ---------- | -------- | ------- | ----- | ------ | ----- | --- | --- | --- |
was“MultiobjectiveIntelligentEnergyManagementforaMicrogrid”
byChaouachietal.(2012)publishedin“IEEETransactionsonIndus-
|     |     |     |     |     |     |     |     | detsoob-tneidargdna,PIRJ,eertnoisiced,84J citsigolenilesab,krowtenlaruenlaicifitrapeed | ,RL,NNA,)BN(seyaBeviaN,eertnoisiced84J |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------------------------------------------- | -------------------------------------- | --- |
trialElectronics”,anditproposedasmartsolutionformicrogridpower ,84J,gniggab,mhtirogla)FR(tserofmodnaR
|            |                  |     |          |         |          |           |     | enihcamrotcevtroppusdnanoisserger |     | ,)OMS(noitazimitpolaminimlaitneuqes eviaNdna,)PLM(nortpecrepreyalitlum |
| ---------- | ---------------- | --- | -------- | ------- | -------- | --------- | --- | --------------------------------- | --- | ---------------------------------------------------------------------- |
| prediction | and optimisation |     | problems | with an | AI-based | technique |     |                                   |     |                                                                        |
desu/deidutssledoM/)s(dohtemIA
togetherwiththelinearprogramming-basedmulti-objectiveoptimisa-
tion.Palliatingtheworld'scarbondebtisanotherburningissueinthis
area,withapublicationfromSandermanetal.(2017)titled“Soilcar-
OMSdna,REPPIR,RLS
| bondebtof | 12,000yearsofhumanlanduse” |     |     |     | havingaddressed |     | this |     |     |     |
| --------- | -------------------------- | --- | --- | --- | --------------- | --- | ---- | --- | --- | --- |
issuethroughamachinelearningmodelonaglobalcompilationofsoil
mhtiroglairoirpA
| organic carbon | data | along | with (HYDE) | land | use data | and | several |     |     |     |
| -------------- | ---- | ----- | ----------- | ---- | -------- | --- | ------- | --- | --- | --- |
)BN(seyaB
otherclimaticdata.AIapplicationsinclimatedatahandlingandenergy sreifissalc
sledom
relatedsystemsmanagementisamajorfocusareainthisSDG.
5.4.1 | TrendsofknowledgeflowinAI4SDG noitacudEenilnO noitacudEenilnO
|     |     |     |     |     |     |     |     |     | tnempoleveD | tnempoleveD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ----------- |
researchrelatedtoSDG13
|     |     |     |     |     |     |     |     |     | erawtfoS | erawtfoS |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | -------- |
emehT
ThepathanalysisofpapersinthisdomainshowthatSDG13network
| consists of | 1401 | nodes and | 778 links. | There | is a single | prominent |     |     |     |     |
| ----------- | ---- | --------- | ---------- | ----- | ----------- | --------- | --- | --- | --- | --- |
chainthatwasfoundtobethemostrelevantforSDG13(Figure10),
| Assoulineetal.(2017)–AyzelandIzhitskiy(2019).Thereisonepoint |     |     |     |     |     |     |     | tegrat4GDS |     |     |
| ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- |
| ofdivergenceBogneretal.(2019),whichlinkstoCroceetal.(2020)   |     |     |     |     |     |     |     | derevoc    |     |     |
andAyzelandIzhitskiy(2019).
|     |     |     |     |     |     |     |     | A.4 | A.4 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
4.4
.sisylanahtapgnisudecudederutaretil evitciderprofgninraeLpeeD
|     |     |     |     |     |     |     |     | noitacilppafo)s(aerA rofgninraeLenihcaM sisylanaevitciderp | rofgninraeLenihcaM sisylanaevitciderp | rofgninraeLenihcaM sisylanaevitciderp |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------------- | ------------------------------------- | ------------------------------------- |
sisylana
ataDgiB
4
ELBAT
8102 0202
| FIGURE | 9 Mostprominentpathofknowledgeflowinthe |     |     |     |     |     |     | raeY |     |     |
| ------ | --------------------------------------- | --- | --- | --- | --- | --- | --- | ---- | --- | --- |
citationnetworkofpublicationsonSDG4.

 10991719, 2024, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/sd.2706 by NICE, National Institute for Health and Care Excellence, Wiley Online Library on [29/06/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| 738 |     |     |     |     |     |     |     |     |     | SINGHETAL. |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- |
Studies featured on the most prominent path for SDG 13 pre- SDG was also found to be popular. With (n=1296) publications it
sentedmachinelearningmodelsforpredictionandincreasingopera- standsat5thplaceinthelist.Here,aleadofChinawasobservedwith
tionalefficiencyofelectricalsystems.Thesestudiespertaintoareas 26.4% of publication share followed by the US and UK. The major
ofRenewableandNon-Renewableelectricitygenerationtechnologies contributingsubjectareastothisSDGarefoundtobeEnvironment
(Table5). Science(29.34%papers)andBiologicalScience(24.52%papers)(see
|     |     |     |     | Figure 6). | “Convolutional | Neural | Network” | and | “Internet | of Things” |
| --- | --- | --- | --- | ---------- | -------------- | ------ | -------- | --- | --------- | ---------- |
werethemostoccurringtechnologicalconcepts,while“SmartCities”
5.5 | SDG11–Sustainablecitiesandcommunities
|     |     |     |     | was the most | popular | problem-specific |     | concept, | showing | a shift of |
| --- | --- | --- | --- | ------------ | ------- | ---------------- | --- | -------- | ------- | ---------- |
paradigmfromconventionaltorevolutionarytechnologiestoaddress
Makinghumansettlementsabetterplace,raisingthestandardofliv- thevariousproblemsintheurbanplanningdomain(seeFigureA5in
| ingofanindividual,anderadicatingslumsaresomeoftheprimefocus |     |     |     | AppendixB). |     |     |     |     |     |     |
| ----------------------------------------------------------- | --- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- |
areasofthisSDG.TheuseofAItoaddressproblemsrelatingtothis Nowwelookatsomemostcitedpapersinthisdomain.Themost
“Forecasting
|     |     |     |     | cited paper  | in the      | domain    | was   |         | energy consumption | of          |
| --- | --- | --- | --- | ------------ | ----------- | --------- | ----- | ------- | ------------------ | ----------- |
|     |     |     |     | multi-family | residential | buildings | using | support | vector             | regression: |
Investigatingtheimpactoftemporalandspatialmonitoringgranularity
|     |     |     |     | on performance | accuracy” |     | with 326 | citations | by Jain | et al. (2014) |
| --- | --- | --- | --- | -------------- | --------- | --- | -------- | --------- | ------- | ------------- |
andwaspublishedin“AppliedEnergy”journal.Itdiscussedaboutpre-
|     |     |     |     | dicting energy | consumption   |             | in a multi-family |         | building       | system using |
| --- | --- | --- | --- | -------------- | ------------- | ----------- | ----------------- | ------- | -------------- | ------------ |
|     |     |     |     | regression     | and suggested |             | an advanced       | way     | of development | and          |
|     |     |     |     | installation   | of smart      | electricity | metering          | devices | for            | smart homes. |
|     |     |     |     | Another paper  | discussing    | smart       | homes             | was     | “The Smart     | House for    |
FIGURE 10 Mostprominentpathofknowledgeflowinthe
citationnetworkofpublicationsonSDG13. Older Persons and Persons with Physical Disabilities: Structure,
TABLE 5
Year-wiselistingofmajorareasofapplicationandtargetsinSDG13,artificialintelligence(AI)methodsandmodelsused,natureof
thestudy,andresearchfindingsoftheavailableliteraturededucedusingpathanalysis.
SDG13
| Area(s)of |     | target | AImethod(s)/Models |     |     | Natureof |     |     |     |     |
| --------- | --- | ------ | ------------------ | --- | --- | -------- | --- | --- | --- | --- |
Year application Theme covered studied/used thestudy Inference/Conclusion
2017 PVSolarEnergy Renewableenergy 13.3 SupportVectorMachines Predictive/ EstimationstrategyusingSVM
Potential 13.2 (SVM)Geographic Validation andGISforRooftopsolar
|     |     |     | InformationSystems(GIS) |     |     |     |     | PV  |     |     |
| --- | --- | --- | ----------------------- | --- | --- | --- | --- | --- | --- | --- |
2017 Renewable Renewable 13.3 Descriptive Possiblepenetrationof
| Energy   | energy/Grid |     |     |     |     | Study/ |     | renewableenergywith   |     |     |
| -------- | ----------- | --- | --- | --- | --- | ------ | --- | --------------------- | --- | --- |
| Adoption | Management  |     |     |     |     | Review |     | existinglimitationsof |     |     |
electricalgrids
2019 Power Renewable 13.3 ANN,SupportVector Validation ModelsbasedonML
Generation energy/Grid Regression(SVR),Gaussian algorithmstopredictwind
|     | Management |     | processregression(GPR) |     |     |     |     | andsolarpowerpotential |     |     |
| --- | ---------- | --- | ---------------------- | --- | --- | --- | --- | ---------------------- | --- | --- |
andelectricitydemandfora
givengridsystem
2019 Energy EnergyProduction 13.2 MultivariateAdaptive UsefulnessofMLmethodsin
Production/ 13.3 RegressionSplines(MARS), accurateestimationof
| Consumption |     |     | QuantileRandomForest   |     |     |     |     | energyconsumptionand   |     |     |
| ----------- | --- | --- | ---------------------- | --- | --- | --- | --- | ---------------------- | --- | --- |
|             |     |     | (QRF),GradientBoosting |     |     |     |     | productionatthelevelof |     |     |
|             |     |     | Machines(GBM),         |     |     |     |     | grids                  |     |     |
NonhomogeneousGaussian
Regression(NGR)
2019 ClimateChange Hydrology/ 13.1 ExtremeGradientBoosting Modelforpredictionofimpact
|     | Ecology | 13.B | (XGB)Machine |     |     |     |     | ofclimatechangeon |     |     |
| --- | ------- | ---- | ------------ | --- | --- | --- | --- | ----------------- | --- | --- |
freshwaterinflowinAral
Sea
2020 Renewable EnergyUse/Smart 13.3 MultipleLinearRegression Predictive/ Methodologyforaccurate
| Energy   | Grid | 13.B |     |     |     | Validation |     | planningofenergysupplyin |     |     |
| -------- | ---- | ---- | --- | --- | --- | ---------- | --- | ------------------------ | --- | --- |
| Adoption |      |      |     |     |     |            |     | districtsbasedonenergy   |     |     |
demandestimation

SINGHETAL. 739
Technology Arrangements, and Perspectives” by Stefanov et al. dominance of the three nations the US, UK, and China respectively
(2004)appearedinthejournal“IEEETransactionsonNeuralSystems was again observed here. With about 81% of the publications pub-
and Rehabilitation Engineering” and explored the various ways lishedafter2017,wemaysaythatthisSDGhasrecentlystartedgain-
throughwhichsmarthomescanhelptheagedanddisabledpeoplein ing attention among the AI researcher community. The major
thecurrentscenario.Thepaper“Surveyofcomputationalintelligence contributingsubjectareastothisSDGarefoundtobeInformation&
asthebasistobigfloodmanagement:challenges,researchdirections ComputingScience(33.41%papers)andLaw&LegalStudies(22.61%
andfuturework”byFotovatikhahetal.(2018)wasanotherinterest- papers)(seeFigure6).“NeuralNetwork”and“BigData”wereoneof
ingreviewpapertohaveexploredtheAIandCI(computationalintelli- themostingeminatedconceptsrelatingtoAIinthearea.Ontheother
gence)basedapproachesfortheproblemof thefloodmanagement. hand, “Human Rights” and “Legal Regulations” were their domain-
Anotherinterestingpublicationwithhighattentionwas“Longshort- specific counterparts, suggesting, an emphasis on non-conventional
term memory neural network for air pollutant concentration predic- methods to supplement the conventional onses in these sensitive
tions: Method development and evaluation” by Li et al. (2017) pub- areas(seeFigureA6inAppendixB).
lished in the “Environment Pollution” journal. It proposed a novel Now we look at some of the most cited publications in this
LSTME-based model to predict the air pollutant concentration to domain.Thepublicationwiththemostattention(citation=821)was
ensureabetterstandardoflivinginbigcities.AIapplicationsinsmart “Stop explaining black box machine learning models for high stakes
buildings and homes and pollution related aspects is a major focus decisionsanduseinterpretablemodelsinstead”byRudin(2019)pub-
areainthisSDG. lishedinthejournal“NatureMachineIntelligence”,anditstressedthe
interpretabilityofAIandmachinelearning-basedalgorithmsforcrimi-
nal justice and medicine. Another notable publication “Explainable
5.5.1 | TrendsofknowledgeflowinAI4SDG Artificial Intelligence (XAI): Concepts, taxonomies, opportunities, and
researchrelatedtoSDG11 challenges toward responsible AI” by Arrieta et al. (2020) was a
reviewpaperinasimilardiscipline,thatis,explainableAIandittried
ThepathanalysisofthepapersinthisdomainshowthatSDG11net- to segregate different societal stakeholders in the AI paradigm and
workconsistsof1149nodesand798links.Twochainscanbeseenin identifiedtheirchallengesintrustingAIusingataxonomicalapproach.
the most relevant path obtained from the citation network Suicideshavebecomeaseriousissuelatelyinourmodernsociety,as
(Figure11),namely,Xuetal.(2018)–Abdollahietal.(2020)andXu shownbyapaper“PredictingSuicidesAfterPsychiatricHospitalization
et al. (2018) – Abdollahi et al. (2020) ‘a’. It is also noteworthy that inUSArmySoldiers:TheArmyStudytoAssessRiskandResiliencein
theexistingresearchinAI4SDGrelatedtoSDG11isrelativelyrecent, Servicemembers(ArmySTARRS)”byKessleretal.(2015).Thepaper
startingonlyin2017–18. proposes a regression tree-based ML model that was trained on
ThestudiesinSDG11wererelatedtotheareasofBuildingSeg- data collected from various sources like sociodemographic, US Army
mentation,Extraction,Footprintestimationbasedinpatternrecogni- career, criminal justice, pharmacy, and so forth, to predict the post-
tionandusingcomputervisionmodels(Table6). hospitalisation suicide possibilities in US soldiers. One more popular
paperinthedomainwas“Theaccuracy,fairness,andlimitsofpredict-
ingrecidivism”byDresselandFarid(2018).Thatcriticisedtheexisting
5.6 | SDG16–Peace,justice,andstrong criminalriskassessmenttoolbeingusedforthepurposeandcompared
institutions theresultswithahumanbasedprediction.ExplainabilityofAImodels
fortasksinthisdomainisakeyresearchareainthisdomain.
ItisoneofthemostversatilegoalsamongSDGs.Itstressesonensur-
ingruleoflawatalllevels(national/international), reducingviolence
anddeathsamongallclassesof socialstrata,warranting transparent 5.6.1 | TrendsofknowledgeflowinAI4SDG
and responsive governmental institutions, and assuring justice to all. researchrelatedtoSDG16.
This SDG also had a fair share of AI implications as a total of
(n=1059) publications appeared in the publication data. The ThepathanalysisofthepapersinthisdomainshowthatSDG16net-
workconsistsof703nodesand251links.Thehighestrelevancewas
seen for the path shown in Figure 12. There are three chains, Berk
(2009)–Berneckeretal.(2018),Berk(2009)–Rosellinietal.(2018),
andBerk(2009)–Ghasemietal.(2020).Thesechainsconsistofthree
nodesofdivergencenamely,BeckandBleich(2013),Rosellinietal.
(2015),andStreetetal.(2016).
It is observed that the main areas of application of AI for SDG
16were,Criminology,PublicHealthandPsychologywithmostofthe
FIGURE 11 Mostprominentpathofknowledgeflowinthe studies being based on predictive models based on regression tech-
citationnetworkofpublicationsonSDG11. niques(Table7).
10991719,
2024,
1, Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1002/sd.2706
by
NICE,
National
Institute
for
Health
and
Care
Excellence,
Wiley
Online
Library
on
[29/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

 10991719, 2024, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/sd.2706 by NICE, National Institute for Health and Care Excellence, Wiley Online Library on [29/06/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
740 SINGHETAL.
TABLE 6 Year-wiselistingofmajorareasofapplicationandtargetsinSDG11,artificialintelligence(AI)methodsandmodelsused,natureof
thestudy,andresearchfindingsoftheavailableliteraturededucedusingpathanalysis.
SDG11
| Area(s)of | target | AImethod(s)/Models | Natureof |     |
| --------- | ------ | ------------------ | -------- | --- |
Year application Theme covered studied/used thestudy Inference/Conclusion
2018 Building Remote 11.3 DeepLearning,Residual Validation AsegmentationmodelusingCNNand
Segmentation Sensing/ 11.B NeuralNetwork Study guidedfilterwithhighaccuracyof
Computer buildingidentificationinRemote
Vision sensingimages
2018 Building DeepLearning,Dense DenseAttentionNetworkprovidesan
| Extraction    |     | AttentionNetworks   |     | improvementonDenseNets           |
| ------------- | --- | ------------------- | --- | -------------------------------- |
| 2018          |     | CNN,Richer          |     | RCFnetwork-basedmodelwithbetter  |
|               |     | ConvolutionFeatures |     | F-measuresthantypicalmethodsfor  |
|               |     | Networks            |     | buildingedgedetection            |
| 2019 Building |     | DeepLearningbased   |     | HybridU-netbasedsemantic         |
| Footprint/    |     | Segmentation        |     | segmentationmodelusingGISmap     |
| Pattern       |     | Methods             |     | datasetsalongwithsatelliteimages |
Recognition
| 2019 Building |     | CNN,Deep       |     | Deeplearningmodelusingspatial   |
| ------------- | --- | -------------- | --- | ------------------------------- |
| Extraction    |     | Convolutional  |     | pyramidpoolingandencoder-decode |
|               |     | EncoderDecoder |     | withincreasedefficiency         |
Model
| 2020 |     | CNN,FullyConvolution |     | Non-localResidualU-ShapeNetwork |
| ---- | --- | -------------------- | --- | ------------------------------- |
|      |     | Network              |     | composedofU-Shapeencoder-       |
decoderandnon-localblockhas
improvedmeasuresoverpreviousstate
ofartsemanticsegmentationmodels
(FCN8s,U-Net,SegNet,Deeplab3)
SegUNet–ahybridDeepNeural
| 2020 Building |     | CNN,Deep |     |     |
| ------------- | --- | -------- | --- | --- |
Segmentation ConvolutionSegenet Networkshowsimprovedperformance
|     |     | &Unetnetwork |     | inbuildingsegmentationofFCN |
| --- | --- | ------------ | --- | --------------------------- |
Network
2020 BuildingFootprint GAN,BConvLSTM Anend-to-endCNNmodelcalled
GenerativeAdversarialNetwork(using
SegNet&BConvLSTM)withbetter
buildingseparationaccuracy.
Abbreviations:BConvLSTM,bi-directionalconvolutionalLSTM;GAN,generativeadversarialnetworks.
|     |     |     | FIGURE | 12 Mostprominentpathof |
| --- | --- | --- | ------ | ---------------------- |
knowledgeflowinthecitationnetworkof
publicationsonSDG16.
5.7 | Summarisingtheobservedpatternsin
Tables2,3,4,5,6and7showtheareasofapplication,themes,SDG
detailedanalysis targets covered, AI methods/models studied/used, nature of studies
andinferencesdrawnfromthestudiesregardingtheimpactofAIon
The detailed analysis of articles featuring on the most prominent theapplicationarea.Among thearticlefeaturedonthemostpromi-
pathsforeachofthesixselectedSDGsprovidedinsightsonthechar- nentpathsofknowledgeflowinthecitationnetworkofpublications,
acteristicsof knowledgeflowin therespectivedomainsofresearch. thetrendsofknowledgeflowareasfollows.

 10991719, 2024, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/sd.2706 by NICE, National Institute for Health and Care Excellence, Wiley Online Library on [29/06/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
SINGHETAL. 741
ycaruccaevitciderptsedomevahsledomdesabCFR
|                                                                                                                                                              | yfissalcotdesuebnacsdohteMgninraelenihcaM |                                              | nisseccuslaitrapdahseuqinhcetgninraelenihcaM | gnitsacerofgnivorpministesatadtnereffidfoeloR |     | latnemgniyfissalcrofledomgninraelelbmesnenA |                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------- | -------------------------------------------- | -------------------------------------------- | --------------------------------------------- | --- | ------------------------------------------- | ----------------------------------------- |
| elbaliavaehtfosgnidnifhcraeserdna,ydutsehtfoerutan,desusledomdnasdohtem)IA(ecnegilletnilaicifitra,61GDSnistegratdnanoitacilppafosaerarojamfognitsilesiw-raeY |                                           | gnitsacerofygolonimircgnilledomnignimoctrohS |                                              |                                               |     |                                             | sdohtemyrotnevnItnemeganaMesaC/ecivreS    |
|                                                                                                                                                              |                                           | enihcamotevitanretlanasaseertnoitacifissalC  |                                              | slaudividniksirhgihgniyfitnedinisnoitciderp   |     |                                             | foleveLnahtevitceffeeromsigninraelenihcaM |
ruoivaheblanimircgnitsacerofrofgninrael
rofsledomdesabgninraeLenihcaMfoesU
desabgninraelenihcaMesuotytilibissoP
sledoMgninraeLenihcaMfoycarucca
ruoivaheblanimircgnitciderprof
ruoivahebs'reidlosgnitciderp
noitaborpfoeruliaffoksir
slaudividnifoksirhtlaeh
ruoivaheblaudividni
|     | noisulcnoC/ecnerefnI |     |     |     |     |     | secneffolauxesrof |
| --- | -------------------- | --- | --- | --- | --- | --- | ----------------- |
ehtfoerutaN
|     |            | sisylanA evitpircseD sisylanA | sisylanA |     |     |     |     |
| --- | ---------- | ----------------------------- | -------- | --- | --- | --- | --- |
|     | evitciderP | evitciderP                    |          |     |     |     |     |
yduts
|     |     |     |     | modnaR,noissergeRdesilaneP,noissergeResiwpetS | tseroFmodnaR,ledoMnoissergeRraeniLdesilaneP |     |     |
| --- | --- | --- | --- | --------------------------------------------- | ------------------------------------------- | --- | --- |
modnaR,noissergeResiwpetSnoitadilaV-ssorC
sdohtemLMelpitlumgnisugninraelelbmesnE
MVSdnastseroFmodnaR,eerTnoisiceD
|     | desu/deidutssledoM/)s(dohtemIA |     |     |     |     | sledoMnoitacifissalCtseroFmodnaR |     |
| --- | ------------------------------ | --- | --- | --- | --- | -------------------------------- | --- |
eerTnoissergeRdnanoitacifissalC
|     |     |     | noissergeRdesilaneP,stserof | sisylanAlavivruSemiTetercsiD |     |     |     |
| --- | --- | --- | --------------------------- | ---------------------------- | --- | --- | --- |
seerTsnoitacifissalC
eerTnoisiceD
tseroF
tegrat61GDS
derevoc
|     | 1.61 | A.61 |     | 1.61 | 7.61 A.61 | 1.61 7.61 2.61 | 1.61 4.61 A.61 |
| --- | ---- | ---- | --- | ---- | --------- | -------------- | -------------- |
htlaeHlatneM
|     |           | gnitsaceroF |     |     |     |           | gnitsaceroF |
| --- | --------- | ----------- | --- | --- | --- | --------- | ----------- |
|     | ruoivaheB |             |     |     |     | ruoivaheB |             |
.sisylanahtapgnisudecudederutaretil emehT
|     |                         |                         | htlaeHcilbuP | htlaeHcilbuP htlaeHcilbuP |            |                       |             |
| --- | ----------------------- | ----------------------- | ------------ | ------------------------- | ---------- | --------------------- | ----------- |
|     | noitacilppa ygolonimirC | ygolonimirC ygolonimirC |              |                           | ygolohcysP | ygolohcysP ygolohcysP | ygolonimirC |
fo)s(aerA
7
ELBAT
|     | 9002 | 3102 3102 | 5102 | 6102 8102 | 8102 | 8102 9102 | 0202 |
| --- | ---- | --------- | ---- | --------- | ---- | --------- | ---- |
raeY

742 SINGHETAL.
FIGURE 13 ThematicareasofresearchandtheAImethodsusedinstudiesfocusedonSDGs3,4,7,11,13and16forarticlesidentified
throughpathanalysis.AI,artificialintelligence;SDGs,SustainableDevelopmentGoals.
1. SDG 3 consisted of Genetics, Pharmaco-genomics, Psychology studiesutilisedregression-basedMachinelearningtechniquessuch
related papers using Deep Learning, and Ensemble Learning as Decision tree, Random Forest, SVM, and ML based ensemble
methodsofAI(Figure13). methods(Figure13).
2. SDG 7 consisted of Energy Efficient Houses/ Smart Electricity
Grids, and Energy generation and optimisation related papers Foranalternativevisualisationofthefindingsofthepathanalysis
usingSoftComputing,DistributedAI,DeepLearning,andsomehybrid andsubsequentcontentanalysisoftheliteratureonAI4SDG,Table8
approachescombiningdeeplearningandmachinelearning(Figure13). presents thelistof majorapplication areas,topkeywords,topthree
3. SDG 4 has papers related to Online Education and project team countrycollaborationsandtheSDGtargetsaddressedbythearticles
efficiencies in Software Development industry. These studies featuredonthemostprominentpathsinpathanalysis.
focusedonpredictiveandrecommendationanalysisusingmodels ItwasfoundthattheoverallnumberofpublicationsonAI4SDG
suchasJ48,SVM,andNeuralNetworks(Figure13). has increased all across the world, with a major focus on six SDGs
4. MostprominentpathsincaseofSDG11consistofpapersrelated (3, 4, 7, 11, 13, & 16). Two of these, SDG 3 (Good Health & Well-
to Remote Sensing and Computer vision. These utilised specific being) and SDG 7 (Affordable and Clean Energy) were found as the
computer vision techniques for image processing, such as GAN, areaswithmostapplicationsofAI.Simplemachinelearninganddata
CNNanditsvariants.HybridapproachessuchasBi-directionalCon- analytics techniques such as Decision Tree, Random Forest, SVM,
volutionalLSTMarealsousedinrecentpublications(Figure13). SVR, Multiple linear regression, and so forth, were widely used in
5. IncaseofSDG13,prominentpathshavepapersrelatedtoRenew- someofthemostinfluentialstudies.Somestudiesalsousedrecom-
able energy generation and Efficient electricity grid management mendation analysisusing modelssuchas J48, SVM,and so forth. In
approaches. Predictive analysis using regression techniques like addition, more intricate deep learning techniques like Neural Net-
SVR,Multiplelinearregression,andensembleapproachesnamely, worksandComputerVision,suchasGAN,CNN,ANNandtheirvari-
GBMandXGB(Figure13). ants are now being applied in AI4SDG. Some hybrid approaches
6. SDG16hadstudiesmainlyfocusingonbehaviourforecastingand combining deep learning and machine learning (such as SegUNet,
mental health of convicts, soldiers, and victims of trauma. These Bi-directionalConvolutionalLSTM,etc.),ensembleapproaches(GBM
10991719,
2024,
1,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1002/sd.2706
by
NICE,
National
Institute
for
Health
and
Care
Excellence,
Wiley
Online
Library
on
[29/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

SINGHETAL. 743
TABLE 8 Trendsinappliedresearchandknowledgeflowintop6SustainableDevelopmentGoals(SDGs).
Topcountry SDGtargets
SDG Applicationareas Topkeyword collaborations addressed(No)*
SDG3–GoodHealthandWell Precision/GenomicMedicine ConvolutionalNeural US-China 3.4,3.D(2)
Being Networks US-UK
US-Canada
SDG7–AffordableandClean EnergyEfficientHouses/SmartGrids, NeuralNetwork China-US 7.2,7.3,7.A(3)
Energy EnergyGenerationandOptimisation China-Aus
Aus-US
SDG4–QualityEducation OnlineEducation,SoftwareDevelopment LearningApproach US-Canada 4.4,4.A(2)
US-China
US-UK
SDG13–ClimateAction RenewableEnergy,GridManagement ClimateChange US-China 13.1,13.2,13.3,13.
US-UK B(4)
US-Canada
SDG11–SustainableCities RemoteSensing/ComputerVision SmartCities China-US 11.3,11.B(2)
andCommunities China-UK
China-Aus
SDG16–Peace,Justice,and BehaviourForecasting,MentalHealth ArtificialIntelligence US-UK 16.1,16.2,16.4,
StrongInstitutions US-China 16.7,16.A(5)
US-Germany
Note:*AlistoftheSDGtargetsfeaturedinthisstudyisprovidedinAppendixC.
andXGB,etc.)havealsobeenappliedbyresearchersinrecentyears. prominent literature in the respective areas. This work quantifies the
Inaddition,avariationinappliedtechniqueswasalsoseenbasedon totalresearchactivityonAIforSDGsfromdifferentpartsoftheworld,
theareaofapplication. analysehowhasitchangedovertime,identifieswhichregionsofthe
worldareworkingtowardsAIapplicationstoSDGsandhowdothey
collaborate with each other for this purpose (RQ1 and RQ2). Our
6 | PRACTICAL IMPLICATIONS/ resultsreflectanincrementaltrendinoverallpublicationsontheappli-
USEFULNESS OF THE STUDY RESULTS cationofAIforSDGsacrossthedifferentregionsoftheworld.SDGs
3 (good health & well-being) and 7 (affordable and clean energy) are
The findings of the study present a comprehensive picture of the foundastheareaswiththemostapplicationsofAI.SDG4(qualityedu-
research and application landscape of AI with respect to the SDGs. cation),SDG13(climateaction),SDG11(sustainablecitiesandcommu-
Someofthepracticaluses/implicationsoftheresultsareasfollows. nities)andSDG16(peace,justiceandstronginstitutions)aretheother
SDGswhereAIapproachesandtechniquesareapplied.Inaddition,the
1. SpecificareasofSDGswhereAIcanbeappliedareidentified.Fur- studyhasanalysedtheknowledgeflowsinAIresearchforSDGsand
ther,specificmethods/modelsappliedintheseareasarealsoiden- has identified major application areas along with AI methods and
tified. This is essential information which can guide regional, modelsappliedtoaddressdifferentSDGtargets(RQ3andRQ4).
nationalandinternationalAIstrategies. These observations can form the basis for researchers, and uni-
2. DifferentialfocusofAIonSDGsandregion-specific patternsare versities to invest in the upcoming or neglected areas of SDG
identifiedwhichcanbeusedtoinstituteappropriateactionplans research, including application of AI for the purpose. Governments
for utilising AI technologies in the domain of SDGs in the given can realign their policies and programmes to boost certain activities
national/regionalcontext. basedontheirnationalandregionalpreferences.Someoftheobser-
3. Major publication venues where AI research focused on SDGs is vationsspeciallyfromthecontent-analysissectionaresubjectiveand
published are identified, this can help researchers, policymakers may vary in future studies depending on the analytical framework
and practitionersin benefittingfromandalso contributingto the chosenbytheresearchers,buttheyprovidevaluableinsightsintothe
existingbodyofknowledge. growth and development of the discipline. Alternative methods for
conducting these analyses can be explored in future studies.
Researchers can focus on domain specific studies to provide micro-
7 | CONCLUSION scopic picture of the progress in selected domains. Regional differ-
encesintrendsofresearchareanotherareawheresimilarstudiescan
Thisstudypresentsanin-depthanalysisoftheavailableliteraturein be directedto prepare country/region specific recommendations for
theareaofAI4SDG.Thepath-analysisandcontent-analysissections policyandgovernanceinterventions(Goh&Vinuesa,2021)foraccel-
highlight the important areas of activity and identify the most eratingprogresstowardstheachievementoftheSDGs.
10991719,
2024,
1,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1002/sd.2706
by
NICE,
National
Institute
for
Health
and
Care
Excellence,
Wiley
Online
Library
on
[29/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

 10991719, 2024, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/sd.2706 by NICE, National Institute for Health and Care Excellence, Wiley Online Library on [29/06/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| 744 |     |     |     |     |     |     |     |     |     | SINGHETAL. |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- |
ACKNOWLEDGEMENTS Farrukh,M.,Meng,F.,Wu,Y.,&Nawaz,K.(2020).Twenty-eightyearsof
The authors would like to acknowledge the support in form of the businessstrategyandtheenvironmentresearch:Abibliometricanaly-
sis.BusinessStrategyandtheEnvironment,29(6),2572–2582.
| extramural | research grant | no. MTR/2020/000625 | from Science and |     |     |     |     |     |     |     |     |
| ---------- | -------------- | ------------------- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Foley,A.M.,Leahy,P.G.,Marvuglia,A.,&McKeogh,E.J.(2012).Current
EngineeringResearchBoard(SERB),India,andbyHPEArubaCentre
|     |     |     |     | methods | and | advances | in forecasting | of  | wind power | generation. |     |
| --- | --- | --- | --- | ------- | --- | -------- | -------------- | --- | ---------- | ----------- | --- |
forResearchinInformationSystemsatBHU(No.M-22-69ofBHU). RenewableEnergy,37(1),1–8.
|     |     |     |     | Fotovatikhah,           | F., | Herrera, | M., Shamshirband, |               | S.,    | Chau,       | K. W., |
| --- | --- | --- | --- | ----------------------- | --- | -------- | ----------------- | ------------- | ------ | ----------- | ------ |
|     |     |     |     | FaizollahzadehArdabili, |     | S.,      | & Piran,          | M. J. (2018). | Survey | of computa- |        |
CONFLICTOFINTERESTSTATEMENT
|     |     |     |     | tional | intelligence | as basis | to  | big flood | management: | Challenges, |     |
| --- | --- | --- | --- | ------ | ------------ | -------- | --- | --------- | ----------- | ----------- | --- |
The authors declare that the manuscript complies with ethical stan- researchdirectionsandfuturework.EngineeringApplicationsofCom-
dardsofthejournalandthereisnoconflictofinterestswhatsoever. putationalFluidMechanics,12(1),411–437.
|     |     |     |     | Garfield, E.,Sher, |             | I. H.,&Torpie, | R.J.(1964). |     | Theuse     | ofcitationdatain |     |
| --- | --- | --- | --- | ------------------ | ----------- | -------------- | ----------- | --- | ---------- | ---------------- | --- |
|     |     |     |     | writing            | the history | of science.    | Institute   | for | Scientific | Information      | Inc |
ORCID
PhiladelphiaPA.
AnuragKanaujia https://orcid.org/0000-0002-5813-7427 Goh,H.H.,&Vinuesa,R.(2021).Regulatingartificial-intelligenceapplica-
tionstoachievetheSustainableDevelopmentGoals.DiscoverSustain-
| VivekKumarSingh | https://orcid.org/0000-0002-7348-6545 |     |     |     |     |     |     |     |     |     |     |
| --------------- | ------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ability,2(52),1–6.https://doi.org/10.1007/s43621-021-00064-5
Goralski,M.A.,&Tan,T.K.(2020).Artificialintelligenceandsustainable
REFERENCES development. The International Journal of Management Education,
18(1),100330.
Allen,C.,Reid,M.,Thwaites,J.,Glover,R.,&Kestin,T.(2020).Assessing
|     |     |     |     | Graesser, | A. C., | Lu, S., Jackson, | G.  | T., Mitchell, | H.  | H., Ventura, | M., |
| --- | --- | --- | --- | --------- | ------ | ---------------- | --- | ------------- | --- | ------------ | --- |
nationalprogressandprioritiesfortheSustainableDevelopmentGoals
(SDGs): Experience from Australia. Sustainability Science, 15(2), Olney,A.,&Louwerse,M.M.(2004).AutoTutor:Atutorwithdialogue
521–538. in natural language. Behavior Research Methods, Instruments, & Com-
Anderson,E.F.,McLoughlin,L.,Liarokapis,F.,Peters,C.,Petridis,P.,&De puters,36(2),180–192.
Freitas, S. (2010). Developing serious games for cultural heritage: A Gupta, S., Langhans, S. D., Domisch, S., Fuso-Nerini, F., Felländer, A.,
state-of-the-artreview.VirtualReality,14(4),255–275. Battaglini,M.,Tegmark,M.,&Vinuesa,R.(2021).Assessingwhether
Arrieta, A. B., Díaz-Rodríguez, N., Del Ser, J., Bennetot, A., Tabik, S., artificial intelligence is an enabler or an inhibitor of sustainability at
Barbado, A., García, S., Gil-Lo(cid:2)pez, S., Molina, D., Benjamins, R., & indicatorlevel.TransportationEngineering,4,100064.
Chatila, R. (2020). Explainable artificial intelligence (XAI): Concepts, Haenlein,M.,&Kaplan,A.(2019).Abriefhistoryofartificialintelligence:
|     |     |     |     | On the | past, | present, and | future | of artificial | intelligence. |     | California |
| --- | --- | --- | --- | ------ | ----- | ------------ | ------ | ------------- | ------------- | --- | ---------- |
taxonomies,opportunitiesandchallengestowardresponsibleAI.Infor-
| mationFusion,58,82–115. |     |     |     | ManagementReview,61(4),5–14. |     |     |     |     |     |     |     |
| ----------------------- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- |
Batagelj,V.(2003).Efficientalgorithmsforcitationnetworkanalysis,arXiv Hummon,N.P.,&Dereian,P.(1989).Connectivityinacitationnetwork:
ThedevelopmentofDNAtheory.SocialNetworks,11(1),39–63.
preprint,arXiv:cs/0309023.
Baum, K., Bryson, J., Dignum, F., Dignum, V., Grobelnik, M., Hoos, H., Jain,R.K.,Smith,K.M.,Culligan,P.J.,&Taylor,J.E.(2014).Forecasting
Irgens, M., Lukowicz, P., Muller, C., Rossi, F., & Shawe-Taylor, J. energyconsumptionofmulti-familyresidentialbuildingsusingsupport
(2023). Fromfeartoaction:AIgovernanceandopportunitiesforall. vector regression: Investigating the impact of temporal and spatial
Frontiers in Computer Science, 5, 49. https://doi.org/10.3389/fcomp. monitoringgranularityonperformanceaccuracy.AppliedEnergy,123,
| 2023.1210421 |     |     |     | 168–178. |     |     |     |     |     |     |     |
| ------------ | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
Biswas, G., Leelawong, K., Schwartz, D., Vye, N., & The Teachable Agents Jo,S.J.,Jeung,C.W.,Park,S.,&Yoon,H.J.(2009).Whoiscitingwhom:
|     |     |     |     | Citation | network | analysis | among | HRD publications |     | from | 1990 to |
| --- | --- | --- | --- | -------- | ------- | -------- | ----- | ---------------- | --- | ---- | ------- |
GroupatVanderbilt.(2005).Learningbyteaching:Anewagentparadigm
foreducationalsoftware.AppliedArtificialIntelligence,19(3–4),363–392. 2007.HumanResourceDevelopmentQuarterly,20(4),503–537.
Borgatti,S.P.(2005).Centralityandnetworkflow.SocialNetworks,27(1), Jung, M., Reichstein, M., Ciais, P., Seneviratne, S. I., Sheffield, J.,
55–71. Goulden, M. L., Bonan, G., Cescatti, A., Chen, J., De Jeu, R., &
Brughmans,T.(2013).Networksofnetworks:Acitationnetworkanalysis Dolman,A.J.(2010).Recentdeclineinthegloballandevapotranspira-
oftheadoption,use,andadaptationofformalnetworktechniquesin tiontrendduetolimitedmoisturesupply.Nature,467(7318),951–954.
archaeology.LiteraryandLinguisticComputing,28(4),538–562. Kessler, R. C., Warner, C. H., Ivany, C., Petukhova, M. V., Rose, S.,
Chaouachi,A.,Kamel,R.M.,Andoulsi,R.,&Nagasaka,K.(2012).Multiob- Bromet, E. J., Brown, M., Cai, T., Colpe, L. J., Cox, K. L., &
jective intelligent energy management for a microgrid. IEEE Transac- Fullerton,C.S.(2015).Predictingsuicidesafterpsychiatrichospitaliza-
tionsonIndustrialElectronics,60(4),1688–1699. tioninUSArmysoldiers:TheArmystudytoassessriskandresilience
inservicemembers(ArmySTARRS).JAMAPsychiatry,72(1),49–57.
| Chiang, M., | & Zhang, T. (2016). | Fog and IoT: | An overview of research |     |     |     |     |     |     |     |     |
| ----------- | ------------------- | ------------ | ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
opportunities.IEEEInternetofThingsJournal,3(6),854–864. Kong,W.,Dong,Z.Y.,Jia,Y.,Hill,D.J.,Xu,Y.,&Zhang,Y.(2017).Short-
Chui, M., Harryson, M., Manyika, J., Roberts, R., Chung, R., van termresidentialloadforecastingbasedonLSTMrecurrentneuralnet-
work.IEEETransactionsonSmartGrid,10(1),841–851.
Heteren,A.,&Nel,P.(2018).NotesfromtheAIfrontier:ApplyingAI
forsocialgood.McKinseyGlobalInstitute,3. Kumar,S.,Sureka,R.,Lim,W.M.,KumarMangla,S.,&Goyal,N.(2021).
DeSollaPrice,D.J.(1965).Networksofscientificpapers:Thepatternof What do we know about business strategy and environmental
bibliographicreferencesindicatesthenatureofthescientificresearch research?Insightsfrombusinessstrategyandtheenvironment.Busi-
front.Science,149(3683),510–515. nessStrategyandtheEnvironment,30(8),3454–3469.
Deng,L.,&Li,X.(2013).Machinelearningparadigmsforspeechrecogni- Lambin,P.,Leijenaar,R.T.,Deist,T.M.,Peerlings,J.,DeJong,E.E.,Van
tion: An overview. IEEE Transactions on Audio, Speech and Language Timmeren,J.,Sanduleanu,S.,Larue,R.T.,Even,A.J.,Jochems,A.,&
Processing,21(5),1060–1089. VanWijk,Y.(2017).Radiomics:Thebridgebetweenmedicalimaging
|             |                     |             |                         | and personalized |     | medicine. | Nature | Reviews.Clinical |     | Oncology, | 14(12), |
| ----------- | ------------------- | ----------- | ----------------------- | ---------------- | --- | --------- | ------ | ---------------- | --- | --------- | ------- |
| Donthu, N., | Kumar,S.,Mukherjee, | D., Pandey, | N., & Lim, W.M. (2021). |                  |     |           |        |                  |     |           |         |
749–762.
Howtoconductabibliometricanalysis:Anoverviewandguidelines.
JournalofBusinessResearch,133,285–296. Lathabai,H.H.,George,S.,Prabhakaran,T.,&Changat,M.(2018).Aninte-
Dressel,J.,&Farid,H.(2018).Theaccuracy,fairness,andlimitsofpredict- grated approach to path analysis for weighted citation networks.
ingrecidivism.ScienceAdvances,4(1),eaao5580. Scientometrics,117(3),1871–1904.

SINGHETAL. 745
Lathabai,H.H.,Prabhakaran,T.,&Changat,M.(2015).Centralityandflow Stefanov,D.H.,Bien,Z.,&Bang,W.C.(2004).Thesmarthouseforolder
vergence gradient based path analysis of scientific literature: A case persons and persons with physical disabilities: Structure, technology
studyofbiotechnologyforengineering.PhysicaA:StatisticalMechanics arrangements, and perspectives. IEEE Transactions on Neural Systems
anditsApplications,429,157–168. andRehabilitationEngineering,12(2),228–250.
Lathabai,H.H.,Prabhakaran,T.,&Changat,M.(2017).Contextualproduc- Tampubolon,G.,&Ramlogan,R.(2007).Networksandtemporalityinthe
tivity assessment of authors and journals: A network scientometric developmentofaradicalmedicaltreatment.GraduateJournalofSocial
approach.Scientometrics,110(2),711–737. Science,4(1),54–77.
Li, L., Qin, L., Xu, Z., Yin, Y., Wang, X., Kong, B., Bai, J.,Lu, Y., Fang, Z., Van Griethuysen, J. J., Fedorov, A., Parmar, C., Hosny, A., Aucoin, N.,
Song,Q.,&Cao,K.(2020).ArtificialintelligencedistinguishesCOVID- Narayan, V., Beets-Tan, R. G., Fillion-Robin, J. C., Pieper, S., &
19fromcommunityacquiredpneumoniaonchestCT.Radiology,296, Aerts, H. J. (2017). Computational radiomics system to decode the
E65–E71. radiographicphenotype.CancerResearch,77(21),e104–e107.
Li,X.,Peng,L.,Yao,X.,Cui,S.,Hu,Y.,You,C.,&Chi,T.(2017).Longshort- Vinuesa, R., Azizpour, H., Leite, I., Balaam, M., Dignum, V., Domisch, S.,
term memory neural network for air pollutant concentration predic- Felländer,A.,Langhans,S.D.,Tegmark,M.,&FusoNerini,F.(2020).
tions: Method development and evaluation. Environmental Pollution, TheroleofartificialintelligenceinachievingtheSustainableDevelop-
231,997–1004. mentGoals.NatureCommunications,11(1),1–10.
Liengpunsakul, S. (2021). Artificial intelligence and sustainable develop- Vinuesa,R.,&Sirmacek,B.(2021).Interpretabledeep-learningmodelsto
mentinChina.TheChineseEconomy,54(4),235–248. help achieve the Sustainable Development Goals. Nature Machine
Liu,J.S.,&Lu,L.Y.(2012).Anintegratedapproachformainpathanalysis: Intelligence,3(11),926.
DevelopmentoftheHirschindexasanexample.JournaloftheAmeri- Vinuesa,R.,Theodorou,A.,Battaglini,M.,&Dignum,V.(2020).Asocio-
canSocietyforInformationScienceandTechnology,63(3),528–542. technicalframeworkfordigitalcontacttracing.ResultsinEngineering,
Liu,Y.,Huang,B.,Guo,H.,&Liu,J.(2023).Abigdataapproachtoassess 8,100163.
progresstowardsSustainableDevelopmentGoalsforcitiesofvarying Voyant,C.,Notton, G.,Kalogirou, S.,Nivet,M. L.,Paoli,C.,Motte, F.,&
sizes.CommunicationsEarth&Environment,4(1),66. Fouilloy,A.(2017).Machinelearningmethodsforsolarradiationfore-
Mina,A.,Ramlogan,R.,Tampubolon,G.,&Metcalfe,J.S.(2007).Mapping casting:Areview.RenewableEnergy,105,569–582.
evolutionarytrajectories:Applicationstothegrowthandtransforma- Wamba,S.F.,Bawack,R.E.,Guthrie,C.,Queiroz,M.M.,&Carillo,K.D.A.
tionofmedicalknowledge.ResearchPolicy,36(5),789–806. (2021).ArewepreparingforagoodAIsociety?Abibliometricreview
Moavenzadeh,J.(2015,October).The4thindustrialrevolution:Reshaping andresearchagenda.TechnologicalForecastingandSocialChange,164,
thefutureofproduction.InWorldeconomicforum(p.57).DHLGlobal 120482.
Engineering&ManufacturingSummit. Yeh,S.C.,Wu,A.W.,Yu,H.C.,Wu,H.C.,Kuo,Y.P.,&Chen,P.X.(2021).
Muthukrishnan, N., Maleki, F., Ovens, K., Reinhold, C., Forghani, B., & Public perception of artificial intelligence and its connections to the
Forghani,R.(2020).Briefhistoryofartificialintelligence.Neuroimaging SustainableDevelopmentGoals.Sustainability,13(16),9165.
Clinics,30(4),393–399. Zhao,H.X.,&Magoulès,F.(2012).Areviewonthepredictionofbuilding
NationalStratregyforArtificialIntelligence.(2018).NITIAayog.Retrieved energyconsumption.RenewableandSustainableEnergyReviews,16(6),
from https://niti.gov.in/sites/default/files/2019-01/NationalStrategy- 3586–3592.
for-AI-Discussion-Paper.pdf
Prabhakaran,T.,Lathabai,H.H.,&Changat,M.(2015).Detectionofpara-
digmshiftsandemergingfieldsusingscientificnetwork:Acasestudy
Howtocitethisarticle:Singh,A.,Kanaujia,A.,Singh,V.K.,&
of information Technology for Engineering. Technological Forecasting
andSocialChange,91,124–145. Vinuesa,R.(2024).ArtificialintelligenceforSustainable
Prabhakaran, T., Lathabai, H. H., George, S., & Changat, M. (2018). DevelopmentGoals:Bibliometricpatternsandconcept
Towardspredictionofparadigmshiftsfromscientificliterature.Scien-
evolutiontrajectories.SustainableDevelopment,32(1),
tometrics,117(3),1611–1644.
724–754.https://doi.org/10.1002/sd.2706
Rajkomar,A.,Oren,E.,Chen,K.,Dai,A.M.,Hajaj,N.,Hardt,M.,Liu,P.J.,
Liu,X.,Marcus,J.,Sun,M.,&Sundberg,P.(2018).Scalableandaccu-
ratedeeplearningwithelectronichealthrecords.NPJDigitalMedicine,
1(1),1–10.
Rudin, C.(2019). Stopexplaining black box machine learning modelsfor
high stakes decisions and use interpretable models instead. Nature APPENDIXA
MachineIntelligence,1(5),206–215.
Sætra,H.S.(2021).AIincontextandtheSustainableDevelopmentGoals:
Thisappendixbrieflydescribesthesearchpathcount(SPC)andflow
Factoringintheunsustainabilityofthesociotechnicalsystem.Sustain-
ability,13(4),1738. vergence(FV)gradientweightassignmentandsearchschemes.
Sanderman, J., Hengl, T., & Fiske, G. J. (2017). Soil carbon debt of
12,000yearsofhumanlanduse.ProceedingsoftheNationalAcademy
ofSciences,114(36),9575–9580.
A.1. | SPCmethod:Ashortrevisit
Scardoni,G.,&Laudanna,C.(2012).Centralitiesbasedanalysisofcomplex
networks. In Y. Zhang (Ed.), New frontiers in graph theory (pp.
323–348). As mentioned earlier, SPC method is one of the weight-assignment
Singh, A., Kanaujia, A., & Singh, V. K. (2022). Research on Sustainable methodsthatbelongtotheSPXtopic(traversal-basedweightassign-
Development Goals: How has Indian scientific community
mentmethods)developedbyBatagelj(2003).InSPCmethod,identifi-
responded?JournalofScientific&IndustrialResearch,81(11),1147–
cationofallsourcesandsinksinthecitationnetworkisthefirsttask.
1161.
Singh,V.K.,Singh,P.,Karmakar,M.,Leta,J.,&Mayr,P.(2021).Thejournal Then,foreacharcinthenetwork,thenumberofsearchpaths(from
coverage of web of science, Scopus and dimensions: A comparative sourcestosinks)passingthroughitiscomputedandsuchacountis
analysis.Scientometrics,126(6),5113–5142.
assignedasweightofthatarc.
10991719,
2024,
1, Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1002/sd.2706
by
NICE,
National
Institute
for
Health
and
Care
Excellence,
Wiley
Online
Library
on
[29/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

746 SINGHETAL.
A.2. | FVgradientmethod:Ashortrevisit potential paper. This phenomenon was termed as Flow Vergence
effectorFVeffectandwasusedtodetect(Lathabaietal.,2015)and
Scientificcitationnetwork,akindofinformationnetworkisaninter- predict(Prabhakaranetal.,2018)pivotpapersofparadigmshift.Com-
connectedstructureofscholarlypublicationswhicharelinkedthrough putationofFVgradientsmakesthenetworkasignedweightednet-
citationlinksorarcofcitations.Theselinkscanbetreatedasarepre- workandhenceFVgradientmethodofweightassignmenthelpsfor
sentationoftheflowofinformationfromthecitedworktotheciting the retrieval of paths that might not be highlighted through SPX
work. Most of the vertex measures if used independently fails to methods.Toensurethatthearcswithnegativesignsarenotmissed
reflectoneimportantpropertyofavertex(work)inacitationnetwork and given high priority when certain search schemes like key-route
that arises due to the flow of information through it, namely the searchareemployed,thefollowingtransformationofeqn.(2)should
FV. Flow of information through a paper invokes a dominance in bedone.
termsofflowconvergenceorflowdivergence,whichcanbetermed
asflowvergenceby(Prabhakaranetal.,2015).Flowvergencepoten- ΔFV ðnorm:Þ¼1þ max:ΔFV(cid:2)ΔFV ij ð3Þ
ij max:ΔFV(cid:2)min:ΔFV
tialisthepotentialofapapertocontributetothegrowthofafieldvia
theattainmentorimprovementofflowdivergencedominance.Thus,
workswhicharepresentlyinknowledgeflowdivergencemodecanbe Where, max:ΔFV is the highest FV gradient weight in the network
surely regarded as works of high flow vergence potential. Even andmin:ΔFVisthelowestFVgradientweightinthenetwork.
thoughaworkisnotpresentlyinflowdivergencemode,certainworks
canbetreatedasofhighFVpotential.Thishappensonlyifthatwork
succeededindeliveringknowledgetootherworks(thatcitesthecon- A.3. | Searchschemes
cernedwork)thatareatcertainlevelofqualitywhichisreflectedby
eigenvector centrality (Borgatti, 2005). This concept was introduced Forward Search: In forward search, among all the arcs originating
byPrabhakaranetal.(2015)andanindexforreflectingtheflowver- fromallthesources(thepapersthatdonotciteanyotherpaperbut
gencepotentialwasalsodeveloped.FlowVergenceindexorFVindex get at least one citation), the ones with highest weight will be
ofapapericanbecomputedas: selected.Thetargetnodeofthatarcwillbemadethenewsourceand
the same procedure will be repeated in a greedy fashion till
W ¼ indeg i (cid:2)outdeg iþeig ð1Þ sinkpapers(thepapersthatdonotgetcitedyetbuthascitedatleast
FVi indegþoutdeg i
i i one paper) are found. When there are ties, both the arcs will be
considered.
where, indeg, outdeg and eig are the indegree (the number of cita- BackwardSearch:Inbackwardsearch,unliketheforwardsearch,
i i i
tionsreceived),theoutdegree(numberofcitationsmade)andeigen- search originates from sink papers till source papers are obtained.
vector centrality of paper i in the network (Scardoni & Everythingissameasthatofforwardsearch.Thiswasintroducedby
Laudanna, 2012). Now, we move on to discuss the FV gradient (Liu&Lu,2012).
methodasthetheoreticaloriginandrationalebehindtheformulation Global search/Critical path method: In global search method,
of the FV index is already covered by (Lathabai et al., 2018), insteadofselectinganinitialarcanditssubsequentarcsinagreedy
(Prabhakaran et al., 2015), (Lathabai et al., 2015), (Lathabai or‘localbest’fashion,forallthesource-sinkpaths,thetotalweightof
etal.,2017),and(Prabhakaranetal.,2018). the path (which is equal to the sum of weights of all the arcs that
Sinceaciting-citedpairisrelatedbyknowledgeflow,existenceof formsthatpath)willbecomputedandthehighestamongthatwillbe
flowvergencepotentialforcitingandcitedworkalsoimpliestheexis- consideredasthecriticalpath.
tenceofflowvergencegradientorgradientinflowvergencepotential Key-route Search (Local):In key-route search (local), instead of
between them. The potential difference between works i and initiatingsearchfromsourceorsink(whichinvokestheriskofmissing
jconnectedbyanarcofcitationfromjtoicanbetermedasFVgradi- thehighestweightedarcinthenetwork),searchcommencesfromthe
ent(Lathabaietal.,2015)anditcanbecomputedas: terminal nodes of key-route (the highest weighted arc). From cited
workofthekey-route,searchproceedsasthatinbackwardsearchtill
ΔFV
ij
¼W
FVi
(cid:2)W
FVj
: ð2Þ
sourceisobtainedandfromcitingworkofthekey-route,searchpro-
ceedsinthemannerofforwardsearchtillsinkisfound.Thissearch
ThespecialityoftheofFVgradientortheFVpotentialdifference schemeisthekeyinnovationofLiu-Luapproach(Liu&Lu,2012).This
is that, usually, the knowledge flow tends to appear as to have searchcanbeconductedtoretrievemultiplepathswiththeselection
occurredfromaworkofhighFVpotentialtoaworkoflowFVpoten- ofmultiplekey-routes.Forinstance,thesoftwarepackagePAJEKhas
tial.Thus,inmostofthecases,ΔFV takesapositivevalue.However, settheoption1-10asdefaultchoice,bywhichtop10key-routeswill
ij
insomespecialcases,whennewerworks(citingworks)tendtoout- be selected for the search. This choice can be changed by users
perform the former ones (cited ones) due to its intellectual merit or accordingly.
innovativeappealtothescientificcommunity,wecanhaveΔFV <0, Key-routeSearch(global):Inkey-route(global),insteadoftracing
ij
makingknowledgeflowtooccurfromlowpotentialpapertoahigh fromboththeterminalnodesofkey-routestillsourcesandsinksare
10991719,
2024,
1, Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1002/sd.2706
by NICE,
National
Institute
for
Health
and
Care
Excellence,
Wiley
Online
Library
on
[29/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

 10991719, 2024, 1, Downloaded from https://onlinelibrary.wiley.com/doi/10.1002/sd.2706 by NICE, National Institute for Health and Care Excellence, Wiley Online Library on [29/06/2026]. See the Terms and Conditions (https://onlinelibrary.wiley.com/terms-and-conditions) on Wiley Online Library for rules of use; OA articles are governed by the applicable Creative Commons License
| SINGHETAL. |     |     |     |     |     |     |     | 747 |
| ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
approached, a global search is initiated from terminal nodes of key- can also be systematically done with ease.Thus, the paths obtained
routes.Thatmeans,fromallthepathsreachablefromcitingpaperand after text-integrated path analysis (TPA) can be termed as ‘Concept
EvolutionPaths’.ThemethodologyusedforTPAisgivenbelow:
citedpaperinthekey-route,theoneswithlargestsumofweightswill
| bechosen. |     |     |     | ProcedureforextractionofConceptevolutionPaths |     |     |     |     |
| --------- | --- | --- | --- | --------------------------------------------- | --- | --- | --- | --- |
Alongwiththesesearchschemes,aprovisionfortoleranceisalso Input: Citation network of published articles C and Work-Con-
i
proposedby(Liu&Lu,2012)andavailableinPAJEKforlocalsearch cept/KeywordaffiliationsnetworkWK.
schemes such as forward, backward and key-route (local). If a toler- Output:Conceptevolutionpaths
anceof10%(0.1isthedefaultvaluesetinPAJEK)isselected,ateach
step, instead of choosing the largest weighted arc, all the arcs that 1. FromC,extractSPCpathsandFVpaths
i
fallswith-in90%ofitsweightwillbeselected. 2. ForeverypairofpathsP andP
|     |     |     |     |                | i                        | j                      |              |      |
| --- | --- | --- | --- | -------------- | ------------------------ | ---------------------- | ------------ | ---- |
|     |     |     |     | a. Compute     | U ¼jPi jþjPj j(cid:2)jPi | \Pj j , the uniqueness | index ([15]) | of P |
|     |     |     |     |                | PiPj jPi jþjPj           | j                      |              | i    |
|     |     |     |     | withrespecttoP | andvice-versa.           |                        |              |      |
j
≥δ(desirablevalueis0.65),selectboth(b)Otherwise,
| A.4. | Text-integrationforpathanalysis |     |     |     | b. (a)IfU PiPj |      |        |     |     |
| -------------------------------------- | --- | --- | --- | -------------- | ---- | ------ | --- | --- |
|                                        |     |     |     | i. SelectpathP | ifjP | j>jP j |     |     |
|                                        |     |     |     |                | i i  | j      |     |     |
Once,importantpaths(whicharesubnetworksofcitationnetwork)in ii. SelectpathP ifjP j>jP j
|     |     |     |     |     | j j | i   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
theconcernedliteratureareidentified,nodesofthepaths(i.e.,papers) iii. SelectbothifjPj¼jP j
|           |                       |               |                       |                                                      | i   | j   |          |     |
| --------- | --------------------- | ------------- | --------------------- | ---------------------------------------------------- | --- | --- | -------- | --- |
| should be | relabelled or current | vertex labels | should be replaced by |                                                      |     |     |          |     |
|           |                       |               |                       | FromW(cid:2)Knetwork,extractthesubnetworkW(cid:2)KðP |     |     | Þ(whereP |     |
terms or words that best represent the theme/contribution of that 3. x x
paper.In Dimensions, sinceeachpublished articleis associatedwith istheselectedpathatstep3)networkbychoosingconceptwith
‘concepts’thatrepresentcertainkeywordsthatrepresenttherelation highestrelevancescore
ofworkwiththesubfield/fieldinwhichtheworkbelongsto,therela- 4. ObtainconceptevolutionpathsorconceptcitationpathKðP Þ!
x
| bellingcanbeeasilyachievedbymappingthework'slabel/idwiththe |     |     |     | KðP Þusing |     |     |     |     |
| ----------------------------------------------------------- | --- | --- | --- | ---------- | --- | --- | --- | --- |
x
| concept. Also, | since each concept | are associated | with a relevance |     |     |     |     |     |
| -------------- | ------------------ | -------------- | ---------------- | --- | --- | --- | --- | --- |
scoreorscoreofrelevance,selectionofthebestrepresentativeword KðP Þ!KðP Þ¼ðW(cid:2)KðP ÞÞÞT(cid:3)P (cid:3)ðW(cid:2)KðP ÞÞ
|     |     |     |     | x   | x x | x   | x   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

748 SINGHETAL.
APPENDIXB
FIGURE A1 NetworkmapofmostprominentconceptsfromthepublicationsonSDG3drawnusingVOSviewer.Thesizeofnodesshows
theimportanceoftheconcepts.
10991719,
2024,
1,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1002/sd.2706
by
NICE,
National
Institute
for
Health
and
Care
Excellence,
Wiley
Online
Library
on
[29/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

SINGHETAL. 749
FIGURE A2 NetworkmapofmostprominentconceptsfromthepublicationsonSDG7accordingtotheirfrequencyandlinkages.
“convolutionalneuralnetwork”,“neuralnetwork”,“artificialintelligence”,“sensornetworks”,and“IoTdevices”arethetopfiveconcepts
forSDG7.
10991719,
2024,
1,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1002/sd.2706
by
NICE,
National
Institute
for
Health
and
Care
Excellence,
Wiley
Online
Library
on
[29/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

750 SINGHETAL.
FIGURE A3 NetworkmapofmostprominentconceptsfromthepublicationsonSDG4.ThetopfiveconceptsforSDG4are,“learning
approach”,“artificialintelligence”,“StudyProcessQuestionnaire”,“learningenvironment,and“highereducation”.
10991719,
2024,
1,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1002/sd.2706
by
NICE,
National
Institute
for
Health
and
Care
Excellence,
Wiley
Online
Library
on
[29/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

SINGHETAL. 751
FIGURE A4 Conceptclusteranalysis
ofSDG13wasconductedbydrawinga
co-occurrencenetworkofconceptsusing
NetworkXlibrary(python)andplotted
usingVOSviewer.Themostprominent
conceptsforSDG13were“climate
change”,“organiccarbon”,“artificial
neuralnetworks”,“extinctionrisk”and
“extremeevent”.
10991719,
2024,
1,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1002/sd.2706
by
NICE,
National
Institute
for
Health
and
Care
Excellence,
Wiley
Online
Library
on
[29/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

752 SINGHETAL.
FIGURE A5 NetworkmapofmostprominentconceptsfromthepublicationsonSDG11drawnusingVOSviewer.“smartcities”,“deep
learning”,“convolutionalneuralnetwork”,“dataanalytics”,and“smartbuildings”arethetopfiveoccurringconceptsamongpapersfocusingon
SDG11.
10991719,
2024,
1,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1002/sd.2706
by
NICE,
National
Institute
for
Health
and
Care
Excellence,
Wiley
Online
Library
on
[29/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

SINGHETAL. 753
FIGURE A6 NetworkmapofmostprominentconceptsfromthepublicationsonSDG16drawnusingVOSviewer.Thetopfiveconceptsby
frequencyofoccurrenceare,“artificialintelligence”,“humanrights”,“legalregulation”,“convolutionalneuralnetwork”and“ruleoflaw”.
10991719,
2024,
1,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1002/sd.2706
by
NICE,
National
Institute
for
Health
and
Care
Excellence,
Wiley
Online
Library
on
[29/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License

754 SINGHETAL.
APPENDIXC
SDGtargetscoveredbystudiesfeaturinginthemostprominentpathsforAI4SDGresearchpublicationsinselectedsixSDGs.
SDG
targets Targetdescription
3.4 By2030,reducebyonethirdprematuremortalityfromnon-communicablediseasesthroughpreventionandtreatmentandpromote
mentalhealthandwell-being.
3.D Strengthenthecapacityofallcountries,inparticulardevelopingcountries,forearlywarning,riskreductionandmanagementofnational
andglobalhealthrisks.
4.4 By2030,substantiallyincreasethenumberofyouthandadultswhohaverelevantskills,includingtechnicalandvocationalskills,for
employment,decentjobsandentrepreneurship.
4.A Buildandupgradeeducationfacilitiesthatarechild,disabilityandgendersensitiveandprovidesafe,non-violent,inclusiveandeffective
learningenvironmentsforall.
7.2 By2030,increasesubstantiallytheshareofrenewableenergyintheglobalenergymix.
7.3 By2030,doubletheglobalrateofimprovementinenergyefficiency.
7.A By2030,enhanceinternationalcooperationtofacilitateaccesstocleanenergyresearchandtechnology,includingrenewableenergy,
energyefficiencyandadvancedandcleanerfossil-fueltechnology,andpromoteinvestmentinenergyinfrastructureandcleanenergy
technology.
11.3 By2030,enhanceinclusiveandsustainableurbanisationandcapacityforparticipatory,integratedandsustainablehumansettlement
planningandmanagementinallcountries.
11.B By2020,substantiallyincreasethenumberofcitiesandhumansettlementsadoptingandimplementingintegratedpoliciesandplans
towardsinclusion,resourceefficiency,mitigationandadaptationtoclimatechange,resiliencetodisasters,anddevelopand
implement,inlinewiththeSendaiFrameworkforDisasterRiskReduction2015–2030,holisticdisasterriskmanagementatalllevels.
13.1 Strengthenresilienceandadaptivecapacitytoclimate-relatedhazardsandnaturaldisastersinallcountries.
13.2 Integrateclimatechangemeasuresintonationalpolicies,strategiesandplanning.
13.3 Improveeducation,awareness-raisingandhumanandinstitutionalcapacityonclimatechangemitigation,adaptation,impactreduction
andearlywarning.
13.B Promotemechanismsforraisingcapacityforeffectiveclimatechange-relatedplanningandmanagementinleastdevelopedcountries,
includingfocusingonwomen,youthandlocalandmarginalisedcommunities.
16.1 Significantlyreduceallformsofviolenceandrelateddeathrateseverywhere.
16.2 Endabuse,exploitations,traffickingandallformsofviolenceagainstandtortureofchildren.
16.4 By2030,significantlyreduceillicitfinancialandarmsflows,strengthentherecoveryandreturnofstolenassetsandcombatallformsof
organisedcrime.
16.7 Ensureresponsive,inclusive,participatoryandrepresentativedecision-makingatalllevels.
16.A Strengthenrelevantnationalinstitutions,includingthroughinternationalcooperation,forbuildingcapacityatalllevels,inparticularin
developingcountries,topreventviolenceandcombatterrorismandcrime.
10991719,
2024,
1,
Downloaded
from
https://onlinelibrary.wiley.com/doi/10.1002/sd.2706
by
NICE,
National
Institute
for
Health
and
Care
Excellence,
Wiley
Online
Library
on
[29/06/2026].
See
the
Terms
and
Conditions
(https://onlinelibrary.wiley.com/terms-and-conditions)
on
Wiley
Online
Library
for
rules
of
use;
OA
articles
are
governed
by
the
applicable
Creative
Commons
License
