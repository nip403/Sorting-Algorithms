import pygame

class MergeBU:
    def __init__(self,array,displayObject,clock,fps):
        self.array = array
        self.display = displayObject
        self.clock = clock
        self.fps = fps
        self.accesses = 0
        self.comparisons = 0

    def get_drawable(self,groups):
        out = []
        
        for i in groups:
            for e in i:
                out.append(e)

        return out

    def merge(self,a,b=None):
        if b is None:
            return a
        
        out = []
        total = a+b

        while len(total):
            self.clock.tick(self.fps)
            
            smallest = min(total)
            out.append(smallest)
            del total[total.index(smallest)]

            self.display.events()

            if self.tmp3 == 2:
                self.display.add_green(range(len(out)))
            
            self.display.draw(self.tmp+out+total+self.tmp2,len(self.tmp+out))

            pygame.display.flip()

        return out

    def sort(self,groups):
        if len(groups) == 1:
            return groups
        
        out = []
        self.display.events()
        self.display.draw(self.get_drawable(groups))
        pygame.display.flip()

        for i in range(0,len(groups),2):
            self.clock.tick(self.fps)
            self.tmp = self.get_drawable(out)
            self.tmp2 = self.get_drawable(groups[i+2:])
            self.tmp3 = len(groups)
            
            out.append(self.merge(groups[i],groups[i+1] if i+1 < len(groups) else None))

        self.display.draw(self.get_drawable(out))
        pygame.display.flip()

        return self.sort(out)

    def main(self):
        self.sort([[self.array[i],self.array[i+1]] if i < len(self.array) else [self.array[i]] for i in range(0,len(self.array),2)])

