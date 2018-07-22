import pygame

class Selection:
    def __init__(self,array,displayObject,clock,fps):
        self.array = array
        self.display = displayObject
        self.clock = clock
        self.fps = fps
        self.accesses = 0
        self.comparisons = 0

    def main(self):
        self.accesses += len(self.array)
        for i in range(0,len(self.array)-1):
            min_pos = i
            self.accesses += 1

            self.accesses += len(self.array)
            for j in range(i+1,len(self.array)):
                self.clock.tick(self.fps)
                self.accesses += 1

                if self.array[min_pos] > self.array[j]:
                    min_pos = j
                self.comparisons += 1
                self.accesses += 2

                self.display.events()
                self.display.draw(self.array,j,min_pos,i)
                self.display.draw_other(self.accesses,self.comparisons)

                pygame.display.flip()

            self.array[i],self.array[min_pos] = self.array[min_pos],self.array[i]
            self.accesses += 4

            self.display.events()
            self.display.draw(self.array,j,min_pos,i)
            self.display.draw_other(self.accesses,self.comparisons)

            pygame.display.flip()
