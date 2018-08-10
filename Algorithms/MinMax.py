import pygame
import itertools
import sys

class MinMax:
    def __init__(self,array,displayObject,clock,fps):
        self.array = array
        self.display = displayObject
        self.clock = clock
        self.fps = fps
        self.accesses = 0
        self.comparisons = 0

    def main(self):
        small_end = []
        large_end = []
        
        while len(self.array) > 1:
            self.clock.tick(self.fps)
            self.accesses += 1
            self.comparisons += 1
            
            smallest = 0
            largest = 0

            for p,i in enumerate(self.array):
                self.accesses += 3
                self.comparisons += 2
                
                if self.array[smallest] > i:
                    smallest = p
                if self.array[largest] < i:
                    largest = p

                self.display.events()
                self.display.add_green(list(itertools.chain(range(len(small_end)),range(len(small_end+self.array+large_end)-1,len(small_end+self.array)-1,-1))))
                self.display.draw(small_end+self.array+large_end,smallest+len(small_end),largest+len(small_end),p+len(small_end))
                self.display.draw_other(self.accesses,self.comparisons)

                pygame.display.flip()

            self.accesses += len(self.array) + 2
            self.comparisons += len(self.array)
            
            small_end.append(self.array[smallest])
            large_end.insert(0,self.array[largest])
            self.array = [i for p,i in enumerate(self.array) if not p in [smallest,largest]]

        self.display.add_green(range(len(small_end+self.array+large_end)))
        self.display.draw(small_end+self.array+large_end)
        self.display.draw_other(self.accesses,self.comparisons)

        pygame.display.flip()
