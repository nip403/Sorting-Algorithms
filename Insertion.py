import pygame

class Insertion:
    def __init__(self,displayObject,array,fps,arr_length,accesses,comparisons,clock):
        self.display = displayObject
        self.array = array
        self.fps = fps
        self.length = arr_length
        self.accesses = accesses
        self.comparisons = comparisons
        self.clock = clock

    def main(self):
        for i in range(0,self.length-1):
            min_pos = i
            self.accesses += 1

            for j in range(i+1,self.length):
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

        
