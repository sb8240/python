'''
pygame.Rect(x,y,width,height) -> new rectangle
surface.get_rect(pos) -> rectangle around surface
pygame.draw.rect(surface, color, rect)
pygame.KEYDOWN -> this is going to be triggered whenever we press a key
'''

import pygame, sys, random
from pygame.math import Vector2

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init() 

CELL_SIZE = 40
CELL_NUMBER = 20

FPS = 60

# BLUE_COLOR = (0,0,255) # RGB tuple
SCREEN_COLOR = (175,215,70)

screen = pygame.display.set_mode((CELL_SIZE * CELL_NUMBER, CELL_SIZE * CELL_NUMBER))
pygame.display.set_caption("snake@souro")
clock = pygame.time.Clock() # going to create a clock object in pygame
APPLE_IMAGE = pygame.image.load("apple.png").convert_alpha()
GAME_FONT = pygame.font.Font('PoetsenOne-Regular.ttf', 20)
# test_surface = pygame.Surface((100,200)) # the arguments are width and height
# test_surface.fill((BLUE_COLOR))

SCREEN_UPDATE = pygame.USEREVENT # custom event that we could trigger by timmer
pygame.time.set_timer(SCREEN_UPDATE, 150) # timmer; 150 is in miliseconds

class Snake:

    def __init__(self) -> None:
        
        self.body = [Vector2(7,10),Vector2(6,10),Vector2(5,10)]
        self.direction = Vector2(0,0)
        self.add_new_body = False

        self.head_up = pygame.image.load('head_up.png').convert_alpha()
        self.head_down = pygame.image.load('head_down.png').convert_alpha()
        self.head_right = pygame.image.load('head_right.png').convert_alpha()
        self.head_left = pygame.image.load('head_left.png').convert_alpha()
		
        self.tail_up = pygame.image.load('tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('tail_left.png').convert_alpha()
        
        self.body_vertical = pygame.image.load('body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('body_horizontal.png').convert_alpha()
        
        self.body_tr = pygame.image.load('body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('body_bl.png').convert_alpha()
        self.crunch_sound = pygame.mixer.Sound('crunch.wav')

    def draw_snake(self):

        self.update_head_graphics()
        self.update_tail_graphics()

        # for block in self.body:
        #     x_pos = block.x * CELL_SIZE
        #     y_pos = block.y * CELL_SIZE
        #     snake_rect = pygame.Rect(x_pos, y_pos, CELL_SIZE, CELL_SIZE )
        #     pygame.draw.rect(screen, (183, 111, 122), snake_rect)

        for index, block in enumerate(self.body):

            #1. we still need a rect for the positioning
            x_pos = int(block.x * CELL_SIZE)
            y_pos = int(block.y * CELL_SIZE)
            block_rect = pygame.Rect(x_pos, y_pos, CELL_SIZE, CELL_SIZE)

            #2. what direction is the snake heading
            if index == 0:
                screen.blit(self.head, block_rect)

            elif index == len(self.body) - 1:
                screen.blit(self.tail, block_rect)

            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical,block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal,block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl,block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl,block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr,block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br,block_rect)
            # else:
            #     pygame.draw.rect(screen, (150, 100, 100), block_rect)

    def update_head_graphics(self):

        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1,0): self.head = self.head_left
        elif head_relation == Vector2(-1,0): self.head = self.head_right
        elif head_relation == Vector2(0,-1): self.head = self.head_down
        elif head_relation == Vector2(0,1): self.head = self.head_up

    def update_tail_graphics(self):

        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1,0): self.tail = self.tail_left
        elif tail_relation == Vector2(-1,0): self.tail = self.tail_right
        elif tail_relation == Vector2(0,-1): self.tail = self.tail_down
        elif tail_relation == Vector2(0,1): self.tail = self.tail_up

    def snake_move(self):

        if self.add_new_body == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.add_new_body = False

        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
    
    def add_body(self):

        self.add_new_body = True

    def play_sound(self):

        self.crunch_sound.play()

    def reset(self):

        self.body = [Vector2(7,10),Vector2(6,10),Vector2(5,10)]
        self.direction = Vector2(0,0)
        
class Fruit:

    def __init__(self) -> None:

        self.randomize()

    def draw_fruit(self):

        # create a rectangle and then draw a rectangle
        fruit_rect = pygame.Rect(self.pos.x * CELL_SIZE, self.pos.y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        # pygame.draw.rect(screen, (126,166,114), fruit_rect)
        screen.blit(APPLE_IMAGE, fruit_rect)

    def randomize(self):

        self.x = random.randint(0, CELL_NUMBER - 1)
        self.y = random.randint(0, CELL_NUMBER - 1) 
        self.pos = Vector2(self.x, self.y) 
        
class Main:
    
    def __init__(self) -> None:

        self.snake = Snake()
        self.fruit = Fruit()
    
    def update(self):

        self.snake.snake_move()
        self.check_collision()
        self.check_lose()

    def draw_elements(self):

        self.draw_grass()
        self.snake.draw_snake()
        self.fruit.draw_fruit()
        self.draw_score()

    def check_collision(self):

        if self.fruit.pos == self.snake.body[0]:
            # 1) reposition the snake
            # 2) add another block to the snake
            self.fruit.randomize()
            self.snake.add_body()
            self.snake.play_sound()

            for block in self.snake.body[1:]:
                if block == self.fruit.pos:
                    self.fruit.randomize()
    
    def check_lose(self):

        if not 0 <= self.snake.body[0].x < CELL_NUMBER or not 0 <= self.snake.body[0].y < CELL_NUMBER:
            self.game_over()
        
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):

        self.snake.reset()

    def draw_grass(self):

        grass_color = (167, 209, 61)

        for row in range(CELL_NUMBER):
            if row % 2 == 0:
                for col in range(CELL_NUMBER):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                        pygame.draw.rect(screen, grass_color, grass_rect)

            else:
                for col in range(CELL_NUMBER):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                        pygame.draw.rect(screen, grass_color, grass_rect)

    def draw_score(self):

        score_text = str(len(self.snake.body) - 3)
        score_surface = GAME_FONT.render(score_text, True, (56, 74, 12))
        score_x = int(CELL_SIZE * CELL_NUMBER - 50)
        score_y = int(CELL_SIZE * CELL_NUMBER - 30)
        score_rect = score_surface.get_rect(center = (score_x, score_y))
        apple_rect = APPLE_IMAGE.get_rect(midright = (score_rect.left, score_rect.centery))

        screen.blit(score_surface, score_rect)
        screen.blit(APPLE_IMAGE, apple_rect)

def main():

    main_game = Main()
    run = True

    while run: 
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # closing the window by pressing the x button
                run = False
                pygame.quit()
                sys.exit()
            
            if event.type == SCREEN_UPDATE:
                main_game.update()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if main_game.snake.direction.y != 1:
                        main_game.snake.direction = Vector2(0, -1)
                
                if event.key == pygame.K_RIGHT:
                    if main_game.snake.direction.x != -1:
                        main_game.snake.direction = Vector2(1, 0)
                
                if event.key == pygame.K_DOWN:
                    if main_game.snake.direction.y != -1:
                        main_game.snake.direction = Vector2(0, 1)
                
                if event.key == pygame.K_LEFT:
                    if main_game.snake.direction.x != 1:
                        main_game.snake.direction = Vector2(-1, 0)

        
        screen.fill(SCREEN_COLOR)
        main_game.draw_elements()
        # screen.blit(test_surface,(200,250))
        pygame.display.update() # draw all our elements
        clock.tick(FPS)
   
if __name__ == "__main__":
    main()