import sys
import pygame
import time

from game.const import *

class Drawing:
    def __init__(self) -> None:
        self.blue_circle = pygame.transform.scale(pygame.image.load("img/x.png"), (100, 100))
        self.yellow_circle = pygame.transform.scale(pygame.image.load("img/o.png"), (100, 100))

    def draw_grid(self, screen):
        for i in range(1, NB_COLUMN_ROW):
            pygame.draw.line(screen, GRID_COLOR, (i * SCREEN_SIZE // 3, 0), (i * SCREEN_SIZE // 3, SCREEN_SIZE), 5)

        for i in range(1, NB_COLUMN_ROW):
            pygame.draw.line(screen, GRID_COLOR, (0, i * SCREEN_SIZE // 3), (SCREEN_SIZE, i * SCREEN_SIZE // 3), 5)
    
    def draw_pieces(self, screen, board):
        #blue_circle = pygame.transform.scale(pygame.image.load("img/x.png"), (100, 100))
        #yellow_circle = pygame.transform.scale(pygame.image.load("img/o.png"), (100, 100))
        size = SCREEN_SIZE / NB_COLUMN_ROW

        for i in range(NB_COLUMN_ROW):
            for j in range(NB_COLUMN_ROW):
                x = int(i * size)
                y = int(j * size)

                if board[i][j] == 1:
                    screen.blit(self.blue_circle, (x + size // 2 - 50, y + size // 2 - 50))
                
                if board[i][j] == 2:
                    screen.blit(self.yellow_circle, (x + size // 2 - 50, y + size // 2 - 50))
    
    def draw_line(self, screen, start, end):
        x_start = SCREEN_SIZE // NB_COLUMN_ROW * (start[0] + 1) - SCREEN_SIZE // NB_COLUMN_ROW // 2
        y_start = SCREEN_SIZE // NB_COLUMN_ROW * (start[1] + 1) - SCREEN_SIZE // NB_COLUMN_ROW // 2

        x_end = SCREEN_SIZE // NB_COLUMN_ROW * (end[0] + 1) - SCREEN_SIZE // NB_COLUMN_ROW // 2
        y_end = SCREEN_SIZE // NB_COLUMN_ROW * (end[1] + 1) - SCREEN_SIZE // NB_COLUMN_ROW // 2

        pygame.draw.line(screen, DARK_BLUE, (x_start, y_start), (x_end, y_end), 5)
    
    def end_screen(self, screen, result):
        screen.fill(BACKGROUND_COLOR)
        font = pygame.font.Font("game/font/Roboto-Regular.ttf", 20)
        
        str = result + "  Click to play again!"
        text = font.render(str, True, (0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (SCREEN_SIZE // 2, SCREEN_SIZE // 2)
        screen.blit(text, text_rect)
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return True
                    