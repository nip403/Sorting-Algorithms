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

        self.accesses += 1
        self.comparisons += 1
        if len(array) <= 1:
            return array,i0,i1

        self.accesses += 6
        left,l0,l1 = self.m(array[:len(array)//2],i0,i0+(len(array)//2))
        right,r0,r1 = self.m(array[len(array)//2:],i0+(len(array)//2),i1)

        new = []
        while len(left) and len(right):
            self.clock.tick(self.fps)
            
            self.comparisons += 3
            self.accesses += 5

            if left[0] < right[0]:
                tmp = left.pop(0)
                new.append(tmp)
            else:
                tmp = right.pop(0)
                new.append(tmp)

            self.array[l0+len(new)-1] = tmp

            self.display.events()
            self.display.draw(self.array,i0,i1,l0,l1,r0,r1,l0+len(new)-1)
            self.display.draw_other(self.accesses,self.comparisons)

            pygame.display.flip()

        while len(left) or len(right):
            self.clock.tick(self.fps)
            
            try:
                tmp = left.pop(0)
            except:
                tmp = right.pop(0)
            finally:
                self.accesses += 1
                self.comparisons += 2
                
                new.append(tmp)
                self.array[l0+len(new)-1] = tmp

                self.display.events()
                self.display.draw(self.array,i0,i1,l0,l1,r0,r1,l0+len(new)-1)
                self.display.draw_other(self.accesses,self.comparisons)

                pygame.display.flip()

        return new,l0,r1

    def main(self):
        self.m(self.array,0,len(self.array)-1)
