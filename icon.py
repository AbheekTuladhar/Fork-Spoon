import pygame, sys                                   
pygame.init()                                           

WIDTH=840                                                
HEIGHT=WIDTH*0.8                                                   
size=(WIDTH,HEIGHT)
surface = pygame.display.set_mode(size)

pygame.display.set_caption("Fork and Spoon Scale Factored")

BLACK    = (0, 0, 0)     
WHITE    = (255, 255, 255)

#Converts the screen into a 25 by 18 grid
xu = WIDTH/25
yu = HEIGHT/18

#Program helper functions:
def drawIcon(x, y, sf):
    drawFork(x, y, sf)
    drawSpoon(sf*11*xu, sf* yu, sf)


def drawFork(x, y, sf):
    ForkWIDTH = WIDTH/3 *sf
    ForkHEIGHT = ForkWIDTH * 14/10
    Fxu = ForkWIDTH / 10
    Fyu = ForkHEIGHT / 14
    pygame.draw.rect(surface, BLACK, [x,         y, 2*Fxu, 6*Fyu], 0)
    pygame.draw.rect(surface, BLACK, [x+(4*Fxu), y, 2*Fxu, 14*Fyu], 0)
    pygame.draw.rect(surface, BLACK, [x+(8*Fxu), y, 2*Fxu, 6*Fyu], 0)
    pygame.draw.rect(surface, BLACK, [x, y+(5*Fyu), 10*Fxu, Fyu], 0)


def drawSpoon(x, y, sf):
    SpoonWIDTH = WIDTH/5 * sf
    SpoonHEIGHT = SpoonWIDTH * 15/6
    Sxu = SpoonWIDTH/6
    Syu = SpoonHEIGHT/15
    pygame.draw.ellipse(surface, BLACK, [x, y, 6*Sxu, 7*Syu], 0)
    pygame.draw.rect(surface, BLACK, [x+(2*Sxu), y+(6*Syu), 2*Sxu, 9*Syu], 0)


# -------- Main Program Loop -----------
def main():
    while True:
        for event in pygame.event.get():
            if ( event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)): #end game
                pygame.quit()                          
                sys.exit()

        surface.fill(WHITE) 
        
        drawIcon(xu, 2*yu, 0.8)
        
        pygame.display.update()                    
        
#----------------------------------------------------------------            
main()