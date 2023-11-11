ROWS = 6
COLS = 7


def GetBoard():
    """
    :return: Empty gird 6X7
    """
    return [[' ' for _ in range(COLS)] for _ in range(ROWS)]


def PrintBoard(board):
    """
    :param board: Grid
    :return: Print grid on console
    """
    for row in board:
        print('|'.join(row))
        print('-' * (COLS * 2 - 1))
    print(' ')


def IsValidMove(board, col):
    """
    :param board: Grid
    :param col: column
    :return: return grid with empty column checks
    """
    return board[0][col] == ' '


def MakeMove(board, col, player):
    """
    :param board: Grid
    :param col: column
    :param player: Assign player value  0 Human X Ai
    :return:
    """
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == ' ':
            board[row][col] = player
            return


def IsWinner(board, player):
    """
    :param board: Grid
    :param player: Assign player value  0 Human X Ai
    :return: Return True if the values are found horizontal,vertically diagonally
    """
    for row in range(ROWS):
        for col in range(COLS - 3):
            if all(board[row][col + i] == player for i in range(4)):
                return True

    for col in range(COLS):
        for row in range(ROWS - 3):
            if all(board[row + i][col] == player for i in range(4)):
                return True

    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            if all(board[row + i][col + i] == player for i in range(4)):
                return True

    for row in range(3, ROWS):
        for col in range(COLS - 3):
            if all(board[row - i][col + i] == player for i in range(4)):
                return True

    return False


def IsBoardFull(board):
    """
    :param board: Grid
    :return: return True if the board is full
    """
    return all(board[0][col] != ' ' for col in range(COLS))


def EvaluateWindow(window, player, opponent):
    """
    :param window:
    :param player:Assign player value  0 Human  and X Ai
    :param opponent: Human or AI
    :return:
    """
    player_count = window.count(player)
    opponent_count = window.count(opponent)

    if player_count == 4:
        return 100
    elif player_count == 3 and opponent_count == 0:
        return 5
    elif player_count == 2 and opponent_count == 0:
        return 2
    elif opponent_count == 3 and player_count == 0:
        return -4
    elif player_count == 1 and opponent_count == 0:
        return 1
    else:
        return 0


def EvaluateBoard(board, player):
    """
    :param board: Grid
    :param player:Assign player value  0 Human  and X Ai
    :return: Evaluation Score
    """
    opponent = 'X' if player == 'O' else 'O'
    score = 0

    # Evaluate rows
    for row in range(ROWS):
        for col in range(COLS - 3):
            window = [board[row][col + i] for i in range(4)]
            score += EvaluateWindow(window, player, opponent)

    # Evaluate columns
    for col in range(COLS):
        for row in range(ROWS - 3):
            window = [board[row + i][col] for i in range(4)]
            score += EvaluateWindow(window, player, opponent)

    # Evaluate diagonals (positive slope)
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            window = [board[row + i][col + i] for i in range(4)]
            score += EvaluateWindow(window, player, opponent)

    # Evaluate diagonals (negative slope)
    for row in range(3, ROWS):
        for col in range(COLS - 3):
            window = [board[row - i][col + i] for i in range(4)]
            score += EvaluateWindow(window, player, opponent)

    return score


def MiniMaxWithAlphaBetaPruning(board, depth, alpha, beta, maximizing_player):
    """
    :param board:Grid
    :param depth:Depth of the tree
    :param alpha: Max value
    :param beta: Min Value
    :param maximizing_player: Assign player value  0 Human  and X Ai
    :return:Returns Minn or Max values
    """
    score = EvaluateBoard(board, 'X')  # Evaluate from the perspective of the AI

    if score == 100 or score == -100 or depth == 0:
        return score

    if maximizing_player:
        max_eval = float('-inf')
        for col in range(COLS):
            if IsValidMove(board, col):
                row = CheckEmptyRow(board, col)
                MakeMove(board, col, 'X')
                eval = MiniMaxWithAlphaBetaPruning(board, depth - 1, alpha, beta, False)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                board[row][col] = ' '  # Undo the move
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = float('inf')
        for col in range(COLS):
            if IsValidMove(board, col):
                row = CheckEmptyRow(board, col)
                MakeMove(board, col, 'O')
                eval = MiniMaxWithAlphaBetaPruning(board, depth - 1, alpha, beta, True)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                board[row][col] = ' '  # Undo the move
                if beta <= alpha:
                    break
        return min_eval


def CheckEmptyRow(board, col):
    """
    :param board: Grid
    :param col: Columns
    :return: Return a row if the position ie empty else Null
    """
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == ' ':
            return row
    return None


def IsBestMove(board):
    """
    :param board: Grid
    :return: Returns the best column
    """
    max_eval = float('-inf')
    alpha = float('-inf')
    beta = float('inf')
    best_col = None

    for col in range(COLS):
        if IsValidMove(board, col):
            row = CheckEmptyRow(board, col)
            MakeMove(board, col, 'X')
            eval = MiniMaxWithAlphaBetaPruning(board, 4, alpha, beta, False)  # Adjust the depth here
            if eval > max_eval:
                max_eval = eval
                best_col = col
            alpha = max(alpha, eval)
            board[row][col] = ' '  # Undo the move

    return best_col


# Driver Code
if __name__ == "__main__":
    board = GetBoard()

    while True:
        PrintBoard(board)

        # Player's move
        while True:
            try:
                player_col = int(input("Enter your move (0-6): "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if 0 <= player_col <= 6 and IsValidMove(board, player_col):
                MakeMove(board, player_col, 'O')
                if IsWinner(board, 'O'):
                    PrintBoard(board)
                    print("You win!")
                    exit()
                break
            else:
                print("Invalid move. Try again.")

        # Check if the board is full after the player's move
        if IsBoardFull(board):
            PrintBoard(board)
            print("It's a tie!")
            exit()

        PrintBoard(board)

        # AI's move
        ai_col = IsBestMove(board)
        MakeMove(board, ai_col, 'X')
        if IsWinner(board, 'X'):
            PrintBoard(board)
            print("AI wins!")
            exit()

        # Check if the board is full after AI's move
        if IsBoardFull(board):
            PrintBoard(board)
            print("It's a tie!")
            exit()
