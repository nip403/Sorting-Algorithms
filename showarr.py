import pygame
import random

class Show_array:
    def __init__(self,length,dimensions):
        self.array = list(range(length))
        random.shuffle(self.array)

        self.surf = pygame.Surface(dimensions)
        self.surf.fill((0,0,0))

        thick = self.surf.get_width()/length

        for p,i in enumerate(self.array):
            pygame.draw.rect(self.surf,(255,255,255),(p*thick,dimensions[1]-(i/len(self.array)*dimensions[1]),thick,i/length*dimensions[1]),0)

    def get_speed_colour(self,length):
        percent = (length/1000*100 if length/1000*100 <= 100 else 100)

        return [255 if (length/1000*100 if length/1000*100 <= 100 else 100) > 50 else int((percent*2)*255/100), 255 if (length/1000*100 if length/1000*100 <= 100 else 100) < 50 else int(255-(percent*2-100)*255/100),0]
        
    def draw(self,surface,topleft,heading,font):
        surface.blit(self.surf,topleft)
        surface.blit(font.render("Length: %s" % len(self.array),True,self.get_speed_colour(len(self.array))),heading)
