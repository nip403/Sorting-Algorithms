import pygame

class Gnome:
    def __init__(self,array,displayObject,clock,fps,arr_length):
        self.array = array
        self.display = displayObject
        self.clock = clock
        self.fps = fps
        self.accesses = 0
        self.comparisons = 0

    def main(self):
        for p in range(1,len(self.array)):
            while p > 0 and self.array[p-1] > self.array[p]:
                self.clock.tick(self.fps)
                
                self.array[p],self.array[p-1] = self.array[p-1],self.array[p]
                p -= 1
                self.accesses += 6
                self.comparisons += 2

                self.display.events()
                self.display.draw(self.array,p,p-1)
                self.display.draw_other(self.accesses,self.comparisons)

                pygame.display.flip()
