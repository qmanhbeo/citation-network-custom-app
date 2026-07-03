AI & SOCIETY (2025) 40:4655–4670
https://doi.org/10.1007/s00146-025-02181-5
OPEN FORUM
AI metrics and policymaking: assumptions and challenges
in the shaping of AI
Konstantinos Sioumalas‑Christodoulou1 · Aristotle Tympas1
Received: 12 September 2024 / Accepted: 10 January 2025 / Published online: 13 February 2025
© The Author(s) 2025
Abstract
This paper explores the interplay between AI metrics and policymaking by examining the conceptual and methodological
frameworks of global AI metrics and their alignment with National Artificial Intelligence Strategies (NAIS). Through topic
modeling and qualitative content analysis, key thematic areas in NAIS are identified. The findings suggest a misalignment
between the technical and economic focus of global AI metrics and the broader societal and ethical priorities emphasized in
NAIS. This highlights the need to recalibrate AI evaluation frameworks to include ethical and other social considerations,
aligning AI advancements with the United Nations Sustainable Development Goals (SDGs) for an inclusive, ethical, and
sustainable future.
Keywords Artificial intelligence (AI) · AI metrics · AI policy · AI Governance · SDGs
1 Introduction
et al. 2021; Binns 2018). Lacking transparent algorithms,
users and regulators cannot fully understand or trust AI deci-
In today's complex and dynamic landscape, defined by sions, potentially leading to breaches in accountability when
the challenge of ‘existential risks’, informed and inclusive errors occur (Ali et al. 2024; Konstantis et al. 2023; Ananny
(Science and Technology) S&T policies are vital. Therein, and Crawford 2018). Furthermore, as AI systems increas-
measuring science and technology is pivotal in setting and ingly process large volumes of personal data, the respect for
determining realistic goals, aligning policy objectives with privacy remains a major concern that requires effective met-
tangible outcomes (Debackere et al. 2019). Especially rics to ensure AI systems uphold privacy standards and do
regarding artificial intelligence (AI), which is rapidly trans- not inadvertently become tools for surveillance (Golda et al.
forming almost all fields (Nature 2023). The metrics, how- 2024; Wachter et al. 2017). Equally important is the role of
ever, that AI-related policies are based on are, as we argue metrics in assessing the impact of AI in advancing the United
here, problematic. Nations Sustainable Development Goals (SDGs). Extensive
As AI becomes more integral to societal functions, the lack research underscores the need for detailed and robust met-
of appropriate metrics to evaluate critical dimensions of such rics to accurately evaluate AI's contributions to these goals.
integration can lead to significant oversight in S&T policy Without metrics that encompass global challenges, ethical
formulation and implementation. While metrics may effec- and social dimensions, the effectiveness of AI in supporting
tively measure AI advancements in terms of innovation, talent critical SDGs, such as climate action, health and well-being
competition and economy, they frequently overlook essen- and equity, cannot be fully realized (Liang et al. 2023; Rocchi
tial aspects like fairness, transparency, and privacy. Without et al. 2022; Chavarro et al. 2022; Gupta et al. 2021; Vinuesa
robust metrics to gage fairness and equity, AI could exacer- et al. 2020).
bate social disparities rather than ameliorate them (Mehrabi Recent studies emphasize the urgent need to ensure that
policies are in line with AI's transformative potential (Hine
and Floridi 2024; Ward et al. 2024; Bengio et al. 2023;
*
Konstantinos Sioumalas-Christodoulou
Nature 2020; Mishra et al. 2020). Current, however, policies
ksioumalas@phs.uoa.gr
heavily rely on inappropriate metrics, focusing on concepts
1 Department of History and Philosophy of Science, National like “competitiveness”, “innovation” and “talent competi-
and Kapodistrian University of Athens, 15772 Athens, tion” (Erkkilä 2023). This should raise serious concerns as
Greece
Vol.:(0123456789)

4 656 AI & SOCIETY (2025) 40:4655–4670
important AI policies inadequately consider indicators that did not represent an official NAIS.1 Hence, our final data-
highlight social and ethical considerations (Deloitte Insights set consists of 43 documents, each representing a country's
2023). Moreover, the challenge extends beyond metrics to NAIS. The dataset includes information about the NAIS’s
the translation of value-driven social/ethical considerations country of origin, time span (issuance and expiration dates),
into tangible policy actions, further emphasizing the need for and authorship (responsible governmental body).
recalibration. Policymakers are challenged to swiftly adapt The second phase pertains to the identification of exist-
their approaches to ensure alignment with AI's dynamic ing metrics (indicators) relating to AI, within the context
nature, addressing societal implications and potential biases of S&T policy. Upon reviewing the available literature, it
inherent in the current metrics-driven policymaking para- appears that there is currently no established national strat-
digm (Schiff 2023). egy that encompasses and publishes metrics related to AI.
Prompted by recent research advocating for responsi- However, highlighting the importance of this aspect, certain
ble AI metrics (Sadek et al. 2024; Minkkinen et al. 2024; institutional sectors have commenced the development of
Papyshev and Yarime 2024) and related studies exploring relevant initiatives (OECD 2024a), with dedicated research
nation-wide AI policy implications (Hine and Floridi 2024; centers issuing specialized reports on AI metrics that are
Hälterlein 2024; Papyshev and Yarime 2023; Foffano et al. viewed as valuable resources to evidence-based policymak-
2023; Saheb and Saheb 2023), our study seeks to delve ing (Perrault and Clark 2024). At the international level,
into the intricate relationship between AI metrics and AI novel global indices are crafted, specifically, for measuring
policy. To our knowledge, this is the first attempt to exam- AI: the Global AI Index (GAI), the Government AI Readi-
ine such an interplay. The objective of our own research ness Index (GAIRI), the Global Cities AI Readiness Index
is to explore how National Artificial Intelligence Strate- (GCAIRI), and the Artificial Intelligence and Democratic
gies (hereafter, “NAIS”) conceptualizes AI and examines Values Index (AIDVI). All the above indices explicitly aim
whether the current AI metrics at a global level are consist- at analyzing countries' AI readiness in a meaningful way
ent with these conceptualizations. Utilizing traditional topic while AIDVI further focuses on evaluating progress toward
modeling techniques (LDA) and qualitative content analysis trustworthy AI.
for obtaining the topics of NAIS and the existing global AI
2.2 Topic delineation and content analysis
metrics, this research sheds light on the intricate interplay
of AI metrics and policy.
To delineate the topics discussed in the totality of the NAIS
documents, we employ a mixed methods approach by com-
2 Methodology and data
bining qualitative content analysis with Latent Dirichlet
Allocation (LDA) topic modeling technique (Blei et al.
This section outlines the methodological framework 2003). LDA topic modeling has been extensively used in
employed in this study, detailing the processes for data col- literature, ranging from studying topic transition in social
lection, identifying topics within NAIS, and determining media platforms (Wang et al. 2012) to exploring topic evolu-
global AI metrics. For a visual representation of the entire tions within EU-funded research projects in social sciences
process, please refer to Fig. 3 in the Appendix. (Kropp and Larsen 2023). It is a standard, unsupervised
document classification technique that allows for an open
2.1 Data collection
interpretation of the obtained distribution of words. Qualita-
tive content analysis complements LDA topic modeling by
The first phase entails the identification and the corpus col- providing a nuanced understanding of the contextual and
lection of all the National Artificial Intelligence Strategies thematic dimensions embedded in the data (Schreier 2012).
(hereinafter “NAIS”). With an eye to constructing a com- Within the premises of this study, we conduct qualita-
prehensive dataset, the following four official databases and tive content analysis (coding and non-coding) approaches to
platforms were probed into: the OECD AI Policy Observa- complement and validate the LDA results, enabling a more
tory (OECD.AI 2024), the EU AI Watch Act (Van Roy et al. comprehensive exploration and detailed description of the
2021), the STIP Compass (STIP Compass 2024), and the AI identified topics. This approach was deliberately chosen to
Governance Database by Nesta (2024). Triangulating the address the known limitations of LDA's textual interpreta-
information from all databases, 53 countries have authored tion (Hagen 2018; Maier et al. 2021). The integration of
their NAIS policy documents. While processing the docu- qualitative and quantitative methodologies has proven
ments, we exclude several countries, namely Argentina,
Chile, Colombia, Thailand, Indonesia, and Latvia from the
analysis as the original documents’ text was either not writ- 1 For example, see here: https:// ai- watch. ec. europa. eu/ count ries/ switz
ten in the English language or the identified documentation erland/ switz erland- ai- strat egy- report_ en

AI & SOCIETY (2025) 40:4655–4670 4657
effective in policy research as demonstrated by Papyshev using NVivo software to examine findings and delve deeper
and Yarime (2023) and Isoaho et al. (2021). into the contextual characteristics of each topic. Nodes were
created to represent the LDA topics, populated with the key-
2.3 LDA topic modeling
words associated with each topic based on their probabil-
ity of occurrence (e.g., "talent", "skills", "program", "job"
In the initial phase, as the documents primarily pertain to etc. for "Human Capital"). Relevant passages in the NAIS
National Artificial Intelligence strategies, we anticipate a documents containing these keywords were identified and
comprehensive exploration of AI across various facets of a assigned to the respective topic nodes. Each passage was
nation’s caveat. As such, documents were divided into dis- manually reviewed to ensure contextual accuracy, verify-
tinct paragraphs for the purpose of conducting LDA. This ing that the keywords reflected the intended meaning of
process has previously been shown to outperform document- the topic rather than unrelated contexts. Generic concepts
level analysis (Du et al. 2012; van Berkel et al. 2020). Sec- representing key themes were explored in greater depth
ond, the raw corpus of all NAIS documents was processed, and keywords with broad meanings, such as "innovation,"
performing all the necessary sequential steps involved in "development," "ethics," "social," "infrastructure," "datum,"
data preprocessing, such as tokenization, stopword removal,2 and "investment," were carefully analyzed within their spe-
lemmatization, and vectorization. To extract the distribu- cific contexts. Through this process, codes were iteratively
tion of topics, we used unigrams, bigrams, and trigrams, refined and grouped into broader, more cohesive categories,
while we implemented the topic modeling within the Python ensuring a deeper understanding of the thematic structure.
(3.12.1) environment. While no additional topics emerged during this process,
In the application of LDA to analyze document collection, the analysis affirmed the comprehensiveness and reliability
hyperparameters alpha and eta were defined at values of 1 and of the LDA-derived topics and offered insights into their
0.01, respectively. We chose this setting to accommodate a description and functionality (see Findings section, Table 1
diverse array of topics within the corpus allowing for specific for the topics’ description).
words or vocabulary that appear to be more significant. These To identify which of the 15 topics were discussed in each
parameters influence the distribution of topics across documents NAIS document, we organized the documents by country,
and the distribution of words within the topics, aiming to capture assigning each document to a case node. Using topic nodes
distinct thematic elements with clarity. and contextual keywords derived during the validation step,
To ascertain the optimal number of topics for our analy- relevant passages were coded sequentially. The matrix cod-
sis, we conducted a systematic optimization of the coherence ing query tool was then employed to create a matrix that
score across a range of possible topic numbers from 2 to highlighted the presence of each topic across countries,
20. The coherence score measures the semantic similarity uncovering national patterns and variations in global AI
among the top words in each topic, indicating how mean- strategies.
ingfully the words are grouped. The optimization process Both the identification of topics and their presence across
revealed that the highest coherence score, recorded at 0.583, all NAIS countries were triangulated and validated through
was achieved with a configuration of fifteen topics. This out- a targeted, non-coding manual review of all 43 NAIS docu-
come suggests that seventeen (15) topics most effectively ments by the authors. This review ensured the appropriate-
represent the semantic structures within the data. Following ness of the topic titles, the comprehensiveness of the topics
the identification of these topics, the top 20 words from each discussed, and their contextual relevance within the policy
topic were extracted along with their respective weights, framework.
which signify the strength of association with the topic (for
2.5 Findings
details please refer to the Data Availability section, ‘topic
distribution of words.csv’).
2.5.1 AI topics
2.4 Qualitative content analysis
This section consists of two parts: the first part presents the
To validate and refine the 15 topics identified by LDA, the topics identified through the application of LDA in tandem
authors used a complementary qualitative analysis approach with the qualitative content analyses (both coding and non-
coding) conducted across the entirety of the NAIS. It also
highlights the presence and prominence of each topic across
countries, uncovering variations in global AI strategies. The
2 In addition, country names and subsequent adjectives related to ori-
second part introduces the current global AI metrics and
gin (e.g., Spain, Spanish), standard abbreviations and disproportion-
provides a critical analysis of the concepts they encom-
ally common terms such as “Artificial Intelligence”, “AI” or “strat-
egy” were removed from the documents’ corpus. pass. Finally, it evaluates their conceptual alignment with

4 658 AI & SOCIETY (2025) 40:4655–4670
Table 1 The topics discussed in the totality of NAIS documents
Topic Title Description
1 Research and Development (R&D) Research and development, from an academic and industry perspective
2 Innovation Strategy Framework for technological innovation, predominantly from a governmental standpoint
3 Public Sector Administration and service with a focus on citizens
4 Private Sector Business projects on development and investment prospects
5 Infrastructure Technologies related to public infrastructure
6 Data Governance Data, access and infrastructure
7 National Security Defense AI strategies
8 National Challenges AI-enabled solutions for societal issues (i.e., healthcare, agriculture, education)
9 Human Capital Measures aimed at attracting and growing AI talent
10 Socioeconomic Risks Diffusion, awareness, public trust
11 Ethical Framework Non-enforceable and non-binding value-based principles (i.e., inclusivity, diversity,
human rights)
12 Automation AI-driven automation, especially on the labor market
13 Regulation Legal frameworks, guidelines, and standards
14 Collaboration Cooperation and alliances on an international level
15 Alignment with Transnational Organizations Adherence to principles and recommendations by specific transnational organizations.
(i.e., EU, OECD, UN)
the identified NAIS topics, presenting their methodological Development Goals (SDGs) to ensure it benefits humanity
frameworks and data sources (see Table 3 in the Appendix and advances global development (OECD 2024b; United
section for further details). Nations 2022, European Commission 2019).
The following table (Table 1) describes the topics identi- In addition, a review of the existing literature reveals that
fied and discussed in the totality of NAIS topics: most topics identified in our research correspond directly
Most countries have authored their NAIS in 2019, with or conceptually with those explored in prior studies (Papy-
14 countries publishing their strategies this year. Other nota- shev and Yarime 2023; Saheb and Saheb 2023; van Berkel
ble years include 2020, with 11 countries, and 2021, with 8 et al. 2020). However, the topic that refers to the alignment
countries authoring their NAIS. Observing the data, there is of strategies with transnational organizations emerges as a
a small number of countries where the NAIS spans shorter distinct area of discussion (‘Alignment with Transnational
periods, such as 3 to 4 years; for example, Italy (2022–2024) Organizations’). This is further corroborated through both
and Denmark (2019–2022). In contrast, most of the strategies quantitative and qualitative analyses, identifying it as a dis-
last between 8 and 15 years. For instance, Malta’s strategy tinct topic that primarily reflects the European regions' focus
spans from 2019 to 2030, and China’s from 2017 to 2030. on regulatory and cooperative frameworks, which are closely
Noticeably, some countries have particularly long spans, such intertwined with both regional and international dynamics
as Czech Republic (2019–2035). In other countries, such as (see also Fig. 1). This distinction can likely be attributed
Canada, Poland, Luxembourg, and Lithuania, only the date to the broader scope of data and strategies analyzed in this
of the document’s issuance is provided without mentioning study, as well as the refined preprocessing steps undertaken,
the duration of the NAIS. By now, some countries (e.g., the which have enabled a more granular examination of these
USA, Germany, Norway, Austria, Estonia) have updated their unique thematic dimensions.
NAIS to reflect more recent developments and to be aligned
2.6 Discussion of topics
with their evolving national priorities.
It is to be noted that the majority of the topics identified
in these strategies are compatible with the recommenda- To assess the distribution of covered topics across different
tions and principles of transnational organizations, such as countries, we perform a qualitative content analysis. This
the OECD, the European Union, and the United Nations. involves delving into the totality of the NAIS and evaluating
Such principles on AI stress values like inclusive growth, whether each country has indeed established strategic objec-
sustainable development, human-centered values, fairness, tives or implemented specific tasks related to each topic. The
transparency, robustness, security, safety, and accountability, figure below (Fig. 1) reflects this analysis using a check mark
while focusing on ethical considerations, inclusivity, diver- to indicate countries that align with this criterion.
sity and trust, as well as aligning AI with the Sustainable

AI & SOCIETY (2025) 40:4655–4670 4659
Fig. 1 Distribution of topics in NAIS across countries (from most frequently to least frequently discussed)
Drawing from Fig. 1, the topics featured most frequently
across National AI Strategies (NAIS) are: Human Capi-
tal, Research and Development (R&D), Private Sector,
Data Governance, Regulation, Innovation Strategy, Ethical
Framework, Public Sector, Infrastructure, National Chal-
lenges, Socioeconomic Risks, Automation, Collaboration,
Alignment with Transnational Organizations, National
Security.
Below, the 15 topics are presented along with their
descriptions, complemented by insights derived from the
word cloud in Fig. 2. For further information regarding the
distribution of topics data, please refer to the link in the Data Fig. 2 Frequency of words (word cloud) in the totality of the NAIS
documents
Availability section.
‘Human Capital’: This is the most prominent topic
of NAIS, which relates to the development of AI talent measures to nurture and attract a skilled workforce. This
through educational programs, training initiatives, and talent concept is also reflected in the word cloud through terms

4 660 AI & SOCIETY (2025) 40:4655–4670
like "training", "skill", "talent" and "workforce" highlighting in the word cloud underlines the strategic role of AI in trans-
the focus on building human capacity for AI adoption and forming public services (Fig. 2).
growth (Fig. 2). ‘Infrastructure’: This topic features the investment in
‘R&D’: The second most discussed topic in NAIS is on digital infrastructure, such as high-performance comput-
Research and Development. It refers to funding schemes, ing, data centers, and network connectivity, to support AI
research centers, and academia-industry collaboration to development and deployment, with a focus on local lan-
drive innovation and technological advancement. Terms like guage data resources in smaller countries. This may be
"research", "development", and "investment" have a high reflected in terms, such as "infrastructure", "technology",
frequency in the word cloud underlining the significance of "network", and "investment" (Fig. 2).
R&D in fostering AI-driven technological progress (Fig. 2). National Challenges: This topic embodies addressing
‘Private Sector’: Another topic that receives equal atten- societal issues like healthcare, agriculture, education, and
tion is funding, accelerators, and technology support pro- smart cities through AI solutions, leveraging AI's potential
grams to encourage private companies in developing and to tackle pressing challenges and improve quality of life.
applying AI solutions, alongside facilitating dialog while Terms like "health", "education", "solution" and "field"
removing legal obstacles to foster innovation. Terms, such in the word cloud reflect this focus on using AI to tackle
as "business", "industry", and "company", point to the role pressing societal challenges (Fig. 2).
of private entities in shaping the AI landscape (Fig. 2). ‘Socioeconomic Risks’: This topic comprises evalu-
‘Data Governance’: This topic relates to policies and ating and mitigating risks associated with AI adoption,
mechanisms for data infrastructure development, including including awareness, trust, job displacement, inequality,
open data initiatives, data-sharing platforms, or regulatory and privacy concerns, through policies aimed at ensuring
frameworks that ensure responsible and ethical use of data in equitable access and distribution of AI benefits. This is
AI applications. Terms like "datum", "system", "platform", reflected in the word cloud terms "trust", "risk", "aware-
and "infrastructure" have a high frequency of occurrence ness" and "public" (Fig. 2).
signifying the critical role of data governance in enabling ‘Automation’: The topic involves exploring the impli-
AI systems (Fig. 2). cations of AI-driven automation on various industries and
‘Regulation’: Regulation of relevance to the development employment sectors, with a focus on re-skilling and re-
of legal frameworks, guidelines, and standards to regulate AI training initiatives to adapt to changing labor markets. The
technology, including risk assessment mechanisms, trans- word cloud terms "process", "change", "application" and
parency requirements and regulatory sandboxes to address "job" depict the concept of automation on the workforce
societal impacts and ensure accountability. The word cloud (Fig. 2).
terms "government", "regulation" and "standards" reflect the ‘Collaboration’: Among the less-discussed topics in
importance of this topic (Fig. 2). NAIS, related to engaging in international cooperation,
‘Innovation Strategy’: This topic consists of imple- participating in policy discussions, and sharing exper-
menting measures, such as pilot projects, innovation hubs, tise to foster a collaborative ecosystem for AI develop-
and procurement mechanisms, to stimulate innovation and ment. This is reflected in the word cloud terms "coopera-
adoption of AI technologies in the public sector. Terms, like tion", "international", "collaboration", and "engagement"
"innovation", "initiative", and "strategy”, highlight the rel- (Fig. 2).
evance of this topic (Fig. 2). ‘Alignment with Transnational Organizations’:
‘Ethical Framework’: This topic includes the devel- Another topic rarely touched upon in NAIS is that of align-
opment of ethical principles, codes of ethics, and ethics ing national AI strategies with the objectives and frame-
committees to govern AI technology, with an emphasis on works of transnational organizations like the European
values, such as transparency, diversity and inclusivity, to Commission, the OECD or the United Nations. The terms
address societal values and concerns. Terms like "value", "order", "framework", "global", and "European" reflect this
"diversity" and "human" in the word cloud align with the alignment of strategies with global frameworks (Fig. 2).
ethical considerations embedded in NAIS (Fig. 2). ‘National Security’: The least-discussed topic is that of
‘Public Sector’: This topic involves integrating AI tech- national security. It concerns addressing national security
nologies into public services through pilot projects, task concerns through investments in defense AI, cybersecu-
forces, and awareness-raising initiatives, while optimizing rity defense strategies, and military–civilian integration to
public administration. The prominence of terms, such as safeguard critical infrastructure and protect against emerg-
"government", "technology", "public sector", and "service", ing threats. Terms like "security", "risk", "critical", and
"national" underscore the relevance of this topic (Fig. 2).

AI & SOCIETY (2025) 40:4655–4670 4661
2.7 AI metrics For example, metrics that assess socio-economic risks or
ethical aspects of AI such as trust or gender diversity in AI,
In this section, we provide an overview of the available as well as regulatory or governance aspects including level
global AI indicators, exploring the dimensions underlying of data privacy legislation or participation in the interna-
each of them. Additionally, we identify the key concepts tional open data charter (‘Regulation’, ‘Data Governance’),
associated with these dimensions and conceptually link them carry the least weight (overall weight < 0.6) compared to
to the topics discussed in the NAIS. In total, four such indi- other "operating environment" indicators such as the cost of
cators related to AI have been identified: the Global AI Index getting the fastest visa processing for high-skilled tech work-
(GAI), the Global City AI Readiness Index (GCAIRI), the ers (‘Human Capital’). The former carries a significantly
Government AI Readiness Index (GAIRI) and the Artificial higher weight; approximately three times greater (overall
Intelligence and Democratic Values Index (AIDVI). weight = 1.5). This discrepancy highlights a critical aspect of
The table below (Table 2) outlines the focus (subject), how different factors within the "operating environment" and
composition (dimensions), and the producers of the indices, GAI in general are prioritized. It points out that the weight-
with the conceptually aligned topics with the NAIS indicated ing of indicators, such as trust in AI and gender diversity, is
in bold parentheses. relatively low, which suggests a lesser focus on these ethical
and socio-economic aspects. In contrast, more pragmatic
factors like visa processing for high-skilled workers are
2.7.1 GAI given higher priority, reflecting a more immediate economic
or operational concern for countries aiming to attract talent
The Global AI Index (GAI) produced by Tortoise Media in in the technology sector.
2019 assesses the national capacity for AI. It is updated in The innovation and investment pillars of the GAI focus on
an annual manner and structured around three main concep- R&D and commercial ventures, incorporate university rank-
tual pillars: implementation, innovation and investment. The ings (Times Higher Education, SCOPUS database), R&D
implementation pillar specifically includes sub-pillars, such spending, researcher counts (World Bank, UNESCO), and
as "talent", "infrastructure", and "operating environment", patents (GitHub, Google). Regulatory aspects are minimally
with the first two aligning closely with the NAIS topics of represented but acknowledged in the "development" sub-pil-
‘Human Capital’ and ‘Infrastructure’ (Tortoise Media 2024). lar, which includes countries’ participation in ISO AI stand-
The "talent" sub-pillar draws on LinkedIn data to meas- ardization efforts. Both pillars mirror the NAIS's emphasis on
ure AI professionals, programming language downloads (R fostering an environment conducive to technological advance-
and Python from CRAN and Google), GitHub activity, and ment and economic growth through ‘Innovation Strategy’ and
participation in AI-focused MOOCs (e.g., Amazon Alexa). ‘Private Sector’ involvement.
It also uses Meetup and Kaggle data to gage the AI commu- Overall, the emphasis on NAIS’s topics on ‘Human
nity's size and UNESCO data to count science, AI, and IT Capital’, ‘Infrastructure’, and ‘Innovation Strategy’ in GAI
graduates. The "infrastructure" pillar combines generic tech- framework receives heavier consideration compared to the
nological indicators from organizations like the OECD and societal and ethical issues. This highlights a pragmatic focus
World Bank with IT-specific metrics from private sources where immediate economic benefits and enhancements in
(ISP Review, Top500, Speedtest). technological capacity are prioritized. These areas are criti-
As regards the "operating environment" sub-pillar, cal as they directly impact a nation's ability to compete and
according to the defined methodology (Tortoise Media innovate in the rapidly evolving global AI landscape. Con-
2024), focuses on survey data that reflects public trust in versely, the lighter weighting of ethical considerations, such
Artificial Intelligence, diversity among practitioners, visa as inclusivity and the socio-economic impacts of AI, sug-
processing, and data governance as enabling factors. It eval- gests that these issues, while recognized, are not yet seen as
uates factors like talent competition (visa policies), gender immediately impactful to national competitiveness as the
diversity (UNESCO, Kaggle), trust (Ipsos MORI), open data more tangible technology-driven factors. This realization
(OECD), and data protection (UNCTAD). This sub-pillar might reflect an oversight in long-term strategic planning,
conceptually intersects with NAIS topics, such as ‘Human where the socio-ethical dimensions of AI, critical for sus-
Capital’, ‘Data Governance’, ‘Regulation’, and ‘Socioeco- tainable and equitable growth, are underemphasized.
nomic Risks’. However, when examining the more detailed
2.7.2 GCAIRI
"sub-sub-pillars" within the methodological framework used
to evaluate the AI operating environment, it becomes appar-
ent that these concepts/topics are not represented uniformly The Global Cities AI readiness index (GCAIRI) is updated
across the metrics. annually and assesses the cities’ AI readiness, is divided into
four conceptual categories called “vectors”, namely vision,

4 662 AI & SOCIETY (2025) 40:4655–4670
Table 2 Composition and structure of AI indices
Indices Subject Dimensions Producer
GAI National capacity for artificial intelligence 1.Implementation Tortoise Media
- Talent (Human Capital)
- Infrastructure (Infrastructure)
- Operating Environment (Human Capital,
Data Governance, Regulation, Socioeco-
nomic Risks, Ethical Framework)
2.Innovation
- Research, Development (R&D)
3. Investment
- Government strategy (Innovation Strategy)
- Commercial ventures (Private Sector)
GCAIRI Cities' AI readiness 1.Vision Oliver Wyman Forum
- Vision, Priorities, Mindset (Innovation Strat-
egy)
2. Activation
- Quality of life and Diversity (Human Capital)
- Demographic enablers (Public Sector)
- Legal and governmental enablers (Public Sec-
tor, Private Sector)
3. Asset base
- Companies (Private Sector)
- Workforce (Human Capital)
- Funding (R&D, Private Sector)
- Education and research (Innovation Strategy,
Human Capital)
- Infrastructure (Infrastructure)
4.Development and Trajectory
- Activation (development over time) (Public
Sector, Private Sector)
- Asset base (growth over time)
(Private Sector, R&D, Infrastructure)
GAIRI Government readiness to employ AI in public 1. Government Oxford Insights
services - Vision (Innovation Strategy)
- Governance and Ethics (Regulation)
- Digital capacity (Innovation Strategy, R&D,
Infrastructure)
- Adaptability
(Public Sector)
2. Technology Sector
- Maturity (Infrastructure)
- Innovation Capacity (Innovation Strategy,
Private Sector)
- Human Capital (Human Capital)
3. Data & Infrastructure
- Infrastructure (Infrastructure)
- Data availability (Data Governance)
- Data representativeness (Public Sector)
AIDVI Assess progress toward trustworthy AI 1. Frameworks for AI policy Center for AI and Digital Policy
- OECD/G20 AI Principles
- UNESCO Recommendation on the Ethics of
AI
(Alignment with Transnational Organiza-
tions)
2. Human Rights
- Universal Declaration for Human Rights
(Ethical Framework)
3. Democratic decision-making
- Public participation
- Access to policy documents
- Transparency
(Ethical Framework, Socioeconomic Risks)

AI & SOCIETY (2025) 40:4655–4670 4663
activation, asset base, development and trajectory (Oliver Largely, the Global Cities AI Readiness Index (GCAIRI)
Wyman Forum 2024). offers a framework for assessing urban AI readiness, primar-
The vision vector, specifically the “Vision, Priorities, ily emphasizing indicators centered around economy, inno-
Mindset” sub-pillar, evaluates how cities plan for techno- vation and human capital. However, this focus tends to side-
logical advancements, reflecting the NAIS's emphasis on line broader regulatory and ethical considerations essential
‘Innovation Strategy’. This assessment underlines the strate- for a sustainable AI ecosystem. In fact, the GCAIRI lacks
gic intentions of cities to harness AI technologies for future any dedicated AI-specific metrics and relies entirely on pre-
development. It further encompasses smart city plans, urban existing indicators related to good governance, economic
strategies, and economic development initiatives, supple- competitiveness, education, and innovation (Erkkilä 2023).
mented by data from the World Economic Forum. This emphasis, while vital, may obscure the importance of
In the activation vector, the focus is on the attractiveness inclusivity, regulation, and ethical frameworks, which are
and governance of urban spaces through three sub-vectors: crucial for cultivating an ethical and socially responsible AI
quality of life and diversity, demographic enablers, and legal environment. To truly benefit society, AI global indicators
and government enablers. The “quality of life and diver- should integrate a more holistic view that combines eco-
sity” metric (Mercer and UN data), particularly its diversity nomic growth with ethical governance and social well-being
aspect, evaluates urban inclusivity primarily through the lens (Foffano et al. 2023).
of immigration policies aimed at attracting high-skilled indi-
viduals, thus highlighting NAIS’s topic of ‘Human Capital’ 2.7.3 GAIRI
but with a limited scope on broader inclusivity measures.
“Demographic enablers” address wealth distribution, link- The Government AI readiness index (GAIRI) developed by
ing to NAIS’s ‘Public Sector’ topic by considering societal Oxford Insights is updated annually and assesses the govern-
equity. “Legal and government enablers”—building on the ment readiness to employ AI in public services. It consists
World Bank's Worldwide Governance Indicators and Doing of three “pillars”: government, technology sector, and data
Business rankings—signal existing rankings of good govern- & infrastructure (Oxford Insights 2024).
ance focusing on government effectiveness, ease of doing The government pillar covers the following four dimen-
business and intellectual property rights connecting to ‘Pub- sions: vision, government and ethics, digital capacity, and
lic Sector’, ‘Private Sector’, as well as ‘Regulation’. adaptability. Similar to the GCAIRI, the vision dimension
The objective of the asset base vector is to assess whether of GAIRI assesses the degree to which a country has for-
the city possesses the essential resources to realize its mulated a strategic plan for technological innovation. This
vision. The focal points are companies, workforce, fund- is primarily measured by the presence of a National AI
ing, education and research, and infrastructure. Inquiring Strategy (NAIS) and related initiatives. The data for this
about whether a city possesses "a reservoir of talent in col- dimension are derived from sources, such as the OECD
leges and universities, an educated workforce, high-quality AI Policy Observatory and the UN IDIR AI policy portal,
STEM education in primary and tertiary education, a track where countries’ published AI strategies are evaluated for
record for innovation and attracting pioneering companies, comprehensiveness, scope, and innovation focus. The con-
and the necessary infrastructure" (Oliver Wyman Forum ceptual framework of this dimension is fundamentally tied to
2024), aligns conceptually this dimension with the topics the NAIS topic that pertains to ‘Innovation Strategy’.
of ‘Human Capital’, ‘Research and Development (R&D)’, The government and ethics dimension encompasses met-
‘Innovation Strategy’, ‘Private Sector’, and ‘Infrastructure’. rics of data protection and privacy, cybersecurity, national
Once more, the prominence of ‘Human Capital’, ‘Innovation ethics, and legal frameworks, aligning closely with the
Strategy’, and the ‘Private Sector’ stands out compared to NAIS topic on ‘Regulation’. The digital capacity dimension
other topics, giving this "vector" a resemblance to the con- includes metrics related to government-supported innovation
cept of an "innovation ecosystem" while strongly reflecting initiatives promoting investment in emerging technologies,
the talent competition paradigm. IT infrastructure, and online services, which are relevant to
The "development and trajectory" vector, assessing changes the topics of ‘Research and Development (R&D)’, ‘Innova-
in city capabilities over recent years, indicates a progressive out- tion Strategy’, and ‘Infrastructure’. Data for this dimension
look yet remains confined to traditional metrics of economic and are drawn from the UN e-Government Survey, the World
governance effectiveness. It focuses on updates in government Bank GovTech Maturity Index, and the Network Readiness
effectiveness, the business environment, venture capital flows, Index. The adaptability dimension of the same pillar meas-
and infrastructure improvements, touching upon ‘Public Sector’, ures government effectiveness (sourced from the Worldwide
‘Private Sector’ as well as ‘Research and Development (R&D)’ Governance Indicators), responsiveness to change and e-pro-
and ‘Infrastructure’. curement capacity (Global Data Barometer), features related
to the ‘Public Sector’ topic. Similar to the development and

4 664 AI & SOCIETY (2025) 40:4655–4670
trajectory dimension of GCAIRI, this dimension focuses on diversity, transparency, and human rights. It should also con-
indicators that assess good governance. sider socio-economic factors like public awareness of AI and
The objective of the technology sector pillar is to assess trust in its applications.
the size of the sector that supplies governments with AI
technologies (maturity) but also its “innovation capacity” 2.7.4 AIDVI
and citizens' skill set (human capital). It's worth noting that
aside from the count of AI unicorns, the metrics employed The "Artificial Intelligence and Democratic Values Index”
are general evaluations of the IT sector. Similarly, the inno- (AIDVI) developed by the Center for AI and Digital Policy
vation capacity dimension concentrates on the factors foster- (CAIDP) is an annual assessment that focuses on promot-
ing innovation, encompassing entrepreneurial culture, and ing democratic values and human-centered policies in the
business administrative requirements. Such features mostly development and use of artificial intelligence. AIDVI aims
relate to the NAIS topics of ‘Innovation Strategy’, ‘Infra- to evaluate countries based on their progress toward trust-
structure’, ‘Private Sector’, and ‘Human Capital’. worthy AI, using criteria that emphasize transparency, fair-
The data and infrastructure pillar of GAIRI encompasses ness, accountability, and respect for fundamental rights. In
metrics concerning infrastructure, data availability, and data total, 12 factors/questions are included in the methodologi-
representativeness. Hence, this pillar is primarily associ- cal framework to assess national AI policies and practices.
ated with NAIS concepts concerning ‘Data Governance’ These factors are reflected in the following three dimensions
and ‘Public Sector’. Upon closer examination of the metric (CAIDP 2024): 1) well-known frameworks for AI policy (the
construction, it becomes evident that while the methodo- OECD/G20 AI Principles, UNESCO Recommendation on
logical approach regarding the infrastructure dimension is the Ethics of AI), 2) human rights (the Universal Declara-
straightforward, the other two dimensions, albeit linked to tion for Human Rights), and 3) democratic decision-making
AI,3 lack clarity and comprehensiveness. Specifically, the (transparency, public participation, and access to policy
notion of data availability for training AI models is confined documents).
to open government data and policies, statistical capacity, As regards the frameworks for AI policy, binary ques-
mobile phone and internet access coverage, thereby over- tions are employed to create metrics that assess the adoption
simplifying the concept of actual data generation, collection, and implementation of internationally recognized guide-
and dissemination as merely dependent on internet access lines, such as the OECD AI Principles and the UNESCO
and ownership of digital devices. Similarly, data representa- Recommendation on the Ethics of AI. These questions are
tiveness is evaluated solely based on gender disparities in specifically designed to gage whether national AI strate-
internet access and socio-economic disparities in internet gies align with these global standards, as outlined in the
usage and the ability to acquire an internet-enabled device. NAIS topic: ‘Alignment with transnational organizations’.
Overall, only 3 (three) of the 39 indicators in the Govern- Though endorsement alone in such questions is not sufficient
ment AI Readiness Index (GAIRI) are specifically tailored to determine country’s AI practices, such dimensions are in
to AI: (1) the presence of a national AI strategy (government line with the objective to promote trustworthy and respon-
pillar), (2) the number of AI Unicorns (technology sector sible artificial intelligence.
pillar), and (3) the number of AI-related research publica- Similar questions are posed for the endorsement and
tions (human capital pillar). While the index does address implementation of the Universal Declaration for Human
certain aspects relevant to AI policy, such as data availability Rights4 (‘Ethical Framework’). The authors note that
for AI model training and data representativeness, these are although the Declaration predates AI, it is expected to under-
treated superficially. Many metrics of GAIRI are adapted pin many upcoming policy debates due to its foundational
from conventional digital governance indices, which do not principles.
fully capture the unique challenges of AI. Furthermore, as In the third dimension of the index, which focuses on
highlighted by Erkkilä (2023), GAIRI's dependence on pre- democratic decision-making, there is a notable emphasis on
existing data underscores a continuity with traditional met- public participation in the development of AI policy. This
rics that evaluate competitiveness, innovation, and digital dimension incorporates metrics and questions that evaluate
governance. A comprehensive indicator intended to assess the extent to which AI policies are broadly disseminated
government readiness for AI should include factors that
evaluate the ethical dimensions of AI, such as inclusivity,
3 Issues pertaining to the data used to train AI algorithms, such as its 4 The one notable exception is Saudi Arabia which did not endorse
availability and representativeness of the population, are crucial for the UDHR but is a member of the United Nations and has recognized,
mitigating biases and addressing concerns, such as fairness, transpar- according to human rights organizations, certain human rights obliga-
ency, accountability and other ethical considerations. tions.

AI & SOCIETY (2025) 40:4655–4670 4665
and how principles, such as algorithmic transparency, fair- 3 Discussion and implications
ness, and accountability,5 are promoted. These elements
are crucial for ensuring that AI governance is transparent By examining the conceptual and methodological frame-
and inclusive. Moreover, these aspects are closely linked work of current global AI metrics and the way that AI is
to NAIS topics concerning the ‘Ethical Framework’ and conceptualized in National Artificial Intelligence Strate-
‘Socioeconomic Risks’, underscoring their importance in gies (NAIS), this research reveals a critical misalignment
shaping policies that govern AI. between the two. Despite the mentioning of ethical frame-
Here, unlike the GAIRI and GCAIRI, AIDVI specifically works and social considerations of AI within NAIS, global
includes AI-focused indicators, with 10 out of its 12 metrics AI metrics largely overlook these aspects. While global
directly related to AI aspects. However, the concept of trust- AI metrics heavily monitor the technical and economic
worthy and responsible AI, although encapsulated by a set aspects of AI, ethical and other social dimensions, such as
of critical yet broad questions, demands intensified scrutiny the impact on public services, legal and ethical adherence,
especially due to the rapid advancements in generative AI. and national sector-specific challenges, are significantly
The development of a comprehensive and robust method- underrepresented.
ological framework for constructing AI metrics necessitates Highlighting this gap, this study suggests that AI metrics,
a multifaceted approach spanning from conceptual nuances in their current form, may shape AI policies that prioritize
of trustworthiness and responsibility of and in AI (OECD technological innovation over societal and ethical concerns.
2024a, b; Perrault and Clark 2024; Salloum 2024; Schoe- This realization is critical, as what is being measured (and
nherr et al. 2023) to the inclusion of important dedicated how) significantly shapes the development of policies,
projects, databases, and initiatives that have been developed. which in turn influences societal functions (Muller 2018;
Notably, the OECD AI Incidents Monitor,6 which tracks Beer 2016; Espeland and Stevens 1998). The findings sup-
AI-related incidents to concretely identify and mitigate AI port the growing argument that responsible AI governance
risks, serves as a crucial tool for establishing trustworthy AI. demands metrics that integrate both technical aspects and
Similarly, the AI Incidents Database7 by the Partnership on ethical concerns, as emphasized in recent literature (Mink-
AI catalogs failures of AI systems to enhance transparency kinen et al. 2024; Papyshev and Yarime 2024; Schiff 2023;
and accountability. Such endeavors, coupled with significant Erkkilä 2023). Given the uncertainty surrounding AI’s rapid
academic contributions (Perrault and Clark 2024; Lin et al. evolution (Nordström 2022), such metrics must remain
2021; Dhamala et al. 2021; Gehman et al. 2020) are essential adaptable to both technological and societal changes and
in developing evaluation frameworks that comprehensively regularly monitored within a dynamic AI policy framework.
capture the intricacies of AI technologies and measure their ‘Human Capital’ is the topic that is prominently featured
trustworthiness and responsibility. This approach not only in almost all global indices. Recognizing the importance of
highlights the ongoing need for rigorous oversight mecha- talent and skills necessary for AI development, these indi-
nisms but also underlines the importance of global coop- ces evaluate educational frameworks, workforce capabilities,
eration in developing standards that can guide the ethical and the availability of skilled professionals in the field of AI,
deployment of AI systems worldwide. thereby reflecting a focus on enhancing the workforce to meet
the demands of AI-driven economies (Papyshev and Yarime
2023; Saheb and Saheb 2023; van Berkel et al. 2020). Topics,
such as ‘Innovation Strategy’, ‘Private Sector’, ‘Infrastructure’
and ‘Research and Development (R&D)’, receive substantial
attention across most global AI indices like the Global AI
5 The key questions considered for the construction of the relevant
Index, the Government AI Readiness Index and the Global
metrics are the following: (a) Has the country established a pro-
Cities AI Readiness Index (Schiff 2023; Erkkilä 2023). These
cess for meaningful public participation in the development of a
national AI Policy?, (b) are materials about the country’s AI policies indices assess national capacity for AI, focusing on aspects
and practices readily available to the public?, (c) Do the following like technological infrastructure, investment in AI technolo-
goals appear in the national AI policy: “Fairness,” “Accountability,”
gies, and innovation capacities, which are crucial for a coun-
“Transparency,” “Rule of Law,” “Fundamental Rights”?, (d) Has the
try’s competitiveness in AI.
country by law established a right to Algorithmic Transparency?
6 For more information refer to: https:// oecd. ai/ en/ incid ents? search_ On the other hand, topics concerning ethical and soci-
terms=%5 B% 5D& and_ condi tion= false & from_ date= 2014- 01- 01& etal dimensions of AI, such as ‘Public Sector’, ‘Regulation’,
to_ date= 2024- 05- 12& prope rties_ confi g=% 7B% 22pri ncipl es% 22:% ‘Data Governance’, ‘Ethical Framework’, ‘Socioeconomic
5B% 5D,% 22ind ustri es% 22:% 5B% 5D,% 22harm_ types% 22:% 5B%
Risks’ and ‘Alignment with Transnational Organizations’,
5D,% 22harm_ levels% 22:% 5B% 5D,% 22har med_ entit ies% 22:% 5B%
are notably underrepresented. This is particularly evident for
5D% 7D&o nly_ threa ts= false & order_ by= date& num_ resul ts= 20, and
here: https:// oecd. ai/ en/ catal ogue/ metri cs topics like ‘Ethical Framework’ and ‘Socioeconomic Risks’,
7 For further details see: https:// incid entda tabase. ai/

4 666 AI & SOCIETY (2025) 40:4655–4670
which are either assigned disproportionately low weights adequately reflect a country's performance and innovative
in indices, such as the Global AI Index (GAI), completely capacity. This limitation becomes even more pronounced
omitted from metrics like the Government AI Readiness with the rise of generative AI, which has unprecedented
Index (GAIRI) and the Global Cities AI Readiness Index potential in knowledge creation—spanning from authoring
(GCAIRI), or inadequately addressed due to deficient meth- scientific papers to generating entirely new forms of knowl-
odological frameworks in indices like the Artificial Intelli- edge (Feuerriegel et al. 2024; Goto and Katanoda 2023).
gence and Democratic Values Index (AIDVI). This indicates These capabilities challenge foundational concepts, such
a need for more robust and comprehensive approaches in the as transparency, originality, authenticity, and accountabil-
development and application of AI metrics that adequately ity (Hamed and Wu 2024; Picano 2024), raising profound
reflect these critical dimensions. questions about the evolving dynamics between human and
Other topics related to ‘Automation’, ‘Collaboration’, artificial roles. These challenges become even more signifi-
‘National Challenges’, and ‘National Security’, are absent cant when extrapolated in critical domains like education,
from global AI metrics. While AI-related automation has healthcare, and defense, wherein the interplay between
made significant strides, the full extent of its development, human autonomy, control, and oversight with AI dynam-
particularly in complex and unpredictable environments, has ics, carries far-reaching ethical, practical and vital implica-
yet to be realized. As regards ‘Collaboration’, such indices tions (Hadlington et al. 2024; Farina et al. 2024). Therefore,
often prioritize quantifiable data that can be uniformly meas- addressing AI's proper integration into society necessitates
ured and compared across countries, which makes the quali- a paradigm shift, one that embraces these complexities and
tative aspects of international collaborations challenging to acknowledges the distinctive capabilities and transformative
include in a standardized global indicator/ranking format. impact of AI.
The omission of 'National Challenges' perceived as AI-ena- A promising approach to addressing the complexities of
bled solutions for societal issues (i.e., healthcare, agricul- identifying, measuring, and monitoring AI's societal impact
ture, education) in global AI metrics is indeed a significant is to actively engage with society to gain a deeper under-
lack. Given the direct relevance of these challenges to the standing of its implications. This can be achieved by creating
Sustainable Development Goals (SDGs), there is a pressing dedicated platforms that systematically capture, analyze, and
need to develop indices that can specifically measure AI's monitor AI's influence on critical socio-economic sectors.
impact in these areas. Such metrics would not only demon- In view of this, initiatives like the “AI Incidents Monitor”
strate how AI contributes to solving societal issues but also (developed by the OECD, accessible at oecd.ai/incidents),
align AI developments with broader global objectives that the “AI Incident Database” (developed by Partnership on AI,
genuinely benefit humanity. 'National Security' is presum- accessible at incidentdatabase.ai), the “AI, Algorithmic, and
ably excluded due to the sensitive nature of defense-related Automation Incident and Controversy Repository” (devel-
data, which countries might not wish to disclose publicly. oped by the University of California, Berkeley, and accessi-
The analysis highlights a critical issue in the dynamics ble at aiaaic.org), and the “MITRE AI Incidents Repository”
of policy development: the over-reliance on traditional met- (developed by MITRE Corporation, mitre.org) exemplify
rics that are easy to measure rather than those that address efforts already underway. These repositories offer valuable
deeper, more meaningful objectives. This tendency to prior- insights into real-world AI incidents and hazards, provid-
itize measurable and immediate outcomes often skews poli- ing a strong foundation for developing metrics that assess
cies toward visible economic and technological benchmarks, AI's societal and sector-specific impacts across domains like
neglecting social outcomes. As a result, policies risk becom- healthcare, education, agriculture, defense, etc. while also
ing disproportionately shaped by what existing metrics can illuminating national/localization priorities and unique inte-
capture, creating a reinforcing cycle that prioritizes areas gration challenges faced by individual countries.
already well-represented in traditional indicators while leav- Considering the existential risks posed by AI, such
ing critical dimensions underexplored. approaches are essential for evaluating its impact on advanc-
Traditional metrics in science and technology further ing or potentially hindering progress toward the Sustain-
exemplify this limitation, often falling short in capturing able Development Goals (SDGs). They provide an evidence
the complexities and transformative potential of AI. For base for scrutinizing key issues including transparency (e.g.,
instance, conventional indicators such as the number of ensuring AI algorithms in healthcare diagnostics are inter-
AI-related scientific publications or patents may no longer pretable and auditable), ethical challenges (e.g., addressing

AI & SOCIETY (2025) 40:4655–4670 4667
biases in AI models used in education that could reinforce Through critical analysis, it contextualizes the insights of
existing inequalities), and risks (e.g., the environmental this research within the broader premises of studies focusing
impact of training large-scale AI models). In this context, the on NAIS priorities (Papyshev and Yarime 2023; Saheb and
role of civil society and public in general is pivotal. Public Saheb 2023) and those examining global AI metrics (Erkkilä
engagement enriches the construction of socially conscious 2023). In doing so, it introduces a framework for understand-
metrics and informs policy development, ensuring inclu- ing how national AI priorities can inform the creation of bal-
sivity and responsiveness to societal needs. The growing anced, context-sensitive metrics. This contribution enriches
recognition of society's role in AI governance has naturally ongoing debates about the transparency and accountability
expanded to influence the development of regulatory frame- in data-driven AI governance, emphasizing the necessity of
works. Perspectives like experimental and anticipatory regu- responsible metrics that align with societal needs and ethi-
lation reflect this shift, embedding public participation and cal imperatives (Papyshev and Yarime 2024; Schiff 2023;
engagement as fundamental components of the regulatory Charles et al. 2022).
process (Nesta 2024; CUP 2024). On an empirical level, this research identifies and exam-
This approach would disrupt the existing cycle by ensur- ines 15 topics across 43 NAIS documents, uncovering
ing a balanced representation of diverse topics within global national variations in strategic priorities. This study provides
AI metrics while fostering a more holistic, inclusive, and a comprehensive dataset that highlights both the gaps and
ethically grounded integration of AI, effectively translating overlaps between national strategies and global AI metrics.
value-driven social and ethical considerations into action- While not the primary focus of this research, the dataset
able policies (Schiff 2023; Foffano et al. 2023). offers opportunities for future studies to delve deeper into
In conclusion, there is a significant space for international individual countries' specific priorities. Such analyses could
bodies and national policymakers to refine AI evaluation reveal patterns in how certain strategic topics correlate with
frameworks to better reflect a comprehensive view of AI's specific metric outcomes, providing valuable insights for
impacts. This would entail a strategic recalibration of AI refining national AI evaluation frameworks.
metrics to encompass a broader spectrum of considerations, Third, this research provides actionable insights for
ensuring that AI development is aligned with both global policymakers and metric developers by advocating for the
standards and local societal needs. This recalibration is cru- integration of societal dimensions and public engagement
cial for promoting an AI future that is inclusive, ethical, and into AI evaluation frameworks (Foffano et al. 2023; Erkkilä
fully integrated into the fabric of global society. 2023; Wilson and Van Der Velden 2022). It underscores
that AI metrics should not only focus on technical and eco-
nomic outputs but also reflect the broader societal priorities
4 Contribution
outlined in NAIS. To this end, the development of special-
ized platforms for systematically capturing, analyzing, and
This study contributes to the understanding of the interplay assessing AI's impact on critical socio-economic sectors
between AI metrics and policymaking by addressing the would offer substantial value. Moreover, it lays the theoreti-
conceptual alignment between how AI progress is measured cal foundation for developing country-specific metrics that
and how it is framed in national policies. To our knowledge, align more closely with national priorities, enabling govern-
this is the first research effort to explore the intersection of ments to monitor the effectiveness of AI policies and meas-
global AI metrics and National AI Strategies (NAIS), pro- ure their impact on societal challenges, such as healthcare,
viding both empirical and theoretical insights. The analysis education, and sustainability.
reveals a critical misalignment between the global measure-
ment of AI progress and the policy objectives articulated in
national strategies, highlighting the need for more nuanced 5 Appendix
and comprehensive evaluation frameworks.
Theoretically, this study advances the understanding
See Table 3 and Fig. 3.
of AI governance by offering insights into bridging the
gap between policy intentions and measurable outcomes.

4 668 AI & SOCIETY (2025) 40:4655–4670
|                                                                                                              |  ,xednI ytirutaM hceTvoG ,knaB dlroW ,seigetarts IA lanoitaN |     |                                                     |  ycavirp atad lanoitaN ,weiveR PSI ,retrahC ataD nepO DCEO |                                                   |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------ | --- | --------------------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------- |
|  ,DCEO ,recreM ,knaB dlroW ,elggaK ,OCSENU ,nIdekniL -ocE dlroW ,stroper DCEO ,tsetdeepS ,005poT ,weiveR PSI | noitacudE rehgiH semiT ,OCSENU ,knaB dlroW ,SUPOCS           |     |                                                     |                                                            |                                                   |
|                                                                                                              |                                                              |     |  yciloP IA DCEO ,yevruS tnemnrevoG-e NU ,knaB dlroW | -adnemmoceR scihtE OCSENU ,selpicnirP IA 02G/DCEO          | -adnemmoceR scihtE OCSENU ,selpicnirP IA 02G/DCEO |
 noitazidradnats OSI ,retemoraB ataD labolG ,DATCNU
muroF namyW revilO ,sthgisnI drofxO ,aideM esiotroT
|     |     | DCEO ,elggaK ,atad NU ,recreM ,IROM sospI |     | sthgiR namuH fo noitaralceD lasrevinU ,noit |     |
| --- | --- | ----------------------------------------- | --- | ------------------------------------------- | --- |
srotacidnI ecnanrevoG ediwdlroW ,stroffe
yevruS tnemnrevoG-e NU ,muroF cimon
SUPOCS ,noitacudE rehgiH semiT
stroper GDS NU ,noit
secruos noitalsigel
yrotavresbO
secruoS ataD
atad NU
- - - -
|  ecnamrofrep-hgih ekil ssenidaer lacigolonhcet no gnisucof ,derevoc-lleW  elbatiuqe dna erutcurtsarfni larur ,revewoH .sretnec atad dna gnitupmoc |                                                                                                                                                                                                                    |  ,tsurt cilbup ,ytilauqeni no sucof cidarops htiw ,llarevo desserdda ylkaeW  spag gnivael ,htworg cimonoce ezitiroirp scirteM .tnemecalpsid boj dna |                                                                                                                                              |  selpicnirp IA tuoba snoitseuq daorb hguorht IVDIA ni desserdda ylkaeW  egarevoc decnaun skcal tub swal ycavirp dna ytilibaliava atad no sesucoF |  ,)OCSENU ,DCEO( skrowemarf labolg htiw tnemngila sthgilhgih IVDIA    |
| ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------- |
|  tnelat ,noitacude ecrofkrow gnizisahpme ,secidni lla ssorca sucof gnortS -tem ytivisulcni dna ytisrevid ,revewoH .gniniart METS dna ,noitcartta  |  dna noitaroballoc yrtsudni-aimedaca no gnisucof ,dezisahpme ylgnortS -nemid lacihte dna ecnaveler lateicos eht ,revewoH .stuptuo noitavonni  dna ytilibaniatsus koolrevo secidni eht ,revewoH .troppus tnemnrevog |  lacihtE .stnemtsevni dna ,noitavonni ,ssenidaer etaroproc fo noitaulavE                                                                            |  kcal ro dezisahpmerednu era scirtem ecnanrevog lacihtE .skrowemarf  ssenevisulcni dna ytilauq eht gnissessa ni htped kcal scirtem ,revewoH  | -lanigram rof ssecca atad elbatiuqe dna ,noitagitim saib ,ytilauq atad fo                                                                        |                                                                       |
|                                                                                                                                                   |                                                                                                                                                                                                                    |                                                                                                                                                     |  lagel dna ecnanrevog IA fo smret ni derusaem yliramirp si noitalugeR  .secivres tnemnrevog ni noitpoda IA no gnisucof ,detcefler yletaredoM |                                                                                                                                                  |  noitatnemelpmI .tnemesrodne fo scirtem yranib ot detimil si siht tub |
 skrowemarf yrotaluger no ylworran sesucof IAG .sthgir namuh dna
|     |  dna ,sbuh noitavonni ,stcejorp tolip no sisahpme htiw derevoc lleW | stfieneb cimonoce dnoyeb noitavonni fo tcapmi lateicos mret-gnol  IA rotces etavirp fo snoitacilpmi tekram robal dna snoitaredisnoc |     |     | dessessa yletauqedani era selpicnirp eseht ot ecnerehda lautca dna |
| --- | ------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | --- | --- | ------------------------------------------------------------------ |
secidni eseht ni detaroprocni ylerar era seitivitca D&R fo snois
sevitaitini ssenerawa cilbup ro secivres cilbup nevird-IA fo
scirtem rehto ot tcepser htiw dethgiewrednu era scir
IA lacihte fo stcapmi lateicos lacitcarp naht rehtar
|     | noitnetta elttil eviecer stfieneb IA fo noitubirtsid | noitpoda IA yb desop sksir lateicos gnitaulave ni |     |     |     |
| --- | ---------------------------------------------------- | ------------------------------------------------- | --- | --- | --- |
derevoc yllaminim era seitivitca
| secidnI ni noitcefleR |     |     | sthgisni elbanoitca |     |     |
| --------------------- | --- | --- | ------------------- | --- | --- |
seitinummoc dezi
secruos atad dna secidnI IA dengila ot scipot SIAN fo gnippaM  3 elbaT
- - - -
| IRIAG ,IRIACG ,IAG IRIAG ,IRIACG ,IAG | IRIAG ,IRIACG ,IAG IRIAG ,IRIACG ,IAG | IRIAG ,IRIACG ,IAG |     |     |     |
| ------------------------------------- | ------------------------------------- | ------------------ | --- | --- | --- |
IRIAG ,IRIACG
secidnI dengilA
|     |     | IAG ,IVDIA | IRIAG ,IAG | IAG ,IVDIA IRIAG ,IAG |     |
| --- | --- | ---------- | ---------- | --------------------- | --- |
IVDIA
- - - -
 tnempoleveD dna hcraeseR
-ansnarT htiw tnemngilA
|     |     | sksiR cimonoceoicoS |     |     | snoitazinagrO lanoit |
| --- | --- | ------------------- | --- | --- | -------------------- |
segnellahC lanoitaN
|     | ygetartS noitavonnI |     |     | krowemarF lacihtE |     |
| --- | ------------------- | --- | --- | ----------------- | --- |
ecnanrevoG ataD ytiruceS lanoitaN
latipaC namuH
| erutcurtsarfnI |     | rotceS etavirP | rotceS cilbuP |     | noitaroballoC |
| -------------- | --- | -------------- | ------------- | --- | ------------- |
noitamotuA
noitalugeR
)D&R(
cipoT

AI & SOCIETY (2025) 40:4655–4670 4669
Fig. 3 Methodology flowchart
showing the sequential steps
from data collection to critically
analyzing metrics and aligning
topics
Funding Open access funding provided by HEAL-Link Greece. This Chavarro D, Perez-Taborda JA, Ávila A (2022) Connecting brain and
research was supported by funding from the European Union under the heart: artificial intelligence for sustainable development. Scien-
projects Ethics4Challenges and Tethics Game. tometrics 127(12):7041–7060
Debackere K, Glänzel W, Thijs B (2019) Scientometrics shaping sci-
Data availability The data and code used for this study are available at: ence policy and vice versa, the ECOOM case. Springer Handbook
https://g ithub.c om/b audsi ou/A I-M etric s-a nd-P olicy makin g of Science and Technology Indicators, pp 447–464
Deloitte Insights (2023) The AI regulations that aren’t being talked
Declarations about. Available here: https://w ww2.d eloit te.c om/u s/e n/i nsigh ts/
indust ry/p ublic-s ector/a i-r egula tions-a round-t he-w orld.h tml
Conflict of Interest The authors have no competing interests. Dhamala J, Sun T, Kumar V, Krishna S, Pruksachatkun Y, Chang KW,
Gupta R (2021) Bold: Dataset and metrics for measuring biases
Open Access This article is licensed under a Creative Commons Attri- in open-ended language generation. In: Proceedings of the 2021
bution 4.0 International License, which permits use, sharing, adapta- ACM Conference on fairness, accountability, and transparency,
tion, distribution and reproduction in any medium or format, as long pp. 862–872
as you give appropriate credit to the original author(s) and the source, Du L, Buntine W, Jin H, Chen C (2012) Sequential latent Dirichlet
provide a link to the Creative Commons licence, and indicate if changes allocation. Knowl Inf Syst 31:475–503
were made. The images or other third party material in this article are Erkkilä T (2023) Global indicators and AI policy: metrics, policy
included in the article’s Creative Commons licence, unless indicated scripts, and narratives. Rev Policy Res 40(5):811–839
otherwise in a credit line to the material. If material is not included in Espeland WN, Stevens ML (1998) Commensuration as a social pro-
the article’s Creative Commons licence and your intended use is not cess. Ann Rev Sociol 24(1):313–343
permitted by statutory regulation or exceeds the permitted use, you will European Commission (2019) Ethics guidelines for trustworthy AI.
need to obtain permission directly from the copyright holder. To view a Available at: https://d igita l-s trate gy.e c.e uropa.e u/e n/l ibrar y/e th-
copy of this licence, visit http://creativecommons.org/licenses/by/4.0/. ics-g uidel ines-t rustw orthy-a i
Farina M, Lavazza A, Sartori G, Pedrycz W (2024) Machine learning
in human creativity: status and perspectives. AI & Soc 39:1–13
Feuerriegel S, Hartmann J, Janiesch C, Zschech P (2024) Generative
References ai. Bus Inf Syst Eng 66(1):111–126
Foffano F, Scantamburlo T, Cortés A (2023) Investing in AI for social
good: an analysis of European national strategies. AI & Soc
Ali AE, Venkatraj KP, Morosoli S, Naudts L, Helberger N, Cesar P 38(2):479–500
(2024) Transparent AI disclosure obligations: Who, What, When, Gehman S, Gururangan S, Sap M, Choi Y, Smith NA (2020) Realtox-
Where, Why, How. arXiv preprint arXiv:2 403.0 6823 icityprompts: Evaluating neural toxic degeneration in language
Ananny M, Crawford K (2018) Seeing without knowing: Limitations of models. arXiv preprint arXiv:2 009.1 1462
the transparency ideal and its application to algorithmic account- Golda A, Mekonen K, Pandey A, Singh A, Hassija V, Chamola V,
ability. New Media Soc 20(3):973–989 Sikdar B (2024) Privacy and security concerns in generative AI:
Beer D (2016) Metric power, vol 10. Palgrave Macmillan, London a comprehensive survey. IEEE Access. 12:48126–48144
Bengio Y, Hinton G, Yao A, Song D, Abbeel P, Harari YN, Minder- Goto A, Katanoda K (2023) Should we acknowledge ChatGPT as an
mann S (2023) Managing ai risks in an era of rapid progress. author? J Epidemiol 33(7):333–334
arXiv preprint arXiv:2 310.1 7688. Gupta S, Langhans SD, Domisch S, Fuso-Nerini F, Felländer A, Batt-
Binns R (2018) Fairness in machine learning: Lessons from political aglini M, Vinuesa R (2021) Assessing whether artificial intel-
philosophy. In: Conference on fairness, accountability and trans- ligence is an enabler or an inhibitor of sustainability at indicator
parency, pp. 149–159. PMLR level. Transport Eng 4:100064
CAIDP (2024) Artificial Intelligence Development and Vision Index. Hadlington L, Karanika-Murray M, Slater J, Binder J, Gardner S,
Available at: https://w ww.c aidp.o rg/r eport s/a idv-2 022/ . Accessed Knight S (2024) Public perceptions of the use of artificial intelli-
07 Aug 2024 gence in Defence: a qualitative exploration. AI & SOCIETY, 1–14
CUP (2024) Cambridge Forum on AI: Law and Governance. Experi- Hagen L (2018) Content analysis of e-petitions with topic modeling:
mental Regulation for AI Governance. Available at: https://w ww. How to train and evaluate LDA models? Inf Process Manage
cambri dge.o rg/c ore/j ourna ls/c ambri dge-f orum-o n-a i-l aw-a nd- 54(6):1292–1307
govern ance/a nnoun cemen ts/c all-f or-p apers/e xperi menta l-r egul Hamed AA, Wu X (2024) Detection of ChatGPT fake science with the
ation-f or-a i-g overn ance xFakeSci learning algorithm. Sci Rep 14(1):16231
Charles V, Rana NP, Carter L (2022) Artificial Intelligence for data- Hine E, Floridi L (2024) Artificial intelligence with American values
driven decision-making and governance in public affairs. Gov Inf and Chinese characteristics: a comparative analysis of American
Q 39(4):101742 and Chinese governmental AI policies. AI & Soc 39(1):257–278

4 670 AI & SOCIETY (2025) 40:4655–4670
Hälterlein, J (2024) Imagining and governing artificial intelligence: the Picano E (2024) Who is the author: genuine, honorary, ghost, gold, and
ordoliberal way—an analysis of the national strategy ‘AI made in fake authors? Explor Cardiol 2:88–96
Germany’. AI & SOCIETY, 1–12 Rocchi L, Ricciolini E, Massei G, Paolotti L, Boggia A (2022) Towards
Isoaho K, Gritsenko D, Mäkelä E (2021) Topic modeling and text anal- the 2030 Agenda: measuring the progress of the European Union
ysis for qualitative policy research. Policy Stud J 49(1):300–324 countries through the SDGs achievement index. Sustainability
Konstantis K, Georgas A, Faras A, Georgas K, Tympas A (2023) 14(6):3563
Ethical considerations in working with ChatGPT on a question- STIP Compass (2024) Stip Compass. Available at: https://s tip.o ecd.
naire about the future of work with ChatGPT. AI and Ethics, org/s tip/
1–10 Sadek M, Kallina E, Bohné T, Mougenot C, Calvo RA,Cave S (2024)
Kropp K, Larsen AG (2023) Changing the topics: the social sciences Challenges of responsible AI in practice: scoping review and rec-
in EU-funded research projects. Comp Europ Polit 21(2):176–207 ommended actions. AI & SOCIETY, pp 1–17
Liang D, Guo H, Nativi S, Kulmala M, Shirazi Z, Chen F, Jelinek Saheb T, Saheb T (2023) Topical review of artificial intelligence
T (2023) A future for digital public goods for monitoring SDG national policies: a mixed method analysis. Technol Soc
indicators. Sci Data 10(1):875 74:102316
Lin S, Hilton J, Evans O (2021) Truthfulqa: Measuring how models Salloum SA (2024) Trustworthiness of the AI. In: Al-Marzouqi A,
mimic human falsehoods. arXiv preprint arXiv:2 109.0 7958 Salloum SA, Al-Saidat M, Aburayya A, Gupta B (eds) Artificial
Maier D, Waldherr A, Miltner P, Wiedemann G, Niekler A, Keinert intelligence in education: The power and dangers of ChatGPT in
A, Adam S (2021) Applying LDA topic modeling in communica- the classroom, vol 144, pp 643–650. Springer Nature
tion research: Toward a valid and reliablemethodology. In: van Schiff DS (2023) Looking through a policy window with tinted
Atteveldt W, Peng Q (eds) Computational methods for communi- glasses: setting the agenda for US AI policy. Rev Policy Res
cation science, pp 13–38. Routledge 40(5):729–756
Mehrabi N, Morstatter F, Saxena N, Lerman K, Galstyan A (2021) A Schoenherr JR, Abbas R, Michael K, Rivas P, Anderson TD (2023)
survey on bias and fairness in machine learning. ACM Comput Designing AI using a human-centered approach: Explainability
Surv (CSUR) 54(6):1–35 and accuracy toward trustworthiness. IEEE Trans Technol Soc
Minkkinen M, Niukkanen A, Mäntymäki M (2024) What about 4(1):9–23
investors? ESG analyses as tools for ethics-based AI auditing. Schreier M (2012) Qualitative content analysis in practice. Jacobs Uni-
AI & Soc 39(1):329–343 versity Bremen
Mishra S, Clark J, Perrault C R (2020) Measurement in AI policy: Tortoise Media (2024) Global AI index—Methodology. Available at:
Opportunities and challenges. arXiv preprint arXiv:2 009.0 9071 https://w ww.t ortoi semed ia.c om/w p-c onten t/u pload s/s ites/3/2 023/
Muller J (2018) The tyranny of metrics. Princeton University Press 06/A I-M ethod ology-2 306.p df
Nature (2020) AI will change the world, so it’s time to change AI. United Nations (2022) Principles for the Ethical Use of Artificial Intel-
Available at: https://d oi.o rg/1 0.1 038/d 41586-0 20-0 3412-z ligence in theUnited Nations System. Available at: https://u nsceb.
Nature (2023) AI will transform science—now researchers must org/s ites/d efaul t/fi les/2 022-0 9/P rinci ples%2 0for%2 0the%2 0Eth
tame it. Available at: https://w ww.n ature.c om/a rticl es/ ical%2 0Use%2 0of%2 0AI%2 0in%2 0the%2 0UN%2 0Syst em_1.p df
d41586-0 23-0 2988-6 van Berkel N, Papachristos E, Giachanou, A, Hosio S, Skov MB (2020)
Nesta (2024) AI Governance Database. Available at: https://w ww. A systematic assessment of national artificial intelligence policies:
nesta.o rg.u k/d ata-v isual isati on-a nd-i ntera ctive/a i-g overn ance- Perspectives from the Nordics and beyond. In: Proceedings of the
databa se/ 11th Nordic Conference on human-computer interaction: shaping
Nesta (2024) Innovation methods. Anticipatory regulation. Available experiences, Shaping Society, pp. 1–12
at: https://w ww.n esta.o rg.u k/f eatur e/i nnova tion-m ethod s/a ntic Van Roy V, Rossetti F, Perset K, Galindo-Romero L (2021) AI watch-
ipator y-r egula tion/ national strategies on artificial intelligence: a European perspec-
Nordström M (2022) AI under great uncertainty: implications and tive (No. JRC122684). Joint Research Centre (Seville site)
decision strategies for public policy. AI & Soc 37(4):1703–1714 Vinuesa R, Azizpour H, Leite I, Balaam M, Dignum V, Domisch S,
OECD.AI (2024). National AI policies & strategies. Available at: Fuso Nerini F (2020) The role of artificial intelligence in achiev-
https://o ecd.a i/e n/d ashbo ards/o vervi ew ing the Sustainable Development Goals. Nat Commun 11(1):1–10
OECD (2024a) Defining AI incidents and related terms. OECD Wachter S, Mittelstadt B, Floridi L (2017) Why a right to explanation
Artificial Intelligence Papers, No. 16, OECD Publishing, Paris, of automated decision-making does not exist in the general data
https://d oi.o rg/1 0.1 787/d 1a8d9 65-e n protection regulation. Int Data Privacy Law 7(2):76–99
OECD (2024b) OECD AI Principles overview. Available at: https:// Wang Y, Agichtein E, Benzi M (2012) TM-LDA: efficient online mod-
oecd.a i/e n/a i-p rinci ples eling of latent topic transitions in social media. In: Proceedings of
Oliver Wyman Forum (2024) Global cities AI readiness index. Meth- the 18th ACM SIGKDD International Conference on Knowledge
odology. Available at: https://w ww.o liver wyman forum.c om/ discovery and data mining, pp. 123–131
city-r eadin ess/g lobal-c ities-a i-r eadin ess-i ndex-2 019/m etho Ward F, Toni F, Belardinelli F, Everitt T (2024) Honesty is the best
dology.h tml policy: defining and mitigating AI deception. Advances in neural
Oxford Insights (2024) Government AI readiness index. Available at: information processing systems, 36
https://o xford insig hts.c om/w p-c onten t/u pload s/2 023/1 1/G over Wilson C, Van Der Velden M (2022) Sustainable AI: An integrated
nment_A I_R eadin ess_2 022_F V model to guide public sector decision-making. Technol Soc
Papyshev G, Yarime M (2023) The state’s role in governing artifi- 68:101926
cial intelligence: development, control, and promotion through
national strategies. Policy des Pract 6(1):79–102 Publisher's Note Springer Nature remains neutral with regard to
Papyshev G, Yarime M (2024) The limitation of ethics-based jurisdictional claims in published maps and institutional affiliations.
approaches to regulating artificial intelligence: regulatory gifting
in the context of Russia. AI & Soc 39(3):1381–1396
Perrault R, Clark J (2024) Artificial Intelligence Index Report 2024
