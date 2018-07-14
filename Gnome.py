import pygame

class Gnome:
    def __init__(self,displayObject,array,fps,arr_length,accesses,comparisons,clock):
        self.display = displayObject
        self.array = array
        self.fps = fps
        self.length = arr_length
        self.accesses = accesses
        self.comparisons = comparisons
        self.clock = clock

    def main(self):
        for p in range(1,self.length):
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
                
