import pygame

class Comb:
    def __init__(self,array,displayObject,clock,fps,arr_length):
        self.array = array
        self.display = displayObject
        self.clock = clock
        self.fps = fps
        self.accesses = 0
        self.comparisons = 0

    def main(self):
        gap = len(self.array)
        shrink = 1.2

        while True:
            done = True
            gap //= shrink

            if gap > 1:
                done = False
            elif gap < 1:
                gap = 1

            for i in range(int(len(self.array)-gap)):
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

            
                    
