
#www.checkio.org



def fed_pigeons(n=0): #no working yet
    """
    I start to feed one of the pigeons. 
    A minute later two more fly by and a minute after that another 3. Then 4, and so on (Ex: 1+2+3+4+...). 
    One portion of food lasts a pigeon for a minute, 
    but in case there's not enough food for all the birds,
    the pigeons who arrived first ate first. 
    Pigeons are hungry animals and eat without knowing when to stop. 
    If I have N portions of bird feed, 
    how many pigeons will be fed with at least one portion of wheat?
    example:
    checkio(1) == 1
    checkio(2) == 1
    checkio(5) == 3
    checkio(10) == 6
    """
    
    stop = False
    i = 0
    pigeons = 0
    fed_pigeons = 0
    
    while(not stop):
    
        i = i+1
        pigeons = pigeons + i
        n = n - i 
        
        print "index:%s, pigeons:%s, fed_pigeons:%s"%(i,pigeons,fed_pigeons)
        
        if(fed_pigeons <= 0):
            stop = True
            return fed_pigeons
        
        # stop = raw_input("indes:%x"%i)
        
    return pigeons
    
    
    
def num_to_roman_num(num):  #DONE
    """
    For this task, you should return a roman numeral using the specified integer value ranging from 1 to 3999.
    """
    milares = num / 1000
    cien = num % 1000
    # print cien
    centenas = cien / 100
    # print centenas
    diez = cien % 100
    # print diez
    decenas = diez / 10
    # print decenas
    unidades = diez % 10
    # print unidades
    
    roman_num = ""
        
    for m in range(0,milares,1):
        roman_num = roman_num + 'M'
    
    if centenas == 9:
        roman_num = roman_num + 'CM'
    else:
        if centenas > 5:
            roman_num = roman_num + 'D'
            for c in range(0,centenas-5,1):
                roman_num = roman_num + 'C'
        elif centenas == 5:
            roman_num = roman_num + 'D'
        elif centenas == 4:
            roman_num = roman_num + 'CD'
        else:
            for c in range(0,centenas,1):
                roman_num = roman_num + 'C'
                
                
    if decenas == 9:
        roman_num = roman_num + 'XC'
    else:
        if decenas > 5:
            roman_num = roman_num + 'L'
            for c in range(0,decenas-5,1):
                roman_num = roman_num + 'X'
        elif decenas == 5:
            roman_num = roman_num + 'L'
        elif decenas == 4:
            roman_num = roman_num + 'XL'
        else:
            for c in range(0,decenas,1):
                roman_num = roman_num + 'X'
                
    if unidades == 9:
        roman_num = roman_num + 'IX'
    else:
        if unidades > 5:
            roman_num = roman_num + 'V'
            for c in range(0,unidades-5,1):
                roman_num = roman_num + 'I'
        elif unidades == 5:
            roman_num = roman_num + 'V'
        elif unidades == 4:
            roman_num = roman_num + 'IV'
        else:
            for c in range(0,unidades,1):
                roman_num = roman_num + 'I'
    
    return roman_num
    
    # return milares, centenas, decenas, unidades
    
def tic_tac_toe(array=["X.O","XX.","XOO"]):
    """
    Input: A game result as a list of strings (unicode).
    Output: "X", "O" or "D" as a string.
    Example:
    
    checkio([
    "X.O",
    "XX.",
    "XOO"]) == "X"
    checkio([
    "OO.",
    "XOX",
    "XOX"]) == "O"
    checkio([
    "OOX",
    "XXO",
    "OXX"]) == "D"
    """
    winRow = 0
    winCol = 0
    winTilt = 0
    
    if ( array[0][0] == array[1][1] and array[0][0] == array[2][2]):
        if(array[0][0] != '.'):
            return array[0][0]
        
    if ( array[0][2] == array[1][1] and array[0][2] == array[2][0]):
        if(array[2][0] != '.'):
            return array[2][0]
    
    for i in range(0,3,1):
    
        for j in range(0,3,1):
            if (array[i][0] == array[i][j] ):
                winRow = winRow + 1
                
            if (array[0][i] == array[j][i] ):
                winCol = winCol + 1           
                
        if winRow >= 3 :
            # if (array[i][0] == 'X' or array[i][0] == 'O'):
            if(array[i][0] != '.'):
                return array[i][0]
        if winCol >= 3 :
            # if (array[0][i] == 'X' or array[0][i] == 'O'):
            if(array[0][i] != '.'):
                return array[0][i]
                      
        winRow = 0
        winCol = 0
        
    return "D"
          
def test_tic_tac_toe():    
    tic_tac_toe(["XXX","OXX","OXO"])
    tic_tac_toe(["OXX","OXX","OXO"])
    tic_tac_toe(["OXX","OX.",".XO"])
    tic_tac_toe(["XOO","OXX","OXO"])
    tic_tac_toe(["X..","OXO","OOO"])
    tic_tac_toe(["X..","XXX","OXO"])
    tic_tac_toe([".XX","OXX","OXO"])
    tic_tac_toe(["OXX","XOX","OXO"])
    tic_tac_toe(["OXX","OXX","XXO"])
    
    
def numbered_triangles(input = [[1,4,20],[3,1,5],[50,2,3],[5,2,7],[7,5,20],[4,7,50]]):
    """
    http://www.checkio.org/mission/numbered-triangles/
    Input: The chip info as a list of lists. Each list contain three integers.

    Output: The highest possible score as an integer.
    
    Example:
            checkio([[1, 4, 20], [3, 1, 5], [50, 2, 3], [5, 2, 7], [7, 5, 20], [4, 7, 50]]) == 152
            checkio([[1, 10, 2], [2, 20, 3], [3, 30, 4], [4, 40, 5], [5, 50, 6], [6, 60, 1]]) == 210
            checkio([[1, 2, 3], [2, 1, 3], [4, 5, 6], [6, 5, 4], [5, 1, 2], [6, 4, 3]]) == 21
            checkio([[5, 9, 5], [9, 6, 9], [6, 7, 6], [7, 8, 7], [8, 1, 8], [1, 2, 1]]) == 0
    """
    pass
    
def count_neighbours(grid, row, col):
    """
    http://www.checkio.org/mission/count-neighbours/
    
    Input: Three arguments. A grid as a tuple of tuples with integers (1/0), a row number and column number for a cell as integers.

    Output: How many neighbouring cells have chips as an integer.
    
    Example:
            count_neighbours(((1, 0, 0, 1, 0),
                              (0, 1, 0, 0, 0),
                              (0, 0, 1, 0, 1),
                              (1, 0, 0, 0, 0),
                              (0, 0, 1, 0, 0),), 1, 2) == 3
            count_neighbours(((1, 0, 0, 1, 0),
                              (0, 1, 0, 0, 0),
                              (0, 0, 1, 0, 1),
                              (1, 0, 0, 0, 0),
                              (0, 0, 1, 0, 0),), 0, 0) == 1
    """
    count = 0
    if(len(grid) >= 3 and len(grid) <= 11):
    
        len_grid0 = len(grid[0])
        len_grid = len(grid)
        print len_grid0
        for row_ in grid: 
            if(col >= len_grid0 or row >= len_grid):
                return
            if(len_grid0 == len(row_)):
                continue
            else:   
                return

        print "col:%s, row:%s"%(col, row)
        
        print "col1:%s, row:%s"%(col+1, row)
        if( col+1 < len_grid0):
            if( grid[row][col+1] == 1 ):
                count = count + 1
        
        print "col1:%s, row1:%s"%(col+1, row+1)
        if( col+1 < len_grid0 and row+1 < len_grid0):
            if( grid[row+1][col+1] == 1 ):
                count = count + 1
        
        print "col1:%s, row-1:%s"%(col+1, row-1)        
        if( row-1 >= 0 and col+1 < len_grid0 ):
            if( grid[row-1][col+1] == 1 ):
                count = count + 1

        print "col:%s, row1:%s"%(col, row+1)
        if( row+1 < len_grid0 ):
            if( grid[row+1][col] == 1 ):
                count = count + 1
        
        print "col-1:%s, row:%s"%(col-1, row)
        if( col-1 >= 0 ):
            if( grid[row][col-1] == 1 ):
                count = count + 1
                
        print "col-1:%s, row-1:%s"%(col-1, row-1)    
        if( col-1 >= 0 and row-1 >= 0 ):
            if( grid[row-1][col-1] == 1 ):
                count = count + 1
                
        print "col-1:%s, row1:%s"%(col-1, row+1)
        if( col-1 >= 0 and row+1 < len_grid0):
            if( grid[row+1][col-1] == 1 ):
                count = count + 1
                
        print "col:%s, row1:%s"%(col, row+1)    
        if( row-1 >= 0 ):
            if( grid[row-1][col] == 1 ):
                count = count + 1
                    
        return count
    
    else:
        return
        
FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"        
               
    
def num_to_stringNum(number):
    """
    Input: A number as an integer.
    Output: The string representation of the number as a string.
    """
    
    string_num = ""
    enter = False
    if( number > 0 and number < 1000 ):
        
        if number >= 100:
        
            idx = number // 100
            number = number % 100
            if number == 0:
                return FIRST_TEN[idx-1] + " " + HUNDRED
            string_num = FIRST_TEN[idx-1] + " " + HUNDRED
            # print number
            enter = True
            
        if number >= 10 and number < 20:
            

            number = number % 10
            # print SECOND_TEN[number-1] 
            # print string_num
            if enter: string_num = string_num + " " + SECOND_TEN[number] 
            else: string_num = SECOND_TEN[number] 
            return string_num
            
        if number >= 20:

            idx = number // 10
            number = number % 10
            if number == 0:
                if enter: return string_num + " " + OTHER_TENS[idx - 2]
                else: return OTHER_TENS[idx - 2]
            else:
                if enter: return string_num + " " + OTHER_TENS[idx-2] + " " + FIRST_TEN[number-1]
                else: return OTHER_TENS[idx-2] + " " + FIRST_TEN[number-1]
            
        # if number < 10:
        # else:
        # print number
        # print enter
        # print FIRST_TEN[number-1]
        if enter: return string_num + " " + FIRST_TEN[number-1]
        else: return FIRST_TEN[number-1]
            
        return string_num
        
    else:
        return
    
    
    
def how_to_find_friends(network, first, second):
    """
    http://www.checkio.org/mission/find-friends/
    Input: Three arguments: Information about friends as a tuple of strings; first name as a string; second name as a string.
    Output: Are these drones related or not as a boolean.
    Example:
    check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True
    check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False
    """
    
    
    # index = 0
    # couple = ''
    
    
    for couple, index in enumerate(network):
        network_split = couple.split('-')
        
        
    
    
    
    
    
    
    
    
def safe_pawns(pawns=["b4", "d4", "f4", "c3", "e3", "g5", "d2"]):
    """
    http://www.checkio.org/mission/pawn-brotherhood/
    You are given a set of square coordinates where we have placed white pawns. You should count how many pawns are safe.

    Input: Placed pawns coordinates as a set of strings.

    Output: The number of safe pawns as a integer.

    Example:

    safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    """
    pawns_indexes = set()
    for p in pawns:
        row = int(p[1]) - 1
        col = ord(p[0]) - 97
        pawns_indexes.add((row, col))
    
    count = 0
    
    for row, col in pawns_indexes:
        is_safe = ((row-1, col-1) in  pawns_indexes) or ((row-1, col+1) in  pawns_indexes)
        #print "row: %s, col: %s, is safe? %s"%(row,col,is_safe)
        if is_safe:
            count += 1
    
    return count
    




