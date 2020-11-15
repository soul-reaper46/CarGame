import pygame
import load_resources as res
from game_action import quit_game
import random
from game_component import text_objects
from end_game import crashed

score = 0

def show_score(score):
    text_objects("Arial","Score:"+str(score),30,res.red,100,50)

pygame.init()

def road(y1,y2):
    y1 = y1+5

    if y1 > 0:
        res.display_surface.blit(res.road_img,(0,y1))
        y2 += 5.105
        res.display_surface.blit(res.road_img,(0,y2))

    if y1 > 800:
        y1 = 0
        y2 = -800

    return y1,y2

def opponent(x,y,speed,img):
    global score
    res.display_surface.blit(img,(x,y))
    y += speed

    if y > 800:
        y = -200
        x = random.randrange(0,800)
        img = random.choice(res.opp_list)
        score += 1

    return x,y,img    


def game_window():
    global score
    running = True
    #pygame.mixer.music.play(-1)

    road_y1 = 0
    road_y2 = -800

    car_x = 400
    car_y = 450

    x_change = 0 
    y_change = 0

    opp_x1 = random.randrange(0,1024)
    opp_y1 = -500

    opp_x2 = random.randrange(0,1024)
    opp_y2 = -600

    opp_x3 = random.randrange(0,1024)
    opp_y3 = -700

    img1 = random.choice(res.opp_list)
    img2 = random.choice(res.opp_list)
    img3 = random.choice(res.opp_list)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running  = False
                quit_game()

            if event.type == pygame.KEYDOWN:
                print(event.key)
                if event.key == pygame.K_UP:
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change = 5
                elif event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.type == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                    y_change = 0

        car_x += x_change
        car_y += y_change


        road_y1,road_y2 = road(road_y1,road_y2)

        res.display_surface.blit(res.car_img,(car_x,car_y))

        opp_x1,opp_y1,img1 = opponent(opp_x1,opp_y1,10,img1)
        opp_x2,opp_y2,img2 = opponent(opp_x2,opp_y2,12,img2)
        opp_x3,opp_y3,img3 = opponent(opp_x3,opp_y3,14,img3)

        #res.display_surface.blit(res.road_img,(0,0))


        #crash
        car_width = res.car_img.get_size()[0] #(width,height)
        car_height = res.car_img.get_size()[1]

        opp_width = res.opp1_img.get_size()[0] #(width,height)
        opp_height = res.opp1_img.get_size()[1]

        if car_y < opp_y1 + opp_height:
            if car_x < opp_x1 + opp_width and car_x + car_width > opp_x1:
                crashed(score)
            
        if car_y < opp_y2 + opp_height:
            if car_x < opp_x2 + opp_width and car_x + car_width > opp_x2:
                crashed(score)
            
        if car_y < opp_y1 + opp_height:
            if car_x < opp_x3 + opp_width and car_x + car_width > opp_x3:
                crashed(score)

        if car_x < 0 or car_x > res.display_width or car_y > res.display_height or car_y < 0:
            crashed(score)
        
        show_score(score)

        pygame.display.update()
        res.clock.tick(40)