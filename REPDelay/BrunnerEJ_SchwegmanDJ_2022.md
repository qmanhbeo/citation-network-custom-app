d
Commercial Wind Energy Installations and Local Economic Development:
e
Evidence from U.S. Counties
w
December 2021 e
i
v
e
Abstract
We examine the causal impact of wind energy installation on ther local economies of counties in the
United States. Using data on the universe of commercial wind energy installations from 1995-2018 and a
difference-in-differences instrumental variable identification strategy, we find that wind energy
r
installation led to economically meaningful and statistically significant increases in county GDP per-
capita, income per-capita, median household income,e and median home values. We also find evidence
that while wind energy installation has little effect on total employment, the composition of local
employment shifts away from farm towards non-farm employment, notably leading to an increase in
e
construction and manufacturing employment. Finally, we show that the impact of wind energy installation
on local economic development varies significantly by installed capacity and by county urban/rural status.
p
Keywords: wind energy, economic development, economic impact, renewable energy
t
o
n
t
n
i
r
p
e
r
P
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4030617

d
e
I. Introduction
In the past 25 years, wind energy has grown from a novel energy source to noww representing
close to 40 percent of all new commercial energy installations in the United States. Installed wind energy
e
capacity has grown from less than 2 gigawatts in 1995 to over 122 gigawatts in 2020 (Center for
i
Sustainable Systems, 2021). The majority of these wind farms are located in rural communities and are
v
increasingly viewed as a potential source of economic development for rural counties which have
e
struggled to recover since the Great Recession (AWEA 2020; Munday, Bristow and Cowell, 2011;
r
Shoeib et al., 2021).
r
While there is a robust literature on the impact of wind energy on property values (Hoen et al.,
e
2011; Lang et al., 2014; Hoen et al., 2015; Gibbons, 2015; Hoen and Atkinson-Palombo, 2016; Sunak and
e
Madlener, 2016; Jensen et al., 2018), a relatively small set of studies have examined the impact of
commercial wind energy on local economipc development. What evidence is available comes primarily
from studies that focus on specific states or regions and use project-based case studies or input/output
t
models to estimate the effect of wind energy on local economic development (e.g., De Silva et al., 2016;
o
Slattery et al., 2011; Loomis et al., 2016; Faturay et al., 2020). Furthermore, much of this literature is
n
descriptive, providing estimates of the conditional correlation rather than the causal relationship, between
wind energy installation and local economic development.1
t
The purnpose of this paper is to provide new and nationally representative evidence on the causal
impact of commercial wind energy installation on local economic development. We exploit variation in
i
r
the location and timing of adoption of wind energy installations across counties to provide new evidence
p
on the causal impact of commercial wind energy on local economic development. We combine data on
e
the timing, location, and capacity of the universe of wind energy installations in the U.S. from 1995-2018
r
P
1 Exceptions include Mauritzen (2020) who uses a difference-in-difference identification strategy to examine the
impact of wind energy installation on county wages and Shoeib, Renski and Infield (2022) who use difference-in-
differences and propensity score matching methods to examine the impact of large wind energy installations in rural
U.S. counties. We discuss these papers in more detail in Section II.
1
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4030617

d
with data from the Bureau of Economic Analysis (BEA), U.S. Bureau of Labor Statistics, and the U.S.
e
Census on a host of annual county-level measures related to economic development, namely: 1) GDP per-
w
capita; 2) income per-capita; 3) median household income; 4) median home values; 5) total employment;
and 6) the share of employment by industry. e
To isolate the causal effect of wind energy installation on county-level economic development,
i
v
we first estimate non-parametric event study models that allow us to examine the evolution of our
e
outcomes both before and after the introduction of commercial wind energy in a county. We then estimate
difference-in-differences instrumental variables models (DD IV)r where we relate our outcomes of interest
to annual installed wind energy capacity per-capita (measured in megawatts) in a county and account for
r
the potentially nonrandom location of wind energy inestallations by instrumenting for wind energy
capacity using county wind speeds. Further, we allow for separate treatment effects of wind energy
e
installation on our outcomes of interest in the construction phase (i.e., two years prior to an installation
p
generating electricity) and the operation phase (after an installation starts generating electricity).
We find that wind energy installation led to economically meaningful and statistically significant
t
increases in county-level GDP poer-capita, income per-capita, median household income, and median
home values. The increases in GDP, per-capita income, and median income begin in the construction
n
phase and accelerate during the operation phase. In contrast, wind energy installation appears to affect
housing values only dturing the operation phase. While we find that wind energy had little impact on total
n
employment, wind energy installation changes the composition of the local labor market with a shift away
i
from farm employment towards non-farm employment, notably through an increase in manufacturing and
r
consptruction employment.
We also document significant heterogeneity in all of our outcomes based on installed wind energy
e
capacity per-capita. Specifically, counties with installed wind capacity of less than the median
r
experienced only small changes in our outcomes of interest while those above the median and
P
particularly, those above the 75th percentile of installed capacity experienced much larger effects. Finally,
we find that the impact of wind energy installation differed for rural and non-rural counties, with rural
2
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4030617

d
counties experiencing larger increases in GDP per-capita and the share of employment in the construction
e
and manufacturing sectors. We also find that while the adoption of commercial wind energy led to
w
declines in total population in more urban counties it had no effect on total population in rural counties.
e
2. Background and Related Literature
i
Wind energy is an increasingly important energy source in the United States, particularly in the
v
western and southwestern states. In 2020, there were over 1,500 commercial wind installations in the
e
United States, consisting of over 60,000 utility-scale wind turbines capable of producing enough
r
electricity to power 32 million homes (AWEA 2020). Over the past three decades, both the number of
r
commercial wind installations and installed wind energy generating capacity has grown tremendously.
e
Figure 1 presents the distribution of county-level wind energy capacity in 1995 and 2019. As shown in
e
Figure 1A, in 1995, wind energy production was extremely rare and was concentrated almost entirely in
California and to a lesser degree in Texas apnd there were only 7 counties in the U.S. with wind energy
installations, producing less than 2 gigawatts of power. As shown in Figure 1B, by 2019, installed wind
t
energy generating capacity had grown to over 122 gigawatts and wind energy production had spread
o
across 670 counties and 38 states. The vast majority of these wind energy installations are concentrated in
n
the western, south western, and central United States, and there is significant variation in installed wind
energy capacity both ac ross states, as well as across counties within a state.
t
As noted by Brown et al. (2012), wind energy advocates often tout the potential local economic
n
benefits, as well as the global, national, and local environmental benefits, of wind energy. There are a
i
r
number of ways that commercial wind energy installations can affect the local economies in which they
p
are situated. Commercial wind energy can have a direct effect on local employment, income and GDP
e
per-capita by providing jobs, notably construction jobs, to those working on building the wind
rinstallations and income through lease payments to local landowners. These income and employment
P
effects should materialize during the construction phase, as work begins on constructing the turbines and
lease payments begin to landowners, and continue through the operation phase, although the employment
3
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4030617

d
effects during the operation phase may be diminished as less labor is needed once the turbines become
e
operational. Commercial wind energy can also have indirect effects on local economic development via
w
the effect of wind installations (and those working on building the installations) on the consumption of
locally produced goods (e.g., hardware, constructional material, etc.) and servicees (e.g., restaurants,
hotels, environmental management, consultants, etc.). These indirect consumption effects will provide
i
v
additional income and increase employment for these other services and sectors in the local economy.
e
Commercial wind energy installations can also directly affect the local tax base of the
jurisdictions in which they reside. The increase in the local tax barse along with any payments in lieu of
taxes (PILOTS) or other forms of indirect compensation to local governments, can then be used by local
r
governments to increase public services and/or providee property tax relief to local citizens. Consistent
with that notion, Kahn (2013), Silva et al. (2016), Castleberry and Green (2017), and Brunner, Hoen, and
e
Hyman (forthcoming) find evidence that wind energy installation led to increases in public school
p
spending and in some cases declines in local property tax rates. In related work, Brunner and Schwegman
(2021) find evidence that wind energy installation led to increases in county own-revenues and
t
expenditures with particularly laorge increases in highway and hospital expenditures.
As noted previously, much of the existing literature on the impact of wind energy installation on
n
economic development focuses on regional or national impacts and uses project-based case studies or
input/output models tto estimate the economic impacts of wind power developments (e.g., Government
n
Accountability Office, 2004; Greene and Geisken, 2013; Pedden, 2006; Slattery et al., 2011; Loomis et
i
al., 2016; Faturay et al., 2020). More recently a smaller set of studies has begun to use econometric
r
technpiques to estimate the economic impact of wind power developments at the local level (e.g., Brown et
al., 2012; Hartley et al., 2015; De Silva et al., 2016; Mauritzen, 2020; Shoeib et al., 2022).
e
Using an ex-post econometric model and national data on changes in installed wind energy
r
capacity per-capita from 2000 through 2008, Brown et al. (2012) found an $11,000 increase in per-capita
P
income and an increase of 0.5 jobs per megawatt of wind power capacity per-capita. Using county-level
data from Texas, Hartley et al. (2015) and De Silva, McComb, and Schiller (2016) find a fairly small
4
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4030617

d
impact of wind energy installation on local employment and wages, while De Silva, McComb, and
e
Schiller (2016) find significant increases in per capita income accompanying wind power development.
w
Most recently, Shoeib et al. (2021) examine the impact of large (over 100 MW in 2012) wind energy
installations on community services, the cost of living and employment in 11 rureal counties located in five
different states. They provide descriptive evidence that wind energy installation led to a modest increase
i
v
in construction employment (particularly during the construction phase) and that wind development tax
e
income improved community services without any noticeable increase in local taxes or cost of living.
In the two studies closest to ours, Mauritzen (2020) usesr national data on rural counties to
examine the impact of wind energy installation on county wages while Shoeib et al. (2022) uses data on
r
rural and non-rural counties to examine the impact ofe wind energy installation on employment, income,
poverty rates and population. Using a Bayesian multilevel model, and a difference-in-differences research
e
design, Mauritzen (2020) finds evidence of a modest increase in wages associated with wind energy.
p
Similarly, using a difference-in-differences research design and data on wind energy installations from
1990 to 2015, Shoeib et al. (2022) find that wind energy led to increases in per-capita income and small
t
increases in employment per-caopita. They also find that wind energy installation is associated with small
declines in county-level poverty rates, unemployment rates and population, particularly for counties with
n
higher wind speeds.2
We contributte to this existing literature in several ways. First, we employ an identification
n
strategy that explicitly accounts for biases that can arise due to nonrandom selection into treatment (i.e.,
i
adoption of wind energy installations) and in models with staggered timing of treatment and
r
heterpogeneous treatment effects. Second, we provide new evidence on the heterogeneous effects of wind
energy installations with respect to wind energy capacity per-capita and with respect to whether a wind
e
energy installation is located in a more rural or urban county. Third, we examine the effect of wind energy
r
P
2 Using propensity score matching techniques, Shoeib et al. (2022) also find that wind energy installation had
insignificant effects on county employment per-capita, unemployment rates or per-capita income in rural counties
with large wind energy installations (over 100 MW).
5
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4030617

d
installations on a broader set of outcomes including median home values and manufacturing and
e
construction employment shares within a county.
w
Finally, our paper contributes to the literature on how wind energy affects home values. A
relatively large body of literature has examined how proximity to wind turbines eimpacts individual home
values. Within the U.S. context, the evidence is mixed but the majority of the literature has found
i
v
insignificant effects of wind turbines on home values (e.g., Laposa and Mueller 2010; Hoen et al. 2015;
e
Sampson et al. 2020). For example, Hoen et al. (2015) use data on over 50,000 homes, including 1,198
homes within 1 mile of a turbine and find negative but small andr insignificant effects of turbines on
homes located in close proximity to turbines. Lang, Opaluch & Sfinarolakis (2014), reach a similar
r
conclusion using data on 48,554 housing transactionse in Rhode Island while Sampson et al. (2020) find
that wind turbines did not affect agricultural property values. Our paper contributes to this literature by
e
providing some of the first evidence on how large-scale wind energy developments affect home values at
p
the county level via their effect on local economic development.3
3. Data
t
We construct a county-loevel panel dataset that combines information on the universe of wind
energy installations in the United States with data from a variety of sources pertaining to local economic
n
development. National data on installed wind capacity comes from the United States Wind Turbine
Database (USWTDBt), which is a turbine-level dataset with detailed information on the date each wind
n
turbine became operational, the nameplate capacity of each turbine measured in kilowatts, and the
i
longitude and latitude of each turbine. These data also include the county in which the turbine is located.
r
We tphen create a panel dataset containing annual data on total installed wind capacity in each county by
aggregating the capacity of every turbine in operation in a county in a given year up to the county level.
e
r
P
3 Brunner and Schwegman (2021) also examine the impact of wind energy installation on county-level home values
and find that wind energy increased home values on average by approximately 4 percent. We build on their work by
examining heterogeneity in housing value effects by installed capacity per-capita and by whether a county is
classified as rural or urban.
6
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4030617

d
We combine these data with county-specific data on Gross Domestic Product (GDP), per-capita
e
income and county-level employment by SIC industry codes from the Bureau of Economic Analysis. The
w
BEA’s data on GDP for counties begins in 2001, while data on total employment, farm employment,
construction employment, and manufacturing employment is available back to thee first year of our sample
time frame, namely 1995. We then combine these data with county-level total population, and median
i
v
household income data from the U.S. Census Bureau (adjusted to real 2012 dollars using the consumer
e
price index).
As we demonstrate later in the paper, wind energy instalrlation led to meaningful declines in
county population, particularly in less rural counties. As a result, if we standardize income per-capita,
r
GDP per-capita and other measures of economic deveelopment by annual population, we are likely to
conflate changes in these measures with changes that occur simply because of the effect wind energy
e
installation has on county population. We therefore standardize all of our outcomes that are measured in
p
per-capita terms by dividing by population in our base year, namely 1995.
Finally, we combine our county panel dataset with data on housing transactions and sale prices
t
from the Federal Housing Finanoce Agency (FHFA) Housing Price Index (HPI), which provides a county-
level weighted repeat-sales HPI for single-family homes with the base year set to 2000. We merge the
n
HPI data with data on median home values for each county from the 2000 decennial census and then
inflate this median hotme value using the HPI. This provides us with the median home value for each
n
county in each year. In keeping with the hedonics literature, in all analyses, we use the log of this home
i
value measure.
r
pIn all our specifications we include a number of county-level control variables taken from the
1990 Decennial Census, namely: 1) county population; 2) percent urban; 3) poverty rate; 4) the share of
e
the population 25 or older with a Bachelor’s degree or higher; 5) the share of the population that is non-
r
P
7
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4030617

d
white; 6) the share of the population that is 65 or older; and 7) the fraction of homeowners. We measure
e
county population in our base year of 1995, while all other variables are from 1990.4
w
We restrict our analytic sample in two primary ways. First, we drop counties that have a
cumulative installed wind energy capacity of 2 megawatts (MW) or less.5 Seconed, we drop a small
number of counties that had wind installations constructed prior to 1995, the beginning of our time
i
v
period. In some of our specifications, we also explicitly focus on rural counties to examine whether there
e
are important differences between how wind energy installation affects rural versus non-rural counties.
Specifically, we use the 1993 USDA rural–urban continuum codres to identify counties which the USDA
categorizes as “rural” implying a rural–urban continuum code of 6 or higher.6
r
Our final sample consists of 2,971 counties (2e,000 rural counties) over the period 1995-2018.
465 counties (338 rural counties) had a wind energy installation at some point between 1995 and 2018.
e
Table 1 provides summary statistics for our primary outcomes (top panel) and control variables (bottom
p
panel). We present separate summary statistics for the full sample of counties, and counties with and
without wind energy installations in Columns 1 through 3 and then the same information for the sample
t
of rural counties in Columns 4 tohrough 6. To better compare counties with and without commercial wind
energy installations, we present summary statistics for our outcomes of interest measured in the first year
n
the data is available. As Table 1 reveals, rural counties tend to have significantly smaller populations,
lower income and a htigher share of employment in the farming sector. For both the full sample and the
n
i
r
4 Given that all our empirical specifications include county fixed effects, all of the above variables enter our
specipfications as interactions between the variable and a linear time trend to allow for differential trending based on
these factors. Also note that all our results are robust if we include no controls or a more parsimonious set of
controls as one would expect if commercial wind energy installations are as good as randomly assigned.
e
5 Median turbine nameplate capacity was approximately 2.0 MW in 2016. Thus, a cumulative installed capacity of 2
MW or less, represents a single wind turbine which is typically intended for private on-site use rather than being part
rof a larger wind energy project designed for commercial electrical generation. Our results are robust to this
restriction.
P6 A code of 6 or higher includes: “Urban, adjacent to metropolitan area, 2,500-19,999 population” (code 6); “Urban,
not adjacent to metropolitan area, 2,500-19,999 population” (code 7); “Rural, adjacent to metropolitan area, less
than 2,500 population” (code 8); and “Rural, not adjacent to metropolitan area, less than 2,500 population” (code 9).
We find similar, but much nosier, results if we define the “rural” sample as 7 or greater.
8
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4030617

d
rural sample, counties with commercial wind installations also tend to have smaller populations, higher
e
shares of the population that is non-Hispanic white, and a higher share of farm employment.
w
4. Methods
To examine the effect of wind energy on county economic developmente, we begin by presenting
a non-parametric difference-in-differences event study of the following form:
i
v
8
𝑦 =∑ 𝛾𝑇 +𝑿𝜃 𝜅+ 𝛿 +𝜆 +𝜂 , (1)
𝑖𝑡 𝑗=‒8 𝑗 𝑗,𝑖𝑡 𝑖 𝑡 𝑖 𝑡 𝑖𝑡 e
r
where 𝑦 denotes an outcome of interest for county i in year t and 𝑇 represents a series of lead and lag
𝑖𝑡 𝑗,𝑖𝑡
indicators for when a wind installation becomes operationarl in county i. We re-center 𝑇
𝑗,𝑖𝑡
so that 𝑇
0,𝑖𝑡
e
always equals one in the year the installation became operational. We include an indicator variable for 8
or more years prior to an installation becoming oeperational (‒𝑇 ), a series of indicators from 0 to 7
8,𝑖𝑡
years prior to an installation becoming operational (‒𝑇 to 𝑇 ), and a series of indicators for 1 to 8
p‒7,𝑖𝑡 0,𝑖𝑡
or more years after becoming operational (𝑇 to 𝑇 ). The omitted category for our treatment indicators
1,𝑖𝑡 8,𝑖𝑡
t
(i.e. the reference year for all estimates) is three years prior to a wind installation becoming operational (
o
𝑇 ). Our rationale for choosing three years prior to a wind energy installation becoming operational
‒3,𝑖𝑡
n
stems from the fact that, on average, wind energy installations take approximately two years to construct,
leading to employment effects and royalty and landlord lease payments prior to operations. In that sense,
t
counties with wnind energy installations are already “treated” two years prior to becoming operational. We
include both county fixed effects (𝛿) and year fixed effects (𝜆 ), and 𝜂 is a random disturbance term.
𝑖 𝑡 𝑖𝑡
i
r
Given that treatment (wind energy installation) occurs at the county level, in all specifications we cluster
p
the standard errors at the county level.
e
The coefficients of primary interest in equation (1) are the 𝛾'𝑠. The estimated coefficients on the
𝑗
r
lead treatment indicators ( 𝛾 , ..., 𝛾 ) provide evidence on whether the parallel trends assumption,
‒8 ‒4
P
which underlies all causal claims based on DD models, appears to hold. If wind energy installation
induces exogenous increases in county income, GDP, etc., these lead treatment indicators should be small
9
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4030617

d
in magnitude and statistically insignificant. The lagged treatment indicators (𝛾 , …,𝛾 ) allow the effect
0 +8 e
of wind energy installation on our outcomes of interest to grow over time and in a nonparametric way in
w
the post treatment period.
We include a vector of control variables (𝑿), namely 1995 population aend 1990 share urban,
𝑖
share 65 or older, share homeowner, share non-white, share of the population wiith a bachelor’s degree or
v
higher and the 1990 poverty rate, all interacted with a linear time trend (𝜃 ) to allow for differential
𝑡
e
trending by counties with different baseline (pre-treatment) values of these characteristics. We do not
r
include time-varying control variables because they could be affected by the installation of wind energy
(i.e., endogenous controls).
r
Several recent studies have shown that estimaetes from standard event studies and DD
specifications relying on the staggered timing of treatment for identification may be biased in the
e
presence of heterogeneous treatment effects (Callaway and Sant’Anna 2020; Sun and Abraham 2020;
p
Goodman-Bacon 2021). Specifically, in the presence of heterogeneous treatment effects, event study
estimates of lags and leads can be biased by the effects from other relative time periods (i.e., effects from
t
o
early versus later adopters). To address this concern, we employ the estimator developed by Sun and
Abraham (2020), which isn free from any contamination and bias that may arise in event study models
with staggered timing of treatment and heterogeneous treatment effects.
t
To improve the precision, we complement the event study specification with a binary difference-
n
in-differences (DD) specification. To avoid the potential biases noted above that arise in models with
i
staggered timing of treatment and heterogeneous treatment effects, we follow Cengiz et al. (2019) and
r
p
Goodman and Bacon (2021) and estimate a stacked DD model. Specifically, we first create a set of
edatasets that include observations from a cohort of counties where wind energy development becomes
operational in the same year and other counties that never had a wind energy development during our
r
Psample timeframe. We then append these cohort-specific datasets and estimate models of the following
form:
10
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4030617

d
𝑦 =𝛼 𝐶𝑜𝑛𝑠𝑡𝑟𝑢𝑐𝑡𝑖𝑜𝑛 +𝛼 𝑂𝑝𝑒𝑟𝑎𝑡𝑖𝑜𝑛 +𝑋𝜃 + 𝛿 +𝜆 +𝜀 , (2)
𝑖𝑡𝑐 1 𝑖𝑡 2 𝑖𝑡 𝑖 𝑡 𝑖𝑐 𝑡𝑐 𝑖𝑡𝑐 e
where 𝑦 is an outcome of interest for county i in year t and a member of cohort c, 𝐶w𝑜𝑛𝑠𝑡𝑢𝑐𝑡𝑖𝑜𝑛 is an
𝑖𝑡𝑐 𝑖𝑡
indicator that takes the value of one in the two years prior to a wind energy installation becoming
e
operational, zero otherwise, 𝑂𝑝𝑒𝑟𝑎𝑡𝑖𝑜𝑛 is an indicator that takes the value of one in all years after an
𝑖𝑡
i
installation becomes operational, 𝛿
𝑖𝑐
and 𝜆
𝑡𝑐
are vectors of county-by-cohvort and year-by-cohort fixed
effects respectively, 𝜀
𝑖𝑡𝑐
is a random disturbance term, and all other eterms are as defined in equation (1).
The coefficients of primary interest in equation (2) are 𝛼 and 𝛼 which represent the DD estimate of the
1 2r
effect of treatment (wind energy installation) on our outcomes of interest during the construction phase
r
and the operation phase respectively.
e
Next, to account for the fact that the capacity of wind energy installations varies across counties
e
and across time, in our preferred specification we allow for continuous treatment by replacing the two
p
binary treatment indicators in equation (2) with the installed wind capacity per-capita in a county in a
given year:
t
o
𝑦 =𝛽 𝐶𝑜𝑛𝑠𝑡𝑟𝑢𝑐𝑡𝑖𝑜𝑛_𝑀𝑊 +𝛽 𝑂𝑝𝑒𝑟𝑎𝑡𝑖𝑜𝑛_𝑀𝑊 +𝑿𝜃 + 𝛿 +𝜆 +𝜐 , (3)
𝑖𝑡𝑐 1 𝑖𝑡 2 𝑖𝑡 𝑖 𝑡 𝑖𝑐 𝑡𝑐 𝑖𝑡𝑐
n
where 𝑀𝑊 is installed wind capacity per-capita in county i in year t measured in megawatts per-capita,
𝑖𝑡
𝜐
𝑖𝑡𝑐
is a random distutrbance term, and all other terms are as defined in Equation (2).7 𝑀𝑊
𝑖𝑡
is equal to
n
zero for county-years with no installed wind energy. Thus, 𝑂𝑝𝑒𝑟𝑎𝑡𝑖𝑜𝑛_𝑀𝑊 , equals installed capacity
𝑖𝑡
i
per capita in all years following a wind energy installation becoming operational and zero otherwise and
r
𝐶𝑜𝑛𝑠p𝑡𝑟𝑢𝑐𝑡𝑖𝑜𝑛_𝑀𝑊 equals installed capacity per capita in the two years prior to a wind installation
𝑖𝑡
becoming operational and zero otherwise. The coefficients of primary interest in (3) are 𝛽 and 𝛽 which
e 1 2
represent the effect of a one-megawatt per-capita increase in installed wind energy capacity on our
r
Poutcomes of interest in the construction and operation phases respectively.
7 Similar to our per-capita outcomes, we standardize wind energy capacity by dividing it by 1995 population so that
the measure is not affected by changes in population that arise due to treatment.
11
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4030617

d
A potential concern with our DD specifications, is that counties with commercial wind energy
e
installations may be different from other counties along unobservable dimensions that may also affect
w
local economic development (i.e., nonrandom self-selection into treatment). For example, counties that
actively pursue commercial wind energy (potentially by offering tax abatementse and other incentives)
may be better primed and positioned for economic development than other counties, leading to estimates
i
v
that overstate the impact of commercial wind energy on local economic development. To address that
e
concern, in all our DD models, we account for the possibility of nonrandom self-selection into treatment
by adopting a difference-in-differences instrumental variables (DrD IV) identification strategy.
Specifically, we use average county wind speed as an instrumental variable in our DD framework given
r
by equations (2) and (3).8 Note that in our DD IV moedels, the coefficients of primary interest, 𝛽
1
and 𝛽
2
,
are now identified solely based on the portion of the variation in wind energy capacity per-capita that is
e
explained by wind speeds and thus our IV estimates net out all strategic behavior on the part of counties
p
or other unobservables that might be correlated with economic development.9
5. Results
t
We begin by presentingo the impact of commercial wind energy on our main outcomes of interest
by plotting the estimated 𝛾 n𝑗 '𝑠 and associated 90 and 95 percent confidence intervals from our event study
specification given by Equation 1. Figure 2A, 2B, 2C and 2D show that GDP per-capita, per-capita
income, median houstehold income, and median home values (all measured in logs) begin to increase after
n
a county installs wind energy. Importantly, there is no evidence of differential trending prior to the
i
installation of wind energy—the estimated pre-treatment effects are small in magnitude and nearly all are
r
p
e
8 Average county wind speed satisfies the conditions for a valid instrument given: 1) it is highly correlated with
rwind energy installation and total installed capacity (first-stage F-statistic always greater than 100), (2) it is as good
as randomly assigned (i.e., counties do not choose their wind speed), and (3) the only reason wind speed should
P
affect county economic development outcomes is through its effect on wind energy adoption and capacity.
9To construct the instrument, we interact average county wind speed with an indicator for having installed turbines
and use this as an instrumental variable for turbine capacity. Data on county wind speeds come from the Wind
Integration National Dataset (WIND) Toolkit (Draxl et al., 2015) and reflects wind speeds at a 100-meter height
(typical wind turbine height) over the period 2007-2013.
12
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4030617

d
statistically insignificant. The lack of differential trending prior to the installation of wind energy provides
e
evidence that our main identification assumption—the parallel trends assumption—holds.
w
We next examine the impact of wind energy installation on county employment patterns. Figure
2E shows that total employment is relatively unaffected by wind energy installateion. Figures 2F and 2G
show that the share of employment in the construction and manufacturing sectors respectively begin to
i
v
increase during the construction phase of wind energy installation and continues through the operation
e
phase while Figure 2H shows that these shifts in the share of employment dedicated to construction and
manufacturing are accompanied by a small decline in farm emploryment that begins later in the operation
phase. Finally, Figure 2I shows that wind energy installation is associated with a decline in total
r
population relative to counties without wind energy weith the decline in population starting during the
construction phase and continuing into the operation phase.
e
We present the DD IV estimates of the impact of wind energy installation in Table 2. Results
p
based on equation (2) with binary treatment are presented in columns 1 and 2 while results based on
equation (3) with continuous treatment are presented in columns 3 and 4. All results reported in Table 2
t
and subsequent tables are DD IVo estimates where we use average county wind speed as an instrumental
variable for wind energy adoption and wind energy capacity per-capita. Furthermore, similar to our event
n
study models, all of our outcomes other than employment shares and total population are measured in
natural logs so that thte estimates can be interpreted as rates of return. Column 1 presents the results from
n
equation (2) with only a single treatment indicator that equals one in all years after a wind energy
i
installation become operational (i.e., equation (2) without the 𝐶𝑜𝑛𝑠𝑡𝑟𝑢𝑐𝑡𝑖𝑜𝑛 indicator), whereas
𝑖𝑡
r
Colupmn 2 presents the results from the complete version of equation (2).
Beginning with Columns 1 and 2 in the top panel of Table 2, we find that wind energy led to
e
large increases in GDP per capita (approximately 6 percent), income per capita (5 percent), median
r
household income (3 percent), and home values (2.6 percent). As shown in column 2, the impact of wind
P
energy installation on GDP and both income measures begins during the construction phase and the
impact increases during the operating phase. For example, GDP per-capita increases by 2 percent during
13
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4030617

d
the construction phase and by 7 percent during the operation phase. In contrast, home values only increase
e
after a wind energy installation has begun operating. Finally, consistent with the event study figures
w
presented above, we find that wind energy installation leads to a decline in total population. This
population decline begins during the construction phase (although the estimate ise not statistically
significant) and accelerates during the operation phase.
i
v
We present the employment outcomes in the bottom panel of Table 2. Consistent with the event
e
studies presented above, wind energy appears to have little impact on total employment. However, wind
energy installation causes a small decline in farm employment (ar decrease of 0.2 percent) and a shift from
farm employment towards construction and manufacturing employment. Specifically, wind energy
r
installation leads to a 1.3 percent increase in the sharee of manufacturing employment and a 0.7% increase
in the share of construction employment. As shown in Column 2, this increase in the share of employment
e
in construction and manufacturing began during the construction phase, which is consistent with the event
p
studies presented above.
Our per-capita income results are consistent with Brown et al. (2012), De Silva et al. (2016) and
t
Shoeib et al. (2022) who also finod positive impacts of wind energy installation on per-capita income.
Similarly, our total employment results are generally consistent with the prior literature which tends to
n
find small effects of wind energy installation on employment.
The DD modtels with binary treatment are useful because they provide an intuitive and easy to
n
interpret estimate of the impact of wind energy installation on our outcomes. However, these models
i
suffer from two drawbacks. First, as in the event-study analysis, the binary treatment variable turns on
r
whenp the first installation in a county occurs, and so it does not capture the increased capacity of
subsequent installations for the 58.71 percent of counties with multiple installations over time. Second,
e
the binary treatment variable misses important variation stemming from different wind energy
r
installations having very different installed capacity. The distribution of installed wind capacity per capita
P
is heavily right skewed: the 10th and 25th percentiles of installed capacity per capita in our sample among
14
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4030617

d
counties with installed wind energy are 0.0006 MW/capita and 0.0009 MW/capita, respectively, while the
e
75th and 90th percentiles are 0.014 and 0.036 MW/capita.
w
Given these limitations, in columns 3 and 4 of Table 2 we present results based on equation (3)
where we use a continuous measure of treatment, namely installed capacity (meaesured in megawatts) per
capita. The direct interpretation of these coefficients is the estimated effect of a one MW increase in
i
v
installed capacity per capita. Thus, an increase of one MW per capita of installed capacity increased GDP
e
per capita by 507 percent. Note however, that the average installed capacity in the full sample is 0.0168
MW/capita. Thus, as we show in column 5, evaluated at the mearn capacity per-capita, wind energy
installation increases GDP per capita by 8.5 percent (5.07 MW / per capita x 0.0168). Similarly, we find
r
that the average wind installation increased per capitae income by approximately 6 percent, median
household income by 4 percent, home values by approximately 7 percent, and decreased total population
e
by approximately 5,300 people. Consistent with column 2, we find that wind energy installation began
p
affecting GDP, per capita income, and median household income during the construction phase (see
Column 4).
t
As seen in the bottom poanel of Table 2, we continue to find no impact on total employment: the
estimated coefficients are small in magnitude and statistically insignificant. However, we continue to find
n
a decrease in farm employment—a 0.3 percent decline (-0.18 x 0.016 MW / capita) at the mean of
capacity per-capita. Utsing a continuous measure of installed capacity, we find that wind energy led to a
n
1.6 percent increase in the share of manufacturing employment and a 0.8 percent increase in the share of
i
construction employment.
r
A. Hpeterogeneity by Capacity per Capita and Rural and Non-Rural Designation
As noted previously, there is wide variation in the distribution of capacity per capita across
e
counties with wind energy installations. Consequently, the mean effects reported in column 5 of Table 2
r
could mask important heterogeneity in the impact of wind energy installation across the distribution of
P
capacity. Thus, in columns 6 and 7 of Table 2 we show effects at the median and 75th percentile of
capacity per capita. For example, the effect of wind energy installation on GDP per capita at the median is
15
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4030617

d
a 1.8 percent increase (relative to the GDP per-capita in the control counties), and at the 75th percentile the
e
effect is 7.2 percent. Similarly, the effects on home values at the median and 75th percentile are 2 percent
w
(a $1,88610 increase) and 6 percent (a $5,658 increase), respectively.
We show in Figure 3 the effects on a select number of our outcomes of ienterest by ventiles of
installed capacity, revealing the same patterns. The effects of wind installation on our outcomes of
i
v
interest for counties in the bottom half of the distribution are quite small but increase at an increasing rate
e
past the 50th percentile.
Proponents have touted commercial wind energy as a portential source of economic development
for rural counties which have struggled to recover both in terms of job and population growth since the
r
Great Recession. Thus, in Figure 4, we present event estudy estimates of the impact of wind energy
installation on a select number of outcomes separately for urban counties (in blue) and rural counties (in
e
red).11
p
Figures 4A through 4F reveal some important heterogeneity between rural and non-rural counties.
For example, while wind energy has a negative impact on population in urban counties, it has very little,
t
if any, impact on the populationo of rural counties (see Figure 4F). The impact of wind energy on the local
economy (GDP) is much gnreater in rural counties than urban counties (see Figure 4A) and as shown in
Figure 4D and 4E, wind energy installation led to a greater shift towards construction and manufacturing
employment in rural tcounties compared to urban counties. Perhaps more importantly, this shift towards
n
manufacturing and construction employment persists past the construction phase.
i
Figure 5 provides one explanation for why rural counties appear to benefit more in terms of GDP
r
per-cpapita and employment than more urban counties. Specifically, Figure 5 shows the distribution of
installed wind energy capacity per-capita among rural and more urban counties, with the mean value of
e
capacity per-capita in both distributions illustrated with a vertical line. As the figure makes clear, the
r
P
10 The average home value in counties without turbines in 2000 is $94,298.
11 Specifically, we present separate estimates based on equation (1) where the full sample of counties is split based
on whether it is coded as rural or more urban.
16
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4030617

d
distribution of capacity is significantly more rightward skewed among the sample of rural counties with
e
mean capacity per-capita being significantly higher among rural counties (0.0253 MW per-capita) than
w
more urban counties (0.0017 MW per-capita).
We present DD IV estimates of the impact of wind energy installation separaetely for rural and more
urban counties in Table 3. In the interest of brevity, we present only the results based on our preferred
i
v
specification with continuous treatment (i.e. equation 3) and show estimated impacts at the mean, 50th and
e
75th percentiles of the distribution of capacity per-capita among the respective samples of rural and more
urban counties. The results reported in Table 3 mirror the event srtudy results presented in Figure 4.
Specifically, we find that wind energy installation has little impact on the total population of rural
r
counties. This stands in stark contrast to the results foer more urban counties where we find a relatively
sharp decline in population. Similar to the event studies above, wind energy installation has a larger
e
impact on GDP, and to a slightly lesser extent, per-capita and median income among rural counties than
p
among more urban counties. Finally, the impact on the composition of the local labor market is more
pronounced in the rural sample than the full sample: wind energy installation has a greater impact on the
t
share of the local labor market ion the construction and manufacturing sectors in rural counties than in
more urban counties.
n
6. Conclusion & Policy Implications
In this papert, we use data on the timing, location, and capacity of the universe of wind energy
n
installations in the U.S. from 1995 through 2018 to provide novel evidence on the impact of commercial
i
wind energy on county economic development. We use event-study and difference-in-differences
r
instrpumental variable methodologies that exploit the plausibly exogenous timing and location of wind
energy installations and variation in average county wind speeds to examine the impacts of wind energy
e
installation on county-level GDP per-capita, income per-capita, median household income, median home
r
values, total employment, and the share of employment by industry.
P
We find that wind energy installation led to exogenous and economically meaningful increases in
in county-level GDP per-capita, income per-capita, median household income and median home values
17
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4030617

d
with the increases in county GDP and income beginning in the construction phase of wind energy
e
installation and accelerating during the operation phase. While we find that wind energy installation has
w
little impact on total employment, the composition of local employment shifts away from farm
employment towards non-farm employment, notably leading to increases in consetruction and
manufacturing employment. Finally, we show that the impact of wind energy installation on local
i
v
economic development varies significantly by installed capacity and by county urban/rural status.
e
To reduce its carbon emissions and transition away from fossil fuels, the United States must
invest in renewable energies. Collectively, the results of this paprer suggest that wind energy not only
provides a renewable source of energy but it also has the potential to improve the local economies of the
r
communities in which these energy installations are leocated. Furthermore, our results suggest that the
positive impacts of commercial wind energy on county economic development are larger for more rural
e
counties. Specifically, relatively to more urban counties with wind energy installations, rural counties
p
experience larger increases in GDP per-capita and the share of employment in construction and
manufacturing with no measurable displacement of the population. As rural communities continue to
t
struggle with population declineo and a limited tax base, our results suggest that wind energy investments
may stimulate and diversify local rural economies.
n
t
n
i
r
p
e
r
P
18
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4030617

d
References
e
American Wind Energy Association (AWEA). 2020. Wind Powers America Annual Report 2019.
w
Brown, J. P., Pender, J., Wiser, R., Lantz, E., & Hoen, B. (2012). Ex post analysis of economic impacts
from wind power development in US counties. Energy Economics, 34(6), 1743-1754.
e
Brunner, E, Hoen, B., & Hyman J. (forthcoming). School District Revenue Shocks, Resource Allocations,
and Student Achievement: Evidence from the Universe of U.S. Wind Energy Installations. Journal
i
of Public Economics.
v
Brunner, E. & Schwegman, D. (2021). Windfall Revenues from Windfarms: How do County
e
Governments Respond to Increases in the Local Tax Base Induced by Wind Energy Installations?.
Working Paper.
r
Callaway, B., & Sant’Anna, P. H. (2020). Difference-in-differences with multiple time periods. Journal
of Econometrics.
r
Castleberry, B. & Greene, S.. (2017). Impacts of Wined Power Development on Oklahoma’s Public
Schools. Energy, Sustainability and Society 7(1), 34.
e
Center for Sustainable Systems, University of Michigan. 2021. “Wind Energy Factsheet.” Pub. No.
CSS07-09
p
De Silva, D. G., McComb, R. P., & Schiller, A. R. (2016). What blows in with the wind?. Southern
Economic Journal, 82(3), 826-858.
t
Faturay, F., Vunnava, V. S. G., Lenzen, M., & Singh, S. (2020). Using a new USA multi-region input
output (MRIO) model for aossessing economic and energy impacts of wind energy expansion in USA.
Applied Energy, 261, 114141.
n
Goodman-Bacon, A. (2021). Difference-in-differences with variation in treatment timing. Journal of
Econometrics.
Greene, J. S., & Geistken, M. (2013). Socioeconomic impacts of wind farm development: a case study of
Weatherfonrd, Oklahoma. Energy, Sustainability and Society, 3(1), 1-9.
Hartley, P. R., Medlock III, K. B., Temzelides, T., & Zhang, X. (2015). Local employment impact from
i
competing energy sources: Shale gas versus wind generation in Texas. Energy Economics, 49, 610-
r
619.
p
Hoen, B., Brown, J. P., Jackson, T., Thayer, M. A., Wiser, R., & Cappers, P. (2015). Spatial hedonic
analysis of the effects of US wind energy facilities on surrounding property values. The Journal of
e
Real Estate Finance and Economics, 51(1), 22-51.
rJensen, C. U., Panduro, T. E., Lundhede, T. H., Nielsen, A. S. E., Dalsgaard, M., & Thorsen, B. J. (2018).
The impact of on-shore and off-shore wind turbine farms on property prices. Energy Policy, 116, 50-
P
59.
Kahn, M. E. (2013). Local non-market quality of life dynamics in new wind farms communities. Energy
Policy, 59, 800-807.
19
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4030617

d
e
Lang, C., Opaluch, J. J., & Sfinarolakis, G. (2014). The windy city: Property value impacts of wind
turbines in an urban setting. Energy Economics, 44, 413-421.
w
Loomis, D. G., Hayden, J., Noll, S., & Payne, J. E. (2016). Economic impact of wind energy development
in Illinois. Journal of Business Valuation and Economic Loss Analysis, 11(1), 3-23.
e
Mauritzen, J. (2020). Will the locals benefit?: The effect of wind power investments on rural wages.
Energy Policy, 142, 111489.
i
v
Mills, S. (2018). Wind energy and rural community sustainability. In Handbook of Sustainability and
Social Science Research (pp. 215-225). Springer, Cham.
e
Munday, M., Bristow, G., & Cowell, R. (2011). Wind farms in rural areas: How far do community
benefits from wind farms represent a local economic develorpment opportunity?. Journal of Rural
Studies, 27(1), 1-12.
r
Sampson, G. S., Perry, E. D., & Tayler, M. R. (2020). The On-Farm and Near-Farm Effects of Wind
Turbines on Agricultural Land Values. Journal oef Agricultural and Resource Economics, 45(3), 410-
427.
e
Shoeib, E. A. H., Infield, E. H., & Renski, H. C. (2021). Measuring the impacts of wind energy projects
on US rural counties’ community services and cost of living. Energy Policy, 153, 112279.
p
Slattery, M. C., Lantz, E., & Johnson, B. L. (2011). State and local economic impacts from wind energy
projects: Texas case study. Energy Policy, 39(12), 7930-7940.
t
Sun, L., & Abraham, S. (2020). Estimating dynamic treatment effects in event studies with heterogeneous
treatment effects. Journal oof Econometrics.
n
t
n
i
r
p
e
r
P
20
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4030617

d
Figure 1: Changes in Installed Wind Energy Capacity over Time
e
Installed Capacity in 1995
w
e
i
v
e
r
r
Figure 1B: Installed Capacity in 2019
e
e
p
t
o
n
t
n
i
r
p
e
r
P
21
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4030617

d
Figure 2: Event Studies on Main Outcomes
e
w
e
i
v
2A: Log of GDP per Capita 2B: Log of Per Capita Income 2C: Log of Median Household
eIncome
r
r
e
e
2D: Log of Median Home Value 2E: Log of Total Employment 2F: Share of Employment in
p Construction Sector
t
o
n
t
2G: Share of Employment in the 2H: Share of Employment in the 2I: Total Population
n
Manufacturing Sector Farm Sector
i
r
p
e
r
P
22
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4030617

d
Figure 3: Impact of Wind Energy Installation on Outcomes of Interest at Various Percentiles of the
e
Distribution of Installed Capacity Per Capita
w
e
i
v
e
r
r
3A: Log of GDP per Capita 3B: Log of Median Household Income
e
e
p
t
o
n
3C: Log of Median Home Values 3D: Log of Employment
t
n
i
r
p
e
r
3E: Share of Employment in the Manufacturing 3F: Share of Employment in Construction Sector
P Sector
23
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4030617

d
e
Figure 4: Event Study Graphs Comparing Urban and Rural Counties
w
e
i
v
e
r
r
4A: Log of GDP per Capita 4B: Log of Median Household Income
e
e
p
t
o
n
4C: Log of Median Home Values 4D: Share of Employment in the Manufacturing
Sector
t
n
i
r
p
e
r
P4E: Share of Employment in Construction Sector 4F: Total Population
24
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4030617

Figure 5: Distribution of Installed Wind Energy Capacity Per-Capita among Rural and More Urban
Counties
Mean - Urban Sample
Mean - Rural Sample
25
ytisneD
005
004
003
002
001
0
d
e
w
Distribution of Energy per Capita (MW Capacity < 0.06 MW / Capita)
e
i
v
e
r
r
e
e
0 .01 .02 .03 .04 .05
Installed Capacity (MW / Capita)
p
Rural Sample Urban Sample
Means for the Urban sample is 0.001 69 MW / Capita and for Rural Sample is 0.0253 MW / Capita
t
o
n
t
n
i
r
p
e
r
P
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4030617

d
e
| Table 1: Descriptive Statistics |     |     |     |     |     | w   |     |
| ------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|                                 |     | (1) | (2) | (3) | (4) | (5) | (6) |
e
|     |     |     | Counties  | Counties  |     | Rural  | Rural Sample  |
| --- | --- | --- | --------- | --------- | --- | ------ | ------------- |
Rural
|     |     | Full Sample | with  | without  |     | Counties with  | without  |
| --- | --- | ----------- | ----- | -------- | --- | -------------- | -------- |
Countiies
|     |     |     | Turbines | Turbines |     | Turbines | Turbines |
| --- | --- | --- | -------- | -------- | --- | -------- | -------- |
v
Socio-Economic Covariates
e
Population (1990) 131,125 107,396 135,462 21,680 18,383 22,413
r
| Share Non-White (1990) |     | 0.14 | 0.10 | 0.1 5 | 0.13 | 0.08 | 0.14 |
| ---------------------- | --- | ---- | ---- | ----- | ---- | ---- | ---- |

| Share Homeowner (1990) |     | 0.72 | 0.71 | 0.72 | 0.74 | 0.74 | 0.74 |
| ---------------------- | --- | ---- | ---- | ---- | ---- | ---- | ---- |
r
| Share 65+ Population (1990) |     | 0.19 | 0.20 | 0.18 | 0.20 | 0.22 | 0.20 |
| --------------------------- | --- | ---- | ---- | ---- | ---- | ---- | ---- |
e
| Share BA or Higher (1990) |     | 0.14 | 0.14  | 0.14 | 0.11 | 0.12 | 0.11 |
| ------------------------- | --- | ---- | ----- | ---- | ---- | ---- | ---- |
| Poverty Rate (1990)       |     | 0.15 | e0.15 | 0.15 | 0.18 | 0.15 | 0.18 |
| Percent Urban (1990)      |     | 0.46 | 0.46  | 0.46 | 0.27 | 0.31 | 0.26 |
p
Outcomes

Per Capita Income (1990)  t$   27,694  $   26,820   $ 27,852   $ 24,847   $ 25,390   $ 24,726
Median Household Income (1990) o $   32,336   $   31,523   $ 32,481   $ 28,369   $ 29,442   $ 28,131
| GDP Per Capita (2000) |     | 38.58 | 39.77 | 38.38 | 36.18 | 40.03 | 35.15 |
| --------------------- | --- | ----- | ----- | ----- | ----- | ----- | ----- |
n
Log of Home Values (2001) 11.36 11.27 11.38 11.22 11.17 11.23
Total Employment (1990)   72,934 53,393 76,498 11,139 9,718 11,455
t
| Share Farm Employment (1990) |     | 0.07 | 0.10 | 0.06 | 0.11 | 0.15 | 0.10 |
| ---------------------------- | --- | ---- | ---- | ---- | ---- | ---- | ---- |
n
Share Manufacturing Employment (1990) 0.15 0.11 0.16 0.15 0.10 0.16
Share Construction Emploiyment (1990) 0.06 0.05 0.06 0.05 0.05 0.05
r
p
| N of Counties  | in Sample | 2,971 | 465 | 2,506 | 2,000 | 338 | 1,662 |
| -------------- | --------- | ----- | --- | ----- | ----- | --- | ----- |
e
r
P
26
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4030617

d
e
Table 2: Effect of Wind Energy on the Full Sample  w
| (1) |     | (2)  | (3) | (4) |     | (5) | (6) | (7) |
| --- | --- | ---- | --- | --- | --- | --- | --- | --- |
Treatment: Installed
|     | Treatment: Wind  |     | Treatment:  |     |     | e   |     |     |
| --- | ---------------- | --- | ----------- | --- | --- | --- | --- | --- |
Turbine Capacity Per-
| Treatment:  | Turbine Installed  |     | Installed  |                   |     |                                    |     |     |
| ----------- | ------------------ | --- | ---------- | ----------------- | --- | ---------------------------------- | --- | --- |
|             |                    |     |            | Capita (MW) with  |     | Effect by Capacity Per Capita (MW) |     |     |
i
| Wind     | with Construction  |     | Turbine   |                     |     |     |     |     |
| -------- | ------------------ | --- | --------- | ------------------- | --- | --- | --- | --- |
|          |                    |     |           | Construction Phase  | v   |     |     |     |
| Turbine  | Phase Indicator    |     | Capacity  |                     |     |     |     |     |
Indicator
| Installed |               |            | Per-Capita  |                        |        |      |           |           |
| --------- | ------------- | ---------- | ----------- | ---------------------- | ------ | ---- | --------- | --------- |
|           | Construction  | Operating  |             | ConstructioeOperating  |        |      |           |           |
|           |               |            | (MW)        |                        |        | Mean | 50th pctl | 75th Pctl |
|           | Phase         | Phase      |             | n Phase                | Phase  |      |           |           |
r
Non-Employment Outcomes

Log of GDP Per Capita1 0.065*** 0.023* 0.071*** 5.068*** 3.106* 5.618*** 0.085*** 0.018*** 0.072***
r
(0.012) (0.012) (0.014) (0.929) (1.719) (1.100) (0.016) (0.003) (0.013)
e
Log of Income Per Capita1
0.049*** 0.030*** 0.054*** 3.586*** 3.912*** 3.993*** 0.060*** 0.013*** 0.051***
(0.006) (0.006) (0.007e) (0.540) (0.867) (0.596) (0.009) (0.002) (0.008)
Log of Median Household Income 0.033*** 0.018*** 0.036*** 2.412*** 2.352*** 2.657*** 0.041*** 0.009*** 0.034***
p
(0.004) (0.004) (0.005) (0.363) (0.604) (0.403) (0.006) (0.001) (0.005)
Log of Home Values 0.026*** 0.012 0.028*** 4.229*** 3.905 4.615*** 0.071*** 0.015*** 0.060***
(0.009) (0.t009) (0.009) (1.459) (2.743) (1.634) (0.024) (0.005) (0.021)
o
Total Population -4,333** -1,065 -4,503** -318,055** -139,864 -332,600** -5352** -1122.48** -4499**
(1,695) n (1,223) (1,860) (131,248) (162,321) (145,181) (2209) (463) (1857)
Employment Outcomes
Log of Total Employment per Capita1
|  -0.000 | 0.006 | 0.001 | -0.013 | 0.776 | 0.068 | 0.000 | -0.000 | -0.000 |
| ------- | ----- | ----- | ------ | ----- | ----- | ----- | ------ | ------ |
t(0.006) (0.007) (0.007) (0.459) (0.907) (0.523) (0.007) (0.002) (0.006)
n
Share Farm Employment -0.002** -0.002** -0.003** -0.177** -0.261** -0.204*** -0.003** -0.001** -0.003**
(0.001) (0.001) (0.001) (0.070) (0.114) (0.078) (0.001) (0.000) (0.001)
i
Share Manufacturing Ermployment
0.013*** 0.013*** 0.016*** 0.988*** 1.692*** 1.164*** 0.016*** 0.003 0.014***
p (0.002) (0.002) (0.002) (0.158) (0.260) (0.179) (0.003) (0.001) (0.002)
Share Construction Employment 0.007*** 0.003*** 0.007*** 0.487*** 0.361*** 0.525*** 0.008*** 0.002*** 0.007***
e
(0.001) (0.001) (0.001) (0.077) (0.129) (0.083) (0.001) (0.000) (0.001)
Nortes: *** p<0.01, ** p<0.05, * p<0.1. Robust standard errors clustered at county-level. All models are estimated using two-stage least squared with wind speed as the
instrumental variable with cohort-year and cohort-county fixed effects. (1) Denominator is 1995 population. Average installed capacity is 0.016 MW/Capita, which is larger
P
than both the median installed capacity (0.003MW / capita) and 75th percentile (0.014 MW / capita). In Columns 3 and 4, the coefficients should be scaled by the average
installed capacity.
27
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4030617

d
e
Table 3: Separate Effects of Wind Energy in Rural and More Urban Counties  w
e
|     |     | (1)                                | (2)          | (3)       |                                     |           |           |
| --- | --- | ---------------------------------- | ------------ | --------- | ----------------------------------- | --------- | --------- |
|     |     |                                    |              |           | (4)                                 | (5)       | (6)       |
|     |     |                                    | Rural Sample |           | iUrban Sample                       |           |           |
|     |     | Effect by Capacity Per Capita (MW) |              |           | vEffect by Capacity Per Capita (MW) |           |           |
|     |     | Mean                               | 50th pctl    | 75th Pctl | Mean                                | 50th pctl | 75th Pctl |
e
Installed Capacity (MW / Capita) 0.0253 0.0085 0.0230 0.0017 0.0006 0.0023
r
| Non-Employment Outcomes |     |          |           |           |         |         |         |
| ----------------------- | --- | -------- | --------- | --------- | ------- | ------- | ------- |
|                         |     | 0.087*** | 0.028***  | r0.080*** |         |         |         |
| Log of GDP Per Capita   |     |          |           |           | 0.028*  | 0.010*  | 0.038*  |
|                         |     | 0.019)   | (0.006) e | (0.018)   | (0.016) | (0.006) | (0.022) |
Log of Income Per Capita 0.053*** 0.017*** 0.048*** 0.025*** 0.009*** 0.034***
e
|     |     | (0.011) | (0.003) | (0.010) | (0.008) | (0.003) | (0.010) |
| --- | --- | ------- | ------- | ------- | ------- | ------- | ------- |
Log of Median Household Income 0.035***p0.011*** 0.032*** 0.021*** 0.008*** 0.029***
|     |     | (0.006) | (0.002) | (0.006) | (0.007) | (0.003) | (0.009) |
| --- | --- | ------- | ------- | ------- | ------- | ------- | ------- |

| Log of Home Values |     | 0.047** | 0.015** | 0.043** | 0.019 | 0.007 | 0.025 |
| ------------------ | --- | ------- | ------- | ------- | ----- | ----- | ----- |
t
|     |     | 0.023) | (0.007) | (0.020) | (0.015) | (0.005) | (0.020) |
| --- | --- | ------ | ------- | ------- | ------- | ------- | ------- |
o
| Total Population |     | -309 | -100 | -284 | -8,802** | 3,265** | 11,977** |
| ---------------- | --- | ---- | ---- | ---- | -------- | ------- | -------- |
n(368)
|     |     |     | (118) | (338) | (1,610) | (1,609) | (5,904) |
| --- | --- | --- | ----- | ----- | ------- | ------- | ------- |
Employment Outcomes

Log of Total Employment per Capita t 0.009 0.003 0.008 -0.005 -0.002 -0.006
|     |     | (0.008) | (0.003) | (0.016) | (0.010) | (0.004) | (0.013) |
| --- | --- | ------- | ------- | ------- | ------- | ------- | ------- |
n
Share Farm Employment -0.003** -0.001** -0.003** 0.000 0.000 0.000
|     | i   | (0.02) | (0.000) | (0.002) | (0.000) | (0.000) | (0.000) |
| --- | --- | ------ | ------- | ------- | ------- | ------- | ------- |
r
Share Manufactpuring Employment 0.015*** 0.005*** 0.013*** 0.007*** 0.003*** 0.010***
|     |     | (0.003) | (0.001) | (0.003) | (0.002) | (0.001) | (0.003) |
| --- | --- | ------- | ------- | ------- | ------- | ------- | ------- |
e
Share Construction Employment 0.008*** 0.002*** 0.007*** 0.005*** 0.002*** 0.007***
|     |     | (0.002) | (0.000) | (0.001) | (0.001) | (0.000) | (0.001) |
| --- | --- | ------- | ------- | ------- | ------- | ------- | ------- |
r
PNotes: *** p<0.01, ** p<0.05, * p<0.1. Robust standard errors clustered at county-level. All models are estimated using two-stage least squared with wind speed
as the instrumental variable with cohort-year and cohort-county fixed effects. (1) Denominator is 1995 population.
28
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4030617

d
Commercial Wind Energy Installations and Local Economic Development:
e
Evidence from U.S. Counties
w
Eric Brunner
University of Connecticut
e
David J. Schwegman
American University
i
v
e
December 2021
r
r
Absetract
We examine the causal impact of wind energy installation on the local economies of counties in the
e
United States. Using data on the universe of commercial wind energy installations from 1995-2018 and a
difference-in-differences instrumental variable identification strategy, we find that wind energy
installation led to economically meaningfupl and statistically significant increases in county GDP per-
capita, income per-capita, median household income, and median home values. We also find evidence
that while wind energy installation has little effect on total employment, the composition of local
employment shifts away from farm towards non-farm employment, notably leading to an increase in
t
construction and manufacturing employment. Finally, we show that the impact of wind energy installation
on local economic developmento varies significantly by installed capacity and by county urban/rural status.
n
t
n
i
r
p
e
r
P
1
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4030617

d
e
w
e
i
v
e
r
r
e
e
p
t
o
n
t
n
i
r
p
e
r
P
2
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=4030617
