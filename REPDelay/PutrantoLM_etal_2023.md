2023 15th International Conference on Information Technology and Electrical Engineering (ICITEE)
Analysis of Renewable Energy Project Delays on
The Indonesia’s Energy Transition Process, Case
Study: Java Bali System
|     |     | Tumiran  |     |     |     | Sarjiya  |     | Lesnanto Multa Putranto  |     |     |     |
| --- | --- | -------- | --- | --- | --- | -------- | --- | ------------------------ | --- | --- | --- |
Department of Electrical and  Department of Electrical and   Department of Electrical and
88671301.3202.28595EETICI/9011.01 :IOD | EEEI 3202© 00.13$/32/6-6440-3053-8-979 | )EETICI( gnireenignE lacirtcelE dna ygolonhceT noitamrofnI no ecnerefnoC lanoitanretnI ht51 3202
Information Engineering  Information Engineering  Information Engineering
Universitas Gadjah Mada  Universitas Gadjah Mada  Universitas Gadjah Mada
Yogyakarta, Indonesia  Yogyakarta, Indonesia  Yogyakarta, Indonesia
|     | tumiran@ugm.ac.id  |     |     |     | sarjiya@ugm.ac.id  |     |     | lesnanto@ugm.ac.id  |     |     |     |
| --- | ------------------ | --- | --- | --- | ------------------ | --- | --- | ------------------- | --- | --- | --- |
|     |                    |     |     |     |                    |     |     |                     |     |     |     |
Rizki Firmansyah Setya Budi  Ahmad Adhiim Muthahhari  Amira Hanun
Research Center for Reactor Nuclear  Electrical Engineering Technology  Department of Electrical and
Technology  Universitas Gadjah Mada  Information Engineering
National Research and Innovation  Yogyakarta, Indonesia  Universitas Gadjah Mada
|     |     | Agency             |     | ahmad.adhiim.m@ugm.ac.id  |     |     |     | Yogyakarta, Indonesia       |     |     |     |
| --- | --- | ------------------ | --- | ------------------------- | --- | --- | --- | --------------------------- | --- | --- | --- |
|     |     | Banten, Indonesia  |     |                           |     |     |     | amira.hanun@mail.ugm.ac.id  |     |     |     |
rizk011@brin.go.id
|     |                      |     |     |     |     |     |     |     |     |     |     |
| --- | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | Kurnia Wisesa Kisna  |     |     |     |     |     |     |     |     |     |     |
Department of Electrical and
Information Engineering
Universitas Gadjah Mada
Yogyakarta, Indonesia
kurnia.wisesa.kisna@mail.ugm.ac.id

Abstract— In order to reduce greenhouse gas emissions,  Keywords—  Renewable  energy,  generation  expantion
planning, energy transition, project delays, LCOE
all countries, including Indonesia, are trying to utilize
clean energy in their energy supply. To be able to realize
|           |     |                |              |      |         |     | I.  | INTRODUCTION  |     |     |     |
| --------- | --- | -------------- | ------------ | ---- | ------- | --- | --- | ------------- | --- | --- | --- |
| the  use  | of  | clean  energy  | and  reduce  | the  | effect  | of  |     |               |     |     |     |
Currently, the issue of global warming is a matter of
greenhouse gases, Indonesia has decided to accelerate the
concern to all countries in the world, including Indonesia.
energy transition so that it can achieve NZE by 2060. The
|                                                        |     |     |     |     |     | Various efforts have been made to reduce CO |                |     |            |  emissions and  |     |
| ------------------------------------------------------ | --- | --- | --- | --- | --- | ------------------------------------------- | -------------- | --- | ---------- | --------------- | --- |
| problem that is often encountered in power generation  |     |     |     |     |     |                                             |                |     |            | 2               |     |
|                                                        |     |     |     |     |     | greenhouse                                  | gases  (GHG).  |     | Indonesia  | is  committed   | to  |
projects is delays in power generation projects, which
implementing the Paris Agreement through [1].
have not been considered in the current power plant
|     |     |     |     |     |     | Indonesia  | has  made  | several  | efforts,  | one  | of  them  is  |
| --- | --- | --- | --- | --- | --- | ---------- | ---------- | -------- | --------- | ---- | ------------- |
planning. Based on this, this paper will conduct a study  accelerating the energy transition, especially in the electricity
by considering aspects of the success and delay ratio of a
sector. Based on [2], Indonesia is targeting an increase in its
power plant project in planning. By considering these
renewable energy mix of 23% in 2025 and 31% in 2050. The
aspects, plant planning will be carried out using the MILP  Indonesian government's efforts to increase the utilization of
method and then the influence of the delay and success  clean energy. Based on [3], renewable energy generation
ratio will  be  analyzed  on  the  renewable  energy  mix,  capacity has reached 12.72%.
LCOE, and the plants that will replace it. Based on the  Generation  expansion  planning  with  consider  the
renewable energy has been done in various country, such as
results obtained, The extent of the delay in capacity refers
to the success ratio, delays, and achievements of the power  USA [4], Ireland [5], France [6], China [7]–[9],  Brazil [10],
Portugal [11], Egypt [12], Pakistan [13], Oman [14], South
plant projects. Delayed VRE PP up to 2 GW, and based
Africa [15], Bangladesh [16], Malaysia [17] and Indonesia
on the results, it was found that these generators would be
|     |     |     |     |     |     | [18]–[22]  | have  considered  |     | the  environmentally  |     | friendly  |
| --- | --- | --- | --- | --- | --- | ---------- | ----------------- | --- | --------------------- | --- | --------- |
substituted with Gas Machines up to 2000 MW. This
resource or RES in their GEP model. Based on these studies,
affects the LCOE of the system, increasing it from 9.77
considering VRE can lead to increasing or decreasing the
c$/kWh to up to 8 c$/kWh. This LCOE calculation does  total generation cost.
not yet account for the unavailability of LNG, which
A statistical residual load duration curve (S-RLDC), a
would lead the Gas Machine to utilize more expensive  technique to simplify the duration curve load method, was
HSD (High-Speed Diesel), potentially causing a further  used to model the load for GEP in China [9]. The S-RLDC
increase in the LCOE.  modelled the generation of renewable energy as a negative
|                                        |     |     |     |     |     | load.  In  | [10],  a  GEP  | using  | multiple  objective  |     | functions  |
| -------------------------------------- | --- | --- | --- | --- | --- | ---------- | -------------- | ------ | -------------------- | --- | ---------- |
| 979-8-3503-0446-6/23/$31.00 ©2023 IEEE |     |     |     |     |     | 93         |                |        |                      |     |            |
Authorized licensed use limited to: UNIVERSITY OF BIRMINGHAM. Downloaded on October 28,2025 at 15:18:24 UTC from IEEE Xplore.  Restrictions apply.

2023 15th International Conference on Information Technology and Electrical Engineering (ICITEE)
considering renewable energy was successfully conducted. In
the study, the use of non-hydro renewable energy in the  NAF (3)
|     |     |     |     |     |     |     |     |     |                 | (1-Tax)× |         |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- | -------- | ------- | --- | --- | --- |
|     |     |     |     |     |     |     |     |     | to t al t o tal |          | EcoLife |     |     |     |
Brazilian power system could be increased. Another study  CA n n ual=CI n v ×
|     |     |     |     |     |     |     |     |     |     | g   | ×R1A00F0×P | g   | y   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- |
i n c l u d e d   e x te r na l  c o s t s   o f  e n v i r o n m e n ta l i m p a c t s  o n   G E P  i n   DF y × C m ax NB g   (4)
|     |     |     |     |     |     |     |     | t o tal |     | i   | nv  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- |
C h i n a   to   a c c o m m o d a t e   t h e  e n t r y   o f i n te rm i tte n t   p o w e r  p l an t s  CI n v ="y"g # $
  (5)
| [7].  |     |     |     |     |     |     |       |     |     | g   | g   |     |     |     |
| ----- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
|       |     |     |     |     |     |     | total |     |     |     |     |     | i   |     |
In  addition,  several  studies  on  GEP  have  considered  CFO&M=" " DFy×[CFO&M×Pmax(Ng+" NBg)]
|     |     |     |     |     |     |     |     | to ta ly | g   |     |     | g i≤ | ty  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | ---- | --- | --- |
Indonesia's high share of RES, including dispatchable and  C DF ×L ×(C ×G )  (6)
|     |     |     |     |     |     |     |     | V O & M |     | t y | t   | V O&M | g   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | ----- | --- | --- |
variables  RES  (VREs).  For  example,  research  [22]  ="t"g ∈
|     |     |     |     |     |     |     | C   | to t a l =  | DF  | ×L ×(Heat Rate × C |     | g   | ×G t)   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------------------ | --- | --- | ------- | --- |
incorporates high share VREs of wind in GEP, while research  F u e l t y t f uel g (7)
"t"g
| [23] considers the emission factor among the VREs factor.  |     |     |     |     |     |     |     |     | ∈   |     |     |     |     |     |
| ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1
Moreover, the potential of local energy sources has also been  DF=   (8)
|     |     |     |     |     |     |     |     |     |     | 1+D | y   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
studied in [24], which analyzes utilizing biomass in eastern
|     |     |     |     |     |     |     |     |     |     | (   | )   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Indonesia. Furthermore, research [25] modelled a GEP on  <=>?@ABC  (9)
1−(1+0122+34567894 :67;)
isolated systems, considering local energy sources and the
NAF =
|                                    |     |     |     |     |     |     |     |     | 0122+3456789 |     | 4   |   : 6 7 ;  |     |       |
| ---------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | ---------- | --- | ----- |
| interconnections between systems.  |     |     |     |     |     |     |     |     |              |     |     | C          |     | (10)  |
|                                    |     |     |     |     |     |     |     |     | 1−(1+0122)   |     | <   | = > ? @A B |     |       |
However, based on historical data from [3], the success
RAF =
rasio in a power plant project is not always as expected. Based  With,  0122
on the data that has been processed, the success rate of the         :  Total fixed cost ($/kW/yr)
|                                                          |     |     |     |     |     |     | total |   :  | Total annualized build cost ($/kW/yr)  |     |     |     |     |     |
| -------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ----- | ---- | -------------------------------------- | --- | --- | --- | --- | --- |
| hydro power plant (hydro PP) project is 75%, mini hydro  |     |     |     |     |     |     | CFix  |      |                                        |     |     |     |     |     |
total
power plant (mini hydro PP) 2x%, and PV power plant (PP)  CAnnu al :  Total build cost ($/kW)
total
0% for the Java Bali system until 2021. Delays and success  CInv   :  Total fixed O&M cost ($/kW/yr)
|                                                               |     |     |     |     |     |     | t tooOO | tt&aa ll :  | Total var O&M cost ($/MWh/yr)  |     |     |     |     |     |
| ------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | ------- | ----------- | ------------------------------ | --- | --- | --- | --- | --- |
| of a project can be caused by several factors, such as legal  |     |     |     |     |     |     | CCF V   | & MM        |                                |     |     |     |     |     |
aspects, land acquisition, power purchase agreements, or  Ctotal  :  Total fuel cost ($/MWh)
Fuel
even failures in the construction process.  DF   :  Discount factor
y
Currently, plant planning taking into account aspects of  D  :  Discounted Rate (%)
Pg
success or delay in Indonesia has not been carried out. In  max   :  Generator max capacity (MW)
planning [18], [20], [22], [23], [26], [27], the GEP still does  NBy  :  Number of generator
g
not consider these aspects. Because of this, a study is needed  Gt  :  Generation of generator g in t period
g
that considers the ratio of success and also delays in plant  (MWh)
| planning.  |     |     |     |     |     |     | Cg  |   :  | Build cost of generator g ($/kW)  |     |     |     |     |     |
| ---------- | --- | --- | --- | --- | --- | --- | --- | ---- | --------------------------------- | --- | --- | --- | --- | --- |
inv
In this paper, we will discuss the influence of delay and    :  FO&M cost generator g ($/kW/yr)
g g
success ratios on plant planning. The contribution of this  CCFV OO&&MM   :  VO&M cost generator g ($/MWh/yr)
paper is that it can provide an overview of the impacts and  Cg   :  Fuel cost generator g ($/MWh/yr)
fuel
| mitigation  | that  | need  to  | be  carried  |     | out  if  power  | plant  |     |     |     |     |     |     |     |     |
| ----------- | ----- | --------- | ------------ | --- | --------------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
B. Constraints
| development  | planning  |     | takes  | these  | two  aspects  | into  |     |     |     |     |     |     |     |     |
| ------------ | --------- | --- | ------ | ------ | ------------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
consideration.  During the optimization process, several constraints are
The rest of the paper is as follows: Section II will discuss  taken  into  consideration.  The  power  balance  constraint
the objective function and constraints in the GEP. Section III  ensures that the total generation during a specific period must
describes the methodology of the research to be carried out.  meet or exceed the load demand at that time, as depicted in
Section IV discusses the results of the research. Finally,  equation (11). Additionally, the total generation is limited by
section V presents the conclusions from the results of this  the  available  installed  generating  capacity,  as  stated  in
equation (12). The number of new power plants constructed
research.
|     |     |     |     |     |     |     | cannot  | surpass  | the  maximum  |     | potential,  |     | as  outlined  | in  |
| --- | --- | --- | --- | --- | --- | --- | ------- | -------- | ------------- | --- | ----------- | --- | ------------- | --- |
II.
GENERATION EXPANSION PLANNING  equation (13). However, the total installed capacity must be
adequate to meet the yearly peak load plus a reserve margin
A. Objective Function
specified in equation (14).
In this paper, consider the objective function as in (1). This
aims to obtain the optimal combination of generators to meet
GH
the supply of electricity by considering several aspects such    (11)
|     |     |     |     |     |     |     |     |     |     | F   | F   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
as  delays.  The  objective  function  is  to  minimize  the  "DE ≥L ,∀7
discounted  generation  costs  while  adhering  to  certain  EIJ
GV
constraints [21]–[23], [25]. The calculation of GEP is based    (12)
|     |     |     |     |     |     |     |     | F   |     |     |     | A   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
on the total fixed cost, variable operating and maintenance  DE ≤OPQRESTE+ " TUEY,∀Z,7
cost, and fuel cost. The total fixed cost consists of the total  AWX,XIJ
GV
annualized investment and fixed operating and maintenance    (13)
|                         |     |     |     |     |     |     |     |     |       | A          | A   |     |     |     |
| ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ---------- | --- | --- | --- | --- |
| costs as in (2)-(10).   |     |     |     |     |     |     |     |     | " TUE | ≤TUPQRE,∀Z |     |     |     |     |
AWX,XIJ
|     |           |        |                  |     |       |      | GH         |     | GV  |     |      |           |     | (14)  |
| --- | --------- | ------ | ---------------- | --- | ----- | ---- | ---------- | --- | --- | --- | ---- | --------- | --- | ----- |
|     | minCost=  |        |                  |     |       | (1)  |            |     |     |     |      |           |     |       |
|     |           | to tal | to t al          | to  | t a l |      |            |     |     | A   |      | X         |     |       |
|     |           | CF ix  | + CV O & M + C F |     |       | (2)  | "OPQRESTE+ |     | "   | TUE | Y≥O[ | (1+\]),∀^ |     |       |
u e l
|     |     | total total | total |     |     |     | WiEthIJ,  |     | AWX,XIJ |     |     |     |     |     |
| --- | --- | ----------- | ----- | --- | --- | --- | --------- | --- | ------- | --- | --- | --- | --- | --- |
 CFix =  CAnnual+ CFO&M
94
Authorized licensed use limited to: UNIVERSITY OF BIRMINGHAM. Downloaded on October 28,2025 at 15:18:24 UTC from IEEE Xplore.  Restrictions apply.

2023 15th International Conference on Information Technology and Electrical Engineering (ICITEE)
|     |     |     |     |     |     | 350.000 |     |     |     |     | 45.000 |
| --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | ------ |
Start
|     |     |     |     |     |     | 300.000 |     |     |     |     | 40.000 |
| --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | ------ |
35.000
|     |     | Input Data |     |     |     | 250.000 |     |     |     |     |     |
| --- | --- | ---------- | --- | --- | --- | ------- | --- | --- | --- | --- | --- |
30.000
200.000
25.000
Calculating Power Plant Success Ratio
|     |     | and Delay Ratio for Jawa Bali System |     |     |     | 150.000 |     |     |     |     | 20.000 |
| --- | --- | ------------------------------------ | --- | --- | --- | ------- | --- | --- | --- | --- | ------ |
15.000
100.000
10.000
Jawa Bali Base Case GEP Optimization
50.000
5.000
|                           |     |                            |     |                            |     |     | 0    |                |                     |           | 0   |
| ------------------------- | --- | -------------------------- | --- | -------------------------- | --- | --- | ---- | -------------- | ------------------- | --------- | --- |
|                           |     |                            |     |                            |     |     | 2021 | 2022 2023 2024 | 2025 2026 2027 2028 | 2029 2030 |     |
| Determine Delayed Power   |     | Determine Delayed Power    |     | Determine Delayed Power    |     |     |      |                |                     |           |     |
| Plant Project for 1 year  |     | Plant Project for 3 years  |     | Plant Project for 5 years  |     |     |      |                |                     |           |     |
delayed Scenario delayed Scenario delayed Scenario Demand (GWh) Peak Load (MW)
Fig. 2. Java Bali System Demand and Peak Load

GEP Optimization for Each
Scenario
III.  METHODOLOGY
Optimal power plant
capacity combination The  process  of  the  research  is  illustrated  in  Fig  1.
Information required for this research includes predicted
Energy Mix and LCOE Calc energy  demand  and  peak  load  for  the  planning  period,
potential power plant and primary energy resources. Annual
energy demand and peak load as illustrated in Fig 2. The
End   information on the potential power plant options includes
Fig. 1. The Generation Expansion Planning Workflow  plant size, heat rate, maintenance rate, forced outage rate,
lifetime, investment cost, and operating costs, which are
|     | :  Demand in t period (MWh)               |     |     |     |     |                                    |     |     |     |     |     |
| --- | ----------------------------------------- | --- | --- | --- | --- | ---------------------------------- | --- | --- | --- | --- | --- |
| F   |                                           |     |     |     |     | presented in Table I [28], [29].   |     |     |     |     |     |
| L   | :  Max Number of generator g that can be  |     |     |     |     |                                    |     |     |     |     |     |
A built  The study in this paper uses the Java Bali system as a
TUPQRE
  :  Peak load (MW)  system  test,  which  is  the  largest  electricity  system  in
X
O[   :  Reserve margin (%)  Indonesia. In this paper, a comparison of GEP results from
normal conditions with a delay scenario is carried out. The
\]
TABLE I. POWER PLANT CANDIDATE DATA [28],[29]
|     | Heat  |     |     |     | Technical  |     |     |     |     |     |     |
| --- | ----- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- |
Maintenance   FOR  Investment Cost  Fixed O&M Cost  Variable O&M Cost
Type  Rate  Rate (%)  (%)  Lifetime  ($/kWe)  ($/kWe/y)  ($/MWh)
|             | (GJ/MWh)  |       |        |     | (years)  |     |        |     |        |     |       |
| ----------- | --------- | ----- | ------ | --- | -------- | --- | ------ | --- | ------ | --- | ----- |
| Gas         |           | 8.37  | 2.88   | 3   | 25       |     | 800    |     | 18     |     | 1     |
| Hydro       |           | -     | 11.51  | 4   | 50       |     | 2,000  |     | 6.6    |     | 1     |
| Biomass     |           | 9     | 11.51  | 7   | 25       |     | 1,700  |     | 47.6   |     | 3     |
| Wind        |           | -     | 0.31   | 3   | 27       |     | 1,500  |     | 39.55  |     | 0.8   |
| Solar       |           | -     | 5      | 5   | 25       |     | 790    |     | 24.7   |     | 0.4   |
| Coal        |           | 9     | 11.51  | 7   | 30       |     | 1,650  |     | 45.3   |     | 0.13  |
| Geothermal  |           | 4.32  | 7.67   | 10  | 30       |     | 4,000  |     | 65     |     | 0.37  |
TABLE II. EXISTING POWER PLANT DATA (IN MW)
Existing Gen  2021  2022  2023  2024  2025  2026  2027  2028  2029  2030
Hydro PP  2,615  2,615  2,615  2,615  2,615  2,615  2,615  2,615  2,615  2,615
Mini Hdro PP  150  150  150  150  150  150  150  150  150  150
Geothermal PP  1225  1225  1225  1225  1225  1225  1225  1225  1225  1225
Gas PP  1,467  1,467  1,467  1,467  1,467  1,467  1,467  1,467  1,467  1,467
CCGT  9,477  8,014  6,929  6,929  6,929  6,929  6,929  6,929  6,929  6,929
Gas Machine  182  182  182  182  182  182  182  182  182  182
|     | Diesel  |     | 152  | 152  | 152  152  | 152  | 152  | 152  152  | 152  152  |     |     |
| --- | ------- | --- | ---- | ---- | --------- | ---- | ---- | --------- | --------- | --- | --- |
Coal  22,479  22,479  22,479  22,479  22,479  22,479  22,479  22,479  22,479  22,479
Coal with HSD  927  927  927  927  927  927  927  927  927  0
|     | Biomass  |     | 5   | 5   | 5  5    | 5   | 5   | 5  5    | 5  5    |     |     |
| --- | -------- | --- | --- | --- | ------- | --- | --- | ------- | ------- | --- | --- |
|     | Waste    |     | 15  | 15  | 15  15  | 15  | 15  | 15  15  | 15  15  |     |     |
|     | Excess   |     | 3   | 3   | 3  3    | 3   | 3   | 3  3    | 3  3    |     |     |

95
Authorized licensed use limited to: UNIVERSITY OF BIRMINGHAM. Downloaded on October 28,2025 at 15:18:24 UTC from IEEE Xplore.  Restrictions apply.

2023 15th International Conference on Information Technology and Electrical Engineering (ICITEE)
TABLE III. POWER PLANT CANDIDATE
  2021  2022  2023  2024  2025  2026  2027  2028  2029  2030
|     |     | Hydro PP       |     | 110         | 0  0      | 0    | 0     | 50    | 0    | 0  0      | 0     |     |
| --- | --- | -------------- | --- | ----------- | --------- | ---- | ----- | ----- | ---- | --------- | ----- | --- |
|     |     | Coal PP        |     | 4215        | 924  0    | 0    | 1660  | 1660  | 0    | 0  0      | 0     |     |
|     |     | Geothermal PP  |     | 0           | 0  130    | 65   | 330   | 265   | 55   | 190  75   | 805   |     |
|     |     | PV PP          |     | 0           | 145  235  | 550  | 1240  | 110   | 140  | 140  140  | 140   |     |
|     |     | Waste          |     | 9           | 5  0      | 35   | 183   | 0     | 0    | 0  0      | 0     |     |
|     |     | Mini Hydro     |     | 45          | 38  144   | 102  | 76    | 12    | 0    | 0  0      | 0     |     |
|     |     | Wind PP        |     | 0           | 0  0      | 160  | 100   | 0     | 0    | 0  0      | 0     |     |
|     |     | PS             |     | 0           | 0  0      | 0    | 1040  | 0     | 0    | 943  760  | 1000  |     |
|     |     | CCGT           |     | 2110  1279  | 200       | 0    | 100   | 0     | 0    | 0  0      | 0     |     |
TABLE IV. DELAY AND SUCCESS RATIO
|     |      |     | Hydro PP  |      |      | Wind PP  |     |       |      | Biomass  |       |     |
| --- | ---- | --- | --------- | ---- | ---- | -------- | --- | ----- | ---- | -------- | ----- | --- |
|     | %SR  |     | %DR       | %F   | %SR  | %DR      |     | %F    | %SR  | %DR      | %F    |     |
|     | 75%  |     | 33%       | 25%  | 0%   | 0%       |     | 100%  | 0%   | 0%       | 100%  |     |
%SR : Success Ratio
|     |     | Geothermal  |     |     |     | PV PP  |     |     |     |     |     |     |
| --- | --- | ----------- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- |
%DR : Delay Ratio
%F : Project Failure Percentage
|     | %SR  |     | %DR  | %F   | %SR  | %DR  |     | %F    |     |     |     |     |
| --- | ---- | --- | ---- | ---- | ---- | ---- | --- | ----- | --- | --- | --- | --- |
|     | 19%  |     | 33%  | 81%  | 0%   | 0%   |     | 100%  |     |     |     |     |

delay scenario is divided into 3 scenarios, namely 1 year  MW in 2025, Geothermal PP 330 MW in 2025 and 265 in
delay, 3 years, and 5 years. The delay is applied to renewable  2026, as well as wind PP 160 MW in 2024 and 100 MW in
energy plants that have a failure ratio, such as PV PP, Wind  2025, resulting in changes to the power plants composition in
PP, and Geothermal PP. Existing generating capacity data  the Java Bali System.
can be seen in Table II and the planning power plant in Table  In the base case scenario, the total generating capacity in
III. Success ratio and delay ratio data can be seen in Table IV.  the Java Bali system in 2030 is 60.41 GW. By considering
the delay aspect of the power plant construction project, the
IV.  RESULTS AND DISCUSSION
result is that the system will build additional power plants to
The addition of power plant capacity, both VRE PP and  be able to substitute for the power plants shortfall. In this
research, the power plants that can replace the shortage of
conventional PP, has an impact on energy supply in the Java
Bali System. This section will present and discuss the impact  power plant capacity is assumed to be a gas generator or gas
of  VRE  PP  delays  on  the  composition  of  power  plant  machine. The choice of this type of generator considers
relatively fast supply, both conventional and Mobile Power
capacity, energy mix, and LCOE.
Plant (MPP). The results of plant planning for the base case
| A. Impact  | of  | Power  | Plant  | Project  Delay  | on  Capacity  |     |     |     |     |     |     |     |
| ---------- | --- | ------ | ------ | --------------- | ------------- | --- | --- | --- | --- | --- | --- | --- |
Composition
Based on research that has been done, taking into account
| the delays in PV PP 550 MW generators in 2024 and 1240  |     |     |     |     |     |     |     | 16% |     |     |     |     |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
14%
|     | TABLE V. POWER PLANT TOTAL CAPACITY  |     |     |     |     |     |     | 12% |     |     |     |     |
| --- | ------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
)%( xiM ygrenE
|       | Base Case  |     | Scenario 1- | Scenario 3- | Scenario 5- |     |     | 10% |     |     |     |     |
| ----- | ---------- | --- | ----------- | ----------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
|       |            |     | year        | year        | year        |     |     | 8%  |     |     |     |     |
|       |            |     | Delayed     | Delayed     | Delayed     |     |     |     |     |     |     |     |
| 2021  | 45,186.00  |     | 45,186.00   | 45,186.00   | 45,186.00   |     |     | 6%  |     |     |     |     |
4%
| 2022  | 47,577.00  |     | 47,577.00  | 47,577.00  | 47,577.00  |     |     |     |     |     |     |     |
| ----- | ---------- | --- | ---------- | ---------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
2%
| 2023  | 48,286.00  |     | 48,286.00  | 48,286.00  | 48,286.00  |     |     |     |     |     |     |     |
| ----- | ---------- | --- | ---------- | ---------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
0%
2024  49,197.90  48,487.90  48,487.90  48,487.90  2021202220232024202520262027202820292030
|       |            |     |            |            |            |     |     |     |     | Gas Mix RE Mix |     |     |
| ----- | ---------- | --- | ---------- | ---------- | ---------- | --- | --- | --- | --- | -------------- | --- | --- |
| 2025  | 53,926.90  |     | 52,966.90  | 52,256.90  | 52,256.90  |     |     |     |     |                |     |     |

Fig. 3. Java Bali System Gas Mix Vs RE Mix
| 2026  | 56,164.00  |     | 57,569.00  | 55,899.00  | 55,899.00  |     |     |     |     |     |     |     |
| ----- | ---------- | --- | ---------- | ---------- | ---------- | --- | --- | --- | --- | --- | --- | --- |

2027  56,218.90  56,483.90  56,928.90  56,218.90  TABLE VI. JAVA BALI SYSTEM LCOE
2028  57,491.90  57,491.90  59,161.90  57,491.90  Scenario 1- Scenario 3- Scenario 5-
|       |            |     |            |            |            |     |     |     | Base Case  | year     | year     | year     |
| ----- | ---------- | --- | ---------- | ---------- | ---------- | --- | --- | --- | ---------- | -------- | -------- | -------- |
| 2029  | 58,466.90  |     | 59,066.90  | 59,331.90  | 59,776.90  |     |     |     |            |          |          |          |
|       |            |     |            |            |            |     |     |     |            | Delayed  | Delayed  | Delayed  |
LCOE
2030  60,411.80  61,311.80  61,611.80  63,281.80  7.7  7.9  8  8,1
(c$/kWh)
|     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
96
Authorized licensed use limited to: UNIVERSITY OF BIRMINGHAM. Downloaded on October 28,2025 at 15:18:24 UTC from IEEE Xplore.  Restrictions apply.

2023 15th International Conference on Information Technology and Electrical Engineering (ICITEE)
scenario and delay scenario will produce a plant composition PLN (Persero) 2021-2030.,” Rencana Usaha Penyediaan Tenaga
as in Table V. List. 2021-2030, pp. 2019–2028, 2021.
[4] H. T. Nguyen and F. A. Felder, “Generation expansion planning
To anticipate the delay in the construction of RE power
with renewable energy credit markets: A bilevel programming
plants, as indicated by the research findings, there is a need approach,” Appl. Energy, vol. 276, no. June, p. 115472, 2020, doi:
for the substitution of power plants capacity. The results 10.1016/j.apenergy.2020.115472.
show the establishment of up to 1000 MW gas machines in [5] D. Z. Fitiwi, M. Lynch, and V. Bertsch, “Enhanced network effects
and stochastic modelling in generation expansion planning:
the scenario of a 1-year delay and up to 1800 MW gas
Insights from an insular power system,” Socioecon. Plann. Sci.,
machine in the scenarios of 3 and 5-year delays. These 1000 vol. 71, no. April, p. 100859, 2020, doi:
MW and 1800 MW gas machines are intended to 10.1016/j.seps.2020.100859.
accommodate the delay in RE power plants amounting to [6] G. S. Seck, V. Krakowski, E. Assoumou, N. Maïzi, and V.
Mazauric, “Embedding power system’s reliability within a long-
2645 MW, including PV PP, Geothermal PP, and Wind PP.
term Energy System Optimization Model: Linking high renewable
The delay in these power plants results in an increase in the energy integration and future grid stability for France by 2050,”
installed capacity in the Java Bali system from 60.41 GW to Appl. Energy, vol. 257, no. July 2019, p. 114037, 2020, doi:
up to 63.28 GW. 10.1016/j.apenergy.2019.114037.
[7] A. Z. Khan, S. Yingyun, and A. Ashfaq, “Generation expansion
B. Energy Mix and LCOE planning considering externalities for large scale integration of
renewable energy,” 2014 IEEE Int. Conf. Intell. Energy Power
Based on the installed capacity, changes in the energy mix Syst. IEPS 2014 - Conf. Proc., pp. 135–140, 2014, doi:
in the Java Bali system are obtained. This change primarily 10.1109/IEPS.2014.6874165.
[8] Q. Chen, C. Kang, Q. Xia, and J. Zhong, “Power generation
occurs in the RE mix, which experienced construction delays,
expansion planning model towards low-carbon economy and its
resulting in an increase in the gas energy mix. The results
application in china,” IEEE Trans. Power Syst., vol. 25, no. 2, pp.
indicate a decrease in the RE energy mix when PV PP 1117–1125, 2010, doi: 10.1109/TPWRS.2009.2036925.
delayed year in 2024, as shown in Fig. 3. This can occur due [9] W. Shengyu, C. Lu, Y. Xiaoqing, and Y. Bo, “Long-term
generation expansion planning under uncertainties and
to the delayed PV PP up to 1810 MW.
fluctuations of multi-type renewables,” Int. Conf. Power Eng.
With changes in power plants capacity and energy mix, the
Energy Electr. Drives, vol. 2015-Septe, pp. 612–616, 2015, doi:
Java Bali electrical system experiences a shift in the LCOE 10.1109/PowerEng.2015.7266387.
of generation. As shown in Table VI, the LCOE will increase [10] T. Luz, P. Moura, and A. de Almeida, “Multi-objective power
generation expansion planning with high penetration of
from the base case of 7.7 c$/kWh to 8.1 c$/kWh in the delay
renewables,” Renew. Sustain. Energy Rev., vol. 81, no. November
scenario. This LCOE does not consider the unavailability of
2016, pp. 2637–2643, 2018, doi: 10.1016/j.rser.2017.06.069.
LNG, which would lead the Gas Machine to use more [11] S. Pereira, P. Ferreira, and A. I. F. Vaz, “Generation expansion
expensive HSD (High-Speed Diesel), potentially causing a planning with high share of renewables of variable output,” Appl.
Energy, vol. 190, pp. 1275–1288, 2017, doi:
further increase in the LCOE.
10.1016/j.apenergy.2017.01.025.
V. CONCLUSION
[12] Y. Y. Rady, M. V. Rocco, M. A. Serag-Eldin, and E. Colombo,
“Modelling for power generation sector in Developing Countries:
Based on the research findings, it can be determined that
Case of Egypt,” Energy, vol. 165, pp. 198–209, 2018, doi:
delays in power plants project, such as RE PP, can influence
10.1016/j.energy.2018.09.089.
the capacity planning and the LCOE of the system. This study [13] E. M. F. Shinwari, “Optimization Model using WASP-IV for
focuses on the delays in RE such as PV PP, Geothermal PP, Pakistan’s Power Plants Generation Expansion Plan,” IOSR J.
Electr. Electron. Eng., vol. 3, no. 2, pp. 39–49, 2012, doi:
and Wind PP. The extent of the delay in capacity refers to the
10.9790/1676-0323949.
success ratio, delays, and achievements of the power plant
[14] A. Malik and C. Kuba, “Power Generation Expansion Planning
projects. Delayed VRE PP up to 2 GW, and based on the Including Large Scale Wind Integration: A Case Study of Oman,”
results, it was found that these generators would be Wind Resour. Futur. Energy Secur., vol. 2013, pp. 51–68, 2015,
doi: 10.1201/b18529-5.
substituted with Gas Machines up to 2000 MW. This affects
[15] J. G. Wright, T. Bischof-Niemz, J. R. Calitz, C. Mushwana, and R.
the LCOE of the system, increasing it from 7.7 c$/kWh to up
van Heerden, “Long-term electricity sector expansion planning: A
to 8.1 c$/kWh. This LCOE calculation does not yet account unique opportunity for a least cost energy transition in South
for the unavailability of LNG, which would lead the Gas Africa,” Renew. Energy Focus, vol. 30, no. September, pp. 21–45,
2019, doi: 10.1016/j.ref.2019.02.005.
Machine to utilize more expensive HSD (High-Speed
[16] I. Khan, “Power generation expansion plan and sustainability in a
Diesel), potentially causing a further increase in the LCOE.
developing country: A multi-criteria decision analysis,” J. Clean.
Moreover, the impact of these delays appears to be Prod., vol. 220, pp. 707–720, 2019, doi:
relatively small, due to the limited utilization of VRE. This 10.1016/j.jclepro.2019.02.161.
[17] R. Shirley and D. Kammen, “Energy planning and development in
situation might differ if delays occurred in base load power
Malaysian Borneo: Assessing the benefits of distributed
plants such as Coal PP, Hydro PP, and Biomass PP.
technologies versus large scale energy mega-projects,” Energy
Therefore, further studies are needed to assess the impact of Strateg. Rev., vol. 8, pp. 15–29, 2015, doi:
base load generators on the energy mix, LCOE, and 10.1016/j.esr.2015.07.001.
[18] K. I. Muttaqien, “Perencanaan Pengembangan Pembangkit Sistem
emissions.
Jawa-Bali Menggunakan Model Optimasi OSeMOSYS,”
Universitas Gadjah Mada, Yogyakarta, 2017.
REFERENCES
[19] T. I. Putrisia, “Perencanaan Sistem Pembangkitan untuk Wilayah
[1] Kementerian Hukum dan Hak Asasi Manusia, UU No.16 Tahun Sulawesi dengan Menggunakan OSeMOSYS,” Universitas
2016 Tentang Pengesahaan Paris Agreement to The United Gadjah Mada, 2017.
Nations Framework Convention on Climate Change. Indonesia, [20] R. F. S. Budi, “Optimasi Pengembangan Pembangkit Sistem
2016. Kelistrikan Jawa-Madura-Bali Menggunakan Game Theory :
[2] Sekretariat Jenderal Dewan Energi Nasional (DEN), Bauran Multi-Period Framework, Bi-Level, dan Multi-Objective
Energi Nasional. 2020. Optimization Method,” Universitas Gadjah Mada, Yogyakarta,
[3] PLN, “Rencana Usaha Penyediaan Tenaga Listrik (RUPTL) PT 2017.
97
Authorized licensed use limited to: UNIVERSITY OF BIRMINGHAM. Downloaded on October 28,2025 at 15:18:24 UTC from IEEE Xplore. Restrictions apply.

2023 15th International Conference on Information Technology and Electrical Engineering (ICITEE)
[21] Tumiran, Sarjiya, L. M. Putranto, A. Priyanto, and I. Savitri, 10.3390/su14053032.
“Generation expansion planning for high-potential hydropower [26] Sarjiya, R. F. S. Budi, and L. P. Multanto, “Achieving new and
resources : The case of the Sulawesi electricity system,” Int. J. renewable energy target: A case study of java-bali power system,
Sustain. Energy Plan. Manag., vol. 28, no. 2, pp. 37–52, 2020. Indonesia,” 2020 2nd Int. Conf. Smart Power Internet Energy Syst.
[22] A. A. Muthahhari et al., “Long-Term Generation Expansion SPIES 2020, pp. 560–565, 2020, doi:
Planning in Sulawesi Electricity System Considering High Share 10.1109/SPIES48661.2020.9242984.
of Intermittent Renewable Energy Resource,” 2019 11th Int. Conf. [27] M. R. Kresnawan, I. A. Safitri, and I. Darmawan, “Long term
Inf. Technol. Electr. Eng., 2019. projection of electricity generation sector in east kalimantan
[23] A. A. Muthahhari et al., “Environmental Considerations in Long- province: LEAP model application,” Proc. - 12th SEATUC Symp.
Term Generation Expansion Planning with Emission Limitations: SEATUC 2018, no. 1, pp. 1–5, 2018, doi:
An Analysis of the Sulawesi Power System in Indonesia,” 10.1109/SEATUC.2018.8788875.
Proceeding - 1st FORTEI-International Conf. Electr. Eng. [28] Ministry of Energy and Mineral Resources; Danish Energy
FORTEI-ICEE 2020, pp. 29–34, 2020, doi: 10.1109/FORTEI- Agency, “Technology Data for the Indonesian Power Sector,” no.
ICEE50915.2020.9249863. February, pp. 1–215, 2021, [Online]. Available:
[24] Tumiran et al., “Potential of Biomass as RE Source for Sustainable https://ens.dk/sites/ens.dk/files/Globalcooperation/technology_da
Electricity Supply in Eastern Indonesia,” 2021 3rd Int. Conf. High ta_for_the_indonesian_power_sector_-_final.pdf.
Volt. Eng. Power Syst. ICHVEPS 2021, pp. 022–027, 2021, doi: [29] Pusat Kajian LKFT Universitas Gadjah Mada (LKFT Study Center
10.1109/ICHVEPS53178.2021.9601067. Universitas Gadjah Mada), “Kajian Pengembangan Interkoneksi
[25] Tumiran, L. M. Putranto, Sarjiya, F. D. Wijaya, A. Priyanto, and Sistem Kelistrikan Nusa Tenggara dan Potensi Energi
I. Savitri, “Generation Expansion Planning Based on Local Terbarukan,” Yogyakarta, 2023.
Renewable Energy Resources: A Case Study of the Isolated
Ambon-Seram Power System,” Sustain., vol. 14, no. 5, 2022, doi:
98
Authorized licensed use limited to: UNIVERSITY OF BIRMINGHAM. Downloaded on October 28,2025 at 15:18:24 UTC from IEEE Xplore. Restrictions apply.
