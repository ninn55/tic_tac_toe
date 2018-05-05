from __future__ import print_function
from colorama import init, Fore, Style

init()

def draw(board):
	print('')

	sub_draw(board[0], False)
	print(Fore.WHITE + '|', end = '')
	sub_draw(board[1], False)
	print(Fore.WHITE + '|', end = '')
	sub_draw(board[2], True)
	
	print(Fore.WHITE + '-+-+-')

	sub_draw(board[3], False)
	print(Fore.WHITE + '|', end = '')
	sub_draw(board[4], False)
	print(Fore.WHITE + '|', end = '')
	sub_draw(board[5], True)
	
	print(Fore.WHITE + '-+-+-')

	sub_draw(board[6], False)
	print(Fore.WHITE + '|', end = '')
	sub_draw(board[7], False)
	print(Fore.WHITE + '|', end = '')
	sub_draw(board[8], True)
	
	print('')

def sub_draw(obj, line_end):
	if not line_end:
		if type(obj) is str:
			if obj == 'X':
				print(Fore.GREEN + obj, end = '')
			elif obj == 'O':
				print(Fore.RED + obj, end = '')
			else:
				print('\n')
				print('A error has accrue, use ctrl + c to interupt the program')
		elif type(obj) is int:
			if obj >= 1 and obj <= 9:
				print(Style.DIM + str(obj), end = '')
		else:
			print('\n')
			print('A error has accrue, use ctrl + c to interupt the program')
	else:
		if type(obj) is str:
			if obj == 'X':
				print(Fore.GREEN + obj)
			elif obj == 'O':
				print(Fore.RED + obj)
			else:
				print('\n')
				print('A error has accrue, use ctrl + c to interupt the program')
		elif type(obj) is int:
			if obj >= 1 and obj <= 9:
				print(Style.DIM + str(obj))
		else:
			print('\n')
			print('A error has accrue, use ctrl + c to interupt the program')

	

if __name__ == '__main__':
	#board = [7, 8, 9, 4, 5, 6, 1, 2, 3]
	board = ['X', 'O', 'O', 4, 5, 6, 1, 2, 3]
	draw(board)