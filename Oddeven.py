import pygame

class Oddeven:
    def __init__(self,array,displayObject,clock,fps):
        self.array = array
        self.display = displayObject
        self.clock = clock
        self.fps = fps
        self.accesses = 0
        self.comparisons = 0
        
    def main(self):
        while True:
            done = True

            for e in reversed(range(2)):
                for i in range(e,len(self.array)-1,2):
                    self.clock.tick(self.fps)

                    if self.array[i] > self.array[i+1]:
                        self.array[i],self.array[i+1] = self.array[i+1],self.array[i]
                        done = False
                    self.accesses += 6
                    self.comparisons += 1

                    self.display.events()
                    self.display.draw(self.array,i)
                    self.display.draw_other(self.accesses,self.comparisons)

                    pygame.display.flip()

            if done:
                return
