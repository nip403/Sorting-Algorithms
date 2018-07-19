import pygame

class Cocktail:
    def __init__(self,array,displayObject,clock,fps):
        self.array = array
        self.display = displayObject
        self.clock = clock
        self.fps = fps
        self.accesses = 0
        self.comparisons = 0

    def main(self):
        base = 0
        
        for k in range(len(self.array)-1,0,-1):
            swapped = False

            for i in range(k,base,-1):
                self.clock.tick(self.fps)

                if self.array[i] < self.array[i-1]:
                    self.array[i],self.array[i-1] = self.array[i-1],self.array[i]
                    swapped = True
                    
                self.accesses += 6
                self.comparisons += 1

                self.display.events()
                self.display.draw(self.array,k,i,i-1,base)
                self.display.draw_other(self.accesses,self.comparisons)

                pygame.display.flip()

            for i in range(base,k):
                self.clock.tick(self.fps)

                if self.array[i] > self.array[i+1]:
                    self.array[i],self.array[i+1] = self.array[i+1],self.array[i]
                    swapped = True
                    
                self.accesses += 6
                self.comparisons += 1

                self.display.events()
                self.display.draw(self.array,k,i,i-1,base)
                self.display.draw_other(self.accesses,self.comparisons)

                pygame.display.flip()

            base += 1
            if not swapped:
                return
