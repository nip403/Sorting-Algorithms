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
            self.accesses += 4
            self.comparisons += 1
            self.clock.tick(self.fps)
            
            smallest = min(total)
            out.append(smallest)
            del total[total.index(smallest)]

            self.display.events()

            if self.tmp[2] == 2:
                self.display.add_green(range(len(out)))
            
            self.display.draw(self.tmp[0]+out+total+self.tmp[1],len(self.tmp[0]+out),len(self.tmp[0]+out+total),len(self.tmp[0]))
            self.display.draw_other(self.accesses,self.comparisons)

            pygame.display.flip()

        return out

    def sort(self,groups):
        self.accesses += 1
        self.comparisons += 1
        
        if len(groups) == 1:
            return groups
        
        out = []
        self.accesses += 1
        
        for i in range(0,len(groups),2):
            self.clock.tick(self.fps)
            
            self.tmp = [self.get_drawable(out),self.get_drawable(groups[i+2:]),len(groups)]
            self.accesses += 2
            self.comparisons += 1
            
            out.append(self.merge(groups[i],groups[i+1] if i+1 < len(groups) else None))

        self.display.events()
        self.display.draw(self.get_drawable(out))
        self.display.draw_other(self.accesses,self.comparisons)
        
        pygame.display.flip()

        return self.sort(out)

    def main(self):
        self.accesses += 2
        self.comparisons == 1
        self.sort([[self.array[i],self.array[i+1]] if i < len(self.array)-1 else [self.array[i]] for i in range(0,len(self.array),2)])
