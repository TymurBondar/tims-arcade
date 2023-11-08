from random import randrange
import pygame

vec2 = pygame.math.Vector2


class Snake:
    def __init__(self, game):
        self.game = game
        self.size = game.TILE_SIZE
        self.rect = pygame.rect.Rect([0, 0, game.TILE_SIZE - 2, game.TILE_SIZE - 2])
        self.range = self.size // 2, self.game.WINDOW_SIZE - self.size // 2, self.size
        self.rect.center = self.get_random_position()
        self.direction = vec2(0, 0)
        self.step_delay = 100  # milliseconds
        self.time = 0
        self.length = 1
        self.segments = []
        self.directions = {pygame.K_w: 1, pygame.K_s: 1, pygame.K_a: 1, pygame.K_d: 1}
        
    def control(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and self.directions[pygame.K_w]:
                self.direction = vec2(0, -self.size)
                self.directions = {pygame.K_w: 1, pygame.K_s: 0, pygame.K_a: 1, pygame.K_d: 1}

            if event.key == pygame.K_s and self.directions[pygame.K_s]:
                self.direction = vec2(0, self.size)
                self.directions = {pygame.K_w: 0, pygame.K_s: 1, pygame.K_a: 1, pygame.K_d: 1}

            if event.key == pygame.K_a and self.directions[pygame.K_a]:
                self.direction = vec2(-self.size, 0)
                self.directions = {pygame.K_w: 1, pygame.K_s: 1, pygame.K_a: 1, pygame.K_d: 0}

            if event.key == pygame.K_d and self.directions[pygame.K_d]:
                self.direction = vec2(self.size, 0)
                self.directions = {pygame.K_w: 1, pygame.K_s: 1, pygame.K_a: 0, pygame.K_d: 1}

    def delta_time(self):
        time_now = pygame.time.get_ticks()
        if time_now - self.time > self.step_delay:
            self.time = time_now
            return True
        return False

    def get_random_position(self):
        return [randrange(*self.range), randrange(*self.range)]

    def check_borders(self):
        if self.rect.left < 0 or self.rect.right > self.game.WINDOW_SIZE:
            self.game.new_game()
        if self.rect.top < 0 or self.rect.bottom > self.game.WINDOW_SIZE:
            self.game.new_game()

    def check_food(self):
        if self.rect.center == self.game.food.rect.center:
            self.game.food.rect.center = self.get_random_position()
            self.length += 1

    def check_selfeating(self):
        if len(self.segments) != len(set(segment.center for segment in self.segments)):
            self.game.new_game()

    def move(self):
        if self.delta_time():
            self.rect.move_ip(self.direction)
            self.segments.append(self.rect.copy())
            self.segments = self.segments[-self.length:]

    def update(self):
        self.check_selfeating()
        self.check_borders()
        self.check_food()
        self.move()

    def draw(self):
        [pygame.draw.rect(self.game.screen, 'green', segment) for segment in self.segments]
