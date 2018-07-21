import pygame

class Bubble:
    def __init__(self,array,displayObject,clock,fps):
        self.array = array
        self.display = displayObject
        self.clock = clock
        self.fps = fps
        self.accesses = 0
        self.comparisons = 0

    def main(self):
        pos = 0
        lim = len(self.array)-1
        changed = False

        while True:
            self.clock.tick(self.fps)
            
            if pos == lim:
                pos = 0
                lim -= 1
                
                if not changed:
                    return
                
                changed = False
            
            if self.array[pos] > self.array[pos+1]:
                self.array[pos],self.array[pos+1] = self.array[pos+1],self.array[pos]
                changed = True
                
            pos += 1
            self.accesses += 6
            self.comparisons += 1
              
            self.display.events()
            self.display.draw(self.array,pos,lim-1)
            self.display.draw_other(self.accesses,self.comparisons)

            pygame.display.flip()
