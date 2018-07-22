from display import Display

from Bubble import Bubble
from Quicksort import Quicksort
from Selection import Selection
from Cocktail import Cocktail
from Bogo import Bogo
from Oddeven import Oddeven
from Shell import Shell
from Comb import Comb
from Insertion import Insertion
from MergeTD import MergeTD
from RadixLSD import RadixLSD
from Counting import Counting
from Cycle import Cycle
from Heap import Heap
from Circle import Circle
from Gnome import Gnome
from BinaryInsertion import BinaryInsertion
from Pancake import Pancake

import pygame
import random

class methods:
    def __init__(self,fps,length,clockObject,surface,font,bars):
        self.fps = fps
        self.length = length
        self.clock = clockObject
        self.surface = surface
        self.font = font
        self.bars = bars

    def setup(self,thickness,windowsize):
        self.array = list(range(self.length))
        random.shuffle(self.array)

        self.display = Display(thickness,windowsize,self.surface,self.font)
        self.accesses = 0
        self.comparisons = 0
        
        setattr(self.display,"bars",self.bars)

    bubble = lambda self: Bubble(self.array,self.display,self.clock,self.fps).main()
    quicksort = lambda self: Quicksort(self.array,self.display,self.clock,self.fps).main()
    selection = lambda self: Selection(self.array,self.display,self.clock,self.fps).main()
    cocktail = lambda self: Cocktail(self.array,self.display,self.clock,self.fps).main() 
    bogo = lambda self: Bogo(self.array,self.display,self.clock,self.fps).main()
    oddeven = lambda self: Oddeven(self.array,self.display,self.clock,self.fps).main()
    shell = lambda self: Shell(self.array,self.display,self.clock,self.fps).main()
    comb = lambda self: Comb(self.array,self.display,self.clock,self.fps).main()
    insertion = lambda self: Insertion(self.array,self.display,self.clock,self.fps).main()
    mergetd = lambda self: MergeTD(self.array,self.display,self.clock,self.fps).main()
    radixlsd = lambda self: RadixLSD(self.array,self.display,self.clock,self.fps).main()
    counting = lambda self: Counting(self.array,self.display,self.clock,self.fps).main()
    cycle = lambda self: Cycle(self.array,self.display,self.clock,self.fps).main()
    heap = lambda self: Heap(self.array,self.display,self.clock,self.fps).main()
    circle = lambda self: Circle(self.array,self.display,self.clock,self.fps).main()
    gnome = lambda self: Gnome(self.array,self.display,self.clock,self.fps).main()
    binaryinsertion = lambda self: BinaryInsertion(self.array,self.display,self.clock,self.fps).main()
    pancake = lambda self: Pancake(self.array,self.display,self.clock,self.fps).main()
