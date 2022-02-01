import pygame, sys, random

# Set up pygame
pygame.init()
clock = pygame.time.Clock()

# Set up the window
width = 1280
height = 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong Game")

# Game Rectangles
ball = pygame.Rect(width/2 - 15, height/2 - 15, 30, 30)
opponent = pygame.Rect(width - 20, height/2 - 70, 10, 140)
player = pygame.Rect(10, height/2- 70, 10, 140)

# Background
bg_color = pygame.Color('grey12')
light_grey = (200,200,200)

# Game Variables
ball_speed_x = 5 * random.choice((-1,1))
ball_speed_y = 5 * random.choice((-1,1))
player_speed = 0
opponent_speed = 7

# Text Variables
player_score = 0
opponent_score = 0
game_font = pygame.font.Font('freesansbold.ttf', 35)

# Ball Movement
def ball_animation(): 
    global ball_speed_x, ball_speed_y, player_score, opponent_score
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= height:
        ball_speed_y *= -1
    if ball.left <= 0:
        opponent_score += 1
        ball_reset()
    if ball.right >= width:  
        player_score += 1
        ball_reset()
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

# Player Movement       
def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= height:
        player.bottom = height

# Opponent Movement
def opponent_AI(): 
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= height:
        opponent.bottom = height

# Reset ball to center
def ball_reset():
    global ball_speed_x, ball_speed_y
    ball.center = (width/2, height/2)
    ball_speed_x *= random.choice((-1,1))
    ball_speed_y *= random.choice((-1,1))

while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                player_speed += 7
            if event.key == pygame.K_w:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                player_speed -= 7
            if event.key == pygame.K_w:
                player_speed += 7 
            
    ball_animation()
    player_animation()
    opponent_AI()

    # Visuals Objects
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (width/2,0), (width/2,height))

    score_player = game_font.render(f"{player_score}", False, light_grey)
    screen.blit(score_player, (width/2 - 50, 30))

    score_opponent = game_font.render(f"{opponent_score}", False, light_grey)
    screen.blit(score_opponent, (width/2 + 30, 30))

    # Update screen
    pygame.display.flip()
    clock.tick(60)


