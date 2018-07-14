import pygame
import random

class Bogo:
    def __init__(self,displayObject,array,fps,arr_length,accesses,comparisons,clock):
        self.display = displayObject
        self.array = array
        self.fps = fps
        self.length = arr_length
        self.accesses = accesses
        self.comparisons = comparisons
        self.clock = clock

    def main(self):
        check = lambda arr,acc,com: [all([arr[i+1] > arr[i] for i in range(len(arr)-1)]),2*self.length+acc,self.length+com]

        while True:
            state,self.accesses,self.comparisons = check(self.array,self.accesses,self.comparisons)

            if state:
                break

            self.clock.tick(self.fps)
            random.shuffle(self.array)

            self.display.events()
            self.display.draw(self.array)
            self.display.draw_other(self.accesses,self.comparisons)

            pygame.display.flip()
