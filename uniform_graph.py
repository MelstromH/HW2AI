from state import *
import IDS as dfs
from operator import attrgetter

class Uniform_Graph:
    #Explored states already.
    explored_states = []

    #States in the fringe.
    fringe = []

    #store the final cost of the algorithm.
    final_cost = 0

    def __init__(self, root):
        self.root_state = root
        self.fringe.append(root)

    def find_solution(self):
        state = self.root_state

        while True:
            if len(self.fringe) == 0:
                return False

            if dfs.boardCheck(state.board): #This is the goal state.
                break

            cont = True
            #Has this state been explored?
            for other in self.explored_states:
                if state.compare_states(other):
                    cont = False
                    break
            
            if not cont:
                continue

            #Try to generate each of the children states.
            #Turn on the check to see if the state has already been generated.
            for i in range(5):
                state.generate_child_state(i)

            #Add all the generated children into the fringe.
            for child in state.children:
                self.fringe.append(child)
            
            self.explored_states.append(state)
            self.fringe.remove(state)

            #Now return the node with the smallest overall cost.
            state = min(self.fringe,key=attrgetter('cost'))
            state.print_board()

            print(state.cost)

        
        return True
        