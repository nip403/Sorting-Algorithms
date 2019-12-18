import pygame

class Counting:
    def __init__(self, array, displayObject, clock, fps):
        self.array = array
        self.display = displayObject
        self.clock = clock
        self.fps = fps
        self.accesses = 0
        self.comparisons = 0

    def main(self):
        count = [0] * len(self.array)
        output = [0] * len(self.array)
        self.accesses += 5
       
        for i in range(0, len(self.array)):
            count[self.array[i]] += 1
            self.accesses += 2

        for i in range(1, len(count)):
            count[i] += count[i-1]
            self.accesses += 2

        for i in range(len(self.array)):
            self.clock.tick(self.fps)
            
            output[count[self.array[i]] - 1] = self.array[i]
            count[self.array[i]] -= 1
            self.accesses += 6

            self.display.events()
            self.display.add_green([count[self.array[i]]], False)
            self.display.draw([output[i] if (output[i] or i == 0) else self.array[i] for i in range(len(self.array))], self.array[i], count[self.array[i]])
            self.display.draw_other(self.accesses,self.comparisons)

            pygame.display.flip()
