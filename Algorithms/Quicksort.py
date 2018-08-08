import pygame

class Quicksort:
    def __init__(self,array,displayObject,clock,fps):
        self.array = array
        self.display = displayObject
        self.clock = clock
        self.fps = fps
        self.accesses = 0
        self.comparisons = 0

    def partition(self,array,first,last):
        i = first - 1
        pivot = array[last]
        self.accesses += 1

        for j in range(first,last):
            self.clock.tick(self.fps)

            if array[j] <= pivot:
                i += 1
                array[i],array[j] = array[j],array[i]
            self.accesses += 5
            self.comparisons += 1

            self.display.events()
            self.display.add_green([p for p,i in enumerate(self.array) if sorted(self.array)[p] == i])
            self.display.draw(array,i,j,pivot)
            self.display.draw_other(self.accesses,self.comparisons)

            pygame.display.flip()

        array[i+1],array[last] = array[last],array[i+1]
        self.accesses += 4
        
        return i + 1

    def qs(self,array,first,last):
        if first < last:
            pivot = self.partition(array,first,last)
            self.qs(array,first,pivot-1)
            self.qs(array,pivot+1,last)
            
    def main(self):
        self.accesses += 1
        self.qs(self.array,0,len(self.array)-1)

        self.display.add_green([p for p,i in enumerate(self.array) if sorted(self.array)[p] == i])
        self.display.draw(self.array)
        self.display.draw_other(self.accesses,self.comparisons)

        pygame.display.flip()
