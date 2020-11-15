import pygame
import load_resources as res
from game_action import quit_game
from game_component import text_objects,button
from play_game import game_window
pygame.init()

def game_intro():
    start = True

    while start:
        for event in pygame.event.get():
            if event == pygame.QUIT:
                quit_game()

        res.display_surface.blit(res.start_img, (0, 0))  
        text_objects("Eras Demi ITC", "LETS RACE", 100, res.white, 300, 170)
        text_objects("Eras Demi ITC", "Ready Steady Go", 100, res.red, 600, 600)

        button("GO",res.blue,100,50,310,670,game_window)
        button("Quit",res.red,100,50,650,670,quit_game)

        pygame.display.update()     

if  __name__ == '__main__':
    game_intro()