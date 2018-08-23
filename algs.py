from display import Display

import pygame
import random
import sys

sys.path.insert(0,"./Algorithms")

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
from Permutation import Permutation
from Strand import Strand
from Bucket import Bucket
from MinMax import MinMax
from MergeBU import MergeBU

class methods:
    def __init__(self,fps,clockObject,surface,font,bars,windowsize):
        self.fps = fps
        self.clock = clockObject
        self.surface = surface
        self.font = font
        self.bars = bars
        self.windowsize = windowsize

    def get_array(self,length,mode=0):
        arr = list(range(length))
        
        if not mode:
            random.shuffle(arr)
        elif mode == 2:
            arr = arr[::-1]
        elif mode == 3:
            for i in range(length-1):
                if random.randint(0,10) < 8:
                    tmp = random.randint(4,15)
                    try:
                        arr[i],arr[i+tmp] = arr[i+tmp],arr[i]
                    except:
                        pass

        return arr

    def setup(self,length,mode=0):
        self.array = self.get_array(length,mode)
                
        self.display = Display(self.windowsize[0]/length,self.windowsize,self.surface,self.font)
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
    permutation = lambda self: Permutation(self.array,self.display,self.clock,self.fps).main()
    strand = lambda self: Strand(self.array,self.display,self.clock,self.fps).main()
    bucket = lambda self: Bucket(self.array,self.display,self.clock,self.fps).main()
    minmax = lambda self: MinMax(self.array,self.display,self.clock,self.fps).main()
    mergebu = lambda self: MergeBU(self.array,self.display,self.clock,self.fps).main()
