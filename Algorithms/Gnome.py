import pygame

class Gnome:
    def __init__(self, array, displayObject, clock, fps):
        self.array = array
        self.display = displayObject
        self.clock = clock
        self.fps = fps
        self.accesses = 0
        self.comparisons = 0

    def main(self):
        left = 1
        right = 2

        self.display.add_green([0])

        while left < len(self.array):
            self.clock.tick(self.fps)
            self.accesses += 2
            self.comparisons += 1
            
            if self.array[left-1] <= self.array[left]:
                left, right = right, right+1
                
            else:
                self.array[left-1], self.array[left] = self.array[left], self.array[left-1]
                left -= 1
                
                self.accesses += 4
                self.comparisons += 1

                if not left:
                    left, right = right, right + 1

            self.display.events()
            self.display.add_green([left], False)
            self.display.draw(self.array, left, right, left-1)
            self.display.draw_other(self.accesses,self.comparisons)

            pygame.display.flip()
