import pygame
import math
import random

class Show_array:
    def __init__(self,length,dimensions,bars,mode=0):
        self.array = self.get_array(length,mode)

        self.surf = pygame.Surface(dimensions)
        self.thick = self.surf.get_width()/length
        self.bars = bars
        self.length = length
        self.dimensions = dimensions

    def get_array(self,length,mode=0):
        arr = list(range(length))
        
        if not mode:
            random.shuffle(arr)
        elif mode == 2:
            arr = arr[::-1]
        elif mode == 3:
            for i in range(length-1):
                if random.randint(0,10) < 8:
                    tmp = random.randint(4,15)
                    try:
                        arr[i],arr[i+tmp] = arr[i+tmp],arr[i]
                    except:
                        pass

        return arr
        
    def get_speed_colour(self,length):
        return [255 if (length/1000*100 if length/1000*100 <= 100 else 100) > 50 else int(((length/1000*100 if length/1000*100 <= 100 else 100)*2)*255/100), 255 if (length/1000*100 if length/1000*100 <= 100 else 100) < 50 else int(255-((length/1000*100 if length/1000*100 <= 100 else 100)*2-100)*255/100),0]
 
    def draw(self,surface,topleft,heading,font):
        self.surf.fill((0,0,0))

        for p,i in enumerate(self.array):
            if self.bars:
                pygame.draw.rect(self.surf,(255,255,255),(p*self.thick,self.dimensions[1]-(i/len(self.array)*self.dimensions[1]),math.ceil(self.thick),math.ceil(i/self.length*self.dimensions[1])),0)
            else:
                pygame.draw.circle(self.surf,(255,255,255),list(map(int,(p*self.thick,self.dimensions[1]-(i/len(self.array)*self.dimensions[1])))),1,0)
        
        surface.blit(self.surf,topleft)
        surface.blit(font.render(f"Length: {len(self.array)}",True,self.get_speed_colour(len(self.array))),heading)
