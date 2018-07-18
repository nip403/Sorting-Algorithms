import pygame

class MergeTD:
    def __init__(self,array,displayObject,clock,fps,arr_length):
        self.array = array
        self.display = displayObject
        self.clock = clock
        self.fps = fps
        self.accesses = 0
        self.comparisons = 0
        
    def m(self,array,i0,i1):
        self.clock.tick(self.fps)

        if len(array) <= 1:
            self.comparisons += 1
            return array,i0,i1

        self.accesses += 2
        left,l0,l1 = self.m(array[:len(array)//2],i0,i0+(len(array)//2))
        right,r0,r1 = self.m(array[len(array)//2:],i0+(len(array)//2),i1)

        new = []
        total = left + right
        self.accesses += 2

        while len(total) > 0:
            self.clock.tick(self.fps)
            
            self.comparisons += 1
            self.accesses += 5

            self.array[l0+len(new)] = min(total)
            new.append(min(total))

            self.display.events()
            self.display.draw(self.array,i0,i1,l0,l1,r0,r1,l0+len(new))
            self.display.draw_other(self.accesses,self.comparisons)

            del total[total.index(min(total))]

            pygame.display.flip()

        return new,l0,r1

    def main(self):
        self.m(self.array,0,len(self.array)-1)
