import random
import sys

class TicTacToe:
	
	def __init__(self):
		self.board = [" ", " ", " ", 
					  " ", " ", " ", 
					  " ", " ", " "]

	def display_board(self):
		sys.stderr.write("""
		  {} | {} | {} 
		-------------
		  {} | {} | {} 
		-------------
		  {} | {} | {} """.format(*self.board))

	def select_turn(self):
		self.player_select = False
		self.player_turn = False
		while not self.player_select:
			sys.stderr.write("\nYou want to play 'X' or 'O': ")
			self.check = input()
			if self.check == "X" or self.check == "x":
				self.player_turn = True
				sys.stderr.write("\nYou choose X! Let's start the game! ")
				self.player_mark = "X"
				self.AI_mark = "O"
				self.player_select = True
			elif self.check == "O" or self.check == "o": 
				self.player_turn = False
				sys.stderr.write("\nYou choose O! Let's start the game! ")
				self.player_mark = "O"
				self.AI_mark = "X"
				self.player_select = True
			else:
				sys.stderr.write("\n Invalid select ! ")
	
	def playing(self):
		
		if self.player_turn:
			sys.stderr.write("\nplease choose a number from 1~9: ")
			self.player_position = int(input())
			if self.board[self.player_position - 1] != " ":
				sys.stderr.write("\nPlease select a empty spot : ")
			else:
				self.board[self.player_position - 1] = self.player_mark
				self.display_board()
				self.player_turn = False
		else:
			sys.stderr.write("\n********* AI's Turn *********")
			AI_best = self.AI_choice(self.AI_mark)
			self.board[AI_best] = self.AI_mark					
			test.display_board()
			self.player_turn = True
			
	def alphabeta(self, mark, alpha, beta):
		if self.check_win() == self.player_mark:
			return -1
		elif self.check_full():
			return 0
		elif self.check_win() == self.AI_mark:
			return 1
		
		for spot in self.available_spot():
			self.board[spot]= mark
			value = self.alphabeta(self.oppo(mark), alpha, beta)
			self.board[spot]= " "
			if mark == self.AI_mark:
				if value > alpha:
					alpha = value
				if alpha > beta:
					break
			else:
				if value < beta:
					beta = value
				if alpha > beta:
					break
		if mark == self.AI_mark:
			return alpha
		else:
			return beta


	def AI_choice(self, mark):
		bestvalue = float("-inf")
		choices = []
		random.seed()
		if len(self.available_spot()) == 9:
			return random.randint(1,9)	
		for spot in self.available_spot():
			self.board[spot]= mark
			value = self.alphabeta(self.oppo(mark), float("-inf"), float("inf"))
			self.board[spot]= " "
			if value > bestvalue:
				bestvalue = value
				choices = [spot]
			elif value == bestvalue:
				choices.append(spot)
		return random.choice(choices)
	
	def oppo(self,mark):
		if mark == self.AI_mark:
			return self.player_mark
		else:
			return self.AI_mark
		
				
	def available_spot(self):
		pool = []
		for i in range(len(self.board)):
			if self.board[i] == " ":
				pool.append(i)				
		return pool
		
	def check_win(self):
		win_cases = ([0, 1, 2], [3, 4, 5], [6, 7, 8],
					 [0, 3, 6], [1, 4, 7], [2, 5, 8],
					 [0, 4, 8], [2, 4, 6])
		
		for a,b,c in win_cases:
			if self.board[a]== self.board[b]== self.board[c]== self.player_mark:
				self.win_mark = self.player_mark
				return self.win_mark
			elif self.board[a]== self.board[b]== self.board[c]== self.AI_mark:
				self.win_mark = self.AI_mark
				return self.win_mark
				

	def check_full(self):
		if " " not in self.board:
			return True
		
	def game_over(self):
		if self.check_win() == self.AI_mark:
			sys.stderr.write("\nGame over ! AI wins !")
			return True
		elif self.check_win() == self.player_mark:
			sys.stderr.write("\nGame over ! Player wins !")
			return True
		elif self.check_full():
			sys.stderr.write("\nGame Over ! Draw !")
			return True
	
	
	def main(self):
		while self.game_over() != True:
			self.playing()
		
		
if __name__ == '__main__':
	while True:
		test = TicTacToe()
		test.select_turn()
		test.main()

	

	



