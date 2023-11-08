import pygame
class Player:
    def __init__(self):
        pass

    def make_move(self, board):
        pos = pygame.mouse.get_pos()
        cell_x = pos[0] // 200
        cell_y = pos[1] // 200
        if board.markers[cell_x][cell_y] == None:
            board.markers[cell_x][cell_y] = board.player_to_move
            board.player_to_move = "O" if board.player_to_move == "X" else "X"
