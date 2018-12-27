#
#
# 
#
#

class board(object):
	def __init__(self):
		self.table = [['-' for x in range(0,3)] for y in range(0,3)]

	def modify(self,ai,x,y):
		# make sure pos is valid
		if (ai):
			self.table[y][x] = 'O'
		else:
			self.table[y][x] = 'X'

	def output(self):
		for y in range(0,3):
			str = ''
			for x in range(0,3):
				str += self.table[y][x]
				if (x != 2):
					str += '|'
			print(str)

	def is_valid(self,x,y):
		if self.board[y][x] == '-':
			return True
		else:	
			return False

	def is_full(self):
		for y in range(0,3):
			for x in range(0,3):
				if self.table[y][x] == '-':
					return False
		return True


class AI(object):

	def any_move(self,board):
		if board.is_full():
			raise ValueError('a move was tried on an full board')
		else:
			for y in range(0,3):
				for x in range(0,3):
					if board.table[y][x] == '-':
						board.modify(True,x,y)
						return


b = board()
ai = AI()




def main():
	while True:
		print('Which x and y coordinate for your move?')
		s_in = input()
		e = s_in.split(' ')
		x = int(e[0])-1
		y = int(e[1])-1

		if (b.isvalid(x,y)):
			b.modify(False,x,y)

		else:
			print('That move isn\'t valid - try again!')

		if b.is_full():
			print('Board full! Game over')
			break

main()