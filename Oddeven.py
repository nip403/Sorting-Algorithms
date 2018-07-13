import pygame

class Oddeven:
    def __init__(self,displayObject,array,fps,arr_length,accesses,comparisons,clock):
        self.display = displayObject
        self.array = array
        self.fps = fps
        self.length = arr_length
        self.accesses = accesses
        self.comparisons = comparisons
        self.clock = clock

    def main(self):
        while True:
            done = True

            for e in reversed(range(2)):
                for i in range(e,self.length-1,2):
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
