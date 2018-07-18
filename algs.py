from display import Display

from Bubble import Bubble
from Quicksort import Quicksort
from Insertion import Insertion
from Cocktail import Cocktail
from Bogo import Bogo
from Oddeven import Oddeven
from Shell import Shell
from Comb import Comb
from Gnome import Gnome
from MergeTD import MergeTD
from RadixLSD import RadixLSD

import pygame
import random

class methods:
    def __init__(self,fps,length,clockObject,surface,font,bars):
        self.fps = fps
        self.length = length
        self.clock = clockObject
        self.surface = surface
        self.font = font
        
        setattr(self.display,"bars",self.bars)

    def setup(self,thickness,windowsize):
        self.array = list(range(self.length))
        random.shuffle(self.array)

        self.display = Display(thickness,windowsize,self.surface,self.font)
        self.accesses = 0
        self.comparisons = 0

    def bubble(self):
        method = Bubble(self.array,self.display,self.clock,self.fps)
        method.main()

    def quicksort(self):
        method = Quicksort(self.array,self.display,self.clock,self.fps)
        method.main()

    def insertion(self):
        method = Insertion(self.array,self.display,self.clock,self.fps)
        method.main()

    def cocktail(self):
        method = Cocktail(self.array,self.display,self.clock,self.fps)
        method.main()

    def bogo(self):
        method = Bogo(self.array,self.display,self.clock,self.fps)
        method.main()

    def oddeven(self):
        method = Oddeven(self.array,self.display,self.clock,self.fps)
        method.main()

    def shell(self):
        method = Shell(self.array,self.display,self.clock,self.fps)
        method.main()

    def comb(self):
        method = Comb(self.array,self.display,self.clock,self.fps)
        method.main()

    def gnome(self):
        method = Gnome(self.array,self.display,self.clock,self.fps)
        method.main()

    def mergetd(self):
        method = MergeTD(self.array,self.display,self.clock,self.fps)
        method.main()
        
    def radixlsd(self):
        method = RadixLSD(self.array,self.display,self.clock,self.fps)
        method.main()
