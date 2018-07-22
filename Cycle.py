import pygame

class Cycle:
    def __init__(self,array,displayObject,clock,fps):
        self.array = array
        self.display = displayObject
        self.clock = clock
        self.fps = fps
        self.accesses = 0
        self.comparisons = 0

    def main(self):
        self.accesses += 1
        for i in range(len(self.array)-1):
            self.clock.tick(self.fps)
            
            item = self.array[i]
            self.accesses += 2
            pos = i
           
            for j in range(i+1,len(self.array)):
                if self.array[j] < item:
                    pos += 1
                self.accesses += 1
                self.comparisons += 1

            if pos == i:
                continue
                
            self.array[pos],item = item,self.array[pos]
            self.accesses += 2

            self.display.events()
            self.display.draw(self.array,pos,i,j)
            self.display.draw_other(self.accesses,self.comparisons)

            pygame.display.flip()

            while not pos == i:
                self.clock.tick(self.fps)
                self.comparisons += 1
                
                pos = i
                for j in range(i+1,len(self.array)):
                    if self.array[j] < item:
                        pos += 1

                    self.accesses += len(self.array) + 1
                    self.comparisons += 1

                self.array[pos],item = item,self.array[pos]
                self.accesses += 1

                self.display.events()
                self.display.draw(self.array,i,j,pos)
                self.display.draw_other(self.accesses,self.comparisons)

                pygame.display.flip()
