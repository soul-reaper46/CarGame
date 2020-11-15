import pygame
import load_resources as res
from game_component import text_objects,button
from game_action import quit_game
import play_game as pg

def crashed(score):
    #pygame.mixer.music.stop()

    #pygame.mixer.Sound.play(res.crash_sound)

    res.display_surface.blit(res.start_img,(0,0))

    text_objects("Eras Demi ITC","You Crashed!",100,res.red,340,100)
    text_objects("Eras Demi ITC","Final Score:"+str(score),50,res.red,310,200)

    end = True
    while end:
        for event in pygame.event.get():
            if event == pygame.QUIT:
                quit_game()

        button("Retry",res.green,100,50,450,670,pg.game_window)
        button("Quit",res.red,100,50,750,670,quit_game)

        pygame.display.update()