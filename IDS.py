from state import *
import time

# Here's a function that checks if the entire board is clean
# returns True if all squares are clean and False otherwise
def boardCheck(boardState):
  clean_board = True
  for aRow in boardState:
    if True in aRow:
      clean_board = False
  return clean_board

class Iterative_Deepening:

  expanded = 0
  generated = 0

  def __init__(self, root):
    self.root_state = root

  def dfs(self, node, depth):
    
    if time.time() - self.t0 > 3600:
      print("Error timeout")
      print("Nodes expanded: ", self.expanded)
      print("Nodes generated: ", self.generated)
      return False

    if node == None:
      return False

    
    self.expanded += 1
    
    if boardCheck(node.board):
      node.print_board()
      print("The total cost is: ", node.cost)
      print("Moves taken: ", node.move_sequence)
      return True

    if depth == 0:
      return False

    child_states = []
    for i in range(5):
      child_states.append(node.generate_child_state(i))

    self.generated += len(child_states)
    for child in child_states:
      if self.dfs(child, depth - 1):
        return True
        
    return False

  # now that we've created depth limited search, here's IDS. Really just calls DLS with a loop to increase the max depth each time
  def find_solution(self, maxDepth):
    
    print("--------------- Iterative Deepening Search -----------------")
    self.t0 = time.time()
    
    found = self.dfs(self.root_state, maxDepth)

    print("Search time: ", time.time()-self.t0)
    print("Nodes expanded: ", self.expanded)
    print("Nodes generated: ", self.generated)

    return found # no solution was found
  
 

