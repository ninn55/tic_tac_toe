import sys
import os
sys.path.append(os.path.abspath('..\\game'))

from Draw import draw

board = ['X', 'O', 'O', 4, 5, 6, 1, 2, 3]
draw(board)

