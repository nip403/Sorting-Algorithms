import pygame
import math
import sys

class Display:
    def __init__(self,bar_thickness,windowsize,surface,font):
        self.base_colour = (255,255,255)
        self.sorting_colour = (255,0,0)
        self.done_colour = (0,255,0)
        
        self.thickness = bar_thickness
        self.s = windowsize
        self.surface = surface
        self.font = font

        self.green = []

    def add_green(self,arr,replace=True):
        if replace:
            self.green = arr
        else:
            self.green = list(set(self.green+arr))

    def draw(self,array,*highlighted,background=(0,0,0)):
        self.surface.fill(background)

        for index,item in enumerate(array):
            if self.bars: 
                if index in highlighted:
                    pygame.draw.rect(self.surface,self.sorting_colour,(index*self.thickness,math.ceil(self.s[1]-(item/len(array)*self.s[1])),self.thickness,math.ceil(item/len(array)*self.s[1])),0)
                elif index in self.green:
                    pygame.draw.rect(self.surface,self.done_colour,(index*self.thickness,math.ceil(self.s[1]-(item/len(array)*self.s[1])),self.thickness,math.ceil(item/len(array)*self.s[1])),0)
                else:
                    pygame.draw.rect(self.surface,self.base_colour,(index*self.thickness,math.ceil(self.s[1]-(item/len(array)*self.s[1])),self.thickness,math.ceil(item/len(array)*self.s[1])),0)

            else:
                if index in highlighted:
                    pygame.draw.circle(self.surface,self.sorting_colour if not index in highlighted else self.sorting_colour,list(map(int,(index*self.thickness,self.s[1]-(item/len(array)*self.s[1])))),1,0)
                elif index in self.green:
                    pygame.draw.circle(self.surface,self.done_colour if not index in highlighted else self.sorting_colour,list(map(int,(index*self.thickness,self.s[1]-(item/len(array)*self.s[1])))),1,0)
                else:
                    pygame.draw.circle(self.surface,self.base_colour if not index in highlighted else self.sorting_colour,list(map(int,(index*self.thickness,self.s[1]-(item/len(array)*self.s[1])))),1,0)
                   
    def draw_other(self,accesses,comparisons):
        a = self.font.render(f"Array Accesses: {accesses}",True,(255,0,0))
        c = self.font.render(f"Array Comparisions: {comparisons}",True,(255,0,0))

        self.surface.blit(a,a.get_rect(topleft=[10,10]))
        self.surface.blit(c,c.get_rect(topleft=[10,30]))

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
