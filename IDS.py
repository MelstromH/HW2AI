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

    
  # now that we've created depth limited search, here's IDS. Really just calls DLS with a loop to increase the max depth each time
  def find_solution(self, maxDepth):
    
    print("--------------- Iterative Deepening Search -----------------")
    t0 = time.time()
    t1 = 0
    to_search = [self.root_state]
    children = []
    found = None

    timeout = False

    for i in range(maxDepth):
      t1 = time.time()
      if t1 - t0 > 3600:
        timeout = True
        break 

      for node in to_search:
        if boardCheck(node.board):
          found = node
          break
        
        for i in range(5): 
          children.append(node.generate_child_state(i))
          self.generated += 1
        
        self.expanded += 1
      
      if found != None:
        break


      #Remove the None objects
      children = [obj for obj in children if obj]
      #Check that there are children left.
      if len(children) == 0:
        break

      to_search = children [:]
      children.clear()

    print("Search time, ", t1-t0)
    if timeout:
      print("Algorithm timed out")
      print("Nodes expanded: ", self.expanded)
      print("Nodes generated: ", self.generated)
      return False
    elif found != None:
      found.print_board()
      print("The total cost is: ", found.cost)
      print("Moves taken: ", found.move_sequence)
      print("Nodes expanded: ", self.expanded)
      print("Nodes generated: ", self.generated)
      return True

    else:
      return False # no solution was found
  
 

