1.How to execute the program

**python3 ConnectFourAiGameMinimax.py**

**python3 ConnectFourAiGameMinimaxAlphaBeta.py**

Player have input number between 0-6 which is the location of  column values and follow the pattern


Human Player  is denoted by O
Computer Player is denoted by X

Sample Execution is shown below:


(msds) PS C:\Users\Ashish\PycharmProjects\ConnectFour> py .\ConnectFourAiGameMinimax.py

-------------
 | | | | | | 
-------------
 | | | | | |
-------------
 | | | | | |
-------------
 | | | | | |
-------------
 | | | |X| |
-------------
 | | | |O| |
-------------

Enter your move (0-6): 4


**Analysis:**

The Connect Four game has a finite number of states, and theoretically, a perfect player should be able to find a
strategy that guarantees winning or at least guarantees not losing.
The minimax algorithm is designed to find the optimal strategy for a player assuming that the opponent plays optimally as well.
However, the Connect Four game tree is quite large, and exploring all possible moves might be computationally expensive.
Alpha-beta pruning is an optimization technique applied to the minimax algorithm, which reduces the number of nodes evaluated in the search tree.
It can significantly improve the performance of the algorithm, especially in games with a large search space.

When running the code with MiniMax algorithm we could observe some lag in the computer AI moves while with
alpha beta pruning they computer moves are instantaneously.


The performance of the minimax algorithm and alpha-beta pruning algorithm depends on the specific problem and the size of the search space. In the context of the Connect Four game, which has a relatively large search space, alpha-beta pruning is expected to outperform the basic minimax algorithm because it reduces the number of nodes explored in the game tree.
Below  are some key points of comparison between minimax and alpha-beta pruning:

**Time Complexity:**
        Minimax: The time complexity is exponential in the depth of the search tree.
        Alpha-Beta Pruning: Alpha-beta pruning significantly reduces the number of nodes evaluated, leading to a much lower effective branching factor. In the best-case scenario, the time complexity is O(b^(d/2)), where b is the branching factor and d is the depth of the tree.

**Effect on Search Space:**
        Minimax explores the entire search space, even nodes that are known to be irrelevant for the final decision.
        Alpha-beta pruning prunes away branches that cannot affect the final decision, resulting in a more efficient search.

**Performance Improvement:**
        Alpha-beta pruning generally performs better than minimax, especially as the depth of the search tree increases. The improvement becomes more significant for larger search spaces.

**Memory Usage:**
        Both algorithms have similar memory requirements, as they operate on the same search tree structure. Memory usage is typically proportional to the depth of the tree.

**Optimality:**
        Both algorithms guarantee optimal results when searching the entire game tree. However, alpha-beta pruning achieves optimality more efficiently by avoiding unnecessary exploration.

**Depth of Search:**
        The depth parameter in the minimax_move and alphabeta_move calls controls the depth of the search. A deeper search generally provides more accurate results but takes longer.

In summary, alpha-beta pruning is an optimization of the minimax algorithm, designed to reduce the number of nodes explored and improve efficiency. In games like Connect Four with a large search space, alpha-beta pruning is likely to show a significant performance improvement over the basic minimax algorithm#   C o n n e t F o u r A i G a m e  
 