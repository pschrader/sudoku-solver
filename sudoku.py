from random import randint

def getRowMates(tile, board):
    row = tile/9
    rowMates = []
    for i in range(len(board)):
        if (i/9 == row) and (i != tile):
            rowMates.append(board[i])
    return rowMates

def getColMates(tile, board):
    col = tile%9
    colMates = []
    for i in range(len(board)):
        if (i%9 == col) and (i != tile):
            colMates.append(board[i])
    return colMates

def getQuadMates(tile,board):
    rowQuad = (tile/9)/3
    colQuad = (tile%9)/3
    quadMates = []
    for i in range(len(board)):
        if ((i%9)/3 == colQuad) and ((i/9)/3 == rowQuad) and (i != tile):
            quadMates.append(board[i])
    return quadMates

def getAllConcerned(tile,board):
    allConcerned = []
    row = getRowMates(tile,board)
    for r in row:
        if r not in allConcerned:
            allConcerned.append(r)
    col = getColMates(tile,board)
    for c in col:
        if c not in allConcerned:
            allConcerned.append(c)
    quad = getQuadMates(tile,board)
    for q in quad:
        if q not in allConcerned:
            allConcerned.append(q)
    return allConcerned

def possibleValues(tile,board):
    takenValues = getAllConcerned(tile,board)
    possibleValues = []
    #print 'takenValues: ', takenValues
    for i in range (1,10):
        if i not in takenValues:
            possibleValues.append(i)
    #print 'possibleValues: ', possibleValues
    return possibleValues

def testBoard(board):
    for i in range(len(board)):
        possibleValues(i,board)
        if (board[i] < 1) or (board[i] > 9):
            #print 'unsolved: value not 1 - 9'
            return False
        if len(possibleValues(i,board)) != 1:
            #print 'unsolved:  len possible values not 1'
            return False
        if board[i] not in possibleValues(i,board):
            #print 'unsolved:  tile ', i, 'not a possible value'
            return False
    return True

def workBoard(tile, board):
    #header output
    #print '<==============================='
    #print 'Attempting to Solve at tile: ',tile
    #print 'Tile value board[tile] = ', board[tile]
    #printBoard(board)
    possibleVals = possibleValues(tile,board)
    #print 'Possible Values are: ', possibleVals 


    # 0. if you have no options - go back
    if len(possibleVals) == 0:
        #print 'at tile',tile,'I got stuck with no possible values'
        #print 'end of this road'
        #printBoard(board)
        #print '=================================>'
        return board
    
    # 1.update the tile if it is 0 and there is only one possible option
    if (board[tile] == 0) and (len(possibleVals) == 1):
        board[tile] = possibleVals[0]

    # 2. test the board    
    if testBoard(board):
        printBoard(board)
        print "QED!"
        return board

    # 3. if the square is not 0 then go to next tile
    elif (board[tile] != 0):
        copiedBoard = list(board)
        workBoard(tile + 1, copiedBoard)

    # 4. if the square is 0 (and there are multiple possible) run for each
    else:
        for i in possibleVals:
            copiedBoard = list(board)
            copiedBoard[tile] = i
            #print 'setting tile',tile,'to',i
            #print 'calling workboard for tile',tile+1
            #print '=================================>'
            workBoard(tile + 1, copiedBoard)    
    
def printBoard(board):
    linebreak = '\n-------------\n'
    row = linebreak
    for i in range (0,81):            
        if i == 9:
           row = row + '|' + '\n' + '|' + str(board[i])
        elif (i%27 == 0) and (i != 0):
            row = row + '|' + linebreak + '|' + str(board[i])           
        elif (i%9 == 0) and (i != 0):
            row = row + '|' + '\n' + '|' + str(board[i])
        elif (i%3 == 0) and (board[i] < 10):
            row = row + '|' + str(board[i])
        elif (i%3 == 0):
            row = row + '|' + str(board[i])
        else: row = row + str(board[i])
    row = row + '|' + linebreak
    print row


        

board = []
for i in range (0,81):
    board.append(0)

board2 = []
for i in range (0,81):
    board2.append(i)

solvedBoard = [5,7,4,9,3,1,6,8,2,1,9,2,4,8,6,7,3,5,6,8,3,7,2,5,4,9,1,9,2,8,1,5,7,3,4,6,3,5,6,8,4,9,2,1,7,4,1,7,3,6,2,8,5,9,8,6,9,2,1,3,5,7,4,2,4,1,5,7,8,9,6,3,7,3,5,6,9,4,1,2,8]
easyBoard = [6,0,0,1,0,8,2,0,3,0,2,0,0,4,0,0,9,0,8,0,3,0,0,5,4,0,0,5,0,4,6,0,7,0,0,9,0,3,0,0,0,0,0,5,0,7,0,0,8,0,3,1,0,2,0,0,1,7,0,0,9,0,6,0,8,0,0,3,0,0,2,0,3,0,2,9,0,4,0,0,5]
hardBoard = [0,0,0,2,0,0,0,6,3,3,0,0,0,0,5,4,0,1,0,0,1,0,0,3,9,8,0,0,0,0,0,0,0,0,9,0,0,0,0,5,3,8,0,0,0,0,3,0,0,0,0,0,0,0,0,2,6,3,0,0,5,0,0,5,0,3,7,0,0,0,0,8,4,7,0,0,0,1,0,0,0]
