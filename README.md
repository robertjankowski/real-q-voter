[![Build Status](https://travis-ci.com/robertjankowski/real-q-voter.svg?token=xJWSE2zxzWsgsf4jc3ef&branch=master)](https://travis-ci.com/robertjankowski/real-q-voter)

[![codecov](https://codecov.io/gh/robertjankowski/real-q-voter/branch/master/graph/badge.svg)](https://codecov.io/gh/robertjankowski/real-q-voter)

### Simulation of q-voter model on real networks (e.g. Facebook and Twittter)

**Metrics of used networks**
|    |        `<C>` |      `<k_nn>` |        `<k>` |      `E` |     `N` |       `<l>` |
|---:|---------:|----------:|---------:|-------:|------:|--------:|
|  [moreno-health](http://konect.uni-koblenz.de/networks/moreno_health) | 0.146677 |   9.85148 |  8.23553 |  10455 |  2539 | 4.55939 |
|  [soc-fb](http://networkrepository.com/socfb-Stanford3.php) | 0.241639 | 165.38    | 98.1027  | 568309 | 11586 | 2.81857 |
|  [routers](http://networkrepository.com/tech-routers-rf.php) | 0.246429 |  18.2824  |  6.27733 |   6632 |  2113 | 4.60742 |

*** 
***

| **`q`-experiment by dataset**  	|   **`q`-experiment by `q`** 	|  
|:--------:	|:------:	| 
|   <img src="figures/q-experiment-ba.png" width="400" height="300"/>	|  <img src="figures/q-experiment-q=2.png" width="400" height="300"/> 	| 
|   <img src="figures/q-experiment-soc-fb.png" width="400" height="300"/>	| <img src="figures/q-experiment-q=3.png" width="400" height="300"/>  	| 
|   <img src="figures/q-experiment-routers.png" width="400" height="300"/>	|  <img src="figures/q-experiment-q=4.png" width="400" height="300"/> 	| 

*** 
***

| **directed-undirected experiment**  	|   **`q`-experiment by `q`** 	|  
|:--------:	|:------:	| 
|   <img src="figures/directed_undirected_all.png" width="400" height="300"/>	|  <img src="figures/directed_undirected_q=2.png" width="400" height="300"/> 	| 
|   <img src="figures/directed_undirected_q=3.png" width="400" height="300"/>	| <img src="figures/directed_undirected_q=4.png" width="400" height="300"/>  	| 


***
***

| **Preference sampling experiment**  	|   **Majority voting experiment** 	|  
|:--------:	|:------:	| 
|   <img src="figures/preference_sampling_q_2.png" width="400" height="300"/>	|  <img src="figures/majority_voting_all.png" width="400" height="300"/> 	| 
|   <img src="figures/preference_sampling_q_3.png" width="400" height="300"/>	| <img src="figures/majority_voting_q_3.png" width="400" height="300"/>  	| 
|   <img src="figures/preference_sampling_q_4.png" width="400" height="300"/>	|  <img src="figures/majority_voting_q_4.png" width="400" height="300"/> 	| 

