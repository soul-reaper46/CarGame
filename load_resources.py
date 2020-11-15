import pygame

pygame.init()

clock = pygame.time.Clock()

display_width = 1024
display_height = 800

#create window
display_surface = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("This is a car game")

start_img = pygame.image.load("resources/images/example1.jpg")
road_img = pygame.image.load("resources/images/example.png")
car_img = pygame.image.load("resources/images/car1.jpg")
opp1_img = pygame.image.load("resources/images/car1.jpg")
opp2_img = pygame.image.load("resources/images/car1.jpg")
opp3_img = pygame.image.load("resources/images/car1.jpg")

opp_list = [opp1_img, opp2_img, opp3_img]

#pygame.mixer.music.load("resources/sounds/example.mp3")
#pygame.mixer.sound("resources/sounds/example2.mp3")

#colors #rgb
red = (255, 14, 20)
blue = (15, 25, 250)
white = (255 ,255, 255)
black = (0, 0, 0)
green = (0,128,0)