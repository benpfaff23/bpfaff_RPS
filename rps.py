# File created by: Ben Pfaff

# Libraries; outside python code to be used for this specific code
from time import sleep
from random import randint
import pygame as pg
import os

# Accesses the game folder
game_folder = os.path.dirname(__file__)
print(game_folder)

# Sets the width, height, and frames per second for the pygame window
WIDTH = 860
HEIGHT = 680
FPS = 30

# Defines the colors; colors defined by Red/Green/Blue values with 255 = white and 0 = black
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# List of three strings
# List because of brackets; Tuple uses parenthesis
# Tuples can't be changed; Lists can be changed
objects = ["rock", "paper", "scissors"]

# defines the function start screen, which dislays the images on black background at the start
def start_screen():
    screen.fill(BLACK)
    screen.blit(rock_image, rock_image_rect)
    screen.blit(paper_image, paper_image_rect)
    screen.blit(scissors_image, scissors_image_rect)
    pg.display.flip()


# defines the function win screen, which shows the winning image after the game and determines its coordinates
def win_screen():
    screen.blit(win_image, win_image_rect)
    win_image_rect.x = 325
    win_image_rect.y = 400
    pg.display.flip()

# defines the function tie screen, which shows the tie image after the game and determines its coordinates
def tie_screen():
    screen.blit(tie_image, tie_image_rect)
    tie_image_rect.x = 400
    tie_image_rect.y = 400
    pg.display.flip()

# defines the function lose screen, which shows the losing image after the game and determines its coordinates
def lose_screen():
    screen.blit(lose_image, lose_image_rect)
    lose_image_rect.x = 300
    lose_image_rect.y = 400
    pg.display.flip()

# defines the function restart button, which displays the restart image
# I couldn't get the restart button to work properly, but when you press the same image as chosen previously, the computer chooses a new image
def restart_button():
    screen.blit(restart_image, restart_image_rect)
    restart_image_rect.x = 5
    restart_image_rect.y = 475
    pg.display.flip()

# defines the randchoice function which allows the computer to choose randomly between the 3 parts of the choice variable 
def cpu_randchoice():
    choice = objects[randint(0, 2)]
    print("The computer chose " + choice)
    return choice

# defines the cpu rock function, which displays the image of the rock as the computers selection
def cpu_rock():
    screen.blit(cpu_rock_image, cpu_rock_image_rect)
    cpu_rock_image_rect.x = 500
    cpu_rock_image_rect.y = 50
    pg.display.flip()

# defines the cpu paper function, which displays the image of the paper as the computers selection
def cpu_paper():
    screen.blit(cpu_paper_image, cpu_paper_image_rect)
    cpu_paper_image_rect.x = 500
    cpu_paper_image_rect.y = 150
    pg.display.flip()

# defines the cpu scissors function, which displays the image of the scissors as the computers selection
def cpu_scissors():
    screen.blit(cpu_scissors_image, cpu_scissors_image_rect)
    cpu_scissors_image_rect.x = 500
    cpu_scissors_image_rect.y = 150
    pg.display.flip()

# defines the player rock function, which displays the rock image as the players selection, it determines the coordinates of all the images when rock is selected
def player_rock():
    screen.blit(rock_image, rock_image_rect)
    rock_image_rect.x = 150
    rock_image_rect.y = 50
    paper_image_rect.x = -500
    scissors_image_rect.x = -500
    pg.display.flip

# defines the player scissors function, which displays the scissors image as the players selection, it determines the coordinates of all the images when scissors is selected
def player_scissors():
    screen.blit(scissors_image, scissors_image_rect)
    scissors_image_rect.x = 250
    scissors_image_rect.y = 150
    rock_image_rect.x = -500
    paper_image_rect.x = -500
    pg.display.flip

# defines the player paper function, which displays the paper image as the players selection, it determines the coordinates of all the images when paper is selected
def player_paper():
    screen.blit(paper_image, paper_image_rect)
    paper_image_rect.x = 250
    paper_image_rect.y = 150
    scissors_image_rect.x = -500
    rock_image_rect.x = -500
    pg.display.flip


# "init" initializes the pygame modules, allows for everything to start running
pg.init()

# "screen" is defined with the Width and Height
# "set_caption" displays text in the window bar
# "time.clock" tracks amount of time
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Rock, Paper, Scissors")
clock = pg.time.Clock()

# variable that uses the you win image from the folder, also determines location of image, get rect allows image to work in pygame
win_image = pg.image.load(os.path.join(
    game_folder, 'youwin.png')).convert()
win_image_rect = win_image.get_rect()
win_image_rect.x = -2050

# variable that uses the you lose image from the folder, also determines location of image, get rect allows image to work in pygame
lose_image = pg.image.load(os.path.join(
    game_folder, 'youlose.png')).convert()
lose_image_rect = lose_image.get_rect()
lose_image_rect.x = -2050

# variable that uses the tie image from the folder, also determines location of image, get rect allows image to work in pygame
tie_image = pg.image.load(os.path.join(
    game_folder, 'tie.png')).convert()
tie_image_rect = tie_image.get_rect()
tie_image_rect.x = -2050

# variable that uses the reset image from the folder, also determines location of image, get rect allows image to work in pygame
restart_image = pg.image.load(os.path.join(
    game_folder, 'restart.png')).convert()
restart_image_rect = restart_image.get_rect()
restart_image_rect.x = -2050


# variable that uses the rock image from the folder, also determines location of image, get rect allows image to work in pygame
rock_image = pg.image.load(os.path.join(game_folder, 'rock.jpg')).convert()
rock_image_rect = rock_image.get_rect()
rock_image_rect.x = (10)
rock_image_rect.y = (10)

# variable that uses the scissors image from the folder, also determines location of image, get rect allows image to work in pygame
scissors_image = pg.image.load(os.path.join(
    game_folder, 'scissors.jpg')).convert()
scissors_image_rect = scissors_image.get_rect()
scissors_image_rect.x = (0)
scissors_image_rect.y = (400)

# variable that uses the paper image from the folder, also determines location of image, get rect allows image to work in pygame
paper_image = pg.image.load(os.path.join(game_folder, 'paper.jpg')).convert()
paper_image_rect = paper_image.get_rect()
paper_image_rect.x = (250)
paper_image_rect.y = (400)

# variable that also uses rock image from folder, as well as determining location, and allowing image to work in pygame
cpu_rock_image = pg.image.load(os.path.join(
    game_folder, 'rock.jpg')).convert()
cpu_rock_image_rect = cpu_rock_image.get_rect()
cpu_rock_image_rect.x = -500
cpu_rock_image_rect.y = -500

# variable that also uses scissors image from folder, as well as determining location, and allowing image to work in pygame
cpu_scissors_image = pg.image.load(os.path.join(
    game_folder, 'scissors.jpg')).convert()
cpu_scissors_image_rect = cpu_scissors_image.get_rect()
cpu_scissors_image_rect.x = -600
cpu_scissors_image_rect.y = -600

# variable that also uses paper image from folder, as well as determining location, and allowing image to work in pygame
cpu_paper_image = pg.image.load(
    os.path.join(game_folder, 'paper.jpg')).convert()
cpu_paper_image_rect = cpu_paper_image.get_rect()
cpu_paper_image_rect.x = -700
cpu_paper_image_rect.y = -700

# "running" is the pygame engine displaying its function
# "player_choice" is a variable, the option that the user chooses
# "cpu_choice" is a variable, the option the computer chooses
running = True
player_choice = ""
cpu_choice = ""

# while loop keeps the program running forever, for keeps the program running for a certain amount of time
# if statement says if the mouse clicks on the rock, paper, or scissors image, then the function below it will occur, and the variables will be true
# elif statement says if the above if statement doesn't occur, then another alternate statement could happen 
# else says if none of the above happens, then it will print "you chose nothing"
while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONUP:
            mouse_coords = pg.mouse.get_pos()
            if rock_image_rect.collidepoint(mouse_coords):
                print("You chose rock")
                player_choice = "rock"
                cpu_choice = cpu_randchoice()
            elif paper_image_rect.collidepoint(mouse_coords):
                print("You chose paper")
                player_choice = "paper"
                cpu_choice = cpu_randchoice()
            elif scissors_image_rect.collidepoint(mouse_coords):
                print("You chose scissors")
                player_choice = "scissors"
                cpu_choice = cpu_randchoice()
            else:
                print("You chose nothing")

# start screen function
    start_screen()

# "if" statement: if the player chooses rock, and the cpu chooses rock, then the functions cpu_rock, player_rock, tie_screen, and restart_button will run
# the same applies for the rest, if the two certain variables are chosen, then the corresponding functions will runs 
    if player_choice == "rock":
        if cpu_choice == "rock":
            cpu_rock()
            player_rock()
            tie_screen()
            restart_button()
        if cpu_choice == "paper":
            cpu_paper()
            player_rock()
            lose_screen()
            restart_button()
        if cpu_choice == "scissors":
            cpu_scissors()
            player_rock()
            win_screen()
            restart_button()
    if player_choice == "paper":
        if cpu_choice == "rock":
            cpu_rock()
            player_paper()
            win_screen()
            restart_button()
        if cpu_choice == "paper":
            cpu_paper()
            player_paper()
            tie_screen()
            restart_button()
        if cpu_choice == "scissors":
            cpu_scissors()
            player_paper()
            lose_screen()
            restart_button()
    if player_choice == "scissors":
        if cpu_choice == "rock":
            cpu_rock()
            player_scissors()
            lose_screen()
            restart_button()
        if cpu_choice == "paper":
            cpu_paper()
            player_scissors()
            win_screen()
            restart_button()
        if cpu_choice == "scissors":
            cpu_scissors()
            player_scissors()
            tie_screen()
            restart_button()

# pygame stops running and exits
pg.quit
