import pygame

class Quick3:
    def __init__(self, array, displayObject, clock, fps):
        self.array = array
        self.display = displayObject
        self.clock = clock
        self.fps = fps
        self.accesses = 0
        self.comparisons = 0

    def partition(self, arr, low, high):
        if high - low <= 1:
            self.accesses += 1
            self.comparisons += 1
            
            if arr[high] < arr[low]:
                self.accesses += 4
                arr[high], arr[low] = arr[low], arr[high]

                self.display.events()
                self.display.add_green([p for p, i in enumerate(arr) if sorted(arr)[p] == i])
                self.display.draw(self.array, low, high)
                self.display.draw_other(self.accesses, self.comparisons)

                pygame.display.flip()
                
            return low, high

        self.accesses += 1
        
        mid = low
        pivot = arr[high]

        while mid <= high:
            self.clock.tick()

            self.accesses += 3
            self.comparisons += 3
            
            if arr[mid] < pivot:
                arr[mid], arr[low] = arr[low], arr[mid]
                
                mid += 1
                low += 1

                self.accesses += 4
                
            elif arr[mid] == pivot:
                mid += 1

            elif arr[mid] > pivot:
                self.accesses += 4

                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1

            self.display.events()
            self.display.add_green([p for p, i in enumerate(arr) if sorted(arr)[p] == i])
            self.display.draw(self.array, low, high, mid)
            self.display.draw_other(self.accesses, self.comparisons)
            
            pygame.display.flip()

            i = low - 1
            j = mid

        return i, j

    def quicksort(self, arr, low, high):
        if low >= high:
            return arr

        i, j = self.partition(arr, low, high)
        arr = self.quicksort(self.quicksort(arr, low, i), j, high)

        return arr

    def main(self):
        self.quicksort(self.array, 0, len(self.array)-1)
