import pygame

class Shell:
    def __init__(self,displayObject,array,fps,arr_length,accesses,comparisons,clock):
        self.display = displayObject
        self.array = array
        self.fps = fps
        self.length = arr_length
        self.accesses = accesses
        self.comparisons = comparisons
        self.clock = clock

    def main(self):
        n = self.length
        gap = n//2

        while gap > 0:
            self.comparisons += 1
            
            for i in range(gap,n):
                self.clock.tick(self.fps)
                tmp = self.array[i]
                self.accesses += 1

                j = i
                while j >= gap and self.array[j-gap] > tmp:
                    self.accesses += 3
                    self.comparisons += 2
                    self.array[j] = self.array[j-gap]
                    j -= gap

                self.array[j] = tmp
                self.accesses += 1

                self.display.events()
                self.display.draw(self.array,j,i,gap,j-gap)
                self.display.draw_other(self.accesses,self.comparisons)

                pygame.display.flip()
            gap //= 2

        
