# File Created by Ben Pfaff

# import libraries 

# important the sleep function that stops the code for a certain number of seconds
from time import sleep 

from random import randint
# import pygame: thorough in game library for use in python
import pygame as pg
# library that allows you to manage files and folders
import os 

game_folder = os.path.dirname(__file__) 

# variables that define the choices in the game
choices0 = ["rock", "paper", "scissors"]

# game settings, capatalized because they cannot change

WIDTH = 500
HEIGHT = 500
FPS = 30


# RGB values
# define colors
# tuples are immutable - cannot change once created
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# makes the gameover always false, the game won't end until we make it end
GAMEOVER = False

# pygame initializer 
pg.init()
pg.mixer.init()

# opens up pygame and describes its location
screen = pg.display.set_mode((WIDTH, HEIGHT))
# sets the name at the top of the display as ...
pg.display.set_caption("Rock, Paper, Scissors...")
# class sets fps
clock = pg.time.Clock()
# loads in the images
paper_image = pg.image.load(os.path.join(game_folder, 'paper.jpg')).convert()
scissors_image = pg.image.load(os.path.join(game_folder, 'scissors.jpg')).convert()
rock_image = pg.image.load(os.path.join(game_folder, 'rock.jpg')).convert()
# stores location and dimensions of pixels, and allows us to change those things
rock_image_rect = rock_image.get_rect()
paper_image_rect = paper_image.get_rect()
scissors_image_rect = scissors_image.get_rect()
# defines the variable as a true statement 
running = True

# determines the location of the images on the x and y axis 
paper_image_rect.x = 250
paper_image_rect.y = 100
scissors_image_rect.y = 200
scissors_image_rect.x = -10

#define the function cpu_randchoice
def cpu_randchoice():
    # global allows for the variable randchoice to be used outside the cpu_randchoice function
    global randchoice
    randchoice = choices0[randint(0,2)].upper()
    return choices0

player_choice = ""
# repeats the function for as long as it runs
while running:
    # sets the frame rate - 30 fps
    clock.tick(FPS)
    # sets up event
    for event in pg.event.get():
        # sets up the variables to be defined
        if event.type == pg.QUIT:
            running = False
        # sets up the events for mouse button input release
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                print("game on!!!!")
                show_rock = True
        if event.type == pg.MOUSEBUTTONUP:
            # displays the coordinates clicked
            mouse_coords = pg.mouse.get_pos()
         #    if pg.mouse.get_pos()[0] <= my_image_rect.width and pg.mouse.get_pos()[1] < my_image_rect.height:
            if rock_image_rect.collidepoint(mouse_coords):
                print("you clicked on rock..")
                player_choice = "rock"
                randchoice = cpu_randchoice()
                # call a function that gets the cpu choice...
            elif paper_image_rect.collidepoint(mouse_coords):
                print("you clicked on paper...")
                player_choice = "paper"
                randchoice = cpu_randchoice()
            elif scissors_image_rect.collidepoint(mouse_coords):
                print("you clicked on scissors...")
                player_choice = "scissors"
                randchoice = "paper"                 
            else:
                print("you didn't click on anythin...")
            
    # get user input
    # HCI - human computer interaction
    # keyboard, mouse, controller
    # update
    # rock_image_rect.x += 0
    # rock_image_rect.y += 1
    screen.fill(BLACK)
    
    # draw
    if player_choice == "":
        screen.blit(scissors_image, scissors_image_rect)
        screen.blit(rock_image, rock_image_rect)
        screen.blit(paper_image, paper_image_rect)
    elif player_choice == "rock" and randchoice == "scissors":
        screen.blit(rock_image, rock_image_rect)
        screen.blit(scissors_image, scissors_image_rect)
    elif player_choice == "paper" and randchoice == "rock":
        screen.blit(paper_image, paper_image_rect)
        screen.blit(rock_image, rock_image_rect)
    elif player_choice == "scissors" and randchoice == "paper":
        screen.blit(scissors_image, scissors_image_rect)
        screen.blit(paper_image, paper_image_rect)
    elif player_choice == "rock" and randchoice == "rock":
        screen.blit(rock_image, rock_image_rect)
    elif player_choice == "scissors" and randchoice == "scissors":
        screen.blit(scissors_image, scissors_image_rect)
    elif player_choice == "paper" and randchoice == "paper":
        screen.blit(paper_image, paper_image_rect)
    else:
        pass

    
    pg.display.flip()

    pg.quit