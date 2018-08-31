import pygame

class Stooge:
    def __init__(self,array,displayObject,clock,fps):
        self.array = array
        self.display = displayObject
        self.clock = clock
        self.fps = fps
        self.accesses = 0
        self.comparisons = 0

    def sort(self,last,index=0):
        self.accesses += 2
        self.comparisons += 2
        
        if self.array[index] > self.array[last]:
            self.clock.tick(self.fps)
            self.accesses += 4
            
            self.array[index],self.array[last] = self.array[last],self.array[index]

            self.display.events()
            self.display.add_green([p for p,i in enumerate(self.array) if i == sorted(self.array)[p]])
            self.display.draw(self.array,index,last)
            self.display.draw_other(self.accesses,self.comparisons)

            pygame.display.flip()

        if last-index > 1:
            t = int((last-index+1)/3)

            self.sort(last-t,index)
            self.sort(last,index+t)
            self.sort(last-t,index)
            
    def main(self):
        self.sort(len(self.array)-1)
