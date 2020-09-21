# This file implements the Iterative Deepening Search Algorithm.
# This code is based on the iterative deepening search algorith from geeksforgeeks.org
# https://www.geeksforgeeks.org/iterative-deepening-searchids-iterative-deepening-depth-first-searchiddfs/

# first define a function for depth limited search.
# takes a state and the max depth it can search.
# if a solution is found, returns that state. If no solution is found, return False
def DLS(current_state, max_depth):
  #check to see if this state is the solution. i.e. no dirty squares remain
  if boardCheck(current_state) == True: return current_state
    
  #check to see if the search has exceeded the max depth
  if max_depth <= 0: return False
  
  #recurse for all possible actions from current state
  for i in range(5):
    DLS( (generate_child_state(self, i, graph_check = False) ), max_depth-1)
  
  return False
  
# now that we've created depth limited search, here's IDS. Really just calls DLS with a loop to increase the max depth each time
# Technically the maxDepth for the vacuum problem is infinity, so make sure to specify a reasonable value for input.
def IDDFS(source, maxDepth):
  for i in range(maxDepth):
    solution = DLS(source, maxDepth)
    if solution:
      return solution
  return False # no solution was found
 
 
# Here's a function that checks if the entire board is clean
# returns True if all squares are clean and False otherwise
def boardCheck(boardState):
  clean_board = True
  for aRow in boardState:
    if True in aRow:
      clean_board = False
  return clean_board
