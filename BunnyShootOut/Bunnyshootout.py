#Olayinka Jimba jr.
#Section 1
#Final Project
##############
import sys, pygame, random, pgzrun 
import random
global game_status
global game
WIDTH = 700
HEIGHT = 500
RED = 229, 211, 179
BLUE = 0, 130, 0
#WHITE = 255, 255, 255
SKY = 135, 206, 235
BOX = Rect((((WIDTH//2) + 80), 3), (20, 485))
PLAT = Rect((0, 480), (700, 30))
life1 = Actor("p2")
life2 = Actor("p2")
life3 = Actor("p2")
life1.x = 600
life1.y = 15
life2.x = 640
life2.y = 15
life3.x = 680
life3.y = 15

p2life = [life1,life2,life3]
actors=[]

beam = Actor("bullet")
fired = Actor("fired")
PLAY1 = Actor("p1")
PLAY1.y = HEIGHT - 30
PLAY1.x = (WIDTH//2)-100
PLAY2 = Actor("p2")
PLAY2.y = HEIGHT - 30
PLAY2.x = (WIDTH//2)+100
fired.y = HEIGHT - 40
fired.x = (WIDTH//2)+20
beam.y = HEIGHT - 40
beam.x = (WIDTH//2)+35
game = Actor('start')

game.state = ['start', 'main', 'endscreen1', 'endscreen2']
game_status = game.state[0]

endscreen1=Actor('endscreen1')
endscreen2=Actor('endscreen2')


GRAVITY = 0.3
JUMP_STRENGTH = 6.5
PLAY1.vy = 0
PLAY2.vy = 0

bullets = []

gamestart=1
#This function is just updating the game for everytime there is a user input
# and or event.
run_once = 0
#def win():
    #screen.blit('youwon',(0,0))

        #clock.schedule(fire_bullet_func,1.5)
def draw_game1():
    screen.draw('endgame1')
    #screen.blit('press-enter2', (300, 400))
def draw_time():
    screen.draw.text(str(game_timer),(0,30), color="black")
def draw_intruct():
    screen.draw.text(str("Player 2, Dodge the bullets for 30 seconds using the W,A,D keys to win!"),(80,250), color="black")
def draw_intruct2():
    screen.draw.text(str("Player 1, Shoot Player 2 three times using spacebar and move with the arrow keys!"),(30,220), color="black")
def draw_credit():
    screen.draw.text(str(" Game Developed by Olayinka"),(30,500), color="black")
def endgame():
    screen.blit("endscreen1", (0,0))
    game_status = game.state[2]
    if game_status == game.state[2]:
        endscreen1.draw()
def draw_game_won():
    #clock.schedule(win, 3.0)
    screen.blit('youwon',(0,0))
    
def update_PLAY1():
    uy = PLAY1.vy
    PLAY1.vy += GRAVITY
    PLAY1.y += (uy + PLAY1.vy)/ 2

    if PLAY1.colliderect(PLAT):
        PLAY1.y = PLAT.y -18
        if PLAY1.vy > -3:
            PLAY1.image = 'p1'

def update_PLAY2():
    uy = PLAY2.vy
    PLAY2.vy += GRAVITY
    PLAY2.y += (uy + PLAY2.vy)/ 2

    if PLAY2.colliderect(PLAT):
        PLAY2.y = PLAT.y -18
        if PLAY2.vy > -3:
            PLAY2.image = 'p2'

def draw_main_menu():
    if game_status == game.state[0]:
        screen.blit('start', (0,0))


def main_loop():
    global game_status
    if game_status == game.state[1]:
        draw_game()
        if keyboard.rshift or keyboard.lshift:
            sys.exit()
            
        if keyboard.left:
            PLAY1.x -=3
            if PLAY1.x <= 5:
                PLAY1.x = 5 
        elif keyboard.right:
            PLAY1.x +=3
            if PLAY1.x >= 340:
                PLAY1.x = 340
        elif keyboard.a:
            PLAY2.x -=3
            if PLAY2.x <= 380:
                PLAY2.x = 380
        elif keyboard.d:
            PLAY2.x +=3
            if PLAY2.x >= 695:
                PLAY2.x = 695
            
            
        for bullet in bullets:
            bullet.x +=10
        
def draw_game():
    #while game_status == game.state[0]:
    screen.blit("start",(0,0))
    if game_status == game.state[1]:
        screen.fill((229, 211, 179))
 
   
#Background Music is here
game_timer = 30
#game_timer_start = 30
#timer_decrement = 0.2

#Below is where the music is implemented.

if gamestart ==1:
    music.set_volume(1)
    music.play("mainmusic")
    print(music.is_playing("mainmusic"))
    if game_timer <= 0:
        sounds.stop("mainmusic")
    
    
def on_key_down(key):
    global game_status
    if game_status == game.state[0]:
        if key==keys.RETURN:
            game_status = game.state[1]
    if game_status == game.state[1]:
        
        if key==keys.SPACE:
            bullets.append(Actor("bullet"))
            sounds.shoot.play()
            bullets[-1].x = PLAY1.x + 13
            bullets[-1].y = PLAY1.y + 5
        if key==keys.UP:
            PLAY1.vy = -JUMP_STRENGTH
        if key==keys.W:
            PLAY2.vy = -JUMP_STRENGTH
            
    if keyboard.rshift or keyboard.lshift:
            #sys.exit()
            # Change the state to be "game"
        #game_status = game.state[0]
    # Exit the program
        sys.exit()
def draw_entities():
    PLAY1.draw()
    PLAY2.draw()
    for life in p2life:
        life.draw()
    #fire_bullet()
    #draw_bullets()
    
    for bullet in bullets:
        if PLAY2.colliderect(bullet):
                sounds.hit.play()
                bullets.remove(bullet)
                p2life.remove(life)
                if p2life:
                    pass
                    #going to implement the game ending here in this else statement
                else:
                    endscreen1.draw()
                    game_status = game.state[2]
                    #clock.schedule_unique(endgame, 1.0)
                    #screen.blit("endscreen1", (0,0))

        bullet.draw()
    screen.draw.filled_rect(PLAT,BLUE)
def update():
    global game_status
    global game_timer
    if game_status == game.state[1]:
        if (game_timer <= 0) and p2life:
            game_status = game.state[3]
            endscreen2.draw()
        else:
            game_timer -= 0.017
        main_loop()
        update_PLAY1()
        update_PLAY2()
    if PLAY1.y >= 500:
        PLAY1.y = 462
    if PLAY2.y >= 500:
        PLAY2.y = 462
    if p2life: 
        pass
    else:
        endscreen1.draw()
        game_status = game.state[2]

def draw():

    screen.clear()
    if game_status == game.state[0]:
        draw_main_menu()
    if game_status == game.state[1]:
        draw_game()
        draw_intruct()
        draw_intruct2()
        draw_time()
        draw_entities()
    if game_status == game.state[2]:
        endscreen1.draw()
    if game_status == game.state[3]:
        endscreen2.draw()

            
pgzrun.go()

 ### IGNORE THIS AND BELOW Setup pygame/window ---------------------------------------- #


