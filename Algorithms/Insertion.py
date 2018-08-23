import pygame

class Insertion:
    def __init__(self,array,displayObject,clock,fps):
        self.array = array
        self.display = displayObject
        self.clock = clock
        self.fps = fps
        self.accesses = 0
        self.comparisons = 0

    def main(self):
        self.accesses += 1
        for i in range(1,len(self.array)):
            j = i-1
            key = self.array[i]
            self.accesses += 1
            
            while j >= 0 and self.array[j] > key:
                self.clock.tick(self.fps)
                
                self.array[j+1] = self.array[j]
                j -= 1
                
                self.accesses += 4
                self.comparisons += 2

                self.display.events()
                self.display.draw(self.array,i,j,j+1)
                self.display.draw_other(self.accesses,self.comparisons)

                pygame.display.flip()

            self.array[j+1] = key
            self.accesses += 1

            self.display.events()
            self.display.add_green([i],False)
            self.display.draw(self.array,i,j,j+1)
            self.display.draw_other(self.accesses,self.comparisons)

            pygame.display.flip()
