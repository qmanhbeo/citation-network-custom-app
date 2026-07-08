EnergyPolicy175(2023)113467
Contents lists available at ScienceDirect
Energy Policy
journal homepage: www.elsevier.com/locate/enpol
Delays in the construction of power plants from electricity auctions
in Brazil
Bruno Andrade Diniza,b, Alexandre Szklob, Maurício T. Tolmasquimb,*, Roberto Schaefferb
aBrazilian National Bank for Economic and Social Development (BNDES), 20031-917, Rio de Janeiro, RJ, Brazil
bEnergy Planning Program, COPPE, Universidade Federal do Rio de Janeiro, 21941-914, Rio de Janeiro, RJ, Brazil
A R T I C L E I N F O A B S T R A C T
Keywords: Brazil has a long-running experience with auctions as an instrument to procure electricity both from renewable
Construction times and non-renewable sources. We build a database containing project-level information from auction rounds held
Delays in Brazil during the 2005–2017 period and employ multiple regression analyses to investigate the integrated
Auction design
effect of auction design elements, individual bids and project features on construction delays. We find that the
Energy auctions
schedule performance of wind power projects has been strongly improved with the introduction of a preliminary
Brazil
transmission capacity phase in auctions and when the risk of delays in the extension of the transmission grid was
transferred to project developers. Projects contracted in auctions with longer lead times took more time to be
completed but faced lower risk of project delays and penalties. Large scale plants were more prone to delays,
while no significant difference was found between projects awarded in technology-specific or multi-technology
auctions. Lower individual bids were not associated with longer delays, suggesting that apparently the Brazilian
hybrid auction system was able to minimize the winner’s curse. Our results add empirical evidence to the
literature and may provide policy makers with new insights on how to design auctions to promote the expansion
of renewable electricity supply.
1. Introduction to falling remuneration levels and, consequently, ensure fair and cost-
reflective tariffs. In addition, auctions offer more control over the
Auctions have become the main instrument to support electricity expansion of electricity generation by specifying the desired capacity to
generation from renewable energy sources (RES) worldwide (del Río be contracted and its implementation deadline (del Río and Linares,
and Kiefer, 2021). According to IRENA (2019), 106 countries had 2014).
adopted auction schemes to procure renewable-based electricity by the Nevertheless, auctions are not able to overcome competitive market
end of 2018 compared to only 8 by the end of 2005. structure problems or mitigate all risks associated with the imple-
Brazil is one of the pioneers in the use of energy auctions to support mentation of infrastructure projects (Tolmasquim et al., 2021). One of
the expansion of its electric power system. The Brazilian government such risks is that projects might not be completed according to the
structured its current auction programme in 2004 with the objectives of estimated schedule. The delay of output caused by slippage in con-
achieving energy security, improving the efficiency of electricity con- struction projects schedule imposes economic costs when the power
tracting for the regulated market, and promoting diversification of en- system is short of capacity or supplying power from plants with high
ergy supply, especially for renewable energy sources (Tolmasquim et al., variable costs (Bacon et al., 1996). Renewable energy project delays and
2021). Since then, auctions have been the primary mechanism to pro- cancellations may lead to higher CO2 emissions of the respective elec-
cure electricity and capacity with a long-term focus. Thus, Brazil has one tricity market and to a reduced public acceptance of renewable energy
of the longest-running auction programmes in the world and it might (Bayer et al., 2018). Delays may also cause financial impacts on in-
offer important lessons on RES auction design and implementation vestors by increasing their financing charges and incurring on project
(Pahle et al., 2021). loan repayments before revenues are generated (Bacon et al., 1996).
Auctions have the advantage that the remuneration level of gener- Carvalho et al. (2020) studied the financial risk associated with the
ators is determined by a competitive procurement process that may lead anticipation or delay in the completion of solar and wind projects in the
* Corresponding author.
E-mail address: tolmasquim@ppe.ufrj.br (M.T. Tolmasquim).
https://doi.org/10.1016/j.enpol.2023.113467
Received 13 May 2022; Received in revised form 1 December 2022; Accepted 26 January 2023
Availableonline11February2023
0301-4215/©2023ElsevierLtd.Allrightsreserved.

B.A. Diniz et al. E n e r g y P o l i c y 175(2023)113467
Brazilian energy market, finding that delays significantly increase the database assembled by the authors gathering information published by
probability of a failed business. regulators and energy market operators, we measure the incurred delays
Thus, ensuring that power plants are built according to the and perform statistical analyses seeking to identify possible correlations
contractual schedule is a legitimate concern for policy makers, reflected between observed delays and characteristics of projects (technology,
in several publications addressing mechanisms aimed at avoiding scale, individual bids) and auction design elements (e.g., lead time and
implementation delays in energy generation projects (del Río, 2017; penalties).
Held et al., 2014; IRENA and CEM, 2015; Kreiss et al., 2017). Auction Our work is structured as follows: in the next section we provide an
realization rates (i.e., the share of contracted capacity actually being overview of the Brazilian auction scheme, focusing on the main auction
commissioned) have been used in the literature as a proxy to quantify design elements adopted and on regulatory changes that have been
the effectiveness of RES auctions and investigate the effect of different implemented to deal with low realization rates. We also discuss the
auction design elements (Bayer et al., 2018; del Río and Linares, 2014; literature on project delays and RES auction design to identify elements
Mattha¨us, 2020; Shrimali et al., 2016; Winkler et al., 2018). assumed to be important for an empirical analysis on project delays.
According to Quintana-Rojo et al. (2020), the effectiveness and ef- Section 3 details the methodology adopted, describing the database
ficiency of auction mechanisms is a topic that requires a greater load of used, the definitions and analyses employed. In section 4 results are
econometric studies. Recent work has been published in the field presented and their implications for renewable energy auctions planning
(Anatolitis et al., 2022; Mattha¨us, 2020), but studies are typically are discussed. Finally, the last section brings the main conclusions and
limited to auction-level aggregated data (e.g., total deployed capacity, policy recommendations.
average bidding prices), and information regarding projects’ construc-
tion status after auction deadlines is scarce. For example, the compre- 2. Background: literature review and electricity auctions in
hensive online database developed by the European Union AURES1 II Brazil
Project gathers structured data about 820 auction rounds held in EU
countries, but realization rates are available for only 6% of those An increasing number of countries uses auctions as an instrument to
(AURES II, 2022). This lack of structured project-level data prevents the allocate support for renewable energies (IRENA, 2019). When designing
assessment of other interesting dynamics related to the effective their support schemes, policy makers must decide on several aspects that
deployment of projects, such as the effects of individual bidding prices, may impact cost-efficiency, social acceptability, level of competition,
geographical location, technology and scale. technology diversity, transaction costs, among others. The success of
Recently, few articles have employed econometric techniques on auctions in meeting policy objectives depends on the choice of design
project-level data to assess the effects of RES auction design features. elements in specific settings, i.e. the devil is in the details (del Río et al.,
Probst et al. (2020) econometrically analyzed data on solar PV projects 2015).
from auctions held in India between 2014 and 2017 to evaluate the ef- The main objectives for policymakers in auction design are effi-
fect of local content requirements (LCR) on average bid prices and ciency, in the sense of minimizing support level through low awarded
project completion rates. They found that the LCR component has auction prices (Anatolitis et al., 2022), and effectiveness, i.e., achieving
increased awarded prices significantly but had no effect on the realiza- high realization rates of awarded projects (Mattha¨us, 2020). In this
tion rates of the projects. Based on data from onshore wind auctions paper, we focus on the latter, as the risk of delays and underbuilding of
conducted in Italy from 2012 to 2016, Cassetta et al. (2017) used a the auctioned projects have been a recurring concern (Azuela Elizondo
multiple linear model for an empirical analysis of project-related, et al., 2014; Bayer, 2018; del Río and Linares, 2014; Kreiss et al., 2017).
firm-specific and auction design determinants of awarded base tariff.
Nevertheless, the authors point out the difficulty of making a similar
2.1. Electricity auctions in Brazil
assessment on project delays and cancellation due to the lack of
consistent data on the stages of construction of single awarded projects.
Batz Lin˜eiro and Müsgens (2021) assessed project-specific, dis- The Brazilian auction system was created in 2004 with the objective
of providing an efficient, transparent, and competitive instrument for
aggregated individual bid data from the solar PV auction program in
the awarding of long-term PPAs for distribution companies, while
Germany. They employed regression analysis to explore the impact of
reducing investor risks and facilitating project financing of new power
project and developer characteristics, competition, and PV module pri-
plants. The auction system takes place in the context of the regulated
ces on bid values and project realization.
market,2 in which was traded about 64% of all electricity consumed in
In the Brazilian context, monthly reports on the expansion of elec-
the country in January 2022 (CCEE, 2021a). These auctions are coor-
tricity generation supply published by the Brazilian Power Regulatory
dinated by the Ministry of Mines and Energy (MME) and performed by
Agency (ANEEL, 2021) contain data and statistics concerning project
ANEEL and the Brazilian Power Trade Chamber (CCEE). In Brazil
delays, but these are restricted to the execution of projects under con-
existing and new energies compete in separated processes, which allows
struction. Based on expert interviews and extensive data analysis, Bayer
the average price in the regulated market to be calculated apart from the
et al. (2018) investigated the causes for delays in on-shore wind power
marginal expansion cost, thus contributing to fair electricity rates
plants from Brazilian auctions and discussed potential mitigation mea-
(Tolmasquim et al., 2021). There are three types of electricity auctions
sures. We argue that a comprehensive assessment of the Brazilian
related to the construction of greenfield projects:
experience with electricity auctions, from both renewable and
New Energy Auction (LEN): Auction designed to contract electricity
non-renewable sources, with the employment of econometric tech-
from greenfield projects, with the aim of meeting the increase in dis-
niques, might bring new quantitative insights on how design elements
tribution companies’ power demand, according to estimates provided by
and individual project characteristics influence implementation sched-
each of them prior to the auction round. These auctions can be held from
ules and auction effectiveness. Such analysis has the potential to bring
important lessons regarding the future designs and planning of renew-
able energy auctions both in Brazil and elsewhere.
2 In the Free Contracting Market (FCM), non-regulated agents, such as free
Therefore, the aim of this paper is to assess the implementation
consumers and energy traders, can directly negotiate bilateral contracts,
schedule performance of electricity generation projects contracted in
whereby prices and contract terms are freely agreed on by the parties. However,
auctions held in Brazil in the period between 2005 and 2017. Using a
purchase of electricity in the free market is exclusive for those end-users with
installed load capacity equal or greater than 500 kW (ANEEL, 2021). Captive
consumers are only allowed to buy electricity from the distributor in whose
1 (AUctions for Renewable Energy Support II). network they are connected, paying regulated rates.
2

B.A. Diniz et al. E n e r g y P o l i c y 175(2023)113467
three to six years before the starting delivery date. Power generation Table 1
projects compete in the auction and each winner signs contracts with Brazilian auction scheme basic design elements
several distribution companies according to their expected increase in Source: Own elaboration based on (Bayer et al., 2018; Tolmasquim et al., 2021).
demand. Some generation projects, such as the Madeira River hydro- Metrics for volume setting The contracted volume is set in terms of generation
electric plants and the Belo Monte Hydroelectric Power Plant, because of and disclosure (MWh)
their strategic nature and relevant public interest, are auctioned through Timing (schedule) There is no fixed schedule of auctions, but these are
a project-specific new energy auction called Structuring Project Auc- organized on a regular basis – usually 2 rounds per
tions (LPE). year.
Reserve Energy Auction (LER): Auctions created to increase security Technological Diversity Technology-specific (TS) or multi-technology (MT)
auctions.
in the electricity supply in the National Interconnected System by pur-
Geographical Diversity Geographically neutral - no requirement to deploy
chasing power from plants specially contracted for this purpose. Since the project in a given location (except for project-
renewable sources, mostly contracted in these auctions, are non- specific auctions).
controllable sources and have inflexible dispatch, the concept of Pricing rule(a) Hybrid model in two phases:
1 - Descending-clock auction with uniform price,
reserve energy is here interpreted as additional energy to the system that
starting with a ceiling price defined by regulators.
aims to reduce the depletion of hydroelectric power plant reservoirs Bidders indicate how much they are willing to
(Tolmasquim et al., 2021). CCEE act as a single buyer and sign contracts supply at this price. The auctioneer then lowers the
with all the winners of the auction. As the reserve auction works as an price until the desired supply level is met, plus a
insurance for the entire power system, the energy charges apply to all certain margin, to stimulate competition in the
second phase.
consumers from both the regulated and the free market.
2 Final pay-as-bid round for the winners of first
Renewable energy auction (LFA): Auction designed to increase the phase. The lowest (sealed) bids are awarded PPAs
share of renewable energy sources - which includes wind, solar, and at the price of their bid
small hydropower plants - in the Brazilian energy system. Despite the Winner selection criteria Price-only
Remuneration Full payment through long-term PPAs, signed with
creation of a specific auction modality, so far only three rounds of LFA
either CCEE (Reserve auctions) or a pool of
have taken place (in 2007, 2010 and 2015), and most RES capacity was
distribution companies
procured through LEN and LER. Lead time From 2 to 6 years
Table 1 summarizes the main elements in the design of the Brazilian Pre-qualifications
auction scheme, classified according to the categories described in Physical Bidders must secure social and environmental
permits, land use rights and interconnection
literature (del Río and Kiefer, 2021; IRENA and CEM, 2015). A more
agreements to be allowed to register for bidding.
detailed description of Brazilian auctions regulatory and policy frame- Financial - Bid bond (1% of total estimated investment costs)
work is beyond the scope of this paper and can be found elsewhere in before joining the bidding stage
literature (Correia et al., 2020; Tolmasquim et al., 2021). - Winners must provide completion bonds (5% of
estimated investment) before contract signing
Some design elements and contract obligations vary across distinct
- Project developer financial health (General
auction types and products, and some regulatory changes have been
liquidity indicator threshold to participate).
implemented over the years. The adoption of different design elements Penalties In case of delays, project developers are subject to
for each auction round considered in this study is shown in Table A1. In administrative fines, obligation to reimburse energy
the next paragraphs, we discuss how some of those variations in auction costs, termination of contract, or exclusion from
future auctions.
design and individual project features might have affected imple-
Risks
mentation delays and formulate predictions to be empirically tested in Seller Construction, operation, equipment performance
our study. risks and exposure to the spot market (in the case of
‘quantity contract’ modality(b))
Buyer Inflation and exposure to the spot market, in the case
2.2. Penalties and exposure to spot market prices
of the ‘availability contract’ modality
In case of non-realization or delay, penalties include obligation to a From 2017 onwards, the bidding process changed to a continuous trade
reverse auction in two phases. In the first one, ‘temporary winners’ are selected
reimburse the energy that was not delivered, execution of financial
through sealed bids with a price and quantity. The second phase consists of
guarantees, and further sanctions, such as termination of the contract
descending clock iterations in which any temporarily disqualified bidder can
with contractual fees, a ban from auctions, or administrative fines up to
replace a temporary winner by submitting a bid lower than the marginal price
10% of the respective investment. The legal consequences of each in-
minus a decrement defined by the auctioneer.
dividual case are defined by the regulatory authorities, who can make an b The PPAs awarded to auction winners may be of two types: quantity and
ex-post decision on which administrative measure is the most suitable in availability contracts. In the quantity modality, the seller is responsible for
order to improve the implementation process (Bayer et al., 2018). The delivering the contracted amount of electricity, assuming the operating costs
specific reimbursement obligation in case of delays depends on the and the risks of variations in energy generation and short-term market prices. In
auction type. For projects awarded in Reserve Energy Auctions (LER), a the availability contracts, generators receive a fixed revenue for offering their
charge on the non-supplied electricity is applied based on project bid plant’s available capacity, while buyers bear variable costs (fuel) and generation
price, while in other auction types project developers must purchase the imbalance settlement costs/revenues.
missing quantity on the electricity market, bearing the risk of market
price volatility if the market price exceeds the contractual remuneration. separate tenders, which can be either technology-specific or multi-
According to (Bayer et al., 2018), the obligation to bear market price technology (i.e., where different technologies compete directly). The
risks creates an even stronger financial incentive for on-time imple- question of technological banding in auctions is a much debated topic
mentation, since spot market prices have been historically higher than (Lena Kitzing et al., 2019; Lucas et al., 2020). While multi-technology
the auction price, especially in dry seasons. Following these arguments, auctions have the potential to maximize cost-efficiency (Kreiss et al.,
we test the prediction that projects awarded in LER auctions are subject 2021), technology-specific designs may stimulate technological learning
to longer delays. and avoid crowding out of less mature technologies (Lena Kitzing et al.,
2019). Also, technological banding allow support levels and auction
2.3. Technological banding rules to be adjusted according to market conditions and technology
maturity (Polzin et al., 2015), which may potentially increase realiza-
Each auction round includes one or more products, auctioned in tion rates. However (Mattha¨us, 2020), analyzed RES auction rounds
3

B.A. Diniz et al. E n e r g y P o l i c y 175(2023)113467
worldwide and found no empirical evidence that technological banding remuneration if the project developer could prove that their plant was
affect effectiveness. In this study, we test whether, in the Brazilian ready to operate, while buyers had to arrange alternative procurement
context, projects awarded in technology-specific auctions are less prone options. Since 2013, such waiver has been removed, and the risk of the
to delays. unavailability of transmission capacity has been fully transferred to
generation project developers, who became obligated to fulfill their
2.4. Lead time contractual obligation to supply electricity even in case of delays in the
extension of the transmission grid.
According to IRENA and CEM (2015), lead time is a key attribute of Another regulatory change implemented for dealing with this prob-
electricity commercialization auctions, being typically defined based on lem was the introduction, for certain electricity auctions with shorter
expectations regarding the time required for the construction of projects lead times, of a preliminary phase to select the projects with connection
and execution of the administrative procedures related to them. If the feasibility through competition among projects with the same connec-
lead time is shorter than necessary, entrepreneurs have little margin for tion point. In this preliminary phase, bidders submit a single bid with
error, resulting in a higher risk of delays that can result in penalties. price and quantity for each project, and bids are classified by their price
However, auctions held too far in advance can lead to a certain degree of at each connection point. Projects that exceed the ‘transmission
speculation, attracting, for example, investors who plan to delay the margin’4 are excluded from the auction, and winners then engage in the
start of construction in anticipation of possible reductions in develop- general auction process (Tolmasquim et al., 2021).
ment costs. Sovacool et al. (2014) consider that longer construction Bayer et al. (2018) observed a reduction trend on wind power project
lead-times deal with several uncertainties during the construction pro- delays due to transmission grid issues after the implementation of both
cess, including unforeseen changes in interest rates, availability of ma- auction design amendments. Based on this evidence, and including
terials, exchange rates, severe weather and labor strikes, making outcomes from recent auction rounds, we empirically test whether each
planning and financing difficult. of those regulatory changes effectively reduced project delays.
In the Brazilian case, investors have the option to sell in the free
market whatever energy is generated before the auctioned PPA’s supply 2.6. Pricing rule, underbidding, and underbuilding
period, which might create an incentive to anticipate the commercial
operation of projects contracted in auctions with longer lead times. As described in Table 1 - Brazilian auction scheme basic design ele-
However, this is not a straightforward decision for investors, depending ments, the regular Brazilian auction procedure is a hybrid model that
on several factors including bidding prices, market conditions and ex- occurs in two phases: a first descending clock phase with uniform
pectations. Dalbem et al. (2014) modeled bidders’ price decision in pricing, followed by a pay-as-bid final round in which the lowest
Brazilian A-53 wind auctions as real options and concluded that given (sealed) bids are awarded PPAs at the price of their bid. The auctioneer
low bid prices, winners might be tempted to defer the start of con- may expect lower prices under a pay-as-bid sealed auction, but the
struction, expecting more favorable equipment and energy prices, trade-off might be a higher risk of the winner’s curse in this scenario
though evidence from European RES auctions (Anatolitis et al., 2022) (Tolmasquim et al., 2021). Haufe et al. (2018) points out the risk of ir-
suggests that this behavior might be inhibited when prequalification rational underbidding under pay-as-bid models: bidders may tend to bid
criteria and penalties are in place. lower than their costs, leading to project delays and cancellations. On
Based on this debate, we test the hypothesis that longer auction lead the other hand (Mattha¨us, 2020), found no empirical evidence that the
times increase the on-time implementation of awarded projects. pricing rule affect effectiveness. Based on this debate, we formulate the
hypothesis that, among projects awarded in an auction round, individ-
2.5. Transmission related delays ual projects with lower bid prices are more prone to delays.
In Brazil, transmission was traditionally planned, auctioned and built 2.7. Project technology and scale
after generation auction winners were revealed and their location and
nature were defined. However, in practice, delays in the implementation There is a panoply of studies assessing the magnitude and frequency
schedule of transmission facilities, related to environmental constraints of delays and showing it is a pervasive issue in infrastructure projects
or underbidding in transmission auctions, have resulted in many cases in worldwide. Sovacool et al. (2014) assessed construction costs and
which generation facilities are ready to operate by the time their schedule affiliated with 401 power infrastructure projects worldwide,
contractual delivery date is achieved, but the output of renewable finding that electricity infrastructure is prone to delays and cost overrun
generators cannot reach the market because transmission capacity re- issues almost independently of technology or location, though wind,
inforcements are not ready in time (IRENA and CEM, 2015). solar and small thermoelectric power plants showed significantly lower
Herrera et al. (2019) point to the transmission capacity deficit as the risks of cost overruns and construction delays in comparison to nuclear
main bottleneck to the expansion of generation in the Northeast Region, (Portugal-Pereira et al., 2018) and large hydropower plants. Bacon and
which concentrates most of the Brazilian potential for wind and solar Besant-Jones (1998) show that large projects have larger cost and time
sources. Indeed, a significant part of the delays incurred in the genera- overruns even in proportion to their size. Callegari et al. (2018) sug-
tion projects located in this region did not result from situations related gested that solar and wind sources present a delivery time shorter than
to the implementation of these projects themselves, but from delays in initially estimated due to their rapid learning curves. Other studies for
the associated transmission projects. This problem is not unique to Brazil have arrived at similar results (Ko¨berle et al., 2018). However,
Brazil: delayed connection to the grid has been identified as one of the studies addressing project delays in the first rounds of wind power
key factors accounting for the gap between the technical potential and auctions in Brazil have identified low rates of on-time implementation,
the actual output of Chinese wind farms (Huenteler et al., 2018; Lu et al., with many projects being delayed for more than one year (Azuela
2016; Zhang et al., 2013). Elizondo et al., 2014; Bayer, 2018).
In some of Brazil’s early auctions, such transmission risks were Biomass-powered thermoelectric plants are expected to face lower
allocated almost entirely to electricity buyers. The PPAs awarded as a delays in the recent Brazilian auctions, since many of those are actually
result of the auctions included a clause that exempted the project de-
velopers from their contractual obligations and guaranteed
4 Limiting draining capacity calculated by the Energy Research Company
(Empresa de Pesquisa Energ´etica, or EPE) and the Independent System Operator
3 Auctions for electricity with first delivery date 5 years after the auction. (ONS) for each connection point indicated by the registered projects.
4

B.A. Diniz et al. E n e r g y P o l i c y 175(2023)113467
brownfield processes associated to sugarcane mills, initially built to Regarding wind power and solar photovoltaic plants, due to tax in-
generate electricity to supply their own consumption and then retro- centives and regulatory issues,7 it is usual that larger generation com-
fitted to sell the surplus power. Moreover, sugarcane mills are usually plexes are virtually segmented into smaller adjacent farms. For this
near the load centers, thus implying reduction of transmission grid study, based on information extracted from ONS (2022), 660 projects
connection issues (Watanabe et al., 2020). were grouped into 130 complexes, each considered as a single project, as
In an attempt to address some of these questions in the context of the they usually share the same facilities, developers, licensing and con-
Brazilian auction program, we include in our analysis variables to ac- struction process. For projects that sold energy in more than one auction,
count for the effect of project scale (measured by installed capacity) and we considered only the first auction in which the project was awarded a
technology. contract. In the end, 523 observations remained in the full database,8
which comprises all bid winners, including projects that have been
3. Methodology and data officially cancelled or those with extremely large delays and low prob-
ability of realization.
3.1. Research design For the econometric analysis developed in this study, we restricted
the sample in 4 steps. First, we dropped 83 fossil-fuel thermal plants and
Initially, following the procedure described in the next subsection, kept just the most relevant sources in terms of number of projects and
we build a database containing information on several project, auction, installed capacity: Wind, Solar PV, Biomass and Hydropower (large and
bids, and PPA features. small) plants. Second, we excluded 50 officially cancelled projects.
We then employ a multiple regression technique to test the hy- Third, we removed 28 projects with extremely small implementation
potheses discussed in Section 2 on the influence of auction design ele- times (less than one year), which does not seem compatible with con-
ments, underbidding, project scale and technology on measured delays. struction times for the technologies. Finally, we filtered out 23 projects
This approach allows for inference on the integrated effect of several that have been either delayed or anticipated by more than 3 years from
variables on the observed delays, which might not be captured in a the auction deadline, which indicates high probability that the schedule
descriptive analysis of the database. If statistically significant5 correla- of such projects is related to specificities beyond the project features and
tions can be established, then quantitative knowledge about those ef- auction design elements under analysis. Thus, the final sample for sta-
fects might bring insights to the improvement of auction mechanisms. tistical analysis contains 339 projects, with 45 GW total installed ca-
pacity and that sold 3802 TWh in 34 auction rounds.
3.2. Database
3.2.1. Dependent variables
Our main dependent variable is project delay, defined as the differ-
The database used in this study (Diniz, 2022) was compiled gath-
ence between the auction completion deadline and the commercial
ering information published by the Brazilian Power Trade Chamber
operation date, which corresponds to the moment when the first
(CCEE), the Brazilian Electricity Regulatory Agency (ANEEL) and the
generating unit of the plant was connected to the power system. Delays
Independent System Operator (ONS). Basic information on project
are expressed in absolute terms (days), and negative values mean that
characteristics, commercial operation date, and main PPA features were
commercial operation started before the beginning of the contractual
obtained from the combination of two CCEE’s monthly updated publi-
electricity supply period. For power plants that did not start operation
cations: the “Consolidated Auction Results” (CCEE, 2021a) and the
by the end of 2021, delay is calculated as the time elapsed between
“Market Information Bulletin - Individual Project Data” (CCEE, 2021b).
auction deadline and the reference date of this study (Dec. 21). We
Additionally, we accessed auction notices and PPA drafts to verify,
choose delay as our main variable of study because it measures how
for each case, the auction design features employed, such as techno-
implementation schedules deviate from the targets agreed by the
logical banding (technology-specific or multi-technology products),
auctioneer and project developers, which may jeopardize projects
preliminary phase for project elimination by connection point and
feasibility and RES auction effectiveness. Alternatively, we also employ
allocation of transmission delays risks to project developers.
as dependent variable Realization_Time, which is defined as the time
The resulting database contains, for each project, information
elapsed between auction date and project commercial operation date.
regarding energy source, geographic location, installed capacity; date of
Table 2 summarizes our potential explanatory variables, chosen ac-
effective start of commercial operation, project status (in operation,
cording to the hypothesis and predictions discussed in Section 2, while
delayed or cancelled); auction type, date and relevant design features;
summary descriptive statistics of the final sample used in the analysis is
contract modality (quantity or availability); start and end date of the
presented in Table 3.
contracted supply period; bidding price and average energy traded per
year.
We focus on auction rounds related to the construction of new power 3.3. Model selection and implementation
plants6 and for which deadlines had been met by December 2021. We
collected information on 1068 generation projects that sold a total To quantify the integrated effect of potential explanatory variables in
amount of 6682 TWh in 37 auction rounds, held between 2005 and project delays, we estimate the following multi-variate model:
2017. The database comprises wind power plants, hydroelectric power Delay i ∼ β 0 +β 1 .Predictors i +β 2 .Controls i +ε i (3)
plants, small hydropower plants (<30 MW), photovoltaic solar plants
(solar PV), and thermal power plants fueled with natural gas, biomass, In this model, Predictors is a vector including the potential explana-
oil and coal. tory variables and some relevant interactions between them, while
Controls is a vector of control variables and covariates introduced in each
model. Auction_Year corresponds to a covariate representing the year
5 Unless otherwise stated, this paper adopts a general significance level of when the auction round took place to capture possible time-varying
0.05.
6 Auctions intended for contracting energy generated by plants already built
and in operation (Existing Energy Auctions and Adjustment Auctions) were not 7 Power plants from renewable energy sources with less than 30 MW of
included in the base. installed capacity were eligible for reduced tax rates and discounts on trans-
mission and distribution system fees.
8 The full database (Diniz, 2022) includes raw data and a version in which
projects are not grouped into complexes.
5

B.A. Diniz et al. E n e r g y P o l i c y 175(2023)113467
Table 2 assumptions for a usual Ordinary Least Square (OLS) regression have
Description of potential explanatory variables. been met, we concluded that there is heteroskedasticity in our data.
Variable Type Description Consequently, we follow Wooldridge (2018) and report
heteroskedasticity-robust standard errors and test statistics for OLS.
Technology_Specific(1) Dummy 1: awarded project did not compete
All computations were conducted in R version 4.2.1 (R Core Team,
directly with other technologies;
0: project awarded in a multi-technology 2022), and we used packages “performance” (Lüdecke et al., 2021) and
auction. “lmtest” (Zeileis and Hothorn, 2002) for calculations, tests and model
Lead_Time Continuous Period (in years) between auction date and diagnostics. Additionally, we used packages “stargazer” (Hlavac, 2022)
the start of supply period defined in the and “flextable” (Gohel and Skintzos, 2022) for creating tables, and
PPA.
Dev_Transmission_Risks Dummy 1: transmission grid connection risks are “ggplot2” (Wickham, 2016) for plots.
allocated to generation project developer;
0: risk of unavailability of transmission 4. Results and discussion
capacity is transferred to buyers.
Preliminary_Phase Dummy 1: project awarded in an auction with a
In this section, we test whether the predictions from literature dis-
preliminary phase to shortlist projects that
fit in the available transmission capacity; cussed in Section 2 hold for our empirical data. Table 4 summarizes the
0: project awarded in auction without results of our models.
transmission capacity phase. Our baseline model (Model 1) focuses on the potential explanatory
LER Dummy 1: project awarded in a Reserve Energy
variables described in Table 2. Given the historical prominence of grid
Auction type (LER), 0 otherwise.
Individual_Bid_Ratio Continuous Ratio between the individual project bid connection issues in wind power project delays in Brazil (Bayer et al.,
price and the auction round average price. 2018), we include interaction terms to account for the effect of regula-
Wind Dummy 1: on-shore wind power plant; 0 otherwise. tory changes intended to mitigate transmission-related delays (Dev_-
Biomass Dummy 1: biomass-powered thermoelectric plant;
Transmission_Risks and Preliminary_Phase) on on-shore wind projects. For
0 otherwise.
Solar_PV projects, we add only the interaction with Preliminary_Phase
Hydro Dummy 1: Hydropower plant (large or small);
0 otherwise. since Dev_Transmission_Risks equals one for every awarded Solar PV
Proj_Installed_Capacity Continuous Project installed capacity (in MW). project. In Model 2, we add the control variable Quantity_Contract to
(2)
account for potential effect of different PPA types (Quantity or Avail-
(1) Auctions with competition between large and small hydro, or between ability contract modalities). Furthermore, in Model 3 we add the Auc-
different thermal sources (e.g, gas, coal, biomass), are considered as multi- tion_Year covariate to account for continuous time-varying effects.
technology auctions. (2) Logarithmic transformation applied to normalize the Finally, in Model 4 we replicate all explanatory and control variables
residuals of the model, which would otherwise be positively skewed. from Model 3, but Realization_Time is adopted as the dependent variable.
The estimators in our full model are able to explain a fair portion of the
variation in project delays (Model 3, adjusted R2 of 0.25), and even more
Table 3 in Realization_Time (Model 4, adjusted R2 of 0.38).
Summary descriptive statistics of final sample.
The coefficient on Technology_Specific is insignificant in all models,
Mean St. Dev. Min Median Max which suggests that competing in specific or multi-technology auctions
Delay 70 416 (cid:0) 1092 59 1086 did not play a major role in steering the implementation schedule of
Realization_Time 1209 458 474 1152 2559 power plants. This result adds to the evidence from the worldwide RES
Lead_Time 3.120 0.967 1.353 2.970 4.704 auctions assessment performed by Matth¨aus (2020), who found no as-
Individual_Bid_Ratio 1.009 0.131 0.598 1.001 1.553
sociation of technological banding with the realization rate of auctions.
Proj_Installed_Capacity 133 667 0.56 45 11233
ln_Proj_Installed_Capacity 3.743 1.304 (cid:0) 0.580 3.807 9.327 Lead_Time has a significant positive effect on Realization_Time in
Dev_Transmission_Risks 0.593 0.492 0 1 1 Model 4, but the estimated coefficient (245 days for one additional year
Preliminary_Phase 0.124 0.330 0 0 1 in Lead_Time) suggests that the increase in project implementation pe-
Technology_Specific 0.522 0.500 0 1 1
riods is shorter than the auction lead time extension. Accordingly, the
Wind 0.327 0.470 0 0 1
effect of Lead_Time on the delays of awarded projects is significant and
Solar_PV 0.112 0.316 0 0 1
Biomass 0.183 0.387 0 0 1 negative on Models 1, 2 and 3. This is an expected result since with
Hydro 0.351 0.478 0 0 1 longer realization periods project developers are granted enough time to
Quantity_Contract 0.649 0.478 0 1 1 comply with necessary administrative requirements and complete the
Note: N =339 observations for all variables. power plants. Also, for generators whose grid access is conditioned to
grid expansion, longer deadlines may provide the time required to the
hidden effects, such as technological development, the learning curves execution of grid expansion activities (IRENA and CEM, 2015).
of renewable energies, and experience acquired by auctioneers and Although shorter periods might be desirable for auctioneers willing to
project developers. It is added as a continuous variable to avoid multi- meet electricity demand and RES expansion targets in the short term,
collinearity issues arising from splitting the study period into bins that literature suggests that the reduced risk of delays and penalties faced by
might be correlated with the introduction of some design elements project developers in auctions with longer lead times might lead to lower
under analysis. In order to account for possible effects of the two bid prices (del Río and Linares, 2014; Hochberg and Poudineh, 2018;
different PPA modalities described in Table 1, we include Quantity_- IRENA and CEM, 2015). Anatolitis et al. (2022) empirically found that,
Contract as a dummy control variable that indicates whether the PPA is a in European RES auctions, longer realization periods were associated
Quantity (=1) or Availability (=0) contract. with lower awarded prices, though this effect is reversed when long lead
We conducted several tests9 with fitted models to check for the as- times are adopted in combination with financial prequalification.
sumptions of normality of residuals, multi-collinearity and hetero- Similar analyses on the effect of lead time on bid prices and its in-
skedasticity that might bias the inference of our results. While other terrelations with other design features, both in Brazil and elsewhere,
may bring additional insights to policy makers designing RES auctions.
The coefficients on LER are insignificant in all models. In LER auc-
tions, penalties are calculated based on awarded PPA prices, while in
9 Shapiro-Wilk test for normality of residuals, Breush-Pagan test for hetero- other auction types project developers are exposed to market price
skedasticity and Variance Inflation Factor (VIF) for multicollinearity. volatility risks in case of delays. Apparently, adding this risk to the
6

B.A. Diniz et al. E n e r g y P o l i c y 175(2023)113467
Table 4
Regression results.
Delay Realization_Time
(1) (2) (3) (4)
Technology_Specific 65.42 (65.99) 63.32 (66.49) 142.08 (78.18) 142.08 (75.94)
Lead_Time (cid:0) 98.39*** (29.03) (cid:0) 95.97** (29.46) (cid:0) 119.77*** (28.78) 245.23*** (31.38)
LER (cid:0) 0.74 (61.20) 20.37 (82.50) (cid:0) 100.55 (107.07) (cid:0) 100.55 (100.05)
Individual_Bid_Ratio (cid:0) 10.02 (189.22) (cid:0) 7.43 (189.21) 34.31 (185.98) 34.31 (168.25)
Solar_PV 97.82 (92.02) 85.06 (99.06) 23.09 (101.82) 23.09 (114.69)
Wind 285.45*** (69.28) 263.62** (91.82) 339.88*** (102.17) 339.88*** (92.01)
Biomass (cid:0) 172.90* (78.72) (cid:0) 211.59 (125.11) (cid:0) 83.33 (147.97) (cid:0) 83.33 (130.95)
ln_Proj_Installed_Capacity 46.90** (16.86) 48.24** (17.19) 64.20*** (17.25) 64.20*** (18.42)
Dev_Transmission_Risks:Wind (cid:0) 367.07*** (67.93) (cid:0) 378.70*** (68.22) (cid:0) 416.98*** (73.21) (cid:0) 416.98*** (89.87)
Preliminary_Phase:Wind (cid:0) 239.70** (78.41) (cid:0) 229.33** (81.59) (cid:0) 347.64*** (97.47) (cid:0) 347.64** (126.77)
Preliminary_Phase:Solar_PV (cid:0) 78.24 (101.04) (cid:0) 85.23 (101.50) (cid:0) 100.91 (105.65) (cid:0) 100.91 (123.62)
Constant 158.95 (233.81) 177.47 (238.88) 64.76 (237.89) 64.76 (227.55)
Auction Year Covariate No No Yes Yes
Contract Type Control No Yes Yes Yes
Observations 339 339 339 339
R2 0.26 0.26 0.28 0.40
Adjusted R2 0.24 0.24 0.25 0.38
*p <0.05.
**p <0.01.
***p <0.001.
existing prequalification criteria and penalties did not create relevant Proj_Installed_Capacity has a significant positive effect on project de-
further incentive to the on-implementation of projects. lays, which is in line with previous findings in the literature (Callegari
Individual_Bid_Ratio was not significantly related to delays incurred et al., 2018; Portugal-Pereira et al., 2018; Sovacool et al., 2014), that
by the contracted power plants, which means that apparently there was large scale projects are more prone to cost overruns and schedule slip-
not a problem with project delays caused by excessively low bids of pages, due to their inherently higher complexity and more associated
individual projects. This result might be associated with the hybrid uncertainties. Thus, although this finding may advocate towards the
system adopted in Brazilian auctions in which, according to Del Río and adoption of auction design mechanisms that favor small-scale projects,
Linares (2014), the first descending-clock phase allow for price discov- which might lead to higher on-time implementation rates, restricting the
ery and minimizes the winner’s curse, while the second sealed-bid phase participation of larger projects can impede economies of scale and
prevents collusion. reduce competition levels in the short-term, leading to lower support
Biomass-powered thermoelectric plants were less prone to delays, cost efficiency. For example, Anatolitis et al. (2022) empirically found a
which is in line with prediction from Section 2, though the coefficient on price-increasing effect in RES auctions implemented exclusively for
Biomass is only significant in Model 1. On the other hand, Wind showed a small-scale (<1 MW) projects. On this issue, the literature (Flyvbjerg,
significantly positive coefficient in all models, which reflects the poor 2014) does not always recommend avoiding larger projects. Instead, it
on-time implementation of on-shore wind farms in Brazilian early auc- recommends having a very careful pre-FID (final investment decision)
tions (see Fig. 1), mainly caused by grid connection issues (Bayer et al., analysis of them, raising all risks that might be incurred with larger
2018). projects (e.g. cost inflation and delays) and addressing the possible ad-
The coefficients on the interaction term Dev_Transmission_Risks:Wind aptations that might be needed during the implementation phase.
are negative and significant in all models, indicating that the allocation It is important to note that, although multiple regression techniques
of transmission risks to generators is associated with a strong improve- allow controlling for certain confounding variables, it is not possible to
ment in the implementation schedule of wind power plants. This cor- determine from data the presence of unmeasured lurking variables that
roborates IRENA and CEM (2015), who point out that this design option might be affecting the observed delays. For this reason, in the analyses
is an efficient way of improving the on-time realization rate, since it employed in this study, the association between variables and outcomes
forces generation developers to prioritize the development of projects in may bring interesting insights but does not necessarily imply the exis-
sites with lower risk of network connection, but bidders might include tence of causal relations.
this liability as a risk premium in their bids, potentially resulting in price Another limitation of our study is the potential bias introduced by
increases. Although wind power bid prices have indeed increased after the exclusion from the sample of projects delayed by more than 3 years
this change in auction rules, further studies are needed to investigate or that have been ultimately cancelled. Although some variables from
eventual causal relations, since such increase may be associated to a our study may have influence on project cancellations, our sample size
plethora of factors lying outside tender rules, such as changes on Bra- and information available do not allow for establishing robust in-
zilian currency (BRL) exchange rates and the rise of infrastructure ferences. Moreover, cancellations shall be analyzed in each case, since it
financing interest rates. The effect of the allocation of grid connection may be affected by a multitude of specific factors and circumstances not
risks on wind power plants delays can be seen in Fig. 2, which shows the considered in our analysis, including individual negotiation with regu-
distribution of project delays for different technologies in our sample. lators on the application of potential sanctions, contract termination
Regarding the adoption of a preliminary transmission capacity stage,
the terms Preliminary_Phase:Wind and Preliminary_Phase:Solar_PV
showed a negative effect on awarded project delays, though for solar
photovoltaic projects this reduction is not significant at usual levels. This
result indicates the success of this design element intended to reduce
grid connection issues, especially for on-shore wind power plants, for
which grid connection issues might have been more relevant to
completion schedules than for other RE sources, such as Solar PV.
7

B.A. Diniz et al. E n e r g y P o l i c y 175(2023)113467
Fig. 1. Project delays per technology, scale and auction date. Source: Own depiction based on (Diniz, 2022).
opportunities due to electricity oversupply, land-use conflicts, problems rounds held in Brazil between 2005 and 2017. From this universe, we
with suppliers, and the effect of economic cycles10. selected a sample of projects from the sources that had a considerable
expansion in Brazil in the period (Wind, Solar PV, Biomass and Hydro-
5. Conclusions and policy implications power) and employed multiple regression analyses to investigate the
integrated effect of auction design elements and individual bids and
Brazil has a long-running experience with auctions as an instrument project features on observed project delays.
to procure electricity both from renewable and non-renewable sources. Our results add empirical evidence to the literature and may provide
We argue that important lessons on policy options for RES auction policy makers with new insights on how to design effective and efficient
design may be drawn from the Brazilian historical experience on the auctions to promote the expansion of renewable electricity supply.
implementation schedule of awarded projects. We find that biomass-powered thermal plants were less prone to
We built and published a unique database containing detailed in- delays than other types of power plants, while on-shore wind projects
formation on 522 generation projects with a total installed capacity of had significantly longer delays in comparison to other sources. However,
74.5 GW, which sold electricity equivalent to 6682 TWh in 37 auction we present empirical evidence that the on-time implementation per-
formance of wind power projects has been strongly improved after the
introduction of regulatory changes aimed at mitigating problems related
to the connection of power plants to the transmission grid, which was
10 For example, there was a 36% devaluation of the Brazilian currency (BRL) the key determinant for project delays. This includes, first, the assign-
against the US Dollar in the year following the first auction round with
ment to project developers of the risk of delay in the transmission grid
participation of photovoltaic technology (6th LER, 2014). Contracted projects
extension; then, the introduction, in auctions with shorter lead times, of
faced a significant challenge, with escalation of costs for imported equipment
a preliminary phase to shortlist projects that fit in the available trans-
that had to be purchased at an exchange rate higher than estimated at bidding
mission capacity in each connection point. The Brazilian experience
time (Barbosa et al., 2020). From 11 solar PV plants awarded in that auction
round, 6 have been cancelled, while the others were completed out of schedule. shows that policy makers might consider the adoption of similar auction
8

B.A. Diniz et al. E n e r g y P o l i c y 175(2023)113467
Fig. 2. Project delays by project technology and allocation of grid connection risks.
design mechanisms that may extensively reduce project delays, espe- projects database from this study, could eventually provide insights into
cially in countries facing the challenge of transmission grid expansion to potential improvements on the integrated expansion of generation and
connect new renewable energy capacity. transmission infrastructure. Also, similar studies on the experience of
Projects contracted in auctions with longer lead times took more other countries may bring different perspectives and solutions. Finally, it
time to be completed but were less prone to delays. Thus, extending the would be interesting to include other relevant variables in the database
period available for the construction of power plants might be an option and apply econometric techniques to analyze the effect of the design
to reduce project developers’ risks of incurring in penalties, which in elements discussed in this paper on bid prices and other policy objec-
theory may lead to lower bid prices. tives, which might shed light on interrelations and trade-offs between
We find no significant difference in terms of completion schedule them.
performance between projects awarded in technology-specific auctions
and those that competed directly with other technologies in the same CRediT authorship contribution statement
tender. This is in line with findings from Matth¨aus (2020), that tech-
nological banding do not have a major impact on RES auction realization Bruno Andrade Diniz: Conceptualization, Methodology, Writing –
rates. Therefore, auctioneers’ decision on whether to adopt this design original draft, Writing – review & editing. Alexandre Szklo: Concep-
element should focus on other policy objectives, such as fostering tualization, Methodology, Supervision, Writing – review & editing.
immature technologies, diversifying the generation mix or minimizing Maurício T. Tolmasquim: Conceptualization, Methodology, Supervi-
support cost levels. sion, Writing – review & editing. Roberto Schaeffer: Conceptualization,
Moreover, no association was found between low bids of individual Methodology, Supervision, Writing – review & editing.
projects and the delays incurred by the respective power plants, which
apparently supports the theoretical prediction that hybrid auction sys-
tems as the one adopted in Brazilian auctions may minimize the win- Declaration of competing interest
ner’s curse.
Large scale projects were significantly associated with longer delays, The authors declare that they have no known competing financial
which corroborates results from previous studies on electricity infra- interests or personal relationships that could have appeared to influence
structure worldwide. This suggests that policy makers concerned with the work reported in this paper.
on-time implementation rates should consider the adoption of auction
design mechanisms that favor small-scale projects. However, such de- Data availability
cision must carefully consider the risks and benefits in terms of
competition, economies of scale and support cost efficiency, as well as We have shared our research data on Mendeley Data Repository
other policy objectives such as actor diversity, social acceptability and
decentralization of renewable energy production. Acknowledgements
The conclusions from this work and the published database open the
door for insightful further research. First, adding information on projects Alexandre Szklo and Roberto Schaeffer would like to acknowledge
shareholder structure might enable the assessment of how developer size financial support from the National Council for Scientific and Techno-
and experience impact project delays. Likewise, data on transmission logical Development (CNPq) of Brazil [grants 303554/2021-5 and
auctions and project schedules, in combination with the generation 310992/2020-6, respectively].
9

B.A. Diniz et al.                                                                                                                                                                                                              E  n  e r  g y   P  o l i c  y 175(2023)113467
Appendix A
Table A.1
Auction rounds for which deadlines have been met
Auction  Official  Auction  Auction with  Transmission  Auction products  Awarded projects
| Type  name  | date  preliminary  | risks allocated to  |                |               |                      |                   |
| ----------- | ------------------ | ------------------- | -------------- | ------------- | -------------------- | ----------------- |
|             |                    |                     | Technological  | Technologies  | Contract  Lead Time  | Number  Capacity  |
|             | transmission       | generators          |                |               |                      |                   |
|             | capacity stage     |                     | banding        |               | Type  (months)       | of  (MW)          |
projects
LEN  01◦LEN  2005-12-  No  Yes  Specific  Small Hydro  Quantity  25  2  739
|     | 16  |     |     |     | 37  | 8  1412  |
| --- | --- | --- | --- | --- | --- | -------- |
49  1  84
|     |     |     | Multi-      | Thermal (any)  | Availability  25  | 8  1604  |
| --- | --- | --- | ----------- | -------------- | ----------------- | -------- |
|     |     |     | technology  |                | 37                | 10  945  |
49  2  566
LEN  02◦LEN  2006-06-  No  Yes  Specific  Small Hydro  Quantity  31  10  587
|     | 29  |     | Multi-  | Thermal (any)  | Availability  31  | 14  1280  |
| --- | --- | --- | ------- | -------------- | ----------------- | --------- |
technology
LEN  03◦LEN  2006-10-  No  Yes  Multi-  Small Hydro,  Quantity  51  5  891
|     | 10  |     | technology  | Large Hydro    |                   |           |
| --- | --- | --- | ----------- | -------------- | ----------------- | --------- |
|     |     |     |             | Thermal (any)  | Availability  51  | 10  1948  |
01◦LFA
LFA  2007-06-  No  Yes  Specific  Small Hydro  Quantity  31  6  107
|     | 18  |     | Multi-  | Wind, Biomass  | Availability  31  | 8  502  |
| --- | --- | --- | ------- | -------------- | ----------------- | ------- |
technology
04◦LEN
LEN  2007-07-  No  Yes  Multi-  Thermal (any)  Availability  30  12  1808
|     | 26  |     | technology  |     |     |     |
| --- | --- | --- | ----------- | --- | --- | --- |
LEN  05◦LEN  2007-10-  No  Yes  Multi-  Small Hydro,  Quantity  51  5  2383
|     | 16  |     | technology  | Large Hydro    |                   |          |
| --- | --- | --- | ----------- | -------------- | ----------------- | -------- |
|     |     |     |             | Thermal (any)  | Availability  51  | 5  2140  |
LPE  UHE  2007-12-  No  No  Specific  Large Hydro  Quantity  49  1  3151
| Santo  | 10  |     |     |     |     |     |
| ------ | --- | --- | --- | --- | --- | --- |
Antoˆnio
LPE  UHE  2008-05-  No  No  Specific  Large Hydro  Quantity  57  1  3300
| Jirau  | 09  |     |     |     |     |     |
| ------ | --- | --- | --- | --- | --- | --- |
01◦LER
LER  2008-08-  No  No  Specific  Biomass  Availability  5  2  176
|     | 14  |     |     |     | 17  | 29  2000  |
| --- | --- | --- | --- | --- | --- | --------- |
LEN  06◦LEN  2008-09-  No  Yes  Multi-  Thermal (any),  Availability  28  10  1935
|     | 17  |     | technology  | Small Hydro  |     |     |
| --- | --- | --- | ----------- | ------------ | --- | --- |
07◦LEN
LEN  2008-09-  No  Yes  Multi-  Wind, Small  Availability  52  22  5096
|     | 30  |     | technology  | Hydro, Thermal  |     |     |
| --- | --- | --- | ----------- | --------------- | --- | --- |
(any)
|     |     |     | Specific  | Large Hydro  | Quantity  52  | 1  350  |
| --- | --- | --- | --------- | ------------ | ------------- | ------- |
08◦LEN
LEN  2009-08-  No  Yes  Multi-  Thermal (any)  Availability  29  1  68
|     | 27  |     | technology  |     |     |     |
| --- | --- | --- | ----------- | --- | --- | --- |
LER  02◦LER  2009-12-  No  No  Specific  Wind  Quantity  31  27  1744
14
LPE  UHE Belo  2010-04-  No  No  Specific  Large Hydro  Quantity  57  1  11233
| Monte  | 20  |     |     |     |     |     |
| ------ | --- | --- | --- | --- | --- | --- |
10◦LEN
LEN  2010-07-  No  No  Multi-  Large Hydro,  Quantity  54  7  823
|     | 30  |     | technology  | Small Hydro  |     |     |
| --- | --- | --- | ----------- | ------------ | --- | --- |
LER  03◦LER  2010-08-  No  No  Specific  Biomass  Quantity  4  3  228
|     | 25  |     |     |     | 16  | 1  70  |
| --- | --- | --- | --- | --- | --- | ------ |
29  1  80
|     |     |     |     | Wind         | Quantity  37  | 11  548  |
| --- | --- | --- | --- | ------------ | ------------- | -------- |
|     |     |     |     | Small Hydro  | Quantity  37  | 2  32    |
02◦LFA
LFA  2010-08-  No  No  Multi-  Wind,Small  Availability  29  17  1384
|     | 26  |     | technology  | Hydro,Biomass  | Quantity  29  | 5  107  |
| --- | --- | --- | ----------- | -------------- | ------------- | ------- |
LEN  11◦LEN  2010-12-  No  No  Specific  Large Hydro  Quantity  49  2  2174
17
12◦LEN
LEN  2011-08-  No  No (*)  Multi-  Wind,Thermal  Availability  31  18  2169
|     | 17  |     | technology  | (any)         |               |         |
| --- | --- | --- | ----------- | ------------- | ------------- | ------- |
|     |     |     |             | Large Hydro,  | Quantity  31  | 1  450  |
Small Hydro
04◦LER
LER  2011-08-  No  No  Multi-  Wind,Biomass  Quantity  35  15  961
|     | 18  |     | technology  |     |     |     |
| --- | --- | --- | ----------- | --- | --- | --- |
LEN  13◦LEN  2011-12-  No  No  Multi-  Large Hydro,  Quantity  49  1  135
|     | 20  |     | technology  | Small Hydro   |                   |          |
| --- | --- | --- | ----------- | ------------- | ----------------- | -------- |
|     |     |     |             | Wind,Thermal  | Availability  49  | 10  823  |
(any)
15◦LEN
LEN  2012-12-  No  No  Multi-  Wind,Thermal  Availability  49  3  252
|     | 14  |     | technology  | (any)         |               |         |
| --- | --- | --- | ----------- | ------------- | ------------- | ------- |
|     |     |     |             | Large Hydro,  | Quantity  49  | 2  258  |
Small Hydro
05◦LER
LER  2013-08-  Yes  No  Specific  Wind  Quantity  25  8  1044
23
LEN  16◦LEN  2013-08-  No  No  Multi-  Thermal (any)  Availability  53  6  497
|     | 29  |     | technology  | Small Hydro,  | Quantity  53  | 10  633  |
| --- | --- | --- | ----------- | ------------- | ------------- | -------- |
Large Hydro
(continued on next page)
10

B.A. Diniz et al.                                                                                                                                                                                                              E  n  e r  g y   P  o l i c  y 175(2023)113467
Table A.1 (continued)
Auction  Official  Auction  Auction with  Transmission  Auction products  Awarded projects
| Type  name  | date  preliminary  | risks allocated to  |                |               |                      |                   |
| ----------- | ------------------ | ------------------- | -------------- | ------------- | -------------------- | ----------------- |
|             |                    |                     | Technological  | Technologies  | Contract  Lead Time  | Number  Capacity  |
|             | transmission       | generators          |                |               |                      |                   |
|             |                    |                     | banding        |               | Type  (months)       | of  (MW)          |
capacity stage
projects
LEN  17◦LEN  2013-11-  No  Yes  Multi-  Wind,Solar,  Availability  26  3  377
|     | 18  |     | technology  | Thermal (any)  |     |     |
| --- | --- | --- | ----------- | -------------- | --- | --- |
18◦LEN
LEN  2013-12-  No  Yes  Multi-  Wind,Solar  Availability  53  20  1775
|     | 13  |     | technology  | Thermal (any)  | Availability  53  | 4  142    |
| --- | --- | --- | ----------- | -------------- | ----------------- | --------- |
|     |     |     |             | Small Hydro,   | Quantity  53      | 15  1049  |
Large Hydro
19◦LEN
LEN  2014-06-  No  Yes  Multi-  Wind,Thermal  Availability  31  3  398
|     | 06  |     | technology  | (any)         |               |         |
| --- | --- | --- | ----------- | ------------- | ------------- | ------- |
|     |     |     |             | Large Hydro,  | Quantity  31  | 1  418  |
Small Hydro
06◦LER
LER  2014-10-  No  Yes  Specific  Wind  Quantity  36  3  370
|     | 31  |     |     | Solar  | 36  | 11  827  |
| --- | --- | --- | --- | ------ | --- | -------- |
LEN  20◦LEN  2014-11-  No  Yes  Multi-  Wind,Solar  Availability  50  8  764
|     | 28  |     | technology  | Thermal (any)  | Availability  50  | 7  3865  |
| --- | --- | --- | ----------- | -------------- | ----------------- | -------- |
|     |     |     |             | Large Hydro,   | Quantity  50      | 3  44    |
Small Hydro
03◦LFA
LFA  2015-04-  Yes  Yes  Specific  Wind  Availability  27  1  90
27
LEN  21◦LEN  2015-04-  No  Yes  Multi-  Thermal (any)  Availability  57  3  1607
|     | 30  |     | technology  | Large Hydro,  | Quantity  57  | 10  355  |
| --- | --- | --- | ----------- | ------------- | ------------- | -------- |
Small Hydro
LEN  22◦LEN  2015-08-  Yes  Yes  Specific  Wind  Availability  29  3  325
|     | 21  |     | Multi-      | Thermal (any)  | Availability  29  | 2  36  |
| --- | --- | --- | ----------- | -------------- | ----------------- | ------ |
|     |     |     | technology  | Large Hydro,   | Quantity  29      | 7  66  |
Small Hydro
LER  07◦LER  2015-08-  No  Yes  Specific  Solar  Quantity  23  12  626
28
08◦LER
LER  2015-11-  Yes  Yes  Specific  Wind  Quantity  36  5  524
|     | 13  |     |     | Solar  | Quantity  36  | 16  853  |
| --- | --- | --- | --- | ------ | ------------- | -------- |
LEN  23◦LEN  2016-04-  No  Yes  Multi-  Thermal (any)  Availability  57  1  6
|     | 29  |     | technology  | Thermal (any)  | Availability  57  | 6  188   |
| --- | --- | --- | ----------- | -------------- | ----------------- | -------- |
|     |     |     |             | Small Hydro,   | Quantity  57      | 14  194  |
Large Hydro
LER  10◦LER  2016-09-  No  Yes  Specific  Small Hydro  Quantity  42  31  184
23
LEN  25◦LEN  2017-12-  Yes  Yes  Specific  Wind  Availability  37  1  69
|     | 18  |     |             | Solar         | Availability  37  | 6  639  |
| --- | --- | --- | ----------- | ------------- | ----------------- | ------- |
|     |     |     | Multi-      | Large Hydro,  | Quantity  37      | 2  12   |
|     |     |     | technology  | Small Hydro   |                   |         |
Source: Own depiction based on ANEEL’s auction notices, PPA drafts and CCEE (2021a).
(*) In this auction round, in case of delays in the transmission system, generators would receive contract revenues as normal, but they would need to procure
compensatory firm energy certificates in order to honor the contract.
References  Callegari, C., Szklo, A., Schaeffer, R., 2018. Cost overruns and delays in energy
megaprojects: how big is big enough? Energy Pol. 114, 211–220. https://doi.org/
10.1016/j.enpol.2017.11.059.
Anatolitis, V., Azanbayev, A., Fleck, A., 2022. How to design efficient renewable energy
Carvalho, D.B., Pinto, B.L., Guardia, E.C., Marangon Lima, J.W., 2020. Economic impact
auctions ? Empirical insights from Europe. Energy Pol. 166, 112982 https://doi.org/
1 0 . 1 0 1 6 / j . e np o l. 2 0 2 2 .1 1 2 9 8 2 .   of anticipations or delays in the completion of power generation projects in the
Brazilian energy market. Renew. Energy 147, 1312–1320. https://doi.org/10.1016/
| ANE E L ,  2 0 2 1 .   R A L IE   -  | R e la to´ r i o  d e   Acompanhamento da Expans˜ao da Oferta de Geraça˜o  |     |     |     |     |     |
| ------------------------------------ | -------------------------------------------------------------------------- | --- | --- | --- | --- | --- |
de Energia El´etrica [WWW Document]. URL. https://www.aneel.gov.br/acompanha  j . r e n e n e . 20 1 9 . 0 9 . 0 7 4 .
|     |     |     | Cass e | t t a ,  E . ,  M o n a r c a ,  U . | ,  R ubina, C., Meleo, L., 2017. Is the answer blowin’ in the wind  |     |
| --- | --- | --- | ------ | ------------------------------------ | ------------------------------------------------------------------- | --- |
mento-da-expansao-da-oferta-de-geracao-de-energia-eletrica, 11.30.21.
(auctions)? An assessment of the Italian support scheme. Energy Pol. 110, 662–674.
AURES II, 2022. AURES II Project Auction Database. URL. http://aures2project.eu/auct
ion-database/.  https://doi.org/10.1016/j.enpol.2017.08.055.
CCEE, 2021a. Consolidated Auction Results - December 2021.
Azuela Elizondo, G., Barroso, L., Khanna, A., Wang, X., Wu, Y., Cunha, G., 2014.
CCEE, 2021b. Market Information Bulletin - Individual Project Data - December 2021.
Performance of Renewable Energy Auctions: Experience in Brazil, China and India.  Correia, T. de B., Tolmasquim, M.T., Hallack, M., 2020. Guide for Designing Contracts for
Bacon, R.W., Besant-Jones, J.E., 1998. Estimating construction costs and schedules:
Renewable Energy Procured by Auctions, Inter-American Development Bank
experience with power generation projects in developing countries. Energy Pol. 26,
317–333. https://doi.org/10.1016/S0301-4215(97)00164-X.  Monograph. https://doi.org/10.18235/0002583.
Dalbem, M.C., Brand˜ao, L.E.T., Gomes, L.L., 2014. Can the regulated market help foster a
Bacon, R.W., Besant-Jones, J.E., Heidarian, J., 1996. Estimating Construction Costs and  free market for wind energy in Brazilα. Energy Pol. 66, 303–311. https://doi.org/
Schedules : Experience with Power Generation Projects in Developing Countries (No.  10.1016/j.enpol.2013.11.019.
WTP325). Energy, Washington,D.C.
del Río, P., 2017. Designing auctions for renewable electricity support. Best practices
Barbosa, J.P., Saraiva, J.D., Seixas, J., 2020. Solar energy policy to boost Brazilian power  from around the world. Energy Sustain. Dev. 41, 1–13. https://doi.org/10.1016/j.
sector. Int. J. Clim. Change Strat. Manag. 12 (3), 349–367. https://doi.org/10.1108/
esd.2017.05.006.
IJCCSM-07-2019-0039.
Batz Lin˜eiro, T., Müsgens, F., 2021. Evaluating the German PV auction program: the  del Río, P., Haufe, M.-C., Wigan, F., Steinhilber, S., 2015. Overview of Design Elements
for RES-E Auction. EU Horizon 2020 program grant number 646172.
secrets of individual bids revealed. Energy Pol. 159 https://doi.org/10.1016/j.
del Río, P., Kiefer, C.P., 2021. Analysing patterns and trends in auctions for renewable
enpol.2021.112618.  electricity. Energy Sustain. Dev. 62, 195–213. https://doi.org/10.1016/j.
Bayer, B., 2018. Experience with auctions for wind power in Brazil. Renew. Sustain.
esd.2021.03.002.
Energy Rev. 81, 2644–2658. https://doi.org/10.1016/j.rser.2017.06.070.
del Río, P., Linares, P., 2014. Back to the future? Rethinking auctions for renewable
Bayer, B., Berthold, L., Moreno Rodrigo de Freitas, B., 2018. The Brazilian experience  electricity support. Renew. Sustain. Energy Rev. 35, 42–56. https://doi.org/
with auctions for wind power: an assessment of project delays and potential
mitigation measures. Energy Pol. 122, 97–117. https://doi.org/10.1016/j.  10.1016/j.rser.2014.03.039.
enpol.2018.07.004.
11

B.A. Diniz et al. E n e r g y P o l i c y 175(2023)113467
Diniz, B.A., 2022. Delays in the Construction of Power Plants from Electricity Auctions in ONS, 2022. Power Plants List Table [WWW Document]. URL. http://www.ons.org.br/
Brazil, vol. 2. Mendeley Data. https://doi.org/10.17632/5c74fkwd5y.2. Paginas/resultados-da-operacao/historico-da-operacao/tabela-relacao-usinas.aspx,
Flyvbjerg, B., 2014. What you should know about megaprojects and why: an overview. 2.25.22.
Proj. Manag. J. 45, 6–19. https://doi.org/10.1002/pmj.21409. Pahle, M., Schaeffer, R., Pachauri, S., Eom, J., Awasthy, A., Chen, W., Di Maria, C.,
Gohel, D., Skintzos, P., 2022. Flextable: Functions for Tabular Reporting. Jiang, K., He, C., Portugal-Pereira, J., Safonov, G., Verdolini, E., 2021. The crucial
Haufe, M.C., Ehrhart, K.M., Haufe, M.C., Ehrhart, K.M., 2018. Auctions for renewable role of complementarity, transparency and adaptability for designing energy policies
energy support – suitability, design, and first lessons learned. Energy Pol. 121, for sustainable development. Energy Pol. 159, 112662 https://doi.org/10.1016/j.
217–224. https://doi.org/10.1016/j.enpol.2018.06.027. enpol.2021.112662.
Held, A., Ragwitz, M., Gephart, M., de Visser, E., Klessmann, C., 2014. Design Features of Polzin, F., Migendt, M., Ta¨ube, F.A., von Flotow, P., 2015. Public policy influence on
Support Schemes for Renewable Electricity. Ecofys. renewable energy investments-A panel data study across OECD countries. Energy
Herrera, M.M., Dyner, I., Cosenz, F., 2019. Assessing the effect of transmission Pol. 80, 98–111. https://doi.org/10.1016/j.enpol.2015.01.026.
constraints on wind power expansion in northeast Brazil. Util. Pol. 59, 100924. htt Portugal-Pereira, J., Ferreira, P., Cunha, J., Szklo, A., Schaeffer, R., Araújo, M., 2018.
ps://doi.org/10.1016/j.jup.2019.05.010. Better late than never, but never late is better: risk assessment of nuclear power
Hlavac, M., 2022. Stargazer: Well-Formatted Regression and Summary Statistics Tables. construction projects. Energy Pol. 120, 158–166. https://doi.org/10.1016/j.
Hochberg, M., Poudineh, R., 2018. Renewable auction design in theory and practice: enpol.2018.05.041.
lessons from the experiences of Brazil and Mexico. Oxford Inst. Energy Stud 1–62. Probst, B., Anatolitis, V., Kontoleon, A., Anado´n, L.D., 2020. The short-term costs of local
Huenteler, J., Tang, T., Chan, G., Anadon, L.D., 2018. Why is China’s wind power content requirements in the Indian solar auctions. Nat. Energy 5, 842–850. https://
generation not living up to its potential? Environ. Res. Lett. 13 https://doi.org/ doi.org/10.1038/s41560-020-0677-7.
10.1088/1748-9326/aaadeb. Quintana-Rojo, C., Callejas-Albin˜ana, F.E., Taranco´n, M.´angel, Martínez-Rodríguez, I.,
IRENA, 2019. Renewable energy auctions: status and trends beyond price. Renewable 2020. Econometric studies on the development of renewable energy sources to
energy auctions: Status and trends beyond price. URL. https://www.irena.org/-/me support the European Union 2020-2030 climate and energy framework: a critical
dia/Files/IRENA/Agency/Publication/2019/Dec/IRENA_RE-Auctions_Status-and- appraisal. Sustain. Times 12. https://doi.org/10.3390/su12124828.
trends_2019.pdf. R Core Team, 2022. R: a Language and Environment for Statistical Computing. R
IRENA, CEM, 2015. Renewable Energy Auctions, Renewable Energy Auctions - A Guide Foundation for Statistical Computing.
to Design. Shrimali, G., Konda, C., Farooquee, A.A., 2016. Designing renewable energy auctions for
Ko¨berle, A.C., Garaffa, R., Cunha, B.S.L., Rochedo, P., Lucena, A.F.P., Szklo, A., India: managing risks to maximize deployment and cost-effectiveness. Renew.
Schaeffer, R., 2018. Are conventional energy megaprojects competitive? Suboptimal Energy 97, 656–670. https://doi.org/10.1016/j.renene.2016.05.079.
decisions related to cost overruns in Brazil. Energy Pol. 122, 689–700. https://doi. Sovacool, B.K., Gilbert, A., Nugent, D., 2014. Risk, innovation, electricity infrastructure
org/10.1016/j.enpol.2018.08.021. and construction cost overruns: testing six hypotheses. Energy 74, 906–917. https://
Kreiss, J., Ehrhart, K.-M., Haufe, M.-C., Rosenlund Soysal, E., 2021. Different cost doi.org/10.1016/j.energy.2014.07.070.
perspectives for renewable energy support: assessment of technology-neutral and Tolmasquim, M.T., de Barros Correia, T., Addas Porto, N., Kruger, W., 2021. Electricity
discriminatory auctions. Econ. Energy Environ. Policy 10. https://doi.org/10.5547/ market design and renewable energy auctions: the case of Brazil. Energy Pol. https://
2160-5890.10.1.jkre. doi.org/10.1016/j.enpol.2021.112558.
Kreiss, J., Ehrhart, K.M., Haufe, M.C., 2017. Appropriate design of auctions for Watanabe, M.D.B., Morais, E.R., Cardoso, T.F., Chagas, M.F., Junqueira, T.L.,
renewable energy support – prequalifications and penalties. Energy Pol. 101, Carvalho, D.J., Bonomi, A., 2020. Process simulation of renewable electricity from
512–520. https://doi.org/10.1016/j.enpol.2016.11.007. sugarcane straw: techno-economic assessment of retrofit scenarios in Brazil. J. Clean.
Kitzing, Lena, Anatolitis, Vasilios, Fitch-Roy, Oscar, Klessmann, Corinna, Jan, Kreiss, Prod. 254, 120081 https://doi.org/10.1016/j.jclepro.2020.120081.
Pablo Del Río, Wigand, Fabian, Woodman, Bridget, 2019. Auctions for renewable Wickham, H., 2016. ggplot2: Elegant Graphics for Data Analysis. Springer-Verlag, New
energy support: lessons learned in the AURES project. IAEE Energy Forum 11–14. York.
Lu, X., McElroy, M.B., Peng, W., Liu, S., Nielsen, C.P., Wang, H., 2016. Challenges faced Winkler, J., Magosch, M., Ragwitz, M., 2018. Effectiveness and efficiency of auctions for
by China compared with the US in developing wind power. Nat. Energy 1. https:// supporting renewable electricity – what can we learn from recent experiences?
doi.org/10.1038/nenergy.2016.61. Renew. Energy 119, 473–489. https://doi.org/10.1016/j.renene.2017.09.071.
Lucas, H., del Río, P., Cabeza, L.F., 2020. Stand-alone renewable energy auctions: the Wooldridge, J.M., 2018. Introductory Econometrics.
case of Peru. Energy Sustain. Dev. 55, 151–160. https://doi.org/10.1016/j. Zeileis, A., Hothorn, T., 2002. Diagnostic checking in regression relationships. R. News 2,
esd.2020.01.009. 7–10.
Lüdecke, D., Ben-Shachar, M., Patil, I., Waggoner, P., Makowski, D., 2021. Performance: Zhang, S., Andrews-Speed, P., Zhao, X., He, Y., 2013. Interactions between renewable
an R package for assessment, comparison and testing of statistical models. J. Open energy policy and renewable energy industrial policy: a critical analysis of China’s
Source Softw. 6, 3139. https://doi.org/10.21105/joss.03139. policy approach to renewable energies. Energy Pol. 62, 342–353. https://doi.org/
Mattha¨us, D., 2020. Designing effective auctions for renewable energy support. Energy 10.1016/j.enpol.2013.07.063.
Pol. 142 https://doi.org/10.1016/j.enpol.2020.111462.
12
