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

    def insertion(self,array,clength):
        self.accesses += 1
        
        for i in range(1,len(array)):
            j = i-1
            key = array[i]
            self.accesses += 2
            self.comparisons += 2

            while j >= 0 and array[j] > key:
                self.clock.tick(self.fps)
                self.accesses += 3
                self.comparisons += 2
                
                array[j+1] = array[j]
                j -= 1

                self.display.events()
                self.display.add_green([p+clength for p,i in enumerate(array) if sorted(array)[p] == i],False)
                self.display.draw(self.array[:clength] + array + self.array[clength+len(array):],clength,clength+j,clength+i)
                self.display.draw_other(self.accesses,self.comparisons)

                pygame.display.flip()
    
            array[j+1] = key
            self.accesses += 1

        return array

    def hash(self,array):
        m = array[0]
        self.accesses += 2
        
        for i in array[1:]:
            self.comparisons += 1
            
            if m < i:
                m = i

        self.accesses += 1
        return [m,int(math.sqrt(len(array)))]

    def re_hash(self,i,c):
        self.accesses += 2
        return int(i/c[0]*(c[1]-1))

    def merge_buckets(self,buckets,array,draw=False):
        n = 0
        self.accesses += 1 if not draw else 0

        for b in range(len(buckets)):
            self.accesses += 1 if not draw else 0
            
            for v in buckets[b]:
                array[n] = v
                n += 1

                self.accesses += 1 if not draw else 0
                
        return array

    def main(self):
        self.accesses += 3
        c = self.hash(self.array)
        buckets = [[] for _ in range(c[1])]

        for p0,i in enumerate(self.array):
            self.clock.tick(self.fps)
            
            buckets[self.re_hash(i,c)].append(i)
            self.accesses += 1
            tmp = self.merge_buckets(buckets,self.array,True)
            
            self.display.events()
            self.display.draw(tmp+self.array[len(tmp):],p0)
            self.display.draw_other(self.accesses,self.comparisons)

            pygame.display.flip()

        cumulative_length = 0 # Uneven bucket size
        for p,bucket in enumerate(buckets):
            self.clock.tick(self.fps)
            self.accesses += 3
            
            self.array[cumulative_length:cumulative_length+len(bucket)] = self.insertion(bucket,cumulative_length)
            cumulative_length += len(buckets[p])

        self.display.add_green(range(len(self.array)))
        self.display.draw(self.array)
        self.display.draw_other(self.accesses,self.comparisons)

        pygame.display.flip()
