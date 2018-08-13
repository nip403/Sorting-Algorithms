import pygame
import math
import random

class Show_array:
    def __init__(self,length,dimensions,bars):
        self.array = list(range(length))
        random.shuffle(self.array)

        self.surf = pygame.Surface(dimensions)
        self.thick = self.surf.get_width()/length
        self.bars = bars
        self.length = length
        self.dimensions = dimensions
        
    def get_speed_colour(self,length):
        return [255 if (length/1000*100 if length/1000*100 <= 100 else 100) > 50 else int(((length/1000*100 if length/1000*100 <= 100 else 100)*2)*255/100), 255 if (length/1000*100 if length/1000*100 <= 100 else 100) < 50 else int(255-((length/1000*100 if length/1000*100 <= 100 else 100)*2-100)*255/100),0]
 
    def draw(self,surface,topleft,heading,font):
        self.surf.fill((0,0,0))

        for p,i in enumerate(self.array):
            if self.bars:
                pygame.draw.rect(self.surf,(255,255,255),(p*self.thick,math.ceil(self.dimensions[1]-(i/len(self.array)*self.dimensions[1])),math.ceil(self.thick),math.ceil(i/self.length*self.dimensions[1])),0)
            else:
                pygame.draw.circle(self.surf,(255,255,255),list(map(int,(p*self.thick,self.dimensions[1]-(i/len(self.array)*self.dimensions[1])))),1,0)
        
        surface.blit(self.surf,topleft)
        surface.blit(font.render(f"Length: {len(self.array)}",True,self.get_speed_colour(len(self.array))),heading)
