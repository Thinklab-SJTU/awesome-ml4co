

# Awesome Machine Learning for Combinatorial Optimization Resources
We would like to maintain a list of resources that utilize machine learning technologies to solve combinatorial optimization problems.

We mark work contributed by [Thinklab](http://thinklab.sjtu.edu.cn) with ⭐.

*Maintained by members in SJTU-Thinklab: Chang Liu, Runzhong Wang, Jiayi Zhang, Zelin Zhao, Haoyu Geng, Tianzhe Wang, Wenxuan Guo, Wenjie Wu, Nianzu Yang and Junchi Yan. We also thank [all contributers from the community](https://github.com/Thinklab-SJTU/awesome-ml4co/graphs/contributors)!*

*We are looking for post-docs interested in machine learning especially for learning combinatorial solvers, dynamic graphs, and reinforcement learning. Please send your up-to-date resume via yanjunchi AT sjtu.edu.cn.*

## [Content](#content)

<table>
<tr><td colspan="2"><a href="#survey-papers">1. Survey</a></td></tr>
<tr><td colspan="2"><a href="#problems">2. Problems</a></td></tr> 
<tr>
	<td>&emsp;<a href=#graph-matching>2.1 Graph Matching (GM)</a></td>
	<td>&emsp;<a href=#quadratic-assignment-problem>2.2 Quadratic Assignment Problem (QAP)</a></td>
</tr>
<tr>
	<td>&emsp;<a href=#travelling-salesman-problem>2.3 Travelling Salesman Problem (TSP)</a></td>
	<td>&emsp;<a href=#maximal-cut>2.4 Maximal Cut</a></td>
</tr>
<tr>
	<td>&emsp;<a href=#differentiable-optimization>2.5 Differentiable Optimization</a></td>
	<td>&emsp;<a href=#vehicle-routing-problem>2.6 Vehicle Routing Problem (VRP)</a></td>
</tr>
<tr>
	<td>&emsp;<a href=#job-shop-scheduling-problem>2.7 Job Shop Scheduling Problem (JSSP)</a></td>
	<td>&emsp;<a href=#maximal/maximum-independent-set>2.8 Maximal/Maximum Independent Set</a></td>
</tr>
<tr>
	<td>&emsp;<a href=#generalization>2.9 Generalization</a></td>
	<td>&emsp;<a href=#computing-resource-allocation>2.10 Computing Resource Allocation</a></td>
</tr>
<tr>
	<td>&emsp;<a href=#bin-packing-problem>2.11 Bin Packing Problem (BPP)</a></td>
	<td>&emsp;<a href=#graph-edit-distance>2.12 Graph Edit Distance (GED)</a></td>
</tr>
<tr>
	<td>&emsp;<a href=#hamiltonian-cycle-problem>2.13 Hamiltonian Cycle Problem (HCP)</a></td>
	<td>&emsp;<a href=#graph-coloring>2.14 Graph Coloring</a></td>
</tr>
<tr>
	<td>&emsp;<a href=#maximal-common-subgraph>2.15 Maximal Common Subgraph (MCS)</a></td>
	<td>&emsp;<a href=#influence-maximization>2.16 Influence Maximization</a></td>
</tr>
<tr>
	<td>&emsp;<a href=#boolean-satisfiability>2.17 Boolean Satisfiability (SAT)</a></td>
	<td>&emsp;<a href=#mixed-integer-programming>2.18 Mixed Integer Programming</a></td>
</tr>
<tr>
	<td>&emsp;<a href=#causal-discovery>2.19 Causal Discovery</a></td>
	<td>&emsp;<a href=#game-theoretic-semantics>2.20 Game Theoretic Semantics</a></td>
</tr>
<tr>
	<td>&emsp;<a href=#car-dispatch>2.21 Car Dispatch</a></td>
	<td>&emsp;<a href=#electronic-design-automation>2.22 Electronic Design Automation (EDA)</a></td>
</tr>
<tr>
	<td>&emsp;<a href=#conjunctive-query-containment>2.23 Conjunctive Query Containment</a></td>
	<td>&emsp;<a href=#orienteering-problem>2.24 Orienteering Problem (OP)</a></td>
</tr>
<tr>
	<td>&emsp;<a href=#virtual-network-embedding>2.25 Virtual Network Embedding (VNE)</a></td>
	<td>&emsp;<a href=#optical-power-flow>2.26 Optical Power Flow (OPF)</a></td>
</tr>
<tr>
	<td>&emsp;<a href=#facility-location-problem>2.27 Facility Location Problem (FLP)</a></td>
	<td>&emsp;<a href=#portfolio-optimization>2.28 Portfolio Optimization (PortOpt)</a></td>
</tr>
<tr>
	<td>&emsp;<a href=#sorting-&-ranking>2.29 Sorting & Ranking (Sort&Rank)</a></td>
	<td>&emsp;<a href=#knapsack>2.30 Knapsack</a></td>
</tr>
<tr>
	<td>&emsp;<a href=#combinatorial-drug-recommendation>2.31 Combinatorial Drug Recommendation</a></td>
<td>&ensp;</td>
</tr>
</table>




### [Survey Papers](#content)

1. **Neural Networks for Combinatorial Optimization: A Review of More Than a Decade of Research** INFORMS Journal on Computing, 1999. [journal](https://pubsonline.informs.org/doi/abs/10.1287/ijoc.11.1.15)

    *Smith, Kate A.*

2. **Model-Based Search for Combinatorial Optimization: A Critical Survey.** Annals of Operations Research, 2004. [journal](https://link.springer.com/article/10.1023/B:ANOR.0000039526.52305.af)

    *Zlochin, Mark and Birattari, Mauro and Meuleau, Nicolas and Dorigo, Marco.*

3. **A Survey of Reinforcement Learning and Agent-Based Approaches to Combinatorial Optimization.** Citeseer, 2012. [journal](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.468.5208&rep=rep1&type=pdf)

    *Miagkikh, Victor*

4. **Machine Learning Approaches to Learning Heuristics for Combinatorial Optimization Problems.** Procedia Manufacturing, 2018. [journal](https://www.sciencedirect.com/science/article/pii/S2351978918311351)

    *Mirshekarian, Sadegh and Sormaz, Dusan.*

5. **Boosting combinatorial problem modeling with machine learning.** IJCAI, 2018. [paper](https://www.ijcai.org/Proceedings/2018/0772.pdf)

    *Lombardi, Michele and Milano, Michela.*

6. **Deep Reinforcement Learning as a Job Shop Scheduling Solver: A Literature Review** Hybrid Intelligent Systems, 2018. [journal](http://link.springer.com/10.1007/978-3-030-14347-3_34)

    *Bruno Cunha, Ana M. Madureira, Benjamim Fonseca, Duarte Coelho*

7. **A Review of combinatorial optimization with graph neural networks.** BigDIA, 2019. [paper](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8802843)

    *Huang, Tingfei and Ma, Yang and Zhou, Yuzhen and Huang, Honglan Huang and Chen, Dongmei and Gong, Zidan and Liu, Yao.*

8. **Machine Learning for Combinatorial Optimization: a Methodological Tour d'horizon.** EJOR, 2020. [journal](https://arxiv.org/abs/1811.06128)

    *Bengio, Yoshua and Lodi, Andrea and Prouvost, Antoine.*

9. **Reinforcement Learning for Combinatorial Optimization: A Survey.** Arxiv, 2020. [paper](https://arxiv.org/abs/2003.03600)

    *Mazyavkina, Nina and Sviridov, Sergey and Ivanov, Sergei and Burnaev, Evgeny.*

10. **⭐Learning Graph Matching and Related Combinatorial Optimization Problems.** IJCAI, 2020. [paper](https://www.ijcai.org/proceedings/2020/0694.pdf)

    *Yan, Junchi and Yang, Shuang, and Hancock, Edwin R.*

11. **Learning Combinatorial Optimization on Graphs: A Survey with Applications to Networking.** IEEE ACCESS, 2020. [journal](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9125934)

    *Vesselinova, Natalia and Steinert, Rebecca and Perez-Ramirez, Daniel F. and Boman, Magnus.*

12. **From Shallow to Deep Interactions Between Knowledge Representation, Reasoning and Machine Learning.** Arxiv, 2020. [paper](https://arxiv.org/abs/1912.06612)

    *Bouraoui, Zied and Cornuéjols, Antoine and Denœux, Thierry and Destercke, Sébastien and Dubois, Didier and Guillaume, Romain and Marques-Silva, João and Mengin, Jérôme and Prade, Henri and Schockaert, Steven and Serrurier, Mathieu and Vrain, Christel.*

13. **A Survey on Reinforcement Learning for Combinatorial Optimization.** Arxiv, 2020. [paper](https://arxiv.org/abs/2008.12248v2)

    *Yang, Yunhao and Whinston, Andrew.*

14. **Research Reviews of Combinatorial Optimization Methods Based on Deep Reinforcement Learning. (in chinese)** 自动化学报, 2020. [journal](http://www.aas.net.cn/article/doi/10.16383/j.aas.c200551)

    *Li, Kai-Wen and Zhang,  Tao and Wang, Rui and Qin, Wei-Jian and He, Hui-Hui and Huang, Hong.*

15. **Graph Learning for Combinatorial Optimization: A Survey of State-of-the-Art.** Data Science and Engineering, 2021. [journal](https://link.springer.com/article/10.1007/s41019-021-00155-3)

    *Peng, Yue, Choi, Byron, and Xu, Jianliang.*

16. **Combinatorial Optimization and Reasoning with Graph Neural Networks** Arxiv, 2021. [paper](https://arxiv.org/abs/2102.09544)

    *Cappart, Quentin and Chetelat, Didier and Khalil, Elias and Lodi, Andrea and Morris, Christopher and Velickovic, Petar*

17. **Machine Learning for Electronic Design Automation (EDA) : A Survey** TODAES, 2021. [journal](https://arxiv.org/abs/2102.03357)

    *Huang, Guyue and Hu, Jingbo and He, Yifan and Liu, Jialong and Ma, Mingyuan and Shen, Zhaoyang and Wu, Juejian and Xu, Yuanfan and Zhang, Hengrui and Zhong, Kai and others*

18. **⭐A Survey for Solving Mixed Integer Programming via Machine Learning** Neurocomputing, 2022. [journal](https://www.sciencedirect.com/science/article/pii/S0925231222014035)

    *Jiayi Zhang and Chang Liu and Xijun Li and Hui-Ling Zhen and Mingxuan Yuan and Yawen Li and Junchi Yan*

## [Problems](#content)

### [Graph Matching](#content)

1. **Revised Note on Learning Algorithms for Quadratic Assignment with Graph Neural Networks** Arxiv, 2017. [paper](https://arxiv.org/pdf/1706.07450.pdf), [code](https://github.com/alexnowakvila/QAP_pt)

    *Nowak, Alex and Villar, Soledad and Bandeira, S. Afonso and Bruna, Joan*

2. **Deep Learning of Graph Matching.** CVPR, 2018. [paper](https://openaccess.thecvf.com/content_cvpr_2018/html/Zanfir_Deep_Learning_of_CVPR_2018_paper.html)

    *Zanfir, Andrei and Sminchisescu, Cristian*

3. **⭐Learning Combinatorial Embedding Networks for Deep Graph Matching.** ICCV, 2019. [paper](http://openaccess.thecvf.com/content_ICCV_2019/papers/Wang_Learning_Combinatorial_Embedding_Networks_for_Deep_Graph_Matching_ICCV_2019_paper.pdf), [code](https://github.com/Thinklab-SJTU/ThinkMatch)

    *Wang, Runzhong and Yan, Junchi and Yang, Xiaokang*

4. **Deep Graphical Feature Learning for the Feature Matching Problem.** ICCV, 2019. [paper](https://openaccess.thecvf.com/content_ICCV_2019/papers/Zhang_Deep_Graphical_Feature_Learning_for_the_Feature_Matching_Problem_ICCV_2019_paper.pdf)

    *Zhang, Zhen and Lee, Wee Sun*

5. **GLMNet: Graph Learning-Matching Networks for Feature Matching.** Arxiv, 2019. [paper](https://arxiv.org/abs/1911.07681)

    *Jiang, Bo and Sun, Pengfei and Tang, Jin and Luo, Bin*

6. **⭐Learning deep graph matching with channel-independent embedding and Hungarian attention.** ICLR, 2020. [paper](https://openreview.net/forum?id=rJgBd2NYPH), [code](https://github.com/Thinklab-SJTU/ThinkMatch)

    *Yu, Tianshu and Wang, Runzhong and Yan, Junchi and Li, Baoxin*

7. **Deep Graph Matching Consensus.** ICLR, 2020. [paper](http://arxiv.org/abs/2001.09621)

    *Fey, Matthias and Lenssen, Jan E. and Morris, Christopher and Masci, Jonathan and Kriege, Nils M.*

8. **⭐Graduated Assignment for Joint Multi-Graph Matching and Clustering with Application to Unsupervised Graph Matching Network Learning.** NeurIPS, 2020. [paper](https://papers.NeurIPS.cc/paper/2020/file/e6384711491713d29bc63fc5eeb5ba4f-Paper.pdf), [code](https://github.com/Thinklab-SJTU/ThinkMatch)

    *Wang, Runzhong and Yan, Junchi and Yang, Xiaokang*

9. **⭐Combinatorial Learning of Robust Deep Graph Matching: An Embedding Based Approach.** TPAMI, 2020. [paper](https://doi.org/10.1109/TPAMI.2020.3005590), [code](https://github.com/Thinklab-SJTU/ThinkMatch)

    *Wang, Runzhong and Yan, Junchi and Yang, Xiaokang*

10. **Deep Graph Matching via Blackbox Differentiation of Combinatorial Solvers.** ECCV, 2020. [paper](https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123730409.pdf), [code](https://github.com/martius-lab/blackbox-deep-graph-matching)

    *Rolinek, Michal and Swoboda, Paul and Zietlow, Dominik and Paulus, Anselm and Musil, Vit and Martius, Georg*

11. **⭐Neural Graph Matching Network: Learning Lawler's Quadratic Assignment Problem with Extension to Hypergraph and Multiple-graph Matching.** TPAMI, 2021. [paper](https://arxiv.org/abs/1911.11308), [code](https://github.com/Thinklab-SJTU/ThinkMatch)

    *Wang, Runzhong and Yan, Junchi and Yang, Xiaokang*

12. **⭐Deep Latent Graph Matching** ICML, 2021. [paper](http://proceedings.mlr.press/v139/yu21d/yu21d.pdf)

    *Yu, Tianshu and Wang, Runzhong and Yan, Junchi and Li, Baoxin.*

13. **IA-GM: A Deep Bidirectional Learning Method for Graph Matching** AAAI, 2021. [paper](https://ojs.aaai.org/index.php/AAAI/article/view/16461/16268)

    *Zhao, Kaixuan and Tu, Shikui and Xu, Lei*

14. **Deep Graph Matching under Quadratic Constraint** CVPR, 2021. [paper](https://openaccess.thecvf.com/content/CVPR2021/papers/Gao_Deep_Graph_Matching_Under_Quadratic_Constraint_CVPR_2021_paper.pdf)

    *Gao, Quankai and Wang, Fudong and Xue, Nan and Yu, Jin-Gang and Xia, Gui-Song*

15. **GAMnet: Robust Feature Matching via Graph Adversarial-Matching Network** MM, 2021. [paper](https://dl.acm.org/doi/pdf/10.1145/3474085.3475669)

    *Jiang, Bo and Sun, Pengfei and Zhang, Ziyan and Tang, Jin and Luo, Bin*

16. **Hypergraph Neural Networks for Hypergraph Matching** ICCV, 2021. [paper](https://openaccess.thecvf.com/content/ICCV2021/papers/Liao_Hypergraph_Neural_Networks_for_Hypergraph_Matching_ICCV_2021_paper.pdf)

    *Liao, Xiaowei and Xu, Yong and Ling, Haibin*

17. **Learning to Match Features with Seeded Graph Matching Network** ICCV, 2021. [paper](https://openaccess.thecvf.com/content/ICCV2021/html/Chen_Learning_To_Match_Features_With_Seeded_Graph_Matching_Network_ICCV_2021_paper.html)

    *Chen, Hongkai and Luo, Zixin and Zhang, Jiahui and Zhou, Lei and Bai, Xuyang and Hu, Zeyu and Tai, Chiew-Lan and Quan, Long*

18. **⭐Appearance and Structure Aware Robust Deep Visual Graph Matching: Attack, Defense and Beyond** CVPR, 2022. [paper](https://openaccess.thecvf.com/content/CVPR2022/papers/Ren_Appearance_and_Structure_Aware_Robust_Deep_Visual_Graph_Matching_Attack_CVPR_2022_paper.pdf), [code](https://github.com/Thinklab-SJTU/RobustMatch)

    *Ren, Qibing and Bao, Qingquan and Wang, Runzhong and Yan, Junchi*

19. **⭐Self-supervised Learning of Visual Graph Matching** ECCV, 2022. [paper](), [code](https://github.com/Thinklab-SJTU/ThinkMatch-SCGM)

    *Liu, Chang and Zhang, Shaofeng and Yang, Xiaokang and Yan, Junchi*

20. **⭐Revocable Deep Reinforcement Learning with Affinity Regularization for Outlier-Robust Graph Matching.** ICLR, 2023. [paper](https://openreview.net/forum?id=QjQibO3scV_), [code](https://github.com/Thinklab-SJTU/RGM)

    *Liu, Chang and Jiang, Zetian and Wang, Runzhong and Yan, Junchi and Huang, Lingxiao and Lu, Pinyan*

### [Quadratic Assignment Problem](#content)

1. **Revised Note on Learning Algorithms for Quadratic Assignment with Graph Neural Networks** Arxiv, 2017. [paper](https://arxiv.org/pdf/1706.07450.pdf), [code](https://github.com/alexnowakvila/QAP_pt)

    *Nowak, Alex and Villar, Soledad and Bandeira, S. Afonso and Bruna, Joan*

2. **⭐Neural Graph Matching Network: Learning Lawler's Quadratic Assignment Problem with Extension to Hypergraph and Multiple-graph Matching.** TPAMI, 2021. [paper](https://arxiv.org/abs/1911.11308), [code](https://github.com/Thinklab-SJTU/ThinkMatch)

    *Wang, Runzhong and Yan, Junchi and Yang, Xiaokang*

3. **⭐Revocable Deep Reinforcement Learning with Affinity Regularization for Outlier-Robust Graph Matching.** ICLR, 2023. [paper](https://openreview.net/forum?id=QjQibO3scV_), [code](https://github.com/Thinklab-SJTU/RGM)

    *Liu, Chang and Jiang, Zetian and Wang, Runzhong and Yan, Junchi and Huang, Lingxiao and Lu, Pinyan*

### [Travelling Salesman Problem](#content)

1. **Learning Combinatorial Optimization Algorithms over Graphs.** NeurIPS, 2017. [paper](https://arxiv.org/abs/1704.01665)

    *Dai, Hanjun and Khalil, Elias B and Zhang, Yuyu and Dilkina, Bistra and Song, Le*

2. **Learning Heuristics for the TSP by Policy Gradient** CPAIOR, 2018. [paper](https://link.springer.com/chapter/10.1007/978-3-319-93031-2_12), [code](https://github.com/MichelDeudon/encode-attend-navigate)

    *Michel DeudonPierre CournutAlexandre Lacoste*

3. **Attention, Learn to Solve Routing Problems!** ICLR, 2019. [paper](https://arxiv.org/abs/1803.08475)

    *Kool, Wouter and Van Hoof, Herke and Welling, Max.*

4. **Learning to Solve NP-Complete Problems: A Graph Neural Network for Decision TSP.** AAAI, 2019. [paper](https://ojs.aaai.org/index.php/AAAI/article/view/4399)

    *Prates, Marcelo and Avelar, Pedro HC and Lemos, Henrique and Lamb, Luis C and Vardi, Moshe Y.*

5. **An Efficient Graph Convolutional Network Technique for the Travelling Salesman Problem** Arxiv, 2019. [paper](https://arxiv.org/abs/1906.01227), [code](https://github.com/chaitjo/graph-convnet-tsp)

    *Chaitanya K. Joshi, Thomas Laurent, Xavier Bresson*

6. **POMO: Policy Optimization with Multiple Optima for Reinforcement Learning.** NeurIPS, 2020. [paper](https://arxiv.org/abs/2010.16011), [code](https://github.com/yd-kwon/POMO/)

    *Kwon, Yeong-Dae and Choo, Jinho and Kim, Byoungjip and Yoon, Iljoo and Min, Seungjai and Gwon, Youngjune.*

7. **Generalize a Small Pre-trained Model to Arbitrarily Large TSP Instances.** Arxiv, 2020. [paper](https://arxiv.org/abs/2012.10658)

    *Fu, Zhang-Hua and Qiu, Kai-Bin and Zha, Hongyuan.*

8. **A Reinforcement Learning Approach for Optimizing Multiple Traveling Salesman Problems over Graphs** KBS, 2020. [journal](https://www.sciencedirect.com/science/article/pii/S0950705120304445)

    *Hu, Yujiao and Yao, Yuan and Lee, Wee Sun*

9. **Learning 2-opt Heuristics for the Traveling Salesman Problem via Deep Reinforcement Learning** ACML, 2020. [paper](http://proceedings.mlr.press/v129/costa20a), [code](https://github.com/paulorocosta/learning-2opt-drl)

    *d O Costa, Paulo R and Rhuggenaath, Jason and Zhang, Yingqian and Akcay, Alp*

10. **Deep Reinforcement Learning for Combinatorial Optimization: Covering Salesman Problems.** IEEE Trans Cybern, 2021. [journal](https://arxiv.org/abs/2102.05875)

    *Kaiwen Li, Tao Zhang, Rui Wang Yuheng Wang, and Yi Han*

11. **The Transformer Network for the Traveling Salesman Problem** IPAM, 2021. [paper](http://helper.ipam.ucla.edu/publications/dlc2021/dlc2021_16703.pdf)

    *Xavier Bresson，Thomas Laurent*

12. **Learning Improvement Heuristics for Solving Routing Problems** TNNLS, 2021. [journal](https://ieeexplore.ieee.org/abstract/document/9393606?casa_token=mFeyLmrOGfIAAAAA:nmAkjUaTSooYurWHuWGYNoguV453anw9Enyv45xG5jb2oCps6QE4A1CFe1EmFmTzbON6cL5maw)

    *Wu, Yaoxin and Song, Wen and Cao, Zhiguang and Zhang, Jie and Lim, Andrew*

13. **Reversible Action Design for Combinatorial Optimization with Reinforcement Learning** Arxiv, 2021. [paper](https://arxiv.org/abs/2102.07210)

    *Yao, Fan and Cai, Renqin and Wang, Hongning*

14. **Solving Dynamic Traveling Salesman Problems with Deep Reinforcement Learning.** TNNLS, 2021. [journal](https://ieeexplore.ieee.org/document/9537638)

    *Zizhen Zhang, Hong Liu, Meng Chu Zhou, Jiahai Wang*

15. **ScheduleNet: Learn to Solve Multi-agent Scheduling Problems with Reinforcement Learning** Arxiv, 2021. [paper](https://arxiv.org/abs/2106.03051)

    *Junyoung Park, Sanjar Bakhtiyar, Jinkyoo Park*

16. **DAN: Decentralized Attention-based Neural Network to Solve the MinMax Multiple Traveling Salesman Problem** Arxiv, 2021. [paper](https://arxiv.org/abs/2109.04205)

    *Cao, Yuhong and Sun, Zhanhong and Sartoretti, Guillaume*

17. **Reinforcement Learning for Route Optimization with Robustness Guarantees** IJCAI, 2021. [paper](https://www.ijcai.org/proceedings/2021/0357.pdf)

    *Jacobs, Tobias and Alesiani, Francesco and Ermis, Gulcin*

18. **Learning TSP Requires Rethinking Generalization** CP, 2021. [paper](https://arxiv.org/pdf/2006.07054.pdf), [code](https://github.com/chaitjo/learning-tsp)

    *Chaitanya K. Joshi, Quentin Cappart, Louis-Martin Rousseau and Thomas Laurent*

19. **The First AI4TSP Competition: Learning to Solve Stochastic Routing Problems** Arxiv, 2022. [paper](https://arxiv.org/abs/2201.10453), [code](https://github.com/paulorocosta/ai-for-tsp-competition)

    *Bliek, Laurens and da Costa, Paulo and Afshar, Reza Refaei and Zhang, Yingqian and Catshoek, Tom and Vos, Daniel and Verwer, Sicco and Schmitt-Ulms, Fynn and Hottung, Andre and Shah, Tapan and others*

20. **Graph Neural Network Guided Local Search for the Traveling Salesperson Problem** ICLR, 2022. [paper](https://openreview.net/forum?id=ar92oEosBIg)

    *Hudson, Benjamin and Li, Qingbiao and Malencia, Matthew and Prorok, Amanda*

21. **Preference Conditioned Neural Multi-objective Combinatorial Optimization** ICLR, 2022. [paper](https://openreview.net/forum?id=QuObT9BTWo)

    *Lin, Xi and Yang, Zhiyuan and Zhang, Qingfu*

22. **Learning Generalizable Models for Vehicle Routing Problems via Knowledge Distillation** NeurIPS, 2022. [paper](https://openreview.net/forum?id=sOVNpUEgKMp), [code](https://github.com/jieyibi/AMDKD)

    *Bi, Jieyi and Ma, Yining and Wang, Jiahai and Cao, Zhiguang and Chen, Jinbiao and Sun, Yuan and Chee, Yeow Meng*

23. **DIMES: A Differentiable Meta Solver for Combinatorial Optimization Problems** NeurIPS, 2022. [paper](https://openreview.net/forum?id=9u05zr0nhx)

    *Qiu, Ruizhong and Sun, Zhiqing and Yang, Yiming*

24. **Sym-NCO: Leveraging Symmetricity for Neural Combinatorial Optimization** NeurIPS, 2022. [paper](https://openreview.net/forum?id=kHrE2vi5Rvs), [code](https://github.com/alstn12088/Sym-NCO)

    *Kim, Minsu and Park, Junyoung and Park, Jinkyoo*

25. **Simulation-guided Beam Search for Neural Combinatorial Optimization** NeurIPS, 2022. [paper](https://openreview.net/forum?id=tYAS1Rpys5), [code](https://github.com/yd-kwon/SGBS)

    *Choo, Jinho and Kwon, Yeong-Dae and Kim, Jihoon and Jae, Jeongwoo and Hottung, Andr{\'e} and Tierney, Kevin and Gwon, Youngjune*

26. **Generalization of Neural Combinatorial Solvers Through the Lens of Adversarial Robustness** ICLR, 2022. [paper](https://openreview.net/forum?id=vJZ7dPIjip3)

    *Simon Geisler, Johanna Sommer, Jan Schuchardt, Aleksandar Bojchevski and Stephan Günnemann*

27. **Learning to CROSS exchange to solve min-max vehicle routing problems** ICLR, 2023. [paper](https://openreview.net/forum?id=ZcnzsHC10Y)

    *Kim, Minjun and Park, Junyoung and Park, Jinkyoo*

28. **Generalize Learned Heuristics to Solve Large-scale Vehicle Routing Problems in Real-time** ICLR, 2023. [paper](https://openreview.net/forum?id=6ZajpxqTlQ)

    *Hou, Qingchun and Yang, Jingwei and Su, Yiqiang and Wang, Xiaoqing and Deng, Yuming*

29. **⭐ROCO: A General Framework for Evaluating Robustness of Combinatorial Optimization Solvers on Graphs** ICLR, 2023. [paper](https://openreview.net/forum?id=2r6YMqz4Mml), [code](https://github.com/Thinklab-SJTU/ROCO)

    *Lu, Han and Li, Zenan and Wang, Runzhong and Ren, Qibing and Li, Xijun and Yuan, Mingxuan and Zeng, Jia and Yang, Xiaokang and Yan, Junchi*

30. **Pointerformer: Deep Reinforced Multi-Pointer Transformer for the Traveling Salesman Problem** Arxiv, 2023. [paper](https://arxiv.org/abs/2304.09407), [code](https://github.com/Pointerformer/Pointerformer)

    *Yan Jin, Yuandong Ding, Xuanhao Pan, Kun He, Li Zhao, Tao Qin, Lei Song, Jiang Bian*

31. **H-tsp: Hierarchically solving the large-scale traveling salesman problem** AAAI, 2023. [paper](https://www.microsoft.com/en-us/research/publication/h-tsp-hierarchically-solving-the-large-scale-traveling-salesman-problem/), [code](https://github.com/Learning4Optimization-HUST/H-TSP)

    *Xuanhao Pan,  Yan Jin,  Yuandong Ding,  Mingxiao Feng,  Li Zhao,  Lei Song,  Jiang Bian*

32. **Select and Optimize: Learning to solve large-scale TSP instances** AISTATS, 2023. [paper](https://proceedings.mlr.press/v206/cheng23a.html)

    *Hanni Cheng, Haosi Zheng, Ya Cong, Weihao Jiang, Shiliang Pu*

33. **Multi-View Graph Contrastive Learning for Solving Vehicle Routing Problems** UAI, 2023. [paper](https://openreview.net/pdf?id=Z-mRKVaxVU3)

    *Yuan Jiang, Zhiguang Cao, Yaoxin Wu, Jie Zhang*

### [Maximal Cut](#content)

1. **Learning Combinatorial Optimization Algorithms over Graphs.** NeurIPS, 2017. [paper](https://arxiv.org/abs/1704.01665)

    *Dai, Hanjun and Khalil, Elias B and Zhang, Yuyu and Dilkina, Bistra and Song, Le*

2. **Exploratory Combinatorial Optimization with Reinforcement Learning.** AAAI, 2020. [paper](https://ojs.aaai.org/index.php/AAAI/article/view/5723)

    *LBarrett, Thomas and Clements, William and Foerster, Jakob and Lvovsky, Alex.*

3. **Erdos Goes Neural: an Unsupervised Learning Framework for Combinatorial Optimization on Graphs.** NeurIPS, 2020. [paper](https://static.aminer.cn/upload/pdf/575/1127/1864/5eede0b791e0116a23aafe7b_1.pdf)

    *Karalias, Nikolaos and Loukas, Andreas*

4. **Reversible Action Design for Combinatorial Optimization with Reinforcement Learning** Arxiv, 2021. [paper](https://arxiv.org/abs/2102.07210)

    *Yao, Fan and Cai, Renqin and Wang, Hongning*

5. **LeNSE: Learning To Navigate Subgraph Embeddings for Large-Scale Combinatorial Optimisation** ICML, 2022. [paper](https://proceedings.mlr.press/v162/ireland22a.html), [code](https://github.com/davidireland3/LeNSE)

    *Ireland, David and G. Montana*

6. **Learning to Solve Combinatorial Graph Partitioning Problems via Efficient Exploration** Arxiv, 2022. [paper](https://arxiv.org/abs/2205.14105), [code](https://github.com/tomdbar/ecord)

    *Barrett, Thomas D and Parsonson, Christopher WF and Laterre, Alexandre*

7. **Let the Flows Tell: Solving Graph Combinatorial Optimization Problems with GFlowNets** Arxiv, 2023. [paper](https://arxiv.org/abs/2305.17010)

    *Dinghuai Zhang, Hanjun Dai, Nikolay Malkin, Aaron Courville, Yoshua Bengio, Ling Pan*

### [Differentiable Optimization](#content)

1. **Differentiable Learning of Submodular Models** NeurIPS, 2017. [paper](https://papers.NeurIPS.cc/paper/2017/hash/192fc044e74dffea144f9ac5dc9f3395-Abstract.html), [code](https://github.com/josipd/torch-submod)

    *Josip Djolonga, Andreas Krause*

2. **OptNet: differentiable optimization as a layer in neural networks** ICML, 2017. [paper](https://dl.acm.org/doi/abs/10.5555/3305381.3305396), [code](https://github.com/locuslab/optnet)

    *Brandon Amos and J. Zico Kolter*

3. **Melding the Data-Decisions Pipeline: Decision-Focused Learning for Combinatorial Optimization** AAAI, 2019. [paper](https://ojs.aaai.org//index.php/AAAI/article/view/3982)

    *Bryan Wilder, Bistra Dilkina, Milind Tambe*

4. **Differentiable Convex Optimization Layers** NeurIPS, 2019. [paper](https://dl.acm.org/doi/abs/10.5555/3454287.3455145), [code](https://github.com/cvxgrp/cvxpylayers)

    *Agrawal, Akshay and Boyd, Stephen*

5. **Predict+optimise with ranking objectives: exhaustively learning linear functions** IJCAI, 2019. [paper](https://dl.acm.org/doi/abs/10.5555/3367032.3367186)

    *Demirovic, Emir and Stuckey, Peter J. and Bailey, James and Chan, Jeffrey and Leckie, Christopher and Ramamohanarao, Kotagiri and Guns, Tias*

6. **Differentiation of Blackbox Combinatorial Solvers** ICLR, 2020. [paper](https://arxiv.org/pdf/1912.02175v2.pdf), [code](https://github.com/martius-lab/blackbox-backprop)

    *Marin Vlastelica, Anselm Paulus, Vít Musil, Georg Martius, Michal Rolínek*

7. **MIPaaL: Mixed Integer Program as a Layer** AAAI, 2020. [paper](https://ojs.aaai.org//index.php/AAAI/article/view/5509), [code](https://github.com/amf272/MIPaaL/)

    *Aaron Ferber, Bryan Wilder, Bistra Dilkina, Milind Tambe*

8. **Smart Predict-and-Optimize for Hard Combinatorial Optimization Problems** AAAI, 2020. [paper](https://arxiv.org/abs/1911.10092), [code](https://github.com/JayMan91/aaai_predit_then_optimize)

    *Jaynta Mandi, Emir Demirovi, Peter. J Stuckey, Tias Guns*

9. **Differentiation of blackbox combinatorial solvers** ICLR, 2020. [paper](https://openreview.net/forum?id=BkevoJSYPB), [code](https://github.com/martius-lab/blackbox-backprop)

    *Marin Vlastelica Pogani, Anselm Paulus, Vit Musil, Georg Martius, Michal Rolinek*

10. **Interior Point Solving for LP-based prediction+optimization** NeurIPS, 2020. [paper](https://proceedings.neurips.cc//paper/2020/hash/51311013e51adebc3c34d2cc591fefee-Abstract.html), [code](https://github.com/JayMan91/NeurIPSIntopt)

    *Jayanta Mandi, Tias Guns*

11. **Automatically Learning Compact Quality-aware Surrogates for Optimization Problems** NeurIPS, 2020. [paper](https://openreview.net/forum?id=v8hzdOdOle)

    *Kai Wang, Bryan Wilder, Andrew Perrault, Milind Tambe*

12. **Contrastive Losses and Solution Caching for Predict-and-Optimize** IJCAI, 2021. [paper](https://www.ijcai.org/proceedings/2021/0390.pdf), [code](https://github.com/jayman91/ltr-predopt)

    *Maxime Mulamba, Jayanta Mandi, Michelangelo Diligenti , Michele Lombardi, Victor Bucarey, Tias Guns*

13. **A Surrogate Objective Framework for Prediction+Programming with Soft Constraints** NeurIPS, 2021. [paper](https://openreview.net/forum?id=9Sa2xh4mGR), [code](https://github.com/PredOptwithSoftConstraint/PredOptwithSoftConstraint)

    *Kai Yan, Jie Yan, Chuan Luo, Liting Chen, Qingwei Lin, Dongmei Zhang*

14. **Implicit MLE: Backpropagating Through Discrete Exponential Family Distributions** NeurIPS, 2021. [paper](https://openreview.net/forum?id=lR4aaWCQgB), [code](https://github.com/uclnlp/torch-imle)

    *Mathias Niepert, Pasquale Minervini, Luca Franceschi*

15. **COPS: Combinatorial Optimization for Panoptic Segmentation: A Fully Differentiable Approach** NeurIPS, 2021. [paper](https://proceedings.neurips.cc/paper/2021/hash/83a368f54768f506b833130584455df4-Abstract.html), [code](https://github.com/aabbas90/COPS)

    *Ahmed Abbas, Paul Swoboda*

16. **An Exact Symbolic Reduction of Linear Smart Predict+Optimize to Mixed Integer Linear Programming** ICML, 2022. [paper](https://proceedings.mlr.press/v162/jeong22a.html), [code](https://github.com/jihwan-jeong/xaddpy)

    *Jeong, Jihwan, Parth Jaggi, Andrew Butler and Scott Sanner. “An Exact Symbolic Reduction of Linear Smart Predict+Optimize to Mixed Integer Linear Programming.” ICML (2022).*

17. **Constrained Discrete Black-Box Optimization using Mixed-Integer Programming** ICML, 2022. [paper](https://proceedings.mlr.press/v162/papalexopoulos22a.html)

    *Papalexopoulos, Theodore, Christian Tjandraatmadja, Ross Anderson, Juan Pablo Vielma and Daving Belanger.*

18. **End-to-End Stochastic Optimization with Energy-Based Model** NeurIPS, 2022. [paper](https://openreview.net/forum?id=_sYOodxTMcF), [code](https://github.com/Lingkai-Kong/so-ebm)

    *Lingkai Kong, Jiaming Cui, Yuchen Zhuang, Rui Feng, B. Aditya Prakash, Chao Zhang*

19. **Deep Declarative Networks** TPAMI, 2022. [paper](https://ieeexplore.ieee.org/document/9355027), [code](https://github.com/anucvml/ddn)

    *Stephen Gould, Richard Hartley and Dylan Campbell*

### [Vehicle Routing Problem](#content)

1. **Learning to Perform Local Rewriting for Combinatorial Optimization.** NeurIPS, 2019. [paper](https://arxiv.org/abs/1810.00337), [code](https://github.com/facebookresearch/neural-rewriter)

    *Chen, Xinyun and Tian, Yuandong.*

2. **Deep Reinforcement Learning for the Electric Vehicle Routing Problem with Time Windows.** Arxiv, 2020. [paper](https://arxiv.org/abs/2010.02068)

    *Lin, Bo and Ghaddar, Bissan and Nathwani, Jatin.*

3. **Efficiently Solving the Practical,Vehicle Routing Problem: A Novel Joint Learning Approach.** KDD, 2020. [paper](https://www.kdd.org/kdd2020/accepted-papers/view/efficiently-solving-the-practical-vehicle-routing-problem-a-novel-joint-lea)

    *Lu Duan, Yang Zhan, Haoyuan Hu, Yu Gong, Jiangwen Wei, Xiaodong Zhang, Yinghui Xu*

4. **Reinforcement Learning with Combinatorial Actions: An Application to Vehicle Routing** NeurIPS, 2020. [paper](https://papers.nips.cc/paper/2020/file/06a9d51e04213572ef0720dd27a84792-Paper.pdf), [code](https://github.com/google-research/tf-opt)

    *Arthur Delarue, Ross Anderson, Christian Tjandraatmadja*

5. **A Learning-based Iterative Method for Solving Vehicle Routing Problems** ICLR, 2020. [paper](https://static.aminer.cn/upload/pdf/program/5e5e18dd93d709897ce3720b_0.pdf)

    *Lu, Hao and Zhang, Xingwen and Yang, Shuang*

6. **Neural Large Neighborhood Search for the Capacitated Vehicle Routing Problem** Arxiv, 2020. [paper](https://arxiv.org/abs/1911.09539)

    *Hottung, Andre and Tierney, Kevin*

7. **Learning Improvement Heuristics for Solving Routing Problems** TNNLS, 2021. [journal](https://ieeexplore.ieee.org/abstract/document/9393606?casa_token=mFeyLmrOGfIAAAAA:nmAkjUaTSooYurWHuWGYNoguV453anw9Enyv45xG5jb2oCps6QE4A1CFe1EmFmTzbON6cL5maw)

    *Wu, Yaoxin and Song, Wen and Cao, Zhiguang and Zhang, Jie and Lim, Andrew*

8. **Reinforcement Learning for Route Optimization with Robustness Guarantees** IJCAI, 2021. [paper](https://www.ijcai.org/proceedings/2021/0357.pdf)

    *Jacobs, Tobias and Alesiani, Francesco and Ermis, Gulcin*

9. **Multi-Decoder Attention Model with Embedding Glimpse for Solving Vehicle Routing Problems.** AAAI, 2021. [paper](https://arxiv.org/abs/2012.10638), [code](https://github.com/liangxinedu/MDAM)

    *Liang Xin, Wen Song, Zhiguang Cao, Jie Zhang*

10. **Analytics and Machine Learning in Vehicle Routing Research** Arxiv, 2021. [paper](https://arxiv.org/abs/2102.10012)

    *Bai, Ruibin and Chen, Xinan and Chen, Zhi-Long and Cui, Tianxiang and Gong, Shuhui and He, Wentao and Jiang, Xiaoping and Jin, Huan and Jin, Jiahuan and Kendall, Graham and others*

11. **RP-DQN: An application of Q-Learning to Vehicle Routing Problems** Arxiv, 2021. [paper](https://arxiv.org/abs/2104.12226)

    *Bdeir, Ahmad and Boeder, Simon and Dernedde, Tim and Tkachuk, Kirill and Falkner, Jonas K and Schmidt-Thieme, Lars*

12. **Deep Policy Dynamic Programming for Vehicle Routing Problems** Arxiv, 2021. [paper](https://arxiv.org/abs/2102.11756)

    *Kool, Wouter and van Hoof, Herke and Gromicho, Joaquim and Welling, Max*

13. **Learning to Delegate for Large-scale Vehicle Routing** NeurIPS, 2021. [paper](https://proceedings.neurips.cc/paper/2021/hash/dc9fa5f217a1e57b8a6adeb065560b38-Abstract.html)

    *Li, Sirui and Yan, Zhongxia and Wu, Cathy*

14. **Learning a Latent Search Space for Routing Problems using Variational Autoencoders** ICLR, 2021. [paper](https://openreview.net/forum?id=90JprVrJBO)

    *Hottung, Andre and Bhandari, Bhanu and Tierney, Kevin*

15. **Preference Conditioned Neural Multi-objective Combinatorial Optimization** ICLR, 2022. [paper](https://openreview.net/forum?id=QuObT9BTWo)

    *Lin, Xi and Yang, Zhiyuan and Zhang, Qingfu*

16. **Learning Generalizable Models for Vehicle Routing Problems via Knowledge Distillation** NeurIPS, 2022. [paper](https://openreview.net/forum?id=sOVNpUEgKMp), [code](https://github.com/jieyibi/AMDKD)

    *Bi, Jieyi and Ma, Yining and Wang, Jiahai and Cao, Zhiguang and Chen, Jinbiao and Sun, Yuan and Chee, Yeow Meng*

17. **Sym-NCO: Leveraging Symmetricity for Neural Combinatorial Optimization** NeurIPS, 2022. [paper](https://openreview.net/forum?id=kHrE2vi5Rvs), [code](https://github.com/alstn12088/Sym-NCO)

    *Kim, Minsu and Park, Junyoung and Park, Jinkyoo*

18. **Simulation-guided Beam Search for Neural Combinatorial Optimization** NeurIPS, 2022. [paper](https://openreview.net/forum?id=tYAS1Rpys5), [code](https://github.com/yd-kwon/SGBS)

    *Choo, Jinho and Kwon, Yeong-Dae and Kim, Jihoon and Jae, Jeongwoo and Hottung, Andr{\'e} and Tierney, Kevin and Gwon, Youngjune*

19. **Learning to CROSS exchange to solve min-max vehicle routing problems** ICLR, 2023. [paper](https://openreview.net/forum?id=ZcnzsHC10Y)

    *Kim, Minjun and Park, Junyoung and Park, Jinkyoo*

20. **Generalize Learned Heuristics to Solve Large-scale Vehicle Routing Problems in Real-time** ICLR, 2023. [paper](https://openreview.net/forum?id=6ZajpxqTlQ)

    *Hou, Qingchun and Yang, Jingwei and Su, Yiqiang and Wang, Xiaoqing and Deng, Yuming*

### [Job Shop Scheduling Problem](#content)

1. **Smart Manufacturing Scheduling With Edge Computing Using Multiclass Deep Q Network** Transactions on Industrial Informatics, 2019. [journal](https://ieeexplore.ieee.org/document/8676376)

    *Chun-Cheng Lin, Der-Jiunn Deng, Yen-Ling Chih, Hsin-Ting Chiu*

2. **Multi-Agent Reinforcement Learning for Job Shop Scheduling in Flexible Manufacturing Systems** International Conference on Artificial Intelligence for Industries (AI4I), 2019. [paper](https://ieeexplore.ieee.org/document/9027776)

    *Schirin Baer, Jupiter Bakakeu, Richard Meyes, Tobias Meisen*

3. **Learning to Dispatch for Job Shop Scheduling via Deep Reinforcement Learning.** NeurIPS, 2020. [paper](https://arxiv.org/abs/2010.12367), [code](https://github.com/zcajiayin/L2D)

    *Zhang, Cong and Song, Wen and Cao, Zhiguang and Zhang, Jie and Tan, Puay Siew and Xu, Chi.*

4. **ScheduleNet: Learn to Solve Multi-agent Scheduling Problems with Reinforcement Learning** Arxiv, 2021. [paper](https://arxiv.org/abs/2106.03051)

    *Junyoung Park, Sanjar Bakhtiyar, Jinkyoo Park*

5. **Dynamic job-shop scheduling in smart manufacturing using deep reinforcement learning** Computer Networks, 2021. [journal](https://www.sciencedirect.com/science/article/pii/S1389128621001031)

    *Libing Wang, Xin Hu, Yin Wang, Sujie Xu, Shijun Ma, Kexin Yang, Zhijun Liu, Weidong Wang*

6. **Learning to schedule job-shop problems: Representation and policy learning using graph neural network and reinforcement learning.** International Journal of Production Research, 2021. [journal](https://arxiv.org/abs/2106.01086)

    *Junyoung Park, Jaehyeong Chun, Sang Hun Kim, Youngkook Kim, Jinkyoo Park*

7. **Explainable reinforcement learning in production control of job shop manufacturing system.** International Journal of Production Research, 2021. [journal](https://www.tandfonline.com/doi/abs/10.1080/00207543.2021.1972179?journalCode=tprs20)

    *Andreas Kuhnle,Marvin Carl May,Louis Sch?fer & Gisela Lanza*

8. **Neural DAG Scheduling via One-Shot Priority Sampling** ICLR, 2023. [paper](https://openreview.net/forum?id=WL8FlAugqQ)

    *Jeon, Wonseok and Gagrani, Mukul and Bartan, Burak and Zeng, Weiliang Will and Teague, Harris and Zappi, Piero and Lott, Christopher*

9. **Robust Scheduling with GFlowNets** ICLR, 2023. [paper](https://openreview.net/forum?id=ZBUthI6wK9h)

    *Zhang, David W and Rainone, Corrado and Peschl, Markus and Bondesan, Roberto*

### [Maximal/Maximum Independent Set](#content)

1. **Combinatorial Optimization with Graph Convolutional Networks and Guided Tree Search.** NeurIPS, 2018. [paper](https://arxiv.org/abs/1810.10659)

    *Li, Zhuwen and Chen, Qifeng and Koltun, Vladlen.*

2. **Learning What to Defer for Maximum Independent Sets** ICML, 2020. [paper](http://proceedings.mlr.press/v119/ahn20a.html)

    *Ahn, Sungsoo and Seo, Younggyo and Shin, Jinwoo*

3. **Distributed Scheduling Using Graph Neural Networks** ICASSP, 2021. [paper](https://ieeexplore.ieee.org/abstract/document/9414098?casa_token=Q4coRBbINPMAAAAA:0T8L49Kyn9p4CoM20-FqINKCyk_Sm3ye5TemPT8GlG3C3wXXLvn1RGKeHgriiyZIcg_GFB4z1A)

    *Zhao, Zhongyuan and Verma, Gunjan and Rao, Chirag and Swami, Ananthram and Segarra, Santiago*

4. **Solving Graph-based Public Good Games with Tree Search and Imitation Learning** NeurlPS, 2021. [paper](https://arxiv.org/abs/2106.06762)

    *Darvariu, Victor-Alexandru and Hailes, Stephen and Musolesi, Mirco*

5. **NN-Baker: A Neural-network Infused Algorithmic Framework for Optimization Problems on Geometric Intersection Graphs** NeurlPS, 2021. [paper](https://papers.nips.cc/paper/2021/file/c236337b043acf93c7df397fdb9082b3-Paper.pdf)

    *McCarty, Evan and Zhao, Qi and Sidiropoulos, Anastasios and Wang, Yusu*

6. **What's Wrong with Deep Learning in Tree Search for Combinatorial Optimization** ICLR, 2022. [paper](https://openreview.net/forum?id=mk0HzdqY7i1), [code](https://github.com/MaxiBoether/mis-benchmark-framework)

    *Bother, Maximilian and Kissig, Otto and Taraz, Martin and Cohen, Sarel and Seidel, Karen and Friedrich, Tobias*

7. **Optimistic tree search strategies for black-box combinatorial optimization** NeurlPS, 2022. [paper](https://openreview.net/forum?id=JGLW4DvX11F)

    *Malherbe, Cedric and Grosnit, Antoine and Tutunov, Rasul and Ammar, Haitham Bou and Wang, Jun*

8. **⭐ROCO: A General Framework for Evaluating Robustness of Combinatorial Optimization Solvers on Graphs** ICLR, 2023. [paper](https://openreview.net/forum?id=2r6YMqz4Mml), [code](https://github.com/Thinklab-SJTU/ROCO)

    *Lu, Han and Li, Zenan and Wang, Runzhong and Ren, Qibing and Li, Xijun and Yuan, Mingxuan and Zeng, Jia and Yang, Xiaokang and Yan, Junchi*

9. **Unsupervised Learning for Combinatorial Optimization Needs Meta Learning** ICLR, 2023. [paper](https://openreview.net/forum?id=-ENYHCE8zBp), [code](https://github.com/Graph-COM/Meta_CO)

    *Wang, Haoyu and Li, Pan*

10. **Graph-based Deterministic Policy Gradient for Repetitive Combinatorial Optimization Problems** ICLR, 2023. [paper](https://openreview.net/forum?id=yHIIM9BgOo), [code](https://github.com/XzrTGMu/twin-nphard)

    *Zhao, Zhongyuan and Swami, Ananthram and Segarra, Santiago*

11. **Let the Flows Tell: Solving Graph Combinatorial Optimization Problems with GFlowNets** Arxiv, 2023. [paper](https://arxiv.org/abs/2305.17010)

    *Dinghuai Zhang, Hanjun Dai, Nikolay Malkin, Aaron Courville, Yoshua Bengio, Ling Pan*

### [Generalization](#content)

1. **It's Not What Machines Can Learn It's What We Cannot Teach** ICML, 2020. [paper](http://proceedings.mlr.press/v119/yehuda20a/yehuda20a.pdf)

    *Gal Yehuda, Moshe Gabel and Assaf Schuster*

2. **Learning TSP Requires Rethinking Generalization** CP, 2021. [paper](https://arxiv.org/pdf/2006.07054.pdf), [code](https://github.com/chaitjo/learning-tsp)

    *Chaitanya K. Joshi, Quentin Cappart, Louis-Martin Rousseau and Thomas Laurent*

3. **Generalization of Neural Combinatorial Solvers Through the Lens of Adversarial Robustness** ICLR, 2022. [paper](https://openreview.net/forum?id=vJZ7dPIjip3)

    *Simon Geisler, Johanna Sommer, Jan Schuchardt, Aleksandar Bojchevski and Stephan Günnemann*

4. **Learning for Robust Combinatorial Optimization: Algorithm and Application** INFOCOM, 2022. [journal](https://ieeexplore.ieee.org/abstract/document/9796715/)

    *Shao, Zhihui and Yang, Jianyi and Shen, Cong and Ren, Shaolei*

5. **⭐ROCO: A General Framework for Evaluating Robustness of Combinatorial Optimization Solvers on Graphs** ICLR, 2023. [paper](https://openreview.net/forum?id=2r6YMqz4Mml), [code](https://github.com/Thinklab-SJTU/ROCO)

    *Lu, Han and Li, Zenan and Wang, Runzhong and Ren, Qibing and Li, Xijun and Yuan, Mingxuan and Zeng, Jia and Yang, Xiaokang and Yan, Junchi*

### [Computing Resource Allocation](#content)

1. **Resource Management with Deep Reinforcement Learning.** HotNets, 2016. [paper](https://dl.acm.org/doi/abs/10.1145/3005745.3005750)

    *Mao, Hongzi and Alizadeh, Mohammad and Menache, Ishai and Kandula, Srikanth.*

2. **Learning to Perform Local Rewriting for Combinatorial Optimization.** NeurIPS, 2019. [paper](https://arxiv.org/abs/1810.00337), [code](https://github.com/facebookresearch/neural-rewriter)

    *Chen, Xinyun and Tian, Yuandong.*

3. **Learning Scheduling Algorithms for Data Processing Clusters** SIGCOMM, 2019. [paper](https://static.aminer.cn/storage/pdf/arxiv/18/1810/1810.01963.pdf), [code](https://github.com/hongzimao/decima-sim)

    *Mao, Hongzi and Schwarzkopf, Malte and Venkatakrishnan, Bojja Shaileshh and Meng, Zili and Alizadeh, Mohammad.*

4. **Smart Resource Allocation for Mobile Edge Computing: A Deep Reinforcement Learning Approach** IEEE Transactions on Emerging Topics in Computing, 2019. [Paper](https://ieeexplore.ieee.org/abstract/document/8657791)

    *Jiadai; Lei Zhao; Jiajia Liu; Nei Kato*

5. **A Two-stage Framework and Reinforcement Learning-based Optimization Algorithms for Complex Scheduling Problems** Arxiv, 2021. [paper](https://arxiv.org/abs/2103.05847)

    *He, Yongming and Wu, Guohua and Chen, Yingwu and Pedrycz, Witold*

6. **⭐A Bi-Level Framework for Learning to Solve Combinatorial Optimization on Graphs** NeurIPS, 2021. [paper](https://arxiv.org/abs/2106.04927), [code](https://github.com/Thinklab-SJTU/PPO-BiHyb)

    *Wang, Runzhong and Hua, Zhigang and Liu, Gan and Zhang, Jiayi and Yan, Junchi and Qi, Feng and Yang, Shuang and Zhou, Jun and Yang, Xiaokang*

### [Bin Packing Problem](#content)

1. **Small Boxes Big Data: A Deep Learning Approach to Optimize Variable Sized Bin Packing** BigDataService, 2017. [paper](https://ieeexplore.ieee.org/abstract/document/7944923/?casa_token=mRzI_XBy3ycAAAAA:yD9Le2KBNq1TMpW_1etb0RF-oFVcLJj9Up0Z2qI6XJmA-UffxxSZRIx7RklaQED-yXwuwBC4M_w)

    *Mao, Feng and Blanco, Edgar and Fu, Mingang and Jain, Rohit and Gupta, Anurag and Mancel, Sebastien and Yuan, Rong and Guo, Stephen and Kumar, Sai and Tian, Yayang*

2. **Solving a New 3D Bin Packing Problem with Deep Reinforcement Learning Method** Arxiv, 2017. [paper](https://arxiv.org/abs/1708.05930)

    *Hu, Haoyuan and Zhang, Xiaodong and Yan, Xiaowei and Wang, Longfei and Xu, Yinghui*

3. **Best Arm Identification in Multi-armed Bandits with Delayed Feedback** PMLR, 2018. [paper](http://proceedings.mlr.press/v84/grover18b.html)

    *Grover, Aditya and Markov, Todor and Attia, Peter and Jin, Norman and Perkins, Nicolas and Cheong, Bryan and Chen, Michael and Yang, Zi and Harris, Stephen and Chueh, William and others*

4. **Ranked Reward: Enabling Self-Play Reinforcement Learning for Combinatorial Optimization Alexandre** Arxiv, 2018. [paper](https://arxiv.org/abs/1807.01672)

    *Laterre, Alexandre and Fu, Yunguan and Jabri, Mohamed Khalil and Cohen, Alain-Sam and Kas, David and Hajjar, Karl and Dahl, Torbjorn S and Kerkeni, Amine and Beguir, Karim*

5. **A Multi-task Selected Learning Approach for Solving 3D Bin Packing Problem.** AAMAS, 2019. [paper](https://arxiv.org/abs/1804.06896)

    *Duan, Lu and Hu, Haoyuan and Qian, Yu and Gong, Yu and Zhang, Xiaodong and Xu, Yinghui and Wei, Jiangwen.*

6. **A Data-Driven Approach for Multi-level Packing Problems in Manufacturing Industry** KDD, 2019. [paper](https://dl.acm.org/doi/abs/10.1145/3292500.3330708)

    *Chen, Lei and Tong, Xialiang and Yuan, Mingxuan and Zeng, Jia and Chen, Lei*

7. **Solving Packing Problems by Conditional Query Learning** OpenReview, 2019. [paper](https://openreview.net/forum?id=BkgTwRNtPB)

    *Li, Dongda and Ren, Changwei and Gu, Zhaoquan and Wang, Yuexuan and Lau, Francis*

8. **RePack: Dense Object Packing Using Deep CNN with Reinforcement Learning** CACS, 2019. [paper](https://ieeexplore.ieee.org/abstract/document/9024360/?casa_token=ScXezdDDiwMAAAAA:fglP_vbiQUJgLZcM7YZyqnDh_qA8jOjIh-zbH7ru0XSVBghh8OAxpThOU3BqhBeet4NlSrdHPcU)

    *Chu, Yu-Cheng and Lin, Horng-Horng*

9. **Reinforcement learning driven heuristic optimization** Arxiv, 2019. [paper](https://arxiv.org/pdf/1906.06639.pdf)

    *Cai, Qingpeng and Hang, Will and Mirhoseini, Azalia and Tucker, George and Wang, Jingtao and Wei, Wei*

10. **A Generalized Reinforcement Learning Algorithm for Online 3D Bin-Packing.** AAAI Workshop, 2020. [paper](https://arxiv.org/abs/2007.00463)

    *Verma, Richa and Singhal, Aniruddha and Khadilkar, Harshad and Basumatary, Ansuma and Nayak, Siddharth and Singh, Harsh Vardhan and Kumar, Swagat and Sinha, Rajesh.*

11. **Robot Packing with Known Items and Nondeterministic Arrival Order.** TASAE, 2020. [paper](https://ieeexplore.ieee.org/abstract/document/9205914/)

    *Wang, Fan and Hauser, Kris.*

12. **TAP-Net: Transport-and-Pack using Reinforcement Learning.** TOG, 2020. [paper](https://dl.acm.org/doi/abs/10.1145/3414685.3417796), [code](https://github.com/Juzhan/TAP-Net)

    *Hu, Ruizhen and Xu, Juzhan and Chen, Bin and Gong, Minglun and Zhang, Hao and Huang, Hui.*

13. **Simultaneous Planning for Item Picking and Placing by Deep Reinforcement Learning** IROS, 2020. [paper](http://ras.papercept.net/images/temp/IROS/files/0330.pdf)

    *Tanaka, Tatsuya and Kaneko, Toshimitsu and Sekine, Masahiro and Tangkaratt, Voot and Sugiyama, Masashi*

14. **Monte Carlo Tree Search on Perfect Rectangle Packing Problem Instances** GECCO, 2020. [paper](https://dl.acm.org/doi/abs/10.1145/3377929.3398115)

    *Pejic, Igor and van den Berg, Daan*

15. **PackIt: A Virtual Environment for Geometric Planning** ICML, 2020. [paper](http://proceedings.mlr.press/v119/goyal20b.html), [code](https://github.com/princeton-vl/PackIt)

    *Goyal, Ankit and Deng, Jia*

16. **Online 3D Bin Packing with Constrained Deep Reinforcement Learning.** AAAI, 2021. [paper](https://arxiv.org/abs/2006.14978), [code](https://github.com/alexfrom0815/Online-3D-BPP-DRL)

    *Zhao, Hang and She, Qijin and Zhu, Chenyang and Yang, Yin and Xu, Kai.*

17. **Learning Practically Feasible Policies for Online 3D Bin Packing** Arxiv, 2021. [paper](https://arxiv.org/abs/2108.13680)

    *Hang Zhao and Chenyang Zhu and Xin Xu and Hui Huang and Kai Xu*

18. **Attend2Pack: Bin Packing through Deep Reinforcement Learning with Attention** ICML Workshop, 2021. [paper](https://arxiv.org/abs/2107.04333)

    *Jingwei Zhang and Bin Zi and Xiaoyu Ge*

19. **Solving 3D bin packing problem via multimodal deep reinforcement learning** AAMAS, 2021. [paper](https://www.ifaamas.org/Proceedings/aamas2021/pdfs/p1548.pdf)

    *Jiang, Yuan, Zhiguang Cao, and Jie Zhang*

20. **Learning to Solve 3-D Bin Packing Problem via Deep Reinforcement Learning and Constraint Programming** IEEE transactions on cybernetics, 2021. [paper](https://ieeexplore.ieee.org/document/9606618/)

    *Jiang, Yuan and Cao, Zhiguang and Zhang, Jie*

21. **Learning to Pack: A Data-Driven Tree Search Algorithm for Large-Scale 3D Bin Packing Problem** CIKM, 2021. [paper](https://dl.acm.org/doi/abs/10.1145/3459637.3481933)

    *Zhu, Qianwen and Li, Xihan and Zhang, Zihan and Luo, Zhixing and Tong, Xialiang and Yuan, Mingxuan and Zeng, Jia*

22. **Learning Efficient Online 3D Bin Packing on Packing Configuration Trees.** ICLR, 2022. [paper](https://openreview.net/forum?id=bfuGjlCwAq)

    *Hang Zhao and Kai Xu*

### [Graph Edit Distance](#content)

1. **SimGNN - A Neural Network Approach to Fast Graph Similarity Computation** WSDM, 2019. [paper](https://arxiv.org/abs/1808.05689), [code](https://github.com/yunshengb/SimGNN)

    *Bai, Yunsheng and Ding, Hao and Bian, Song and Chen, Ting and Sun, Yizhou and Wang, Wei*

2. **Graph Matching Networks for Learning the Similarity of Graph Structured Objects** ICML, 2019. [paper](https://arxiv.org/abs/1904.12787), [code](https://github.com/Lin-Yijie/Graph-Matching-Networks)

    *Li, Yujia and Gu, Chenjie and Dullien, Thomas and Vinyals, Oriol and Kohli, Pushmeet*

3. **Convolutional Embedding for Edit Distance** SIGIR, 2020. [paper](https://dl.acm.org/doi/abs/10.1145/3397271.3401045), [code](https://github.com/xinyandai/string-embed)

    *Dai, Xinyan and Yan, Xiao and Zhou, Kaiwen and Wang, Yuxuan and Yang, Han and Cheng, James*

4. **Learning-Based Efficient Graph Similarity Computation via Multi-Scale Convolutional Set Matching** AAAI, 2020. [paper](https://ojs.aaai.org/index.php/AAAI/article/view/5720), [code](https://github.com/yunshengb/GraphSim)

    *Bai, Yunsheng and Ding, Hao and Gu, Ken and Sun, Yizhou and Wang, Wei*

5. **⭐A Bi-Level Framework for Learning to Solve Combinatorial Optimization on Graphs** NeurIPS, 2021. [paper](https://arxiv.org/abs/2106.04927), [code](https://github.com/Thinklab-SJTU/PPO-BiHyb)

    *Wang, Runzhong and Hua, Zhigang and Liu, Gan and Zhang, Jiayi and Yan, Junchi and Qi, Feng and Yang, Shuang and Zhou, Jun and Yang, Xiaokang*

6. **⭐Combinatorial Learning of Graph Edit Distance via Dynamic Embedding.** CVPR, 2021. [paper](https://arxiv.org/abs/2011.15039), [code](https://github.com/Thinklab-SJTU/GENN-Astar)

    *Wang, Runzhong and Zhang, Tianqi and Yu, Tianshu and Yan, Junchi and Yang, Xiaokang.*

### [Hamiltonian Cycle Problem](#content)

1. **⭐A Bi-Level Framework for Learning to Solve Combinatorial Optimization on Graphs** NeurIPS, 2021. [paper](https://arxiv.org/abs/2106.04927), [code](https://github.com/Thinklab-SJTU/PPO-BiHyb)

    *Wang, Runzhong and Hua, Zhigang and Liu, Gan and Zhang, Jiayi and Yan, Junchi and Qi, Feng and Yang, Shuang and Zhou, Jun and Yang, Xiaokang*

### [Graph Coloring](#content)

1. **Deep Learning-based Hybrid Graph-Coloring Algorithm for Register Allocation.** Arxiv, 2019. [paper](https://arxiv.org/abs/1912.03700)

    *Das, Dibyendu and Ahmad, Shahid Asghar and Venkataramanan, Kumar.*

2. **Neural Models for Output-Space Invariance in Combinatorial Problems** ICLR, 2022. [paper](https://openreview.net/forum?id=ibrUkC-pbis)

    *Nandwani, Yatin and Jain, Vidit and Singla, Parag and others*

3. **Enhancing Column Generation by a Machine-Learning-Based Pricing Heuristic for Graph Coloring** AAAI, 2022. [paper](https://www.aaai.org/AAAI22Papers/AAAI-4026.ShenY.pdf), [code](https://github.com/Joey-Shen/MLPH.git)

    *Shen, Yunzhuang, Yuan Sun, Xiaodong Li, Andrew Craig Eberhard and Andreas T. Ernst.*

4. **Learning to Generate Columns with Application to Vertex Coloring** ICLR, 2023. [paper](https://openreview.net/forum?id=JHW30A4DXtO), [code](https://github.com/yuansuny/mlcg)

    *Sun, Yuan and Ernst, Andreas T and Li, Xiaodong and Weiner, Jake*

### [Maximal Common Subgraph](#content)

1. **Fast Detection of Maximum Common Subgraph via Deep Q-Learning.** Arxiv, 2020. [paper](https://arxiv.org/abs/2002.03129)

    *Bai, Yunsheng and Xu, Derek and Wang, Alex and Gu, Ken and Wu, Xueqing and Marinovic, Agustin and Ro, Christopher and Sun, Yizhou and Wang, Wei.*

### [Influence Maximization](#content)

1. **Learning Heuristics over Large Graphs via Deep Reinforcement Learning.** NeurIPS, 2020. [paper](https://arxiv.org/abs/1903.03332)

    *Mittal, Akash and Dhawan, Anuj and Manchanda, Sahil and Medya, Sourav and Ranu, Sayan and Singh, Ambuj.*

2. **Controlling Graph Dynamics with Reinforcement Learning and Graph Neural Networks.** ICML, 2021. [paper](https://arxiv.org/abs/2010.05313)

    *Eli A. Meirom, Haggai Maron, Shie Mannor, Gal Chechik*

3. **LeNSE: Learning To Navigate Subgraph Embeddings for Large-Scale Combinatorial Optimisation** ICML, 2022. [paper](https://proceedings.mlr.press/v162/ireland22a.html), [code](https://github.com/davidireland3/LeNSE)

    *Ireland, David and G. Montana*

4. **⭐Towards One-shot Neural Combinatorial Solvers: Theoretical and Empirical Notes on the Cardinality-Constrained Case** ICLR, 2023. [paper](https://openreview.net/forum?id=h21yJhdzbwz), [code](https://github.com/Thinklab-SJTU/One-Shot-Cardinality-NN-Solver)

    *Wang, Runzhong and Shen, Li and Chen, Yiting and Yan, Junchi and Yang, Xiaokang and Tao, Dacheng*

### [Boolean Satisfiability](#content)

1. **Graph neural networks and boolean satisfiability.** Arxiv, 2017. [paper](https://arxiv.org/pdf/1702.03592)

    *Bünz, Benedikt, and Matthew Lamm.*

2. **Learning a SAT solver from single-bit supervision.** Arxiv, 2018. [paper](https://arxiv.org/pdf/1903.04671), [code](https://github.com/dselsam/neurosat)

    *Selsam, Daniel, Matthew Lamm, Benedikt Bünz, Percy Liang, Leonardo de Moura, and David L. Dill.*

3. **Machine learning-based restart policy for CDCL SAT solvers.** SAT, 2018. [paper](http://www.t-news.cn/Floc2018/FLoC2018-pages/proceedings_paper_477.pdf)

    *Liang, Jia Hui, Chanseok Oh, Minu Mathew, Ciza Thomas, Chunxiao Li, and Vijay Ganesh.*

4. **Learning to solve circuit-SAT: An unsupervised differentiable approach.** ICLR, 2019. [paper](https://openreview.net/pdf?id=BJxgz2R9t7), [code](https://github.com/johannaSommer/generalization-neural-co-solvers)

    *Amizadeh, Saeed, Sergiy Matusevych, and Markus Weimer.*

5. **Learning Local Search Heuristics for Boolean Satisfiability.** NeurIPS, 2019. [paper](https://www.cs.cmu.edu/~eyolcu/papers/learning-local-search-heuristics-sat.pdf), [code](https://github.com/emreyolcu/sat)

    *Yolcu, Emre and Poczos, Barnabas*

6. **Improving SAT solver heuristics with graph networks and reinforcement learning.** Arxiv, 2019. [paper](https://arxiv.org/pdf/1909.11830)

    *Kurin, Vitaly, Saad Godil, Shimon Whiteson, and Bryan Catanzaro.*

7. **Graph neural reasoning may fail in certifying boolean unsatisfiability.** Arxiv, 2019. [paper](https://arxiv.org/pdf/1909.11588)

    *Chen, Ziliang, and Zhanfu Yang.*

8. **Guiding high-performance SAT solvers with unsat-core predictions.** SAT, 2019. [paper](https://arxiv.org/pdf/1903.04671)

    *Selsam, Daniel, and Nikolaj Bjørner.*

9. **G2SAT: Learning to Generate SAT Formulas.** NeurIPS, 2019. [paper](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7138247/), [code](https://github.com/JiaxuanYou/G2SAT)

    *You, Jiaxuan, Haoze Wu, Clark Barrett, Raghuram Ramanujan, and Jure Leskovec.*

10. **Learning Heuristics for Quantified Boolean Formulas through Reinforcement Learning.** Arxiv, 2019. [paper](https://arxiv.org/pdf/1807.08058), [code](https://github.com/lederg/learningqbf)

    *Lederman, Gil, Markus N. Rabe, Edward A. Lee, and Sanjit A. Seshia.*

11. **Enhancing SAT solvers with glue variable predictions.** Arxiv, 2020. [paper](https://arxiv.org/pdf/2007.02559)

    *Han, Jesse Michael.*

12. **Can Q-Learning with Graph Networks Learn a Generalizable Branching Heuristic for a SAT Solver?** NeurIPS, 2020. [paper](http://www.cs.ox.ac.uk/people/shimon.whiteson/pubs/kurinnips20.pdf)

    *Whiteson, Shimon.*

13. **Online Bayesian Moment Matching based SAT Solver Heuristics.** ICML, 2020. [paper](http://proceedings.mlr.press/v119/duan20c/duan20c.pdf), [code](https://github.com/saeednj/BMMSAT)

    *Duan, Haonan, Saeed Nejati, George Trimponias, Pascal Poupart, and Vijay Ganesh.*

14. **Learning Clause Deletion Heuristics with Reinforcement Learning.** AITP, 2020. [paper](http://aitp-conference.org/2020/abstract/paper_25.pdf)

    *Vaezipoor, Pashootan, Gil Lederman, Yuhuai Wu, Roger Grosse, and Fahiem Bacchus.*

15. **Classification of SAT problem instances by machine learning methods.** CEUR, 2020. [paper](http://ceur-ws.org/Vol-2650/paper11.pdf)

    *Danisovszky, Márk, Zijian Győző Yang, and Gábor Kusper.*

16. **Predicting Propositional Satisfiability via End-to-End Learning.** AAAI, 2020. [paper](https://ojs.aaai.org/index.php/AAAI/article/download/5733/5589)

    *Cameron, Chris, Rex Chen, Jason Hartford, and Kevin Leyton-Brown.*

17. **Neural heuristics for SAT solving.** Arxiv, 2020. [paper](https://arxiv.org/pdf/2005.13406)

    *Jaszczur, Sebastian, Michał Łuszczyk, and Henryk Michalewski.*

18. **NLocalSAT: Boosting Local Search with Solution Prediction.** Arxiv, 2020. [paper](https://arxiv.org/pdf/2001.09398), [code](https://github.com/myxxxsquared/NLocalSAT)

    *Zhang, Wenjie, Zeyu Sun, Qihao Zhu, Ge Li, Shaowei Cai, Yingfei Xiong, and Lu Zhang.*

19. **Optimistic tree search strategies for black-box combinatorial optimization** NeurlPS, 2022. [paper](https://openreview.net/forum?id=JGLW4DvX11F)

    *Malherbe, Cedric and Grosnit, Antoine and Tutunov, Rasul and Ammar, Haitham Bou and Wang, Jun*

20. **Goal-Aware Neural SAT Solver.** IJCNN, 2022. [paper](https://ieeexplore.ieee.org/document/9892733)

    *Ozolins, Emils, Karlis Freivalds, Andis Draguns, Eliza Gaile, Ronalds Zakovskis, and Sergejs Kozlovics.*

21. **NeuroComb: Improving SAT Solving with Graph Neural Networks.** Arxiv, 2022. [paper](https://arxiv.org/abs/2110.14053)

    *Wang, Wenxi, Yang Hu, Mohit Tiwari, Sarfraz Khurshid, Kenneth McMillan, and Risto Miikkulainen.*

22. **On the Performance of Deep Generative Models of Realistic SAT Instances.** SAT, 2022. [paper](https://drops.dagstuhl.de/opus/volltexte/2022/16677/pdf/LIPIcs-SAT-2022-3.pdf)

    *Garzón, Iván, Pablo Mesejo, and Jesús Giráldez-Cru.*

23. **DeepSAT: An EDA-Driven Learning Framework for SAT.** Arxiv, 2022. [paper](http://arxiv.org/abs/2205.13745)

    *Li, Min, Zhengyuan Shi, Qiuxia Lai, Sadaf Khan, and Qiang Xu.*

24. **SATformer: Transformers for SAT Solving.** Arxiv, 2022. [paper](https://arxiv.org/abs/2209.00953)

    *Shi, Zhengyuan, Min Li, Sadaf Khan, Hui-Ling Zhen, Mingxuan Yuan, and Qiang Xu.*

25. **Augment with Care: Contrastive Learning for Combinatorial Problems.** ICML, 2022. [paper](https://proceedings.mlr.press/v162/duan22b.html), [code](https://github.com/h4duan/contrastive-sat)

    *Duan, Haonan, Pashootan Vaezipoor, Max B. Paulus, Yangjun Ruan and Chris J. Maddison*

26. **NSNet: A General Neural Probabilistic Framework for Satisfiability Problems** NeurIPS, 2022. [paper](https://arxiv.org/abs/2211.03880)

    *Zhaoyu Li, Xujie Si*

27. **Neural Set Function Extensions: Learning with Discrete Functions in High Dimensions** NeurIPS, 2022. [paper](https://arxiv.org/abs/2208.04055)

    *Nikolaos Karalias, Joshua Robinson, Andreas Loukas, Stefanie Jegelka*

28. **Generalization of Neural Combinatorial Solvers Through the Lens of Adversarial Robustness** ICLR, 2022. [paper](https://openreview.net/forum?id=vJZ7dPIjip3)

    *Simon Geisler, Johanna Sommer, Jan Schuchardt, Aleksandar Bojchevski and Stephan Günnemann*

### [Mixed Integer Programming](#content)

1. **Sequential model-based optimization for general algorithm configuration** International conference on learning and intelligent optimization, 2011. [journal](https://link.springer.com/chapter/10.1007/978-3-642-25566-3_40)

    *Hutter, Frank and Hoos, Holger H and Leyton-Brown, Kevin*

2. **Non-model-based Search Guidance for Set Partitioning Problems** AAAI, 2012. [paper](https://www.aaai.org/ocs/index.php/AAAI/AAAI12/paper/view/5082)

    *Kadioglu, Serdar and Malitsky, Yuri and Sellmann, Meinolf*

3. **A Aupervised Machine Learning Approach to Variable Branching in Branch-and-bound** Citeseer, 2014. [journal](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=f35ba2bbc87dd31ae0a89d3ed9538fec9d15b4f0)

    *Alvarez, Alejandro Marcos and Louveaux, Quentin and Wehenkel, Louis*

4. **Learning to Search in Branch-and-Bound Algorithms** NeurlPS, 2014. [paper](http://papers.nips.cc/paper/5495-learning-to-search-in-branch-and-bound-algorithms)

    *He, He and Daume III, Hal and Eisner, Jason M*

5. **Learningto Branch in Mixed Integer Programming** AAAI, 2016. [paper](https://www.aaai.org/ocs/index.php/AAAI/AAAI16/paper/download/12514/11657)

    *E. B. Khalil, P. L. Bodic, L. Song, G. Nemhauser, B. Dilkina*

6. **Dash: Dynamic Approach for Switching Heuristics** European Journal of Operational Research, 2016. [journal](https://www.sciencedirect.com/science/article/pii/S0377221715007559)

    *Di Liberto, Giovanni and Kadioglu, Serdar and Leo, Kevin and Malitsky, Yuri*

7. **Learning When to Use a Decomposition** International conference on AI and OR techniques in constraint programming for combinatorial optimization problems, 2017. [journal](https://link.springer.com/chapter/10.1007/978-3-319-59776-8_16)

    *Kruber, Markus and L{\u}bbecke Marco E and Parmentier  Axel"*

8. **Learning to Run Heuristics in Tree Search** IJCAI, 2017. [paper](https://www.ijcai.org/proceedings/2017/0092.pdf)

    *Khalil, Elias B and Dilkina, Bistra and Nemhauser, George L and Ahmed, Shabbir and Shao, Yufen*

9. **Exact Combinatorial Optimization with Graph Convolutional Neural Networks** NeurlPS, 2019. [paper](https://arxiv.org/abs/1906.01629), [code](https://github.com/ds4dm/learn2branch)

    *Gasse, Maxime and Chetelat, Didier and Ferroni, Nicola and Charlin, Laurent and Lodi, Andrea*

10. **Improving Learning to Branch via Reinforcement Learning** NeurIPS Workshop, 2020. [paper](https://openreview.net/forum?id=z4D7-PTxTb)

    *Sun, Haoran and Chen, Wenbo and Li, Hui and Song, Le.*

11. **Reinforcement learning for variable selection in a branch and bound algorithm** International Conference on Integration of Constraint Programming, 2020. [journal](https://link.springer.com/chapter/10.1007/978-3-030-58942-4_12)

    *Etheve, Marc and Al{\`e}s, Zacharie and Bissuel, C{\^o}me and Juan, Olivier and Kedad-Sidhoum, Safia*

12. **Random sampling and machine learning to understand good decompositions** Annals of Operations Research, 2020. [journal](https://link.springer.com/article/10.1007/s10479-018-3067-9)

    *Basso, Saverio and Ceselli, Alberto and Tettamanzi, Andrea*

13. **Hybrid Models for Learning to Branch** NeurlPS, 2020. [paper](https://arxiv.org/abs/2006.15212), [code](https://github.com/pg2455/Hybrid-learn2branch)

    *Gupta, Prateek and Gasse, Maxime and Khalil, Elias B and Kumar, M Pawan and Lodi, Andrea and Bengio, Yoshua*

14. **Reinforcement Learning for Integer Programming: Learning to Cut** ICML, 2020. [paper](http://proceedings.mlr.press/v119/tang20a.html)

    *Tang, Yunhao and Agrawal, Shipra and Faenza, Yuri*

15. **Solving Mixed Integer Programs Using Neural Networks** Arxiv, 2020. [paper](https://arxiv.org/abs/2012.13349)

    *Nair, Vinod and Bartunov, Sergey and Gimeno, Felix and von Glehn, Ingrid and Lichocki, Pawel and Lobov, Ivan and O'Donoghue, Brendan and Sonnerat, Nicolas and Tjandraatmadja, Christian and Wang, Pengming and others*

16. **Learning Efficient Search Approximation in Mixed Integer Branch and Bound** Arxiv, 2020. [paper](https://arxiv.org/abs/2007.03948)

    *Yilmaz, Kaan and Yorke-Smith, Neil*

17. **Learning a Large Neighborhood Search Algorithm for Mixed Integer Programs** Arxiv, 2020. [paper](https://arxiv.org/abs/2107.10201)

    *Sonnerat, Nicolas and Wang, Pengming and Ktena, Ira and Bartunov, Sergey and Nair, Vinod*

18. **A General Large Neighborhood Search Framework for Solving Integer Linear Programs** NeurlPS, 2020. [paper](https://arxiv.org/abs/2004.00422)

    *Song, Jialin and Lanka, Ravi and Yue, Yisong and Dilkina, Bistra*

19. **Neural Large Neighborhood Search** NeurlPS Workshop, 2020. [paper](https://openreview.net/forum?id=xEQhKANoVW)

    *Nair, Vinod and Alizadeh, Mohammad and others*

20. **Accelerating Primal Solution Findings for Mixed Integer Programs Based on Solution Prediction** AAAI, 2020. [paper](https://arxiv.org/abs/1906.09575)

    *Ding, Jian-Ya, Chao Zhang, Lei Shen, Shengyin Li, Bing Wang, Yinghui Xu, and Le Song*

21. **CombOptNet: Fit the Right NP-Hard Problem by Learning Integer Programming Constraints** Arxiv, 2021. [paper](https://openreview.net/forum?id=z4D7-PTxTb), [code](https://github.com/martius-lab/CombOptNet)

    *Paulus, Anselm and Rolinek, Michal and Musil, Vit and Amos, Brandon and Martius, Georg*

22. **Reinforcement Learning for (Mixed) Integer Programming: Smart Feasibility Pump** ICML Workshop, 2021. [paper](https://arxiv.org/abs/2102.09663)

    *Qi, Meng and Wang, Mengxin and Shen, Zuo-Jun*

23. **Parameterizing Branch-and-Bound Search Trees to Learn Branching Policies** AAAI, 2021. [paper](https://www.aaai.org/AAAI21Papers/AAAI-9826.ZarpellonG.pdf), [code](https://github.com/ds4dm/branch-search-trees)

    *Zarpellon, Giulia and Jo, Jason and Lodi, Andrea and Bengio, Yoshua*

24. **Learning to Select Cuts for Efficient Mixed-Integer Programming** Arxiv, 2021. [journal](https://arxiv.org/abs/2105.13645)

    *Huang, Zeren and Wang, Kerong and Liu, Furui and Zhen, Hui-ling and Zhang, Weinan and Yuan, Mingxuan and Hao, Jianye and Yu, Yong and Wang, Jun*

25. **Confidence Threshold Neural Diving** NeurIPS ML4CO Competition Workshop, 2021. [paper](https://arxiv.org/abs/2202.07506)

    *Taehyun Yoon*

26. **Learning large neighborhood search policy for integer programming** NeurlPS, 2021. [paper](https://proceedings.neurips.cc/paper/2021/hash/fc9e62695def29ccdb9eb3fed5b4c8c8-Abstract.html)

    *Wu, Yaoxin and Song, Wen and Cao, Zhiguang and Zhang, Jie*

27. **Generative Deep Learning for Decision Making in Gas Networks** Arxiv, 2021. [paper](https://arxiv.org/abs/2102.02125)

    *Lovis Anderson and Mark Turner and Thorsten Koch*

28. **Offline Constraint Screening for Online Mixed-integer Optimization** Arxiv, 2021. [paper](https://arxiv.org/abs/2103.13074)

    *Asunción Jiménez-Cordero and Juan Miguel Morales and Salvador Pineda*

29. **Mixed Integer Programming versus Evolutionary Computation for Optimizing a Hard Real-World Staff Assignment Problem** ICAPS, 2021. [paper](https://ojs.aaai.org/index.php/ICAPS/article/view/3521)

    *Peters, Jannik and Stephan, Daniel and Amon, Isabel and Gawendowicz, Hans and Lischeid, Julius and Salabarria, Lennart and Umland, Jonas and Werner, Felix and Krejca, Martin S and Rothenberger, Ralf and others*

30. **Learning To Scale Mixed-Integer Programs** AAAI, 2021. [paper](https://www.aaai.org/AAAI21Papers/AAAI-7940.BertholdT.pdf)

    *Berthold, Timo, and Gregor Hendel*

31. **Learning Pseudo-Backdoors for Mixed Integer Programs** AAAI, 2021. [paper](https://arxiv.org/pdf/2106.05080.pdf)

    *Aaron Ferber and Jialin Song and Bistra Dilkina and Yisong Yue*

32. **Confidence Threshold Neural Diving** NeurIPS ML4CO Competition Workshop, 2021. [paper](https://arxiv.org/abs/2202.07506)

    *Taehyun Yoon*

33. **Learning Primal Heuristics for Mixed Integer Programs** IJCNN, 2021. [paper](https://arxiv.org/pdf/2107.00866.pdf)

    *Shen, Yunzhuang and Sun, Yuan and Eberhard, Andrew and Li, Xiaodong*

34. **Learning to Solve Large-scale Security-constrained Unit Commitment Problems** INFORMS Journal on Computing, 2021. [journal](https://pubsonline.informs.org/doi/abs/10.1287/ijoc.2020.0976)

    *Xavier, {\'A}linson S and Qiu, Feng and Ahmed, Shabbir*

35. **Learning to Branch with Tree MDPs** Arxiv, 2022. [paper](https://arxiv.org/abs/2205.11107), [code](https://github.com/lascavana/rl2branch)

    *Scavuzzo, Lara, F. Chen, Didier Ch'etelat, Maxime Gasse, Andrea Lodi, N. Yorke-Smith and Karen Aardal.*

36. **A Deep Reinforcement Learning Framework For Column Generation** Arxiv, 2022. [paper](https://arxiv.org/abs/2206.02568)

    *Chi, Cheng, Amine Mohamed Aboussalah, Elias Boutros Khalil, Juyoung Wang and Zoha Sherkat-Masoumi.*

37. **Ranking Constraint Relaxations for Mixed Integer Programs Using a Machine Learning Approach** Arxiv, 2022. [journal](https://arxiv.org/abs/2207.00219)

    *Weiner, Jake, Andreas T. Ernst, Xiaodong Li and Yuan Sun.*

38. **Learning to Accelerate Approximate Methods for Solving Integer Programming via Early Fixing** Arxiv, 2022. [journal](https://arxiv.org/abs/2207.02087), [code](https://github.com/SCLBD/Accelerated-Lpbox-ADMM)

    *Li, Longkang and Baoyuan Wu.*

39. **Learning to Cut by Looking Ahead: Cutting Plane Selection via Imitation Learning** ICML, 2022. [paper](https://proceedings.mlr.press/v162/paulus22a.html)

    *Paulus, Max B., Giulia Zarpellon, Andreas Krause, Laurent Charlin and Chris J. Maddison.*

40. **Lookback for Learning to Branch** Arxiv, 2022. [journal](https://arxiv.org/abs/2206.14987)

    *Gupta, Prateek, Elias Boutros Khalil, Didier Chet'elat, Maxime Gasse, Yoshua Bengio, Andrea Lodi and M. Pawan Kumar.*

41. **Learning to Search in Local Branching** AAAI, 2022. [paper](https://ojs.aaai.org/index.php/AAAI/article/view/20294), [code](https://github.com/pandat8/ML4LB)

    *Liu, Defeng and Fischetti, Matteo and Lodi, Andrea*

42. **Deep Reinforcement Learning for Exact Combinatorial Optimization: Learning to Branch** Arxiv, 2022. [paper](https://arxiv.org/abs/2206.06965)

    *Zhang, Tianyu and Banitalebi-Dehkordi, Amin and Zhang, Yong*

43. **Learning to Branch with Tree-aware Branching Transformers** Knowledge-Based Systems, 2022. [journal](https://www.sciencedirect.com/science/article/pii/S0950705122007298?via%3Dihub), [code](https://github.com/linjc16/TBranT)

    *Lin, Jiacheng and Zhu, Jialin and Wang, Huangang and Zhang, Tao*

44. **An Improved Reinforcement Learning Algorithm for Learning to Branch** Arxiv, 2022. [paper](https://arxiv.org/abs/2201.06213)

    *Qu, Qingyu and Li, Xijun and Zhou, Yunfan and Zeng, Jia and Yuan, Mingxuan and Wang, Jie and Lv, Jinhu and Liu, Kexin and Mao, Kun*

45. **Learning to Use Local Cuts** Arxiv, 2022. [paper](https://arxiv.org/abs/2206.11618)

    *Berthold, Timo and Francobaldi, Matteo and Hendel, Gregor*

46. **DOGE-Train: Discrete Optimization on GPU with End-to-end Training** Arxiv, 2022. [paper](https://arxiv.org/abs/2205.11638)

    *Abbas, Ahmed and Swoboda, Paul*

47. **Structural Analysis of Branch-and-Cut and the Learnability of Gomory Mixed Integer Cuts** NeurIPS, 2022. [paper](https://openreview.net/forum?id=e2gRdexoTZf)

    *Balcan, Maria-Florina and Prasad, Siddharth and Sandholm, Tuomas and Vitercik, Ellen*

48. **A GNN-Guided Predict-and-Search Framework for Mixed-Integer Linear Programming** ICLR, 2023. [paper](https://openreview.net/forum?id=pHMpgT5xWaE), [code](https://github.com/sribdcn/Predict-and-Search_MILP_method)

    *Han, Qingyu and Yang, Linxin and Chen, Qian and Zhou, Xiang and Zhang, Dong and Wang, Akang and Sun, Ruoyu and Luo, Xiaodong*

49. **Learning Cut Selection for Mixed-Integer Linear Programming via Hierarchical Sequence Model** ICLR, 2023. [paper](https://openreview.net/forum?id=Zob4P9bRNcK), [code](https://github.com/MIRALab-USTC/L2O-HEM-Torch)

    *Wang, Zhihai and Li, Xijun and Wang, Jie and Kuang, Yufei and Yuan, Mingxuan and Zeng, Jia and Zhang, Yongdong and Wu, Feng*

### [Causal Discovery](#content)

1. **DAGs with NO TEARS: Continuous Optimization for Structure Learning.** NeurIPS, 2018. [paper](https://arxiv.org/pdf/1803.01422.pdf)

    *Zheng, Xun and Aragam, Bryon and Ravikumar, Pradeep and Xing, Eric.*

2. **Causal Discovery with Reinforcement Learning.** ICLR, 2020. [paper](https://arxiv.org/abs/1906.04477)

    *Zhu, Shengyu and Ng, Ignavier and Chen, Zhitang.*

3. **Large-Scale Differentiable Causal Discovery of Factor Graphs** NeurIPS, 2022. [paper](https://openreview.net/forum?id=k713e8vXzwR), [code](https://github.com/Genentech/dcdfg)

    *Lopez, Romain and H{\"u}tter, Jan-Christian and Pritchard, Jonathan K and Regev, Aviv*

4. **Boosting Causal Discovery via Adaptive Sample Reweighting** ICLR, 2023. [paper](https://openreview.net/forum?id=LNpMtk15AS4), [code](https://github.com/anzhang314/ReScore)

    *Zhang, An and Liu, Fangfu and Ma, Wenchang and Cai, Zhibo and Wang, Xiang and Chua, Tat-seng*

5. **CUTS: Neural Causal Discovery from Irregular Time-Series Data** ICLR, 2023. [paper](https://openreview.net/forum?id=UG8bQcD3Emv), [code](https://github.com/jarrycyx/unn)

    *Cheng, Yuxiao and Yang, Runzhao and Xiao, Tingxiong and Li, Zongren and Suo, Jinli and He, Kunlun and Dai, Qionghai*

6. **Diffusion Models for Causal Discovery via Topological Ordering** ICLR, 2023. [paper](https://openreview.net/forum?id=Idusfje4-Wq), [code](https://github.com/vios-s/DiffAN)

    *Sanchez, Pedro and Liu, Xiao and O'Neil, Alison Q and Tsaftaris, Sotirios A*

### [Game Theoretic Semantics](#content)

1. **First-Order Problem Solving through Neural MCTS based Reinforcement Learning.** Arxiv, 2021. [paper](https://arxiv.org/abs/2101.04167)

    *Xu, Ruiyang and Kadam, Prashank and Lieberherr, Karl.*

### [Car Dispatch](#content)

1. **Dispatch of autonomous vehicles for taxi services: A deep reinforcement learning approach** Transportation Research, 2020. [journal](https://www.sciencedirect.com/science/article/pii/S0968090X19312227)

    *Chao Mao, Yulin Liu, Zuo-Jun (Max) Shen*

### [Electronic Design Automation](#content)

1. **⭐On Joint Learning for Solving Placement and Routing in Chip Design** NeurIPS, 2021. [paper](https://arxiv.org/abs/2111.00234), [code](https://github.com/Thinklab-SJTU/EDA-AI)

    *Cheng, Ruoyu and Yan, Junchi*

2. **A graph placement methodology for fast chip design** Nature, 2021. [journal](https://www.nature.com/articles/s41586-021-03544-w.pdf)

    *Azalia Mirhoseini, Anna Goldie, Mustafa Yazgan, Joe Wenjie Jiang, Ebrahim Songhori, Shen Wang, Young-Joon Lee, Eric Johnson, Omkar Pathak, Azade Nazi, Jiwoo Pak, Andy Tong, Kavya Srinivasa, William Hang, Emre Tuncer, Quoc V. Le, James Laudon, Richard Ho, Roger Carpenter & Jeff Dean*

3. **Unsupervised Learning for Combinatorial Optimization with Principled Objective Relaxation** NeurIPS, 2022. [paper](https://openreview.net/forum?id=HjNn9oD_v47), [code](https://github.com/Graph-COM/CO_ProxyDesign)

    *Wang, Haoyu Peter and Wu, Nan and Yang, Hang and Hao, Cong and Li, Pan*

4. **CktGNN: Circuit Graph Neural Network for Electronic Design Automation** ICLR, 2023. [paper](https://openreview.net/forum?id=NE2911Kq1sp)

    *Dong, Zehao and Cao, Weidong and Zhang, Muhan and Tao, Dacheng and Chen, Yixin and Zhang, Xuan*

### [Conjunctive Query Containment](#content)

1. **It's Not What Machines Can Learn It's What We Cannot Teach** ICML, 2020. [paper](http://proceedings.mlr.press/v119/yehuda20a/yehuda20a.pdf)

    *Gal Yehuda, Moshe Gabel and Assaf Schuster*

### [Orienteering Problem](#content)

1. **A reinforcement learning approach to the orienteering problem with time windows** Computers & Operations Research, 2021. [paper](https://arxiv.org/abs/2011.03647v2), [code](https://github.com/mustelideos/optw_rl)

    *Ricardo Gama, Hugo L. Fernandes*

### [Virtual Network Embedding](#content)

1. **Virtual Network Embedding via Monte Carlo Tree Search** IEEE Trans. Cybern, 2017. [journal](https://ieeexplore.ieee.org/document/7859375)

    *Soroush Haeri; Ljiljana Trajković*

2. **A novel reinforcement learning algorithm for virtual network embedding** Neurocomputing, 2018. [journal](https://www.sciencedirect.com/science/article/abs/pii/S0925231218300420)

    *Haipeng Yao,Xu Chen, Maozhen Li, Peiying Zhang, Luyao Wang*

3. **NeuroViNE: A Neural Preprocessor for Your Virtual Network Embedding Algorithm** INFOCOM, 2018. [paper](https://ieeexplore.ieee.org/document/8486263)

    *Andreas Blenk; Patrick Kalmbach; Johannes Zerwas; Michael Jarschel; Stefan Schmid; Wolfgang Kellerer*

4. **A Virtual Network Embedding Algorithm Based On Double-Layer Reinforcement Learning** TCJ, 2019. [journal](https://ieeexplore.ieee.org/document/9514735)

    *Meng Li; MeiLian Lu*

5. **NFVdeep: Adaptive Online Service Function Chain Deployment with Deep Reinforcement Learning** IWQoS, 2019. [paper](https://ieeexplore.ieee.org/document/9068634)

    *Yikai Xiao; Qixia Zhang; Fangming Liu; Jia Wang; Miao Zhao; Zhongxing Zhang; Jiaxing Zhang*

6. **A Continuous-Decision Virtual Network Embedding Scheme Relying on Reinforcement Learning** IEEE TNSM, 2020. [journal](https://ieeexplore.ieee.org/document/8982091)

    *Haipeng Yao; Sihan Ma; Jingjing Wang; Peiying Zhang; Chunxiao Jiang; Song Guo*

7. **Automatic Virtual Network Embedding A Deep Reinforcement Learning Approach With Graph Convolutional Networks** J-SAC, 2020. [journal](https://ieeexplore.ieee.org/document/9060910)

    *Zhongxia Yan; Jingguo Ge; Yulei Wu; Liangxiong Li; Tong Li*

8. **A Q-learning-based approach for virtual network embedding in data center** NCA, 2020. [journal](https://link.springer.com/article/10.1007/s00521-019-04376-6)

    *Ying Yuan, Zejie Tian, Cong Wang, Fanghui Zheng & Yanxia Lv*

9. **Accelerating Virtual Network Embedding with Graph Neural Networks** CNSM, 2020. [journal](https://ieeexplore.ieee.org/document/9269128)

    *Farzad Habibi; Mahdi Dolati; Ahmad Khonsari; Majid Ghaderi*

10. **Dynamic Virtual Network Embedding Algorithm Based on Graph Convolution Neural Network and Reinforcement Learning** IoT-J, 2021. [journal](https://ieeexplore.ieee.org/document/9475485)

    *Peiying Zhang; Chao Wang; Neeraj Kumar; Weishan Zhang; Lei Liu*

11. **Deep Reinforcement Based Optimization of Function Splitting in Virtualized Radio Access Networks** ICC, 2021. [paper](https://ieeexplore.ieee.org/document/9473703), [code](https://github.com/rubensolozabal/vnf_placement_optimization_rl)

    *Fahri Wisnu Murti; Samad Ali; Matti Latva-aho*

12. **DRL-SFCP: Adaptive Service Function Chains Placement with Deep Reinforcement Learning** ICC, 2021. [paper](https://ieeexplore.ieee.org/document/9500964)

    *Tianfu Wang; Qilin Fan; Xiuhua Li; Xu Zhang; Qingyu Xiong; Shu Fu; Min Gao*

### [Optical Power Flow](#content)

1. **Predicting AC Optimal Power Flows: Combining Deep Learning and Lagrangian Dual Methods** AAAI, 2020. [paper](https://ojs.aaai.org/index.php/AAAI/article/view/5403)

    *Ferdinando Fioretto, Terrence W.K. Mak, Pascal Van Hentenryck*

2. **Adversarially Robust Learning for Security-Constrained Optimal Power Flow** NeurIPS, 2021. [paper](https://proceedings.neurips.cc/paper/2021/hash/f0f07e680de407b0f12abf15bd520097-Abstract.html)

    *Priya Donti, Aayushya Agarwal, Neeraj Vijay Bedmutha, Larry Pileggi, J. Zico Kolter*

### [Facility Location Problem](#content)

1. **Solving uncapacitated P-Median problem with reinforcement learning assisted by graph attention networks** Applied Intelligence, 2023. [paper](https://link.springer.com/article/10.1007/s10489-022-03453-z)

    *Wang, Chenguang and Han, Congying and Guo, Tiande and Ding, Man*

2. **⭐Towards One-shot Neural Combinatorial Solvers: Theoretical and Empirical Notes on the Cardinality-Constrained Case** ICLR, 2023. [paper](https://openreview.net/forum?id=h21yJhdzbwz), [code](https://github.com/Thinklab-SJTU/One-Shot-Cardinality-NN-Solver)

    *Wang, Runzhong and Shen, Li and Chen, Yiting and Yan, Junchi and Yang, Xiaokang and Tao, Dacheng*

### [Portfolio Optimization](#content)

1. **Integrating prediction in mean-variance portfolio optimization** Quantitative Finance, 2023. [paper](https://arxiv.org/pdf/2102.09287.pdf)

    *Butler, Andrew and Kwon, Roy H*

2. **⭐Towards One-shot Neural Combinatorial Solvers: Theoretical and Empirical Notes on the Cardinality-Constrained Case** ICLR, 2023. [paper](https://openreview.net/forum?id=h21yJhdzbwz), [code](https://github.com/Thinklab-SJTU/One-Shot-Cardinality-NN-Solver)

    *Wang, Runzhong and Shen, Li and Chen, Yiting and Yan, Junchi and Yang, Xiaokang and Tao, Dacheng*

### [Sorting & Ranking](#content)

1. **Ranking via sinkhorn propagation** Arxiv, 2011. [paper](https://arxiv.org/abs/1106.1925#)

    *Ryan Prescott Adams, Richard S. Zemel*

2. **Predict+optimise with ranking objectives: exhaustively learning linear functions** IJCAI, 2019. [paper](https://dl.acm.org/doi/abs/10.5555/3367032.3367186)

    *Demirovic, Emir and Stuckey, Peter J. and Bailey, James and Chan, Jeffrey and Leckie, Christopher and Ramamohanarao, Kotagiri and Guns, Tias*

3. **Stochastic Optimization of Sorting Networks via Continuous Relaxations** ICLR, 2019. [paper](https://openreview.net/forum?id=H1eSS3CcKX), [code](https://github.com/ermongroup/neuralsort)

    *Aditya Grover, Eric Wang, Aaron Zweig, Stefano Ermon*

4. **Differentiable Ranking and Sorting using Optimal Transport** NeurIPS, 2019. [paper](https://papers.nips.cc/paper/2019/hash/d8c24ca8f23c562a5600876ca2a550ce-Abstract.html)

    *Marco Cuturi, Olivier Teboul, Jean-Philippe Vert*

5. **Optimizing Rank-Based Metrics With Blackbox Differentiation** CVPR, 2020. [paper](https://openaccess.thecvf.com/content_CVPR_2020/papers/Rolinek_Optimizing_Rank-Based_Metrics_With_Blackbox_Differentiation_CVPR_2020_paper.pdf), [code](https://github.com/martius-lab/blackbox-backprop)

    *Marin Vlastelica,Anselm Paulus,Vít Musil,Georg Martius and Michal Rolínek*

6. **Fast Differentiable Sorting and Ranking** ICML, 2020. [paper](http://proceedings.mlr.press/v119/blondel20a/blondel20a.pdf), [code](https://github.com/google-research/fast-soft-sort/)

    *Mathieu Blondel Olivier Teboul Quentin Berthet Josip Djolonga*

7. **SoftSort: A Continuous Relaxation for the argsort Operator** ICML, 2020. [paper](http://proceedings.mlr.press/v119/prillo20a/prillo20a.pdf), [code](https://github.com/sprillo/softsort)

    *Sebastian Prillo, Julian Martin Eisenschlos*

8. **differentiable top k with optimal transport** NeurIPS, 2020. [paper](https://proceedings.neurips.cc/paper/2020/hash/ec24a54d62ce57ba93a531b460fa8d18-Abstract.html)

    *Yujia Xie, Hanjun Dai, Minshuo Chen, Bo Dai, Tuo Zhao, Hongyuan Zha, Wei Wei, Tomas Pfister*

9. **Automatic Loss Function Search for Predict-Then-Optimize Problems with Strong Ranking Property** ICLR, 2022. [paper](https://openreview.net/forum?id=hSktDu-h94), [code](https://github.com/Microsoft/AutoPredOptConnector)

    *Boshi Wang, Jialin Yi, Hang Dong, Bo Qiao, Chuan Luo, Qingwei Lin*

10. **Decision-Focused Learning: Through the Lens of Learning to Rank** ICML, 2022. [paper](https://proceedings.mlr.press/v162/mandi22a.html), [code](https://github.com/jayman91/ltr-predopt)

    *Jayanta Mandi, Vı́ctor Bucarey, Maxime Mulamba Ke Tchomba, Tias Guns*

11. **PiRank-Scalable Learning To Rank via Differentiable Sorting** NeurIPS, 2022. [paper](https://openreview.net/forum?id=dL8p6rLFTS3), [code](https://github.com/ermongroup/pirank)

    *Robin Marcel Edwin Swezey, Aditya Grover, Bruno Charron, Stefano Ermon*

### [Knapsack](#content)

1. **A Pointer Network Based Deep Learning Algorithm  for 0-1 Knapsack Problem** ICACI, 2018. [paper](https://ieeexplore.ieee.org/abstract/document/8377505)

    *Gu Shenshen, and Tao Hao*

2. **An Investigation into Prediction + Optimisation for the Knapsack Problem** CPAIOR, 2019. [paper](https://link.springer.com/chapter/10.1007/978-3-030-19212-9_16)

    *"Demirovic Emir and Stuckey Peter J and Bailey James and Chan Jeffrey and Leckie Chris and Ramamohanarao Kotagiri and Guns Tias"*

3. **A Novel Method to Solve Neural Knapsack Problems** ICML, 2021. [paper](http://proceedings.mlr.press/v139/li21m.html)

    *"Li Duanshun and Liu Jing and Lee Dongeun and Seyedmazloom Ali and Kaushik Giridhar and Lee Kookjin and Park Noseong"*

4. **Provably Good Solutions to the Knapsack Problem via Neural Networks of Bounded Size** AAAI, 2021. [paper](https://pubsonline.informs.org/doi/abs/10.1287/ijoc.2021.0225)

    *Hertrich Christoph and Martin Skutella*

### [Combinatorial Drug Recommendation](#content)

1. **GAMENet: Graph Augmented MEmory Networks for Recommending Medication Combination** AAAI, 2019. [paper](https://ojs.aaai.org/index.php/AAAI/article/view/3905), [code](https://github.com/sjy1203/GAMENet)

    *Shang, Junyuan and Xiao, Cao and Ma, Tengfei and Li, Hongyan and Sun, Jimeng*

2. **SafeDrug: Dual Molecular Graph Encoders for Recommending Effective and Safe Drug Combinations** IJCAI, 2021. [paper](https://www.ijcai.org/proceedings/2021/0514.pdf), [code](https://github.com/ycq091044/SafeDrug)

    *Yang, Chaoqi and Xiao, Cao and Ma, Fenglong and Glass, Lucas and Sun, Jimeng*

3. **Debiased, Longitudinal and Coordinated Drug Recommendation through Multi-Visit Clinic Recordss** NeurIPS, 2022. [paper](https://openreview.net/forum?id=zVglD2W0EAS), [code](https://github.com/ssshddd/DrugRec)

    *Sun, Hongda and Xie, Shufang and Li, Shuqi and Chen, Yuhan and Wen, Ji-Rong and Yan, Rui*

4. **⭐MoleRec: Combinatorial Drug Recommendation with Substructure-Aware Molecular Representation Learning** TheWebConf, 2023. [paper](https://dl.acm.org/doi/10.1145/3543507.3583872), [code](https://github.com/yangnianzu0515/MoleRec)

    *Yang, Nianzu and Zeng, Kaipeng and Wu, Qitian and Yan, Junchi*

