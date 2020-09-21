from state import *
import IDS as dfs
import uniform_graph as ug
import uniform_tree as ut
import time

def main():
    
    #Generate a root state.
    '''
    board = [[False,True,False,False,False],
             [False,False,False,True,False],
             [False,False,False,False,True],
             [False,False,False,False,False]]
    

    v_pos = [1,1]
    '''

    
    board = [[False,True,False,False,False],
             [False,False,False,False,False],
             [False,True,False,False,False],
             [False,False,False,False,False]]
    

    v_pos = [0,1]
    
    

    root = State(5,4,v_pos,board)


    print("--------------- Iterative Deepening Search -----------------")
    graph = dfs.Iterative_Deepening(root)

    t0 = time.time()
    print(graph.IDDFS(100))
    t1 = time.time()

    print("Uniform Cost Graph Search CPU time: ", (t1- t0))

    print("--------------- Uniform Cost Graph Search -----------------")
    graph = ug.Uniform_Graph(root)

    t0 = time.time()
    print(graph.find_solution())
    t1 = time.time()

    print("Uniform Cost Graph Search CPU time: ", (t1- t0))
    

    
    print("--------------- Uniform Cost Tree Search -----------------")
    graph = ut.Uniform_Tree(root)

    t0 = time.time()
    print(graph.find_solution())
    t1 = time.time()

    print("Uniform Cost Tree Search CPU time: ", (t1- t0))
    


if __name__ == '__main__':
    main()
