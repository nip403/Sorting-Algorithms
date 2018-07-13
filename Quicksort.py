import pygame

class Quicksort:
    def __init__(self,displayObject,array,fps,arr_length,accesses,comparisons,clock):
        self.display = displayObject
        self.array = array
        self.fps = fps
        self.length = arr_length
        self.accesses = accesses
        self.comparisons = comparisons
        self.clock = clock

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
            self.display.draw(array,i,j,pivot)
            self.display.draw_others(self.accesses,self.comparisons)

            pygame.display.flip()

    def qs(self,array,first,last):
        if first < last:
            pivot = partition(array,first,last)
            self.qs(array,first,pivot-1)
            self.qs(array,pivot+1,last)
            
    def main(self):
        self.qs(self.array,0,len(self.array)-1)
        
