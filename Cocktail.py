import pygame

class Cocktail:
    def __init__(self,displayObject,array,fps,arr_length,accesses,comparisons,clock):
        self.display = displayObject
        self.array = array
        self.fps = fps
        self.length = arr_length
        self.accesses = accesses
        self.comparisons = comparisons
        self.clock = clock

    def main(self):
        for k in range(self.length-1,0,-1):
            swapped = False

            for i in range(k,0,-1):
                self.clock.tick(self.fps)

                if self.array[i] < self.array[i-1]:
                    self.array[i],self.array[i-1] = self.array[i-1],self.array[i]
                    swapped = True
                self.accesses += 6
                self.comparisons += 1

                self.display.events()
                self.display.draw(self.array,k,i,i-1)
                self.display.draw_other(self.accesses,self.comparisons)

                pygame.display.flip()

            for i in range(k):
                self.clock.tick(self.fps)

                if self.array[i] > self.array[i+1]:
                    self.array[i],self.array[i+1] = self.array[i+1],self.array[i]
                    swapped = True
                self.accesses += 6
                self.comparisons += 1

                self.display.events()
                self.display.draw(self.array,k,i,i-1)
                self.display.draw_other(self.accesses,self.comparisons)

                pygame.display.flip()

            if not swapped:
                return
