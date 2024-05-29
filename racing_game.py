import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Racing Game')

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Car settings
car_width = 50
car_height = 100
car_speed = 10

# Other settings
obstacle_width = 50
obstacle_height = 100
obstacle_speed = 7
obstacle_frequency = 1500  # milliseconds

# Font settings
font = pygame.font.SysFont(None, 55)

def draw_car(x, y):
    pygame.draw.rect(screen, green, [x, y, car_width, car_height])

def draw_obstacle(x, y):
    pygame.draw.rect(screen, red, [x, y, obstacle_width, obstacle_height])

def show_score(score):
    score_text = font.render(f"Score: {score}", True, white)
    screen.blit(score_text, [10, 10])

def game_loop():
    car_x = screen_width // 2
    car_y = screen_height - car_height - 20
    car_x_change = 0

    obstacles = []
    score = 0
    clock = pygame.time.Clock()
    running = True

    pygame.time.set_timer(pygame.USEREVENT + 1, obstacle_frequency)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    car_x_change = -car_speed
                if event.key == pygame.K_RIGHT:
                    car_x_change = car_speed
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    car_x_change = 0
            if event.type == pygame.USEREVENT + 1:
                obstacle_x = random.randint(0, screen_width - obstacle_width)
                obstacles.append([obstacle_x, -obstacle_height])

        car_x += car_x_change

        if car_x < 0:
            car_x = 0
        if car_x > screen_width - car_width:
            car_x = screen_width - car_width

        screen.fill(black)
        draw_car(car_x, car_y)

        for obstacle in obstacles:
            obstacle[1] += obstacle_speed
            draw_obstacle(obstacle[0], obstacle[1])

        obstacles = [obstacle for obstacle in obstacles if obstacle[1] < screen_height]

        for obstacle in obstacles:
            if car_y < obstacle[1] + obstacle_height and car_y + car_height > obstacle[1]:
                if car_x > obstacle[0] and car_x < obstacle[0] + obstacle_width or \
                   car_x + car_width > obstacle[0] and car_x + car_width < obstacle[0] + obstacle_width:
                    running = False

        score += 1
        show_score(score)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    game_loop()
