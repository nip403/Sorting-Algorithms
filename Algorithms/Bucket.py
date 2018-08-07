import pygame
import math

class Bucket:
    def __init__(self,array,displayObject,clock,fps):
        self.array = array
        self.display = displayObject
        self.clock = clock
        self.fps = fps
        self.accesses = 0
        self.comparisons = 0

    def insertion(self,array,p,c):
        for i in range(1,len(array)):
            j = i-1
            key = array[i]

            while j >= 0 and array[j] > key:
                self.clock.tick(self.fps)
                array[j+1] = array[j]
                j -= 1

                self.display.events()
                self.display.draw(self.array[:p*c+p+1] + array + self.array[p*c+p+1+len(array):],p*c+p,p*c+p+len(array),p*c+p+j,p*c+p+i)

                pygame.display.flip()
    
            array[j+1] = key

            self.display.events()
            self.display.add_green([p for p,i in enumerate(self.array) if i == sorted(self.array)[p]])
            self.display.draw(self.array[:p*c+p+1] + array + self.array[p*c+p+1+len(array):],p*c+p,p*c+p+len(array),p*c+p+j,p*c+p+i)

            pygame.display.flip()

        return array

    def hash(self,array):
        m = array[0]

        for i in array[1:]:
            if m < i:
                m = i

        return [m,int(math.sqrt(len(array)))]

    def re_hash(self,i,c):
        return int(i/c[0]*(c[1]-1))

    def merge_buckets(self,buckets,array):
        n = 0

        for b in range(len(buckets)):
            for v in buckets[b]:
                array[n] = v
                n += 1
                
        return array

    def main(self):
        c = self.hash(self.array)
        buckets = [[] for _ in range(c[1])]

        for p0,i in enumerate(self.array):
            self.clock.tick(self.fps)
            
            x = self.re_hash(i,c)
            buckets[x].append(i)

            tmp = self.merge_buckets(buckets,self.array)
            self.display.events()
            self.display.add_green([p for p,i in enumerate(tmp) if i == sorted(tmp)[p]])
            self.display.draw(tmp+self.array[len(tmp):],p0)

            pygame.display.flip()

        for p,bucket in enumerate(buckets):
            self.clock.tick(self.fps)
            buckets[p] = self.insertion(bucket,p,c[1])

            self.display.events()
            self.display.add_green([p for p,i in enumerate(self.array) if i == sorted(self.array)[p]])
            self.display.draw(self.merge_buckets(buckets,self.array))

            pygame.display.flip()

        self.merge_buckets(buckets,self.array)
