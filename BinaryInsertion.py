import pygame

class BinaryInsertion:
    def __init__(self,array,displayObject,clock,fps):
        self.array = array
        self.display = displayObject
        self.clock = clock
        self.fps = fps
        self.accesses = 0
        self.comparisons = 0

    def main(self):
        self.accesses += 1
        for i in range(1,len(self.array)):
            self.clock.tick(self.fps)
            
            key = self.array[i]
            low = 0
            high = i

            self.accesses += 1

            while high > low:
                self.clock.tick(self.fps)
                
                mid = (low+high)//2

                if self.array[mid] < key:
                    low = mid + 1
                else:
                    high = mid

                self.comparisons += 2
                self.accesses += 1

                self.display.events()
                self.display.draw(self.array,low,mid,high)
                self.display.draw_other(self.accesses,self.comparisons)

                pygame.display.flip()

            self.accesses += len(self.array)
            self.array[:] = self.array[:low] + [key] + self.array[low:i] + self.array[i+1:]

            self.display.events()
            self.display.add_green([self.array.index(i) for i in self.array[:i+1]])
            self.display.draw(self.array,low,i,mid,high)
            self.display.draw_other(self.accesses,self.comparisons)

            pygame.display.flip()
