# Two player and one player tic tac toe 
# By TKChadwick
# https://trinket.io/python/3df33620ca

board = [' ',' ',' ',' ',' ',' ',' ',' ',' '] # This list is the board spaces
def drawboard(): # this function draws the board and board template
  print ''
  print '1|2|3'
  print '-+-+-'
  print '4|5|6' # board template
  print '-+-+-'
  print '7|8|9'
  print ''
  print board[0] + '|' + board[1] + '|' + board[2]
  print '-+-+-'
  print board[3] + '|' + board[4] + '|' + board[5] # the real board format
  print '-+-+-'
  print board[6] + '|' + board[7] + '|' + board[8]
  print ''
    
def moveMaker(player): # gathers input and places the input for the player
  while True:
    inputStr = raw_input(player +': Where do you want to move?').strip() # gathers input
    if inputStr.isdigit(): # input check 1
      input = int(inputStr)
      if 1 <= input <= 9: # input check 2
        if board[input - 1] == ' ': # input check 3
          board[input - 1] = player
          drawboard()
          break
        else: # error message 1
          print ""
          print "Game: Someone has already gone there, try again!"
          print ""
      else: # error message 2
        print ""
        print "Game: Only type digits 1-9, try again!"
        print ""
    else: # error message 3
      print ""
      print "Game: Only type digits 1-9, try again!"
      print ""
        
def winning(player): # checks for winning combos
  winCombos = [ # combos
    [0,1,2],[3,4,5],[6,7,8],
    [0,3,6],[1,4,7],[2,5,8],
    [0,4,8],[2,4,6]]
  for winCombo in winCombos:
    for win in winCombo:
      if player != board[win]: # checks board for combos
        break
    else:
      return True
  return False
  
def drawing(): # checks for a tie
  drawNums = [0,1,2,3,4,5,6,7,8]
  for draw in drawNums:
    if board[draw] == ' ':
      return False
  return True
  
def play2Game(): # Pulls together and runs the 2 player Tic Tac Toe game
  drawboard()
  player = 'X'
  while True: # game loop
    moveMaker(player)
    if winning(player): # prints win message
      print "Game: Player " + player + " has won the game!"
      break
    if drawing(): # prints draw message
      print "Game: Good game! It's a draw!"
      break
    if player == 'X': # switch player
      player = 'O'
    else:
      player = 'X'

play2Game() # plays the 2 player Tic Tac Toe game