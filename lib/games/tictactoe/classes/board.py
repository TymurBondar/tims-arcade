import pygame
class Board():
    def __init__(self):
        self.markers = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]
        self.player_to_move = "X"
    
    def draw(self, screen, background_color, grid_color = (255, 255, 255)):
        screen.fill(background_color)
        for x in range (1, 3):
            pygame.draw.line(screen, grid_color, (0, x*200), (600, x * 200), 3)
            pygame.draw.line(screen, grid_color, (x*200, 0), (x * 200, 600), 3)
    

    def draw_markers(self, screen, color=(255, 255, 255)):
        x_pos = 0
        for x in self.markers:
            y_pos = 0
            for y in x:
                if y == 1:
                    pygame.draw.line(screen, color, (x_pos * 200 + 15, y_pos * 100 + 15), (x_pos * 100 + 85, y_pos * 100 + 85), 3)
                    pygame.draw.line(screen, color, (x_pos * 200 + 85, y_pos * 100 + 15), (x_pos * 100 + 15, y_pos * 100 + 85), 3)
                if y == -1:
                    pygame.draw.circle(screen, color, (x_pos * 200 + 50, y_pos * 100 + 50), 38, 3)
                y_pos += 1
            x_pos += 1	


    def check_winner(self, markers):
        # Check rows for winner
        for row in markers:
            if row.count(row[0]) == len(row) and row[0] != None:
                return row[0]

        # Check columns for winner
        for col in range(len(markers[0])):
            check = set([markers[row][col] for row in range(len(markers))])
            if len(check) == 1 and markers[0][col] != None:
                return markers[0][col]

        # Check diagonals for winner
        if markers[0][0] == markers[1][1] == markers[2][2] != None:
            return markers[0][0]
        if markers[0][2] == markers[1][1] == markers[2][0] != None:
            return markers[0][2]

        # Check for draw
        if all(cell != None for row in markers for cell in row):
            return 'Draw'

        # No winner or draw
        return None
