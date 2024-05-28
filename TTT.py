# Define the game board as a list
board = [" " for _ in range(9)]

# Function to print the board
def print_board():
  for i in range(3):
    for j in range(3):
      print(board[i*3 + j], end=" ")
    print()

# Function to check if a player has won
def is_winner(player):
  win_conditions = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
  for condition in win_conditions:
    if all(board[i] == player for i in condition):
      return True
  return False

# Function to check if the board is full
def is_board_full():
  return all(x != " " for x in board)

# Main game loop
while True:
  # Print the current board
  print_board()

  # Get player 1's move
  player = "X"
  move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
  if board[move] != " ":
    print("Invalid move. Please try again.")
    continue
  board[move] = player

  # Check for winner or draw
  if is_winner(player):
    print_board()
    print(f"Player {player} wins!")
    break
  elif is_board_full():
    print_board()
    print("It's a draw!")
    break

  # Switch player
  player = "O" if player == "X" else "X"
