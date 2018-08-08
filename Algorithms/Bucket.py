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
                self.display.draw(self.array[:p*c+p+1] + array + self.array[p*c+p+1+len(array):],p*c+p,p*c+p+len(array),p*c+p+j,p*c+p+i)
                self.display.draw_other(self.accesses,self.comparisons)

                pygame.display.flip()
    
            array[j+1] = key
            self.accesses += 1

            self.display.events()
            self.display.add_green([p for p,i in enumerate(self.array) if i == sorted(self.array)[p]])
            self.display.draw(self.array[:p*c+p+1] + array + self.array[p*c+p+1+len(array):],p*c+p,p*c+p+len(array),p*c+p+j,p*c+p+i)
            self.display.draw_other(self.accesses,self.comparisons)

            pygame.display.flip()

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
        c = self.hash(self.array)
        self.accesses += 1
        buckets = [[] for _ in range(c[1])]

        for p0,i in enumerate(self.array):
            self.clock.tick(self.fps)
            
            x = self.re_hash(i,c)
            buckets[x].append(i)
            self.accesses += 1

            tmp = self.merge_buckets(buckets,self.array,True)
            self.display.events()
            self.display.add_green([p for p,i in enumerate(tmp) if i == sorted(tmp)[p]])
            self.display.draw(tmp+self.array[len(tmp):],p0)
            self.display.draw_other(self.accesses,self.comparisons)

            pygame.display.flip()

        for p,bucket in enumerate(buckets):
            self.clock.tick(self.fps)
            buckets[p] = self.insertion(bucket,p,c[1])
            self.accesses += 1
            print(len(buckets[p]))

            self.display.events()
            self.display.add_green([p for p,i in enumerate(self.array) if i == sorted(self.array)[p]])
            self.display.draw(self.merge_buckets(buckets,self.array,True))
            self.display.draw_other(self.accesses,self.comparisons)

            pygame.display.flip()

        self.merge_buckets(buckets,self.array)
