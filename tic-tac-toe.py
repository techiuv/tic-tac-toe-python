import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = 55

# Colors
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
screen.fill(BG_COLOR)

# Board
board = [[None] * BOARD_COLS for _ in range(BOARD_ROWS)]

# Player
player = 'X'


class TicTacToe:
    def __init__(self):
        self.board = [[None] * BOARD_COLS for _ in range(BOARD_ROWS)]
        self.player = 'X'

    def draw_lines(self):
        # Horizontal lines
        pygame.draw.line(screen, LINE_COLOR, (0, 200), (600, 200), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0, 400), (600, 400), LINE_WIDTH)

        # Vertical lines
        pygame.draw.line(screen, LINE_COLOR, (200, 0), (200, 600), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (400, 0), (400, 600), LINE_WIDTH)

    def draw_figures(self):
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if self.board[row][col] == 'O':
                    pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * 200 + 100), int(row * 200 + 100)), CIRCLE_RADIUS, CIRCLE_WIDTH)
                elif self.board[row][col] == 'X':
                    pygame.draw.line(screen, CROSS_COLOR, (col * 200 + SPACE, row * 200 + 200 - SPACE),
                                     (col * 200 + 200 - SPACE, row * 200 + SPACE), CROSS_WIDTH)
                    pygame.draw.line(screen, CROSS_COLOR, (col * 200 + SPACE, row * 200 + SPACE),
                                     (col * 200 + 200 - SPACE, row * 200 + 200 - SPACE), CROSS_WIDTH)

    def mark_square(self, row, col):
        self.board[row][col] = self.player

    def available_square(self, row, col):
        return self.board[row][col] is None

    def is_board_full(self):
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if self.board[row][col] is None:
                    return False
        return True

    def check_winner(self):
        # Check horizontal, vertical, and diagonal for a winner
        for row in range(BOARD_ROWS):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != None:
                self.draw_win_line(row, 0, row, 2)
                return True
        for col in range(BOARD_COLS):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != None:
                self.draw_win_line(0, col, 2, col)
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != None:
            self.draw_win_line(0, 0, 2, 2)
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != None:
            self.draw_win_line(0, 2, 2, 0)
            return True
        return False

    def draw_win_line(self, row1, col1, row2, col2):
        # Draws winning line
        pygame.draw.line(screen, (255, 0, 0),
                         (col1 * 200 + 100, row1 * 200 + 100), 
                         (col2 * 200 + 100, row2 * 200 + 100), 15)

    def switch_player(self):
        self.player = 'O' if self.player == 'X' else 'X'

    def restart(self):
        time.sleep(2)  # Pause before resetting
        self.board = [[None] * BOARD_COLS for _ in range(BOARD_ROWS)]
        screen.fill(BG_COLOR)
        self.draw_lines()


def get_mouse_click():
    x, y = pygame.mouse.get_pos()

    clicked_row = int(y // 200)
    clicked_col = int(x // 200)

    return clicked_row, clicked_col


def main():
    game = TicTacToe()
    game.draw_lines()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                row, col = get_mouse_click()

                if game.available_square(row, col):
                    game.mark_square(row, col)
                    game.draw_figures()

                    if game.check_winner():
                        game.restart()

                    elif game.is_board_full():
                        game.restart()

                    game.switch_player()

        pygame.display.update()


if __name__ == "__main__":
    main()
