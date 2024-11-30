import pygame, sys, random

# General Setup
pygame.init()
clock = pygame.time.Clock()

# Constants
bg_color = (20, 20, 20)
light_grey = (255, 255, 255)
ball_color = (200, 200, 200)
font = pygame.font.Font('freesansbold.ttf', 40)
title_font = pygame.font.Font('freesansbold.ttf', 70)
player_speed = 0
opponent_speed = 5
ball_speed_x = 5 * random.choice((-1, 1))
ball_speed_y = 5 * random.choice((-1, 1))
player_score = 0
opponent_score = 0
high_score = 0
game_paused = False

# Sound effects
pygame.mixer.init()
bounce_sound = pygame.mixer.Sound('bounce.wav')
score_sound = pygame.mixer.Sound('score.wav')

# Setting up the main window
screen_width = 1350
screen_height = 740
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Enhanced Pong Game')

# Game Rectangles
ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 15, 140)
opponent = pygame.Rect(5, screen_height / 2 - 70, 15, 140)

# Load high score
try:
    with open('highscore.txt', 'r') as file:
        high_score = int(file.read())
except FileNotFoundError:
    high_score = 0

# Function to show the menu
def show_menu():
    screen.fill(bg_color)
    title_text = title_font.render("Pong Game", True, light_grey)
    title_rect = title_text.get_rect(center=(screen_width / 2, screen_height / 4))
    screen.blit(title_text, title_rect)

    instruction_text = font.render("Press 1 for Easy, 2 for Medium, 3 for Hard", True, light_grey)
    instruction_rect = instruction_text.get_rect(center=(screen_width / 2, screen_height / 2))
    screen.blit(instruction_text, instruction_rect)

    pygame.display.flip()

# Ball animation with dynamic speed and angle variation
def ball_animation():
    global ball_speed_x, ball_speed_y, player_score, opponent_score, high_score
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
        pygame.mixer.Sound.play(bounce_sound)

    # Ball collision with player
    if ball.colliderect(player):
        pygame.mixer.Sound.play(bounce_sound)
        if abs(ball.right - player.left) < 10:
            ball_speed_x *= -1.05
            ball_speed_y += random.uniform(-2, 2)

    # Ball collision with opponent
    if ball.colliderect(opponent):
        pygame.mixer.Sound.play(bounce_sound)
        if abs(ball.left - opponent.right) < 10:
            ball_speed_x *= -1.05
            ball_speed_y += random.uniform(-2, 2)

    # Score update
    if ball.left <= 0:
        player_score += 1
        ball_restart()
        pygame.mixer.Sound.play(score_sound)
    if ball.right >= screen_width:
        opponent_score += 1
        ball_restart()
        pygame.mixer.Sound.play(score_sound)

    # Update high score
    high_score = max(high_score, player_score)

# Ball restart
def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_width / 2, screen_height / 2)
    ball_speed_x = 5 * random.choice((-1, 1))
    ball_speed_y = 5 * random.choice((-1, 1))

# Player animation
def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

# Opponent animation with basic AI
def opponent_animation():
    if opponent.centery < ball.centery:
        opponent.y += opponent_speed
    if opponent.centery > ball.centery:
        opponent.y -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

# Drawing visuals
def draw_visuals():
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.aaline(screen, light_grey, (screen_width / 2, 0), (screen_width / 2, screen_height))
    pygame.draw.ellipse(screen, ball_color, ball)

# Pause menu
def pause_menu():
    pause_text = font.render("Paused - Press P to Resume", True, light_grey)
    pause_rect = pause_text.get_rect(center=(screen_width / 2, screen_height / 2))
    screen.blit(pause_text, pause_rect)

# Main loop
menu_active = True
while True:
    if menu_active:
        show_menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    opponent_speed = 3
                    menu_active = False
                elif event.key == pygame.K_2:
                    opponent_speed = 5
                    menu_active = False
                elif event.key == pygame.K_3:
                    opponent_speed = 8
                    menu_active = False
    else:
        # Handling input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open('highscore.txt', 'w') as file:
                    file.write(str(high_score))
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    player_speed += 5
                if event.key == pygame.K_UP:
                    player_speed -= 5
                if event.key == pygame.K_p:
                    game_paused = not game_paused
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    player_speed -= 5
                if event.key == pygame.K_UP:
                    player_speed += 5

        if not game_paused:
            ball_animation()
            player_animation()
            opponent_animation()

        draw_visuals()

        # Score display
        score_text = font.render(f"{opponent_score} : {player_score}  |  High Score: {high_score}", True, light_grey)
        score_rect = score_text.get_rect(center=(screen_width / 2, 60))
        screen.blit(score_text, score_rect)

        if game_paused:
            pause_menu()

        pygame.display.flip()
        clock.tick(120)
