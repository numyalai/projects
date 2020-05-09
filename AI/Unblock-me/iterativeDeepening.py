

import sys, controller, os.path, collections
from timeit import default_timer as time
"""
Importing required files and libraries which are required for some calculations
and easy solution of the program
"""

def IDS(root):
    print("Enter maximum depth for the solution")
    localDepth = int(input())
    
    """
    This Function recieves an object of the root node as a parameter
    which contains all the required attributes of the borad 
    such as borad, width, root, vehicles list
    as a result the functions returns a node or nothing
    if a solution is found the funtction returs a winning state
    """
    max_depth = 0
    x = 0
    
    while len(stack):

        
        # gets the first state from the stack
        state = stack.popleft()
        
        if max_depth > localDepth:
            print("No solution found in the entered depth")
            sys.exit()
        
        # The Algorithm starts it's rules from here
        # generate all the possible states which are possible from the root state
        # by the moves and adds them to stack and closed list
        # until the state depth is less than the maximum depth
        if state.depth < max_depth:
            for move in state.get_moves():
                child = state.move(move[0], move[1])
                x +=1

                # check wether the state is already in closed list or not
                if child.get_hash() not in explored:

                    # add the children node to the closedlist and open list
                    
                    stack.appendleft(child)
                    explored[child.get_hash()] = [state.vehicles, move]
                    

                    # check if current generated state is a solution
                    # which means the red car shoud be at the last column of the board
                    
                    if move[0] == 0:
                        if child.win():
                           
                            print("\nSolution Found \n")
                            x = 0
                            y= 0
                            
                            while(x < len(child.vehicles)):
                                print(child.vehicles[x])
                                x+=1
                            x =0  
                            print()
                            while(x < len(child.board)):
                                y=0
                                while(y < len(child.board[x])):
                                    if child.board[x][y] == None:
                                        print('.', end=' ')
                                    else:
                                         print(child.board[x][y], end =  ' ')
                                   
                                    y +=1  
                                print()    
                                x+=1        
                                        
                               
                            print()    
                            return (child.get_hash())
                
                           

        # adds the roor node to the state to continue for the search
        # increase the maximum_depth for the search which is the main characteristic of IDS
        if len(stack) == 0:
            stack.append(root)
            explored.clear()
            explored[root.get_hash()] = None
            max_depth += 1
      
         

"""
running the scripte
"""
if len(sys.argv) <= 1:
    print ("Error in file")
    print ("Wrong script entered\n")
    print("Try: python iterativeDeepening.py filename.txt")
    sys.exit()



#check if the file is entered correctly and the path is accessable
elif not os.path.isfile(sys.argv[1]):
    print ("Wrong path or script entered")
    print ("Try python iterativeDeepening.py filename.txt")
    sys.exit()

# If everything is correct
else:

    # initialize root state
    root = controller.Board()
    # load the data from the file and assign all it's values to the corresponding
    # variables
    root.load_from_file(sys.argv[1])
#closed list for the objects configuration which takes to the solution
    explored = dict()
    explored[root.get_hash()] = None
    # an open list for the states
    stack = collections.deque()
    stack.append(root)


start = time()
# get the solution state as an object
solutionState = IDS(root)




end = time()
# get the moves from the root to the solution state
moveList = []
while explored[solutionState] is not None:
    
    moveList.append(explored[solutionState][1])
    
    solutionState = explored[solutionState][0]
moveList.reverse()




#print(len(node))

#node[0] = list(node[0])

#node[0][0] = "horizontal"


#print(node[0][0])

#while i < len(node):
 #   node[i] = list(node[i])
  #  if node[i][0] == True:
   #     node[i][0] = "horizontal"
    #else:
     #   node[i][0] ="vertical"
    #i+=1    
#print(node)
#print(str(node))        
# print results
    
print ("\nsolution found in  depth %d" % (len(moveList)))
print ("\n%d states were configured in %f seconds" % (len(explored), (end - start)))
print (moveList)
print


