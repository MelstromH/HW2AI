from state import *
import IDS as dfs
import uniform_graph as ug
import uniform_tree as ut


def main():
    
    print("First board state...")
    #Generate a root state.   
    board = [[False,True,False,False,False],
             [False,False,False,True,False],
             [False,False,False,False,True],
             [False,False,False,False,False]]

    v_pos = [1,1]

    root = State(5,4,v_pos,board)

    graph = dfs.Iterative_Deepening(root)
    print(graph.find_solution(10))

    graph = ug.Uniform_Graph(root)
    print(graph.find_solution())

    graph = ut.Uniform_Tree(root)
    print(graph.find_solution())

    print("Second board state....")
    #Generate a root state.
    
    board = [[False,True,False,False,False],
             [True,False,False,True,False],
             [False,False,True,False,False],
             [False,False,False,True,False]]

    v_pos = [1,2]

    root = State(5,4,v_pos,board)

    
    graph = dfs.Iterative_Deepening(root)
    print(graph.find_solution(20))

    graph = ug.Uniform_Graph(root)
    print(graph.find_solution())

    graph = ut.Uniform_Tree(root)
    print(graph.find_solution())

        


if __name__ == '__main__':
    main()
