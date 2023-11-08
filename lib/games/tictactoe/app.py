#draw board.
# let player choose side
# play game until terminal state
# print the winner
# add play again and return to menu buttons


#Classes: Player, Board

#rewrote this code ('https://github.com/russs123/TicTacToe/blob/master/tictactoe.py')

import pygame
from pygame.locals import *


screen_width = 600
screen_height = 600

background_color = (37,37,37)
clicked = False

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("TicTacToe")
from classes.board import Board
board = Board()
from classes.player import Player
player = Player()

run = True
while run:

    board.draw(screen=screen, background_color=background_color)
    board.draw_markers(screen=screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
            clicked = False
            print(f"Old board is {board.markers}")
            player.make_move(board=board)
            print("made a move!")
            print(f"New board is {board.markers}")
            


    pygame.display.update()


pygame.quit()