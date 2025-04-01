import pygame
import random
import time
 
pygame.init()
pygame.font.init()

font = pygame.font.Font("pixel.ttf", 45)

scale = 2.5
heart_scale = 6.7

screen = pygame.display.set_mode((1200, 800))
player = pygame.image.load('images/example_kurma_robot.jpg')
player = pygame.transform.scale(player, (612/scale, 438/scale))
player.set_colorkey((255, 255, 255))
player_pos = [0, 300]
moving_left = False
moving_right = False
moving_down = False
moving_up = False
clock = pygame.time.Clock()
ballDestroyed = False

heart1 = pygame.image.load('images/heart.webp')
heart2 = pygame.image.load('images/heart.webp')
heart3 = pygame.image.load('images/heart.webp')

heart1 = pygame.transform.scale(heart1, (612/heart_scale, 438/heart_scale))
heart2 = pygame.transform.scale(heart2, (612/heart_scale, 438/heart_scale))
heart3 = pygame.transform.scale(heart3, (612/heart_scale, 438/heart_scale))

hearts = [heart3, heart2, heart1]

lives = 3



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
            pygame.time.set_timer(self.TIMEREVENT, 9000)


            
TIMEREVENT = pygame.USEREVENT + 1
pygame.time.set_timer(TIMEREVENT, 500)


balls = []

def create_random_ball():
    global ball_timer_index
    x = random.randint(75, 1135)
    y = random.randint(0, 650)
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
    pygame.draw.line(screen, (255, 255, 255), (0, 700), (1200, 700))
    lives_text = font.render(f"Lives: ", True, (255, 255, 255), 130)
    screen.blit(lives_text, (750, 740))

    if len(hearts) > 0:
        for i, heart in enumerate(hearts):
            screen.blit(heart, (1100 - i * 100, 730))

    if len(balls) != 0:
        for ball in balls:
            ball.draw(screen)

    if moving_left and player_pos[0] > 0:
        player_pos[0] -= 10
    if moving_right and player_pos[0] < screen.get_width() - player.get_width():  
        player_pos[0] += 10
    if moving_down and player_pos[1] < 700 - player.get_height():  
        player_pos[1] += 10
    if moving_up and player_pos[1] > 0:  
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
                lives -= 1
                print(f"Lives: {lives}")
                hearts.pop()

            if player_rect.colliderect(ball.createRectForBall()):
                print("Collision detected")
                balls.remove(ball)

    if lives == 0:
        print("Game Over")
        running = False

        

    # screen.blit(player, (300, 400))
    # screen.fill((0, 0, 0))
    clock.tick(60)
    pygame.display.update()
