import pgzrun
import random
import time

alien = Actor('dude')
alien.pos = 0, 10

WIDTH = 900
HEIGHT = 600

score = 0
lives = 3
Highscore = 0

Back = ("jetpack_joy")

def draw():
    global Highscore
    global score
    global lives
    global WIDTH
    global HEIGHT
    global Back
    global Back2
    screen.clear()
    screen.blit(Back, (0,0))
    alien.draw()
    screen.draw.text('score: '+str(score),[10,10])
    screen.draw.text('lives: '+str(lives),[10,25])
    screen.draw.text('Highscore: '+str(Highscore),[10,40])
    if score > Highscore:
        Highscore = score
    if lives == 0:
        screen.clear()
        screen.draw.text("game over",[WIDTH/2-21,HEIGHT/2])
        screen.draw.text('press "r" restart',[WIDTH/2-31,200])
        screen.draw.text("Score: "+str(score), [WIDTH/2-10, 250])
        if keyboard.r:
            score = 0
            lives = 3
            draw()

x = 3
y = 5


def update():
    global score
    global x
    global y
    alien.x += x
    alien.y += y
    # time.sleep(1)
    # x = random.randrange(0,900)
    # y = random.randrange(0, 600)
    if alien.y > HEIGHT:
        x = 3
        y = -5
    elif alien.y < 0:
        x = 3
        y = 5
    elif alien.x > WIDTH:
        alien.pos = 0, 10
        x = 3
        y = 5

def on_mouse_down(pos):
    global score
    global lives
    if alien.collidepoint(pos):
        print("Eek!")
        set_alien_hurt()
        score += 1
    elif lives == 0:
        print("game over")
    else:
        print("You missed me!")
        lives -= 1

def set_alien_normal():
    alien.image = 'dude'

def set_alien_hurt():
    alien.image = 'alien_hurt'
    sounds.ovp.play()
    clock.schedule_unique(set_alien_normal, 0.5)

pgzrun.go()