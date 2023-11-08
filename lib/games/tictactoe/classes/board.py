import pygame
class Board():
    def __init__(self):
        # this holds current board state
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
        for row in self.markers:
            y_pos = 0
            for cell in row:
                if cell == "X":
                    pygame.draw.line(screen, color, (x_pos * 200 + 30, y_pos * 200 + 30), (x_pos * 200 + 170, y_pos * 200 + 170), 3)
                    pygame.draw.line(screen, color, (x_pos * 200 + 170, y_pos * 200 + 30), (x_pos * 200 + 30, y_pos * 200 + 170), 3)
                if cell == "O":
                    pygame.draw.circle(screen, color, (x_pos * 200 + 100, y_pos * 200 + 100), 76, 3)
                y_pos += 1
            x_pos += 1	


    def check_winner(self):
        # Check rows for winner
        for row in self.markers:
            if row.count(row[0]) == len(row) and row[0] != None:
                return row[0]

        # Check columns for winner
        for col in range(len(self.markers[0])):
            check = set([self.markers[row][col] for row in range(len(self.markers))])
            if len(check) == 1 and self.markers[0][col] != None:
                return self.markers[0][col]

        # Check diagonals for winner
        if self.markers[0][0] == self.markers[1][1] == self.markers[2][2] != None:
            return self.markers[0][0]
        if self.markers[0][2] == self.markers[1][1] == self.markers[2][0] != None:
            return self.markers[0][2]

        # Check for draw
        if all(cell != None for row in self.markers for cell in row):
            return 'Draw'

        # No winner or draw
        return None
