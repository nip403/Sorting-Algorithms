import pygame

class Heap:
    def __init__(self,array,displayObject,clock,fps):
        self.array = array
        self.display = displayObject
        self.clock = clock
        self.fps = fps
        self.accesses = 0
        self.comparisons = 0

    def siftdown(self,array,start,end):
        root = start

        while True:
            self.clock.tick(self.fps)
            child = root * 2 + 1

            if child > end:
                self.comparisons += 1
                break
            if child + 1 <= end and array[child] < array[child + 1]:
                self.comparisons += 2
                self.accesses += 1
                child += 1
            if array[root] < array[child]:
                self.comparisons += 1
                array[root],array[child] = array[child],array[root]
                self.accesses += 6
                root = child
            else:
                break

            self.display.events()
            self.display.draw(array,child,root,start,end)
            self.display.draw_other(self.accesses,self.comparisons)
            
            pygame.display.flip()

        return array

    def main(self):
        self.accesses += 1
        for start in range(int((len(self.array)-2)/2),-1,-1):
            self.clock.tick(self.fps)
            
            self.accesses += 1
            self.array = self.siftdown(self.array,start,len(self.array)-1)

            self.display.events()
            self.display.draw(self.array,start)
            self.display.draw_other(self.accesses,self.comparisons)
            
            pygame.display.flip()

        self.accesses += 1
        for end in range(len(self.array)-1,0,-1):
            self.clock.tick(self.fps)
            
            self.array[end],self.array[0] = self.array[0],self.array[end]
            self.array = self.siftdown(self.array,0,end-1)

            self.display.events()
            self.display.add_green([self.array.index(i) for i in self.array[end-1:]])
            self.display.draw(self.array,end)
            self.display.draw_other(self.accesses,self.comparisons)
            
            pygame.display.flip()
