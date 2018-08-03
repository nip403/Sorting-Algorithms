import pygame

class Shell:
    def __init__(self,array,displayObject,clock,fps):
        self.array = array
        self.display = displayObject
        self.clock = clock
        self.fps = fps
        self.accesses = 0
        self.comparisons = 0

    def main(self):
        self.accesses += 1
        n = len(self.array)
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
                self.display.add_green([p for p,i in enumerate(self.array) if sorted(self.array)[p] == i])
                self.display.draw(self.array,j,i,j-gap)
                self.display.draw_other(self.accesses,self.comparisons)

                pygame.display.flip()
            gap //= 2
