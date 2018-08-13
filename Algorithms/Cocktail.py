import pygame

class Cocktail:
    def __init__(self,array,displayObject,clock,fps):
        self.array = array
        self.display = displayObject
        self.clock = clock
        self.fps = fps
        self.accesses = 0
        self.comparisons = 0

    def main(self):
        base = 0
        
        self.accesses += 1
        for k in range(len(self.array)-1,0,-1):
            for j in range(2):
                swapped = False
                
                for i in range(k if not j % 2 else base,base if not j % 2 else k,-1 if not j % 2 else 1):
                    self.clock.tick(self.fps)

                    t = i-1 if not j % 2 else i+1
                    if self.array[i if not j % 2 else t] < self.array[t if not j % 2 else i]:
                        self.array[i],self.array[t] = self.array[t],self.array[i]
                        swapped = True
                        
                    self.accesses += 6
                    self.comparisons += 1

                    self.display.events()
                    self.display.add_green([base] if not j % 2 else [k],False)
                    self.display.draw(self.array,k,i,i-1,base)
                    self.display.draw_other(self.accesses,self.comparisons)

                    pygame.display.flip()

                if not swapped:
                    self.display.add_green(range(len(self.array)))
                    self.display.draw(self.array,k,i,i-1,base)
                    self.display.draw_other(self.accesses,self.comparisons)

                    pygame.display.flip()
                    return

                base += 1 if not j % 2 else 0
