def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
def is_valid_move(board, move):
    return move in board and board[move] == ' '
def play_game():
    theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
                'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
                'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
    turn = 'X'
    for i in range(9):
        printBoard(theBoard)
        print(f"Turn for {turn}. Move on which space?")
        move = input().strip()
        if is_valid_move(theBoard, move):
            theBoard[move] = turn
        else:
            print("Invalid move, try again.")
            continue
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
    printBoard(theBoard)
play_game()
