import pygame

class Circle:
    def __init__(self,array,displayObject,clock,fps):
        self.array = array
        self.display = displayObject
        self.clock = clock
        self.fps = fps
        self.accesses = 0
        self.comparisons = 0

    def csort_backend(self,left,right):
        n = right-left

        if n < 2:
            return 0

        swaps = 0
        m = n//2

        for i in range(m):
            self.clock.tick(self.fps)
            
            self.comparisons += 1
            self.accesses += 2
            
            if self.array[right-(i+1)] < self.array[left+i]:
                self.array[right-(i+1)],self.array[left+i] = self.array[left+i],self.array[right-(i+1)]
                swaps += 1
                self.accesses += 4

            self.display.events()
            self.display.draw(self.array,left,right,right-i+1,left+i)
            self.display.draw_other(self.accesses,self.comparisons)

            pygame.display.flip()

        self.comparisons += 1
        self.accesses += 2
        
        if n & 1 and self.array[left+m] < self.array[left+m-1]:
            self.array[left+m-1],self.array[left+m] = self.array[left+m],self.array[left+m-1]
            swaps += 1
            self.accesses += 4

        self.display.events()
        self.display.add_green([p for p,i in enumerate(self.array) if sorted(self.array)[p] == i])
        self.display.draw(self.array,left,right,left+m,left+m-1)
        self.display.draw_other(self.accesses,self.comparisons)

        pygame.display.flip()
        
        return swaps + self.csort_backend(left,left+m) + self.csort_backend(left+m,right)

    def main(self):
        s = 1

        while s:
            self.clock.tick(self.fps)
            
            self.accesses += 1
            s = self.csort_backend(0,len(self.array))
