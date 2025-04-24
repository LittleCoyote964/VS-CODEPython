import pygame
import sys
import random


GRID_SIZE   = 20   # width/height of each snake segment and apple
GRID_WIDTH  = 40   # how many segments across
GRID_HEIGHT = 30   # how many segments down
FPS         = 7   # frames per second, had it at 15 but the snake was to fast to control.

# Colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE = (  0, 0, 255)
RED   = (255,   0,   0)
GOLD = (255, 215, 0)


def random_apple_position():
    return (
        random.randint(0, GRID_WIDTH  - 1) * GRID_SIZE,
        random.randint(0, GRID_HEIGHT - 1) * GRID_SIZE
    )

def main():
    pygame.init()
    screen = pygame.display.set_mode((GRID_WIDTH * GRID_SIZE,
                                      GRID_HEIGHT * GRID_SIZE))
    pygame.display.set_caption("Nick De Leon")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 36)

    # Initialize snake in the center, moving right
    snake = [(GRID_WIDTH//2 * GRID_SIZE,
              GRID_HEIGHT//2 * GRID_SIZE)]
    direction = (GRID_SIZE, 0)

    apple_pos = random_apple_position()
    if random.random() < 0.1:
        apple_color = GOLD
        apple_score = 2
    else:
        apple_color = RED
        apple_score = 1
    score = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP    and direction != (0, GRID_SIZE):
                    direction = (0, -GRID_SIZE)
                elif event.key == pygame.K_DOWN  and direction != (0, -GRID_SIZE):
                    direction = (0, GRID_SIZE)
                elif event.key == pygame.K_LEFT  and direction != (GRID_SIZE, 0):
                    direction = (-GRID_SIZE, 0)
                elif event.key == pygame.K_RIGHT and direction != (-GRID_SIZE, 0):
                    direction = (GRID_SIZE, 0)

        # Move snake head
        head_x, head_y = snake[0]
        dx, dy = direction
        new_head = (head_x + dx, head_y + dy)
        snake.insert(0, new_head)

        # Check for apple collision
        if new_head == apple_pos:
            score += apple_score
            apple_pos = random_apple_position()
            if random.random() < 0.1:
                apple_color = GOLD
                apple_score = 2
            else:
                apple_color = RED
                apple_score = 1
        else:
            snake.pop()  # remove tail segment

        # Check for wall collisions
        if (new_head[0] < 0 or new_head[0] >= GRID_WIDTH*GRID_SIZE or
            new_head[1] < 0 or new_head[1] >= GRID_HEIGHT*GRID_SIZE):
            break  

        # Check for self‑collision
        #if new_head in snake[1:]:
         #   break 

        # 3) DRAW
        screen.fill(BLACK)

        # Draw apple
        pygame.draw.rect(screen, apple_color, (*apple_pos, GRID_SIZE, GRID_SIZE))

        # Draw snake
        for segment in snake:
            pygame.draw.rect(screen, BLUE, (*segment, GRID_SIZE, GRID_SIZE))

        # Draw score
        score_surf = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_surf, (10, 10))

        pygame.display.flip()
        clock.tick(FPS)


    game_over_surf = font.render("Game Over", True, RED)
    screen.blit(game_over_surf, (
        (GRID_WIDTH*GRID_SIZE - game_over_surf.get_width()) // 2,
        (GRID_HEIGHT*GRID_SIZE - game_over_surf.get_height()) // 2
    ))
    pygame.display.flip()
    pygame.time.wait(2000)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
