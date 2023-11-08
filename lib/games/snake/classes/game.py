import pygame
from classes.food import Food
from classes.snake import Snake
import sys

class Game:
    def __init__(self):
        pygame.init()
        self.WINDOW_SIZE = 1000
        self.TILE_SIZE = 50
        self.screen = pygame.display.set_mode([self.WINDOW_SIZE] * 2)
        self.clock = pygame.time.Clock()
        self.new_game()

    def draw_grid(self):
        [pygame.draw.line(self.screen, [50] * 3, (x, 0), (x, self.WINDOW_SIZE))
                                             for x in range(0, self.WINDOW_SIZE, self.TILE_SIZE)]
        [pygame.draw.line(self.screen, [50] * 3, (0, y), (self.WINDOW_SIZE, y))
                                             for y in range(0, self.WINDOW_SIZE, self.TILE_SIZE)]

    def new_game(self):
        self.snake = Snake(self)
        self.food = Food(self)

    def update(self):
        self.snake.update()
        pygame.display.flip()
        self.clock.tick(60)

    def draw(self):
        self.screen.fill('black')
        self.draw_grid()
        self.food.draw()
        self.snake.draw()

    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # snake control
            self.snake.control(event)

    def run(self):
        while True:
            self.check_event()
            self.update()
            self.draw()