import pygame
import random

pygame.init()

WIDTH, HEIGHT = 640, 640
CELL = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
score = 0


class Snake:
    def __init__(self):
        self.body = [(300, 300), (280, 300), (260, 300)]
        self.direction = (CELL, 0)
        self.grow_pending = 0

    def change_direction(self, new_direction):
        dx, dy = self.direction
        if new_direction != (-dx, -dy):
            self.direction = new_direction

    def move(self):
        head_x, head_y = self.body[0]
        dx, dy = self.direction
        self.body.insert(0, (head_x + dx, head_y + dy))
        if self.grow_pending > 0:
            self.grow_pending -= 1
        else:
            self.body.pop()

    def draw(self, screen):
        for x, y in self.body:
            pygame.draw.rect(screen, (50, 205, 50), (x, y, CELL, CELL))


class Food:
    def __init__(self, snake_body):
        self.position = self.random_position(snake_body)

    def random_position(self, snake_body):
        while True:
            pos = (random.randrange(0, WIDTH, CELL),
                   random.randrange(0, HEIGHT, CELL))
            if pos not in snake_body:
                return pos

    def draw(self, screen):
        x, y = self.position
        pygame.draw.rect(screen, (220, 50, 50), (x, y, CELL, CELL))


snake = Snake()
food = Food(snake.body)

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction((0, -CELL))
            elif event.key == pygame.K_DOWN:
                snake.change_direction((0, CELL))
            elif event.key == pygame.K_LEFT:
                snake.change_direction((-CELL, 0))
            elif event.key == pygame.K_RIGHT:
                snake.change_direction((CELL, 0))

    
    snake.move()
    head_x, head_y = snake.body[0]

    
    if snake.body[0] == food.position:
        snake.grow_pending += 1
        score += 1
        food = Food(snake.body)
        pygame.display.set_caption(f"Score: {score}")

    
    if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
        running = False

   
    if snake.body[0] in snake.body[1:]:
        running = False

    
    screen.fill((128, 128, 128))
    food.draw(screen)
    snake.draw(screen)
    pygame.display.flip()

    clock.tick(10)

pygame.quit()