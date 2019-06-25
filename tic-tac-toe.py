def setup(p1_marker, p2_marker):
	while p1_marker != "X" and p1_marker != "O":
		p1_marker = input("Player 1, please enter X or O").upper()
	if p1_marker == "X":
		p2_marker = "O"
	else:
		p2_marker = "X"
	return p1_marker, p2_marker
	
def display_board(board):
	print(" {} | {} | {} |\n".format(board[6], board[7], board[8]))
	print("---------------")
	print(" {} | {} | {} |\n".format(board[3], board[4], board[5]))
	print("---------------")
	print(" {} | {} | {} |\n".format(board[0], board[1], board[2]))
	return

def mark_square(board, p1_marker, p2_marker, p1_turn):
		num = int(input("Please enter a number 1-9\n"))
		if p1_turn == True:
			board[num - 1] = p1_marker
		else:
			board[num - 1] = p2_marker
		return board
		
def check_winner(board, win, p1_turn):
	if(board[0] == board[1] == board[2] or
	   board[3] == board[4] == board[5] or
	   board[6] == board[7] == board[8] or
	   board[0] == board[3] == board[6] or
	   board[1] == board[4] == board[7] or
	   board[2] == board[5] == board[8] or
	   board[0] == board[4] == board[8] or
	   board[2] == board[4] == board[6]):
	   win = True
	   if p1_turn == True:
		   print("P1 wins!")
	   else:
		   print("P2 wins!")   
	return win


p1_marker = ""
p2_marker = ""
p1_turn = True
win = False
sboard = [" ", "_", " ", "#", "#", " ", "_", " ", "_"]

p1_marker, p2_marker = setup(p1_marker, p2_marker)
while win == False:
	sboard = mark_square(sboard, p1_marker, p2_marker, p1_turn)
	display_board(sboard)
	win = check_winner(sboard, win, p1_turn)
	p1_turn = ~(p1_turn)
print("Good Game!")