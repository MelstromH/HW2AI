from state import *
import IDS as dfs
import uniform_graph as ug

def main():
    
    #Generate a root state.
    board = [[False,False,False,True,False],
             [False,False,False,True,False],
             [False,False,False,True,False],
             [False,False,False,True,False]]

    v_pos = [0,0]

    root = State(5,4,v_pos,board)

    root.print_board()

    #dfs.IDDFS(root,10)
    graph = ug.Uniform_Graph(root)
    print(graph.find_solution())




if __name__ == '__main__':
    main()
