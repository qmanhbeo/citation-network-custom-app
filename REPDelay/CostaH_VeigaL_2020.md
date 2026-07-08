Version of Record: https://www.sciencedirect.com/science/article/pii/S0140988320303959
Manuscript_f25f100514e07e1488975f4e4d644211
| Local | labor impact    | of wind      | energy         | investment: | an       | analysis |
| ----- | --------------- | ------------ | -------------- | ----------- | -------- | -------- |
|       | of              | Portuguese   | municipalities |             |          |          |
|       | H´elia          | Costa        |                | Linda       | Veiga    |          |
|       | Toulouse School | of Economics | ∗              | University  | of Minho | †        |
July 2020
Abstract
InvestmentinwindpowerhasgrownremarkablyinthepastdecadesinPortugal. Although
economicdevelopmentisanargumentforinvestmentincentivepolicies,littleevidenceexists
as to their net impact on local-level unemployment. Using data for all 278 Portuguese
mainland municipalities for the years 1997-2017, we assess the existence, distribution and
durationoflocal-levellaborimpactsofwindpowerinvestment. Ourresultsshowthereare
short-term effects during the construction phase. We estimate a decrease of 0.17 and 0.23
percentage points in the total unemployment rate per 100MW of installed power in each
ofthetwoyearsoftheconstructionphase. Theseeffectsarefeltmainlyforunskilledlabor
andmaleworkers. Furtheranalysisofspatialinteractionfindspositivespatialspilloversfor
municipalities that are 30km or less away but not farther, implying workers are willing to
commutebutnotmigrate. Wefindaverysmallsustainedimpactduringtheoperationsand
maintenancephase,despitebothshort-andlong-termimpactsonmunicipalities’revenues.
| JEL classification: | C23,H70,Q50                                   |     |     |     |     |     |
| ------------------- | --------------------------------------------- | --- | --- | --- | --- | --- |
| Keywords:           | Windpower,laboreffects,localeconomy,paneldata |     |     |     |     |     |
∗Corresponding author. Toulouse School of Economics, University of Toulouse Capitole, Toulouse, France.
Address: ToulouseSchoolofEconomics,ManufacturedesTabacs,21All´eedeBrienne,31015Toulouse,France.
Email: helia.costa@tse-fr.eu
†DepartmentofEconomicsandNIPE,UniversityofMinho,Braga,Portugal. Address: UniversityofMinho,
| CampusdeGualtar,4710-057Braga,Portugal. |     |     | Email: linda.veiga@eeg.uminho.pt |     |     |     |
| --------------------------------------- | --- | --- | -------------------------------- | --- | --- | --- |
1
© 2020 published by Elsevier. This manuscript is made available under the Elsevier user license
https://www.elsevier.com/open-access/userlicense/1.0/

1 Introduction
The aim of this paper is to evaluate the impact of wind power investments on the local labor
market. Renewable energy has been a key part of the environmental strategy of the European
Union (EU) to reduce CO emissions, as well as to increase energy independence and security.
2
The EU 2020 climate and energy package, enacted in 2009, set out the objective of raising
the share of European Union’s member states energy consumption produced from renewable
resources to 20% by 2020. In addition to environmental objectives, the European Commission
estimatedthatmeetingthistargetcouldcreateupto417,000newjobsby2020(Ragwitzetal.,
2009). However, doubts remain as to whether these effects translate into an increase in overall
employment - rather than a displacement of resources - as well as into effects at the local-level
rather than at the aggregate level only. This is of major importance to the local communities
that house these projects, sometimes with negative impacts for example in terms of housing
prices (Lang et al., 2014, Gibbons, 2015, Sunak and Madlener, 2016).1 We aim at assessing the
existence,magnitude,duration,anddistributionofeffectsofinvestmentinwindenergyontotal
local employment for a panel of Portuguese municipalities.
Portugal has made large investments in renewable energy, in particular wind power, in the past
decades, despite the economic slowdown. In 2017 the wind share in total electricity demand
in mainland Portugal was of 24.2%, the second highest in the EU (WindEurope, 2018). Total
installedgeneratingcapacityincreasedfrom27.22megawatt(MW)in1997to5332MWin2017,
makingPortugalthecountrywiththethirdhighestkilowatt(KW)installedperkm2 intheEU
(e2p Endogenous Energies of Portugal, 2017a). Understanding local economic consequences of
these investments is therefore important.
ThePortugueseeconomyishighlyenergyintensiveandhastraditionallybeenespeciallydepen-
dent on imports of primary fossil fuels. Consequently, one of the main benefits of investment
in renewables, and in particular in wind power, is to decrease the weight of these imports in
national Gross Value Added. Additionally, the development of the wind industry is expected to
increase competitiveness and contribute to the creation of jobs. Deloitte (2009) estimated that
in2008thewindindustrygeneratedatotalof2200directandindirectjobs,expectedtoincrease
to5850by2015. TheInternationalLaborOrganizationpredictsthat,worldwide, onemegawatt
of wind energy could create between 0.43 and 2.51 jobs at the construction and manufacturing
phase, and 0.27 during the operations and maintenance phase, with a mix of low, medium, and
1Despite concerns that offshore wind development would decrease tourism in coastal areas, Carr-Harris and
Lang(2019)findnosupportforthisclaim.
2

high skilled labor (ILO, 2011). Similar ranges are estimated by input-output models in various
settings (e.g. Slattery et al., 2011).
These project-level or input-output studies that typically focus on gross impacts may not mea-
sure the total net impact of wind investment. The overall impact of a wind park might be
smaller than estimated by these studies if it displaces other kinds of investment, or larger if
the macroeconomic impact resulting from the investment generates further employment. By
performing an econometric analysis with historic data we can account for these effects and es-
timate the total net impact. Whether benefits are accrued at the local-level and how they are
determinedanddistributedareimportantquestionsfordesigningregulationandpoliciesrelated
to wind investment.
We perform the analysis for a panel of all the 278 Portuguese mainland municipalities for the
years between 1997 and 2017. We study the impact of the installation of wind power in a given
municipality on its unemployment rate, and distinguish between the construction phase, and
the operations and maintenance phase. We further investigate how these impacts vary with the
genderandeducationallevelsofworkers. Moreover, weexplorethepossibilityoflocalspillovers
between municipalities. Development in one region may affect employment in another through
migrationorindirecteconomicimpacts(suchastheincreaseindemandforgoodsandservices).
Weuseadistancedecaymatrixtoaddressthispossibility. Finally,wefurtherourunderstanding
of the local economic impacts of wind energy investment by studying its effect on local govern-
ments’ finances. Municipal revenues may increase in the short-run because energy companies
buy public land or in the long run because they rent land or pay taxes and other services.
Our identification strategy is based on the fact that the main determinants of the location of
wind investment within the country, such as the wind energy potential for commercial turbines,
orography,orslopeoftheland,aretimeinvariant. Theyarethuscapturedbymunicipality-level
fixed effects. While incentive schemes for investment in wind power are strong determinants of
the decision to invest, these are decided at the country or European level and implemented
equally across municipalities, and are therefore captured by time fixed effects.
To the best of our knowledge only a few studies have performed similar analyses.2 Brown et al.
(2012) perform a cross section econometric analysis of employment and income impacts of wind
power installation using county total variation in wind power from 2000 to 2008, in the U.S.
They find that personal income and employment increase 11000$ and 0.5 jobs respectively per
MW.Usingacrosssectionvariationofinstalledwindpowerfrom2001and2011inTexascoun-
2Otherstudieshaveinsteadfocusedoncountrylevelimpacts(eg. Inglesi-Lotz,2016).
3

ties, De Silva et al. (2016) find positive impacts of employment at the industry, but not at the
county level, as well as modest income impacts. Xia and Song (2017a) use a similar method
to estimate the impact of wind power development from 2005 to 2011 in Chinese counties on
GDP, finding positive impacts. Panel data allows to surpass endogeneity issues by exploring
within-region variation. Hartley et al. (2015) use monthly data to compare the employment
impacts of wind and shale gas investments for a panel of counties in the state of Texas. They
focus on the impact in the six months after turbines are installed and find no significant impact
for the case of wind.
We find that wind power investment reduces unemployment levels during the construction and
manufacturingphase. Inparticular, a100MWincreaseininstalledpowerleadstoanaverageof
0.17 and 0.23 percentage point decrease in unemployment rates in each of the two years of con-
struction.3 This amounts to roughly 0.39 and 0.55 jobs per MW installed.4 We find that effects
overthesetwoyearsarefeltmainlyformaleworkersandunskilledlabor–i.e.,forworkerswith-
out a college education. Female unemployment also decreases in the last year of construction.
Moreover, we find evidence of spatial spillovers only between close by municipalities, indicating
possiblecommutingjourneysforwork,butnotmigration. Finally,wefoundnobenefitsfortotal
employment of wind power investment during the operations and maintenance phase nor any
long-term impacts.5 We also found both short and long-term positive impacts of wind energy
investment on total municipal revenues. These findings have important implications for renew-
able investment policy and regulation, which we discuss in the conclusion.
The remainder of the paper is organized as follows. Section 2 describes the evolution of wind
investment in Portugal and its legal framework. Section 3 describes the econometric model, the
empirical strategy, and the data. Section 4 presents and discusses the results, and Section 5
concludes the paper.
2 Wind Energy in Portugal
Renewableenergy(RES)developmenthassurgedinthepastdecadesinPortugal. In2009,andin
thecontextoftheEuropeanUnion’s(EU)RenewableEnergyDirective(Directive2009/28/EC),
PortugalcommittedinitsNationalActionPlantoachieve31%offinalconsumptionenergyfrom
renewable sources in 2020. Figure 1 shows the evolution of installed RES capacity in Portugal.
3More precisely, we estimate a 0.059 and 0.082 percentage points decrease in the unemployment rate for 1
KWper capita installed.
4Thisincludesbothpart-andfull-timework.
5With the exception of a very small decrease in unemployment for workers with a college degree and the
secondlevelofbasiceducation.
4

Figure 1: Evolution of installed RES capacity in Portugal
Source: INEGI/APREN—December2017
LegislationguaranteeinggridaccessforindependentpowerproducersusingREScameintoforce
in 1988 (Decree-Law 188/88 and Decree-Law 189/88). It covered only small hydropower, but
in 1995 it was extended to cover other sources such as wind power (Decree-Law 313/95) and
a system of feed-in-tariffs was introduced. Limited knowledge of wind resource potential and
wind technology in Portugal rendered investment in wind power very modest during the 1990’s
(Bento and Fontes, 2014). The lack of clarity of the process of connection to the grid until
2001 further contributed to this (Pen˜a et al., 2017). The development of new wind technology
in Europe, coupled with a favorable Portuguese and European regulatory context, led to the
takeoff of wind power investment in the late nineties.
Aseries ofinitiatives were meantto stimulate renewableelectricityproductionandregulate the
process more clearly. The system of feed-in-tariffs was revised in 1999 (Decree-Law 168/99)
and 2001 (Decree-Law 339-C/2001 and Decree-Law 312/2001) to account for avoided costs of
investing in conventional power plants and differentiated between technologies, with the first
2 000 hours of wind energy production each year being paid EUR 0.082/KWh.6 The same
documents simplified the license-granting process for grid access and introduced a special tax
of 2.5% of total wind revenue to be paid to local municipalities was introduced, with the aim
of increasing local benefits.7 With the same aim, in the 2005 process of releasing a tender for
1800 MW of wind power, in addition to technical requirements, a condition for being granted
6Thistariffisreducedby200hourblocksuntilaminimumofEUR0.04/KWhafter2600hours).
7Thespecialtaxwastobeappliednotonlytonewwindplantsbutalsoforexistingones,ifbilateralagreements
betweenwindplantdevelopersandmunicipalitiesdidnotforeseehighersumsbeingpaid.
5

tendering conditions was working with local manufacturing companies. Additional conditions
included limiting import of turbines, contributing to research and development, and pursuing
the transfer of technology to Portugal. As a result national incorporation of inputs rose from
20% to 100% for this tender (Bento and Fontes, 2014).
InthecontextofthePortugueseeconomiccrisis,andinparticularwiththe2011interventionby
the International Monetary Fund (IMF), incentives for wind power development such as feed-
in-tariffs were slowly revised, and wind power capacity started to grow slower.
Nevertheless, installed wind power generating capacity increased from 27.22 MW in 1997 to
5332MWin2017,withPortugalhavingthethirdhighestKWinstalledperkm2 intheEU(e2p
Endogenous Energies of Portugal, 2017a). In 2017 the wind share in total electricity demand in
Portugal was of 24.1%(e2p Endogenous Energies of Portugal, 2017a).
Permission for the exploration of wind energy is granted by the central government,8 and the
main determinants of location of wind parks are set out in Section 3.3, the most important of
those being wind potential and access to the grid.
Figure 2 overlays the location of all existing wind parks in 2017 on a map of the wind potential
of continental Portugal, as measured by the total number of annual hours of energy production
corresponding to the capacity of a commercial wind turbine.9
8Specifically,theDirectorateGeneralforEnergyandGeology(DGEG)eithergrantsaccessdirectlyforwind
parksorgridconnectionlicencesmaybegrantedthroughapublictender,wherespecificconditionsapply. Most
licenceswhereawardedinpublictendersintheyears2001,2003,and2005(Pen˜aetal.,2017).
9FurtherinformationontheuseofthisvariableanditssourceispresentedinSection3.
6

Figure 2: Wind parks and potential
Source: LNEGande2p/INEGI/APREN,datafrom2017
3 Empirical Model
3.1 Empirical Strategy
The aim of the analysis is to investigate municipality-level effects of investment in wind power
in Portugal. Our dependent variable is the unemployment rate at the municipal level, the
estimationofwhichisdescribedinSection3.2. Ourmainindependentvariableofinterestisthe
amountofaccumulatedwindpowerinstalledinmunicipalityiinagivenyear,inKWper capita.
This variable captures effects of the total power that is installation of a wind park in each year,
and therefore relates to the operations and maintenance phase. It measures whether there are
sustained long-term impacts of installed wind power. In order to account for the effects of the
construction and manufacturing phase, we use two variables measuring the amount of power
per capita that is installed and starts producing in the following one and two years. This is
because it usually takes between 6 months and a year to build a wind park, but in Portugal,
depending on the size of the park and the economic conjuncture, it might take even longer.
We also experiment with past lags, in order to investigate further effects of maintenance and
7

operations that might only have an impact in the future.10
The basic empirical specification is thus given by:
unemp =α +γ power +γ power +γ Apower +α X +η +ρ +(cid:15) (1)
it 1 1 it+2 2 it+1 3 it 2 it i t it
where unemp is the unemployment rate in municipality i year t; power and power are
it it+1 it+2
the total power per capita installed and starting operations in municipality i in years t+1 and
t+2,respectively,(constructionphase);Apower istheaccumulatedinstalledKWpercapita in
it
municipality i in year t (long-term); and X is a vector of economic and demographic variables
it
affecting unemployment in municipality i in year t. Finally, η is a municipality individual fixed
i
effect, ρ a year fixed effect, and (cid:15) the error term.
t it
Included in vector X are growth of Gross Domestic Product (GDP) by NUTS3 region,11 in
it
real per capita terms and in the previous year (∆GDPreg ), that captures changes in re-
it−1
gional economic conditions, and total spending by municipalities in the previous year, in real
per capita terms(expend ),becausepastexpenditurescanstimulateemployment. Thesetwo
it−1
variables are lagged one period in order to avoid endogeneity issues.12 Additionally, it includes
two demographic variables (population density, denspop , and share of population under 15
it
years old, young ). In order to account for possible impacts of urbanization we estimate the
it
model including the interaction between installed power and a dummy variable equal to one if
a municipality includes at least one city, city .
it
We additionally investigate the impact of wind investment for skilled versus unskilled labor. As
a proxy for the level of skill of a job, we use the level of completed education of the worker. We
thus repeat the estimation using as the dependent variable the weight on the working age pop-
ulation of unemployed individuals with, respectively, one, two, or three levels of basic (pre-high
school) education, corresponding to 4, 6, and 9 years of schooling, with secondary (high school)
education, and finally, with a university degree.13 We also investigate whether unemployment
effects depend on gender, by testing the impacts for female and male unemployment.
Finally, employment in municipality i may be affected by the power installed in neighboring
10To test the robustness of the results, we tried different lags and leads of power and Apower. These results
arepresentedinAppendixB.
11NUTSstandsforNomenclatureofUnitsforTerritorialStatistics. TheNUTSisdevelopedbytheEuropean
Unionforreferencingthesubdivisionsofcountriesforstatisticalpurposes. ForeachEUcountry,ahierarchyof
threeNUTSlevelsisestablishedbyEurostat. Thesubdivisionsdonotcorrespondnecessarilytoadministrative
divisionswithinthecountry. OnmainlandPortugalthereare23NUTS3.
12NUTS3 regions include a varying number of municipalities. A measure of GDP is not available at the
municipallevel.
13The third level of basic education was the level of mandatory education in Portugal until 2009, when it
changedtosecondary(highschool)education.
8

municipalities. For example if there is sufficient labor mobility or if development in neighboring
municipalities creates demand for good and services that spill over into municipality i, then
investment by neighbors might have a positive effect in own employment. It may also happen
that development in neighboring municipalities diverts investment away from municipality i,
thereby impacting negatively its levels of employment.
We account for this by including in the regression a measure of the power installed in neigh-
boring municipalities. We weight this power by a matrix based on geographic proximity, such
that closer neighbors have a larger effect in a given municipality’s unemployment rate. In order
to define this matrix, a commonly used method is to assign weights based on binary contiguity.
This would imply that municipalities sharing a border are weighted equally, and others are not
considered neighbors. Since Anselin (1988) argues this method may not account for the full
degreeofspatialinteractioninthedata,wefollowCliffandOrd(1981)anddefineneighborsac-
cording to the geographical distance between them. Specifically, we define neighbors according
to the Euclidean distance between the centers of the municipalities, and construct the weights
as the inverse of this measure. We then standardize the weights w j such that for a given mu-
i
(cid:80)
nicipality i, w = 1. More discussion on the appropriate choice of economic neighbors in
j ij
the context of Portuguese municipalities can be found in Costa et al. (2015).
Wethenlimitmunicipalitiesthatareconsideredneighborstothosethatarexorlesskilometers
apart, with x = 30, x = 50, and x = 100km. The former aims at capturing commuting trav-
elling for work, and the two latter possible migration for work effects. For the municipalities
considered neighbors, a lower weight is assigned the further away they are.
Hence the weight of municipality j relative to municipality i, w , is defined as:
ij

1
(cid:80) disti
1
j if 0<d
ij
≤xkm
w
ij
= j distij (2)
0
otherwise
(cid:80)
Thus, Eq. (1) is augmented with the term Wpower = w power , where j are munici-
jt j(cid:54)=i ijt jt
pality i’s neighbors, becoming:
unemp =α +γ power +γ power +γ Apower +δWP +α X +η +ρ +(cid:15) (3)
it 1 1 it+2 2 it+1 3 it jt(+1/2) 2 it i t it
where the other variables remain unchanged from Eq. (1) and P stands for, respectively,
jt(+1/2)
power , Wpower , and WApower , the spatially weighted variables of interest.14
jt+1 jt+2 jt
14To avoid the correlation between the variables measuring neighboring levels of installed and accumulated
9

| 3.2 Data | and | Sources |     |     |     |     |     |
| -------- | --- | ------- | --- | --- | --- | --- | --- |
The dataset used covers all 278 Portuguese mainland municipalities for the period of 1997-2017
| for a total  | of 5832   | observations. | Table 1 summarizes | the        | data.15 |         |       |
| ------------ | --------- | ------------- | ------------------ | ---------- | ------- | ------- | ----- |
|              |           |               | Table 1: Summary   | statistics |         |         |       |
|              | Variable  |               | Mean               | Std. Dev.  | Min.    | Max.    | N     |
| Unemployment |           | rate          | 6.722              | 2.699      | 1.38    | 18.477  | 5,832 |
| Male         | unemp.    |               | 2.812              | 1.314      | 0.315   | 9.174   | 5,832 |
| Female       | unemp.    |               | 3.893              | 1.643      | 0.804   | 13.775  | 5,832 |
| Unemployment |           | (1st)         | 2.812              | 1.314      | 0.315   | 9.174   | 5,832 |
| Unemployment |           | (2nd)         | 1.284              | 0.611      | 0.143   | 5.367   | 5,832 |
| Unemployment |           | (3rd)         | 1.185              | 0.636      | 0.083   | 4.348   | 5,832 |
| Unemployment |           | (Sec)         | 1.212              | 0.689      | 0.029   | 8.449   | 5,832 |
| Unemployment |           | (Uni)         | 0.542              | 0.378      | 0       | 2.743   | 5,826 |
| Power        | installed | (KW)          | 878.969            | 6,970.495  | 0       | 22,2000 | 5,832 |
| Power        | installed | (KW pc)       | 0.073              | 0.765      | 0       | 32.123  | 5,832 |
| Power        | accum.    | (KW pc)       | 0.778              | 2.964      | 0       | 43.114  | 5,832 |
NEPS16
|            |            |          | 1,355.592  | 368.071    | 665.161 | 2,537.657 | 5,832 |
| ---------- | ---------- | -------- | ---------- | ---------- | ------- | --------- | ----- |
| Population |            |          | 35,706.598 | 57,252.778 | 1,634   | 606,480   | 5,832 |
| Population |            | density  | 306.178    | 856.243    | 4.017   | 7,670.162 | 5,832 |
| City       |            |          | 0.424      | 0.494      | 0       | 1         | 5,832 |
| Weight     | of young   | (<15)    | 13.703     | 2.686      | 4.841   | 23.878    | 5,832 |
| Weight     | of elderly | (>65)    | 22.343     | 6.358      | 8.116   | 45.568    | 5,832 |
| GDP        | growth     | NUTS3 pc | 1.416      | 3.568      | -15.645 | 25.94     | 5,832 |
| Total      | spending   | pc       | 1,064.109  | 538.782    | 177.106 | 8,606.569 | 5,832 |
| Total      | revenue    | pc       | 1,069.657  | 539.903    | 270.275 | 8,601.380 | 5,832 |
The total unemployment rate varies between a minimum of 1.4 and a maximum of 18.5, and
is calculated based on the number of people enrolled in the Portuguese centers of employment
(IEFP), weighted by the total number of working age inhabitants, where the total number of
working age inhabitants is calculated as the total population of the municipality minus those
aged 15 years old or younger, and those aged 65 or older. A graph depicting the annual sum
of unemployment rates across municipalities as well as the annual sum of installed power is
power–Wpowerjt+1,Wpowerjt+2,andWApowerjt–wechosetoincludethemoneatatimeintheestimation.
Wepresentresultsforthefinalyearofconstructionasasimilaranalysisforthefirstyearofconstructionandfor
the maintenance period does not yield any significant results and is not presented in the paper but is available
uponrequest.
15Summary statistics by two groups, one with all 171 municipalities that never had power installed, and one
withall108municipalitiesthatdid,isavailableinAppendixA.
16NEPS stands for the number of annual hours of energy production corresponding to the capacity of a
commercialwindturbine(80meters),andmeasurestheenergyproductivecapacityofthewind. Thevariableis
presentedhereasanaveragebymunicipality. ThisinformationwascededbythePortugueseNationalLaboratory
ofEnergyandGeology(LNEG).
10

presented in Appendix A.
The unemployment rate is followed by six variables that allow us to analyse the effect of wind
investments on unemployment by gender and education level. The first two variables represent
theweightofunemployedmaleandfemaleworkers, respectively, ontheworkingagepopulation
ofeachmunicipality. Thenextfourvariablesmeasuretheweightsofunemployedindividuals,by
educationallevel,ontheworkingagepopulationofthemunicipality. AscanbeseenfromTable
1, on average unemployed women represent a larger proportion of the working age population
than men and, among the four levels of education considered, unemployed individuals with a
university degree the smallest weight.
The following three variables correspond respectively to installed power in KW, installed power
in KW per capita, and to total installed power accumulated by a given municipality in a given
year. Data on the exact location of wind parks, time of production start, and capacity of
turbines was retrieved from e2p Endogenous Energies of Portugal (2017b), with permission
from the institution. Whenever a wind power plant was installed between two municipalities
thetotalpowerwasassumedtobedividedequallybetweenthesemunicipalities. Installedpower
varies greatly, between a minimum of zero and a maximum of 222 MW installed in a given year
and a given municipality. There was a total of 237 increases in power installed in the period of
analysis. All power installed is onshore.17
Total GDP per capita by NUTS3, used to calculate its growth rate, was retrieved from the
National Institute of Statistics (INE). Data on municipalities’ local accounts was obtained from
the DGAL’s annual publication Municipal Finances (DGAL, 1986-2017). These variables were
deflated using the 2017 consumer price index. Data on the consumer price index, municipal
population, the proportions of population under 15 and over 65, as well as the number of cities
were collected from the National Institute of Statistics.
3.3 Identification Strategy
Wind investment in Portugal has grown remarkably mainly due to the national and European
levelregulationdescribedinSection2. Thisregulationisdecidedatthenationalorinternational
(European) level and implemented equally across municipalities, and therefore changes to it are
capturedbytimefixedeffects. Ouridentificationstrategyisbasedonthefactthatwithincountry
determinants of wind power location are mainly time-invariant. Casadinho (2014) distinguishes
three set of criteria for the location of wind parks: location criteria, accessibility criteria, and
17Anexperimentaloffshorewindturbinewasconstructedin2011anddeactivatedin2016. Forthepurposeof
homogeneityitisleftoutofouranalysis.
11

restrictions. The former includes the energy potential of the wind, or orography, the second set
electric grid accessibility and general accessibility, and the latter includes restrictions imposed,
suchasenvironmentallyprotectedareas, areaswithhighslopes, areaswithexistingwindparks,
and areas with high population density. Of these, population density might vary considerably
over time and so, to avoid omitted variable bias, we include it in our analysis.
Tomeasurewindpotential, weusethenumberofannualhoursequivalenttothenominalpower
of a commercial turbine – introduced in 2 – averaged at the municipality level.
Permissionisgrantedbythegovernmentfortheexplorationofwindenergy. Whilethegranting
process was traditionally non-restrictive and so based mainly on technical factors, it is possible
that the central government gives preference to investment in municipalities with lower income
oremploymentlevels,inordertoboostdevelopmenthere. Insuchacase,ourestimationswould
bebiased. Giventhatmeasuresofwindpotentialofeachmunicipalityaremostlytimeinvariant,
wecannotusethisasaninstrumentandstillusefixedeffectstocontrolforallmunicipality-level
unobservables. We instead include annual growth of regional GDP in order to account for this
possibility. We lag this variable one period in order to avoid endogeneity issues. The exclusion
of this variable does not change results.18
Table 2 further investigates possible endogeneity of investment in wind energy. The dependent
variable in regressions (1)-(4) is wind investment in municipality i in year t. The first three
columnsinvestigatethepossibleimpactofpastlevelsofunemploymentinthechoiceoflocation
of wind parks, showing no significant effect. The fourth column investigates the impact of past
levels of GDP growth in the choice of investment, again with no significant impact.19
Finally,columnfiveshowstheimpactofpopulationdensity(denspop )andoftheenergypoten-
i
tialofwindbymunicipality,measuredbythenumberofannualhoursequivalenttothenominal
power of a commercial turbine (neps ). The dependent variable in this regression is the total
i
power accumulated per capita by 2017, as the energy potential is time invariant.20 Both these
variables have a significant impact on the choice of investment in wind energy. In line with
the theory (Casadinho, 2014), population density negatively affects investment levels, while the
energy potential affects it positively.
These findings seem to corroborate our hypothesis that factors that influence the location of
windparksatthemunicipallevelaretimeinvariant(asisthecaseofNEPS)orcanbeaccounted
for (in the case of population density). In particular, it does not seem that past unemployment
18Wefurthermoreincludetheaverageunemploymentrateofthe4yearspriortoconstructionwithoutachange
inresults,butdecideagainstthisduetoendogeneityissues.
19ThisisconsistentwiththeanalysisofXiaandSong(2017b)forChinesemunicipalities.
20Thepopulationdensityusedisalsothatof2017,sincethisdoesnotvarysignificantly.
12

|     |       |      | Table  | 2: Further | tests       | for identification |          |     |            |
| --- | ----- | ---- | ------ | ---------- | ----------- | ------------------ | -------- | --- | ---------- |
|     |       |      | (1)    |            | (2)         | (3)                |          | (4) | (5)        |
|     | Dep.  | Var. | power  | it power   | it          | power              | it power | it  | apower it  |
|     |       |      |        |            | Full Sample |                    |          |     | Year: 2017 |
|     | unemp |      | -103.4 | -197.7     |             | -213.9             |          |     |            |
it−1
|     |       |     | (64.09) | (129.3) |       | (142.3) |     |     |     |
| --- | ----- | --- | ------- | ------- | ----- | ------- | --- | --- | --- |
|     | unemp |     |         |         | 88.53 | 60.29   |     |     |     |
it−2
|     |       |      |     | (99.46) |     | (99.88) |     |     |     |
| --- | ----- | ---- | --- | ------- | --- | ------- | --- | --- | --- |
|     | unemp | it−3 |     |         |     | 17.77   |     |     |     |
(78.72)
|     | GDPregtot |     |     |     |     |     | 29.21 |     |     |
| --- | --------- | --- | --- | --- | --- | --- | ----- | --- | --- |
it−1
(35.65)
|     | denspop |     |     |     |     |     |     |     | -8.671*** |
| --- | ------- | --- | --- | --- | --- | --- | --- | --- | --------- |
i
(1.980)
|     | neps |     |     |     |     |     |     |     | 30.46*** |
| --- | ---- | --- | --- | --- | --- | --- | --- | --- | -------- |
i
(5.961)
|     | Constant     |          | 697.8*      |              | 639.0 | 766.3*           | -64.36  |                    | -20,139*** |
| --- | ------------ | -------- | ----------- | ------------ | ----- | ---------------- | ------- | ------------------ | ---------- |
|     |              |          | (382.8)     | (387.6)      |       | (444.8)          | (189.1) |                    | (6,882)    |
|     | Observations |          | 5,554       |              | 5,276 | 4,998            | 5,554   |                    | 278        |
|     | R-squared    |          | 0.017       |              | 0.017 | 0.016            | 0.017   |                    | 0.093      |
|     | Robust       | standard | errors      | clustered    | by    | municipality.    |         | SE in parentheses. |            |
|     |              | Null     | hypothesis  | is rejected: |       | ***1%,           | **5%    | and *10%.          |            |
|     | Columns      |          | 1-4 include | time dummies |       | and municipality |         | fixed              | effects.   |
levelsaffectthedevelopmentofwindenergy. Wethusconsiderwindcapacityinstalledinagiven
municipality in a given year exogenous in our analysis, and control for time and municipality
| fixed effects | only. |     |     |     |     |     |     |     |     |
| ------------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
4 Results
Our empirical results are presented in Tables 3-6. In Section 4.1 we justify the econometric
estimation technique and present the results of the main empirical specification (Table 3). In
Table 4 we show the results for disaggregated unemployment rates, and in Table 5 we present
the results of the spatial analysis based on geographic proximity. Throughout the analysis
we implement the same estimation method and include similar control variables to facilitate
comparison. Finally,Section4.4discussestheresultsandfurtherinvestigateslocal-levelimpacts
| of investment | on local | public | finance. |     |     |     |     |     |     |
| ------------- | -------- | ------ | -------- | --- | --- | --- | --- | --- | --- |
13

4.1 Wind Investment and Unemployment Rate
The main results are shown in Table 3. Column (1) presents the estimation of Eq.(1) by Fixed
Effects (FE). A Wald test indicates that the dummies for municipalities are jointly statistically
significant and a Hausman specification test gives preference to FE over Random Effects, so
we use FE throughout our estimations. The Breush-Pagan test suggests the presence of het-
eroskedasticity so we use robust standard errors, clustered by municipality in all equations.21
Allequationsincludetimefixedeffectstocaptureallvariablesaffectingallmunicipalitiesatthe
same time. Standard errors are presented in parenthesis.
FEattributesthesameweighttoallobservations,butpopulationvariesconsiderablyacrossmu-
nicipalities. On average, the number of inhabitants was above 529 thousand in Lisbon, while in
Barrancos it was below two thousand (these are the two extreme municipalities in the dataset).
Therefore, the estimation procedure requires special treatment for the aggregate time-series
cross-sectional nature of the data. Columns 2-7 present the estimation of Eq. (1) by FE, using
the average number of inhabitants in each municipality as weights.
Column(2)presentstheresultsforthebasicspecification,testingeffectsduringtheconstruction
andmaintenancephases. Thecoefficientsmeasuringtheeffectofwindpowerinstallationduring
the construction phase, power and power , are negative and highly statistically signifi-
it+2 it+1
cant. In particular, they indicate that a 1KW per capita installed decreases unemployment, in
a given municipality during the construction phase, by 0.08 percentage points one year before
the wind plant starts producing and by 0.06 percentage points two year before. Taking into
accounttheaveragepopulation(35,706.598)bymunicipality, thistranslatesinanaverageeffect
of around 0.39 and 0.55 jobs per MW installed in each of the two years, in line with previous
estimations. The coefficient measuring the impact in the maintenance phase, Apower , is not
it
statistically significant.
As expected, the more dynamic the region where the municipality is (ie, the higher the re-
gional GDP growth, ∆GDPregion ), the lower the unemployment rate is. Population density
it
(denspop ) and the share of young population below working age (young ) also turned out
it it
to be statistically significant and negatively signed.22 Finally, the amount of municipal public
expenditures per capita (expend ) does not seem to influence unemployment.23
it−1
Columns (3) and (4) present the results respectively excluding regional GDP growth and mu-
21Withtheexceptionofthespatialanalysis,whereweclusterthemattheNUTS3regionlevel.
22One explanation for these results is that municipalities more densely populated and with a large share of
young population in Portugal tend to be economically more dynamic, while those less densely populated and
withalargeshareofoldpopulationtendtobelessdynamicandtofaceareductioninpopulation.
23Municipal expenditures per capita are in thousands in all estimations where expendit−1 is an explanatory
variabletomakecoefficientreadingeasier.
14

|            |     | Table 3: Effects | on total                                      | unemployment | rate |     |     |
| ---------- | --- | ---------------- | --------------------------------------------- | ------------ | ---- | --- | --- |
|            |     | (1) (2)          | (3)                                           | (4)          | (5)  | (6) | (7) |
| Estimation |     | FE               | FEusingtheaveragenumberofinhabitantsasweights |              |      |     |     |
powerit+2 -0.0147 -0.0587** -0.0583** -0.0623** -0.0441* -0.0562** -0.0922***
|     |     | (0.0155) (0.0266) | (0.0267) | (0.0277) | (0.0259) | (0.0259) | (0.0340) |
| --- | --- | ----------------- | -------- | -------- | -------- | -------- | -------- |
powerit+1 -0.0426*** -0.0821*** -0.0845*** -0.0863*** -0.0647*** -0.0852*** -0.0980***
|     |     | (0.0154) (0.0245) | (0.0248) | (0.0254) | (0.0249) | (0.0245) | (0.0337) |
| --- | --- | ----------------- | -------- | -------- | -------- | -------- | -------- |
Apowerit 0.0061 -0.0115 -0.0111 -0.0182 0.0069 -0.0100 -0.0378
|     |     | (0.0190) (0.0309) | (0.0308) | (0.0319) | (0.0313) | (0.0307) | (0.0325) |
| --- | --- | ----------------- | -------- | -------- | -------- | -------- | -------- |
∆GDPregit−1 -0.0215** -0.0285* -0.0284* -0.0078 -0.0288* -0.0284*
|            |     | (0.0088) (0.0147) |          | (0.0147) | (0.0152) | (0.0148) | (0.0147) |
| ---------- | --- | ----------------- | -------- | -------- | -------- | -------- | -------- |
| expendit−1 |     | -0.3818** -0.3080 | -0.3065  |          | -0.0496  | -0.3020  | -0.3088  |
|            |     | (0.1738) (0.2902) | (0.2915) |          | (0.2924) | (0.2891) | (0.2906) |
denspopit -0.0007 -0.0011*** -0.0011*** -0.0011*** -0.0008 -0.0011*** -0.0011***
|     |     | (0.0008) (0.0004) | (0.0004) | (0.0004) | (0.0006) | (0.0004) | (0.0004) |
| --- | --- | ----------------- | -------- | -------- | -------- | -------- | -------- |
youngit -0.2496*** -0.2665*** -0.2577*** -0.2583*** -0.2675*** -0.2663***
|       |     | (0.0560) (0.0650) | (0.0652) | (0.0638) |         | (0.0651) | (0.0651) |
| ----- | --- | ----------------- | -------- | -------- | ------- | -------- | -------- |
| oldit |     |                   |          |          | -0.0153 |          |          |
(0.0717)
| cityit |     |     |     |     |     | -0.6394** |     |
| ------ | --- | --- | --- | --- | --- | --------- | --- |
(0.2623)
| city∗powerit+1 |     |     |     |     |     | 0.0408 |     |
| -------------- | --- | --- | --- | --- | --- | ------ | --- |
(0.0748)
| after07it∗powerit+2 |     |     |     |     |     |     | 0.0609 |
| ------------------- | --- | --- | --- | --- | --- | --- | ------ |
(0.0421)
| after07it∗powerit+1 |     |     |     |     |     |     | 0.0265 |
| ------------------- | --- | --- | --- | --- | --- | --- | ------ |
(0.0423)
| after07it∗Apowerit |     |     |     |     |     |     | 0.0248 |
| ------------------ | --- | --- | --- | --- | --- | --- | ------ |
(0.0376)
Constant 10.4989*** 11.7979*** 11.5145*** 11.4514*** 7.0083*** 12.2884*** 11.7949***
|              |     | (0.9152) (1.3710) | (1.3973) | (1.3116) | (1.2938) | (1.3996) | (1.3723) |
| ------------ | --- | ----------------- | -------- | -------- | -------- | -------- | -------- |
| Observations |     | 4,998 4,998       | 4,998    | 4,998    | 4,998    | 4,998    | 4,998    |
| R-squared    |     | 0.5973 0.7223     | 0.7216   | 0.7218   | 0.7082   | 0.7227   | 0.7223   |
Notes: Estimatedcoefficientsindicatetheeffectsofaoneunitchangeintheexplanatoryvariablesonthe
unemploymentrate,inpercentagepoints. Allestimationsincludeyearandmunicipalfixedeffects. Robust
standarderrors(SE)clusteredbymunicipality. SEinparentheses. Significancelevelforwhichthenull
|     | hypothesisisrejected: | ***1%,**5%and*10%. |     | ThenumberofunitsinFEis278. |     |     |     |
| --- | --------------------- | ------------------ | --- | -------------------------- | --- | --- | --- |
nicipal public expenditures, without changes in the results. Column (5) uses the weight of
population,24
population over 65 years of age (old ) instead of the weight of young again with-
it
out significantly affecting the main results. Column (6) presents an estimation including a
dummyformunicipalitieswithatleastonecity(city it )andtheinteractionbetweenthisdummy
and the variable measuring the power being installed. Although the interaction variable is not
statistically significant, it is positive, suggesting the effect of wind power investment could be
| higher in | rural areas. |     |     |     |     |     |     |
| --------- | ------------ | --- | --- | --- | --- | --- | --- |
Finally, we analyse if the requirement, introduced in the 2005 tender, of working with local
manufacturingconditions(pleaserecallSection2)influencedlocalunemploymenteffectsofwind
24Thetwocannotbeincludedatthesametimesincetheyareveryhighlycorrelated(-0.85).
15

energy investments. This tender was distributed in three phases (1200MW in 2006, 400MW in
2007 and 200MW in 2008) and due to delays over the financial crisis (Bento and Fontes, 2014)
thecapacitycontracted inthe earliestphase onlybegan deployment in2008. We thus createda
dummy variable for the years after 2007 (after07 ) and interacted it with the power variables.
it
As can be seen from column (7), none of the new variables turned out to be statistically signif-
icant, which suggests that the effect (reduction) in the unemployment rate associated with the
installation of new wind power plants was not influenced by the change in the requirements for
being granted tendering after 2005.
4.2 Distribution of Impacts by Type of Labor
We next focus on the distribution of the impacts on employment over gender and workers
estimated skill levels. As described in Subsection 3.2, we use the weight of unemployed male
andfemaleworkersontotalworkingagepopulation. Wealsomeasuretheweightofunemployed
workers with the first, second, and third level of basic education (from first to ninth grade),
workers that have graduated from high school, and workers with a university degree.
Table 4 presents these results. The results in columns (1) show significant impacts for male
workers in both the two years before the wind plant starts producing, consistent with the
impact being felt during the construction phase. For female workers, the effect is only visible in
the year immediately before the deployment of the park. Although women tend to work less on
construction, it is likely that wind energy investments streamline the local economy and create
indirect jobs, other than construction, namely on local shops and restaurants.
There is a significant reduction of unemployment during the construction phase for workers
with all three levels of basic education (columns (3)-(5)). The third level of basic education
was the mandatory level of education in Portugal, during which all the population receives the
sametypeofeducation,until2012whensecondaryeducationbecamethemandatorylevel(Law
85/2009). These are therefore likely to be employees performing unskilled labor. There is also
an impact for workers with secondary education and no impact at the level of workers with a
university degree, during the construction phase. Possibly, the high skill, white collar jobs are
concentrated in big cities and not where the wind energy is actually being developed.
There are no effects during the maintenance phase for any of the education levels, except for
a small effect for workers with the second level of basic education and workers with university
degrees. The latter is consistent with the operation and maintenance phase requiring more
skilled labor. This impact is however very small – it amounts to around 0.056 jobs per MW
16

|               | Table 4: Effects | on different | unemployment | rates  |     |     |
| ------------- | ---------------- | ------------ | ------------ | ------ | --- | --- |
|               | (1) (2)          | (3)          | (4)          | (5)    | (6) | (7) |
| Dep. Variable | Men Women        | Basic1       | Basic2       | Basic3 | Sec | Uni |
powerit+2 -0.0309** -0.0198 -0.0246** -0.0197*** -0.0107 -0.0089** -0.0012
|     | (0.0120) (0.0163) | (0.0123) | (0.0066) | (0.0065) | (0.0035) | (0.0026) |
| --- | ----------------- | -------- | -------- | -------- | -------- | -------- |
powerit+1 -0.0354*** -0.0455** -0.0279** -0.0285*** -0.0177*** -0.0121*** -0.0038
|     | (0.0122) (0.0191) | (0.0110) | (0.0066) | (0.0054) | (0.0045) | (0.0034) |
| --- | ----------------- | -------- | -------- | -------- | -------- | -------- |
Apowerit 0.0019 -0.0221 0.0065 -0.0156** 0.0060 -0.0069 -0.0085**
|     | (0.0140) (0.0199) | (0.0149) | (0.0075) | (0.0057) | (0.0054) | (0.0034) |
| --- | ----------------- | -------- | -------- | -------- | -------- | -------- |
∆GDPregit−1 -0.0132* -0.0008 -0.0175*** -0.0097*** 0.0001 0.0010 0.0045***
|     | (0.0070) (0.0083) | (0.0064) | (0.0032) | (0.0025) | (0.0026) | (0.0015) |
| --- | ----------------- | -------- | -------- | -------- | -------- | -------- |
expendit−1 0.0810 -0.4088** -0.1137 -0.1447** 0.0609 -0.0458 -0.0495
|     | (0.1261) (0.1736) | (0.0930) | (0.0613) | (0.0571) | (0.0526) | (0.0411) |
| --- | ----------------- | -------- | -------- | -------- | -------- | -------- |
denspopit -0.0005*** -0.0005*** -0.0002** -0.0002* -0.0002 -0.0001 -0.0003***
|     | (0.0002) (0.0002) | (0.0001) | (0.0001) | (0.0001) | (0.0001) | (0.0001) |
| --- | ----------------- | -------- | -------- | -------- | -------- | -------- |
youngit -0.0832*** -0.1979*** -0.1265*** -0.0533*** -0.0684*** -0.0117 -0.0216*
|     | (0.0305) (0.0409) | (0.0332) | (0.0155) | (0.0156) | (0.0150) | (0.0130) |
| --- | ----------------- | -------- | -------- | -------- | -------- | -------- |
Constant 4.4110*** 7.6040*** 4.4501*** 2.4415*** 2.1247*** 1.2105*** 1.0271***
|              | (0.6543) (0.7907) | (0.5651) | (0.3405) | (0.3100) | (0.2680) | (0.2741) |
| ------------ | ----------------- | -------- | -------- | -------- | -------- | -------- |
| Observations | 4,998 4,998       | 4,998    | 4,998    | 4,998    | 4,998    | 4,992    |
| R-squared    | 0.8026 0.5615     | 0.2225   | 0.4440   | 0.8097   | 0.8732   | 0.8583   |
Notes: Estimatedcoefficientsindicatetheeffectsofaoneunitchangeintheexplanatoryvariablesonthe
unemploymentrate,inpercentagepoints. Allestimationsincludeyearandmunicipalfixedeffects. RobustSE
clusteredbymunicipality. SEinparentheses. Significancelevelforwhichthenullhypothesisisrejected:
|     | ***1%,**5%and*10%. | ThenumberofunitsinFEis278. |     |     |     |     |
| --- | ------------------ | -------------------------- | --- | --- | --- | --- |
installed – which could indicate a lack of locally available skilled labor. If the operations and
maintenance phase requires more skilled labor, this could help explain the reduced significant
impact outside of workers with a university degree locally at this stage. An ILO report (ILO,
2011) predicts increased demand of labor stemming from wind development for all skill levels,
so these results might indicate a skill gap in the Portuguese labor market. It is possible that if
workers with the necessary technical skills are not available locally, developers import this work
| from other countries.25 |         |     |     |     |     |     |
| ----------------------- | ------- | --- | --- | --- | --- | --- |
| 4.3 Spatial             | Impacts |     |     |     |     |     |
We also study the existence of spatial impacts in wind investment. When power is installed
in a given municipality, neighboring municipalities might benefit if they can commute for work
or migrate, or because additional demand for their goods and services boosts local economy.
If mobility is low, however, a displacement of benefits and activities might take away from
neighboring municipalities’ economic development. We study which effect prevails.
25Alternatively,theycouldimportitfromneighboringmunicipalities.
Aspatialanalysisforthemaintenance
phase,availablefromtheauthor,showsthatthisisnotthecase.
17

|     |     |          |      | Table 5:  | Neighboring |            | effects |           |     |
| --- | --- | -------- | ---- | --------- | ----------- | ---------- | ------- | --------- | --- |
|     |     |          |      | (1)       |             |            | (2)     |           | (3) |
|     |     | Matrices |      | 30km      |             | 50km       |         | 100km     |     |
|     |     | power    | it+2 | -0.0520   |             | -0.0538    |         | -0.0643   |     |
|     |     |          |      | (0.0361)  |             | (0.0357)   |         | (0.0401)  |     |
|     |     | power    |      | -0.0741** |             | -0.0746*** |         | -0.0893** |     |
it+1
|     |     |        |     | (0.0280) |     | (0.0259) |     | (0.0345) |     |
| --- | --- | ------ | --- | -------- | --- | -------- | --- | -------- | --- |
|     |     | Apower |     | -0.0115  |     | -0.0113  |     | -0.0117  |     |
it
|     |     |       |     | (0.0365) |     | (0.0364) |     | (0.0362) |     |
| --- | --- | ----- | --- | -------- | --- | -------- | --- | -------- | --- |
|     |     | power |     | -0.1694* |     | -0.2166  |     | 0.4374   |     |
jt+1
|     |     |         |      | (0.0954) |     | (0.2388) |     | (0.5087) |     |
| --- | --- | ------- | ---- | -------- | --- | -------- | --- | -------- | --- |
|     |     | ∆GDPreg | it−1 | -0.0275  |     | -0.0277  |     | -0.0300  |     |
|     |     |         |      | (0.0242) |     | (0.0242) |     | (0.0247) |     |
|     |     | expend  |      | -0.3031  |     | -0.3027  |     | -0.3167  |     |
it−1
|     |     |         |     | (0.5772)   |     | (0.5748)   |     | (0.5704)   |     |
| --- | --- | ------- | --- | ---------- | --- | ---------- | --- | ---------- | --- |
|     |     | denspop |     | -0.0011*** |     | -0.0011*** |     | -0.0011*** |     |
it
|     |     |               |           | (0.0002)     |                 | (0.0002)   |                 | (0.0002)        |          |
| --- | --- | ------------- | --------- | ------------ | --------------- | ---------- | --------------- | --------------- | -------- |
|     |     | young         | it        | -0.2674***   |                 | -0.2676*** |                 | -0.2629***      |          |
|     |     |               |           | (0.0756)     |                 | (0.0759)   |                 | (0.0761)        |          |
|     |     | Constant      |           | 11.8040***   |                 | 11.8067*** |                 | 11.7573***      |          |
|     |     |               |           | (1.4359)     |                 | (1.4393)   |                 | (1.4388)        |          |
|     |     | Observations  |           | 4,998        |                 | 4,998      |                 | 4,998           |          |
|     |     | R-squared     |           | 0.7225       |                 | 0.7225     |                 | 0.7226          |          |
|     |     | Notes:        | Estimated | coefficients |                 | indicate   | effects         | of              | a unit   |
|     |     | change        | in the    | explanatory  | variables       |            | on unemployment |                 | rate,    |
|     |     | in percentage |           | points. All  | regressions     |            | include         | time            | dummies. |
|     |     | Robust        | SE        | clustered by | NUTS3           | region.    | SE              | in parentheses. |          |
|     |     | Sig.          | level     | for which    | null hypothesis |            | is rejected:    |                 | ***1%,   |
|     |     |               | **5% and  | *10%. The    | number          | of         | units           | in FE is        | 278.     |
Table 5 presents the results for spatial analysis, using the three distance decay matrices. We
focus on the construction and manufacturing phase, as it is the only one where significant
found.26
results were The main variable of interest is power jt+1 , measuring installed power in
neighboring municipalities that starts producing in the following year. In Columns (1)-(3) the
variable power jt+1 considers as neighbors only municipalities that are, respectively, 30, 50, and
| 100km apart, | with | weights | in  | inverse proportion |     | to  | their distance. |     |     |
| ------------ | ---- | ------- | --- | ------------------ | --- | --- | --------------- | --- | --- |
Theresultsshowthatthereisonlyasignificantimpactintermsofareductioninunemployment
in a given municipality when investment is made on municipalities less than 30km away (10%
26Westartedbyincludingallthespatialvariables,bothforthetheshortandlong-termimpacts,togetherin
thesameestimationbutnoneofvariablesturnedoutasstatisticallysignificant. Wethenproceededbyincluding
| justonevariableatatime. |     |     | Resultsareavailablefromtheauthors. |     |     |     |     |     |     |
| ----------------------- | --- | --- | ---------------------------------- | --- | --- | --- | --- | --- | --- |
18

significancelevel). Theeffectislarge: anincreaseininstalledpowerinneighboringmunicipalities
of1MWpercapita decreasesunemploymentinmunicipalityiby0.17percentagepoints. Thefact
thateffectsareonlysignificantat30kmorlessseemstoindicateanimpactthroughcommuting
to work, but not effects through migration for work purposes.
4.4 Local public finance
During the first year of production, and in subsequent years, no significant impacts in total
municipality employment were found. It is possible that this is the result solely of the fact that
the maintenance and operations phase is less labor demanding (ILO, 2011), or due to the fact
that this phase requires specific skilled labor (for example electrical and computer engineers)
that is not available at the local-level. However, it is also possible that the short lived effects
on employment are due to investments in wind energy that are too small to have a lasting
impact for the local economy. In order to understand whether this is the case, and in the
absence of a municipality-level GDP measure, we focus on local governments’ revenues. We
expect the development of a wind plant in Portugal to lead to an increase in local governments
revenues because developers will often pay to use land that belongs to the municipality, they
can be subject to municipal taxes, and, additionally, they are required to pay the municipality
2.5% of their revenue. We thus expect wind energy investment to have a positive impact over
municipalities’ finances.
Weestimatetheimpactofwindenergyinvestmentintotalrevenuesandsomeofitscomponents
as well as total expenditures. Descriptive statistics of all these variables and a graph depicting
the annual sum of real revenues per capita across municipalities, as well as the annual sum of
installed power, are presented in Appendix C (Table C.1 and Figure C). Own revenues are all
municipality revenues with the exception of transfers from the central government, which are
not expected to be impacted by wind energy investment. Sales of goods and services, property
revenuesanddirectandindirecttaxesarecurrentrevenuesandcapitalsalesarecapitalrevenues.
All dependent variables are logged.
Theestimationincludesdummiesfortheyearbeforethewindparkstartsproducingpower ,
it+1
to account for the construction period, and the year before that power , to account for
it+2
activitiestakingplacebeforethat,suchaslandsales. Finally,Apower measureslastingimpacts
it
of wind power investment once the park starts producing. We control for economic variables,
namely unemployment levels and the lagged growth of regional GDP, as well as demographic
variables, specifically population density and the percentage of young population.
19

secnanfi
cilbup
revo
tnemtsevni
dniw
fo
tcapmI
:6
elbaT
)8(
)7(
)6(
)5(
)4(
)3(
)2(
)1(
pxE
latoT
R elas
paC
T tceridnI
T
tceriD
R
ytreporP
R selaS
veR
nwO
veR
latoT
.raV
.peD
***6800.0
*8750.0
2030.0
8900.0
***9290.0
9000.0
***3610.0
***4010.0
rewop
2+ti
)3300.0(
)8330.0(
)3030.0(
)1600.0(
)8910.0(
)3700.0(
)3500.0(
)5300.0(
*5700.0
2720.0-
3300.0-
**4110.0
***0490.0
6000.0-
***6910.0
**6800.0
rewop
1+ti
)9300.0(
)8830.0(
)7910.0(
)7400.0(
)2320.0(
)6800.0(
)4400.0(
)9300.0(
***0910.0
**4380.0
**5150.0
***8040.0
8920.0
**1910.0
***4730.0
***2810.0
rewopA ti
)8400.0(
)2230.0(
)8320.0(
)1900.0(
)8220.0(
)6700.0(
)3800.0(
)5400.0(
5500.0-
**8680.0-
5420.0-
*1310.0-
*3170.0
4910.0-
**0210.0-
3500.0-
pmenu ti
)4600.0(
)8340.0(
)1620.0(
)6600.0(
)9830.0(
)2910.0(
)0600.0(
)9600.0(
2200.0
1400.0
***6130.0-
8200.0
7210.0
3100.0-
4000.0-
*1300.0
rPDG∆
1−ti
)6100.0(
)6020.0(
)2110.0(
)8100.0(
)7410.0(
)0600.0(
)3200.0(
)9100.0(
1000.0-
***0100.0-
5100.0
**2000.0-
5000.0-
1000.0-
**2000.0-
1000.0-
popsned ti
)1000.0(
)4000.0(
)2100.0(
)1000.0(
)4000.0(
)2000.0(
)1000.0(
)1000.0(
***5040.0-
**2951.0-
***6541.0-
***8640.0-
*2221.0-
**0640.0-
***0640.0-
***1930.0-
gnuoy
ti
)8500.0(
)3070.0(
)2050.0(
)5600.0(
)7460.0(
)5120.0(
)1800.0(
)6600.0(
*0182.0
***2819.5
***3864.3
***8079.5
**1254.3
***8724.4
***1895.6
***1281.7
tnatsnoC
)4761.0(
)0336.1(
)5720.1(
)6271.0(
)0035.1(
)7625.0(
)3212.0(
)8981.0(
899,4
673,4
619,4
899,4
989,4
899,4
899,4
899,4
snoitavresbO
9542.0
8631.0
3102.0
2583.0
0122.0
2671.0
0923.0
9912.0
derauqs-R
selbairav
yrotanalpxe
eht
ni
egnahc
tinu
eno
a
fo
stceffe
eht
etacidni
stneicffieoc
detamitsE
:setoN
.ytilapicinum
yb
deretsulc
srorre
dradnats
tsuboR
.segnahc
egatnecrep
ni
,selbairav
lacsfi
atipac
rep
laer
eht
no
.872 si
EF
ni
stinu
fo
rebmun
ehT
.seimmud
emit
edulcni
snoisserger
llA
.sesehtnerap
ni
ES
.%01*
dna
%5**
,%1***
:detcejer
si
sisehtopyh
llun
hcihw
rof
level
.giS
20

Table 6 presents the results of this analysis. In columns (1)-(7) we investigate impacts in total
revenue and its components and in column (8) resulting impacts in total spending. We find
thattherearesmallbutsustainedpositiveimpactsontotalrevenues. Thecoefficientmeasuring
increases in installed and operating wind energy (Apower ) is positive and statistically signifi-
it
cantata1%significancelevel. Specifically,wefindthata1KWper capita increaseinoperating
capacity generates a 1.82% increase in per capita municipal revenues, or of around 19.5 euros.27
Significant increases in total expenditures are also visible one and two years before the new
power goes into functioning.
Unpacking this result, we find a strong and significant impact of wind energy investment at all
stages on municipality generated revenues (own revenues). An increase of 1KW per capita in
total power installed increases own revenues by 3.7%. Further unpacking these effects, we turn
tocurrentrevenues. Wefindapositiveeffectofinstalledandoperatingwindenergyonrevenues
from sales of goods and services. This is because wind energy developers pay 2.5% of their
revenues to the municipality. Revenues from property, for example from renting municipality
owned property, increase only in the period before wind energy goes into functioning. Revenues
from direct taxes also increase with installed and operating capacity because wind energy de-
velopers pay the municipal tax on corporate income (derrama) and the municipal property tax
(Imposto Municipal sobre Imoveis). We also find a positive impact on indirect tax revenues,
whichtakesplaceforexampleifinvestmentinwindgeneratedincreaseddemandforlicensesand
other fees by firms. Finally, turning to capital revenues, we find a positive impact on revenues
from the sale of capital goods on the year before construction. This is likely to be due to wind
energy developers buying municipality owned land in order to install wind power.
The last column shows that the impact in revenues translates into an increase in expenditures
once the wind energy installed starts operating, and also in the years before. Results show that
a 1KW per capita increase in installed and operating wind energy increases expenditures by
1.9%, or 20 euros per capita, similar to the effect on total revenues.
5 Conclusion
We find that investment in wind power reduces local unemployment during the construction
phase. In particular, we estimate that a 1KW increase in installed power per capita leads to
0.6 and 0.8 percentage point decrease in unemployment rates in the first and second year of
27Takingintoaccounttheaveragemunicipalpopulation,thismeansthattheimpactofanextra1MWofenergy
operatinginagivenmunicipalityincreasesmunicipalrevenuebyaround50centsper capita.
21

construction. Based on the average population of municipalities and average unemployment
rates, this translates into around 0.39 and 0.55 jobs per MW installed, respectively. Our results
show no evidence of any effect during the operations and maintenance phases in aggregate un-
employment. These results are broadly consistent with previous estimates in different settings.
We then focus on differentiated impacts by gender and on skilled and unskilled employment, by
investigating impacts on workers with different education levels. We find the decrease in unem-
ployment rates during the construction phase is only present for workers without a university
degree, consistent with construction work. There are decreases in male unemployment in the
two years before the park starts producing, and a decrease in female unemployment in the last
year. Theshort-runincreasesinoverallmunicipalityemploymentduringtheconstructionphase
ofwindparksarethuslikelycausednotonlybyadirectincreaseindemandforlaborduetothe
construction of the parks, but also by wind energy development spilling over to other sectors in
a municipality. There seem to be only very small long-term impacts on unemployment of work-
ers with college degrees, indicating that a small part of the demand for skilled labor necessary
during the maintenance phase could be met locally.
We further investigate the possibility of local spillovers between municipalities. Development in
one region may affect employment in another through migration, if job seekers find it optimal
to move in search of employment, or indirect economic impacts, like the increase in demand for
goods and services in neighboring municipalities. We find only an effect for municipalities that
are 30km or less from each other during the construction phase. This indicates migration does
not seem to play an important role, but rather commuting for work does.
Finally, we also found both short and long-term positive impacts of wind energy investment
on total municipal revenues.These were driven specifically by short-term increases in property
revenues and long-term increases in revenues with direct and indirect taxes and sale of goods
and services.
Our findings offer an insight on local labor market effects of incentive policies for renewable
investment. First, they present for the first time a clear evaluation of the overall net impact of
wind power investment in local-level employment in Portugal, a country where extremely large
investments were made. Despite the focus put on job creation, local employment impacts seem
tobemostlyshortlived. Second,theyprovideinformationonthedistributionalimpactsofsuch
policies. The short-term unemployment local benefits are more visible for male and unskilled
workers. Finally,theyofferaninsightintothemechanismsbehindtheseimpacts. Theabsenceof
aggregate long-term impacts, along with the low mobility of labor, could indicate that, if policy
22

makers wish to increase benefits to local labor markets, there might be a case for targeting skill
development towards the needs of this new market, in order to fully take advantage of possible
local labor benefits. If effects are not visible – or are close to zero – during the operating life of
windparks,thismightindicatethatamismatchofskillsrequireswindparkdeveloperstoimport
labor. What is more, we find that sustained increases in local governments’ revenues did not
translate into gains in employment, for example through an increase in public spending. While
further investigation is needed for a complete understanding of the lack of sustained impact on
employmentduringthisphase,ourresultspresentafirststepintoevaluatingtheimpactofwind
power investment at the local level.
Theempiricalstrategyfollowedinthepapercanbeeasilygeneralizedtoothercountries,partic-
ularlythosewithcentralizedpolicyregardingwindenergyinvestment. However,certainaspects
are specific to the Portuguese setting. For example, we abstract from substitution effects be-
tween renewable energy and traditional energy sources. Despite accounting for a negligible
share of employment in Portugal, coal and gas extraction industries have the capacity to gener-
atelargeemploymentimpactsinproducingcountries(e.g. Paredesetal.,2015andManiloffand
Mastromonaco, 2017). But while our results are specific to the Portuguese setting, the insights
generated are useful for parallel analyses. The impact of wind investment on employment on
other settings will depend on factors such as the mobility of the workforce and the availability
of specialized labor at the local level, and policies aiming at promoting local job markets need
to help translate possible increased local revenues to employment gains.
Acknowlegements
The authors thank Francois Cohen, Alexandra Gomes, Ralf Martin and participants of the
Grantham Research Workshop at London School of Economics, the TSE Environmental winter
seminars at the Toulouse School of Economics, the 4th IZA Workshop on Labor Market Effects
of Environmental Policies, the EAERE 2017, and the FSR Climate Annual Conference 2017
for valuable comments. H´elia Costa acknowledges funding from the ESRC Centre for Climate
ChangeEconomicsandPolicy,fromtheEuropeanCommunity’s7thFrameworkProgramunder
Grant Agreement No. 308497 (RAMSES), from the ANR under grant ANR-17-EURE-0010
(Investissements d’Avenir program), and from the IDEX Chair. Linda Veiga’s work is financed
by National Funds of the FCT – Portuguese Foundation for Science and Technology within the
project UID/ECO/03182/2019.
23

| Declaration  | of           | interest |     |     |     |     |
| ------------ | ------------ | -------- | --- | --- | --- | --- |
| Declarations | of interest: | none.    |     |     |     |     |
References
Anselin, L. (1988): Spatial econometrics: methods and models, vol. 4, Springer.
| Bento, | N. and M. | Fontes  |             |                 |               |              |
| ------ | --------- | ------- | ----------- | --------------- | ------------- | ------------ |
|        |           | (2014): | “Mechanisms | that accelerate | the diffusion | of renewable |
technologies in new markets: Insights from the wind industry in Portugal,” dinˆamia’cet-
| Working | Papers. |     |     |     |     |     |
| ------- | ------- | --- | --- | --- | --- | --- |
Brown, J. P., J. Pender, R. Wiser, E. Lantz, and B. Hoen (2012): “Ex post analysis
of economic impacts from wind power development in US counties,” Energy Economics, 34,
1743–1754.
Carr-Harris, A. and C. Lang (2019): “Sustainability and tourism: the effect of the United
States’ first offshore wind farm on the vacation rental market,” Resource and Energy Eco-
| nomics, | 57, 51–67. |     |     |     |     |     |
| ------- | ---------- | --- | --- | --- | --- | --- |
Casadinho, C. S.(2014): “Basededadosdopotenciale´olicoemPortugalContinental,”Ph.D.
| thesis, | Universidade | de Lisboa. |     |     |     |     |
| ------- | ------------ | ---------- | --- | --- | --- | --- |
Cliff, A. and J. Ord (1981): Spatial Processes: Models & Applications, Pion.
| Costa, | H., L. Gonc¸alves | Veiga, | and M. Portela |         |               |                  |
| ------ | ----------------- | ------ | -------------- | ------- | ------------- | ---------------- |
|        |                   |        |                | (2015): | “Interactions | in Local Govern- |
ments’ Spending Decisions: Evidence from Portugal,” Regional Studies, 49, 1441–1456.
De Silva, D. G., R. P. McComb, and A. R. Schiller (2016): “What blows in with the
| wind?” | Southern Economic | Journal, | 82, 826–858. |     |     |     |
| ------ | ----------------- | -------- | ------------ | --- | --- | --- |
Deloitte(2009):
“ImpactoMacroecono´micodoSectordasEnergiasRenov´aveisemPortugal,”
| Tech. | rep., Deloitte. |     |     |     |     |     |
| ----- | --------------- | --- | --- | --- | --- | --- |
DGAL (1986-2017): “Finan¸cas Municipais,” Tech. rep., Dire¸c˜ao Geral das Autarquias Locais,
Lisbon.
e2p Endogenous Energies of Portugal (2017a): “Parques E´olicos em Portugal - Wind
| Farms | in Portugal,” | .   |     |     |     |     |
| ----- | ------------- | --- | --- | --- | --- | --- |
24

| ———      | (2017b):  | “Website          | e2p | Endogenous | Energies                                     |     | of Portugal,” | .   |     |
| -------- | --------- | ----------------- | --- | ---------- | -------------------------------------------- | --- | ------------- | --- | --- |
| Gibbons, | S.(2015): |                   |     |            |                                              |     |               |     |     |
|          |           | “Gonewiththewind: |     |            | Valuingthevisualimpactsofwindturbinesthrough |     |               |     |     |
house prices,” Journal of Environmental Economics and Management, 72, 177–196.
Hartley, P. R., K. B. Medlock III, T. Temzelides, and X. Zhang (2015): “Local
employment impact from competing energy sources: Shale gas versus wind generation in
| Texas,” | Energy | Economics, |     | 49, 610–619. |     |     |     |     |     |
| ------- | ------ | ---------- | --- | ------------ | --- | --- | --- | --- | --- |
ILO
(2011): “Investment in renewable energy generates jobs. Supply of skilled workforce needs
to catch up. Research Brief.” Tech. rep., International Labor Organization.
Inglesi-Lotz, R. (2016): “The impact of renewable energy consumption to economic growth:
| A panel | data   | application,” |     | Energy Economics,   |     | 53, | 58–63.  |                  |                |
| ------- | ------ | ------------- | --- | ------------------- | --- | --- | ------- | ---------------- | -------------- |
| Lang,   | C., J. | J. Opaluch,   |     | and G. Sfinarolakis |     |     |         |                  |                |
|         |        |               |     |                     |     |     | (2014): | “The windy city: | Property value |
impacts of wind turbines in an urban setting,” Energy Economics, 44, 413–421.
Maniloff, P. and R. Mastromonaco (2017): “The local employment impacts of fracking:
| A national | study,” |     | Resource | and Energy | Economics, |     | 49, 62–85. |     |     |
| ---------- | ------- | --- | -------- | ---------- | ---------- | --- | ---------- | --- | --- |
Paredes, D., T. Komarek, and S. Loveridge (2015): “Income and employment effects of
shale gas extraction windfalls: Evidence from the Marcellus region,” Energy Economics, 47,
112–120.
Pen˜a, I., I. L. Azevedo, and L. A. F. M. Ferreira (2017): “Lessons from wind policy in
| Portugal,” | Energy | Policy, | 103, | 193–202. |     |     |     |     |     |
| ---------- | ------ | ------- | ---- | -------- | --- | --- | --- | --- | --- |
Ragwitz, M., W. Schade, B. Breitschopf, R. Walz, N. Helfrich, M. Rathmann,
G. Resch, C. Panzer, T. Faber, R. Haas, et al. (2009): “The impact of renewable en-
ergypolicyoneconomicgrowthandemploymentintheEuropeanUnion,”Brussels, Belgium:
| European  | Commission, |        | DG     | Energy and | Transport.        |     |     |     |     |
| --------- | ----------- | ------ | ------ | ---------- | ----------------- | --- | --- | --- | --- |
| Slattery, | M.          | C., E. | Lantz, | and B.     | L. Johnson(2011): |     |     |     |     |
“Stateandlocaleconomicimpacts
from wind energy projects: Texas case study,” Energy Policy, 39, 7930–7940.
Sunak, Y. and R. Madlener(2016): “Theimpactofwindfarmvisibilityonpropertyvalues:
| A spatial | difference-in-differences |     |     | analysis,” |     | Energy | Economics, | 55, 79–91. |     |
| --------- | ------------------------- | --- | --- | ---------- | --- | ------ | ---------- | ---------- | --- |
WindEurope
|     |     | (2018): | “Wind | in power | 2017,” | .   |     |     |     |
| --- | --- | ------- | ----- | -------- | ------ | --- | --- | --- | --- |
25

Xia, F. and F. Song (2017a): “Evaluating the economic impact of wind power development
| on local economies | in China,” | Energy Policy, | 110, 263–270. |
| ------------------ | ---------- | -------------- | ------------- |
——— (2017b): “The uneven development of wind power in China: Determinants and the role
| of supporting | policies,” Energy | Economics, | 67, 278–286. |
| ------------- | ----------------- | ---------- | ------------ |
26

Appendix
A Data description
atipac
rep
rewop
dellatsni
fo
muS
08
06
04
02
0
0003
0052
0002
0051
0001
setar
tnemyolpmenu
fo
muS
1995 2000 2005 2010 2015
Year
Sum of unemployment rates
Sum of installed power per capita
Figure A.1: Total new installed power and unemployment
27

|     | 0963 | 0963 0963 | 0963 0963 0963 | 0963 7863 | 0963 0963 | 0963 0963 | 0963 0963 | 0963 0963 | 0963 0963 | 0963 0963 |
| --- | ---- | --------- | -------------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- |
N
|     |             |               |                      |              |     | 887.0242 | 261.0767   |        |              | 698.8775 122.0085 |
| --- | ----------- | ------------- | -------------------- | ------------ | --- | -------- | ---------- | ------ | ------------ | ----------------- |
|     | .xaM 774.81 | 572.62 450.51 | 736.81 412.83 696.93 | 672.24 68.02 |     |          | 084606     | 878.32 | 865.54 49.52 |                   |
|     |             |               |                      |              | 0 0 | 0        |            | 1      |              |                   |
|     |             |               |                      |              |     | 161.566  |            |        | 546.51-      | 601.771 572.072   |
|     | .niM 83.1   | 606.1 985.    | 894. 579. 727.1      | 265.1        |     |          | 4361 710.4 | 830.6  | 611.8        |                   |
|     | rewop       |               |                      | 0            | 0 0 | 0        |            | 0      |              |                   |
oN
|     | .veD  |             |                   |             |     |         | 262.69026 |             |             |                 |
| --- | ----- | ----------- | ----------------- | ----------- | --- | ------- | --------- | ----------- | ----------- | --------------- |
|     |       |             |                   |             |     | 200.343 | 262.1501  |             |             | 351.045 887.145 |
|     | 617.2 | 384.3 254.2 | 326.2 652.5 603.4 | 433.4 109.2 |     |         |           | 994.0 366.2 | 324.6 966.3 |                 |
|     |       |             |                   |             | 0 0 | 0       |           |             |             |                 |
.dtS
|     |       |             |               |        |     | 304.2621 | 915.46104 |        |        | 191.0501 878.5501 |
| --- | ----- | ----------- | ------------- | ------ | --- | -------- | --------- | ------ | ------ | ----------------- |
|     | naeM  |             | 487.11 458.01 | 685.01 |     |          | 834.024   | 589.31 | 817.12 |                   |
|     | 389.6 | 985.8 694.5 | 32.5          | 280.6  |     |          |           | 664.0  | 613.1  |                   |
|     |       |             |               |        | 0 0 | 0        |           |        |        |                   |
scitsitats
|     | 2412 | 2412 2412 | 2412 2412 2412 | 2412 9312 | 2412 2412 | 2412 2412 | 2412 2412 | 2412 2412 | 2412 2412 | 2412 2412 |
| --- | ---- | --------- | -------------- | --------- | --------- | --------- | --------- | --------- | --------- | --------- |
N
| yrammuS |             |               |                      |               |               | 756.7352 | 854.4441 |        |        | 965.6068 083.1068 |
| ------- | ----------- | ------------- | -------------------- | ------------- | ------------- | -------- | -------- | ------ | ------ | ----------------- |
|         | .xaM 592.81 | 817.52 954.71 | 603.71 444.73 403.33 | 504.73 607.02 | 000222 321.23 | 411.34   | 189164   | 754.22 | 466.34 |                   |
49.52
1
:1.A
|       |                  |       |             |      |     | 185.698 |            |       | 546.51- | 666.033 348.723 |
| ----- | ---------------- | ----- | ----------- | ---- | --- | ------- | ---------- | ----- | ------- | --------------- |
|       | rewop .niM 484.1 | 327.1 | 683.1 539.1 |      |     |         | 3462 939.4 | 148.4 | 768.9   |                 |
|       |                  | 358.  | 926.        | 714. |     |         |            |       |         |                 |
| elbaT |                  |       |             | 0    | 0 0 | 0       |            | 0     |         |                 |
emoS
.veD
|     |       |             |                   |             | 47.44311 |         | 678.89764 |             |             |                 |
| --- | ----- | ----------- | ----------------- | ----------- | -------- | ------- | --------- | ----------- | ----------- | --------------- |
|     |       |             |                   |             |          | 462.453 | 818.671   |             |             | 986.535 639.535 |
|     | 906.2 | 691.3 824.2 | 812.2 928.4 453.4 | 966.4 948.2 | 352.1    | 295.4   |           | 774.0 556.2 | 790.6 283.3 |                 |
.dtS
589.62082
|     |            |       |                     |              | 161.3932 | 721.6151 | 543.901 |              |              | 680.8801 493.3901 |
| --- | ---------- | ----- | ------------------- | ------------ | -------- | -------- | ------- | ------------ | ------------ | ----------------- |
|     | naeM 272.6 | 337.7 | 214.4 793.01 445.01 | 157.01 431.6 | 991.0    | 911.2    |         | 153.0 712.31 | 914.32 785.1 |                   |
5
)cp
|     |      |     |                   |             |      | )cp |         | )51<( | )56>( cp |     |
| --- | ---- | --- | ----------------- | ----------- | ---- | --- | ------- | ----- | -------- | --- |
|     |      |     | )ts1( )dn2( )dr3( | )ceS( )inU( | )WK( |     |         |       |          |     |
|     |      |     |                   |             | WK(  |     |         |       | 3STUN    |     |
|     | etar |     |                   |             |      | WK( | ytisned |       |          |     |
cp
|     |              |        |                                        |                           |                     |        |     |       | ylredle | cp       |
| --- | ------------ | ------ | -------------------------------------- | ------------------------- | ------------------- | ------ | --- | ----- | ------- | -------- |
|     |              |        | tnemyolpmenU tnemyolpmenU tnemyolpmenU | tnemyolpmenU tnemyolpmenU |                     |        |     | gnuoy |         |          |
|     | tnemyolpmenU | pmenu  |                                        |                           | dellatsni dellatsni |        |     |       |         | gnidneps |
|     |              | .pmenu |                                        |                           |                     | .mucca |     |       |         | eunever  |
htworg
noitalupoP noitalupoP
|     |     |     |     |     |     |     |     | fo  | fo  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
elbairaV
elameF
|     |     |      |     |     |             |            |     | thgieW | thgieW |             |
| --- | --- | ---- | --- | --- | ----------- | ---------- | --- | ------ | ------ | ----------- |
|     |     | elaM |     |     | rewoP rewoP | rewoP SPEN |     |        | PDG    | latoT latoT |
ytiC
28

| B Further |     | results |              |     |           |          |               |     |     |
| --------- | --- | ------- | ------------ | --- | --------- | -------- | ------------- | --- | --- |
|           |     | Table   | B.1: Further |     | testes to | baseline | specification |     |     |
|           |     |         | (1)          |     | (2)       |          | (3)           | (4) | (5) |
| VARIABLES |     |         | FE           |     | FE        |          | FE            | FE  | FE  |
| power     |     |         | -0.0536**    |     |           |          |               |     |     |
it+2
(0.0256)
| power |     |     | -0.0777*** |     | -0.0750*** | -0.0749*** |     | -0.0805*** | -0.0747*** |
| ----- | --- | --- | ---------- | --- | ---------- | ---------- | --- | ---------- | ---------- |
it+1
|        |     |     | (0.0232) |     | (0.0238) | (0.0236) |     | (0.0237) | (0.0239) |
| ------ | --- | --- | -------- | --- | -------- | -------- | --- | -------- | -------- |
| Apower | it  |     |          |     | 0.0108   | 0.0001   |     |          |          |
|        |     |     |          |     | (0.0296) | (0.0325) |     |          |          |
| Apower |     |     |          |     |          | 0.0119   |     |          |          |
it−1
(0.0395)
| power |     |     | -0.0204 |     |     |     |     | -0.0030 | 0.0027 |
| ----- | --- | --- | ------- | --- | --- | --- | --- | ------- | ------ |
it
|            |     |     | (0.0254) |     |     |     |     | (0.0319) | (0.0325) |
| ---------- | --- | --- | -------- | --- | --- | --- | --- | -------- | -------- |
| power it−1 |     |     |          |     |     |     |     | -0.0140  | -0.0112  |
|            |     |     |          |     |     |     |     | (0.0244) | (0.0242) |
| power      |     |     |          |     |     |     |     |          | -0.0011  |
it−2
(0.0354)
Constant 11.7923*** 11.0727*** 11.0733*** 11.0799*** 9.5523***
|              |                   |             | (1.3702)   |              | (1.4344) | (1.4349)         |         | (1.4327)        | (1.4597) |
| ------------ | ----------------- | ----------- | ---------- | ------------ | -------- | ---------------- | ------- | --------------- | -------- |
| Observations |                   |             | 4,998      |              | 5,276    |                  | 5,276   | 5,276           | 4,998    |
| R-squared    |                   |             | 0.7223     |              | 0.7035   | 0.7035           |         | 0.7035          | 0.7273   |
| Number       | of municipalities |             | 278        |              | 278      |                  | 278     | 278             | 278      |
|              | Robust            | standard    | errors     | clustered    | by       | municipality.    | SE      | in parentheses. |          |
|              |                   | Null        | hypothesis | is rejected: |          | ***1%, **5%      | and     | *10%            |          |
|              | All               | regressions | include    | time dummies |          | and all baseline | control | variables.      |          |
29

| C Summary      |          | statistics: |       | Revenues     |      |            |         |     |           |       |
| -------------- | -------- | ----------- | ----- | ------------ | ---- | ---------- | ------- | --- | --------- | ----- |
|                |          |             | Table | C.1: Summary |      | statistics |         |     |           |       |
|                | Variable |             |       | Mean         | Std. | Dev.       | Min.    |     | Max.      | N     |
| Total Revenues |          | pc          |       | 1,069.657    |      | 539.903    | 270.275 |     | 8,601.380 | 5,832 |
| Own Revenues   |          | pc          |       | 324.218      |      | 204.789    | 42.069  |     | 2,713.208 | 5,832 |
Revenue Sale Goods Services pc 86.996 66.53 0.004 691.193 5,832
| Property | Revenues     | pc       |     | 27.161  |     | 35.101  |        | 0   | 621.794   | 5,832 |
| -------- | ------------ | -------- | --- | ------- | --- | ------- | ------ | --- | --------- | ----- |
| Direct   | Tax Revenues |          | pc  | 152.168 |     | 130.791 | 6.225  |     | 1,470.485 | 5,832 |
| Indirect | Tax          | Revenues | pc  | 11.43   |     | 21.635  | -4.098 |     | 554.811   | 5,832 |
| Revenue  | Capital      | Sale     | pc  | 13.162  |     | 36.925  | -0.206 |     | 1,771.438 | 5,832 |
Total Expenditures pc 1,064.109 538.782 177.106 8,606.569 5,832
000053
08
atipac rep rewop dellatsni fo muS
seunever lapicinum fo muS
|     |     | 06  |     |     |     |     |     |     | 000003 |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- |
04
000052
02
000002
0
|     |     | 1995 | 2000 | 2005 |     | 2010 |     | 2015 |     |     |
| --- | --- | ---- | ---- | ---- | --- | ---- | --- | ---- | --- | --- |
Year
Sum of municipal revenues
Sum of installed power per capita
|     |     | Figure C.1: | Total | new installed | power | and | municipal | revenues |     |     |
| --- | --- | ----------- | ----- | ------------- | ----- | --- | --------- | -------- | --- | --- |
30
