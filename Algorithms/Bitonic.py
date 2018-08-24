import pygame
import math

class Bitonic:
    def __init__(self,array,displayObject,clock,fps):
        self.array = array
        self.display = displayObject
        self.clock = clock
        self.fps = fps
        self.accesses = 0
        self.comparisons = 0

    def sort(self,low,n,direction=True):
        if n > 1:
            m = n//2
            
            self.sort(low,m,not direction)
            self.sort(low+m,n-m,direction)
            self.merge(low,n,direction)

    def merge(self,low,n,direction):
        if n > 1:
            m = 2**(math.floor(math.log2(n-1)))

            for i in range(low,low+n-m):
                self.accesses += 2
                self.comparisons += 2
                
                if direction == (self.array[i]>self.array[i+m]):
                    self.clock.tick(self.fps)
                    self.accesses += 4
                    
                    self.array[i],self.array[i+m] = self.array[i+m],self.array[i]

                    self.display.events()
                    self.display.add_green([p for p,j in enumerate(self.array) if j == sorted(self.array)[p]])
                    self.display.draw(self.array,i,i+m,low,low+n-m)
                    self.display.draw_other(self.accesses,self.comparisons)

                    pygame.display.flip()
                
            self.merge(low,m,direction)
            self.merge(low+m,n-m,direction)

    def main(self):
        self.sort(0,len(self.array),True)
        
