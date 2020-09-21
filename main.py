from state import *

def main():
    
    #Generate a root state.
    board = [[False,False,False,True,False],
             [False,False,False,True,False],
             [False,False,False,True,False],
             [False,False,False,True,False]]

    v_pos = [0,0]

    root = State(5,4,v_pos,board)

    root.print_board()

    #Generate a child state.
    cost = root.generate_child_state(3)

    child = root.children[0]

    child.print_board()
    print(cost)
    


if __name__ == '__main__':
    main()
