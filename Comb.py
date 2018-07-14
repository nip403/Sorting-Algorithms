import pygame

class Comb:
    def __init__(self,displayObject,array,fps,arr_length,accesses,comparisons,clock):
        self.display = displayObject
        self.array = array
        self.fps = fps
        self.length = arr_length
        self.accesses = accesses
        self.comparisons = comparisons
        self.clock = clock

    def main(self):
        gap = self.length
        shrink = 1.2

        while True:
            done = True
            gap //= shrink

            if gap > 1:
                done = False
            elif gap < 1:
                gap = 1

            for i in range(int(self.length-gap)):
                self.clock.tick(self.fps)
                
                if self.array[i] > self.array[int(i+gap)]:
                    self.array[i],self.array[int(i+gap)] = self.array[int(i+gap)],self.array[i]
                    done = False
                self.accesses += 6
                self.comparisons += 1

                self.display.events()
                self.display.draw(self.array,i,i+gap)
                self.display.draw_other(self.accesses,self.comparisons)

                pygame.display.flip()

            if done:
                return

            
                    
