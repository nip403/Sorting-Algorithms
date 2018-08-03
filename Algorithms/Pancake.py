import pygame

class Pancake:
    def __init__(self,array,displayObject,clock,fps):
        self.array = array
        self.display = displayObject
        self.clock = clock
        self.fps = fps
        self.accesses = 0
        self.comparisons = 0

    def main(self):
        for pan in range(len(self.array),1,-1):
            self.clock.tick(self.fps)
            big = max(range(pan),key=self.array.__getitem__)

            if not big + 1 == pan:
                if not big == 0:
                    self.array[:big+1] = self.array[:big+1][::-1]
                self.array[:pan] = self.array[:pan][::-1]

            self.display.events()
            self.display.add_green([self.array.index(i) for i in self.array[pan:]])
            self.display.draw(self.array,*range(pan))
            self.display.draw_other(self.accesses,self.comparisons)

            pygame.display.flip()
