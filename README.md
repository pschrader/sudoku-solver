sudoku-solver
=============

Posting some python code I wrote to solve sudoku puzzles.

This code accepts a list of 81 values (0,81) representing a sudoku board. The position in the list correspondes to the position on the sudoku board. 0 is the first cell (called tiles in my script). 80 is the last one. 9 is the first tile of the second row, etc.

The actual integer in the list is the number on a given tile. So if you're sudoku board had a 5 in the very first tile then board[0] = 5.

0 is used in this script to denote an empty tile.

To create a new board you can define a new list and enter in the values in each tile from left to right, top to bottom. Here is an example board list that is in the script.

solvedBoard = [5,7,4,9,3,1,6,8,2,1,9,2,4,8,6,7,3,5,6,8,3,7,2,5,4,9,1,9,2,8,1,5,7,3,4,6,3,5,6,8,4,9,2,1,7,4,1,7,3,6,2,8,5,9,8,6,9,2,1,3,5,7,4,2,4,1,5,7,8,9,6,3,7,3,5,6,9,4,1,2,8]

Defining the board as one continuous list seemed easist to me, but it is impossible to imagine the acutal board in this long list of values. The printBoard(board) function in the script will print the board in a formatted blob of text.

Other core parts of this script are the set of functions that return the numbers in the same row, column and square as the tile you are considering. These come together in the getAllConcerned(tile, board) function which will return a list of all the values already taken up by tiles in the same row, column or quadrant. (quadrant in retrospect was one of many poor terminology choices in this first version, since there are actually 9 squares of nine tiles on the board)

There is a function to test the board to see if it is complete: testBoard(board). That function iterates through each tile and checks to see if it has been populated and if it is populated with the only possible value it could hold.

Finally there a function called workBoard. This function takes a tile and a board as input. It checks to see if it can populate that tile with a value and whether the board is solved. If it is not it recursively calls the function on the next tile. If it can take multiple values, it calls the function recursively with each option, initiating a series of test branches.

Some known problems:

1.  the code doesn't know to stop when it solves the board. I tried to use a break command but I must not be doing that right. 
