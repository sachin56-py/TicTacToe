import pygame, sys
import numpy as np

pygame.init()
HEIGHT = 600
WIDTH = 600
BOARD_ROWS = 3
BOARD_COLS = 3
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = 55

RED = (5,46,20)
BG_COLOR = (255,230,245)
LINE_COLOR = (23,145,135)
CIRCLE_COLOR = (55,230,25)
CROSS_COLOR = (66,60,50)

screen = pygame.display.set_mode( (WIDTH,HEIGHT) )
pygame.display.set_caption( 'TIC_TAC_TOE')
screen.fill( BG_COLOR )

#board
board = np.zeros( (BOARD_ROWS, BOARD_COLS))



def draw_line():
    pygame.draw.line(screen, RED, (0,200), (600,200), 10)
    pygame.draw.line(screen, RED, (0,400), (600,400), 10)
    pygame.draw.line(screen, RED, (200,0), (200,600), 10)
    pygame.draw.line(screen, RED, (400,0), (400,600), 10)

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col]==1:
                pygame.draw.circle(screen, CIRCLE_COLOR,(int(col*200+100), int(row*200+100)), CIRCLE_RADIUS, CIRCLE_WIDTH )
            elif board[row][col]==2:
                pygame.draw.line(screen, CROSS_COLOR,(col*200+SPACE, row*200+200-SPACE), (col*200+200-SPACE, row*200+SPACE), CROSS_WIDTH )
                pygame.draw.line(screen, CROSS_COLOR, (col*200+SPACE, row*200+SPACE), (col*200+200-SPACE, row*200+200-SPACE), CROSS_WIDTH )


def mark_square(row, col, player):
    board[row][col]=player

def available_square(row,col):
    if board[row][col] == 0:
        return True
    else: 
        return False

def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False
    return True


draw_line()

player = 1
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clicked_row = int(mouseY // 200)
            clicked_col = int(mouseX // 200)

            if available_square(clicked_row, clicked_col):
                if player == 1:
                    mark_square (clicked_row, clicked_col, 1)
                    player = 2
                elif player == 2:
                    mark_square(clicked_row, clicked_col, 2)
                    player = 1
                
                draw_figures()
                
    pygame.display.update()
