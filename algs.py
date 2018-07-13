import pygame
import random

from display import Display

from Bubble import Bubble
from Quicksort import Quicksort
from Selection import Selection
from Cocktail import Cocktail
from Bogo import Bogo
from Oddeven import Oddeven
from MergeTD import MergeTD

class methods:
    def __init__(self,fps,length):
        self.fps = fps
        self.length = length

    def setup(self):
        self.array = list(range(self.length))
        random.shuffle(self.array)

        self.display = Display()
        self.accesses = 0
        self.comparisons = 0

    def bubble(self):
        b = Bubble(self.display,self.array,self.fps,self.length,self.accesses,self.comparisons)
        b.main()

    def quicksort(self):
        q = Quicksort(self.display,self.array,self.fps,self.length,self.accesses,self.comparisons)
        q.main()

    def selection(self):
        s = Selection(self.display,self.array,self.fps,self.length,self.accesses,self.comparisons)
        s.main()

    def cocktail(self):
        c = Cocktail(self.display,self.array,self.fps,self.length,self.accesses,self.comparisons)
        c.main()

    def bogo(self):
        b = Bogo(self.display,self.array,self.fps,self.length,self.accesses,self.comparisons)
        b.main()

    def oddeven(self):
        o = Oddeven(self.display,self.array,self.fps,self.length,self.accesses,self.comparisons)
        o.main()

    def mergeTD(self):
        m = MergeTD(self.display,self.array,self.fps,self.length,self.accesses,self.comparisons)
        m.main()
        
