import pygame
import random

from display import Display

from Bubble import Bubble
from Quicksort import Quicksort
from Insertion import Insertion
from Cocktail import Cocktail
from Bogo import Bogo
from Oddeven import Oddeven
from MergeTD import MergeTD

class methods:
    def __init__(self,fps,length,clockObject,surface,font):
        self.fps = fps
        self.length = length
        self.clock = clockObject
        self.surface = surface
        self.font = font

    def setup(self,thickness,windowsize):
        self.array = list(range(self.length))
        random.shuffle(self.array)

        self.display = Display(thickness,windowsize,self.surface,self.font)
        self.accesses = 0
        self.comparisons = 0

    def bubble(self):
        b = Bubble(self.display,self.array,self.fps,self.length,self.accesses,self.comparisons,self.clock)
        b.main()

    def quicksort(self):
        q = Quicksort(self.display,self.array,self.fps,self.length,self.accesses,self.comparisons,self.clock)
        q.main()

    def insertion(self):
        i = Insertion(self.display,self.array,self.fps,self.length,self.accesses,self.comparisons,self.clock)
        i.main()

    def cocktail(self):
        c = Cocktail(self.display,self.array,self.fps,self.length,self.accesses,self.comparisons,self.clock)
        c.main()

    def bogo(self):
        b = Bogo(self.display,self.array,self.fps,self.length,self.accesses,self.comparisons,self.clock)
        b.main()

    def oddeven(self):
        o = Oddeven(self.display,self.array,self.fps,self.length,self.accesses,self.comparisons,self.clock)
        o.main()

    def mergeTD(self):
        m = MergeTD(self.display,self.array,self.fps,self.length,self.accesses,self.comparisons,self.clock)
        m.main()
