import pygame, random, sys
from pygame.math import Vector2 


class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1, 0)
        self.new_block = False
    def draw_snake(self):
        for el in self.body:
            snake_rect = pygame.Rect(int(el[0] * cell_size), int(el[1] * cell_size), cell_size, cell_size)
            pygame.draw.rect(screen, GREEN, snake_rect)
    def move_snake(self):
         if self.new_block == True:
           body_copy = self.body[:]
           body_copy.insert(0, body_copy[0] + self.direction)
           self.body = body_copy[:]
           self.new_block = False
         else: 
           body_copy = self.body[:-1]
           body_copy.insert(0, body_copy[0] + self.direction)
           self.body = body_copy[:]
    def add_block(self):
        self.new_block = True
    def get_length(self):
        return len(self.body)

class APPLE:
    def __init__(self):
        self.x = random.randint(0, cell_num-1)
        self.y = random.randint(0, cell_num-1)
        self.pos = Vector2(self.x, self.y)
    def draw_apple(self):
        fruit_rect = pygame.Rect(int(self.x * cell_size), int(self.y * cell_size), cell_size, cell_size)
        pygame.draw.ellipse(screen, RED, fruit_rect)
    def randomise(self):
        self.x = random.randint(0, cell_num-1)
        self.y = random.randint(0, cell_num-1)
        self.pos = Vector2(self.x, self.y)

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.apple = APPLE()
    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()
    def draw_elements(self):
        self.apple.draw_apple()
        self.snake.draw_snake()
    def check_collision(self):
        if self.apple.pos == self.snake.body[0]:
           self.apple.randomise()
           self.snake.add_block()
    def check_fail(self):
        # if snake hits the wall
        # if snake hits itself
        for el in range(self.snake.get_length()):
            if el != 0:
                if self.snake.body[0] == self.snake.body[el]:
                    self.game_over()
    def game_over(self):
        pygame.quit()
        sys.exit()

cell_size = 30
cell_num = 20
fps = 30

BROWN = (101,70, 33)
GREEN = (170, 215, 60)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((cell_size * cell_num, cell_size * cell_num))
pygame.display.set_caption("my first game")
clock = pygame.time.Clock()

main_game = MAIN()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_UP:
               main_game.snake.direction = Vector2(0, -1)
           if event.key == pygame.K_DOWN:
               main_game.snake.direction = Vector2(0, 1)
           if event.key == pygame.K_RIGHT:
               main_game.snake.direction = Vector2(1, 0)
           if event.key == pygame.K_LEFT:
               main_game.snake.direction = Vector2(-1, 0)

    screen.fill(BROWN)
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(fps)

pygame.quit()