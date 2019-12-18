import pygame

class Smooth:
    def __init__(self, array, displayObject, clock, fps):
        self.array = array
        self.display = displayObject
        self.clock = clock
        self.fps = fps
        self.accesses = 0
        self.comparisons = 0

    def up(self, a, b):
        return a+b + 1, a

    def down(self, a, b):
        return b, a-b - 1

    def sift(self, r1, b1, c1):
        copy, t = r1, self.array[r1]

        self.accesses += 1
        self.comparisons += 1

        while b1 >= 3:
            self.clock.tick(self.fps)
            self.accesses += 3
            self.comparisons += 3
            
            r2 = r1 - b1 + c1

            if self.array[r1-1] > self.array[r2]:
                r2, b1, c1 = r1 - 1, *self.down(b1, c1)
                
            if self.array[r2] <= t:
                b1 = 1
            else:
                self.accesses += 2
                self.array[r1] = self.array[r2]

                self.display.events()
                self.display.add_green([p for p, i in enumerate(self.array) if i == sorted(self.array)[p]])
                self.display.draw(self.array, r1, r2, b1, c1, copy)
                self.display.draw_other(self.accesses, self.comparisons)

                pygame.display.flip()
                
                r1, b1, c1 = r2, *self.down(b1, c1)

        if not r1 == copy:
            self.accesses += 1
            self.array[r1] = t

            self.display.add_green([p for p, i in enumerate(self.array) if i == sorted(self.array)[p]])
            self.display.draw(self.array, r1, r2, b1, c1, copy)
            self.display.draw_other(self.accesses, self.comparisons)

            pygame.display.flip()
                
    def trinkle(self, p, b, c, r1):
        p1, b1, c1, copy, t = p, b, c, r1, self.array[r1]
        
        self.accesses += 1
        self.comparisons += 1

        while p1 > 0:
            self.clock.tick(self.fps)
            self.comparisons += 3
            
            while not p1 & 1:
                p1, b1, c1 = p1 >> 1, *self.up(b1, c1)
                self.comparisons += 1

            r3 = r1 - b1

            if p1 == 1 or self.array[r3] <= t:
                p1 = 0
            else:
                self.comparisons += 2
                p1 -= 1
                
                if b1 == 1:
                    self.array[r1] = self.array[r3]
                    self.accesses += 2

                    self.display.add_green([p for p, i in enumerate(self.array) if i == sorted(self.array)[p]])
                    self.display.draw(self.array, p1, b1, c1, r1, r3, copy)
                    self.display.draw_other(self.accesses, self.comparisons)

                    pygame.display.flip()
                    
                    r1 = r3
                    
                elif b1 >= 3:
                    self.accesses += 4
                    self.comparisons += 2
                    
                    r2 = r1 - b1 + c1
                    
                    if self.array[r1-1] > self.array[r2]:
                        r2, b1, c1, p1 = r1 - 1, *self.down(b1, c1), p1 << 1
                        
                    if self.array[r2] <= self.array[r3]:
                        self.accesses += 2
                        self.array[r1] = self.array[r3]

                        self.display.add_green([p for p, i in enumerate(self.array) if i == sorted(self.array)[p]])
                        self.display.draw(self.array, p1, b1, c1, r1, r3, r2, copy)
                        self.display.draw_other(self.accesses, self.comparisons)

                        pygame.display.flip()
                        
                        r1 = r3
                    else:
                        self.accesses += 2
                        self.array[r1] = self.array[r2]

                        self.display.add_green([p for p, i in enumerate(self.array) if i == sorted(self.array)[p]])
                        self.display.draw(self.array, p1, b1, c1, r1, r3, copy)
                        self.display.draw_other(self.accesses, self.comparisons)

                        pygame.display.flip()
                        
                        r1, b1, c1, p1 = r2, *self.down(b1, c1), 0
                        
        if not copy == r1:
            self.accesses += 1
            self.array[r1] = t

            self.display.add_green([p for p, i in enumerate(self.array) if i == sorted(self.array)[p]])
            self.display.draw(self.array, p1, b1, c1, r1, r3, copy)
            self.display.draw_other(self.accesses, self.comparisons)

            pygame.display.flip()
            
        self.sift(r1, b1, c1)

    def semitrinkle(self, p, b, r, c):
        self.accesses += 2
        self.comparisons += 2
        
        if self.array[r-c] > self.array[r]:
            self.clock.tick(self.fps)
            self.accesses += 4
            
            self.array[r], self.array[r-c] = self.array[r-c], self.array[r]

            self.display.events()
            self.display.add_green([p for p, i in enumerate(self.array) if i == sorted(self.array)[p]])
            self.display.draw(self.array, p, b, r, c, r-c)
            self.display.draw_other(self.accesses, self.comparisons)

            pygame.display.flip()
            
            self.trinkle(p, b, c, r-c)

    def main(self):
        q, r, p, b, c = 1, 0, 1, 1, 1

        self.display.add_green([p for p, i in enumerate(self.array) if i == sorted(self.array)[p]])
        self.display.draw(self.array, p, b, r, c, r-c)
        self.display.draw_other(self.accesses, self.comparisons)

        pygame.display.flip()

        while q < len(self.array):
            r1 = r
            self.accesses += 1
            self.comparisons += 3

            if p & 7 == 3:
                b1, c1 = b, c
                self.sift(r1, b1, c1)
                p, b, c = (p+1) >> 2, *self.up(*self.up(b, c))
                
            elif p & 3 == 1:
                self.accesses += 1
                self.comparisons += 1
                
                if q + c < len(self.array):
                    b1, c1 = b, c
                    self.sift(r1, b1, c1)
                else:
                    self.trinkle(p, b, c, r1)

                b, c, p = *self.down(b, c), p << 1

                while b > 1:
                    self.comparisons += 1
                    b, c, p = *self.down(b, c), p << 1

                p += 1

            q += 1
            r += 1

        r1 = r
        self.trinkle(p, b, c, r1)

        while q > 1:
            self.comparisons += 3
            q -= 1
            
            if b == 1:
                r -= 1
                p -= 1
                
                while not p & 1:
                    self.comparisons += 1
                    p, b, c = p >> 1, *self.up(b, c)
                    
            elif b >= 3:
                self.comparisons += 1
                p -= 1
                r += c - b

                if p > 0:
                    self.semitrinkle(p, b, r, c)
                    
                b, c, p = *self.down(b, c), (p << 1) + 1
                r += c
                
                self.semitrinkle(p, b, r, c)
                b, c, p = *self.down(b, c), (p << 1) + 1
