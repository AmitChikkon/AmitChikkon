import pygame #first i'll import the libraries
pygame.init() #i'll initiate the pygame

window_x=1000 #i'll setup the window size
window_y=700
window = pygame.display.set_mode((window_x,window_y)) #after setting up the window we will display it
pygame.display.set_caption("Game_development") # then give the caption for window as game development

icon = pygame.image.load("icon.png") #then load the icon or image

pygame.display.set_icon(icon) #then display the image


spaceship = pygame.image.load("icon.png")
spaceship_x=500
spaceship_y=300
bg=pygame.image.load("Background.jpg")

def display_spaceship(x,y):
    window.blit(spaceship,(x,y)) #help to add up an image to window
    
game = True
while game:
    window.blit(bg,(0,0))
    for even in pygame.event.get():
        if even.type == pygame.QUIT:
            game = False
    keys = pygame.key.get_pressed() #we declare the keys that we press
    #if left arrow key is pressed
    if keys[pygame.K_LEFT] and spaceship_x > 10: #we are able to move the spaceship ,we declare the condition stop if the limit of window exceeding.
        spaceship_x -= 1
    if keys[pygame.K_RIGHT] and spaceship_x < 700:
        spaceship_x += 1
    if keys[pygame.K_UP]:
        spaceship_y -=1
    if keys[pygame.K_DOWN]:
        spaceship_y += 1
        
    display_spaceship(spaceship_x,spaceship_y)
    pygame.display.update()
pygame.quit()

