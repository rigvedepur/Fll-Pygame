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
ballDestroyed = False

player_rect = pygame.Rect(player_pos[0], player_pos[1], player.get_width(), player.get_height())

ball_timer_index = 2

class Ball:
        def __init__(self, x, y, radius, color):
            self.x = x
            self.y = y
            self.radius = radius
            self.color = color


        def draw(self, screen):
            pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        
        def createRectForBall(self):
            ball_pos = list((self.x, self.y))
            ball_rect = pygame.Rect(ball_pos[0], ball_pos[1], 50, 50)
            return ball_rect

        def create_timer(self, ball_timer_index):

            self.TIMEREVENT = pygame.USEREVENT + ball_timer_index
            pygame.time.set_timer(self.TIMEREVENT, 6000)


            
TIMEREVENT = pygame.USEREVENT + 1
pygame.time.set_timer(TIMEREVENT, 500)


balls = []

def create_random_ball():
    global ball_timer_index
    x = random.randint(0, 1200)
    y = random.randint(0, 800)
    radius = 25
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    ball = Ball(x, y, radius, color)
    ball.create_timer(ball_timer_index)
    ball_timer_index += 1
    balls.append(ball)
    return ball


ball = create_random_ball()

running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(player, player_pos)

    if len(balls) != 0:
        for ball in balls:
            ball.draw(screen)

    if moving_left == True:
        player_pos[0] -= 10
    if moving_right == True:
        player_pos[0] += 10
    if moving_down == True:
        player_pos[1] += 10
    if moving_up == True:
        player_pos[1] -= 10

    player_rect.x = player_pos[0]
    player_rect.y = player_pos[1]


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
            create_random_ball()
            print(f"Number of balls: {len(balls)}")

        for ball in balls:
            if event.type == ball.TIMEREVENT:
                balls.remove(ball)

            if player_rect.colliderect(ball.createRectForBall()):
                print("Collision detected")
                balls.remove(ball)

        

    # screen.blit(player, (300, 400))
    # screen.fill((0, 0, 0))
    clock.tick(60)
    pygame.display.update()
