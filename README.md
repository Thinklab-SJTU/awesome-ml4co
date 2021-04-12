

# Awesome Machine Learning for Combinatorial Optimization Papers
We would like to maintain a list of papers that utilize machine learning technologies to solve combinatorial optimization problems. 

We mark papers contributed by [Thinklab](thinklab.sjtu.edu.cn) by ✨.

## [Content](#content)

<table>
<tr><td colspan="2"><a href="#survey-papers">1. Survey</a></td></tr> 
<tr><td colspan="2"><a href="#problems">2. Problems</a></td></tr> 
<tr>
    <td>&emsp;<a href="#graph-matching">2.1 Graph Matching (GM) </a></td>
    <td>&ensp;<a href="#travelling-salesman-problem">2.2 Travelling Salesman Problem (TSP) </a></td>
</tr> 
<tr>
    <td>&emsp;<a href="#vehicle-routing-problem">2.3 Vehicle Routing Problem (VRP) </a></td>
    <td>&ensp;<a href="#job-shop-scheduling">2.4 Job Shop Scheduling (JSP) </a></td>
</tr>
<tr>
    <td>&emsp;<a href="#bin-packing-problem">2.5 Bin Packing Problem </a></td>
    <td>&ensp;<a href="#graph-edit-distance">2.6 Graph Edit Distance (GED) </a></td>
</tr>
<tr>
    <td>&emsp;<a href="#graph-coloring">2.7 Graph Coloring </a></td>
    <td>&ensp;<a href="#maximal-common-subgraph">2.8 Maximal Common Subgraph (MCS) </a></td>
</tr>
<tr>
    <td>&emsp;<a href="#influence-maximization">2.9 Influence Maximization </a></td>
    <td>&ensp;<a href="#maximal-independent-set">2.10 Maximal Independent Set (MIS) </a></td>
</tr>
<tr>
  <td>&emsp;<a href="#maximal-cut">2.11 Maximal Cut </a></td>
	<td>&ensp;<a href="#mixed-integer-programming">2.12 Mixed Integer Programming </a></td> 
</tr>
<tr>
<td>&emsp;<a href="#causal-discovery">2.13 Causal Discovery </a></td>
<td>&ensp;<a href="#game-theoretic-semantics">2.14 Game Theoretic Semantics</a></td> 
</tr>
<tr>
    <td>&emsp;<a href="#boolean-satisfiability">2.15 Boolean Satisfiability (SAT) </a></td>
   <td>&ensp;<a href="#differentiable-optimization">2.16 Differentiable Optimization</a></td> 
</tr>
<tr>
    <td>&emsp;<a href="#computing-resource-allocation">2.17 Computing Resource Allocation </a></td>
   <td>&ensp;<a href="#car-dispatch">2.18 Car Dispatch</a></td> 
</tr>
<tr>
    <td>&emsp;<a href="#quadratic-assignment-problem">2.18 Quadratic Assignment Problem (QAP) </a></td>
    <td>&ensp;</td>
</tr>
</table>



### [Survey Papers](#content)

1. **Machine Learning for Combinatorial Optimization: a Methodological Tour d'horizon.** EJOR, 2020. [paper](https://arxiv.org/abs/1811.06128)

    *Bengio, Yoshua and Lodi, Andrea and Prouvost, Antoine.*

2. **Reinforcement Learning for Combinatorial Optimization: A Survey.** Arxiv, 2020. [paper](https://arxiv.org/abs/2003.03600)

    *Mazyavkina, Nina and Sviridov, Sergey and Ivanov, Sergei and Burnaev, Evgeny.*

3. **✨Learning Graph Matching and Related Combinatorial Optimization Problems.** IJCAI, 2020. [paper](https://www.ijcai.org/proceedings/2020/0694.pdf)

    *Yan, Junchi and Yang, Shuang, and Hancock, Edwin R.*

## [Problems](#content)

### [Graph Matching](#content)

1. **Revised Note on Learning Algorithms for Quadratic Assignment with Graph Neural Networks** Arxiv, 2017. [paper](https://arxiv.org/pdf/1706.07450.pdf), [code](https://github.com/alexnowakvila/QAP_pt)

    *Nowak, Alex and Villar, Soledad and Bandeira, S. Afonso and Bruna, Joan*

2. **Deep Learning of Graph Matching.** CVPR, 2018. [paper](https://openaccess.thecvf.com/content_cvpr_2018/html/Zanfir_Deep_Learning_of_CVPR_2018_paper.html)

    *Zanfir, Andrei and Sminchisescu, Cristian*

3. **✨Learning Combinatorial Embedding Networks for Deep Graph Matching.** ICCV, 2019. [paper](http://openaccess.thecvf.com/content_ICCV_2019/papers/Wang_Learning_Combinatorial_Embedding_Networks_for_Deep_Graph_Matching_ICCV_2019_paper.pdf), [code](https://github.com/Thinklab-SJTU/PCA-GM)

    *Wang, Runzhong and Yan, Junchi and Yang, Xiaokang*

4. **Deep Graphical Feature Learning for the Feature Matching Problem.** ICCV, 2019. [paper](https://openaccess.thecvf.com/content_ICCV_2019/papers/Zhang_Deep_Graphical_Feature_Learning_for_the_Feature_Matching_Problem_ICCV_2019_paper.pdf)

    *Zhang, Zhen and Lee, Wee Sun*

5. **GLMNet: Graph Learning-Matching Networks for Feature Matching.** Arxiv, 2019. [paper](https://arxiv.org/abs/1911.07681)

    *Jiang, Bo and Sun, Pengfei and Tang, Jin and Luo, Bin*

6. **✨Neural Graph Matching Network: Learning Lawler's Quadratic Assignment Problem with Extension to Hypergraph and Multiple-graph Matching.** Arxiv, 2019. [paper](https://arxiv.org/abs/1911.11308)

    *Wang, Runzhong and Yan, Junchi and Yang, Xiaokang*

7. **✨Learning deep graph matching with channel-independent embedding and Hungarian attention.** ICLR, 2020. [paper](https://openreview.net/forum?id=rJgBd2NYPH)

    *Yu, Tianshu and Wang, Runzhong and Yan, Junchi and Li, Baoxin*

8. **Deep Graph Matching Consensus.** ICLR, 2020. [paper](http://arxiv.org/abs/2001.09621)

    *Fey, Matthias and Lenssen, Jan E. and Morris, Christopher and Masci, Jonathan and Kriege, Nils M.*

9. **✨Graduated Assignment for Joint Multi-Graph Matching and Clustering with Application to Unsupervised Graph Matching Network Learning.** NeurIPS, 2020. [paper](https://papers.NeurIPS.cc/paper/2020/file/e6384711491713d29bc63fc5eeb5ba4f-Paper.pdf)

    *Wang, Runzhong and Yan, Junchi and Yang, Xiaokang*

10. **✨Combinatorial Learning of Robust Deep Graph Matching: An Embedding Based Approach.** TPAMI, 2020. [paper](https://doi.org/10.1109/TPAMI.2020.3005590)

    *Wang, Runzhong and Yan, Junchi and Yang, Xiaokang*

11. **Deep Graph Matching via Blackbox Differentiation of Combinatorial Solvers.** ECCV, 2020. [paper](https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123730409.pdf), [code](https://github.com/martius-lab/blackbox-deep-graph-matching)

    *Rolinek, Michal and Swoboda, Paul and Zietlow, Dominik and Paulus, Anselm and Musil, Vit and Martius, Georg*

12. **✨Deep Reinforcement Learning of Graph Matching.** Arxiv, 2020. [paper](https://arxiv.org/abs/2012.08950)

    *Liu, Chang and Wang, Runzhong and Jiang, Zetian and Yan, Junchi*

### [Quadratic Assignment Problem](#content)

1. **Revised Note on Learning Algorithms for Quadratic Assignment with Graph Neural Networks** Arxiv, 2017. [paper](https://arxiv.org/pdf/1706.07450.pdf), [code](https://github.com/alexnowakvila/QAP_pt)

    *Nowak, Alex and Villar, Soledad and Bandeira, S. Afonso and Bruna, Joan*

2. **✨Neural Graph Matching Network: Learning Lawler's Quadratic Assignment Problem with Extension to Hypergraph and Multiple-graph Matching.** Arxiv, 2019. [paper](https://arxiv.org/abs/1911.11308)

    *Wang, Runzhong and Yan, Junchi and Yang, Xiaokang*

3. **✨Deep Reinforcement Learning of Graph Matching.** Arxiv, 2020. [paper](https://arxiv.org/abs/2012.08950)

    *Liu, Chang and Wang, Runzhong and Jiang, Zetian and Yan, Junchi*

### [Travelling Salesman Problem](#content)

1. **Learning Combinatorial Optimization Algorithms over Graphs.** NeurIPS, 2017. [paper](https://arxiv.org/abs/1704.01665)

    *Dai, Hanjun and Khalil, Elias B and Zhang, Yuyu and Dilkina, Bistra and Song, Le*

2. **POMO: Policy Optimization with Multiple Optima for Reinforcement Learning.** NeurIPS, 2018. [paper](https://arxiv.org/abs/2010.16011)

    *Kwon, Yeong-Dae and Choo, Jinho and Kim, Byoungjip and Yoon, Iljoo and Min, Seungjai and Gwon, Youngjune.*

3. **Learning Heuristics for the TSP by Policy Gradient** CPAIOR, 2018. [paper](https://link.springer.com/chapter/10.1007/978-3-319-93031-2_12), [code](https://github.com/MichelDeudon/encode-attend-navigate)

    *Michel DeudonPierre CournutAlexandre Lacoste*

4. **Attention, Learn to Solve Routing Problems!** ICLR, 2019. [paper](https://arxiv.org/abs/1803.08475)

    *Kool, Wouter and Van Hoof, Herke and Welling, Max.*

5. **Learning to Solve NP-Complete Problems: A Graph Neural Network for Decision TSP.** AAAI, 2019. [paper](https://ojs.aaai.org/index.php/AAAI/article/view/4399)

    *Prates, Marcelo and Avelar, Pedro HC and Lemos, Henrique and Lamb, Luis C and Vardi, Moshe Y.*

6. **An Efficient Graph Convolutional Network Technique for the Travelling Salesman Problem** Arxiv, 2019. [paper](https://arxiv.org/abs/1906.01227), [code](https://github.com/chaitjo/graph-convnet-tsp)

    *Chaitanya K. Joshi, Thomas Laurent, Xavier Bresson*

7. **Generalize a Small Pre-trained Model to Arbitrarily Large TSP Instances Zhang-Hua.** Arxiv, 2020. [paper](https://arxiv.org/abs/2012.10658)

    *Fu, Zhang-Hua and Qiu, Kai-Bin and Zha, Hongyuan.*

8. **Differentiation of Blackbox Combinatorial Solvers** ICLR, 2020. [paper](https://arxiv.org/pdf/1912.02175v2.pdf), [code](https://github.com/martius-lab/blackbox-backprop)

    *Marin Vlastelica, Anselm Paulus, Vít Musil, Georg Martius, Michal Rolínek*

9. **The Transformer Network for the Traveling Salesman Problem** IPAM, 2021. [paper](http://helper.ipam.ucla.edu/publications/dlc2021/dlc2021_16703.pdf)

    *Xavier Bresson，Thomas Laurent*

### [Maximal Cut](#content)

1. **Learning Combinatorial Optimization Algorithms over Graphs.** NeurIPS, 2017. [paper](https://arxiv.org/abs/1704.01665)

    *Dai, Hanjun and Khalil, Elias B and Zhang, Yuyu and Dilkina, Bistra and Song, Le*

2. **Exploratory Combinatorial Optimization with Reinforcement Learning.** AAAI, 2020. [paper](https://ojs.aaai.org/index.php/AAAI/article/view/5723)

    *LBarrett, Thomas and Clements, William and Foerster, Jakob and Lvovsky, Alex.*

3. **Erdos Goes Neural: an Unsupervised Learning Framework for Combinatorial Optimization on Graphs.** NeurIPS, 2020. [paper](https://static.aminer.cn/upload/pdf/575/1127/1864/5eede0b791e0116a23aafe7b_1.pdf)

    *Karalias, Nikolaos and Loukas, Andreas*

### [Vehicle Routing Problem](#content)

1. **Learning to Perform Local Rewriting for Combinatorial Optimization.** NeurIPS, 2019. [paper](https://arxiv.org/abs/1810.00337), [code](https://github.com/facebookresearch/neural-rewriter)

    *Chen, Xinyun and Tian, Yuandong.*

2. **Deep Reinforcement Learning for the Electric Vehicle Routing Problem with Time Windows.** Arxiv, 2020. [paper](https://arxiv.org/abs/2010.02068)

    *Lin, Bo and Ghaddar, Bissan and Nathwani, Jatin.*

3. **A Learning-based Iterative Method for Solving Vehicle Routing Problems** ICLR, 2020. [paper](https://static.aminer.cn/upload/pdf/program/5e5e18dd93d709897ce3720b_0.pdf)

    *Lu, Hao and Zhang, Xingwen and Yang, Shuang*

### [Computing Resource Allocation](#content)

1. **Resource Management with Deep Reinforcement Learning.** HotNets, 2016. [paper](https://dl.acm.org/doi/abs/10.1145/3005745.3005750)

    *Mao, Hongzi and Alizadeh, Mohammad and Menache, Ishai and Kandula, Srikanth.*

2. **Learning to Perform Local Rewriting for Combinatorial Optimization.** NeurIPS, 2019. [paper](https://arxiv.org/abs/1810.00337), [code](https://github.com/facebookresearch/neural-rewriter)

    *Chen, Xinyun and Tian, Yuandong.*

3. **Learning Scheduling Algorithms for Data Processing Clusters** SIGCOMM, 2019. [paper](https://static.aminer.cn/storage/pdf/arxiv/18/1810/1810.01963.pdf), [code](https://github.com/hongzimao/decima-sim)

    *Mao, Hongzi and Schwarzkopf, Malte and Venkatakrishnan, Bojja Shaileshh and Meng, Zili and Alizadeh, Mohammad.*

4. **Smart Resource Allocation for Mobile Edge Computing: A Deep Reinforcement Learning Approach** IEEE Transactions on Emerging Topics in Computing, 2019. [Paper](https://ieeexplore.ieee.org/abstract/document/8657791)

    *Jiadai; Lei Zhao; Jiajia Liu; Nei Kato*

### [Job Shop Scheduling](#content)

1. **Learning to Dispatch for Job Shop Scheduling via Deep Reinforcement Learning.** NeurIPS, 2020. [paper](https://arxiv.org/abs/2010.12367), [code](https://github.com/zcajiayin/L2D)

    *Zhang, Cong and Song, Wen and Cao, Zhiguang and Zhang, Jie and Tan, Puay Siew and Xu, Chi.*

### [Bin Packing Problem](#content)

1. **Small Boxes Big Data: A Deep Learning Approach to Optimize Variable Sized Bin Packing** BigDataService, 2017. [paper](https://ieeexplore.ieee.org/abstract/document/7944923/?casa_token=mRzI_XBy3ycAAAAA:yD9Le2KBNq1TMpW_1etb0RF-oFVcLJj9Up0Z2qI6XJmA-UffxxSZRIx7RklaQED-yXwuwBC4M_w)

    *Mao, Feng and Blanco, Edgar and Fu, Mingang and Jain, Rohit and Gupta, Anurag and Mancel, Sebastien and Yuan, Rong and Guo, Stephen and Kumar, Sai and Tian, Yayang*

2. **Solving a New 3D Bin Packing Problem with Deep Reinforcement Learning Method** Arxiv, 2017. [paper](https://arxiv.org/abs/1708.05930)

    *Hu, Haoyuan and Zhang, Xiaodong and Yan, Xiaowei and Wang, Longfei and Xu, Yinghui*

3. **A Multi-task Selected Learning Approach for Solving 3D Bin Packing Problem.** Arxiv, 2018. [paper](https://arxiv.org/abs/1804.06896)

    *Duan, Lu and Hu, Haoyuan and Qian, Yu and Gong, Yu and Zhang, Xiaodong and Xu, Yinghui and Wei, Jiangwen.*

4. **Ranked Reward: Enabling Self-Play Reinforcement Learning for Combinatorial Optimization Alexandre** Arxiv, 2018. [paper](https://arxiv.org/abs/1807.01672)

    *Laterre, Alexandre and Fu, Yunguan and Jabri, Mohamed Khalil and Cohen, Alain-Sam and Kas, David and Hajjar, Karl and Dahl, Torbjorn S and Kerkeni, Amine and Beguir, Karim*

5. **A Data-Driven Approach for Multi-level Packing Problems in Manufacturing Industry** KDD, 2019. [paper](https://dl.acm.org/doi/abs/10.1145/3292500.3330708)

    *Chen, Lei and Tong, Xialiang and Yuan, Mingxuan and Zeng, Jia and Chen, Lei*

6. **Solving Packing Problems by Conditional Query Learning** OpenReview, 2019. [paper](https://openreview.net/forum?id=BkgTwRNtPB)

    *Li, Dongda and Ren, Changwei and Gu, Zhaoquan and Wang, Yuexuan and Lau, Francis*

7. **RePack: Dense Object Packing Using Deep CNN with Reinforcement Learning** CACS, 2019. [paper](https://ieeexplore.ieee.org/abstract/document/9024360/?casa_token=ScXezdDDiwMAAAAA:fglP_vbiQUJgLZcM7YZyqnDh_qA8jOjIh-zbH7ru0XSVBghh8OAxpThOU3BqhBeet4NlSrdHPcU)

    *Chu, Yu-Cheng and Lin, Horng-Horng*

8. **Online 3D Bin Packing with Constrained Deep Reinforcement Learning.** Arxiv, 2020. [paper](https://arxiv.org/abs/2006.14978)

    *Zhao, Hang and She, Qijin and Zhu, Chenyang and Yang, Yin and Xu, Kai.*

9. **A Generalized Reinforcement Learning Algorithm for Online 3D Bin-Packing.** Arxiv, 2020. [paper](https://arxiv.org/abs/2007.00463)

    *Verma, Richa and Singhal, Aniruddha and Khadilkar, Harshad and Basumatary, Ansuma and Nayak, Siddharth and Singh, Harsh Vardhan and Kumar, Swagat and Sinha, Rajesh.*

10. **Robot Packing with Known Items and Nondeterministic Arrival Order.** TASAE, 2020. [paper](https://ieeexplore.ieee.org/abstract/document/9205914/)

    *Wang, Fan and Hauser, Kris.*

11. **TAP-Net: Transport-and-Pack using Reinforcement Learning.** TOG, 2020. [paper](https://dl.acm.org/doi/abs/10.1145/3414685.3417796), [code](https://github.com/Juzhan/TAP-Net)

    *Hu, Ruizhen and Xu, Juzhan and Chen, Bin and Gong, Minglun and Zhang, Hao and Huang, Hui.*

12. **Simultaneous Planning for Item Picking and Placing by Deep Reinforcement Learning** IROS, 2020. [paper](http://ras.papercept.net/images/temp/IROS/files/0330.pdf)

    *Tanaka, Tatsuya and Kaneko, Toshimitsu and Sekine, Masahiro and Tangkaratt, Voot and Sugiyama, Masashi*

13. **Monte Carlo Tree Search on Perfect Rectangle Packing Problem Instances** GECCO, 2020. [paper](https://dl.acm.org/doi/abs/10.1145/3377929.3398115)

    *Pejic, Igor and van den Berg, Daan*

14. **PackIt: A Virtual Environment for Geometric Planning** ICML, 2020. [paper](http://proceedings.mlr.press/v119/goyal20b.html)

    *Goyal, Ankit and Deng, Jia*

### [Graph Edit Distance](#content)

1. **SimGNN - A Neural Network Approach to Fast Graph Similarity Computation** WSDM, 2019. [paper](https://arxiv.org/abs/1808.05689), [code](https://github.com/yunshengb/SimGNN)

    *Bai, Yunsheng and Ding, Hao and Bian, Song and Chen, Ting and Sun, Yizhou and Wang, Wei*

2. **Graph Matching Networks for Learning the Similarity of Graph Structured Objects** ICML, 2019. [paper](https://arxiv.org/abs/1904.12787)

    *Li, Yujia and Gu, Chenjie and Dullien, Thomas and Vinyals, Oriol and Kohli, Pushmeet*

3. **✨Combinatorial Learning of Graph Edit Distance via Dynamic Embedding.** CVPR, 2021. [paper](https://arxiv.org/abs/2011.15039)

    *Wang, Runzhong and Zhang, Tianqi and Yu, Tianshu and Yan, Junchi and Yang, Xiaokang.*

### [Graph Coloring](#content)

1. **Deep Learning-based Hybrid Graph-Coloring Algorithm for Register Allocation.** Arxiv, 2019. [paper](https://arxiv.org/abs/1912.03700)

    *Das, Dibyendu and Ahmad, Shahid Asghar and Venkataramanan, Kumar.*

### [Maximal Common Subgraph](#content)

1. **Fast Detection of Maximum Common Subgraph via Deep Q-Learning.** Arxiv, 2020. [paper](https://arxiv.org/abs/2002.03129)

    *Bai, Yunsheng and Xu, Derek and Wang, Alex and Gu, Ken and Wu, Xueqing and Marinovic, Agustin and Ro, Christopher and Sun, Yizhou and Wang, Wei.*

### [Influence Maximization](#content)

1. **Learning Heuristics over Large Graphs via Deep Reinforcement Learning.** NeurIPS, 2020. [paper](https://arxiv.org/abs/1903.03332)

    *Mittal, Akash and Dhawan, Anuj and Manchanda, Sahil and Medya, Sourav and Ranu, Sayan and Singh, Ambuj.*

### [Maximal Independent Set](#content)

1. **Combinatorial Optimization with Graph Convolutional Networks and Guided Tree Search.** NeurIPS, 2018. [paper](https://arxiv.org/abs/1810.10659)

    *Li, Zhuwen and Chen, Qifeng and Koltun, Vladlen.*

### [Mixed Integer Programming](#content)

1. **Improving Learning to Branch via Reinforcement Learning.** NeurIPS Workshop, 2020. [paper](https://openreview.net/forum?id=z4D7-PTxTb)

    *Sun, Haoran and Chen, Wenbo and Li, Hui and Song, Le.*

### [Causal Discovery](#content)

1. **Causal Discovery with Reinforcement Learning.** ICLR, 2020. [paper](https://arxiv.org/abs/1906.04477)

    *Zhu, Shengyu and Ng, Ignavier and Chen, Zhitang.*

### [Game Theoretic Semantics](#content)

1. **First-Order Problem Solving through Neural MCTS based Reinforcement Learning.** Arxiv, 2021. [paper](https://arxiv.org/abs/2101.04167)

    *Xu, Ruiyang and Kadam, Prashank and Lieberherr, Karl.*

### [Boolean Satisfiability](#content)

1. **Graph neural networks and boolean satisfiability.** Arxiv, 2017. [paper](https://arxiv.org/pdf/1702.03592)

    *Bünz, Benedikt, and Matthew Lamm.*

2. **Learning a SAT solver from single-bit supervision.** Arxiv, 2018. [paper](https://arxiv.org/pdf/1903.04671), [code](https://github.com/dselsam/neurosat)

    *Selsam, Daniel, Matthew Lamm, Benedikt Bünz, Percy Liang, Leonardo de Moura, and David L. Dill.*

3. **Machine learning-based restart policy for CDCL SAT solvers.** SAT, 2018. [paper](http://www.t-news.cn/Floc2018/FLoC2018-pages/proceedings_paper_477.pdf)

    *Liang, Jia Hui, Chanseok Oh, Minu Mathew, Ciza Thomas, Chunxiao Li, and Vijay Ganesh.*

4. **Learning to solve circuit-SAT: An unsupervised differentiable approach** ICLR, 2019. [paper](https://openreview.net/pdf?id=BJxgz2R9t7), [code](https://github.com/lee-man/circuit-sat)

    *Amizadeh, Saeed, Sergiy Matusevych, and Markus Weimer.*

5. **Learning Local Search Heuristics for Boolean Satisfiability.** NeurIPS, 2019. [paper](https://www.cs.cmu.edu/~eyolcu/papers/learning-local-search-heuristics-sat.pdf), [code](https://github.com/emreyolcu/sat)

    *Yolcu, Emre and Poczos, Barnabas*

6. **Improving SAT solver heuristics with graph networks and reinforcement learning.** Arxiv, 2019. [paper](https://arxiv.org/pdf/1909.11830)

    *Kurin, Vitaly, Saad Godil, Shimon Whiteson, and Bryan Catanzaro.*

7. **Graph neural reasoning may fail in certifying boolean unsatisfiability** Arxiv, 2019. [paper](https://arxiv.org/pdf/1909.11588)

    *Chen, Ziliang, and Zhanfu Yang.*

8. **Guiding high-performance SAT solvers with unsat-core predictions** SAT, 2019. [paper](https://arxiv.org/pdf/1903.04671)

    *Selsam, Daniel, and Nikolaj Bjørner.*

9. **G2SAT: Learning to Generate SAT Formulas** NeurIPS, 2019. [paper](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7138247/), [code](https://github.com/JiaxuanYou/G2SAT)

    *You, Jiaxuan, Haoze Wu, Clark Barrett, Raghuram Ramanujan, and Jure Leskovec.*

10. **Learning Heuristics for Quantified Boolean Formulas through Reinforcement Learning** Arxiv, 2019. [paper](https://arxiv.org/pdf/1807.08058), [code](https://github.com/lederg/learningqbf)

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

18. **NLocalSAT: Boosting Local Search with Solution Prediction** Arxiv, 2020. [paper](https://arxiv.org/pdf/2001.09398), [code](https://github.com/myxxxsquared/NLocalSAT)

    *Zhang, Wenjie, Zeyu Sun, Qihao Zhu, Ge Li, Shaowei Cai, Yingfei Xiong, and Lu Zhang.*

### [Differentiable Optimization](#content)

1. **Differentiable Learning of Submodular Models** NeurIPS, 2017. [paper](https://papers.NeurIPS.cc/paper/2017/hash/192fc044e74dffea144f9ac5dc9f3395-Abstract.html), [code](https://github.com/josipd/torch-submod)

    *Josip Djolonga, Andreas Krause*

2. **Melding the Data-Decisions Pipeline: Decision-Focused Learning for Combinatorial Optimization** AAAI, 2019. [paper](https://ojs.aaai.org//index.php/AAAI/article/view/3982)

    *Bryan Wilder, Bistra Dilkina, Milind Tambe*

3. **MIPaaL: Mixed Integer Program as a Layer** AAAI, 2020. [paper](https://ojs.aaai.org//index.php/AAAI/article/view/5509), [code](https://github.com/amf272/MIPaaL/)

    *Aaron Ferber, Bryan Wilder, Bistra Dilkina, Milind Tambe*

4. **Smart Predict-and-Optimize for Hard Combinatorial Optimization Problems** AAAI, 2020. [paper](https://arxiv.org/abs/1911.10092), [code](https://github.com/JayMan91/aaai_predit_then_optimize)

    *Jaynta Mandi, Emir Demirovi, Peter. J Stuckey, Tias Guns*

5. **Differentiation of blackbox combinatorial solvers** ICLR, 2020. [paper](https://openreview.net/forum?id=BkevoJSYPB), [code](https://github.com/martius-lab/blackbox-backprop)

    *Marin Vlastelica Pogani, Anselm Paulus, Vit Musil, Georg Martius, Michal Rolinek*

6. **Interior Point Solving for LP-based prediction+optimization** NeurIPS, 2020. [paper](https://proceedings.neurips.cc//paper/2020/hash/51311013e51adebc3c34d2cc591fefee-Abstract.html), [code](https://github.com/JayMan91/NeurIPSIntopt)

    *Jayanta Mandi, Tias Guns*

### [Car Dispatch](#content)

1. **Dispatch of autonomous vehicles for taxi services: A deep reinforcement learning approach** Transportation Research, 2020. [paper](https://www.sciencedirect.com/science/article/pii/S0968090X19312227)

    *ChaoMao, Yulin Liu, Zuo-Jun (Max) Shen*

