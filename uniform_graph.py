from state import *
import IDS as dfs
import time

class Uniform_Graph:
    #Explored states already.
    explored_states = []

    #States in the fringe.
    fringe = []
    generated = 0
    expanded =  0

    #store the final cost of the algorithm.
    final_cost = 0

    def __init__(self, root):
        self.root_state = root
        self.fringe.append(root)
        self.generated = 1

    def find_solution(self):
        print("--------------- Uniform Cost Graph Search -----------------")
        t0 = time.time()
        t1 = 0
        timeout = False  

        while True:
            t1 = time.time()
            if t1 - t0 > 3600:
                timeout = True
                break

            if len(self.fringe) == 0:
                return False
  
            state = self.fringe.pop(0)
            
            if dfs.boardCheck(state.board): #This is the goal state.
                break

            #Try to generate each of the children states.
            #Turn on the check to see if the state has already been generated.
            for i in range(5):
                child_state = state.generate_child_state(i)
                
                if child_state != None:
                    #Check that this state hasnt already been explored.
                    explored = False
                    #Has this state been explored?
                    for other in self.explored_states:
                        if child_state.compare_states(other):
                            explored = True
                            break

                    if not explored:
                        self.generated += 1
                        self.fringe.append(child_state)                

            
            self.explored_states.append(state)
            self.fringe.sort(key=lambda x: x.cost)

            self.expanded += 1


        print("Search time: ", t1-t0)
        if timeout:
            print("Algorithm timed out")
            print("Nodes expanded: ", self.expanded)
            print("Nodes generated: ", self.generated)
            return False

        print("The total cost is: ", state.cost)
        print("Moves taken: ", state.move_sequence)
        print("Nodes expanded: ", self.expanded)
        print("Nodes generated: ", self.generated)

        state.print_board()

        return True
        