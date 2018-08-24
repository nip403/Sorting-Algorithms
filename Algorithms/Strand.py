import pygame

class Strand:
    def __init__(self,array,displayObject,clock,fps):
        self.array = array
        self.display = displayObject
        self.clock = clock
        self.fps = fps
        self.accesses = 0
        self.comparisons = 0

    def merge(self,a,b):
        out = []

        while len(a) and len(b):
            self.accesses += 5
            self.comparisons += 3
            
            out.append((a if a[0] < b[0] else b).pop(0))

        return out+a+b

    def strand(self,arr):
        i = 0
        s = [arr.pop(0)]

        self.accesses += 1

        while i < len(arr):
            if arr[i] > s[-1]:
                s.append(arr.pop(i))
            else:
                i += 1

            self.accesses += 4
            self.comparisons += 2

        return s

    def make_output(self,correct,remaining):
        return correct + [i for p,i in enumerate(remaining) if not p in correct]

    def main(self):
        array = self.array[:]
        out = self.strand(array)

        self.display.add_green(range(len(out)))
        self.display.draw(self.array,*range(len(out),len(array)))
        self.display.draw_other(self.accesses,self.comparisons)
            
        pygame.display.flip()

        while len(array):
            self.accesses += 1
            self.comparisons += 1
            
            self.clock.tick(self.fps)
            out = self.merge(out,self.strand(array))
            final_output = self.make_output(out,self.array)

            self.display.events()
            self.display.add_green(range(len(out)))
            self.display.draw(final_output,*range(len(self.array),len(out)-1,-1))
            self.display.draw_other(self.accesses,self.comparisons)
            
            pygame.display.flip()
