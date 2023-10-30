import pygame
import sys
import time

from game.const import *
from game.drawing import *
from engine.ai import *

class Game:
    def __init__(self) -> None:
        self.board = [[0 for j in range(NB_COLUMN_ROW)] for i in range(NB_COLUMN_ROW)]
        self.drawing = Drawing()
        self.turn = 1
        self.end = False
        self.AI = AI()
        self.playCount = 0

    def launch(self):
        pygame.init()
        screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
        screen.fill(BACKGROUND_COLOR)
        pygame.display.set_caption("Tic Tac Toe")
        self.game_loop(screen)

    def game_loop(self, screen):

        while True:
            if (self.playCount == 9 and self.end == False):
                # Game finished
                pygame.display.update()
                self.play_again(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
                # Player Movement
                if self.turn == 1:
                    # Human Movement
                    if event.type == pygame.MOUSEBUTTONDOWN and self.end != True:
                        if event.button == 1:
                            pos = pygame.mouse.get_pos()
                            # column
                            if pos[0] <= SCREEN_SIZE / 3:
                                column = 0
                            elif pos[0] <= SCREEN_SIZE / 3 * 2:
                                column = 1
                            elif pos [0] <= SCREEN_SIZE:
                                column = 2
                            # row
                            if pos[1] <= SCREEN_SIZE / 3:
                                row = 0
                            elif pos[1] <= SCREEN_SIZE / 3 * 2:
                                row = 1
                            elif pos [1] <= SCREEN_SIZE:
                                row = 2
                            # modify board
                            self.modify_board(column, row, self.turn, screen)                            
                        pygame.display.update()

                else:
                    # second player is the AI.
                    (column, row) = self.AI.play(self.board)
                    self.modify_board(column, row, self.turn, screen)
                    pygame.display.update()
                
                if self.end != True:
                    self.drawing.draw_grid(screen)
                    self.drawing.draw_pieces(screen, self.board)
                    pygame.display.update()
                
                if self.check_align() != None:
                    start, end = self.check_align()

                    if self.end != True:
                        self.drawing.draw_line(screen, start, end)

                    self.end = True
                    pygame.display.update()
                    self.play_again(screen)

    def play_again(self, screen):
            self.drawing.save_screen(screen, self.playCount)
            time.sleep(1)
            # Check game result
            res = self.AI.evaluateBoard(self.board)
            if (res == 10):
                str = "I WIN!"
            elif (res == -10):
                str = "YOU WIN!"
            else:
                str = "IT'S A DRAW!"

            play_again = self.drawing.end_screen(screen, str)
                    
            if play_again:
                self.board = [[0 for j in range(NB_COLUMN_ROW)] for i in range(NB_COLUMN_ROW)]
                self.playCount = 0
                self.turn = 1
                self.end = False
                self.launch()

    def modify_board(self, column, row, value, screen):
        if self.board[column][row] == 0:
            self.board[column][row] = value
            
            if self.turn == 1:
                self.turn = 2
            else:
                self.turn = 1
        self.playCount = self.playCount + 1
        self.drawing.save_screen(screen, self.playCount)
    
    def check_align(self):
        for i in range(NB_COLUMN_ROW):
            if self.board[i][0] != 0:
                to_check = self.board[i][0]

                if self.board[i][1] == to_check and self.board[i][2] == to_check:
                    s, e = [i, 0], [i, 2]
                    return s, e
                
                if i == 0:
                    if self.board[1][1] == to_check and self.board[2][2] == to_check:
                        s, e = [0, 0], [2, 2]
                        return s, e
                
                if i == 2:
                    if self.board[1][1] == to_check and self.board[0][2] == to_check:
                        s, e = [2, 0], [0, 2]
                        return s, e
                            
            if self.board[0][i] != 0:
                to_check = self.board[0][i]

                if self.board[1][i] == to_check and self.board[2][i] == to_check:
                    s, e = [0, i], [2, i]
                    return s, e