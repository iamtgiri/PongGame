import pygame, sys, random

# General Setup
pygame.init()
clock = pygame.time.Clock()

# Constant 
# bg_color = pygame.Color("grey12")
bg_color1 = (86,125,70)
bg_color = (126,200,80)
light_grey = (255,255,255)
ball_color = (255,0,0)
font = pygame.font.Font('digital.ttf', 70)
player_speed = 0
ball_speed_x = 5 * random.choice((-1,1))
ball_speed_y = 5 * random.choice((-1,1))
opponent_speed = 5
player_score = 0
opponent_score = 0

# Setting up the main window
screen_width = 1350
screen_height = 740
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong Game made by tanmoyGiri')

# Game Rectangles
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30,30)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70, 15, 140)
opponent = pygame.Rect(5, screen_height/2 - 70, 15, 140)

# Required Functions 
def ball_animation():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y 
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1 
    if ball.left <= 0 or ball.right >= screen_width:
        ball_restart()
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1 

def player_animation():
    player.y += player_speed
    if player.top <=0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def opponent_animation():
    if opponent.center[1] < ball.y:
        opponent.top += opponent_speed
    if opponent.center[1] > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <=0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_width/2, screen_height/2)
    ball_speed_y *= random.choice((-1,1))
    ball_speed_x *= random.choice((-1,1))

def visual():
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)      
    pygame.draw.rect(screen, light_grey, opponent)      
    pygame.draw.aaline(screen, light_grey, (screen_width/2,0),(screen_width/2, screen_height))
    pygame.draw.ellipse(screen, ball_color, ball)

while True:
    # Handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 5
            if event.key == pygame.K_UP:
                player_speed -= 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 5
            if event.key == pygame.K_UP:
                player_speed += 5
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                player_speed -= 5
            if event.button == 5:
                player_speed += 5
                
    ball_animation()
    player_animation()
    opponent_animation()
    
    # score count 
    if ball.left <= 5:
        player_score += 1
    elif ball.right >= screen_width - 5:
        opponent_score += 1
    if player_score == 15 or opponent_score == 15:
        break
    
    # Visuals
    visual()
    
    text = font.render(f"{opponent_score} : {player_score}", True, light_grey, bg_color)
    textRect = text.get_rect()
    textRect.center = (screen_width/2,60)
    screen.blit(text, textRect)

    # Updating the window
    pygame.display.flip()
    clock.tick(120)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    if opponent_score > player_score:
        result1 = '''You Lost the game...Computer Win !'''
    else:
        result1 = '''Congrats ! You Win !'''
    
    screen.fill(bg_color1)    
    text = font.render(result1, True, light_grey, bg_color1)
    textRect = text.get_rect()
    textRect.center = (screen_width/2,screen_height/2)
    screen.blit(text, textRect)
    pygame.display.flip()
    clock.tick(120)    