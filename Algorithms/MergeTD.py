import pygame

class MergeTD:
    def __init__(self,array,displayObject,clock,fps):
        self.array = array
        self.display = displayObject
        self.clock = clock
        self.fps = fps
        self.accesses = 0
        self.comparisons = 0

    def m(self,array,i0,i1):
        self.clock.tick(self.fps)
        final = len(array) == len(self.array)

        self.accesses += 1
        self.comparisons += 1
        
        if len(array) <= 1:
            return array,i0,i1

        self.accesses += 6
        left,l0,l1 = self.m(array[:len(array)//2],i0,i0+(len(array)//2))
        right,r0,r1 = self.m(array[len(array)//2:],i0+(len(array)//2),i1)

        new = []
        total = left + right
        
        while len(total):
            self.clock.tick(self.fps)

            self.accesses += 4
            self.comparisons += 4

            new.append(min(total))
            self.array[l0+len(new)-1] = min(total)
            
            del total[total.index(min(total))]

            if final:
                self.display.add_green([len(new)],False)

            self.display.events()
            self.display.draw(self.array,i0,i1,l0,l1,r0,r1,l0+len(new)-1)
            self.display.draw_other(self.accesses,self.comparisons)

            pygame.display.flip()

        return new,l0,r1

    def main(self):
        self.accesses += 1
        self.m(self.array,0,len(self.array)-1)
