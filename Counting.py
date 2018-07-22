import pygame

class Counting:
    def __init__(self,array,displayObject,clock,fps):
        self.array = array
        self.display = displayObject
        self.clock = clock
        self.fps = fps
        self.accesses = 0
        self.comparisons = 0

    def main(self):
        count = [0] * len(self.array)
       
        for i in range(0,len(self.array)):
            count[self.array[i]] += 1
            self.accesses += 2

        for i in range(1,len(count)):
            count[i] += count[i - 1]
            self.accesses += 2

        output = [0] * len(self.array)
        self.accesses += 5

        for i in range(len(self.array)):
            self.clock.tick(self.fps)
            
            output[count[self.array[i]] - 1] = self.array[i]
            count[self.array[i]] -= 1
            self.accesses += 6 + len(self.array)

            self.display.events()
            drawable = [output[i] if output[i] else self.array[i] for i in range(len(self.array))]
            self.display.draw(drawable,self.array[i],count[self.array[i]])
            self.display.draw_other(self.accesses,self.comparisons)

            pygame.display.flip()
