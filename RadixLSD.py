import pygame

class RadixLSD:
    def __init__(self,array,displayObject,clock,fps):
        self.array = array
        self.display = displayObject
        self.clock = clock
        self.fps = fps
        self.accesses = 0

    def list_to_buckets(self,array,base,iteration):
        buckets = [[] for i in range(base)]

        for number in array:
            digit = (number // (base**iteration)) % base

            self.accesses += 1
            buckets[digit].append(number)

        return buckets

    def buckets_to_list(self,buckets):
        numbers = []
        count = 0

        for bucket in buckets:
            for number in bucket:
                self.clock.tick(self.fps)

                self.accesses += 1
                self.array[count] = number
                count += 1

                numbers.append(number)

                self.display.events()
                self.display.draw(self.array,count)
                self.display.draw_other(self.accesses,0)
                
                pygame.display.flip()

        return numbers

    def main(self):
        m = max(self.array)
        iteration = 0
        base = 256 # default = 10, optimum = 256 (https://cs.stackexchange.com/questions/44138/radix-sort-and-changing-bases)

        while base ** iteration <= m:
            self.array = self.buckets_to_list(self.list_to_buckets(self.array,base,iteration))
            iteration += 1
