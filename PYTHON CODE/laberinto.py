"""
The labyrinth has no walls, but pits surround the path on each side.
 If a players falls into a pit, they lose. 
 The labyrinth is presented as a matrix (a list of lists): 1 is a pit and 0 is part of the path. 
 The labyrinth's size is 12 x 12 and the outer cells are also pits. Players start at cell (1,1). 
 The exit is at cell (10,10). You need to find a route through the labyrinth. 
 Players can move in only four directions--South (down [1,0]), North (up [-1,0]), East (right [0,1]), West (left [0, -1]). 
 The route is described as a string consisting of different characters: "S"=South, "N"=North, "E"=East, and "W"=West
 
    N
W        E
    S
 
"""

maze_map = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1],
[1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1],
[1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
[1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


def labyrinth_map(maze_map):
    #replace this for solution
    #This is just example for first maze
    row=1
    col=1
    solve_path = ""
    solve_path_arry = []
    # south = False
    # north = False
    # easth = False
    # west = False
    #direction = 0b0000 #
    last_direction = 0b1111
    # cout = 0
    
    while(not row == 10 and not col == 10):
    
        start = True
        direction = 0b0000
        
        print "present_row:%s, present_col:%s"%(row,col)
        if(maze_map[row+1][col]==0 and last_direction != 0b1000):
            # south = True
            direction = direction | 0b0010 #^ last_direction
            print "south"
        if(maze_map[row-1][col]==0 and last_direction != 0b0010):
            # north = True
            direction = direction | 0b1000 #^ last_direction
            print "north"
        if(maze_map[row][col+1]==0 and last_direction != 0b0001):
            # easth = True
            direction = direction | 0b0100 #^ last_direction
            print "easth"
        if(maze_map[row][col-1]==0 and last_direction != 0b0100):
            # west = True
            direction = direction | 0b0001 #^ last_direction
            print "west"
        if(direction == 0b0000):
            print "wall infront of me"
            if(last_direction == 0b0010):
                direction = 0b1000
            if(last_direction == 0b1000):
                direction = 0b0010
            if(last_direction == 0b0001):
                direction = 0b0100
            if(last_direction == 0b0100):
                direction = 0b0001
            row = last_row
            col = last_col
        
        print "direction1:"+ bin(direction)
        while(start):
            
            if(direction == 0b0010):
                row = row+1 #south
                start = False
                dir = 'S'
                solve_path_arry.append(dir)
                last_direction = 0b0010
                # print "solve_path:%s"%solve_path
                
            elif(direction == 0b1000):
                row = row-1 #north
                start = False
                dir = 'N'
                last_direction = 0b1000
                solve_path_arry.append(dir)
                # print "solve_path:%s"%solve_path
                
            elif(direction == 0b0100):
                col = col+1 #easth
                start = False
                dir = 'E'
                last_direction = 0b0100
                solve_path_arry.append(dir)
                # print "solve_path:%s"%solve_path
                
            elif(direction == 0b0001):
                col = col-1 #west
                start = False
                dir = 'W'
                last_direction = 0b0001
                solve_path_arry.append(dir)
                # print "solve_path:%s"%solve_path
            else:
                print "choosen direction"
                direction = last_direction >> 1
                if(direction == 0b00000):
                    print "entre!!"
                    direction = 0b1000
                start = True
                last_row = row
                last_col = col
                print "last_row:%s, last_col:%s"%(last_row,last_col)
                # print "cout:%s"%cout
                # if(cout == 0 and direction != 0b0010 and direction != 0b1000):
                    # solve_path_arry.append(dir)
                # cout = cout + 1
                
            cout = 0    
            print solve_path_arry
            #solve_path = solve_path + dir
            print "solve_path:%s"%solve_path
            print "direction2:" + bin(direction)
            print "next_row:%s, next_col:%s"%(row,col)

            raw_input()
    
    return solve_path
    
def labyrinth_map2(maze_map):
    """
    "EESSWWSSESSWEEESSWWWWSN"
    """
    #replace this for solution
    #This is just example for first maze
    debug = True
    row=1
    col=1
    solve_path = ""
    solve_path_arry = []
    # south = False
    # north = False
    # easth = False
    # west = False
    # define_dir = False
    #direction = 0b0000 #
    last_dir_bifurcation = 0b0000
    last_direction = 0b1111
    cout = 0
    state = 'define_state'
    
    while(True):
    
        if debug: raw_input()
        if(row == 10 and col == 10):
            if debug: print "TERMINE."
            break
        if debug: print solve_path_arry        
        direction = 0b0000
        if debug: print "present_row:%s, present_col:%s"%(row,col)
        if debug: print "STATE: %s"%state

        if(state=='define_state'):
            if(maze_map[row+1][col]==0 and last_direction != 0b1000):
                state = 'south'
                direction = direction | 0b0010 #
                if debug: print "south"
            if(maze_map[row-1][col]==0 and last_direction != 0b0010):
                state = 'north'
                direction = direction | 0b1000 #
                if debug: print "north"
            if(maze_map[row][col+1]==0 and last_direction != 0b0001):
                state = 'easth' 
                direction = direction | 0b0100 #
                if debug: print "easth"
            if(maze_map[row][col-1]==0 and last_direction != 0b0100):
                state = 'west' 
                direction = direction | 0b0001 #
                if debug: print "west"
            if(direction == 0b0000):
                if debug: print "wall infront of me"
                state = 'return_path'
                row = last_row
                col = last_col
            elif(direction != 0b1000 and direction != 0b0100 and direction != 0b0010 and direction != 0b0001):
                if debug: print "choose path"
                state = 'multi_path'
            continue
        
            
        if(state=='south'):
            row = row+1 #south
            dir = 'S'
            solve_path_arry.append(dir)
            last_direction = 0b0010
            state = 'define_state'
            # print "solve_path:%s"%solve_path
            if debug: print "next_row:%s, next_col:%s, cout:%s"%(row,col,cout)
            continue
            
        if(state=='north'):
            row = row-1 #north
            dir = 'N'
            last_direction = 0b1000
            solve_path_arry.append(dir)
            state = 'define_state'
            # print "solve_path:%s"%solve_path
            if debug: print "next_row:%s, next_col:%s, cout:%s"%(row,col,cout)
            continue
            
        if(state=='easth'):
            col = col+1 #easth
            dir = 'E'
            last_direction = 0b0100
            solve_path_arry.append(dir)
            state = 'define_state'
            # print "solve_path:%s"%solve_path
            if debug: print "next_row:%s, next_col:%s, cout:%s"%(row,col,cout)
            continue
            
        if(state=='west'):
            col = col-1 #west
            dir = 'W'
            last_direction = 0b0001
            solve_path_arry.append(dir)
            state = 'define_state'
            # print "solve_path:%s"%solve_path
            if debug: print "next_row:%s, next_col:%s, cout:%s"%(row,col,cout)
            continue
            
        if(state=='multi_path'):
            if debug: print "choosen direction"
            
            while True:
                direction = last_direction >> 1
                if(direction == 0b0000):
                    if debug: print "entre!!"
                    direction = 0b1000
                state = dir_binary2state(direction)
                if debug: print "direction: " + bin(direction) + " last_direction: " + bin(last_direction) + " last_dir_bifurcation: " + bin(last_dir_bifurcation)
                if debug: raw_input()
                if(last_dir_bifurcation != direction):
                    if debug: print "fueraa"
                    break
                else:
                    last_direction = direction
            
            last_row = row
            last_col = col
            last_dir_bifurcation = direction
            if debug: print "last_row:%s, last_col:%s, last_bifurcation:%s"%(last_row,last_col,last_dir_bifurcation)
            if debug: print "direction2:" + bin(direction)
            continue

        if(state == 'return_path'):
            if(last_direction == 0b0010): #south
                direction = 0b1000 #north
            if(last_direction == 0b1000): #north
                direction = 0b0010 #south
            if(last_direction == 0b0001): #west
                direction = 0b0100 #easth
            if(last_direction == 0b0100): #easth
                direction = 0b0001 #west
                
            state = dir_binary2state(direction)
            continue
                
        cout = cout + 1  
        if debug: print solve_path_arry
        #solve_path = solve_path + dir
        #print "solve_path:%s"%solve_path
        if debug: print "direction2:" + bin(direction)
        if debug: print "STATE2:%s"%state
        if debug: print "next_row:%s, next_col:%s, cout:%s"%(row,col,cout)
            

        if debug: raw_input()
    
    return solve_path
    
def dir_binary2state(direction):
    if(direction == 0b0010):
        state = 'south'
    if(direction == 0b1000):
        state = 'north'
    if(direction == 0b0100):
        state = 'easth'
    if(direction == 0b0001):
        state = 'west'
    return state
 

maze_map = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1],
[1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1],
[1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
[1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
 