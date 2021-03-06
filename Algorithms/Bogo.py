import pygame
import random

class Bogo:
    def __init__(self, array, displayObject, clock, fps):
        self.array = array
        self.display = displayObject
        self.clock = clock
        self.fps = fps
        self.accesses = 0
        self.comparisons = 0

    def main(self):
        check = lambda arr, acc, com: [all([arr[i+1] > arr[i] for i in range(len(arr)-1)]), 2*len(self.array) + acc + 1, len(self.array) + com]

        while True:
            self.clock.tick(self.fps)
            state, self.accesses, self.comparisons = check(self.array, self.accesses, self.comparisons)

            self.display.events()
            self.display.add_green([p for p, i in enumerate(self.array) if sorted(self.array)[p] == self.array[p]])
            self.display.draw(self.array, *[p for p, i in enumerate(self.array) if not sorted(self.array)[p] == self.array[p]])
            self.display.draw_other(self.accesses, self.comparisons)

            pygame.display.flip()

            if state:
                return

            random.shuffle(self.array)
