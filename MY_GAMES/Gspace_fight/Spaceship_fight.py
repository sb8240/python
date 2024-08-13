import pygame # importing required module
import os
pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # this set the size of the window
pygame.display.set_caption("pygame@souro") # this sets the caption for the window

FPS = 60
VEL = 5
BULLET_VEL = 7
MAX_BULLETS = 3

MIDDLE_WALL = pygame.Rect(WIDTH//2 -5, 0, 10, HEIGHT)
BLACK_COLOR_CODE = (0,0,0)
WHITE_CLOR_CODE= (255,255,255)
RED_COLOR = (255, 0, 0)
YELLOW_COLOR = (255, 255, 0)
HEALTH_FONT = pygame.font.SysFont("comicsans", 40)
WINNER_FONT = pygame.font.SysFont("comicsans", 150)
SPACEFHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2
BULLET_HIT_SOUND = pygame.mixer.Sound("Assets\hit.wav")
BULLET_FIRED_SOUND = pygame.mixer.Sound("Assets\die.wav")

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets','spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(SPACEFHIP_WIDTH, SPACESHIP_HEIGHT)), 90) # FOR ROTATION IN CERTAIN ANGLE
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets','spaceship_red.png'))
RED_SPACESHIPE = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE,(SPACEFHIP_WIDTH, SPACESHIP_HEIGHT)), 270)
SPACE_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'space.png')),(WIDTH, HEIGHT))

def draw_window(RED, YELLOW, RED_BULLETS, YELLOW_BULLETS, RED_HEALTH, YELLOW_HEALTH):

    #WIN.fill(WHITE_CLOR_CODE) # it fill color inside game window
    WIN.blit(SPACE_IMAGE, (0, 0))
    pygame.draw.rect(WIN, BLACK_COLOR_CODE, MIDDLE_WALL)

    RED_HEALTH_TEXT = HEALTH_FONT.render("HEALTH: " + str(RED_HEALTH), 1, WHITE_CLOR_CODE)
    YELLOW_HEALTH_TEXT = HEALTH_FONT.render("HEALTH: " + str(YELLOW_HEALTH), 1, WHITE_CLOR_CODE)
    WIN.blit(RED_HEALTH_TEXT, (WIDTH - RED_HEALTH_TEXT.get_width() - 10, 10))
    WIN.blit(YELLOW_HEALTH_TEXT, (10, 10))

    WIN.blit(YELLOW_SPACESHIP,(YELLOW.x, YELLOW.y)) # we use blit when we want to draw a surface(the images when loaded onto the screen) onto the screen
    WIN.blit(RED_SPACESHIPE, (RED.x, RED.y))

    for bullet in RED_BULLETS:
        pygame.draw.rect(WIN, RED_COLOR, bullet)

    for bullet in YELLOW_BULLETS:
        pygame.draw.rect(WIN, YELLOW_COLOR, bullet)

    pygame.display.update()

def yellow_movement_keys(KEYS_PRESSED, YELLOW):

    if KEYS_PRESSED[pygame.K_a] and YELLOW.x - VEL > 0: # LEFT
            YELLOW.x -= VEL
    if KEYS_PRESSED[pygame.K_s] and YELLOW.y + VEL + YELLOW.height < HEIGHT - 15: # DOWN
            YELLOW.y += VEL 
    if KEYS_PRESSED[pygame.K_d] and YELLOW.x + VEL + YELLOW.width < MIDDLE_WALL.x: # RIGHT
            YELLOW.x += VEL
    if KEYS_PRESSED[pygame.K_w] and YELLOW.y - VEL > 0: # UP 
            YELLOW.y -= VEL

def red_movement_keys(KEYS_PRESSED, RED):

    if KEYS_PRESSED[pygame.K_LEFT] and RED.x - VEL > MIDDLE_WALL.x + MIDDLE_WALL.width: # LEFT
            RED.x -= VEL
    if KEYS_PRESSED[pygame.K_DOWN] and RED.y + VEL + RED.height < HEIGHT - 15: # DOWN
            RED.y += VEL 
    if KEYS_PRESSED[pygame.K_RIGHT] and RED.x + VEL + RED.width < WIDTH: # RIGHT
            RED.x += VEL
    if KEYS_PRESSED[pygame.K_UP] and RED.y - VEL > 0: # UP 
            RED.y -= VEL

def control_bullets(YELLOW_BULLETS, RED_BULLETS, YELLOW, RED):
        for bullet in YELLOW_BULLETS:
                bullet.x += BULLET_VEL
                if RED.colliderect(bullet):
                        pygame.event.post(pygame.event.Event(RED_HIT))
                        YELLOW_BULLETS.remove(bullet)
                elif bullet.x > WIDTH: # IF BULLET MOVES OUT OF SCREEN THEN REMOVE IT
                        YELLOW_BULLETS.remove(bullet)

        for bullet in RED_BULLETS:
                bullet.x -= BULLET_VEL
                if YELLOW.colliderect(bullet):
                        pygame.event.post(pygame.event.Event(YELLOW_HIT))
                        RED_BULLETS.remove(bullet)
                elif bullet.x < 0: # IF BULLET MOVES OUT OF SCREEN THEN REMOVE IT
                        RED_BULLETS.remove(bullet)

def draw_winner(text):
        DRAW_TEXT = WINNER_FONT.render(text, 1, WHITE_CLOR_CODE)
        WIN.blit(DRAW_TEXT, (WIDTH//2 - DRAW_TEXT.get_width()//2, HEIGHT//2 - DRAW_TEXT.get_height()//2))
        pygame.display.update()
        pygame.time.delay(5000)

def main():

    RED = pygame.Rect(700,300, SPACEFHIP_WIDTH, SPACESHIP_HEIGHT) # WE ARE MAKING A RECTANGLE TO KEEP TRACK OF THE X,Y COORDINATE OF SPACESHIP 
    YELLOW = pygame.Rect(100,300, SPACEFHIP_WIDTH, SPACESHIP_HEIGHT)

    RED_BULLETS = []
    YELLOW_BULLETS = []

    RED_HEALTH = 20
    YELLOW_HEALTH = 20

    # game loop
    clock = pygame.time.Clock() # controls the speed of the while loop
    run = True
    
    while run: # when run becomes false the game ends
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(YELLOW_BULLETS) < MAX_BULLETS:
                        BULLET = pygame.Rect(YELLOW.x + YELLOW.width, YELLOW.y + YELLOW.height//2 - 2, 10, 5)
                        YELLOW_BULLETS.append(BULLET)
                        BULLET_FIRED_SOUND.play()

                if event.key == pygame.K_RCTRL and len(RED_BULLETS) < MAX_BULLETS:
                        BULLET = pygame.Rect(RED.x, RED.y + RED.height//2 - 2, 10, 5)
                        RED_BULLETS.append(BULLET)
                        BULLET_FIRED_SOUND.play()

            if event.type == RED_HIT:
                RED_HEALTH -= 1
                BULLET_HIT_SOUND.play()

            if event.type == YELLOW_HIT:
                YELLOW_HEALTH -= 1
                BULLET_HIT_SOUND.play()

        winner_text = ""
        if RED_HEALTH <= 0:
                winner_text = "YELLOW WINS!"

        if YELLOW_HEALTH <= 0:
                winner_text = "RED WINS!"

        if winner_text != "":
                draw_winner(winner_text)
                break

        KEYS_PRESSED = pygame.key.get_pressed() # EVERY SINGLE TIME THE WHILE LOOP IS RUNNING, IT GONNA TELL US WHAT KEY ARE CURRENTLY BEING PRESSED DOWN
        yellow_movement_keys(KEYS_PRESSED, YELLOW)
        red_movement_keys(KEYS_PRESSED, RED)
        
        control_bullets(YELLOW_BULLETS, RED_BULLETS, YELLOW, RED)
        draw_window(RED, YELLOW, RED_BULLETS, YELLOW_BULLETS, RED_HEALTH, YELLOW_HEALTH)
        

    main()

if __name__ =="__main__":
    main()