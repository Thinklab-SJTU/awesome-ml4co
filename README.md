

# Awesome Machine Learning for Combinatorial Optimization Resources
We would like to maintain a list of resources that utilize machine learning technologies to solve combinatorial optimization problems. 

We mark work contributed by [Thinklab](http://thinklab.sjtu.edu.cn) with ✨.

*Maintained by members in SJTU-Thinklab: Chang Liu, Runzhong Wang, Jiayi Zhang, Zelin Zhao, Haoyu Geng, Tianzhe Wang, Wenxuan Guo, Wenjie Wu and Junchi Yan.*

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
	<td>&emsp;<a href=#vehicle-routing-problem>2.5 Vehicle Routing Problem (VRP)</a></td>
	<td>&emsp;<a href=#job-shop-scheduling-problem>2.6 Job Shop Scheduling Problem (JSSP)</a></td>
</tr>
<tr>
	<td>&emsp;<a href=#computing-resource-allocation>2.7 Computing Resource Allocation</a></td>
	<td>&emsp;<a href=#bin-packing-problem>2.8 Bin Packing Problem (BPP)</a></td>
</tr>
<tr>
	<td>&emsp;<a href=#graph-edit-distance>2.9 Graph Edit Distance (GED)</a></td>
	<td>&emsp;<a href=#hamiltonian-cycle-problem>2.10 Hamiltonian Cycle Problem (HCP)</a></td>
</tr>
<tr>
	<td>&emsp;<a href=#graph-coloring>2.11 Graph Coloring</a></td>
	<td>&emsp;<a href=#maximal-common-subgraph>2.12 Maximal Common Subgraph (MCS)</a></td>
</tr>
<tr>
	<td>&emsp;<a href=#influence-maximization>2.13 Influence Maximization</a></td>
	<td>&emsp;<a href=#maximal/maximum-independent-set>2.14 Maximal/Maximum Independent Set</a></td>
</tr>
<tr>
	<td>&emsp;<a href=#mixed-integer-programming>2.15 Mixed Integer Programming</a></td>
	<td>&emsp;<a href=#causal-discovery>2.16 Causal Discovery</a></td>
</tr>
<tr>
	<td>&emsp;<a href=#game-theoretic-semantics>2.17 Game Theoretic Semantics</a></td>
	<td>&emsp;<a href=#boolean-satisfiability>2.18 Boolean Satisfiability (SAT)</a></td>
</tr>
<tr>
	<td>&emsp;<a href=#differentiable-optimization>2.19 Differentiable Optimization</a></td>
	<td>&emsp;<a href=#car-dispatch>2.20 Car Dispatch</a></td>
</tr>
<tr>
	<td>&emsp;<a href=#electronic-design-automation>2.21 Electronic Design Automation (EDA)</a></td>
	<td>&emsp;<a href=#generalization>2.22 Generalization</a></td>
</tr>
<tr>
	<td>&emsp;<a href=#conjunctive-query-containment>2.23 Conjunctive Query Containment</a></td>
	<td>&emsp;<a href=#orienteering-problem>2.24 Orienteering Problem (OP)</a></td>
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

6. **A Review of combinatorial optimization with graph neural networks.** BigDIA, 2019. [paper](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8802843)

    *Huang, Tingfei and Ma, Yang and Zhou, Yuzhen and Huang, Honglan Huang and Chen, Dongmei and Gong, Zidan and Liu, Yao.*

7. **Machine Learning for Combinatorial Optimization: a Methodological Tour d'horizon.** EJOR, 2020. [journal](https://arxiv.org/abs/1811.06128)

    *Bengio, Yoshua and Lodi, Andrea and Prouvost, Antoine.*

8. **Reinforcement Learning for Combinatorial Optimization: A Survey.** Arxiv, 2020. [paper](https://arxiv.org/abs/2003.03600)

    *Mazyavkina, Nina and Sviridov, Sergey and Ivanov, Sergei and Burnaev, Evgeny.*

9. **✨Learning Graph Matching and Related Combinatorial Optimization Problems.** IJCAI, 2020. [paper](https://www.ijcai.org/proceedings/2020/0694.pdf)

    *Yan, Junchi and Yang, Shuang, and Hancock, Edwin R.*

10. **Learning Combinatorial Optimization on Graphs: A Survey with Applications to Networking.** IEEE ACCESS, 2020. [journal](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9125934)

    *Vesselinova, Natalia and Steinert, Rebecca and Perez-Ramirez, Daniel F. and Boman, Magnus.*

11. **From Shallow to Deep Interactions Between Knowledge Representation, Reasoning and Machine Learning.** Arxiv, 2020. [paper](https://arxiv.org/abs/1912.06612)

    *Bouraoui, Zied and Cornuéjols, Antoine and Denœux, Thierry and Destercke, Sébastien and Dubois, Didier and Guillaume, Romain and Marques-Silva, João and Mengin, Jérôme and Prade, Henri and Schockaert, Steven and Serrurier, Mathieu and Vrain, Christel.*

12. **A Survey on Reinforcement Learning for Combinatorial Optimization.** Arxiv, 2020. [paper](https://arxiv.org/abs/2008.12248v2)

    *Yang, Yunhao and Whinston, Andrew.*

13. **Research Reviews of Combinatorial Optimization Methods Based on Deep Reinforcement Learning. (in chinese)** 自动化学报, 2020. [journal](http://www.aas.net.cn/article/doi/10.16383/j.aas.c200551)

    *Li, Kai-Wen and Zhang,  Tao and Wang, Rui and Qin, Wei-Jian and He, Hui-Hui and Huang, Hong.*

14. **Graph Learning for Combinatorial Optimization: A Survey of State-of-the-Art.** Data Science and Engineering, 2021. [journal](https://link.springer.com/article/10.1007/s41019-021-00155-3)

    *Peng, Yue, Choi, Byron, and Xu, Jianliang.*

15. **Combinatorial Optimization and Reasoning with Graph Neural Networks** Arxiv, 2021. [paper](https://arxiv.org/abs/2102.09544)

    *Cappart, Quentin and Chetelat, Didier and Khalil, Elias and Lodi, Andrea and Morris, Christopher and Velickovic, Petar*

16. **Machine Learning for Electronic Design Automation (EDA) : A Survey** TODAES, 2021. [journal](https://arxiv.org/abs/2102.03357)

    *Huang, Guyue and Hu, Jingbo and He, Yifan and Liu, Jialong and Ma, Mingyuan and Shen, Zhaoyang and Wu, Juejian and Xu, Yuanfan and Zhang, Hengrui and Zhong, Kai and others*

## [Problems](#content)

### [Graph Matching](#content)

1. **Revised Note on Learning Algorithms for Quadratic Assignment with Graph Neural Networks** Arxiv, 2017. [paper](https://arxiv.org/pdf/1706.07450.pdf), [code](https://github.com/alexnowakvila/QAP_pt)

    *Nowak, Alex and Villar, Soledad and Bandeira, S. Afonso and Bruna, Joan*

2. **Deep Learning of Graph Matching.** CVPR, 2018. [paper](https://openaccess.thecvf.com/content_cvpr_2018/html/Zanfir_Deep_Learning_of_CVPR_2018_paper.html)

    *Zanfir, Andrei and Sminchisescu, Cristian*

3. **✨Learning Combinatorial Embedding Networks for Deep Graph Matching.** ICCV, 2019. [paper](http://openaccess.thecvf.com/content_ICCV_2019/papers/Wang_Learning_Combinatorial_Embedding_Networks_for_Deep_Graph_Matching_ICCV_2019_paper.pdf), [code](https://github.com/Thinklab-SJTU/ThinkMatch)

    *Wang, Runzhong and Yan, Junchi and Yang, Xiaokang*

4. **Deep Graphical Feature Learning for the Feature Matching Problem.** ICCV, 2019. [paper](https://openaccess.thecvf.com/content_ICCV_2019/papers/Zhang_Deep_Graphical_Feature_Learning_for_the_Feature_Matching_Problem_ICCV_2019_paper.pdf)

    *Zhang, Zhen and Lee, Wee Sun*

5. **GLMNet: Graph Learning-Matching Networks for Feature Matching.** Arxiv, 2019. [paper](https://arxiv.org/abs/1911.07681)

    *Jiang, Bo and Sun, Pengfei and Tang, Jin and Luo, Bin*

6. **✨Learning deep graph matching with channel-independent embedding and Hungarian attention.** ICLR, 2020. [paper](https://openreview.net/forum?id=rJgBd2NYPH), [code](https://github.com/Thinklab-SJTU/ThinkMatch)

    *Yu, Tianshu and Wang, Runzhong and Yan, Junchi and Li, Baoxin*

7. **Deep Graph Matching Consensus.** ICLR, 2020. [paper](http://arxiv.org/abs/2001.09621)

    *Fey, Matthias and Lenssen, Jan E. and Morris, Christopher and Masci, Jonathan and Kriege, Nils M.*

8. **✨Graduated Assignment for Joint Multi-Graph Matching and Clustering with Application to Unsupervised Graph Matching Network Learning.** NeurIPS, 2020. [paper](https://papers.NeurIPS.cc/paper/2020/file/e6384711491713d29bc63fc5eeb5ba4f-Paper.pdf), [code](https://github.com/Thinklab-SJTU/ThinkMatch)

    *Wang, Runzhong and Yan, Junchi and Yang, Xiaokang*

9. **✨Combinatorial Learning of Robust Deep Graph Matching: An Embedding Based Approach.** TPAMI, 2020. [paper](https://doi.org/10.1109/TPAMI.2020.3005590), [code](https://github.com/Thinklab-SJTU/ThinkMatch)

    *Wang, Runzhong and Yan, Junchi and Yang, Xiaokang*

10. **Deep Graph Matching via Blackbox Differentiation of Combinatorial Solvers.** ECCV, 2020. [paper](https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123730409.pdf), [code](https://github.com/martius-lab/blackbox-deep-graph-matching)

    *Rolinek, Michal and Swoboda, Paul and Zietlow, Dominik and Paulus, Anselm and Musil, Vit and Martius, Georg*

11. **✨Revocable Deep Reinforcement Learning with Affinity Regularization for Outlier-Robust Graph Matching.** Arxiv, 2020. [paper](https://arxiv.org/abs/2012.08950)

    *Liu, Chang and Jiang, Zetian and Wang, Runzhong and Yan, Junchi and Huang, Lingxiao and Lu, Pinyan*

12. **✨Neural Graph Matching Network: Learning Lawler's Quadratic Assignment Problem with Extension to Hypergraph and Multiple-graph Matching.** TPAMI, 2021. [paper](https://arxiv.org/abs/1911.11308), [code](https://github.com/Thinklab-SJTU/ThinkMatch)

    *Wang, Runzhong and Yan, Junchi and Yang, Xiaokang*

13. **✨Deep Latent Graph Matching** ICML, 2021. [paper](http://proceedings.mlr.press/v139/yu21d/yu21d.pdf)

    *Yu, Tianshu and Wang, Runzhong and Yan, Junchi and Li, Baoxin.*

### [Quadratic Assignment Problem](#content)

1. **Revised Note on Learning Algorithms for Quadratic Assignment with Graph Neural Networks** Arxiv, 2017. [paper](https://arxiv.org/pdf/1706.07450.pdf), [code](https://github.com/alexnowakvila/QAP_pt)

    *Nowak, Alex and Villar, Soledad and Bandeira, S. Afonso and Bruna, Joan*

2. **✨Revocable Deep Reinforcement Learning with Affinity Regularization for Outlier-Robust Graph Matching.** Arxiv, 2020. [paper](https://arxiv.org/abs/2012.08950)

    *Liu, Chang and Jiang, Zetian and Wang, Runzhong and Yan, Junchi and Huang, Lingxiao and Lu, Pinyan*

3. **✨Neural Graph Matching Network: Learning Lawler's Quadratic Assignment Problem with Extension to Hypergraph and Multiple-graph Matching.** TPAMI, 2021. [paper](https://arxiv.org/abs/1911.11308), [code](https://github.com/Thinklab-SJTU/ThinkMatch)

    *Wang, Runzhong and Yan, Junchi and Yang, Xiaokang*

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

8. **Differentiation of Blackbox Combinatorial Solvers** ICLR, 2020. [paper](https://arxiv.org/pdf/1912.02175v2.pdf), [code](https://github.com/martius-lab/blackbox-backprop)

    *Marin Vlastelica, Anselm Paulus, Vít Musil, Georg Martius, Michal Rolínek*

9. **A Reinforcement Learning Approach for Optimizing Multiple Traveling Salesman Problems over Graphs** KBS, 2020. [journal](https://www.sciencedirect.com/science/article/pii/S0950705120304445)

    *Hu, Yujiao and Yao, Yuan and Lee, Wee Sun*

10. **Learning 2-opt Heuristics for the Traveling Salesman Problem via Deep Reinforcement Learning** ACML, 2020. [paper](http://proceedings.mlr.press/v129/costa20a), [code](https://github.com/paulorocosta/learning-2opt-drl)

    *d O Costa, Paulo R and Rhuggenaath, Jason and Zhang, Yingqian and Akcay, Alp*

11. **Deep Reinforcement Learning for Combinatorial Optimization: Covering Salesman Problems.** IEEE Trans Cybern, 2021. [journal](https://arxiv.org/abs/2102.05875)

    *Kaiwen Li, Tao Zhang, Rui Wang Yuheng Wang, and Yi Han*

12. **The Transformer Network for the Traveling Salesman Problem** IPAM, 2021. [paper](http://helper.ipam.ucla.edu/publications/dlc2021/dlc2021_16703.pdf)

    *Xavier Bresson，Thomas Laurent*

13. **Learning Improvement Heuristics for Solving Routing Problems** TNNLS, 2021. [journal](https://ieeexplore.ieee.org/abstract/document/9393606?casa_token=mFeyLmrOGfIAAAAA:nmAkjUaTSooYurWHuWGYNoguV453anw9Enyv45xG5jb2oCps6QE4A1CFe1EmFmTzbON6cL5maw)

    *Wu, Yaoxin and Song, Wen and Cao, Zhiguang and Zhang, Jie and Lim, Andrew*

14. **Reversible Action Design for Combinatorial Optimization with Reinforcement Learning** Arxiv, 2021. [paper](https://arxiv.org/abs/2102.07210)

    *Yao, Fan and Cai, Renqin and Wang, Hongning*

15. **Solving Dynamic Traveling Salesman Problems with Deep Reinforcement Learning.** TNNLS, 2021. [journal](https://ieeexplore.ieee.org/document/9537638)

    *Zizhen Zhang, Hong Liu, Meng Chu Zhou, Jiahai Wang*

16. **ScheduleNet: Learn to Solve Multi-agent Scheduling Problems with Reinforcement Learning** Arxiv, 2021. [paper](https://arxiv.org/abs/2106.03051)

    *Junyoung Park, Sanjar Bakhtiyar, Jinkyoo Park*

17. **DAN: Decentralized Attention-based Neural Network to Solve the MinMax Multiple Traveling Salesman Problem** Arxiv, 2021. [paper](https://arxiv.org/abs/2109.04205)

    *Cao, Yuhong and Sun, Zhanhong and Sartoretti, Guillaume*

18. **Reinforcement Learning for Route Optimization with Robustness Guarantees** IJCAI, 2021. [paper](https://www.ijcai.org/proceedings/2021/0357.pdf)

    *Jacobs, Tobias and Alesiani, Francesco and Ermis, Gulcin*

19. **Learning TSP Requires Rethinking Generalization** CP, 2021. [paper](https://arxiv.org/pdf/2006.07054.pdf), [code](https://github.com/chaitjo/learning-tsp)

    *Chaitanya K. Joshi, Quentin Cappart, Louis-Martin Rousseau and Thomas Laurent*

20. **Generalization of Neural Combinatorial Solvers Through the Lens of Adversarial Robustness** Arxiv, 2021. [paper](https://arxiv.org/pdf/2110.10942.pdf)

    *Simon Geisler, Johanna Sommer, Jan Schuchardt, Aleksandar Bojchevski and Stephan Günnemann*

21. **The First AI4TSP Competition: Learning to Solve Stochastic Routing Problems** Arxiv, 2022. [paper](https://arxiv.org/abs/2201.10453), [code](https://github.com/paulorocosta/ai-for-tsp-competition)

    *Bliek, Laurens and da Costa, Paulo and Afshar, Reza Refaei and Zhang, Yingqian and Catshoek, Tom and Vos, Daniel and Verwer, Sicco and Schmitt-Ulms, Fynn and Hottung, Andre and Shah, Tapan and others*

### [Maximal Cut](#content)

1. **Learning Combinatorial Optimization Algorithms over Graphs.** NeurIPS, 2017. [paper](https://arxiv.org/abs/1704.01665)

    *Dai, Hanjun and Khalil, Elias B and Zhang, Yuyu and Dilkina, Bistra and Song, Le*

2. **Exploratory Combinatorial Optimization with Reinforcement Learning.** AAAI, 2020. [paper](https://ojs.aaai.org/index.php/AAAI/article/view/5723)

    *LBarrett, Thomas and Clements, William and Foerster, Jakob and Lvovsky, Alex.*

3. **Erdos Goes Neural: an Unsupervised Learning Framework for Combinatorial Optimization on Graphs.** NeurIPS, 2020. [paper](https://static.aminer.cn/upload/pdf/575/1127/1864/5eede0b791e0116a23aafe7b_1.pdf)

    *Karalias, Nikolaos and Loukas, Andreas*

4. **Reversible Action Design for Combinatorial Optimization with Reinforcement Learning** Arxiv, 2021. [paper](https://arxiv.org/abs/2102.07210)

    *Yao, Fan and Cai, Renqin and Wang, Hongning*

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

### [Job Shop Scheduling Problem](#content)

1. **Deep Reinforcement Learning as a Job Shop Scheduling Solver: A Literature Review** Hybrid Intelligent Systems, 2018. [journal](http://link.springer.com/10.1007/978-3-030-14347-3_34)

    *Bruno Cunha, Ana M. Madureira, Benjamim Fonseca, Duarte Coelho*

2. **Smart Manufacturing Scheduling With Edge Computing Using Multiclass Deep Q Network** Transactions on Industrial Informatics, 2019. [journal](https://ieeexplore.ieee.org/document/8676376)

    *Chun-Cheng Lin, Der-Jiunn Deng, Yen-Ling Chih, Hsin-Ting Chiu*

3. **Multi-Agent Reinforcement Learning for Job Shop Scheduling in Flexible Manufacturing Systems** International Conference on Artificial Intelligence for Industries (AI4I), 2019. [paper](https://ieeexplore.ieee.org/document/9027776)

    *Schirin Baer, Jupiter Bakakeu, Richard Meyes, Tobias Meisen*

4. **Learning to Dispatch for Job Shop Scheduling via Deep Reinforcement Learning.** NeurIPS, 2020. [paper](https://arxiv.org/abs/2010.12367), [code](https://github.com/zcajiayin/L2D)

    *Zhang, Cong and Song, Wen and Cao, Zhiguang and Zhang, Jie and Tan, Puay Siew and Xu, Chi.*

5. **ScheduleNet: Learn to Solve Multi-agent Scheduling Problems with Reinforcement Learning** Arxiv, 2021. [paper](https://arxiv.org/abs/2106.03051)

    *Junyoung Park, Sanjar Bakhtiyar, Jinkyoo Park*

6. **Dynamic job-shop scheduling in smart manufacturing using deep reinforcement learning** Computer Networks, 2021. [journal](https://www.sciencedirect.com/science/article/pii/S1389128621001031)

    *Libing Wang, Xin Hu, Yin Wang, Sujie Xu, Shijun Ma, Kexin Yang, Zhijun Liu, Weidong Wang*

7. **Learning to schedule job-shop problems: Representation and policy learning using graph neural network and reinforcement learning.** International Journal of Production Research, 2021. [journal](https://arxiv.org/abs/2106.01086)

    *Junyoung Park, Jaehyeong Chun, Sang Hun Kim, Youngkook Kim, Jinkyoo Park*

8. **Explainable reinforcement learning in production control of job shop manufacturing system.** International Journal of Production Research, 2021. [journal](https://www.tandfonline.com/doi/abs/10.1080/00207543.2021.1972179?journalCode=tprs20)

    *Andreas Kuhnle,Marvin Carl May,Louis Sch?fer & Gisela Lanza*

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

6. **✨A Bi-Level Framework for Learning to Solve Combinatorial Optimization on Graphs** NeurIPS, 2021. [paper](https://arxiv.org/abs/2106.04927), [code](https://github.com/Thinklab-SJTU/PPO-BiHyb)

    *Wang, Runzhong and Hua, Zhigang and Liu, Gan and Zhang, Jiayi and Yan, Junchi and Qi, Feng and Yang, Shuang and Zhou, Jun and Yang, Xiaokang*

### [Bin Packing Problem](#content)

1. **Small Boxes Big Data: A Deep Learning Approach to Optimize Variable Sized Bin Packing** BigDataService, 2017. [paper](https://ieeexplore.ieee.org/abstract/document/7944923/?casa_token=mRzI_XBy3ycAAAAA:yD9Le2KBNq1TMpW_1etb0RF-oFVcLJj9Up0Z2qI6XJmA-UffxxSZRIx7RklaQED-yXwuwBC4M_w)

    *Mao, Feng and Blanco, Edgar and Fu, Mingang and Jain, Rohit and Gupta, Anurag and Mancel, Sebastien and Yuan, Rong and Guo, Stephen and Kumar, Sai and Tian, Yayang*

2. **Solving a New 3D Bin Packing Problem with Deep Reinforcement Learning Method** Arxiv, 2017. [paper](https://arxiv.org/abs/1708.05930)

    *Hu, Haoyuan and Zhang, Xiaodong and Yan, Xiaowei and Wang, Longfei and Xu, Yinghui*

3. **Ranked Reward: Enabling Self-Play Reinforcement Learning for Combinatorial Optimization Alexandre** Arxiv, 2018. [paper](https://arxiv.org/abs/1807.01672)

    *Laterre, Alexandre and Fu, Yunguan and Jabri, Mohamed Khalil and Cohen, Alain-Sam and Kas, David and Hajjar, Karl and Dahl, Torbjorn S and Kerkeni, Amine and Beguir, Karim*

4. **A Multi-task Selected Learning Approach for Solving 3D Bin Packing Problem.** AAMAS, 2019. [paper](https://arxiv.org/abs/1804.06896)

    *Duan, Lu and Hu, Haoyuan and Qian, Yu and Gong, Yu and Zhang, Xiaodong and Xu, Yinghui and Wei, Jiangwen.*

5. **A Data-Driven Approach for Multi-level Packing Problems in Manufacturing Industry** KDD, 2019. [paper](https://dl.acm.org/doi/abs/10.1145/3292500.3330708)

    *Chen, Lei and Tong, Xialiang and Yuan, Mingxuan and Zeng, Jia and Chen, Lei*

6. **Solving Packing Problems by Conditional Query Learning** OpenReview, 2019. [paper](https://openreview.net/forum?id=BkgTwRNtPB)

    *Li, Dongda and Ren, Changwei and Gu, Zhaoquan and Wang, Yuexuan and Lau, Francis*

7. **RePack: Dense Object Packing Using Deep CNN with Reinforcement Learning** CACS, 2019. [paper](https://ieeexplore.ieee.org/abstract/document/9024360/?casa_token=ScXezdDDiwMAAAAA:fglP_vbiQUJgLZcM7YZyqnDh_qA8jOjIh-zbH7ru0XSVBghh8OAxpThOU3BqhBeet4NlSrdHPcU)

    *Chu, Yu-Cheng and Lin, Horng-Horng*

8. **Reinforcement learning driven heuristic optimization** Arxiv, 2019. [paper](https://arxiv.org/pdf/1906.06639.pdf)

    *Cai, Qingpeng and Hang, Will and Mirhoseini, Azalia and Tucker, George and Wang, Jingtao and Wei, Wei*

9. **A Generalized Reinforcement Learning Algorithm for Online 3D Bin-Packing.** AAAI Workshop, 2020. [paper](https://arxiv.org/abs/2007.00463)

    *Verma, Richa and Singhal, Aniruddha and Khadilkar, Harshad and Basumatary, Ansuma and Nayak, Siddharth and Singh, Harsh Vardhan and Kumar, Swagat and Sinha, Rajesh.*

10. **Robot Packing with Known Items and Nondeterministic Arrival Order.** TASAE, 2020. [paper](https://ieeexplore.ieee.org/abstract/document/9205914/)

    *Wang, Fan and Hauser, Kris.*

11. **TAP-Net: Transport-and-Pack using Reinforcement Learning.** TOG, 2020. [paper](https://dl.acm.org/doi/abs/10.1145/3414685.3417796), [code](https://github.com/Juzhan/TAP-Net)

    *Hu, Ruizhen and Xu, Juzhan and Chen, Bin and Gong, Minglun and Zhang, Hao and Huang, Hui.*

12. **Simultaneous Planning for Item Picking and Placing by Deep Reinforcement Learning** IROS, 2020. [paper](http://ras.papercept.net/images/temp/IROS/files/0330.pdf)

    *Tanaka, Tatsuya and Kaneko, Toshimitsu and Sekine, Masahiro and Tangkaratt, Voot and Sugiyama, Masashi*

13. **Monte Carlo Tree Search on Perfect Rectangle Packing Problem Instances** GECCO, 2020. [paper](https://dl.acm.org/doi/abs/10.1145/3377929.3398115)

    *Pejic, Igor and van den Berg, Daan*

14. **PackIt: A Virtual Environment for Geometric Planning** ICML, 2020. [paper](http://proceedings.mlr.press/v119/goyal20b.html), [code](https://github.com/princeton-vl/PackIt)

    *Goyal, Ankit and Deng, Jia*

15. **Online 3D Bin Packing with Constrained Deep Reinforcement Learning.** AAAI, 2021. [paper](https://arxiv.org/abs/2006.14978), [code](https://github.com/alexfrom0815/Online-3D-BPP-DRL)

    *Zhao, Hang and She, Qijin and Zhu, Chenyang and Yang, Yin and Xu, Kai.*

16. **Learning Practically Feasible Policies for Online 3D Bin Packing** Arxiv, 2021. [paper](https://arxiv.org/abs/2108.13680)

    *Hang Zhao and Chenyang Zhu and Xin Xu and Hui Huang and Kai Xu*

17. **Attend2Pack: Bin Packing through Deep Reinforcement Learning with Attention** ICML Workshop, 2021. [paper](https://arxiv.org/abs/2107.04333)

    *Jingwei Zhang and Bin Zi and Xiaoyu Ge*

18. **Solving 3D bin packing problem via multimodal deep reinforcement learning** AAMAS, 2021. [paper](https://www.ifaamas.org/Proceedings/aamas2021/pdfs/p1548.pdf)

    *Jiang, Yuan, Zhiguang Cao, and Jie Zhang*

19. **Learning to Solve 3-D Bin Packing Problem via Deep Reinforcement Learning and Constraint Programming** IEEE transactions on cybernetics, 2021. [paper](https://ieeexplore.ieee.org/document/9606618/)

    *Jiang, Yuan and Cao, Zhiguang and Zhang, Jie*

20. **Learning to Pack: A Data-Driven Tree Search Algorithm for Large-Scale 3D Bin Packing Problem** CIKM, 2021. [paper](https://dl.acm.org/doi/abs/10.1145/3459637.3481933)

    *Zhu, Qianwen and Li, Xihan and Zhang, Zihan and Luo, Zhixing and Tong, Xialiang and Yuan, Mingxuan and Zeng, Jia*

21. **Learning Efficient Online 3D Bin Packing on Packing Configuration Trees** ICLR, 2022. [paper](https://openreview.net/forum?id=bfuGjlCwAq)

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

5. **✨A Bi-Level Framework for Learning to Solve Combinatorial Optimization on Graphs** NeurIPS, 2021. [paper](https://arxiv.org/abs/2106.04927), [code](https://github.com/Thinklab-SJTU/PPO-BiHyb)

    *Wang, Runzhong and Hua, Zhigang and Liu, Gan and Zhang, Jiayi and Yan, Junchi and Qi, Feng and Yang, Shuang and Zhou, Jun and Yang, Xiaokang*

6. **✨Combinatorial Learning of Graph Edit Distance via Dynamic Embedding.** CVPR, 2021. [paper](https://arxiv.org/abs/2011.15039), [code](https://github.com/Thinklab-SJTU/GENN-Astar)

    *Wang, Runzhong and Zhang, Tianqi and Yu, Tianshu and Yan, Junchi and Yang, Xiaokang.*

### [Hamiltonian Cycle Problem](#content)

1. **✨A Bi-Level Framework for Learning to Solve Combinatorial Optimization on Graphs** NeurIPS, 2021. [paper](https://arxiv.org/abs/2106.04927), [code](https://github.com/Thinklab-SJTU/PPO-BiHyb)

    *Wang, Runzhong and Hua, Zhigang and Liu, Gan and Zhang, Jiayi and Yan, Junchi and Qi, Feng and Yang, Shuang and Zhou, Jun and Yang, Xiaokang*

### [Graph Coloring](#content)

1. **Deep Learning-based Hybrid Graph-Coloring Algorithm for Register Allocation.** Arxiv, 2019. [paper](https://arxiv.org/abs/1912.03700)

    *Das, Dibyendu and Ahmad, Shahid Asghar and Venkataramanan, Kumar.*

### [Maximal Common Subgraph](#content)

1. **Fast Detection of Maximum Common Subgraph via Deep Q-Learning.** Arxiv, 2020. [paper](https://arxiv.org/abs/2002.03129)

    *Bai, Yunsheng and Xu, Derek and Wang, Alex and Gu, Ken and Wu, Xueqing and Marinovic, Agustin and Ro, Christopher and Sun, Yizhou and Wang, Wei.*

### [Influence Maximization](#content)

1. **Learning Heuristics over Large Graphs via Deep Reinforcement Learning.** NeurIPS, 2020. [paper](https://arxiv.org/abs/1903.03332)

    *Mittal, Akash and Dhawan, Anuj and Manchanda, Sahil and Medya, Sourav and Ranu, Sayan and Singh, Ambuj.*

2. **Controlling Graph Dynamics with Reinforcement Learning and Graph Neural Networks.** ICML, 2021. [paper](https://arxiv.org/abs/2010.05313)

    *Eli A. Meirom, Haggai Maron, Shie Mannor, Gal Chechik*

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

### [Mixed Integer Programming](#content)

1. **Learning to Search in Branch-and-Bound Algorithms** NeurlPS, 2014. [paper](http://papers.nips.cc/paper/5495-learning-to-search-in-branch-and-bound-algorithms)

    *He, He and Daume III, Hal and Eisner, Jason M*

2. **Exact Combinatorial Optimization with Graph Convolutional Neural Networks** NeurlPS, 2019. [paper](https://arxiv.org/abs/1906.01629), [code](https://github.com/ds4dm/learn2branch)

    *Gasse, Maxime and Chetelat, Didier and Ferroni, Nicola and Charlin, Laurent and Lodi, Andrea*

3. **Improving Learning to Branch via Reinforcement Learning.** NeurIPS Workshop, 2020. [paper](https://openreview.net/forum?id=z4D7-PTxTb)

    *Sun, Haoran and Chen, Wenbo and Li, Hui and Song, Le.*

4. **Hybrid Models for Learning to Branch** NeurlPS, 2020. [paper](https://arxiv.org/abs/2006.15212), [code](https://github.com/pg2455/Hybrid-learn2branch)

    *Gupta, Prateek and Gasse, Maxime and Khalil, Elias B and Kumar, M Pawan and Lodi, Andrea and Bengio, Yoshua*

5. **Accelerating Primal Solution Findings for Mixed Integer Programs Based on Solution Prediction.** AAAI, 2020. [paper](https://arxiv.org/abs/1906.09575)

    *Jian-Ya Ding, Chao Zhang, Lei Shen, Shengyin Li, Bing Wang, Yinghui Xu, Le Song*

6. **Reinforcement Learning for Integer Programming: Learning to Cut** ICML, 2020. [paper](http://proceedings.mlr.press/v119/tang20a.html)

    *Tang, Yunhao and Agrawal, Shipra and Faenza, Yuri*

7. **Solving Mixed Integer Programs Using Neural Networks** Arxiv, 2020. [paper](https://arxiv.org/abs/2012.13349)

    *Nair, Vinod and Bartunov, Sergey and Gimeno, Felix and von Glehn, Ingrid and Lichocki, Pawel and Lobov, Ivan and O'Donoghue, Brendan and Sonnerat, Nicolas and Tjandraatmadja, Christian and Wang, Pengming and others*

8. **Learning Efficient Search Approximation in Mixed Integer Branch and Bound** Arxiv, 2020. [paper](https://arxiv.org/abs/2007.03948)

    *Yilmaz, Kaan and Yorke-Smith, Neil*

9. **Learning a Large Neighborhood Search Algorithm for Mixed Integer Programs** Arxiv, 2020. [paper](https://arxiv.org/abs/2107.10201)

    *Sonnerat, Nicolas and Wang, Pengming and Ktena, Ira and Bartunov, Sergey and Nair, Vinod*

10. **A General Large Neighborhood Search Framework for Solving Integer Linear Programs** NeurlPS, 2020. [paper](https://arxiv.org/abs/2004.00422)

    *Song, Jialin and Lanka, Ravi and Yue, Yisong and Dilkina, Bistra*

11. **Accelerating primal solution findings for mixed integer programs based on solution prediction** AAAI, 2020. [paper](https://arxiv.org/abs/1906.09575)

    *Ding, Jian-Ya, Chao Zhang, Lei Shen, Shengyin Li, Bing Wang, Yinghui Xu, and Le Song*

12. **CombOptNet: Fit the Right NP-Hard Problem by Learning Integer Programming Constraints** Arxiv, 2021. [paper](https://openreview.net/forum?id=z4D7-PTxTb), [code](https://github.com/martius-lab/CombOptNet)

    *Paulus, Anselm and Rolinek, Michal and Musil, Vit and Amos, Brandon and Martius, Georg*

13. **Reinforcement Learning for (Mixed) Integer Programming: Smart Feasibility Pump** ICML Workshop, 2021. [paper](https://arxiv.org/abs/2102.09663)

    *Qi, Meng and Wang, Mengxin and Shen, Zuo-Jun*

14. **Parameterizing Branch-and-Bound Search Trees to Learn Branching Policies** AAAI, 2021. [paper](https://www.aaai.org/AAAI21Papers/AAAI-9826.ZarpellonG.pdf), [code](https://github.com/ds4dm/branch-search-trees)

    *Zarpellon, Giulia and Jo, Jason and Lodi, Andrea and Bengio, Yoshua*

15. **Learning to Select Cuts for Efficient Mixed-Integer Programming** Arxiv, 2021. [journal](https://arxiv.org/abs/2105.13645)

    *Huang, Zeren and Wang, Kerong and Liu, Furui and Zhen, Hui-ling and Zhang, Weinan and Yuan, Mingxuan and Hao, Jianye and Yu, Yong and Wang, Jun*

16. **Generative deep learning for decision making in gas networks** Arxiv, 2021. [paper](https://arxiv.org/abs/2102.02125)

    *Lovis Anderson and Mark Turner and Thorsten Koch*

17. **Offline constraint screening for online mixed-integer optimization** Arxiv, 2021. [paper](https://arxiv.org/abs/2103.13074)

    *Asunción Jiménez-Cordero and Juan Miguel Morales and Salvador Pineda*

18. **Mixed Integer Programming versus Evolutionary Computation for Optimizing a Hard Real-World Staff Assignment Problem** ICAPS, 2021. [paper](https://ojs.aaai.org/index.php/ICAPS/article/view/3521)

    *Peters, Jannik and Stephan, Daniel and Amon, Isabel and Gawendowicz, Hans and Lischeid, Julius and Salabarria, Lennart and Umland, Jonas and Werner, Felix and Krejca, Martin S and Rothenberger, Ralf and others*

19. **Learning To Scale Mixed-Integer Programs** AAAI, 2021. [paper](https://www.aaai.org/AAAI21Papers/AAAI-7940.BertholdT.pdf)

    *Berthold, Timo, and Gregor Hendel*

20. **Learning Pseudo-Backdoors for Mixed Integer Programs** AAAI, 2021. [paper](https://arxiv.org/pdf/2106.05080.pdf)

    *Aaron Ferber and Jialin Song and Bistra Dilkina and Yisong Yue*

### [Causal Discovery](#content)

1. **DAGs with NO TEARS: Continuous Optimization for Structure Learning.** NeurIPS, 2018. [paper](https://arxiv.org/pdf/1803.01422.pdf)

    *Zheng, Xun and Aragam, Bryon and Ravikumar, Pradeep and Xing, Eric.*

2. **Causal Discovery with Reinforcement Learning.** ICLR, 2020. [paper](https://arxiv.org/abs/1906.04477)

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

19. **Generalization of Neural Combinatorial Solvers Through the Lens of Adversarial Robustness** Arxiv, 2021. [paper](https://arxiv.org/pdf/2110.10942.pdf)

    *Simon Geisler, Johanna Sommer, Jan Schuchardt, Aleksandar Bojchevski and Stephan Günnemann*

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

1. **Dispatch of autonomous vehicles for taxi services: A deep reinforcement learning approach** Transportation Research, 2020. [journal](https://www.sciencedirect.com/science/article/pii/S0968090X19312227)

    *Chao Mao, Yulin Liu, Zuo-Jun (Max) Shen*

### [Electronic Design Automation](#content)

1. **✨On Joint Learning for Solving Placement and Routing in Chip Design** NeurIPS, 2021. [paper](https://arxiv.org/abs/2111.00234), [code](https://github.com/Thinklab-SJTU/EDA-AI)

    *Cheng, Ruoyu and Yan, Junchi*

2. **A graph placement methodology for fast chip design** Nature, 2021. [journal](https://www.nature.com/articles/s41586-021-03544-w.pdf)

    *Azalia Mirhoseini, Anna Goldie, Mustafa Yazgan, Joe Wenjie Jiang, Ebrahim Songhori, Shen Wang, Young-Joon Lee, Eric Johnson, Omkar Pathak, Azade Nazi, Jiwoo Pak, Andy Tong, Kavya Srinivasa, William Hang, Emre Tuncer, Quoc V. Le, James Laudon, Richard Ho, Roger Carpenter & Jeff Dean*

### [Generalization](#content)

1. **It’s Not What Machines Can Learn It’s What We Cannot Teach** ICML, 2020. [paper](http://proceedings.mlr.press/v119/yehuda20a/yehuda20a.pdf)

    *Gal Yehuda, Moshe Gabel and Assaf Schuster*

2. **Learning TSP Requires Rethinking Generalization** CP, 2021. [paper](https://arxiv.org/pdf/2006.07054.pdf), [code](https://github.com/chaitjo/learning-tsp)

    *Chaitanya K. Joshi, Quentin Cappart, Louis-Martin Rousseau and Thomas Laurent*

3. **Generalization of Neural Combinatorial Solvers Through the Lens of Adversarial Robustness** Arxiv, 2021. [paper](https://arxiv.org/pdf/2110.10942.pdf)

    *Simon Geisler, Johanna Sommer, Jan Schuchardt, Aleksandar Bojchevski and Stephan Günnemann*

### [Conjunctive Query Containment](#content)

1. **It’s Not What Machines Can Learn It’s What We Cannot Teach** ICML, 2020. [paper](http://proceedings.mlr.press/v119/yehuda20a/yehuda20a.pdf)

    *Gal Yehuda, Moshe Gabel and Assaf Schuster*

### [Orienteering Problem](#content)

1. **A reinforcement learning approach to the orienteering problem with time windows** Computers & Operations Research, 2021. [paper](https://arxiv.org/abs/2011.03647v2), [code](https://github.com/mustelideos/optw_rl)

    *Ricardo Gama, Hugo L. Fernandes*

