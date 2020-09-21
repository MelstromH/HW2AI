#State class contains the board information and child states.
class State:
    #The cost of the current state.
    cost = 0

    board = None #This is the board itself. In the class constructor it will
                 #be initialized to a 4x5 array of booleans (true: room is dirty,
                 #false: room is clean)
    
    vacuum_position = [0,0] #A pair containing the position of the vacuum cleaner.


    x_size = 0
    y_size = 0

    #moves
    move_sequence = ''

    #Takes the x and y size of the board
    #and a 2D array which contains the current dirt distribution.
    def __init__(self,x_size, y_size, vacuum_position, dirt_dist):
        if len(dirt_dist) != y_size or len(dirt_dist[0]) != x_size:
            print("Error: dirst distribution array and board size do not match")
            return
        
        self.x_size = x_size
        self.y_size = y_size

        #Copy over the dirst distribution.
        #Access the array by y then x e.g. board[y][x]
        self.board = [[ dirt_dist[y][x] for x in range(x_size)] for y in range(y_size)]
        self.vacuum_position = vacuum_position
        

    #Geneartes a child state based on its input.
    #action parameter is a number which determines what state to generate.
    #   0 -> suck
    #   1 -> up
    #   2 -> down
    #   3 -> right
    #   4 -> left
    #graph check is a parameter which checks if the state has been generated already
    #(this is False by default but I am including it here so that I can use it for 
    #graph based uniform cost search.)
    #Returns the cost of doing that action.
    def generate_child_state(self, action):
        
        child_pos = self.vacuum_position.copy()
        child_board = [row [:] for row in self.board]

        #The cost for different actions.
        cost = [0.2,0.8,0.7,0.9,1]
        moves = ['Suck ','Up ','Down ','Right ','Left ']

        if action == 0:
            child_board[child_pos[1]][child_pos[0]] = False
        elif action == 1 and self.vacuum_position[1] - 1 >= 0:
            child_pos[1] -= 1
        elif action == 2 and self.vacuum_position[1] + 1 < self.y_size:
            child_pos[1] += 1
        elif action == 3 and self.vacuum_position[0] + 1 < self.x_size:
            child_pos[0] += 1
        elif action == 4 and self.vacuum_position[0] - 1 >= 0:
            child_pos[0] -= 1
        else:
            return None
        
        #Create the child object
        child = State(self.x_size,self.y_size,child_pos,child_board)
        child.cost = self.cost + cost[action]
        child.move_sequence = self.move_sequence + moves[action]

        return child

    def print_board(self):
        separator = '-' * (self.x_size * 6 + 1) #Doesnt adjust for differnt x sizes
                                                #but that doesnt really matter.
        print(separator)
        for y in range(self.y_size):
            for x in range(self.x_size):
                print('| D ' if self.board[y][x] else '| C ', end = '')
                
                if self.vacuum_position[0] == x and self.vacuum_position[1] == y:
                    print('V ', end = '')
                else:
                    print('  ', end = '')
                
            print('|')
            print(separator)

    #Compares if two states are the same.
    #returns true if so and false otherwise.
    def compare_states(self, other):
        if not( self.vacuum_position[0] == other.vacuum_position[0] and
                self.vacuum_position[1] == other.vacuum_position[1]):
                return False

        for x in range(self.x_size):
            for y in range(self.y_size):
                if self.board[y][x] != other.board[y][x]:
                    return False
        
        return True
