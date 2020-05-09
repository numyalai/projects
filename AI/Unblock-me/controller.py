import collections, math,csv

"""


"""

class Board:
  
    #  row for the board
    row = 0
      # rush hour board column variable
    column = 0

    # list that contains the identifiers of the vehicles, used to print a node
    index_vehicle = list()

    
    def __init__(self, board=None, vehicles=None, moved=None, depth=0, value=None):
        self.board = board
        self.vehicles = vehicles
        self.moved = moved
        self.depth = depth
        self.value = value
        
       

    def load_from_file(self, path):
    
        """
        
        :param path: path to file
        Load the board from the file
        """
        board = ""
        self.board = [] # numerical board representation and basic char representation

        # read file and populate matrix
        with open(path) as file:
            for row in csv.reader(file):
                self.board.append(row)
                for value in row:
                    board += value

    
         # get the vehicles from the string
        self.vehicles = list()
        
        Board.column = int(math.sqrt(len(board)))
        Board.row = int(math.floor((Board.column - 1) // 2))

       #counter for the chars of the board
        values = collections.Counter(board)
        #add state of the main vehicle to th list
        self.vehicles.append((True, board.index('r') // Board.column,
                              board.index('r') % Board.column,
                              board.rindex('r') % Board.column))

        # add main vehicle identifier to Board.vehicle_index
        Board.index_vehicle.append('r')
        values.pop('r')
        # add states of other vehicles to the list
        
    
        for identifier in values:

            # get the first and last occurrence of identifier in string
            first = board.index(identifier)
            last = board.rindex(identifier)

            if not identifier == ".":

                # False-> vertical, column, first row, last row
                if last - first > 2:
                    self.vehicles.append((False, first % Board.column, first // Board.column, last // Board.column))

                # true -> horizontal, row, first column, last column)
                else:
                    self.vehicles.append((True, first // Board.column, first % Board.column,  last % Board.column))

                # add vehicle to Board.vehicle_index
                Board.index_vehicle.append(identifier)
        print("Board representation of the rush hour game\n")        
        i = 0
        while(i< len(self.board)):
            print(self.board[i])
            i +=1
            
        print("\nCars whic are present in the rush hour board \n",Board.index_vehicle,"\n")
        # transform list to tuple for hashing
        self.vehicles = tuple(self.vehicles)
        
        
        
        
        # update self.board to use the index of the vehicle instead of identifier
        for index, vehicle in enumerate(self.vehicles):

            # Numerical representation of the cars in the board -> Horizontal vehicles
            if vehicle[0]:
                self.board[vehicle[1]][vehicle[2]] = index
                self.board[vehicle[1]][vehicle[3]] = index
                if vehicle[3] - vehicle[2] > 1:
                    self.board[vehicle[1]][vehicle[2] + 1] = index

            # Numerical representation of the cars in the board -> Vertical vehicles
            else:
                self.board[vehicle[2]][vehicle[1]] = index
                self.board[vehicle[3]][vehicle[1]] = index
                if vehicle[3] - vehicle[2] > 1:
                    self.board[vehicle[2] + 1][vehicle[1]] = index

        # replace '.' with Null
        for row in range(Board.column):
            for col in range(Board.column):
                if self.board[row][col] == ".":
                    self.board[row][col] = None

        x = 0
        y= 0
        print("Initial numerical representation of the rush hour game\n")
        while(x < len(self.board)):
            y=0
            while(y < len(self.board[x])):
                if self.board[x][y] == None:
                    print('.', end=' ')
                else:
                    print(self.board[x][y], end =  ' ')
                y +=1  
            print()    
            x+=1       
            #decrement width of the board 
        Board.column -= 1
        
    def get_hash(self):
        """
       Returns tuple of the vehicles list for hashing the node
        """
        return self.vehicles
    def win(self):
        """
       Return if the red car is at the las cell of the last column
        """
        if self.vehicles[0][3] == Board.column:
            return True
        else:
            return False
    

    def get_moves(self):
        """
            find the vehicles which can move
        :return: array with all possible moves
        """
        moves = []
        
        
        for index, vehicle in enumerate(self.vehicles):
            # enumerate : for the for loop to iterate with a counter 
            # and index for each car
            # horizontally orientated vehicle
            if vehicle[0]:

                # check if vehicle can go backwards
                if not vehicle[2] == 0 and self.board[vehicle[1]][vehicle[2] - 1] is None:
                    moves.append([index, -1])

                # check if vehicle can go forwards
                if not vehicle[3] == Board.column and self.board[vehicle[1]][vehicle[3] + 1] is None:
                    moves.append([index, 1])

            # vertically orientated vehicle
            else:

                # check if vehicle can go upwards
                if not vehicle[2] == 0 and self.board[vehicle[2] - 1][vehicle[1]] is None:
                    moves.append([index, -1])

                # check if vehicle can go backwards
                if not vehicle[3] == Board.column and self.board[vehicle[3] + 1][vehicle[1]] is None:
                    moves.append([index, 1])

        return moves

    def move(self, index, move):
        """
        
        The operators which moves the vehicles accordinf the parameters
         index is the car which can move and move is the value which should be move
             wether -1 or +1
        :returns new Board
        """

        # create new Node
        
        node = Board(list(self.board), list(self.vehicles), (index, move), self.depth + 1)

        # get the vehicle that needs to be moved
        vehicle = node.vehicles[index]

        # move horizontal vehicle
        if vehicle[0]:

            # generate new row for board
            node.board[vehicle[1]] = list(node.board[vehicle[1]])

            if move > 0:
                node.board[vehicle[1]][vehicle[2]] = None
                node.board[vehicle[1]][vehicle[3] + 1] = index
            else:
                node.board[vehicle[1]][vehicle[2] - 1] = index
                node.board[vehicle[1]][vehicle[3]] = None

        # move vertical vehicle
        else:
            if move > 0:

                # copying the modified board for the newly bulild board
                node.board[vehicle[2]] = list(node.board[vehicle[2]])
                node.board[vehicle[3] + 1] = list(node.board[vehicle[3] + 1])

                node.board[vehicle[2]][vehicle[1]] = None
                node.board[vehicle[3] + 1][vehicle[1]] = index
            else:

                # copying the modified board for the newly bulild board
                node.board[vehicle[2] - 1] = list(node.board[vehicle[2] - 1])
                node.board[vehicle[3]] = list(node.board[vehicle[3]])

                node.board[vehicle[2] - 1][vehicle[1]] = index
                node.board[vehicle[3]][vehicle[1]] = None

        # perform the operation 
        
        node.vehicles[index] = (vehicle[0], vehicle[1], vehicle[2] + move, vehicle[3] + move)
        node.vehicles = tuple(node.vehicles)

        # calculate the cost estimate
        node.value = node.cost_estimate()

        return node

   

    def min_distance(self):
        """
        distance for the red vehicle
        :return: minimum distance
        """
        
    
        return Board.column - self.vehicles[0][3]
    
    
    def cost_estimate(self):
        """
       returns the cost estimate for the board to be completed
        """
        return self.depth + self.min_distance() + self.steps()

    def steps(self):
        """
       calculates steps for the completion of the board and returns them
       
        """
            
        steps = 0
        origin = self.vehicles[0][3]

        # check for vehicles in the direct path of the red vehicle
        for i in range(1, self.min_distance() + 1):

            # get the i places from the red vehicle
            index = self.board[Board.row][origin + i]

            if index:

                # get the directly blocking vehicle
                vehicle = self.vehicles[index]

                # center tile of long vehicle in path of red vehicle (1st level blocker)
                if vehicle[2] < self.vehicles[0][1] < vehicle[3]:
                    
                    steps += 2

                    # check if 1st level blocker is blocked on both sides (2nd level blocker)
                    if self.is_blocked(index):
                        steps += 1
                        # check if 2nd level blockers are blocked on both sides (3d level blocker)
                        if self.is_blocked(self.board[vehicle[2] - 1][vehicle[1]]) and self.is_blocked(self.board[vehicle[3] + 1][vehicle[1]]):
                            steps += 1

                # either long or short vehicle in path of red vehicle (1st level blocker)
                else:
                    steps += 1

                    # check if 1st level blocker is blocked on both sides (2nd level blocker)
                    if self.is_blocked(index):
                        steps += 1

                        # check if 2nd level blockers are blocked on both sides (3d level blocker)
                        if self.is_blocked(self.board[vehicle[2] - 1][vehicle[1]]) and self.is_blocked(self.board[vehicle[3] + 1][vehicle[1]]):
                            steps += 1
                    # check if 1st level blocker's shortest route is blocked (2nd level blocker)
                    elif vehicle[2] == self.vehicles[0][1]:
                        if self.is_blocked(self.board[vehicle[3] + 1][vehicle[1]]) and self.board[vehicle[2] - 2][vehicle[1]]:
                            steps += 2
                        elif self.board[vehicle[3] + 1][vehicle[1]]:
                            steps += 1

                    # check if 1st level blocker's shortest route is blocked (2nd level blocker)
                    else:
                        if self.is_blocked(self.board[vehicle[2] - 1][vehicle[1]]) and self.board[vehicle[3] + 2][vehicle[1]]:
                            steps += 2
                        elif self.board[vehicle[2] - 1][vehicle[1]]:
                            steps += 1

        return steps

    def is_blocked(self, index):
        """
        checks whether is blocked
        :param index: index of the vehicle
        :return: boolean indicating if vehicle is blocked
        """
        if not index:
            return False

        #
        vehicle = self.vehicles[index]

        # horizontally orientated vehicle
        if vehicle[0]:
            if vehicle[2] == 0 and self.board[vehicle[1]][vehicle[2] - 1]:
                return True
            elif vehicle[3] == Board.column and self.board[vehicle[1]][vehicle[2] - 1]:
                return True
            elif self.board[vehicle[1]][vehicle[2] - 1] and self.board[vehicle[1]][vehicle[3] + 1]:
                return True

        # vertically orientated vehicle
        else:
            if vehicle[2] == 0 and self.board[vehicle[3] + 1][vehicle[1]]:
                return True
            elif vehicle[3] == Board.column and self.board[vehicle[2] - 1][vehicle[1]]:
                return True
            elif self.board[vehicle[2] - 1][vehicle[1]] and self.board[vehicle[3] + 1][vehicle[1]]:
                return True

        return False
