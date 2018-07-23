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
            out.append((a if a[0] < b[0] else b).pop(0))

        return out+a+b

    def strand(self,arr):
        i = 0
        s = [arr.pop(0)]

        while i < len(arr):
            if arr[i] > s[-1]:
                s.append(arr.pop(i))
            else:
                i += 1

        return s

    def main(self):
        array = self.array[:]
        out = self.strand(array)

        while len(array):
            self.clock.tick(self.fps)
            
            out = self.merge(out,self.strand(array))

            self.display.draw(out)
            pygame.display.flip()
