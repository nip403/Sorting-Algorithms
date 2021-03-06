import pygame

class Pancake:
    def __init__(self, array, displayObject, clock, fps):
        self.array = array
        self.display = displayObject
        self.clock = clock
        self.fps = fps
        self.accesses = 0
        self.comparisons = 0

    def main(self):
        self.accesses += 1
        
        for pan in range(len(self.array), 1, -1):
            self.clock.tick(self.fps)

            self.accesses += 1
            self.comparisons += 1
            big = max(range(pan), key=self.array.__getitem__)
            
            if not big + 1 == pan:
                self.accesses += 2
                self.comparisons += 1
        
                if not big == 0:
                    self.accesses += 2
                    self.array[:big+1] = reversed(self.array[:big+1])
                    
                self.array[:pan] = reversed(self.array[:pan])

            self.display.events()
            self.display.add_green([self.array.index(pan-1)], False)
            self.display.draw(self.array, *range(pan))
            self.display.draw_other(self.accesses, self.comparisons)

            pygame.display.flip()
