import pygame
import random
import time

pygame.init()

scale = 2.5

screen = pygame.display.set_mode((1200, 800))
player = pygame.image.load('example_kurma_robot.jpg')
player = pygame.transform.scale(player, (612/scale, 438/scale))
player.set_colorkey((255, 255, 255))
player_pos = [0, 300]
moving_left = False
moving_right = False
moving_down = False
moving_up = False
clock = pygame.time.Clock()

class Ball:
        def __init__(self, x, y, radius, color):
            self.x = x
            self.y = y
            self.radius = radius
            self.color = color
        
        def draw(self, screen):
            pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)


balls = []

def create_random_ball():
    x = random.randint(0, 1200)
    y = random.randint(0, 800)
    radius = 25
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    ball = Ball(x, y, radius, color)
    return ball

# num_balls = 10
# for _ in range(num_balls):
#     x = random.randint(0, 1200)
#     y = random.randint(0, 800)
#     radius = 25
#     color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#     ball = Ball(x, y, radius, color)
#     balls.append(ball)
    
TIMEREVENT = pygame.USEREVENT + 1
pygame.time.set_timer(TIMEREVENT, 2000)  


ball = create_random_ball()

running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(player, player_pos)
    ball.draw(screen)
    if moving_left == True:
        player_pos[0] -= 10
    if moving_right == True:
        player_pos[0] += 10
    if moving_down == True:
        player_pos[1] += 10
    if moving_up == True:
        player_pos[1] -= 10


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moving_left = True
            if event.key == pygame.K_RIGHT:
                moving_right = True
            if event.key == pygame.K_UP:
                moving_up = True
            if event.key == pygame.K_DOWN: 
                moving_down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moving_left = False
            if event.key == pygame.K_RIGHT:
                moving_right = False
            if event.key == pygame.K_UP:
                moving_up = False
            if event.key == pygame.K_DOWN:
                moving_down = False
        if event.type == TIMEREVENT:
            ball = create_random_ball()


    # for ball in balls:
    #     ball.draw(screen)
        

    # screen.blit(player, (300, 400))
    # screen.fill((0, 0, 0))
    clock.tick(60)
    pygame.display.update()