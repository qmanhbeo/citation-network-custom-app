This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3516500
Date of publication xxxx 00, 0000, date of current version xxxx 00, 0000.
Digital Object Identifier 10.1109/ACCESS.2024. Doi Number
Big Data and AI Algorithms for Sustainable
Development Goals: A Topic Modeling Analysis
Prema Nedungadi1,2, Simi Surendran1, Kai-Yu Tang3, Raghu Raman4
1School of Computing, Amrita Vishwa Vidyapeetham, Amritapuri, Kerala, India
2AmritaCREATE, Amrita Vishwa Vidyapeetham, Amritapuri, Kerala, India
3Graduate Institute of Library & Information Science, National Chung Hsing University, Taoyuan City, Taiwan
4Amrita School of Business, Amrita Vishwa Vidyapeetham, Amritapuri, Kerala, India
Corresponding author: Author (e-mail: raghu@ amrita.edu).
ABSTRACT This study makes significant contributions to the field by examining the transformative role of
big data and artificial intelligence (AI) in advancing Sustainable Development Goals (SDGs), particularly
healthcare (SDG3), sustainable energy (SDG7), and industry and infrastructure (SDG9). Using BERTopic
modeling, a machine learning technique, this research systematically analyzes literature from 2013 to 2024,
providing an overview of AI and big data applications mapped to SDGs which is a first. This structured
approach identifies key SDGs impacted by these technologies and highlights interdisciplinary methods that
further enhance SDG outcomes. AI applications notably improve healthcare by advancing disease tracking,
tailored treatments, and precision medicine, fostering universal healthcare and reducing noncommunicable
disease mortality. In energy, AI-driven solutions optimize forecasting, grid management, and renewable
integration, while in industry, they bolster infrastructure resilience through innovations like predictive
maintenance and automated quality control within Industry 4.0 frameworks. The integration of automated
text analysis and semantic context captures broad trends, contributing both methodologically and
substantively at the intersection of AI and sustainability. Despite these advancements, the study underscores
ethical concerns, including data privacy, security, and algorithmic biases. Interdisciplinary collaboration
among healthcare professionals, engineers, environmental scientists, and AI experts is crucial to developing
ethical, scalable AI solutions. The study suggests future research focus on AI transparency, scaling across
diverse sectors, and integrating advanced techniques such as neurosymbolic AI and quantum neural networks
to enhance system reliability. These insights offer practical implications, reinforcing the potential of AI and
big data to address global challenges sustainably while calling for balanced attention to ethical and regulatory
dimensions.
INDEX TERMS Sustainable development goal, Big data, Artificial intelligence, Healthcare, Resilient
energy, Resilient infrastructure, Industrial innovation, Generative AI
I. INTRODUCTION analytical tools for managing massive datasets and deriving
actionable insights [1]. Big data and AI are crucial for
The rapid advancement of artificial intelligence (AI) progress toward the SDGs set by the United Nations, which
technologies has transformed our ability to address the address key issues such as inequality, environmental
global challenges of climate change, healthcare, and sustainability, and peace. They provide a robust capacity
industrial inefficiencies. Sophisticated tools for analyzing for managing vast amounts of information, including data-
vast datasets enable more efficient decision-making, driven decisions, in tackling these multifaceted challenges
driving innovation in sectors critical to achieving the [2][3][4][5].
United Nations Sustainable Development Goals (SDGs). This study aims to examine how big AI-driven data
The contemporary landscape of global scientific solutions have addressed scientific challenges related to the
challenges, including climate change and public health SDGs. The growth in global data heightens the complexity
crises, benefits significantly from the integration of big data and scale of these challenges, necessitating scalable,
and AI. These complex challenges require advanced effective solutions [6][7]. The relevance of big data and AI
VOLUME XX, 2017 1
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3516500

extends  across  natural  and  life  sciences,  including  understanding their specific impacts across different SDGs
biotechnology  [8],  education  [9],  geophysics  [10,18],  and the effectiveness of interdisciplinary approaches.
genomics [11,13], heritage conservation [12], and medicine,  To analyze the literature systematically, this study follows
as well as engineering fields such as computer science, space  the Preferred Reporting Items for Systematic Reviews and
technology  [14],  chemical  engineering  [15]  and  civil  Meta-Analyses  (PRISMA)  protocol,  ensuring  a  rigorous
engineering [16,17], highlighting their versatility and critical  approach  to  data  collection  and  analysis.  Additionally,
role in diverse scientific inquiries.
BERTopic modeling is used for identifying key themes within
AI and big data research, providing deeper insights into their
| AI  and  | big  | data  | have  | driven  | advancements  |     | across  |     |     |     |     |     |     |     |     |
| -------- | ---- | ----- | ----- | ------- | ------------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
specific contributions to SDG-related fields. This study aims
| numerous  | fields.  | Initially  | centered  |     | around  | data-intensive  |     |     |     |     |     |     |     |     |     |
| --------- | -------- | ---------- | --------- | --- | ------- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
to address gaps in our understanding of the contributions of
areas  such  as  computer  engineering  and  information  AI and big data to sustainable development by answering
| systems,  | these  | technologies  |     | have  | enabled  | foundational  |     |     |     |     |     |     |     |     |     |
| --------- | ------ | ------------- | --- | ----- | -------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
the following research questions:
methodologies for handling complex datasets [19][20]. As
RQ1: Which SDGs are most impacted by AI and big data
| they  have  | evolved,  |     | their  | applications  |     | have  | broadened,  |     |     |     |     |     |     |     |     |
| ----------- | --------- | --- | ------ | ------------- | --- | ----- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
technologies?
| impacting  | diverse  | fields,  | from  | physics  |     | and  urbanism  | to  |     |     |     |     |     |     |     |     |
| ---------- | -------- | -------- | ----- | -------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
RQ2: What specific contributions have big data and AI
bioinformatics advancements [21][22] and sustainable urban  made toward advancing these SDGs?
| planning  | [23][24][25].  |     | Their  | growing  | applications  |     | have  |     |     |     |     |     |     |     |     |
| --------- | -------------- | --- | ------ | -------- | ------------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
RQ3: How do interdisciplinary approaches enhance the
| intensified  | their  | impact  | within  |     | fields  | and  encouraged  |     |     |     |     |     |     |     |     |     |
| ------------ | ------ | ------- | ------- | --- | ------- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
achievement of these SDGs?
interdisciplinary approaches essential for complex problems,
RQ4: What are the emerging trends and future research
highlighting their dynamic capabilities [26][27].
directions for big data and AI addressing these SDGs?
|     |     |     |     |     |     |     |     | RQ5:  | What  | ethical,  | data  | security,  | and  | accessibility  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | ----- | --------- | ----- | ---------- | ---- | -------------- | --- |
AI and big data inherently promote an interdisciplinary
challenges arise with the deployment of big data and AI in
approach, merging insights from various fields to address
addressing these SDGs, and what policies are recommended
| complex  | challenges.  |     | The  | future  | of  research  |     | on  these  |     |     |     |     |     |     |     |     |
| -------- | ------------ | --- | ---- | ------- | ------------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
technologies  is  geared  toward  enhancing  their  ethical  to address these issues?
This paper makes several significant contributions to the
| application,  |     | ensuring   | data  | security,      |     | and  developing  |          |                 |             |          |                 |     |            |     |             |
| ------------- | --- | ---------- | ----- | -------------- | --- | ---------------- | -------- | --------------- | ----------- | -------- | --------------- | --- | ---------- | --- | ----------- |
|               |     |            |       |                |     |                  |          | field.  First,  | it          | applies  | BERTopic        |     | modeling,  | a   | machine     |
| accessible    |     | solutions  | for   | disadvantaged  |     |                  | regions  |                 |             |          |                 |     |            |     |             |
|               |     |            |       |                |     |                  |          | learning        | technique,  | to       | systematically  |     | analyze    |     | literature  |
[28][29][30]. The ongoing advancement of AI and big data
published from 2013 to 2024. This approach provides a
is expected to address previously unsolvable problems in
emerging fields such as space and mechanical engineering,  comprehensive overview of the current research landscape
regarding the application of big data techniques and AI in
with researchers continually exploring ways to improve the
emerging scientific fields mapped directly to SDGs, which is
performance/complexity ratio of AI systems, aiming for
a first. Using this structured understanding of the research
sophisticated yet resource-efficient solutions [31][32]. This
|     |     |     |     |     |     |     |     | landscape,  | the  | study  | highlights  | which  | SDGs  |     | are  most  |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ---- | ------ | ----------- | ------ | ----- | --- | ---------- |
direction is vital for aligning innovations with sustainable
development  needs,  effectively  contributing  to  global  impacted by AI and big data, exploring how interdisciplinary
|     |     |     |     |     |     |     |     | approaches  | can  | enhance  | their  | achievement.  |     | Second,  | the  |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ---- | -------- | ------ | ------------- | --- | -------- | ---- |
challenges, and paving the way for a more resilient and
study effectively integrates automated text analysis with
equitable future.
|      |             |           |          |     |          |            |      | semantic  | context  | to  | capture  | broad  | trends  | through  | topic  |
| ---- | ----------- | --------- | -------- | --- | -------- | ---------- | ---- | --------- | -------- | --- | -------- | ------ | ------- | -------- | ------ |
| The  | literature  | includes  | several  |     | studies  | exploring  | the  |           |          |     |          |        |         |          |        |
modeling, thereby making methodological and substantive
intersection between AI and the SDGs. [33] analyzed this
correlation,  identified  future  research  directions,  and  contributions at the intersection of AI and sustainability.
|     |     |     |     |     |     |     |     | Finally,  | the  paper  | identifies  |     | emerging  | trends  | and  | offers  |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ----------- | ----------- | --- | --------- | ------- | ---- | ------- |
highlighted the roles of green AI and eco-friendly Internet
practical implications for future interdisciplinary research
| of  Things  | (IoT)  | applications  |               | in  | governance  |                 | and  data  |             |             |     |            |      |     |               |     |
| ----------- | ------ | ------------- | ------------- | --- | ----------- | --------------- | ---------- | ----------- | ----------- | --- | ---------- | ---- | --- | ------------- | --- |
|             |        |               |               |     |             |                 |            | directions  | concerning  |     | big  data  | and  | AI  | applications  | in  |
| management  |        | for  SDG      | achievement.  |     | AI’s        | sustainability  |            |             |             |     |            |      |     |               |     |
healthcare, energy management, and industrial innovations.
challenges from environmental and social perspectives can
address issues such as carbon emissions and fairness [34].  The structure of this paper is organized as follows: Section
II reviews the literature and identifies the gaps. In Section III,
[35] emphasized establishing responsible AI practices and
|             |     |                 |     |              |     |          |       | we  describe  | the  | systematic  | approach  |     | employed  |     | for  data  |
| ----------- | --- | --------------- | --- | ------------ | --- | -------- | ----- | ------------- | ---- | ----------- | --------- | --- | --------- | --- | ---------- |
| addressing  |     | sustainability  |     | challenges,  |     | whereas  | [36]  |               |      |             |           |     |           |     |            |
collection and analysis. Section IV presents the key findings
examined how AI and big data can engineer solutions for
from BERTopic modeling. In Section V, we present various
the SDGs. [37] discussed the potential of AI to reduce
greenhouse gas emissions across various sectors, and [38]  applications and emerging trends of AI concerning specific
|     |     |     |     |     |     |     |     | SDGs,  | interpreting  | our  | findings  | in  | depth.  | Finally,  | the  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ------------- | ---- | --------- | --- | ------- | --------- | ---- |
analyzed the impact of AI on industry, education, and
conclusion summarizes the main takeaways and explores their
| sustainability  |     | efforts.  | [39]  | used  predictive  |     | modeling  | to  |     |     |     |     |     |     |     |     |
| --------------- | --- | --------- | ----- | ----------------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
implications for stakeholders.
address environmental health and ecosystem issues.
| The  | integration  | of  | big  | data  and  | AI  | is  crucial  | for  |     |     |     |     |     |     |     |     |
| ---- | ------------ | --- | ---- | ---------- | --- | ------------ | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
II. RELATED WORK
| addressing       | global  | challenges  |     | aligned      |     | with  the  | SDGs.        |     |     |     |     |     |     |     |     |
| ---------------- | ------- | ----------- | --- | ------------ | --- | ---------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
| Despite          | their   | potential,  |     | significant  |     | gaps       | persist  in  |     |     |     |     |     |     |     |     |
| VOLUME XX, 2017  |         |             |     |              |     |            |              |     |     |     |     |     |     |     | 7   |
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3516500
The convergence of AI and big data analytics has The role of AI in reducing greenhouse gas emissions and
emerged as a promising paradigm for providing adapting to environmental challenges was discussed in
opportunities and challenges across multiple sectors, [37]. The authors examined studies that employed AI in
spanning healthcare, education, environmental various sectors, such as electricity, forest fire management,
conservation, sustainable energy, and industrial innovation. transportation, and carbon footprint tracking. They
In recent years, there has been considerable scholarly highlighted the potential of machine learning algorithms,
interest in investigating the impact of AI on the United including linear regression and support vector machines, as
Nations SDGs. Many review papers have emerged that aim well as deep learning approaches, like convolutional neural
to consolidate the literature in this domain to provide networks, in tackling climate change challenges.
insights into the utilization of AI for advancing the Additionally, they deliberated on the advantages, pitfalls,
objectives of sustainable development. and prospects of integrating AI with environmental
A prevailing thematic focus observed is the role of AI in challenges, emphasizing the need for technological
improving environmental sustainability, waste solutions to address these issues. In addition, a review by
management, water management, CO2 emission reduction, [38] examined the influence of AI on the SDGs,
carbon foot printing, and climate change mitigation are key investigating its applications in education, healthcare,
areas where AI interventions are extensively examined. agriculture, and climate change mitigation. The potential of
One study examined machine learning approaches that can AI to revolutionize industry, education, and sustainability
address the sustainability challenges associated with AI efforts by enabling smarter interventions, reducing waste,
from two key perspectives: environmental and social creating new applications, and improving accessibility was
sustainability [34]. The authors addressed various issues, also discussed. Moreover, they introduced a sustainable AI
including carbon emissions from AI model training and framework aligned with the SDGs to enhance the outcomes
inference, the substantial resources required for data in these areas.
collection and annotation, concerns regarding fairness and On the other hand, [39] surveyed the practicality of
privacy in AI models, and ensuring the safety of AI against human reasoning approaches accessible to beginners, who
adversarial attacks and data poisoning. They categorize AI may lack expertise in computer programming or advanced
technologies into four main groups: computation-efficient mathematics, for data analysis and result interpretation.
AI, data-efficient AI, responsible AI, and resilient AI. Additionally, the authors investigated the availability of
Computation-efficient AI focuses on reducing the user-friendly AI-based software for beginners, facilitating
environmental impact of AI by developing compressed AI experimentation. They utilized the 2018 Environmental
models and applying techniques such as pruning. Data- Performance Index (EPI) data from 180 countries,
efficient AI, including transfer learning and active learning encompassing indicators of environmental health and
algorithms, promotes sustainable development by reducing ecosystem vitality. The system employs an AI-based
manual efforts and resources. Responsible AI emphasizes Bayesian network approach for predictive modeling to
considering AI ethics in system design, particularly fairness uncover underlying tensions between environmental
and user data privacy. Resilient AI highlights the health, which typically improves with economic growth
importance of rationalizing AI models to enhance social and rising affluence, and ecosystem vitality, which often
sustainability and acceptance of modern AI systems. deteriorates because of industrialization and urbanization.
[35] stated that AI systems have been developed to [40] explored recent advancements in AI and deep
mitigate societal, ecological, and economic issues. They learning (DL) for achieving the SDGs, focusing on
examined various aspects, including establishing rules for renewable energy, environmental health, and smart
responsible AI and emphasizing transparent and reasonable building energy management. In the renewable energy
responsibilities for developers, operators, and decision- sector, AI and DL techniques have been shown to optimize
makers. They formulated sustainability challenges for AI, energy management, fault detection, and power grid
questioning the suitability of commonly used datasets for stability. The study presented various approaches,
transforming existing productions and exploring the including deep reinforcement learning for optimizing AC
democratic legitimization of AI-supported sustainability power flow, clustering techniques for solar power
efforts. It also scrutinizes the resource and energy generation, and predictive models such as SVR, AdaBoost,
intensities of AI, evaluating whether the benefits of AI and deep neural networks for renewable energy systems.
justify the energy and emissions generated during its Additionally, this paper examines the utilization of GeoAI
lifecycle. Moreover, the review targeted the regulation of for the efficient processing of spatial data and the potential
market power and monopolies in the AI sector, addressing of deep reinforcement learning in smart building energy
revenue generation and data concentration, and proposed management. The authors also discussed digital twin-based
regulatory frameworks to safeguard consumer interests and methods proposed for intelligent optimization and
ensure liability accountability. automation systems in residential energy management.
While existing research review papers have provided
VOLUME XX, 2017 7
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3516500
insights into the broad applications of AI and big data in
various sectors, this review distinguishes itself by focusing III. METHODOLOGY
specifically on the techniques and algorithms used in In alignment with the PRISMA guidelines, this
application areas of the top three researched SDGs. research followed a structured protocol for the identification,
Focusing on the top three SDGs, this paper offers a targeted screening, eligibility assessment, and inclusion of
examination of how AI and big data can contribute to publications. The robustness and reliability of the PRISMA
achieving specific sustainable development objectives. protocol are well established, and it has been utilized in
Additionally, this study suggests future research directions systematic literature reviews across various domains [41][42].
in these fields and recommends AI algorithms to address Figure 1 illustrates the research design.
challenges associated with various SDG-related use cases.
During the screening, we applied search terms ("big data"
OR "bigdata") to the titles and abstracts, which resulted in
FIGURE 1. Research design
9847 publications.
A. IDENTIFICATION PHASE
Employing the Dimensions database, which has 82.2% C. ELIGIBILITY PHASE
journal coverage beyond the Web of Science database and A focused selection of publications mapped directly to the
48.1% journal coverage beyond the Scopus database, this 17 SDGs was conducted via proprietary algorithms within the
study used an exhaustive search of artificial intelligence and Dimensions database, influenced by various SDG mapping
machine learning research, utilizing ANZSRC codes 4602 and initiatives, including the Aurora Network-Global’s SDG-
4611, respectively [43]. The Dimensions database’s Queries, the University of Auckland’s methodology
application of the ANZSCO framework for categorizing (Auckland SDG mapping, n.d.), and Elsevier’s SDG Mapping
research fields facilitated the identification of 813,054 Initiatives (Elsevier’s, n.d.). The Digital Science SDG
publications from 2013-2023 [44]. Mapping Initiative was selected for seamless integration with
Dimensions, providing preset search queries for each SDG,
B. SCREENING PHASE supported by a machine-learning model refined through expert
review. Various studies have utilized detailed SDG mapping
VOLUME XX, 2017 7
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3516500

methods to examine the trajectory of research themes. For
example, the area of green hydrogen was scrutinized by [44],
while the subjects of Fake News and the Dark Web were
investigated by [41] and [42], respectively. These findings
illustrate the use of SDG mapping as a tool to gauge how
| academic  | endeavors  | align  | with  | and  influence  |     | sustainable  |     |     |     |     |     |     |     |
| --------- | ---------- | ------ | ----- | --------------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
development goals.

Our approach acknowledges the interconnected nature
of the SDGs, a complexity that network analysis literature,
such as [44] and [45], has previously characterized. The use
of co-occurrence maps illustrates the semantic proximity of
| SDGs,  | revealing  | conceptual  | relatedness  |     | as  indicated  | by  |     |     |     |     |     |     |     |
| ------ | ---------- | ----------- | ------------ | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
shared citations in the literature [46]. The produced map
| visualizes  | each  | SDG  as  | a  node,  | with  | the  | node’s  size  |     |     |     |     |     |     |     |
| ----------- | ----- | -------- | --------- | ----- | ---- | ------------- | --- | --- | --- | --- | --- | --- | --- |
reflecting the extent of its presence in the research literature.
The thickness of the lines connecting these nodes signifies
| the  frequency  |          | of  co-occurrence   |     | among          | the         | goals,  thus  |     |     |     |     |     |     |     |
| --------------- | -------- | ------------------- | --- | -------------- | ----------- | ------------- | --- | --- | --- | --- | --- | --- | --- |
| illustrating    | the      | interconnectedness  |     | of             | the  SDGs.  | This          |     |     |     |     |     |     |     |
| depiction       | reveals  | the  SDGs           | as  | an  intricate  |             | but  unified  |     |     |     |     |     |     |     |
| framework       | that     | underpins           |     | efforts        | toward      | global        |     |     |     |     |     |     |     |

sustainability [47]. To ensure the quality and reliability of the
FIGURE 2. BERTopic modeling workflow
| data,  English-language  |      |           | research  | articles,  | review     | articles,  |     |     |     |     |     |     |     |
| ------------------------ | ---- | --------- | --------- | ---------- | ---------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
| conferences,             | and  | research  | chapters  | were       | included,  | and        |     |     |     |     |     |     |     |
As shown in Figure 2, the initial step in our modeling process
preprints were excluded. This phase resulted in 1288 eligible
|                |     |                 |     |              |     |            | involves     | embedding  | vectorization,  |                  | which  | transforms  | the        |
| -------------- | --- | --------------- | --- | ------------ | --- | ---------- | ------------ | ---------- | --------------- | ---------------- | ------ | ----------- | ---------- |
| publications.  |     | The  VOSviewer  |     | application  |     | maps  and  |              |            |                 |                  |        |             |            |
|                |     |                 |     |              |     |            | input  text  | into       | numerical       | representations  |        |             | known  as  |
interprets the research landscape in the context of SDGs [48].  embeddings.  Subsequently,  dimensionality  reduction  is
|     |     |     |     |     |     |     | achieved  | via  | Unified  | Manifold  | Approximation  |     | and  |
| --- | --- | --- | --- | --- | --- | --- | --------- | ---- | -------- | --------- | -------------- | --- | ---- |
D.  INCLUSION PHASE  Projection (UMAP), which effectively groups similar data
All 1288 eligible publications were included in the final dataset  points, leading to more distinct topic clusters [53]. After
for detailed analysis.
|     |     |     |     |     |     |     | simplifying  | the  | data,         | hierarchical  | density-based  |            | spatial  |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ---- | ------------- | ------------- | -------------- | ---------- | -------- |
|     |     |     |     |     |     |     | clustering   | of   | applications  | with          | noise          | (HDBSCAN)  | is       |
E.  BERTopic MODELING  employed to identify clusters of closely packed data points,
disregarding scattered or irrelevant information. To interpret
Topic  modeling  techniques,  such  as  nonnegative  matrix  the meaning of each topic cluster, the class-based term
|                |         |         |            |     |             |         | frequency-inverse  |              | document  |       | frequency  | (c-TF-IDF)  | is        |
| -------------- | ------- | ------- | ---------- | --- | ----------- | ------- | ------------------ | ------------ | --------- | ----- | ---------- | ----------- | --------- |
| factorization  | (NMF),  | latent  | Dirichlet  |     | allocation  | (LDA),  |                    |              |           |       |            |             |           |
|                |         |         |            |     |             |         | utilized           | to  extract  | the       | most  | salient    | words  or   | phrases,  |
probabilistic latent semantic analysis (PLSA), and To2Vec,
often struggle to capture semantic word relationships and are  facilitating  the  identification  and  ranking  of  key  topics
limited in handling short texts [49]. Unlike traditional bag- within the documents [54]. For our analysis, we adopted the
"all-MiniLM-L6-v2" text representation model, which is
of-words methods that prioritize term frequency, BERTopic
employs embeddings [50] to represent documents in a lower- well  suited  for  clustering  and  semantic  search  tasks  in
dimensional space, thereby preserving semantic information  English [55]. This modified TF-IDF approach identifies
representative terms within each topic by considering both
and providing a more contextual understanding [51] [45].
BERT, a deep learning language model developed by Google  term  frequency  and  inverse  document  frequency.  By
[52], leverages bidirectional encoder representations from  focusing on terms that appear frequently within a document
|     |     |     |     |     |     |     | but  less  | frequently  | in  others,  |     | the  model  | can  | effectively  |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ----------- | ------------ | --- | ----------- | ---- | ------------ |
transformers to enhance semantic understanding.
extract key concepts. These terms are then used to assign
topics to documents, with associated probabilities indicating
the likelihood of document membership within each topic
[56].
     To enhance topic model performance, we carefully tuned
three key hyperparameters: the n-gram range, the number of
topics, the minimum topic size, and the number of keywords
per topic. By setting the n-gram range to (1, 2), we consider
| VOLUME XX, 2017  |     |     |     |     |     |     |     |     |     |     |     |     | 7   |
| ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3516500
both single words and two-word phrases, enabling a more examined topic keywords and representative publications
comprehensive understanding of contextual relationships and analyzed abstracts, titles, and, when necessary, full
without excessive complexity. The number of topics was papers. Additionally, probability values and citation counts
iteratively adjusted between 5 and 20, and the intertopic were used to select the top three representative articles for
distance and coherence scores were evaluated to achieve a each topic. This rigorous review process guarantees the
balance of specificity and relevance. The minimum topic size accuracy and utility of our unsupervised topic modeling
was set between 20 and the number of keywords per topic, results, facilitating the identification of key themes within
ensuring the exclusion of overly granular or irrelevant topics the data.
by requiring a sufficient number of documents for each topic.
Simultaneously, the number of keywords per topic was Compared with the use of AI and big data analysis, the
carefully selected to capture the most relevant terms, features of BERTopic modeling used in this paper are
avoiding excessive detail. These settings, as emphasized by summarized. First, we use the pretrained BERT language
[93], effectively balance specificity and usability, resulting model as the backbone to understanding the semantic context
in meaningful and practical topics for analysis. Following instead of random word combination results from the AI tool.
stopword removal, common words such as 'use', 'used', 'use', Second, the method combines advanced machine learning
'add', 'added', 'adding', 'useful', 'based', 'related', and others techniques such as UMAP, HDBSCAN, and topic models to
were eliminated. optimize topic consistency and interpretability. Third, we use
the enhanced c-TF-IDF for topic keyword extraction, which
The UMAP algorithm parameters were configured to their considers both word frequency and word uniqueness. In
default settings, with "calculate probabilities" enabled to addition, we employ a rigorous manual review of topics and
assess the likelihood of document‒topic associations and the representative literature to ensure the reliability of the
language specified in English. The number of topics was results. This positions the research to make meaningful
determined through a combination of quantitative and methodological and substantive contributions at the
qualitative evaluations, emphasizing intertopic distance and intersection of data science and sustainability.
coherence scores. We experiment with topic numbers
ranging from 4-20, ensuring a minimum distance of 0.05 to IV. RESULTS
maintain sufficient separation between points in the reduced- A. EVOLUTION OF BIG DATA AND ARTIFICIAL
dimensional space. The "cosine" metric was used to calculate INTELLIGENCE ACROSS FIELDS OF RESEARCH
the angular similarity between vectors, and a random state of Figure 3 shows the influence of big data and AI across
100 was employed for reproducibility. The nearest neighbor various scientific fields over the years. Grounded in
(n_neighbors) parameter was set to 15, with a focus on the communications engineering, mathematical sciences,
local neighborhood of the data points to preserve the detailed computer vision, and information systems, these domains
structure while capturing broader patterns [57]. set the foundational data and computational techniques
crucial for developing big data and AI. As the timeline
Although machine learning techniques excel at clustering advances, there is an evident integration of big data and AI
data, the risk of misclassification persists [58]. To validate in fields such as software engineering, highlighting the
and interpret our results, we conducted a comprehensive need for software capable of managing and interpreting
manual review of both the identified topics and their vast datasets. The emergence of linguistics and data
representative publications. A team of three experts management indicates an increased focus on processing
meticulously evaluated the topics qualitatively, ensuring natural language and structuring data core elements in AI
their coherence and meaningfulness, aligning with recent developments.
BERTopic studies [59][60]. The experts thoroughly
VOLUME XX, 2017 7
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3516500
FIGURE 3. Evolution of big data and AI across diverse research disciplines.
The growing prominence of biomedical and clinical [61][62][63]. "Sustainable Cities and Communities"
sciences signals the intersection of big data with life follows, reflecting a focus on urban sustainability where
sciences, where AI algorithms are increasingly employed AI-driven data analytics help optimize resource use and
to analyze complex biological information. Machine urban planning [64][65][24]. By 2020, "climate action" and
learning is essential in predictive analytics and data pattern "affordable and clean energy" leveraged AI for climate
recognition, which are fundamental to big data modeling, renewable energy optimization, and sustainable
applications. In the latter part of the timeline, the rise of energy solutions [66]. The progression toward "reduced
cybersecurity and privacy research points to the importance inequalities" suggests the application of these technologies
of AI in protecting data integrity and addressing privacy in creating equitable solutions, such as through predictive
concerns within massive datasets. Civil engineering and analytics, to serve underserved communities better.
earth science also reflect the use of AI and big data in "Quality education" includes the adoption of AI in
modeling and solving environmental challenges, personalized learning and educational data mining
optimizing resource use, and improving urban planning. In [67][68]. The sequence continues with "Industry,
commerce, management, tourism, and services, the Innovation, and Infrastructure," indicating an interplay
implications of big data and AI influence customer where AI and big data are critical in driving innovation,
behavior analysis, market trend prediction, and service improving infrastructure, and promoting industrial
personalization. Finally, geoinformatics uses AI to sustainability [69]. By 2020, the focus shifted to "good
interpret geographic data, providing insights into spatial health and well-being," highlighting AI’s role in healthcare
patterns and relationships crucial for decision-making in through data-driven diagnostics, personalized treatment,
various sectors. and managing health crises [70]. In 2021, the attention
given to "Zero Hunger" reflected the use of AI in
B. MOST-IMPACTED SDGs THROUGH BIG DATA AND agricultural technologies to enhance food security, whereas
AI INNOVATIONS (RQ1) "Responsible Consumption and Production" highlighted
Next, we analyze how big data and AI have influenced the culmination of AI and big data in creating sustainable
global scientific challenges through the lens of consumption patterns and improving production efficiency
interdisciplinary SDGs. Starting with "Life on Land", the [71].
emphasis indicates a growing concern for biodiversity and Figure 4 shows how big data and AI research are
ecosystem services, which big data and AI address through instrumental in tackling complex global challenges and
enhanced monitoring and analysis of environmental data driving progress toward a sustainable future. The figure
VOLUME XX, 2017 7
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3516500
indicates that among the SDGs, “good health and well-being" advancement of SDGs 7 and 9, its direct impact on health
has likely been the most impacted by AI and big data makes SDG3 the most significant.
techniques in recent years. Innovations in diagnostics,
personalized medicine, and patient care have led to improved C. BERTopic THEMES FROM SDG3, SDG7 AND SDG9
health outcomes. Additionally, AI-driven tools and Next, we explored major themes from the top three
telemedicine have expanded access to healthcare services, SDGs, SDG3, SDG7, and SDG9, via BERTopic modeling
particularly in remote areas, making a significant difference in (Figure 5). The three topics in SDG3 are AI-enhanced
developing countries. Following SDG3, SDG9 is the second diagnosis, deep learning with health data, and AI for disease
most affected by AI. It enhances innovation in industries by prediction. SDG7 has four topics: optimizing energy systems
optimizing processes, improving efficiency, and driving new using AI, AI-driven models for energy forecasting, sustainable
product development. AI also supports smart infrastructure energy efficiency, and optimization based on AI algorithms.
through predictive maintenance and advanced manufacturing The four topics in SDG9 are leveraging AI and big data to
techniques, promoting sustainable industrial growth. SDG7 is transform industrial infrastructure, AI-driven sustainable
the next group in which AI contributes to optimizing energy industrial innovation, intelligent manufacturing for Industry
consumption, enhancing grid management, and advancing 4.0, and predictive maintenance.
renewable energy technologies. Although AI has a role in the
FIGURE 4. Progression of big data and AI research toward various sustainable development goals.
VOLUME XX, 2017 7
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3516500
FIGURE 5. Evolution of big data and AI across diverse research disciplines
and CT data to detect abnormalities with high accuracy.
D. SDG3: IMPACT ON GLOBAL HEALTH (RQ2) Because these models can manage large volumes of data, they
1) AI-ENHANCED DIAGNOSIS can easily scale to accommodate today's increasing data
To achieve SDG3, many AI and big data tools are availability. [75] reviewed how healthcare services are
being used to improve diagnosis. By analyzing large volumes improved by the use of robust processors, machine
of data, such as health records, medical images, and genetic learning, and deep learning algorithms facilitated by big
information, AI systems can find patterns. This analysis data and artificial intelligence. This review exemplifies the
allows for quick diagnosis and decision-making, which can integration of sophisticated AI techniques to manage
lead to better outcomes for patients. [72] integrated Apache healthcare data, directly supporting SDG3.d by improving
Spark with machine learning to enhance the early diagnosis global health security and disease surveillance systems.
of chronic kidney disease, leveraging feature selection [76] introduced a novel approach using deep similarity
methods and multiple classifiers to achieve high accuracy. learning to increase the predictive accuracy of electronic
Such research supports preemptive health interventions, health records. Their method, which employs CNNs within
aligning with the SDG3.4 target to reduce premature a Siamese-based framework, addresses data sparsity and
mortality from non-communicable diseases. The study by heterogeneity in medical big data. The technique
[73] leverages big data from electronic medical records to exemplifies the potential of AI in personalized patient care,
enhance medical diagnostics through deep Q-learning thereby supporting SDG3.4’s aim of ensuring healthy lives
coupled with gorilla troop optimization to select features through innovative and effective health solutions. [77]
for classifying breast cancer cases. This integration aligns utilized AI to revolutionize dermatological diagnostics. By
with SDG3.8 by promoting health and well-being through employing pretrained CNN models through transfer
advanced diagnostic tools and improving patient care learning, they achieved high accuracy in skin disease
through technological empowerment. [74] explored the classification. By harnessing electronic health records,
application of AI in mental health care, proposing patient monitoring devices, and smartphones, they
techniques such as AI-driven virtual assistants and chatbots advocated the use of big data as a service framework to
to offer evidence-based recommendations for personalized identify skin condition patterns to facilitate targeted
treatments. They suggested machine learning tools to preventive measures. This approach enhances diagnostic
analyze electronic medical records, illustrating AI’s ability efficiency and reduces the likelihood of human error,
to increase diagnostic accuracy and treatment efficacy in supporting SDG3.8 by improving the quality of health
orthopedics, thereby contributing to the broader goals of services and ensuring access to essential healthcare
SDG3.8 by improving health outcomes and medical technologies.
procedures.
2) DEEP LEARNING WITH HEALTH DATA 3) AI FOR DISEASE PREDICTION
Deep learning models can automatically learn and AI-assisted disease forecasting enables healthcare
extract features to analyze medical data such as X-ray, MRI, practitioners to make timely interventions, develop
VOLUME XX, 2017 7
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3516500
personalized treatment plans, and improve patient health distribution systems. The exploration of how big data and
outcomes. [78] focused on the use of artificial intelligence AI can significantly reduce energy consumption within
and big data technologies in traditional Chinese medicine smart buildings was highlighted in a study by [83]. The
orthopedics to optimize rehabilitation information and integration of machine learning techniques for energy
demonstrated that such systems can be faster and more management aligns with SDG7 by promoting energy
convenient. This technological advancement is set against efficiency in urban environments (SDG7.3). The authors
the backdrop of creating a "health cloud platform" to developed a data fusion framework to process power grid
integrate comprehensive community health services. big data generated from heterogeneous sources via
Machine learning algorithms such as support vector imprecise reasoning and clustering algorithms. Reducing
machines are utilized within the orthopedic rehabilitation energy consumption conserves energy and sets a
information data mining system to categorize different framework for sustainable urban development, which is
types of diseases. This approach directly supports SDG3.8, crucial as urban areas continue to grow and consume more
which is about achieving universal health coverage, resources.
including access to quality essential healthcare services.
2) AI-DRIVEN MODELS FOR ENERGY FORECASTING
[79] used the Cleveland dataset to predict heart disease at AI-based energy forecasting systems can analyze
an early stage via the Jellyfish optimization algorithm for data on energy consumption and market trends to predict
feature extraction. The resulting optimal feature set was future energy demands and ensure a reliable supply for all
then employed in machine learning algorithms, including consumers. The use of long short-term memory (LSTM)
artificial neural networks (ANNs), decision trees, support networks combined with human behavior pattern recognition
vector machines (SVMs), and AdaBoost, for predicting by [40] significantly enhanced the prediction and
heart abnormality treatment planning, directly supporting management of home energy consumption. This study
the SDG3.8 goal of promoting well-being through better leveraged data from residential customers to forecast loads,
disease management. A study by [80] introduced an incorporating LSTM with human behavior pattern
automated system that mimics an initial doctor’s diagnosis recognition and multilayer neural networks. By improving
via machine learning to analyze symptoms and recommend load forecasting methods, this research supports the SDG7.3
subtarget to double the global rate of improvement in energy
precautions, achieving nearly perfect accuracy. This
efficiency. These advancements facilitate more informed and
development helps extend healthcare resources and
efficient energy use, contributing to overall reductions in
enhances patient education on disease management,
energy consumption. [84] leveraged deep learning to
contributing to the aim of SDG3.4 for universal health
forecast wind power generation accurately, facilitating the
coverage.
integration of renewable energy sources into power grids
aligned with SDG7.2, which discusses substantially
E. SDG7: IMPACT ON AFFORDABLE AND CLEAN
increasing the share of renewable energy in the global energy
ENERGY (RQ2)
mix. By enhancing the prediction accuracy through principal
1) OPTIMIZING ENERGY SYSTEMS VIA AI AND BIG
component analysis-based dimensionality reduction and
DATA TECHNIQUES
support vector machines, this research contributes to
In the research [81], artificial intelligence (AI) and
improving the planning and utilization of wind energy and
big data techniques were applied to optimize the extraction
advancing sustainable energy solutions. By applying
of oil and gas, a key component of the energy sector. The
machine learning to predict energy consumption efficiently,
utilization of neural networks and evolutionary algorithms
[85] addressed the challenge of managing large datasets
enhances the extraction process, ensuring more efficient
within smart grids. Leveraging H2O’s distributed deep
energy production. This aligns closely with SDG7’s aim for
neural network implementation with support vector
enhanced energy efficiency (SDG7.3) and renewable regression, the proposed approach not only helps reduce the
energy sources, as better extraction techniques can reduce computational load but also enhances the precision of energy
the environmental impact of fossil fuel extraction and consumption forecasts. This directly contributes to SDG7, a
provide more reliable energy sources. [82] focused on subtarget for enhancing international cooperation to
improving the reliability and efficiency of smart grids via facilitate access to clean energy research and technology,
AI-driven analytics to correct data outliers. This is pivotal including renewable energy and energy efficiency.
for SDG7, as enhancing grid efficiency directly contributes
to the availability of affordable and clean energy (SDG7.1). 3) SUSTAINABLE ENERGY EFFICIENCY THROUGH AI
The distributed algorithm proposed in this research uses the AND BIG DATA
[86] explored energy-efficient hardware designs
alternating direction method of multipliers for imbalanced
for AI and machine learning, focusing on approximate
data classification, which saves training time and improves
computing to improve the power and energy efficiency of
scalability. By ensuring that energy distribution is managed
data processing systems. This approach directly supports
more efficiently through sophisticated AI algorithms, this
SDG7’s subtarget of enhancing global energy efficiency
research helps reduce energy waste and optimize
VOLUME XX, 2017 7
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3516500

(SDG7.3), as it reduces the energy demand of AI systems.  1) LEVERAGING AI AND BIG DATA TO TRANSFORM
INDUSTRIAL INFRASTRUCTURE
By designing hardware that requires less energy, this paper
A study by [92] reviewed how deep learning can
contributes to sustainable technological advancements that
monitor machine health by analyzing images and videos
can process large datasets without a proportional increase
that capture machine health components. This vision-based
| in  energy  |     | consumption.  |     | [87]  reviewed  |     | energy-efficient  |     |     |     |     |     |     |     |     |     |
| ----------- | --- | ------------- | --- | --------------- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
neural network implementations via GPUs and emerging  predictive maintenance  aids  in  the  early  detection  and
diagnosis of issues, ultimately minimizing downtime and
memristor technologies. This work is crucial for SDG7,
|               |     |      |            |      |             |          |       | enhancing  | overall  | machine  |        | efficiency.  | Their     | approach   |     |
| ------------- | --- | ---- | ---------- | ---- | ----------- | -------- | ----- | ---------- | -------- | -------- | ------ | ------------ | --------- | ---------- | --- |
| particularly  |     | for  | enhancing  | the  | efficiency  | of  big  | data  |            |          |          |        |              |           |            |     |
|               |     |      |            |      |             |          |       | aligns     | with     | SDG9’s   | focus  | on           | building  | resilient  |     |
operations and reducing the energy footprint of processing
infrastructure (SDG9.1) and underscores the importance of
large-scale neural networks (SDG7.3). This contributes to
more sustainable AI applications by significantly lowering  innovation in achieving sustainable industrial processes
(SDG9.5). [93] focused on optimizing network efficiency
the power required for data analytics, which is essential for
energy-intensive sectors. [88] reviewed accelerators for  in industrial applications through adaptive clustering and
|     |     |     |     |     |     |     |     | machine  | learning,  | addressing  |     | SDG9  | by  improving  |     | the  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---------- | ----------- | --- | ----- | -------------- | --- | ---- |
deep neural networks, addressing the challenges posed by
reliability and sustainability of industrial infrastructures
big data and AI, such as speed, memory requirements, and
energy efficiency. Optimizing the design of deep neural  (SDG9.4).  Their  methodology  reflects  an  innovative
|          |               |     |      |        |             |           |     | approach  | to  | managing  | complex  |     | systems,  | ensuring  |     |
| -------- | ------------- | --- | ---- | ------ | ----------- | --------- | --- | --------- | --- | --------- | -------- | --- | --------- | --------- | --- |
| network  | accelerators  |     | via  | ASICs  | and  FPGAs  | improved  |     |           |     |           |          |     |           |           |     |
computational  efficiency  and  reduced  the  latency  and  operational efficiency and robustness, thereby fostering
|     |     |     |     |     |     |     |     | industry  | innovation  | and  | infrastructure  |     | (SDG9.5).  |     | In  |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ----------- | ---- | --------------- | --- | ---------- | --- | --- |
power consumption of AI systems. This research aids in
exploring next-generation wireless networks, [94] utilized
achieving the SDG7 subtarget of increasing the share and
efficiency of renewable energy by enabling faster and more  AI and big data to enhance network capabilities, which are
essential for modern industrial environments. This review
| efficient  | processing  |     | for  | AI-driven  | energy  | applications  |     |     |     |     |     |     |     |     |     |
| ---------- | ----------- | --- | ---- | ---------- | ------- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(SDG7.a).  examines the key factors influencing the adoption of big
|     |     |     |     |     |     |     |     | data  analytics  |     | and  the  | importance  |     | of  advanced  |     | data  |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --------- | ----------- | --- | ------------- | --- | ----- |
4) ENERGY OPTIMIZATION ALGORITHMS IN BIG DATA
analytics, ML, and AI in optimizing the operation, control,
APPLICATIONS
|     |     |      |           |                 |     |                 |     | and  efficiency  |     | of  data-driven  |     | next-generation  |     | wireless  |     |
| --- | --- | ---- | --------- | --------------- | --- | --------------- | --- | ---------------- | --- | ---------------- | --- | ---------------- | --- | --------- | --- |
|     | In  | the  | Internet  | of  Everything  |     | era,  managing  |     |                  |     |                  |     |                  |     |           |     |
networks.
exploding data volumes requires innovative solutions. [89]
address the challenges posed by the Industrial Internet of  2) AI-DRIVEN SUSTAINABLE INDUSTRIAL INNOVATION
By discussing the integration of big data and AI
| Things,  | where  | devices  |     | often  lack  | sufficient  | computing  |     |     |     |     |     |     |     |     |     |
| -------- | ------ | -------- | --- | ------------ | ----------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
power and energy storage. By integrating mobile edge  technologies,  industrial  cyber-physical  systems  can  be
|            |     |      |       |                |     |            |        | enhanced  | through  | the  | use  | of  machine  | learning  |     | and  |
| ---------- | --- | ---- | ----- | -------------- | --- | ---------- | ------ | --------- | -------- | ---- | ---- | ------------ | --------- | --- | ---- |
| computing  |     | and  | deep  | reinforcement  |     | learning,  | their  |           |          |      |      |              |           |     |      |
multiagent system optimally manages task offloading to  multiagent systems. This automation and efficiency are
conserve energy while reducing delay, directly contributing  crucial for sustainable industrialization, aligning with the
|     |          |           |     |             |     |              |      | SDG9.5  | target  | to  | foster  | innovation  |     | in  resilient  |     |
| --- | -------- | --------- | --- | ----------- | --- | ------------ | ---- | ------- | ------- | --- | ------- | ----------- | --- | -------------- | --- |
| to  | SDG7.3,  | focusing  |     | on  energy  |     | efficiency,  | and  |         |         |     |         |             |     |                |     |
demonstrating the potent fusion of big data techniques and  infrastructure.  [95]  proposed  a  traffic  network  flow
|     |     |     |     |     |     |     |     | prediction  | system  | that  | leverages  | a   | deep  convolutional  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------- | ----- | ---------- | --- | -------------------- | --- | --- |
AI in industrial applications. [90] introduced a novel deep
deterministic policy gradient-based algorithm tailored for  neural network alongside a parallel training algorithm for
5G/6G communications to optimize the use of resources  parameter learning. They utilized Spark cloud deployment
for flexible scaling of computing resources and enhancing
such as frequency and energy. This approach supports
SDG7.3 by promoting energy efficiency and aligns with the  capabilities in processing large volumes of traffic big data.
This discussion aligns with the SDG9.5 target to foster
overall theme of leveraging big data and AI to ensure
sustainable  energy  management  in  next-generation  innovation in resilient infrastructures. [96] explored how
communication systems. [91] explored the optimization of  the  IoT  and  edge  computing  drove  forward  smart
manufacturing systems. By integrating deep learning and
task migration in mobile edge computing environments to
enhance the user experience while minimizing energy use  collaborative robotics, their research promotes intelligent
|     |     |     |     |     |     |     |     | and  sustainable  |     | industries,  | directly  |     | supporting  | SDG9.4  |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | ------------ | --------- | --- | ----------- | ------- | --- |
and processing time. The use of the K-proximal policy
optimization  algorithm,  an  advanced  form  of  deep  objectives  to  enhance  sustainable  industrialization  and
reinforcement learning, exemplifies the application of AI to  infrastructure. In the research highlighted by [97], a crucial
infrastructure challenge concerning road damage detection
achieve greater energy efficiency, supporting the SDG7.3
subtarget. This research is pivotal in revealing how big data  was addressed by employing a deep learning approach
|     |     |     |     |     |     |     |     | based  | on  YOLO.  | They  |     | collected  | data  | through  | a   |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ---------- | ----- | --- | ---------- | ----- | -------- | --- |
and AI can coalesce to optimize computational tasks in
energy-constrained scenarios.  smartphone-based method and devised a lightweight, rapid
  solution  for  object  detection  tasks.  The  application  of
artificial intelligence within these frameworks contributes
F. SDG9: IMPACT ON INDUSTRY, INNOVATION AND
INFRASTRUCTURE (RQ2)  significantly to building robust infrastructures, aligning
| VOLUME XX, 2017  |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 7   |
| ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3516500

with  the  robust  infrastructure  and  innovation  goals  of  for manual labor. The application of predictive analytics
SDG9.1 and SDG9.5.  exemplifies the transformative power of AI in Industry 4.0
|     |     |     |     |     |     |     |     | to  enable  | more  | efficient production  |     | lines  and  | improve  |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ----- | --------------------- | --- | ----------- | -------- |
3) INTELLIGENT MANUFACTURING IN INDUSTRY 4.0
The integration of AI with IoT and robotics provides  industrial sustainability, directly contributing to SDG9 by
machines with intelligence to optimize operations, manage  enhancing sustainable industrialization and infrastructure
(SDG9.4).
failures, maintain quality control, and improve productivity.
[98] delved into integrating deep learning in the context of
V. DISCUSSION
| road  traffic  | to            | investigate  | traffic     | congestion  |     | patterns       | and  |     |     |     |     |     |     |
| -------------- | ------------- | ------------ | ----------- | ----------- | --- | -------------- | ---- | --- | --- | --- | --- | --- | --- |
| explain        | nonrecurring  |              | congestion  | resulting   |     | from  various  |      |     |     |     |     |     |     |
events. They tested the performance of their model through  This research examines the role of big data and AI in
|     |     |     |     |     |     |     |     | advancing  | the  | areas  of  | healthcare,  | sustainable  | energy,  |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ---- | ---------- | ------------ | ------------ | -------- |
three scenarios utilizing real-world data encompassing three
|                                             |     |     |     |     |     |              |     | industry,  | innovation,  | and  | infrastructure.  | AI  | techniques  |
| ------------------------------------------- | --- | --- | --- | --- | --- | ------------ | --- | ---------- | ------------ | ---- | ---------------- | --- | ----------- |
| event types: football games, hockey games,  |     |     |     |     |     | and traffic  |     |            |              |      |                  |     |             |
accelerate progress in SDG3 by enhancing services such as
| incidents.  | It  emphasizes  |     | the  | role  | of  AI  | in  enhancing  |     |     |     |     |     |     |     |
| ----------- | --------------- | --- | ---- | ----- | ------- | -------------- | --- | --- | --- | --- | --- | --- | --- |
disease tracking, predicting disease progression, tailoring
infrastructure, which directly supports SDG9.5 by fostering
treatment plans, advancing precision medicine, providing
innovation in industrial solutions. [99] explored the role of
virtual assistant support, and enhancing drug discovery. For
computational intelligence in smart manufacturing, a core
SDG7, AI aids in energy consumption forecasting, demand
component of Industry 4.0. Their research, which uses the
|     |     |     |     |     |     |     |     | response  | management,  | fault  | detection,  | and  | smart  grid  |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | ------------ | ------ | ----------- | ---- | ------------ |
IoT and advanced AI algorithms such as deep learning and  management. It also enhances the use of renewable energy,
reinforcement learning, aligns with SDG9.4 by promoting
|              |                     |     |     |       |           |           |     | improves                                   | energy  | infrastructure  |     | reliability,  and  | enables  |
| ------------ | ------------------- | --- | --- | ----- | --------- | --------- | --- | ------------------------------------------ | ------- | --------------- | --- | ------------------ | -------- |
| sustainable  | industrialization.  |     |     | This  | approach  | improves  |     |                                            |         |                 |     |                    |          |
|              |                     |     |     |       |           |           |     | predictive planning for energy resources.  |         |                 |     | In SDG9, AI-       |          |
manufacturing  efficiency  and  resource  management,  powered  initiatives  promote  the  development  of  smart
directly  contributing  to  smarter  and  more  sustainable  infrastructure,  intelligent  transportation  systems,  supply
industrial practices. Focusing on the intelligent automation  chain management, automated manufacturing processes, and
and operation management of large enterprise cloud data  automated  quality  control.  This  focused  examination
centers, [100] highlighted the use of big data and AI. This  highlights the potential impact of AI and big data in these
enhances the operational efficiency of data centers, which  domains,  presenting  the  challenges  and  future
is  fundamental  for  supporting  sustainable  industrial  developments required to address key global challenges in
health, energy, and infrastructure development.
| practices  | and  | infrastructure  |     |     | development.  |     | Such  |     |     |     |     |     |     |
| ---------- | ---- | --------------- | --- | --- | ------------- | --- | ----- | --- | --- | --- | --- | --- | --- |
advancements contribute to the targets set by SDG9.1 and
SDG9.4, promoting resilient and sustainable infrastructure.  A.  CONTRIBUTIONS OF BIG DATA AND AI TO TOP
SDGs (RQ2)
4) PREDICTIVE MAINTENANCE
[101] developed a system that enhances defect
Figure 6 illustrates the important role of AI and big
detection in metal manufacturing through convolutional
data for SDG3 to strengthen healthcare by enabling more
neural networks (CNNs) and extensive data mining. The  accurate diagnoses, effective treatments, and personalized
authors proposed the use of machine learning and data
care. Medical researchers have analyzed extensive datasets
fusion techniques to analyze manufacturing datasets to
via advanced algorithms to increase disease detection and
detect quality events and enhance process monitoring. They
treatment accuracy. For example, the "deep learning in
approached defect detection as a binary classification task
medical data analysis" segment underscores the use of
and implemented ensemble learning on datasets derived  sophisticated AI algorithms for dermatological diagnostics
| from         | manufacturing  |     | processes.  |          | This  | technological  |     |              |         |             |           |               |     |
| ------------ | -------------- | --- | ----------- | -------- | ----- | -------------- | --- | ------------ | ------- | ----------- | --------- | ------------- | --- |
|              |                |     |             |          |       |                |     | and  breast  | cancer  | diagnosis,  | directly  | contributing  | to  |
| integration  | improves       |     | product     | quality  | and   | optimizes      |     |              |         |             |           |               |     |
SDG3.8, which emphasizes universal healthcare coverage,
resource use, supporting SDG9’s focus on building resilient
including access to quality essential healthcare services.
| infrastructure  |     | and  fostering  |     | innovation  |     | in  industry  |     |           |      |            |               |              |         |
| --------------- | --- | --------------- | --- | ----------- | --- | ------------- | --- | --------- | ---- | ---------- | ------------- | ------------ | ------- |
|                 |     |                 |     |             |     |               |     | The  "AI  | and  | big  data  | for  Disease  | Prediction"  | branch  |
processes  (SDG9.4  and  SDG9.5).  [102]  utilized  deep  highlights predictive models for chronic kidney disease and
convolutional neural networks to establish an adaptable
heart disease, highlighting how AI-driven insights can lead
| robotic  | inspection  | station.  | This  | station  | is  | proficient  | in  |     |     |     |     |     |     |
| -------- | ----------- | --------- | ----- | -------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
to early diagnosis and better disease management, thus
| autonomously  |     | conducting  | quality  |     | control  | tasks  | within  |            |           |         |               |            |       |
| ------------- | --- | ----------- | -------- | --- | -------- | ------ | ------- | ---------- | --------- | ------- | ------------- | ---------- | ----- |
|               |     |             |          |     |          |        |         | advancing  | SDG3.4’s  | target  | of  reducing  | mortality  | from  |
human−machine interface (HMI) consoles without human
|     |     |     |     |     |     |     |     | noncommunicable  |     | diseases  | through  | prevention  | and  |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --------- | -------- | ----------- | ---- |
intervention.  The  tasks  performed  include  operator  treatment. This integration of AI and big data enhances
recognition, classifying the type of HMI being inspected,
diagnostic accuracy and fosters personalized patient care,
and identifying errors in the display. [103] aimed to employ
significantly transforming healthcare delivery systems.
machine learning algorithms to uncover confusing patterns
in IC testing data to increase quality and reduce the need
| VOLUME XX, 2017  |     |     |     |     |     |     |     |     |     |     |     |     | 7   |
| ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3516500

FIGURE 6. Impact of AI and big data on healthcare applications supporting SDG3’s goal of ensuring healthy lives and well-being.
  and  SDG7.1  for  increasing  renewable  energy  use.  This
     Figure 7 shows the transformative potential of AI and big  integration highlights the crucial role of AI and big data in
data across various facets of energy management, aiming to  making  energy  systems  more  efficient  and  less
advance SDG7, which promotes affordable and clean energy.  environmentally intrusive, highlighting the urgent need for
This approach has diverse applications, from enhancing oil  technological advancements to achieve these global goals
| and gas extraction to optimizing energy use in smart buildings  |                  |                    |                 | sustainably.  |
| --------------------------------------------------------------- | ---------------- | ------------------ | --------------- | ------------- |
| and grids. Each branch of the diagram underscores significant   |                  |                    |                 |               |
| innovations                                                     | such  as  smart  | grid  reliability  | and  AI-driven  |               |
| models for energy forecasting, highlighting the direct impact   |                  |                    |                 |               |
| on subtargets such as SDG7.3 for improving energy efficiency    |                  |                    |                 |               |
VOLUME XX, 2017  7
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3516500
FIGURE 7. Impact of AI and big data in energy management on advancing SDG7 for affordable and clean energy
systems and improve traffic network flow prediction,
Figure 8 illustrates the multifaceted impact of AI and directly fostering innovation within resilient
big data on industry, innovation, and infrastructure, infrastructures. Additionally, intelligent manufacturing in
addressing various components of SDG9. Central themes Industry 4.0 is depicted through initiatives such as traffic
include optimizing industrial infrastructure through congestion analysis and smart manufacturing with the IoT,
machine health monitoring, network efficiency, and which aligns with SDG9.4 by promoting sustainable
wireless network capabilities, highlighting advancements industrialization. The segment on predictive maintenance
that bolster infrastructure resilience (SDG9.1) and drive highlights machine learning’s role in defect detection and
innovation (SDG9.5). The diagram further explores AI- quality control, optimizing industrial processes, and
driven big data solutions that enhance cyber-physical enhancing sustainability.
VOLUME XX, 2017 7
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3516500

FIGURE 8. Impact of AI and big data in energy management on advancing SDG7 for affordable and clean energy

  medicine, rehabilitation, medical image translation, lab result
B.  EMERGING TRENDS OF BIG DATA AND AI FOR
|     |     |     |     |     |     |     | translation,  | drug  discovery,  | automated  | electronic  |     | medical  |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ----------------- | ---------- | ----------- | --- | -------- |
ADVANCING TOP SDGs (RQ4)  records, medical research, and patient education [105][106].
Figure  9  presents  a  comprehensive  framework  Different  types  of  GAI  algorithms,  such  as  generative
showcasing the integration of AI and big data algorithms in
adversarial networks for generating synthetic data closely
addressing SDGs 3, 7, and 9. SDG3 has varying data types,
|     |     |     |     |     |     |     | resembling  | real-world  medical  | images,  | recurrent  |     | neural  |
| --- | --- | --- | --- | --- | --- | --- | ----------- | -------------------- | -------- | ---------- | --- | ------- |
such as clinical notes, patient records, medical images such
networks for processing time series medical data, variational
as X-rays and MRIs, wearable sensor data, and genomic
autoencoders for generating new data samples useful in drug
data. The primary challenges in this sector include high  discovery and personalized medicine, and transformer models
dimensionality, privacy concerns due to the sensitive nature
for natural language processing tasks such as summarizing
of health data, heterogeneity from diverse data sources, and
clinical notes, transcribing medical records, and analyzing
| incomplete  | datasets.  | Moreover,  | the  | data  | might  | be  |     |     |     |     |     |     |
| ----------- | ---------- | ---------- | ---- | ----- | ------ | --- | --- | --- | --- | --- | --- | --- |
patient-doctor conversations, can be utilized in the health care
| unstructured,  | inadequate,  | or  | poor  | quality.  | Currently,  |     |     |     |     |     |     |     |
| -------------- | ------------ | --- | ----- | --------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
field to enhance diagnostic capabilities.
algorithms such as federated learning, capsule networks,  SDG7 uses data from energy consumption metrics, smart
and deep learning techniques are utilized to handle image
|              |                 |               |          |          |            |     | meter  readings,  | weather               | conditions  | influencing   |           | energy  |
| ------------ | --------------- | ------------- | -------- | -------- | ---------- | --- | ----------------- | --------------------- | ----------- | ------------- | --------- | ------- |
| analysis     | and  maintain   | data          | privacy  | while    | analyzing  |     |                   |                       |             |               |           |         |
|              |                 |               |          |          |            |     | production,       | and  operational      | data        | from  energy  | grids.    | The     |
| distributed  | data  sources.  | Transformers  |          | support  | medical    |     |                   |                       |             |               |           |         |
|              |                 |               |          |          |            |     | challenges        | here  are  primarily  | the         | variability   | inherent  | in      |
document analysis by finding insights from many clinical
renewable energy sources, the extensive volume of data, the
notes, research papers, and patient records. Table 1 presents  temporal ordering of sensor data, high noise content, and the
| recommended  | applications  | of  | AI  techniques,  |     | highlighting  |     |     |     |     |     |     |     |
| ------------ | ------------- | --- | ---------------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
need for real-time processing capabilities. Quantum neural
| their  strengths  | and  weaknesses  |     | and  | demonstrating  |     | their  |     |     |     |     |     |     |
| ----------------- | ---------------- | --- | ---- | -------------- | --- | ------ | --- | --- | --- | --- | --- | --- |
networks and reinforcement learning are currently employed
effectiveness in advancing SDGs 3, 7, and 9.
to increase the efficiency of smart grids and optimize energy
AI-driven predictive genomics and neurosymbolic AI could
|     |     |     |     |     |     |     | distribution.  | Future  approaches  |     | could  involve  | advanced  |     |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ------------------- | --- | --------------- | --------- | --- |
improve  personalized  medicine  and  enhance  the  quantum algorithms for real-time, efficient grid optimization,
| interpretability  | of  | AI-driven  | health  |     | assessments.  |     |                 |                |      |                |      |       |
| ----------------- | --- | ---------- | ------- | --- | ------------- | --- | --------------- | -------------- | ---- | -------------- | ---- | ----- |
|                   |     |            |         |     |               |     | rapid  complex  | computations,  | and  | AI  solutions  | for  | self- |
Neurosymbolic AI integrates symbolic reasoning with neural  managed autonomous energy grids. It is important to prioritize
networks, offering improved explainability without sacrificing
|     |     |     |     |     |     |     | the  integration  | of  AI  | technologies  | in  smart  | grids  | and  |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | ------- | ------------- | ---------- | ------ | ---- |
performance, which is crucial in healthcare [104].  Generative
renewable energy utilization to increase energy efficiency.
AI (GAI) models offer vast potential in healthcare, spanning  The use of quantum-based learning algorithms for real-time
clinical decision support, personalized treatments, precision
grid optimization is highly effective since it improves energy
| VOLUME XX, 2017  |     |     |     |     |     |     |     |     |     |     |     | 7   |
| ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3516500
grid operations and decision-making while ensuring robust chains and automate the design of AI models for industrial
security against cyber threats. Additionally, adopting AI- processes. Additionally, neural architecture search (NAS)
driven autonomous energy grids to respond to demand supports industrial applications by automating the design of
fluctuations and optimize energy flow dynamically is optimized AI models that enhance manufacturing processes
essential. The implementation of self-configuring energy grids and innovation. Reinforcement learning is employed in
with preventive maintenance to increase fault tolerance and infrastructure monitoring to optimize maintenance schedules
resilience and minimize disruptions with minimal human and resource allocation. In the future, cognitive automation
intervention is also recommended. Large Language Models could transform manufacturing processes and AI-driven urban
for power system queries and decision-making can increase planning systems, enabling more sustainable and efficient
grid efficiency. Furthermore, public awareness initiatives for urban development.
demand response should be launched to empower consumers In smart industrialization, AI algorithms analyze
to participate in energy conservation efforts actively. manufacturing data to optimize production processes and
Additionally, optimizing the design of renewable energy enable predictive maintenance. GAI virtual assistants enhance
infrastructure through AI-driven simulations and analysis knowledge retrieval by facilitating quick access to relevant
provides the potential of AI technologies in shaping a resilient data for decision-making. Job sequence planning is optimized
energy future. through AI algorithms to schedule tasks and minimize
SDG9 uses manufacturing data such as supply chain logs, resource waste. Moreover, AI-driven status report generation
infrastructure monitoring data, and urban planning data. The automates reporting processes, providing stakeholders
complexity in this field is due to the interconnected nature of with real-time insights into project progress and performance.
the data, the high volume of data, the diversity of formats, and Safety awareness is improved through AI-powered systems
the necessity for high accuracy in planning and management. that analyze sensor data and provide proactive alerts and
Graph neural networks and neural architecture search are key recommendations to mitigate risks.
technologies used today to optimize logistics and supply
VOLUME XX, 2017 7
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3516500

FIGURE 9. Emerging trends of AI and big data algorithms and applications for SDG3, SDG7 and SDG9.

Table 1: Recommended applications of AI techniques, highlighting their strengths and weaknesses, and demonstrating their effectiveness in
advancing SDGs 3, 7, and 9
Techniques  SDG  Recommended  Algorithms  Strengths  Weaknesses
Applications
Machine  ▪  Disease tracking  ▪  Random Forest  ▪  Identifies patterns in  ▪  Requires large,
Learning    ▪  Personalized  ▪  Support Vector  large datasets.  labeled datasets
  treatment  Machines (SVM)  ▪  High accuracy in  for training
[72-74]
| ▪  Disease   | ▪  Gradient boosting  | diagnostics             | ▪  Risk of   |
| ------------ | --------------------- | ----------------------- | ------------ |
| Progression  | models                | ▪  Disease progression  | overfitting  |
▪  Precision  ▪  Regression Models  analysis  ▪  Ethical issues
| medicine           | ▪  Time Series Analysis   | ▪  Personalized medicine  | around data  |
| ------------------ | ------------------------- | ------------------------- | ------------ |
| ▪  Drug discovery  | ▪  Clustering algorithms  | based on genetic          | privacy      |
|                    | such as k-means           | profiles.                 |              |
▪  Bayesian Classifier
▪  Ensemble Methods
▪  Energy  ▪  Regression Models  ▪  Identify patterns  ▪  Good data quality
| consumption  | ▪  Classification Models  | and trends in the data  | is required  |
| ------------ | ------------------------- | ----------------------- | ------------ |

[82-83]  forecasting  such as SVM, k-nn,  ▪  Predicts energy needs  ▪  Data security
  ▪  Demand response  random forest, logistic  ▪  Optimizes resource  concerns
| management          | regression               | allocation  |     |
| ------------------- | ------------------------ | ----------- | --- |
| ▪  Fault Detection  | ▪  Time Series Analysis  |             |     |
VOLUME XX, 2017  7
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3516500

|     | ▪  Smart Grid  | ▪  Clustering Algorithms  |     |     |
| --- | -------------- | ------------------------- | --- | --- |
|     | Management     | such as k-means,          |     |     |
|     |                | DBSCAN                    |     |     |
▪  Ensemble Methods
▪  Automated  ▪  Regression Models  ▪  Enhances operational  ▪  Data availability
|     | manufacturing  | ▪  Classification Models  | efficiency  | and  |
| --- | -------------- | ------------------------- | ----------- | ---- |
  processes  such as SVM, k-nn,  ▪  Reduces waste  implementation
[93]
|     | ▪  Supply chain  | random forest             |     | challenges        |
| --- | ---------------- | ------------------------- | --- | ----------------- |
|     | optimization     | ▪  Time Series Models     |     | ▪  Data security  |
|     |                  | ▪  Clustering Algorithms  |     | concerns          |
|     |                  | such as k-means           |     |                   |
▪  Streaming algorithms

Deep  ▪  Medical image  ▪  Convolutional Neural  ▪  High accuracy in image  ▪  High
Learning  analysis  Networks  and signal analysis  computational

|     | ▪  Medical Signal  | ▪  Recurrent Neural  | ▪  Scalable with a large  | resources  |
| --- | ------------------ | -------------------- | ------------------------- | ---------- |
[75-77]
|     | Analysis           | Networks                 | volume of data  | required            |
| --- | ------------------ | ------------------------ | --------------- | ------------------- |
|     | ▪  Drug discovery  | ▪  Autoencoders          |                 | ▪  Requires high-   |
|     |                    | ▪  Long Short-Term       |                 | quality, annotated  |
|     |                    | Memory Networks          |                 | image datasets      |
|     |                    | ▪  Attention Mechanisms  |                 | ▪  Lack of          |
interpretability of
results

▪  Smart grid  ▪  Convolutional Neural  ▪  Model nonlinear  ▪  Difficulty in real-
|     | management  | Networks  | relationships  | time deployment  |
| --- | ----------- | --------- | -------------- | ---------------- |

| [85-88]  | ▪  Renewable energy  | ▪  Recurrent Neural  | ▪  Handles large data  |     |
| -------- | -------------------- | -------------------- | ---------------------- | --- |
|          | forecasting          | Networks             | volumes                |     |

|     | ▪  Remote sensing  | ▪  Long Short-Term       |                          |              |
| --- | ------------------ | ------------------------ | ------------------------ | ------------ |
|     | data analysis      | Memory Networks          |                          |              |
|     | ▪  Thermal image   | ▪  Deep Belief Network   |                          |              |
|     | analysis of solar  | ▪  Auto encoders         |                          |              |
|     | panel data         |                          |                          |              |
|     | ▪  Industrial      | ▪  Convolutional Neural  | ▪  Improves operational  | ▪  Resource- |
|     | automation         | Networks                 | efficiency               | intensive    |

|     | ▪  Predictive  | ▪  Recurrent Neural  | ▪  Reduces downtime  | algorithms  |
| --- | -------------- | -------------------- | -------------------- | ----------- |
[92,95, 97, 98]
|     | maintenance            | Networks                 |     |     |
| --- | ---------------------- | ------------------------ | --- | --- |
|     | ▪  Visual inspections  | ▪  Auto encoders         |     |     |
|     | in production lines    | ▪  Restricted Boltzmann  |     |     |
Machine
Natural  ▪  Electronic Health  ▪  Text Classification  ▪  Extracts insights from  ▪  Requires large,
Language  Record Analysis  Algorithms  unstructured clinical  diverse datasets

Processing  ▪  Automating  ▪  Named Entity  notes and data    that cover the
[110, 111]
|     | clinical               | Recognition             |                           | medical        |
| --- | ---------------------- | ----------------------- | ------------------------- | -------------- |
|     | documentation          | ▪  Sentiment Analysis   |                           | terminology.   |
|     | ▪  Virtual Assistant   | ▪  Topic Modeling       |                           |                |
|     | support for patient    | ▪  Machine Translation  |                           |                |
|     | education              |                         |                           |                |
|     | ▪  Virtual assistants  | ▪  Text Summarization   | ▪  Analyze large volumes  | ▪  Requires a  |
|     | to educate             | ▪  Machine Translation  | of text                   | substantial    |

consumers  ▪  Topic Modeling  ▪  Extracts effective  amount of labeled
[112, 113]
  ▪  Energy  ▪  Sentiment Analysis  summaries  data for training.
|     | management  |     |     | ▪  Context   |
| --- | ----------- | --- | --- | ------------ |
|     | reports     |     |     | sensitivity  |
▪  Customer
feedback analysis
▪  Summaries of
energy
consumption
▪  Analyzing  ▪  Text Summarization  ▪  Enhances information  ▪  Large volumes of
  industry reports  ▪  Machine Translation  retrieval  domain-specific
|     | ▪  Automating  |     |     | data required   |
| --- | -------------- | --- | --- | --------------- |
[114, 115]
|     | quality control  |     |     |     |
| --- | ---------------- | --- | --- | --- |

documentation
Reinforcement  ▪  Personalized  ▪  Deep Q-Networks  ▪  Adaptive learning with  ▪  Requires large data
Learning  treatment plans  ▪  Policy Gradient  feedback  and long training.

| [116,117]  | ▪  Resource  | Methods          |     |     |
| ---------- | ------------ | ---------------- | --- | --- |
|            | management   | ▪  Actor-Critic  |     |     |
Algorithms
▪  Proximal Policy
Optimization
VOLUME XX, 2017  7
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3516500

▪  Demand-response  ▪  Deep Q-Networks  ▪  Can dynamically adjust  ▪  High resource
|     |     | management  | ▪  Policy Gradient  | strategies for  | usage during  |
| --- | --- | ----------- | ------------------- | --------------- | ------------- |

|     |     | ▪  Optimal  | Methods  | fluctuating energy  | training  |
| --- | --- | ----------- | -------- | ------------------- | --------- |
[118]
  configurations for  ▪  Actor-Critic  demand response  ▪  Safety and

|     |     | maximizing        | Algorithms          | patterns | reliability  |
| --- | --- | ----------------- | ------------------- | -------- | ------------ |
|     |     | renewable energy  | ▪  Proximal Policy  |          | concerns     |
|     |     | resources         | Optimization        |          |              |
|     |     | ▪  Smart grid     |                     |          |              |
management
▪  Automate  ▪  Proximal Policy  ▪  Optimizes  ▪ Requires precise
|     |     | manufacturing  | Optimization  | resource  | environment  |
| --- | --- | -------------- | ------------- | --------- | ------------ |
|     |     |                |               |           |              |
[119,120]  processes under  ▪  Actor-Critic  allocation  modeling
|     |     | dynamic             | Algorithms          | ▪  Effective in  |     |
| --- | --- | ------------------- | ------------------- | ---------------- | --- |
|     |     | environments        | ▪  Policy Gradient  | dynamic          |     |
|     |     | ▪  Route planning,  | Methods             | environments     |     |
|     |     | inventory           |                     |                  |     |
management
resource allocation
in the supply chain
|     |     | ▪   | ▪   | ▪   | ▪   |
| --- | --- | --- | --- | --- | --- |
Big Data  Health Informatics  Distributed storage  Manage large volumes  Issues with
| Analytics  |     | ▪  Disease  | and processing  | of data  | privacy and  |
| ---------- | --- | ----------- | --------------- | -------- | ------------ |

Surveillance  ▪  Cluster computing  ▪  Real-time data  regulatory
[78]
|     |     |     | system               | processing             | compliance  |
| --- | --- | --- | -------------------- | ---------------------- | ----------- |
|     |     |     | ▪  Data Warehousing  | ▪  Heterogeneous data  |             |
|     |     |     | ▪  Cloud Computing   | integration            |             |
▪  Visualize complex
healthcare data
▪  Energy market  ▪  Distributed data  ▪  Facilitates real-time  ▪  Data privacy and
|     |     | analysis  | processing  | analytics  | regulatory  |
| --- | --- | --------- | ----------- | ---------- | ----------- |

|     |     | ▪  Demand response  | ▪  Stream processing  | ▪  Integrates diverse data  | concerns  |
| --- | --- | ------------------- | --------------------- | --------------------------- | --------- |
[91]
|     |     | analysis  | framework  | sources  |     |
| --- | --- | --------- | ---------- | -------- | --- |
▪  Analyze  ▪  Stream Processing  ▪  Identifies patterns in  ▪  Dependence on
|     |     | manufacturing  | ▪  Predictive Analytics  | the manufacturing  | data quality    |
| --- | --- | -------------- | ------------------------ | ------------------ | --------------- |
|     |     |                |                          |                    |                 |
|     |     | data           | Models                   | process            |                 |
[94, 97]
|     |     | ▪  Tracking supply  |     |     |     |
| --- | --- | ------------------- | --- | --- | --- |
chain
Robotics  ▪  Robotic surgery  ▪  Reinforcement  ▪  Enhances precision in  ▪  High cost
|     |     | ▪  Robotic  | Learning  | surgery  | ▪  Ethical concerns  |
| --- | --- | ----------- | --------- | -------- | -------------------- |

|     |     | rehabilitation  | ▪  Motion Planning  | ▪  Minimally invasive,  |     |
| --- | --- | --------------- | ------------------- | ----------------------- | --- |
[118]
|     |     |     | Algorithms  | improving patient  |     |
| --- | --- | --- | ----------- | ------------------ | --- |

recovery time.
|     |     | ▪  Maintenance of  | ▪  Robotic Process  | ▪  Minimizes downtime in  | ▪  Limited     |
| --- | --- | ------------------ | ------------------- | ------------------------- | -------------- |
|     |     | renewable energy   | Automation          | maintenance tasks         | operations in  |

|     | [122]  | sources  | Algorithms  |     | unknown  |
| --- | ------ | -------- | ----------- | --- | -------- |
environments

▪  Automating  ▪  Motion Planning  ▪  Enhances production  ▪  Vulnerable to

|     |     | industrial  | Algorithms  | efficiency  | security threats  |
| --- | --- | ----------- | ----------- | ----------- | ----------------- |

|     | [123]  | processes           | ▪  Autonomous  | ▪  Reduces waste  |     |
| --- | ------ | ------------------- | -------------- | ----------------- | --- |
|     |        | ▪  Maintenance and  | navigation     |                   |     |

Inspection
▪  Quality control
Connected  ▪  Tele medicine  ▪  Chatbots with NLP  ▪   Expands access to care  ▪  Data security and

Devices (IoT)  ▪  Virtual  ▪  Video-based  in remote areas.  privacy concerns.

[121]  consultations  diagnostics  ▪  Reduces requirements
|     |     | ▪  Patient remote  | ▪  Predictive analytics  | on healthcare    |     |
| --- | --- | ------------------ | ------------------------ | ---------------- | --- |
|     |     | monitoring         | models                   | infrastructure.  |     |
▪  Smart meters  ▪  Adaptive data routing  ▪  Improves energy  ▪  Requires robust
|     |     | ▪  Energy  | ▪  Predictive  | efficiency  | security measures  |
| --- | --- | ---------- | -------------- | ----------- | ------------------ |

|     |     | management  | Maintenance  | ▪  Supports demand-side  |     |
| --- | --- | ----------- | ------------ | ------------------------ | --- |
[122]
|     |     | systems  |     | management  |     |
| --- | --- | -------- | --- | ----------- | --- |
▪  Smart  ▪  Edge Computing  ▪  Improves operational  ▪  Security issues
|     |     | manufacturing and  | ▪  Reliable  | efficiency    |     |
| --- | --- | ------------------ | ------------ | ------------- | --- |

|     |     | automation  | communication  |     |     |
| --- | --- | ----------- | -------------- | --- | --- |
[123]
|     |     | ▪  Smart city  | ▪  Authentication  |     |     |
| --- | --- | -------------- | ------------------ | --- | --- |
infrastructure
▪
Urban planning
|     |     |     | C.  | ROLE OF INTERDISCIPLINARY APPROACHES IN  |     |
| --- | --- | --- | --- | ---------------------------------------- | --- |
ACHIEVING SDGs (RQ3)
VOLUME XX, 2017  7
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3516500
Interdisciplinary approaches that integrate big data and make real-time decisions. If these data are manipulated or
AI enhance the achievement of the SDGs by utilizing corrupted, it can lead to incorrect decisions, resulting in
expertise from diverse fields. For SDG3, a collaborative operational failures or safety hazards.
effort among healthcare professionals, biologists,
pharmacists, public health workers, data scientists, and AI To address these ethical and security issues, healthcare
organizations must use data privacy frameworks. In
engineers enhances health outcomes. Healthcare
healthcare systems, patients should be informed about how
professionals, including doctors and nurses, help data
their data will be used and the risks involved. It is mandatory
scientists identify the most relevant health data for analysis.
to invest in cybersecurity measures to protect sensitive
Biologists and pharmacists provide their knowledge of
information and conduct regular security audits to find
human biology and drug interactions, which is important for
vulnerabilities in these systems.
new drug discovery. Public health workers collect data on
health trends within communities, which data scientists then
E. IMPLICATIONS FOR PRACTICE (RQ4)
analyze to forecast potential outbreaks and identify risk Big data techniques and advanced algorithms have the
factors. AI engineers design algorithms that can handle large following implications for practice in healthcare, energy
amounts of health data to create predictive models. management, manufacturing, urban planning, and
interdisciplinary research.
In SDG7, engineers design renewable energy systems to
Healthcare: For SDG3, the use of machine learning
ensure a more reliable energy supply. Environmental
algorithms such as support vector machines and XGBoost
scientists provide information on the ecological impacts of
has revolutionized diagnostic processes, enabling earlier
energy production and provide insights into the sustainability
and more accurate diagnoses. Additionally, deep learning
of renewable energy. These insights can help engineers and
models can analyze medical images with high accuracy,
policymakers create energy solutions that minimize
reducing the time healthcare professionals spend on data
ecological harm. Data scientists and AI engineers analyze processing. NLP and LLMs assist in interpreting clinical
real-time data to forecast various factors, such as energy notes, benefiting the healthcare team and providing tools for
demand and resource utilization. They also provide decision patient education.
support to improve energy management and efficiency. The integration of neurosymbolic AI into healthcare
Similarly, engineers, environmental scientists, data practice holds significant potential for improving patient
scientists, AI engineers, urban planners, and architects work outcomes and enhancing clinical decision-making. By
together to achieve SDG9 by integrating their diverse providing more interpretable AI models, healthcare providers
expertise in building resilient infrastructure and promoting can better trust AI-driven decisions, particularly in complex
sustainable industrialization. cases such as neurodegenerative diseases and cancer [124].
With the potential for personalized medicine, neurosymbolic
D. ETHICAL AND SECURITY CHALLENGES IN BIG
AI processes large datasets, such as genetic and imaging data,
DATA AND AI FOR SDG IMPLEMENTATION (RQ5)
to provide tailored treatment recommendations while ensuring
healthcare providers understand the reasoning behind AI
Data privacy and informed consent are important ethical
decisions [125]. A significant challenge in neurosymbolic AI
issues in healthcare when AI is used. These systems collect
is the complexity of combining neural networks with symbolic
such personal health information to improve treatments and
reasoning. This process involves ensuring seamless interaction
predict disease conditions. However, many patients do not between these two AI components, which can be difficult due
know how their data might be shared. This lack of to the differing nature of learning and reasoning mechanisms
understanding can lead to distrust in healthcare systems. [126]. Data interoperability is another major challenge, as
Additionally, owing to the sensitive nature of healthcare healthcare data comes in various formats, including imaging
data, these data can be vulnerable to cyber threats. Wearable data, clinical notes, and genetic information.
sensors often send data over wireless networks, which can be This integration has led to improved patient outcomes and
attacked. If the data is not properly encrypted while being more personalized treatment plans. However, integrating
transmitted, it may lead to unauthorized access, putting these technologies raises critical questions about the
sensitive health information at risk. transparency and fairness of the algorithms used, especially
given their potential to impact life-altering decisions. The
In the context of SDG7, data security threats are critical ethical implications and the need for robust, transparent
in areas such as smart grids, where interconnected devices frameworks to integrate these technologies into healthcare
depend on real-time data for monitoring and control. systems present vital areas for ongoing research. GAI could
Cyberattacks targeting these systems can result in significant enhance healthcare by generating synthetic data and
disruptions to the power supply and damage to infrastructure. simulations for training, improving diagnostics, and
Additionally, in SDG9, applications such as industrial accelerating drug development.
automation rely on data from various sensors and devices to
VOLUME XX, 2017 7
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3516500

Energy Management: For SDG7, AI-driven smart grids  With respect to BERT topic modeling, we recognize its ability
and renewable energy sources are recommended to utilize  to process extensive datasets and identify central themes. By
machine learning and deep learning algorithms for data trend  creating cohesive topic representations through semantic word
analysis  and  predictions.  Adaptive  decision-making  is  and phrase similarities, topic modeling reduces human bias in
achieved  through  feedback-based  techniques  such  as  topic classification, thereby enhancing the objectivity and
dependability of the outcomes [127]. However, the efficacy of
reinforcement learning. AI systems can be utilized to predict
equipment  failures,  schedule  maintenance,  and  forecast  topic modeling algorithms can be influenced by the quality of
the input data and the underlying assumptions of their design.
| energy  | demands  | while  | dynamically  |     | managing  |     | loads.  |     |     |     |     |     |     |     |     |
| ------- | -------- | ------ | ------------ | --- | --------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
Additionally, these systems can be used to improve smart  Furthermore, mapping publications to SDGs is a complex
metering, enabling consumers to monitor their energy usage  task, and our analysis acknowledges the shortcomings of
relying solely on a particular SDG mapping approach [128].
| in  real-time  | and  | developing  |     | energy-saving  |     | behaviors.  |     |     |     |     |     |     |     |     |     |
| -------------- | ---- | ----------- | --- | -------------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
However, these systems rely heavily on the quality and  For future research, comparing our findings with results from
|     |     |     |     |     |     |     |     | various  | SDG  | mapping  | initiatives  | could  | offer  | a   | more  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---- | -------- | ------------ | ------ | ------ | --- | ----- |
integrity of data, making the scalability and reliability of
these algorithms a major area for future research. Addressing  comprehensive  perspective  and  increase  the  reliability  of
future studies.
| the  limitations  |     | related  | to  | data  | quality  | and  algorithm  |     |     |     |     |     |     |     |     |     |
| ----------------- | --- | -------- | --- | ----- | -------- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
performance in diverse operational environments is crucial
CONCLUSION AND FUTURE DIRECTIONS
to advancing sustainable energy management. The GAI’s
The application of big data and AI, specifically through
| predictive  | models     | could  |            | optimize  | the   | integration  | of   |                   |     |              |       |                  |        |            |      |
| ----------- | ---------- | ------ | ---------- | --------- | ----- | ------------ | ---- | ----------------- | --- | ------------ | ----- | ---------------- | ------ | ---------- | ---- |
|             |            |        |            |           |       |              |      | sophisticated     |     | algorithms,  | is    | revolutionizing  |        | practices  |      |
| renewable   | energies,  |        | enhancing  |           | grid  | efficiency   | and  |                   |     |              |       |                  |        |            |      |
|             |            |        |            |           |       |              |      | across  multiple  |     | sectors      | that  | impact           | SDG3,  | SDG7,      | and  |
sustainability.
SDG9. First, our findings demonstrate that AI-powered
Manufacturing: The integration of AI in Industry 4.0  systems  for  disease  prediction  and  diagnosis  markedly
increase the quality and accessibility of healthcare, thereby
| offers  important  |     | practical  | implications  |     | across  | a   | range  of  |               |     |      |              |     |       |            |     |
| ------------------ | --- | ---------- | ------------- | --- | ------- | --- | ---------- | ------------- | --- | ---- | ------------ | --- | ----- | ---------- | --- |
|                    |     |            |               |     |         |     |            | contributing  | to  | the  | realization  | of  | SDG3  | [70][75].  |     |
applications. AI-driven tools can also be employed for project
scheduling  and  resource  optimization.  Virtual  assistants  Moreover,  the  results  indicated  that  AI-powered  smart
|          |                |     |        |       |           |          |     | grids  and  | energy  | management  |     | systems  | are  | driving  | the  |
| -------- | -------------- | --- | ------ | ----- | --------- | -------- | --- | ----------- | ------- | ----------- | --- | -------- | ---- | -------- | ---- |
| enhance  | collaboration  |     | among  | team  | members,  | leading  | to  |             |         |             |     |          |      |          |      |
improved productivity. By automating the generation of status  development  of  more  adaptive  and  efficient  energy
systems, thereby contributing to the realization of SDG7
| reports,  | AI  provides  |     | real-time  | updates  |     | to  make  | quick  |     |     |     |     |     |     |     |     |
| --------- | ------------- | --- | ---------- | -------- | --- | --------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
[69][85]. Furthermore, the application of AI in Industry 4.0,
decisions. Additionally, safety awareness can be enhanced
through predictive analytics of hazards before they occur.  such  as  predictive  maintenance  and  supply  chain
|     |     |     |     |     |     |     |     | optimization,  |     | contributes  | to  | SDG9  | [100][102].  |     | In  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------------ | --- | ----- | ------------ | --- | --- |
Automation in quality control processes helps to maintain
product standards and reduce defects. AI enables predictive  conclusion, applying big data and AI in interdisciplinary
research and sustainable development presents significant
| maintenance  | and         | optimizes  |                | supply  | chains,  | leading   | to   |          |               |              |     |                |     |             |     |
| ------------ | ----------- | ---------- | -------------- | ------- | -------- | --------- | ---- | -------- | ------------- | ------------ | --- | -------------- | --- | ----------- | --- |
|              |             |            |                |         |          |           |      | ethical  | and  privacy  | challenges,  |     | necessitating  |     | a  balance  |     |
| significant  | efficiency  |            | improvements.  |         |          | However,  | the  |          |               |              |     |                |     |             |     |
scalability of these AI solutions is a major concern, as is  between  harnessing  technology  for  public  benefit  and
|     |     |     |     |     |     |     |     | protecting  | individual  |     | privacy.  | Technology  |     | facilitates  | a   |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ----------- | --- | --------- | ----------- | --- | ------------ | --- |
their ability to maintain performance across different scales
and setups. Future research should focus on developing  deeper  understanding  and  ability  to  act  on  complex
|     |     |     |     |     |     |     |     | datasets,  | improving  |     | efficiency,  | personalization,  |     |     | and  |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ---------- | --- | ------------ | ----------------- | --- | --- | ---- |
robust AI solutions that can be scaled without loss of
predictive capabilities in healthcare, urban planning, and
efficiency or accuracy, a critical step toward fully realizing
Industry 4.0.  energy management. Importantly, while big data and AI
technology can potentially transform many aspects of our
Urban Planning: For SDG9, applying GIS and machine
learning algorithms in urban planning enhances the ability  lives, there are also associated risks. These risks include
ethical implications, data privacy, and the potential for bias
to predict and plan effectively for urban growth. However,
in algorithmic decisions.
| the  use  | of  these  |     | technologies  |     | introduces  | significant  |     |     |     |     |     |     |     |     |     |
| --------- | ---------- | --- | ------------- | --- | ----------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
challenges  related  to  data  privacy  and  the  ethical  To effectively harness the potential of big data and AI for
|     |     |     |     |     |     |     |     | advancing  | the  | SDGs,  | this  | study  | highlights  |     | key  |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ---- | ------ | ----- | ------ | ----------- | --- | ---- |
management of surveillance data. Future research must
address the balance between leveraging AI for public goods  recommendations. Additionally, addressing ethical concerns
around data privacy and security is critical, especially in
| and  protecting  |     | individual  |     | privacy  | rights,  | ensuring  | that  |     |     |     |     |     |     |     |     |
| ---------------- | --- | ----------- | --- | -------- | -------- | --------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
sectors that handle sensitive information. The development of
urban planning practices remain innovative and ethical.
The GAI could simulate urban development and traffic  robust privacy frameworks and transparent AI algorithms is
essential for ensuring public trust. Finally, interdisciplinary
| systems,  | aiding  | planners  |     | in  creating  |     | more  efficient,  |     |     |     |     |     |     |     |     |     |
| --------- | ------- | --------- | --- | ------------- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
sustainable cities.  collaboration  among  data  scientists,  engineers,  healthcare
|      |           |      |          |               |     |       |            | professionals, and policymakers is crucial  |            |             |     |              | for developing  |               |     |
| ---- | --------- | ---- | -------- | ------------- | --- | ----- | ---------- | ------------------------------------------- | ---------- | ----------- | --- | ------------ | --------------- | ------------- | --- |
| Our  | research  | has  | certain  | limitations.  |     | When  | selecting  |                                             |            |             |     |              |                 |               |     |
|      |           |      |          |               |     |       |            | scalable                                    | AI-driven  | strategies  |     | to  address  | the             | multifaceted  |     |
publications via the PRISMA framework, there is a risk of
inherent bias stemming from the specific database chosen.
| VOLUME XX, 2017  |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 7   |
| ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3516500
challenges posed by the SDGs and foster sustainable no. 53, p. 102104, Aug. 2020, doi:
https://doi.org/10.1016/j.ijinfomgt.2020.102104.
development.
[3] M. Lowe, R. Qin, and X. Mao, “A Review on Machine Learning,
Future Research Directions: Several future directions Artificial Intelligence, and Smart Technology in Water Treatment and
are provided as follows. First, future research can continue Monitoring,” Water, vol. 14, no. 9, p. 1384, Jan. 2022, doi:
to develop transparent and fair AI algorithms and integrate https://doi.org/10.3390/w14091384.
[4] D. Rangel-Martinez, K. D. P. Nigam, and L. A. Ricardez-Sandoval,
these technologies into a robust framework within
“Machine learning on sustainable energy: A review and outlook on
healthcare systems. For example, [85] proposed the use of renewable energy systems, catalysis, smart grid and energy
machine learning and data fusion techniques to analyze storage,” Chemical Engineering Research and Design, vol. 174, pp.
414–441, Oct. 2021, doi: https://doi.org/10.1016/j.cherd.2021.08.013.
manufacturing datasets for detecting quality events and
[5] M. Wählisch, “Big Data, New Technologies, and Sustainable Peace:
enhancing process monitoring. The emerging field of AI- Challenges and Opportunities for the UN,” Journal of Peacebuilding
driven predictive genomics opens exciting prospects for & Development, vol. 15, no. 1, p. 154231661986898, Aug. 2019, doi:
https://doi.org/10.1177/1542316619868984.
precision medicine. Ensuring that AI recommendations are
[6] M. Naeem et al., “Trends and Future Perspective Challenges in Big
explainable and interpretable requires transparent models Data,” Advances in Intelligent Data Analysis and Applications, vol.
and ethical frameworks. AI-enabled simulations could 253, pp. 309–325, Nov. 2021, Available:
https://link.springer.com/chapter/10.1007/978-981-16-5036-9_30
accelerate drug discovery and enhance clinical decision-
[7] A. Adadi, “A Survey on Data‐efficient Algorithms in Big Data
making.
Era,” Journal of Big Data, vol. 8, no. 1, Jan. 2021, doi:
Second, future research can enhance the scalability, https://doi.org/10.1186/s40537-021-00419-9.
resource efficiency, and reliability of AI models, particularly [8] A. Holzinger, K. Keiblinger, P. Holub, K. Zatloukal, and H. Müller,
“AI for life: Trends in artificial intelligence for biotechnology,” New
in the healthcare and energy sectors, where technologies such
Biotechnology, vol. 74, pp. 16–24, May 2023, doi:
as neurosymbolic AI and quantum neural networks show https://doi.org/10.1016/j.nbt.2023.02.001.
promise but remain underexplored. Integrating quantum [9] H. Luan et al., “Challenges and Future Directions of Big Data and
Artificial Intelligence in Education,” Frontiers in Psychology, vol. 11,
learning for cybersecurity, self-configuring architectures,
no. 11, Oct. 2020, doi: https://doi.org/10.3389/fpsyg.2020.580820.
and AI for preventive maintenance is pivotal given current [10] S. Yu and J. Ma, “Deep Learning for Geophysics: Current and Future
threats. The use of distributed big data analytics and Trends,” Reviews of Geophysics, vol. 59, no. 3, Jul. 2021, doi:
https://doi.org/10.1029/2021rg000742.
imbalanced data classification to improve the reliability
[11] C. Caudai et al., “AI applications in functional genomics,”
and efficiency of smart grids [82]. AI can improve grid Computational and Structural Biotechnology Journal, vol. 19, pp.
reliability and resilience, especially with real-time 5762–5790, 2021, doi: https://doi.org/10.1016/j.csbj.2021.10.009.
optimization. Optimizing renewable energy infrastructure [12] L. E. Mansuri and D. A. Patel, “Artificial intelligence-based automatic
visual inspection system for built heritage,” Smart and Sustainable
through AI can also mitigate environmental impacts.
Built Environment, vol. ahead-of-print, no. ahead-of-print, Feb. 2021,
Third, the advancement of Industry 4.0 through the doi: https://doi.org/10.1108/sasbe-09-2020-0139.
application of big data and AI is suggested. [86] discussed [13] Ó. Álvarez-Machancoses, E. J. DeAndrés Galiana, A. Cernea, J.
Fernández de la Viña, and J. L. Fernández-Martínez, “On the Role of
the potential for leveraging big data and AI to optimize the
Artificial Intelligence in Genomics to Enhance Precision Medicine,”
intelligent automation and operational management of Pharmacogenomics and Personalized Medicine, vol. 13, pp. 105–119,
large-scale enterprise cloud data centers. Future research Mar. 2020, doi: https://doi.org/10.2147/PGPM.S205082.
[14] G. Furano et al., “Towards the Use of Artificial Intelligence on the
could further explore the development of scalable AI
Edge in Space Systems: Challenges and Opportunities,” IEEE
solutions that can be adapted to different industrial Aerospace and Electronic Systems Magazine, vol. 35, no. 12, pp. 44–
applications and maintain efficiency and accuracy— 56, Dec. 2020, doi: https://doi.org/10.1109/MAES.2020.3008468.
[15] M. R. Dobbelaere, P. P. Plehiers, R. Van de Vijver, C. V. Stevens, and
coordinated demand forecasting in supply chains and
K. M. Van Geem, “Machine Learning in Chemical Engineering:
deployed logistics automation tools to streamline
Strengths, Weaknesses, Opportunities, and Threats,” Engineering,
industrialization processes. vol. 7, no. 9, Jul. 2021, doi: https://doi.org/10.1016/j.eng.2021.03.019.
It is also important to balance leveraging AI to benefit [16] L. Sun, Z. Shang, Y. Xia, S. Bhowmick, and S. Nagarajaiah, “Review
of Bridge Structural Health Monitoring Aided by Big Data and
the public and protect individual privacy rights. [116]
Artificial Intelligence: From Condition Assessment to Damage
explored how the Internet of Things and edge computing Detection,” Journal of Structural Engineering, vol. 146, no. 5, p.
drove the development of smart manufacturing systems 04020073, May 2020, doi: https://doi.org/10.1061/(asce)st.1943-
541x.0002535..
while emphasizing the challenges in privacy protection.
[17] Zoran Babović et al., “Research in computing-intensive simulations
Further studies can be conducted on a mechanism that for nature-oriented civil-engineering and related scientific fields,
promotes innovation and provides sound ethical and using machine learning and big data: an overview of open problems,”
Journal of Big Data, vol. 10, no. 1, May 2023, doi:
privacy protection.
https://doi.org/10.1186/s40537-023-00731-6.
[18] Miroslav Kosanic and V. Milutinovic, “A Survey on Mathematical
REFERENCES Aspects of Machine Learning in GeoPhysics: The Cases of Weather
[1] Y. Xu et al., “Artificial Intelligence: a Powerful Paradigm for Forecast, Wind Energy, Wave Energy, Oil and Gas Exploration,”
Scientific Research,” The Innovation, vol. 2, no. 4, Oct. 2021, doi: arXiv (Cornell University), Jun. 2021, doi:
https://doi.org/10.1016/j.xinn.2021.100179. https://doi.org/10.1109/meco52532.2021.9460245.
[2] R. Nishant, M. Kennedy, and J. Corbett, “Artificial intelligence for [19] J. T. Hancock, T. M. Khoshgoftaar, and J. M. Johnson, “Evaluating
sustainability: Challenges, opportunities, and a research classifier performance with highly imbalanced Big Data,” Journal of
agenda,” International Journal of Information Management, vol. 53, Big Data, vol. 10, no. 1, Apr. 2023, doi:
https://doi.org/10.1186/s40537-023-00724-5.
VOLUME XX, 2017 7
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3516500
[20] J. Hancock, H. Wang, T. M. Khoshgoftaar, and Q. Liang, “Data [38] D. Si, “A Framework to analyze the Impacts of AI with the Sustainable
reduction techniques for highly imbalanced medicare Big Development Goals,” Highlights in Science, Engineering and
Data,” Journal of Big Data, vol. 11, no. 1, Jan. 2024, doi: Technology, vol. 17, pp. 313–323, Nov. 2022, doi:
https://doi.org/10.1186/s40537-023-00869-3. https://doi.org/10.54097/hset.v17i.2621.
[21] F. F. Costa, “Big data in biomedicine,” Drug Discovery Today, vol. [39] M.-L. How, S.-M. Cheah, Y.-J. Chan, A. C. Khor, and E. M. P. Say,
19, no. 4, pp. 433–440, Apr. 2014, doi: “Artificial Intelligence-Enhanced Decision Support for Informing
https://doi.org/10.1016/j.drudis.2013.10.012. Global Sustainable Development: A Human-Centric AI-Thinking
[22] Zhao, L., Ciallella, H. L., Aleksunes, L. M., & Zhu, H. “Advancing Approach,” Information, vol. 11, no. 1, p. 39, Jan. 2020, doi:
computer-aided drug discovery (CADD) by big data and data-driven https://doi.org/10.3390/info11010039.
machine learning modeling,” Drug Discovery Today, vol. 25, no. 9, [40] L. Fan, J. Li, and X. P. Zhang, Machine learning load prediction
pp. 1624–1638, Sep. 2020, doi: methods for home energy management systems based on human
https://doi.org/10.1016/j.drudis.2020.07.005. behavior patterns recognition,” CSEE Journal of Power and Energy
[23] Z. Engin et al., “Data-driven urban management: Mapping the Systems, 2020, doi: https://doi.org/10.17775/cseejpes.2018.01130.
landscape,” Journal of Urban Management, vol. 9, no. 2, pp. 140–150, [41] R. Raman, hiran lathabhai, Сантану Мандал, C. Kumar, and Prema
Jun. 2020, doi: https://doi.org/10.1016/j.jum.2019.12.001. Nedungadi, “Contribution of Business Research to Sustainable
[24] J. Kandt and M. Batty, “Smart cities, big data and urban policy: Development Goals: Bibliometrics and Science Mapping Analysis,”
Towards urban analytics for the long run,” Cities, vol. 109, no. Sustainability, vol. 15, no. 17, pp. 12982–12982, Aug. 2023, doi:
102992, p. 102992, Nov. 2020, doi: https://doi.org/10.3390/su151712982.
https://doi.org/10.1016/j.cities.2020.102992. [42] R. Raman et al., “Mapping sustainability reporting research with the
[25] D. Mhlanga, “Artificial Intelligence in the Industry 4.0, and Its Impact UN’s sustainable development goal,” Heliyon, vol. 9, no. 8, pp.
on Poverty, Innovation, Infrastructure Development, and the e18510–e18510, Aug. 2023, doi:
Sustainable Development Goals: Lessons from Emerging https://doi.org/10.1016/j.heliyon.2023.e18510.
Economies?,” Sustainability, vol. 13, no. 11, p. 5788, May 2021, doi: [43] V. K. Singh, P. Singh, M. Karmakar, J. Leta, and P. Mayr, “The journal
https://doi.org/10.3390/su13115788. coverage of Web of Science, Scopus and Dimensions: A comparative
[26] R. Kusters et al., “Interdisciplinary Research in Artificial Intelligence: analysis,” Scientometrics, vol. 126, no. 6, pp. 5113–5142, Mar. 2021,
Challenges and Opportunities,” Frontiers in Big Data, vol. 3, Nov. doi: https://doi.org/10.1007/s11192-021-03948-5.
2020, doi: https://doi.org/10.3389/fdata.2020.577974. [44] ANZSCO, Australian and New Zealand Standard Classification of
[27] J. Bajorath, “Artificial intelligence in interdisciplinary life science and Occupations (ANZSCO), Version 1.2, Australian Bureau of Statistics,
drug discovery research,” Future Science OA, vol. 8, no. 4, Apr. 2022, Canberra, 2013.
doi: https://doi.org/10.2144/fsoa-2022-0010. [45] R. Raman et al., “Fake news research trends, linkages to generative
[28] N. M. Safdar, J. D. Banja, and C. C. Meltzer, “Ethical Considerations artificial intelligence and sustainable development goals,” Heliyon, vol.
in Artificial Intelligence,” European Journal of Radiology, vol. 122, 10, no. 3, p. e24727, Feb. 2024, doi:
no. 1, p. 108768, Jan. 2020, Available: https://doi.org/10.1016/j.heliyon.2024.e24727.
https://www.sciencedirect.com/science/article/pii/S0720048X193041 [46] R. Raman, D. Pattnaik, C. Kumar, and P. Nedungadi, “Advancing
88 sustainable energy systems: A decade of SETA research contribution to
[29] B. Murdoch, “Privacy and Artificial Intelligence: Challenges for sustainable development goals,” Sustainable Energy Technologies and
Protecting Health Information in a New Era,” BMC Medical Ethics, Assessments, vol. 71, p. 103978, Nov. 2024, doi:
vol. 22, no. 1, Sep. 2021, doi: https://doi.org/10.1186/s12910-021- https://doi.org/10.1016/j.seta.2024.103978.
00687-3. [47] R. Raman et al., “Mapping research in the Journal of Innovation &
[30] J. M. Johnson and T. M. Khoshgoftaar, “Data-Centric AI for Healthcare Knowledge to sustainable development goals,” Journal of Innovation &
Fraud Detection,” SN Computer Science, vol. 4, no. 4, May 2023, doi: Knowledge, vol. 9, no. 3, p. 100538, Jul. 2024, doi:
https://doi.org/10.1007/s42979-023-01809-x. https://doi.org/10.1016/j.jik.2024.100538.
[31] D. Liu, H. Kong, X. Luo, W. Liu, and R. Subramaniam, “Bringing AI [48] N. J. van Eck and L. Waltman, “Software survey: VOSviewer, a
to edge: From deep learning’s perspective,” Neurocomputing, vol. 485, computer program for bibliometric mapping,” Scientometrics, vol. 84,
pp. 297–320, May 2022, doi: no. 2, pp. 523–538, Dec. 2010, doi: https://doi.org/10.1007/s11192-
https://doi.org/10.1016/j.neucom.2021.04.141. 009-0146-3.
[32] S. Weixing, L.-F. Li, F. Liu, M. He, and L. Lin, “AI on the edge: a [49] R. Egger and J. Yu, “A Topic Modeling Comparison Between LDA,
comprehensive review,” Artificial Intelligence Review, vol. 55, no. 8, NMF, Top2Vec, and BERTopic to Demystify Twitter Posts,” Frontiers
pp. 6125–6183, Mar. 2022, doi: https://doi.org/10.1007/s10462-022- in Sociology, vol. 7, May 2022, doi:
10141-4. https://doi.org/10.3389/fsoc.2022.886498.
[33] R. Walshe, A. Koene, S. Baumann, M. Panella, L. Maglaras, and F. [50] Maarten Grootendorst, “BERTopic: Neural topic modeling with a class-
Medeiros, “Artificial Intelligence as Enabler for Sustainable based TF-IDF procedure,” arXiv (Cornell University), Mar. 2022, doi:
Development,” 2021 IEEE International Conference on Engineering, https://doi.org/10.48550/arxiv.2203.05794.
Technology and Innovation (ICE/ITMC), Jun. 2021, doi: [51] J. Devlin, M.-W. Chang, K. Lee, and K. Toutanova, “BERT: Pre-
https://doi.org/10.1109/ice/itmc52061.2021.9570215. training of Deep Bidirectional Transformers for Language
[34] Z. Chen, M. Wu, A. Chan, X. Li, and Y.-S. Ong, “Survey on AI Understanding,” arXiv.org, May 24, 2019.
Sustainability: Emerging Trends on Learning Algorithms and Research https://arxiv.org/abs/1810.04805#
Challenges [Review Article],” IEEE Computational Intelligence [52] Andry Alamsyah and Nadhif Ditertian Girawan, “Improving Clothing
Magazine, vol. 18, no. 2, pp. 60–77, May 2023, doi: Product Quality and Reducing Waste Based on Consumer Review
https://doi.org/10.1109/mci.2023.3245733. Using RoBERTa and BERTopic Language Model,” Big data and
[35] F. Rohde, M. Gossen, J. Wagner, and T. Santarius, “Sustainability cognitive computing, vol. 7, no. 4, pp. 168–168, Oct. 2023, doi:
challenges of Artificial Intelligence and Policy Implications,” https://doi.org/10.3390/bdcc7040168.
Ökologisches Wirtschaften - Fachzeitschrift, vol. 36, no. O1, pp. 36–40, [53] J. Yi, Yun Kyung Oh, and J.-M. Kim, “Unveiling the drivers of
Feb. 2021, doi: https://doi.org/10.14512/oewo360136. satisfaction in mobile trading: Contextual mining of retail investor
[36] H. Guo, H. Hackmann, and K. Gong, “Big data in support of the experience through BERTopic and generative AI,” Journal of Retailing
Sustainable Development Goals: a celebration of the establishment of and Consumer Services, vol. 82, pp. 104066–104066, Jan. 2025, doi:
the International Research Center of Big Data for Sustainable https://doi.org/10.1016/j.jretconser.2024.104066.
Development Goals (CBAS),” Big Earth Data, vol. 5, no. 3, pp. 259– [54] Yun Kyung Oh, J. Yi, and J.-D. Kim, “What enhances or worsens the
262, Jul. 2021, doi: https://doi.org/10.1080/20964471.2021.1962621. user-generated metaverse experience? An application of BERTopic to
[37] Rishikesh Bamdale, S. Shelar, and V. Khandekar, “How to tackle Roblox user eWOM,” Internet Research, Dec. 2023, doi:
Climate Change using Artificial Intelligence,” Jul. 2021, doi: https://doi.org/10.1108/intr-03-2022-0178.
https://doi.org/10.1109/icccnt51525.2021.9579674.
VOLUME XX, 2017 7
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3516500
[55] K. Kim, D. F. Kogler, and Sira Maliphol, “Identifying interdisciplinary [75] Habeeb Omotunde and M. R. Mouhamed, “The Modern Impact of
emergence in the science of science: combination of network analysis Artificial Intelligence Systems in Healthcare: A Concise Analysis,”
and BERTopic,” Humanities and Social Sciences Communications, vol. Mesopotamian Journal of Artificial Intelligence in Healthcare, vol.
11, no. 1, May 2024, doi: https://doi.org/10.1057/s41599-024-03044-y. 2023, pp. 66–70, Nov. 2023, doi:
[56] Khodeir, N., & Elghannam, F. (2024). Efficient topic identification for https://doi.org/10.58496/mjaih/2023/013.
urgent MOOC Forum posts using BERTopic and traditional topic [76] V. Gupta, S. Sachdeva, and S. Bhalla, “A Novel Deep Similarity
modeling techniques. Education and Information Technologies, 1-27. Learning Approach to Electronic Health Records Data,” IEEE Access,
[57] McInnes, L., Healy, J., & Melville, J. (2018). UMAP: Uniform pp. 1–1, 2020, doi: https://doi.org/10.1109/access.2020.3037710.
Manifold Approximation and Projection for Dimension Reduction. [77] M. Elbes, S. AlZu’bi, T. Kanan, A. Mughaid, and S. Abushanab, “Big
[58] Lyutov, A., Uygun, Y., & Hütt, M. T. (2024). Machine learning dermatological data service for precise and immediate diagnosis by
misclassification networks reveal a citation advantage of utilizing pre-trained learning models,” Cluster Computing, vol. 27, no.
interdisciplinary publications only in high-impact journals. Scientific 5, pp. 6931–6951, Mar. 2024, doi: https://doi.org/10.1007/s10586-024-
Reports, 14(1), 21906. 04331-8.
[59] Capra L (2024) A computational linguistic approach to study border [78] M. Ye, H. Zhang, and L. Li, “Research on Data Mining Application of
theory at scale. ACM Trans Comput-Hum Interaction 37(4):1–23 Orthopedic Rehabilitation Information for Smart Medical,” IEEE
[60] G. Castellanos, C. Jing, J. Chen, and H. Chen, “Identifying Access, vol. 7, pp. 177137–177147, 2019, doi:
interdisciplinary topics and their evolution based on BERTopic,” https://doi.org/10.1109/access.2019.2957579.
Scientometrics, Jul. 2023, doi: https://doi.org/10.1007/s11192-023- [79] N. Ahmad, Z. Ullah, Hyungseo Bobby Ryu, A. Ariza-Montes, and H.
04776-5. Han, “From Corporate Social Responsibility to Employee Well-Being:
[61] V. O. K. Li, J. C. K. Lam, and J. Cui, “AI for Social Good: AI and Big Navigating the Pathway to Sustainable Healthcare,” Psychology
Data Approaches for Environmental Decision-Making,” Environmental Research and Behavior Management, vol. Volume 16, no. 16, pp. 1079–
Science & Policy, vol. 125, pp. 241–246, Nov. 2021, doi: 1095, Apr. 2023, doi: https://doi.org/10.2147/prbm.s398586.
https://doi.org/10.1016/j.envsci.2021.09.001. [80] Sriya Kanamarlapudi, Venkata Santhosh Yakkala, Badisa Gayathri,
[62] R. Lokers, R. Knapen, S. Janssen, Y. van Randen, and J. Jansen, Krishna Vamsi Nusimala, S. S. Aravinth, and S Srithar, “Comparison
“Analysis of Big Data technologies for use in agro-environmental and Analysis of Various Machine Learning Algorithms for Disease
science,” Environmental Modelling & Software, vol. 84, pp. 494–504, Prediction,” Feb. 2023, doi:
Oct. 2016, doi: https://doi.org/10.1016/j.envsoft.2016.07.017. https://doi.org/10.1109/iccmc56507.2023.10083509.
[63] S. E. Bibri, A. Alexandre, A. Sharifi, and J. Krogstie, “Environmentally [81] G. Braswell, “Artificial Intelligence Comes of Age in Oil and Gas,”
sustainable smart cities and their converging AI, IoT, and big data Journal of Petroleum Technology, vol. 65, no. 01, pp. 50–57, Jan. 2013,
technologies and solutions: an integrated approach to an extensive doi: https://doi.org/10.2118/0113-0050-jpt.
literature review,” Energy Informatics, vol. 6, no. 1, Apr. 2023, doi: [82] H. Wang, M. Xiao, C. Wu, and J. Zhang, “Distributed classification for
https://doi.org/10.1186/s42162-023-00259-2. imbalanced big data in distributed environments,” Wireless Networks,
[64] D. Kamrowska-Załuska, “Impact of AI-Based Tools and Urban Big Feb. 2021, doi: https://doi.org/10.1007/s11276-021-02552-y.
Data Analytics on the Design and Planning of Cities,” Land, vol. 10, [83] H. Dong, W. Hongkai, W. Xiaohua, H. Haichao, M. Shule, and G.
no. 11, p. 1209, Nov. 2021, doi: https://doi.org/10.3390/land10111209. Yang, “Log fusion technology of power information system based on
[65] M. Maisonobe, “The future of urban models in the Big Data and AI era: fuzzy reasoning,” 2020 International Conference on Virtual Reality and
a bibliometric analysis (2000–2019),” AI & SOCIETY, Mar. 2021, doi: Intelligent Systems (ICVRIS), vol. 43, pp. 296–299, Jul. 2020, doi:
https://doi.org/10.1007/s00146-021-01166-4. https://doi.org/10.1109/icvris51417.2020.00076.
[66] L. H. Kaack, P. L. Donti, E. Strubell, G. Kamiya, F. Creutzig, and D. [84] Qu Xiaoyun, Kang Xiaoning, Zhang Chao, Jiang Shuai, and Ma Xiuda,
Rolnick, “Aligning artificial intelligence with climate change “Short-term prediction of wind power based on deep Long Short-Term
mitigation,” Nature Climate Change, vol. 12, no. 6, pp. 518–527, Jun. Memory,” 2016 IEEE PES Asia-Pacific Power and Energy Engineering
2022, doi: https://doi.org/10.1038/s41558-022-01377-7. Conference (APPEEC), Oct. 2016, doi:
[67] K. Zhang and A. B. Aslan, “AI technologies for education: Recent https://doi.org/10.1109/appeec.2016.7779672.
research & future directions,” Computers and Education: Artificial [85] Katarina Grolinger, Miriam, and L. Seewald, “Energy Consumption
Intelligence, vol. 2, no. 100025, p. 100025, Jun. 2021, doi: Prediction with Big Data: Balancing Prediction Accuracy and
https://doi.org/10.1016/j.caeai.2021.100025. Computational Resources,” International Congress on Big Data, Jun.
[68] K. G. Srinivasa, M. Kurni, and K. Saritha, “Harnessing the Power of AI 2016, doi: https://doi.org/10.1109/bigdatacongress.2016.27.
to Education,” Springer Texts in Education, pp. 311–342, 2022. [86] M. A. Hanif, R. Hafiz, M. U. Javed, S. Rehman, and M. Shafique,
[69] T. Ahmad et al., “Artificial Intelligence in Sustainable Energy industry: “Energy-Efficient Design of Advanced Machine Learning Hardware,”
Status Quo, Challenges and Opportunities,” Journal of Cleaner Springer eBooks, pp. 647–678, Jan. 2019, doi:
Production, vol. 289, no. 289, p. 125834, Mar. 2021, doi: https://doi.org/10.1007/978-3-030-04666-8_21.
https://doi.org/10.1016/j.jclepro.2021.125834. [87] Mohd Saqib Akhoon et al., “High performance accelerators for deep
[70] P. Rajpurkar, E. Chen, O. Banerjee, and E. J. Topol, “AI in health and neural networks: A review,” Expert Systems, vol. 39, no. 1, Oct. 2021,
medicine,” Nature Medicine, vol. 28, no. 1, pp. 31–38, Jan. 2022, doi: doi: https://doi.org/10.1111/exsy.12831.
https://doi.org/10.1038/s41591-021-01614-0. [88] Z. Wang, Shamma Nasrin, R. Islam, A. Haque, and Muhammed,
[71] S. Qazi, B. A. Khawaja, and Q. U. Farooq, “IoT-Equipped and AI- “Emerging memories and their applications in neuromorphic
Enabled Next Generation Smart Agriculture: A Critical Review, computing,” Elsevier eBooks, pp. 305–357, Jan. 2023, doi:
Current Challenges and Future Trends,” IEEE Access, vol. 10, pp. https://doi.org/10.1016/b978-0-323-91832-9.00005-1.
21219–21235, 2022, doi: https://doi.org/10.1109/access.2022.3152544. [89] G. Wu, Z. Xu, H. Zhang, S. Shen, and S. Yu, “Multi-agent DRL for
[72] M. A. Abdel-Fattah, N. A. Othman, and N. Goher, “Predicting Chronic joint completion delay and energy consumption with queuing theory in
Kidney Disease Using Hybrid Machine Learning Based on Apache MEC-based IIoT,” vol. 176, pp. 80–94, Jun. 2023, doi:
Spark,” Computational Intelligence and Neuroscience, vol. 2022, pp. 1– https://doi.org/10.1016/j.jpdc.2023.02.008.
12, Feb. 2022, doi: https://doi.org/10.1155/2022/9898831. [90] Z. Shi, X. Xie, S. Garg, H. Lu, H. Yang, and Z. Xiong, “Deep
[73] Saad Almutairi, S. Manimurugan, B.-G. Kim, Majed Aborokbah, and Reinforcement Learning Based Big Data Resource Management for
C. Narmatha, “Breast cancer classification using Deep Q Learning 5G/6G Communications,” 2021 IEEE Global Communications
(DQL) and gorilla troops optimization (GTO),” Applied Soft Conference (GLOBECOM), pp. 01–06, Dec. 2021, doi:
Computing, vol. 142, pp. 110292–110292, Jul. 2023, doi: https://doi.org/10.1109/globecom46510.2021.9685098.
https://doi.org/10.1016/j.asoc.2023.110292. [91] X. Zhao, Y. Zhang, and M. Li, “Task Migration Optimization
[74] A. Mittal, L. Dumka, and L. Mohan, “A Comprehensive Review on the Algorithm in Mobile Edge Computing,” pp. 133–137, Jun. 2023, doi:
Use of Artificial Intelligence in Mental Health Care,” Jul. 2023, doi: https://doi.org/10.1145/3605801.3605827.
https://doi.org/10.1109/icccnt56998.2023.10308255. [92] I. Ul Haq, S. Anwar, and T. Khan, “Machine Vision Based Predictive
Maintenance for Machine Health Monitoring: A Comparative
VOLUME XX, 2017 7
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3516500
Analysis,” IEEE Xplore, Mar. 01, 2023. Energies, vol. 17, no. 8, pp. 1935–1935, Apr. 2024, doi:
https://ieeexplore.ieee.org/document/10089572/ (accessed Apr. 26, https://doi.org/10.3390/en17081935.
2023). [111] C. Wu et al., “Natural language processing for smart construction:
[93] K. M. Baalamurugan and Aanchal Phutela, “A Brief Study of Adaptive Current status and future directions,” Automation in Construction, vol.
Clustering for Self-aware Machine Analytics,” Disruptive technologies 134, p. 104059, Feb. 2022, doi:
and digital transformations for society 5.0, pp. 49–69, Jan. 2024, doi: https://doi.org/10.1016/j.autcon.2021.104059.
https://doi.org/10.1007/978-981-99-8118-2_3. [112] N. Tyagi and B. Bhushan, “Demystifying the Role of Natural Language
[94] M. G. Kibria, K. Nguyen, G. P. Villardi, O. Zhao, K. Ishizu, and F. Processing (NLP) in Smart City Applications: Background, Motivation,
Kojima, “Big Data Analytics, Machine Learning, and Artificial Recent Advances, and Future Research Directions,” Wireless Personal
Intelligence in Next-Generation Wireless Networks,” IEEE Access, vol. Communications, Mar. 2023, doi: https://doi.org/10.1007/s11277-023-
6, pp. 32328–32338, 2018, doi: 10312-8.
https://doi.org/10.1109/access.2018.2837692. [113] Alaa Awad Abdellatif, Naram Mhaisen, A. Mohamed, Aiman Erbad,
[95] Y. Zhang, Y. Zhou, H. Lu, and H. Fujita, “Traffic Network Flow and Mohsen Guizani, “Reinforcement Learning for Intelligent
Prediction Using Parallel Training for Deep Convolutional Neural Healthcare Systems: A Review of Challenges, Applications, and Open
Networks on Spark Cloud,” IEEE Transactions on Industrial Research Issues,” IEEE internet of things journal (Online), vol. 10, no.
Informatics, vol. 16, no. 12, pp. 7369–7380, Feb. 2020, doi: 24, pp. 21982–22007, Dec. 2023, doi:
https://doi.org/10.1109/tii.2020.2976053. https://doi.org/10.1109/jiot.2023.3288050.
[96] M. Abbasi, M. Plaza-Hernandez, J. Prieto, and J. M. Corchado, [114] Y. Chen, S. Han, G. Chen, J. Yin, Kate Nana Wang, and J. Cao, “A deep
“Security in the Internet of Things Application Layer: Requirements, reinforcement learning-based wireless body area network offloading
Threats, and Solutions,” IEEE Access, vol. 10, pp. 97197–97216, 2022, optimization strategy for healthcare services,” Health information
doi: https://doi.org/10.1109/access.2022.3205351. science and systems, vol. 11, no. 1, Jan. 2023, doi:
[97] D. Jeong, “Road Damage Detection Using YOLO with Smartphone https://doi.org/10.1007/s13755-023-00212-3.
Images,” 2020 IEEE International Conference on Big Data (Big Data), [115] Fisayo Sangoleye, J. Jao, K. Faris, Eirini Eleni Tsiropoulou, and
Dec. 2020, doi: https://doi.org/10.1109/bigdata50022.2020.9377847. Symeon Papavassiliou, “Reinforcement Learning-Based Demand
[98] F. Sun, A. Dubey, and J. White, “DxNAT — Deep neural networks for Response Management in Smart Grid Systems With Prosumers,” IEEE
explaining non-recurring traffic congestion,” 2017 IEEE International Systems Journal, vol. 17, no. 2, pp. 1797–1807, Mar. 2023, doi:
Conference on Big Data (Big Data), Dec. 2017, doi: https://doi.org/10.1109/jsyst.2023.3248320.
https://doi.org/10.1109/bigdata.2017.8258162. [116] L. Yun, D. Wang, and L. Li, “Explainable multi-agent deep
[99] N. Thillaiarasu, S. Lata Tripathi, and V. Dhinakaran, Artificial reinforcement learning for real-time demand response towards
Intelligence for Internet of Things. Boca Raton: CRC Press, 2022. doi: sustainable manufacturing,” Applied energy, vol. 347, pp. 121324–
https://doi.org/10.1201/9781003335801. 121324, Oct. 2023, doi:
[100] G. Feng and A. Li, “Intelligent Automated Operation and Operation https://doi.org/10.1016/j.apenergy.2023.121324.
Management of Large Enterprise Cloud Data Center Based on Artificial [117] Y. Wang, F. Shang, J. Lei, X. Zhu, H. Qin, and J. Wen, “Dual-attention
Intelligence,” Advances in intelligent systems and computing, pp. 531– assisted deep reinforcement learning algorithm for energy-efficient
538, Jan. 2021, doi: https://doi.org/10.1007/978-981-16-1726-3_65. resource allocation in Industrial Internet of Things,” Future Generation
[101] C. A. Escobar, D. Macias, and R. Morales-Menendez, “Process Computer Systems, vol. 142, pp. 150–164, May 2023, doi:
monitoring for quality — A multiple classifier system for highly https://doi.org/10.1016/j.future.2022.12.009.
unbalanced data,” Heliyon, vol. 7, no. 10, p. e08123, Oct. 2021, doi: [118] N. Deo and A. Anjankar, “Artificial Intelligence With Robotics in
https://doi.org/10.1016/j.heliyon.2021.e08123. Healthcare: A Narrative Review of Its Viability in India,” Artificial
[102] L. Variz, L. Piardi, P. J. Rodrigues, and P. Leitao, “Machine Learning Intelligence With Robotics in Healthcare: A Narrative Review of Its
Applied to an Intelligent and Adaptive Robotic Inspection Station,” Viability in India, vol. 15, no. 5, May 2023, doi:
2019 IEEE 17th International Conference on Industrial Informatics https://doi.org/10.7759/cureus.39416.
(INDIN), Jul. 2019, doi: [119] Z. Qin, Z. D. Xu, Q. C. Sun, P. Poovendran, and P. Balamurugan,
https://doi.org/10.1109/indin41052.2019.8972298. “Investigation of Intelligent Substation Inspection Robot by Using
[103] B. C. Wu, “IC Test Quality Enhancement by Introducing Machine Mobile Data,” International Journal of Humanoid Robotics, May 2022,
Learning,” 2019 Joint International Symposium on e-Manufacturing & doi: https://doi.org/10.1142/s0219843622400035.
Design Collaboration(eMDC) & Semiconductor Manufacturing [120] Prasenjit Bhadra, S. Chakraborty, and S. Saha, “Cognitive IoT Meets
(ISSM), vol. 106, pp. 1–4, Sep. 2019, doi: Robotic Process Automation: The Unique Convergence
https://doi.org/10.23919/emdc/issm48219.2019.9052135. Revolutionizing Digital Transformation in the Industry 4.0 Era,” Smart
[104] Garcez and L. C. Lamb, “Neurosymbolic AI: the 3rd wave,” Mar. 2023, Innovation, Systems and Technologies, pp. 355–388, Jan. 2023, doi:
doi: https://doi.org/10.1007/s10462-023-10448-w. https://doi.org/10.1007/978-981-19-8296-5_15.
[105] J. Varghese and J. Chapiro, “ChatGPT: The transformative influence of [121] F. Subhan et al., “AI-Enabled Wearable Medical Internet of Things in
generative AI on science and healthcare,” Journal of Hepatology, Aug. Healthcare System: A Survey,” Applied Sciences, vol. 13, no. 3, p.
2023, doi: https://doi.org/10.1016/j.jhep.2023.07.028. 1394, Jan. 2023, doi: https://doi.org/10.3390/app13031394.
[106] P. Zhang and Maged, “Generative AI in Medicine and Healthcare: [122] M. Khalid, “Energy 4.0: AI-enabled digital transformation for
Promises, Opportunities and Challenges,” Future Internet, vol. 15, no. sustainable power networks,” Computers & industrial engineering, pp.
9, pp. 286–286, Aug. 2023, doi: https://doi.org/10.3390/fi15090286. 110253–110253, May 2024, doi:
[107] E. Hossain et al., “Use of ai/ml-enabled state-of-the-art method in https://doi.org/10.1016/j.cie.2024.110253.
electronic medical records: A systematic review,” Computers in [123] M. Soori, B. Arezoo, and R. Dastres, “Internet of things for smart
Biology and Medicine, vol. 155, p. 106649, Feb. 2023, doi: factories in industry 4.0, a review,” Internet of Things and Cyber-
https://doi.org/10.1016/j.compbiomed.2023.106649. Physical Systems, vol. 3, pp. 192–204, 2023, doi:
[108] Y. Juhn and H. Liu, “Artificial intelligence approaches using natural https://doi.org/10.1016/j.iotcps.2023.04.006.
language processing to advance EHR-based clinical research,” Journal [124] H. Goswami and P. Kumar, “Is Artificial Intelligence a Helping Hand
of Allergy and Clinical Immunology, vol. 145, no. 2, pp. 463–469, Feb. for the Future of Neurosurgery?,” 2021 5th International Conference on
2020, doi: https://doi.org/10.1016/j.jaci.2019.12.897. Information Systems and Computer Networks (ISCON), Oct. 2021, doi:
[109] J. Aguilar, A. Garces-Jimenez, M. D. R-Moreno, and R. García, “A https://doi.org/10.1109/iscon52037.2021.9702473.
systematic literature review on the use of artificial intelligence in energy [125] T. Feng, “Applications of Artificial Intelligence to Diagnosis of
self-management in smart buildings,” Renewable and Sustainable Neurodegenerative Diseases,” Studies in health technology and
Energy Reviews, vol. 151, p. 111530, Nov. 2021, doi: informatics, Nov. 2023, doi: https://doi.org/10.3233/shti230896.
https://doi.org/10.1016/j.rser.2021.111530. [126] Z. Lu, I. Afridi, H. J. Kang, I. Ruchkin, and X. Zheng, “Surveying
[110] Amali Matharaarachchi et al., “Optimizing Generative AI Chatbots for neuro-symbolic approaches for reliable artificial intelligence of things,”
Net-Zero Emissions Energy Internet-of-Things Infrastructure,”
VOLUME XX, 2017 7
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3516500

| Journal  of  Reliable  | Intelligent  Environments,  | Jul.  2024,  | doi:    |
| ---------------------- | --------------------------- | ------------ | ------- |
https://doi.org/10.1007/s40860-024-00231-1.
| [127] T. Kimura, “Virtual Teams: A Smart Literature Review of Four  |     |     |     |
| ------------------------------------------------------------------- | --- | --- | --- |
Decades of Research,” Human behavior and emerging technologies,

| vol.  2024,  | pp.  1–20,  | Feb.  2024,  | doi:    |
| ------------ | ----------- | ------------ | ------- |
https://doi.org/10.1155/2024/8373370.

[128] R. Raman, V. K. Nair, and P. Nedungadi, “Discrepancies in Mapping

| Sustainable  Development  | Goal 3  (Good  | Health  and  Well-Being)  |     |
| ------------------------- | -------------- | ------------------------- | --- |

| Research:  A  Comparative  | Analysis  | of  Scopus  and  Dimensions  |     |
| -------------------------- | --------- | ---------------------------- | --- |
Databases,” Sustainability, vol. 15, no. 23, p. 16413, Jan. 2023, doi:
https://doi.org/10.3390/su152316413.
VOLUME XX, 2017  7
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/

This article has been accepted for publication in IEEE Access. This is the author's version which has not been fully edited and
content may change prior to final publication. Citation information: DOI 10.1109/ACCESS.2024.3516500
PREMA NEDUNGADI received a Ph.D. degree KAI-YU TANG received his Ph.D. from National
in Computer Science and Engineering from Chiao Tung University. He is an Associate
Amrita Vishwa Vidyapeetham, India. She is the Professor at the Graduate Institute of Library &
Director of the Amrita Center for Research in Information Science, National Chung Hsing
Analytics, Technologies & Education University, Taiwan. His research interests include
(AmritaCREATE), Amrita University, and a electronic commerce, computational thinking, and
Professor at the Amrita School of Computing, social network analysis. His research papers have
Amrita Vishwa Vidyapeetham, India. She is a been published in Computers & Education,
recipient of the Digital India Award from the Electronic Commerce Research and Applications,
Ministry of Electronics and Information Educational Technology Research and
Technology, India, in the category of digital Development, the International Journal of
empowerment. She was a finalist in the U.S. $7 million Barbara Bush Computer-Supported Collaborative Learning, Scientometrics, Telematics
Foundation Adult Literacy XPRIZE Competition. and Informatics, and the International Journal of Information Management.
RAGHU RAMAN received a Ph.D. degree in
Management from Amrita Vishwa
Vidyapeetham, India, and an M.B.A. degree
from the Haas School of Business, UC
SIMI SURENDRAN is an Assistant Professor (Sr. Gr.) and Vice-Chair, Berkeley, Berkeley, CA, USA. He is currently
CSE(AI) at the School of Computing, Amrita Vishwa Vidyapeetham, the Dean of the School of Business, Amrita
Amritapuri. She received her Ph. D. in Wireless Vishwa Vidyapeetham. He has over 30 years of
Networks and Applications from Amrita Vishwa executive management experience at a variety
Vidyapeetham, India. She has an M.Tech degree of Fortune 500 companies and has been with
in Wireless network and Applications from Amrita Amrita Vishwa Vidyapeetham since its
Vishwa Vidyapeetham, India, and a B.Tech founding in 2003. He established the Center for
degree in Computer Science and Engineering from Research in Analytics and Technologies for Education (CREATE), with
Mahatma Gandhi University, India. She was also over U.S. $5 million in research funding. He was a recipient of the President
selected as a candidate for the Erasmus of India Gold Medal in 1986. He serves on the Board of Directors for Amrita
International Credit Mobility Program at the Technology Business Incubator. He is the Past Chair of the IEEE Education
University of Trento, Italy, as part of the Ph.D. Society Chapter India.
program. Her research interests are in networking
in extreme environments, stochastic algorithms,
predictive analytics, and reinforcement learning. In collaboration with the
University of Trento, she has published papers in reputed journals and
conferences in the field of wireless networks with a particular emphasis on
predictive analytics.
8 VOLUME XX, 2017
This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/
