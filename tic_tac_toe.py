## STEP 1: Create the Board and Variables
# ==========================================
# A simple list of 9 spots for our board
while True:
    # Fresh board for a new game
    board = ['1', '2', '3', 
             '4', '5', '6', 
             '7', '8', '9']

    # We start with player 'X'
    current_player = 'X'

    print("Welcome to Tic-Tac-Toe!")

    # ==========================================
    # STEP 2: The Main Game Loop
    # ==========================================
    # This loop keeps running until someone wins or ties
    while True:
    # 1. Show the board to the player
        print("\n")
        print(" " + board[0] + " | " + board[1] + " | " + board[2] + " ")
        print("---|---|---")
        print(" " + board[3] + " | " + board[4] + " | " + board[5] + " ")
        print("---|---|---")
        print(" " + board[6] + " | " + board[7] + " | " + board[8] + " ")
        print("\n")

        # 2. Ask the player for their move
        choice = input("Player " + current_player + ", choose a spot (1-9): ")
    
        # 3. Check if the input is valid (must be 1 to 9)
        if choice not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print("Invalid input! Please type a number from 1 to 9.")
            continue # This restarts the loop so they can try again

          
        # Convert their text choice into a list number (index)
        # Example: Spot '1' is actually index 0 in Python
        index = int(choice) - 1
    
        # 4. Check if that spot is already taken
        if board[index] == 'X' or board[index] == 'O':
            print("That spot is already taken! Try another one.")
            continue # This restarts the loop so they can try again
        
        # 5. Place the player's mark on the board
        board[index] = current_player

# ==========================================
        # STEP 3: Check for a Winner
        # ==========================================
        # We check all 8 possible winning combinations manually using simple IF statements
        is_winner = False
    
        # Check Rows
        if board[0] == board[1] == board[2]: is_winner = True
        if board[3] == board[4] == board[5]: is_winner = True
        if board[6] == board[7] == board[8]: is_winner = True
        # Check Columns
        if board[0] == board[3] == board[6]: is_winner = True
        if board[1] == board[4] == board[7]: is_winner = True
        if board[2] == board[5] == board[8]: is_winner = True
        # Check Diagonals
        if board[0] == board[4] == board[8]: is_winner = True
        if board[2] == board[4] == board[6]: is_winner = True
    
        if is_winner == True:
            # Show final board
            print("\n")
            print(" " + board[0] + " | " + board[1] + " | " + board[2] + " ")
            print("---|---|---")
            print(" " + board[3] + " | " + board[4] + " | " + board[5] + " ")
            print("---|---|---")
            print(" " + board[6] + " | " + board[7] + " | " + board[8] + " ")
            print("\n")
            print("Congratulations! Player " + current_player + " wins! 🎉")
            break # Ends the game
        
        # ==========================================
        # STEP 4: Check for a Tie
        # ==========================================
        # If there are no numbers left on the board, it means it's full
        is_tie = True
        for spot in board:
            if spot != 'X' and spot != 'O':
                is_tie = False # Found a number, so game can continue
            
        if is_tie == True:
            print("It's a tie! 👔")
            break # Ends the game
        
        # ==========================================
        # STEP 5: Switch Players
        # ==========================================
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'

# ==========================================
# POST-MATCH: This runs ONLY when a match ends
# ==========================================
print("-" * 30)
play_again = input("Do you want to play another game? (yes/no): ")
    
if play_again.lower() != "yes" and play_again.lower() != "y":
    print("Thanks for playing! Goodbye! 👋")
   