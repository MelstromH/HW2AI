from state import *
import IDS as dfs
import uniform_graph as ug
import uniform_tree as ut


def main():
    
    '''
    print("First board state...")
    #Generate a root state.   
    board = [[False,True,False,False,False],
             [False,False,False,True,False],
             [False,False,False,False,True],
             [False,False,False,False,False]]

    v_pos = [1,1]

    root = State(5,4,v_pos,board)
    '''

    #graph1 = dfs.Iterative_Deepening(root)
    #print(graph1.find_solution(10))

    
    #graph2 = ug.Uniform_Graph(root)
    #print(graph2.find_solution())
    
    #graph = ut.Uniform_Tree(root)
    #print(graph.find_solution())
    
    
    #print("Second board state....")
    #Generate a root state.
    
    board2 = [[False,True,False,False,False],
             [True,False,False,True,False],
             [False,False,True,False,False],
             [False,False,False,True,False]]

    v_pos2 = [1,2]


    root2 = State(5,4,v_pos2,board2)
    
    #graph3 = ug.Uniform_Graph(root2)
    #print(graph3.find_solution())
    
    graph4 = dfs.Iterative_Deepening(root2)
    print(graph4.find_solution(15))

    #graph = ut.Uniform_Tree(root2)
    #print(graph.find_solution())
    
        


if __name__ == '__main__':
    main()
