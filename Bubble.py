import pygame

class Bubble:
    def __init__(self,displayObject,array,fps,arr_length,accesses,comparisons,clock):
        self.display = displayObject
        self.array = array
        self.fps = fps
        self.length = arr_length
        self.accesses = accesses
        self.comparisons = comparisons
        self.clock = clock

    def main(self):
        pos = 0
        changed = False

        while not changed:
            self.clock.tick(self.fps)

            try:
                if self.array[pos] > self.array[pos+1]:
                    self.array[pos],self.array[pos+1] = self.array[pos+1],self.array[pos]
                    changed = True
                pos += 1
                accesses += 6
                comparisons += 1
                
            except:
                pos = 0

                if not done:
                    return

                changed = False

            self.display.events()
            self.display.draw(self.array,pos)
            self.display.draw_other(self.accesses,self.comparisons)

            pygame.display.flip()
                

    
