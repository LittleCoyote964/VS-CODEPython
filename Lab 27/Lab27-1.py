import pygame
import random
pygame.init() # initializing the pygame is required.

screen_width = 600
screen_height = 400
game_screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Nick De Leon")

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

#GAME LOOP
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.update()

#FPS Control
clock = pygame.time.Clock()
fps = 15
direction = "RIGHT"
score = 0
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
    clock.tick(fps)

#SNAKE AND APPLE
snake_segments = []
snake_size = 10
snake_length = 5
for i in range(snake_length):
    x = 250 - (snake_size * i)
    y = 200
    segment = pygame.Rect(x, y, snake_size, snake_size)
    snake_segments.append(segment)

#APPLE
apple_size = 10
apple_position = (random.randrange(0, screen_width // apple_size) * apple_size,
                  random.randrange(0, screen_height // apple_size) * apple_size)

apple = pygame.Rect(apple_position[0], apple_position[1], apple_size, apple_size)

#DRAWING THE SNAKE AND APPLE
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    game_screen.fill(black)
    for segment in snake_segments:
        pygame.draw.rect(game_screen, green, segment)
    pygame.draw.rect(game_screen, red, apple)
    pygame.display.update()
    clock.tick(fps)

# CONTROLLING THE SNAKE
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP and direction != 'DOWN':
            direction = 'UP'
        elif event.key == pygame.K_DOWN and direction != 'UP':
            direction = 'DOWN'
        elif event.key == pygame.K_LEFT and direction != 'RIGHT':
            direction = 'LEFT'
        elif event.key == pygame.K_RIGHT and direction != 'LEFT':
            direction = 'RIGHT'

#updating the snake's position
x,y = snake_segments[0].topleft
if direction == 'UP':
    y -= snake_size
elif direction == 'DOWN':
    y += snake_size 
elif direction == 'LEFT':
    x -= snake_size
elif direction == 'RIGHT':
    x += snake_size

new_head = pygame.Rect(x, y, snake_size, snake_size)
snake_segments.insert(0, new_head)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                direction = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                direction = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                direction = 'RIGHT'
#time to move the snake
    x, y = snake_segments[0].topleft
    if direction == 'UP':
        y -= snake_size
    elif direction == 'DOWN':
        y += snake_size
    elif direction == 'LEFT':
        x -= snake_size
    elif direction == 'RIGHT':
        x += snake_size
    new_head = pygame.Rect(x, y, snake_size, snake_size)
    snake_segments.insert(0, new_head)

# Check for collisions
    if ( snake_segments[0].left < 0 or snake_segments[0].right > screen_width or
        snake_segments[0].top < 0 or snake_segments[0].bottom > screen_height or
        snake_segments[0] in snake_segments[1:] ):
        running = False # Game over

# Check if snake eats apple
    if snake_segments[0].colliderect(apple):
        score += 10
        apple_position = (random.randrange(0, screen_width // apple_size) * apple_size,
        random.randrange(0, screen_height // apple_size) * apple_size)
        apple = pygame.Rect(apple_position[0], apple_position[1], apple_size, apple_size)
    else:
        snake_segments.pop() # Remove the last segment

font = pygame.font.Font(None, 36)
score_text = font.render('Score: ' + str(score), True, white) # smoothing
game_screen.blit(score_text, (10, 10))

# Game over screen
game_screen.fill(black)
game_over_text = font.render('Game Over', True, red)
game_screen.blit(game_over_text, (screen_width//2 - game_over_text.get_width()//2, screen_height//2))
pygame.display.update()
pygame.time.wait(2000) # Wait two seconds before closing
pygame.quit()