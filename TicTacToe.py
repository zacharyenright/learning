import pygame
import sys
pygame.init()

WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")
screen.fill("black")
x_turn = True
o_turn = False

board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

def reset_board():
    global board
    screen.fill((0,0,0))
    board = [
        ["-", "-", "-"],
        ["-", "-", "-"],
        ["-", "-", "-"]
    ]

def load_level():
    # Vertical lines
    pygame.draw.line(screen, (255, 255, 255), (WIDTH/3, 0), (WIDTH/3, HEIGHT), 5)
    pygame.draw.line(screen, (255, 255, 255), (2 * WIDTH/3, 0), (2 * WIDTH/3, HEIGHT), 5)
    
    # Horizontal lines
    pygame.draw.line(screen, (255, 255, 255), (0, HEIGHT/3), (WIDTH, HEIGHT/3), 5)
    pygame.draw.line(screen, (255, 255, 255), (0, 2 * HEIGHT/3), (WIDTH, 2 * HEIGHT/3), 5)


def draw_x(pos_x, pos_y):
    pygame.draw.line(screen, (255, 255, 255), (pos_x - 50, pos_y - 50), (pos_x + 50, pos_y + 50), 5)
    pygame.draw.line(screen, (255, 255, 255), (pos_x + 50, pos_y - 50), (pos_x - 50, pos_y + 50), 5)


def draw_o(pos_x, pos_y):
    pygame.draw.circle(screen, (255, 255, 255), (pos_x, pos_y), 50, 5)


def check_win(board):
    # Check rows
    for row in board:
        if all(element == row[0] and element != "-" for element in row):
            reset_board()
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != "-":
            reset_board()
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "-":
        reset_board()
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "-":
        reset_board()
        return board[0][2]

    # If no winner
    return None


def check_tie(board):
    for row in board:
        for cell in row:
            if cell == "-":
                return False  # If any "-" is found, the game is not tied yet
    return True  # If no "-" is found, the game is tied


def main():
    global x_turn, o_turn
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                running = False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                row = mouse_y // (HEIGHT // 3)
                col = mouse_x // (WIDTH // 3)
                
                if board[row][col] == "-" and x_turn:
                    draw_x(mouse_x, mouse_y)
                    board[row][col] = "X"
                    x_turn = False
                    o_turn = True
                    winner = check_win(board)
                    if winner:
                        reset_board()
                        load_level()
                        break
                    elif check_tie(board):
                        reset_board()
                        load_level()
                        break

                elif board[row][col] == "-" and o_turn:
                    draw_o(mouse_x, mouse_y)
                    board[row][col] = "O"
                    x_turn = True
                    o_turn = False
                    winner = check_win(board)
                    if winner:
                        print("o wins")
                        load_level()
                        break  # Exit the event loop
                    elif check_tie(board):
                        reset_board()
                        load_level()
                        break

        load_level()
        pygame.display.flip()

main()

