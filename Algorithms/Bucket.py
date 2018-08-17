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
        self.display.add_green([clength],False)
        
        for i in range(1,len(array)):
            key = array[i]
            low = 0
            high = i
            self.accesses += 2
            self.comparisons += 2

            while high > low:
                self.clock.tick(self.fps)
                self.accesses += 1
                self.comparisons += 1
                
                mid = (low+high)//2
                
                if array[mid] < key:
                    low = mid+1
                else:
                    high = mid

                self.display.events()
                self.display.add_green([array.index(key)+clength],False)
                self.display.draw(self.array[:clength] + array + self.array[clength+len(array):],clength,clength+mid,clength+i,clength+high,clength+low)
                self.display.draw_other(self.accesses,self.comparisons)

                pygame.display.flip()

            array[:] = array[:low]+[key]+array[low:i]+array[i+1:]
            self.accesses += len(array)

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

            p = self.re_hash(i,c)
            buckets[p].append(i)
            self.accesses += 1
            tmp = self.merge_buckets(buckets,self.array,True)

            l = p
            for k in buckets[:p]:
                for v in k:
                    l += 1
            
            self.display.events()
            self.display.draw(tmp+self.array[len(tmp):],p0,l)
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
