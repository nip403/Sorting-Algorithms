import pygame
import itertools

class Permutation:
    def __init__(self, array, displayObject, clock, fps):
        self.array = array
        self.display = displayObject
        self.clock = clock
        self.fps = fps
        self.accesses = 0
        self.comparisons = 0

    def ordered(self, arr):
        return all(x <= arr[i+1] for i, x in enumerate(arr[:-1]))

    def main(self):
        self.accesses += 1
        for perm in itertools.permutations(self.array):
            self.clock.tick(self.fps)

            self.accesses += len(perm) - 1
            self.comparisons += len(perm) - 2

            self.display.events()
            self.display.add_green([i for i in range(len(perm)) if perm[i] == sorted(perm)[i]])
            self.display.draw(perm, *[i for i in range(len(perm)) if not perm[i] == sorted(perm)[i]])
            self.display.draw_other(self.accesses, self.comparisons)

            pygame.display.flip()

            if self.ordered(perm):
                return
