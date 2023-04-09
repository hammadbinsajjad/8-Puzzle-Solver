# 8 Puzzle Solver

## Introduction:

8 puzzle is a puzzle game with 8 tiles in a 3 x 3 grid. 1 tile is empty space which is used to move the tiles around.
The goal of this game is to move the tiles in such a way to arrange then in increasing order starting from top right.
Like the pattern below.

| 1   | 2   | 3   |
|-----|-----|-----|
| 4   | 5   | 6   |
| 7   | 8   | 0   |

## Algorithms:

This puzzle solver is a combination of 2 algorithms.
1. DLS or Depth Limited Search
2. IDS or Iterative Deepening Search

### Depth Limited Search
- This algorithm performs DFS or Depth First Search with a specified limit. If the goal cannot be found within that depth
limit than the search has failed.

### Iterative Deepening Search
- This algorithm used DLS and iteratively increases the depth limit to continue searching for the goal state one level
deeper in every iteration. 

Using both these algorithms prevents creating a entire tree to perform DFS on it which can become a problem for cases 
where the tree can grow to large depths.

## Method:
The pseudocode for the algorithm (coded in Python) is as follows

- First check if the problem can be solved
  - Count the number of inversions (count numbers greater than the current number ahead of it in a flattened list)
  - If number of inversion is even, solution is possible. Otherwise not possible.
- Initialize the depth to 0
- Create a loop that increments the dept limit by 1 in each iteration
  - For every iteration we run DLS search.
      - If the goal is the current state, return current state
      - If the depth limit is reached, return None
      - For all the actions (UP, DOWN, LEFT, RIGHT) possible for the current state, repeat DLS recursively with decrementing depth.
      
        Any action is possible if and only if
        - Performing the action does not go beyond the limits of the grid
        - The inverse of the action was not the previous action
      - If the path was found from any of the actions, append current state to the path and return it.
- Print out the path in reverse order