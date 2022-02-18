import pygame
import sys
import numpy as np

pygame.init()

WIDTH = 1000
HEIGHT = WIDTH
BG_COLOR = (0, 89, 84)
BOARD_COLOR = (1, 149, 147)
BOARD_GRID_COLOR = (156, 212, 204)

PADDING = 100
BOARD_HEIGHT = HEIGHT - PADDING
BOARD_WIDTH = WIDTH - PADDING
BOARD_ROWS = 15
BOARD_COLS = BOARD_ROWS

SQUARE_SIZE = (WIDTH - PADDING) // BOARD_ROWS
RED = (255, 0, 0)
GREEN = (0, 255, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('SCRABBLE')

# -- Color background and board
screen.fill(BG_COLOR)

board = np.zeros((BOARD_ROWS, BOARD_COLS), str)

color = RED

game_over = False


def draw_board_base():

    # -- Draw board background
    pygame.draw.rect(
        screen, BOARD_COLOR,
        (0 + PADDING / 2, 0 + PADDING / 2, BOARD_WIDTH, BOARD_HEIGHT))

    # -- Draw horizontal lines
    for row in range(BOARD_ROWS + 1):
        pygame.draw.line(
            screen, BOARD_GRID_COLOR,
            (0 + PADDING / 2, row * SQUARE_SIZE + PADDING / 2),
            (BOARD_WIDTH + PADDING / 2, row * SQUARE_SIZE + PADDING / 2), 3)

    # -- Draw horizontal lines
    for col in range(BOARD_COLS + 1):
        pygame.draw.line(
            screen, BOARD_GRID_COLOR,
            (col * SQUARE_SIZE + PADDING / 2, 0 + PADDING / 2),
            (col * SQUARE_SIZE + PADDING / 2, BOARD_WIDTH + PADDING / 2), 3)


def mark_square(row, col, key):
    board[row][col] = key


draw_board_base()

print(f'padding: {PADDING}, SqSize: {SQUARE_SIZE}')

# -- Mainloop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX, mouseY = event.pos

            clicked_row = int((mouseY - PADDING / 2) // SQUARE_SIZE)
            clicked_col = int((mouseX - PADDING / 2) // SQUARE_SIZE)

        if event.type == pygame.KEYDOWN:
            mark_square(clicked_row, clicked_col, pygame.key.name(event.key))
            print(board)

    pygame.display.update()
