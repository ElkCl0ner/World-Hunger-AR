import pygame
import os.path

file = open('data.txt','r')

pygame.init()
width = 800
height = 800
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
font = pygame.font.SysFont("baskervilleoldface", 32)

counter = 0
while True:
    counter += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stap = True

    line = file.readline()
    
    if not line:
        print("Done")
        break

    inse = line[:-1].split(";")

    screen.fill((255,255,255))
    screen.blit(font.render(inse[0],False,(0,0,0)),(40,20))
    screen.blit(font.render("Population that is food insecure: "+inse[1],False,(0,0,0)),(40,60))
    screen.blit(font.render("Total population: "+inse[2],False,(0,0,0)),(40,100))
    screen.blit(font.render("Percent: "+inse[3],False,(0,0,0)),(40,140))
    '''
    if os.path.isfile('plots/image{}.png'.format(counter)):
        img = pygame.image.load('plots/image{}.png'.format(counter))
        screen.blit(img,(0,180))
    else:
        screen.blit(font.render("No data for undernourished population",False,(255,100,100)),(80,240))
    '''
    line = file.readline()
    if line == "\n":
        screen.blit(font.render("No data for undernourished population",False,(255,100,100)),(80,240))
    
    else:
        file.readline()
        img = pygame.image.load('plots/image{}.png'.format(counter))
        screen.blit(img,(0,180))
    
    clock.tick(10)
    pygame.display.update()

    pygame.image.save(screen,'AR/{}.png'.format(inse[0]))
    
pygame.quit()
