from algs import methods
from showarr import Show_array

import pygame
import random
import sys

# Options
arr_length = 100
fps = 0
draw_bars = False

# Window dimensions
s = [1000,700]

# Initialisations
pygame.init()
screen = pygame.display.set_mode(s,0,32)
clock = pygame.time.Clock()
pygame.display.set_caption("Sorting Algorithms by NIP")

# Fonts
bigfont = pygame.font.SysFont("Garamond MS",140)
medfont = pygame.font.SysFont("Garamond MS",40)
smallfont = pygame.font.SysFont("Garamond MS",20)
labels = pygame.font.SysFont("comicsansms",20)

def main():
    global arr_length

    # Initialisations
    M = methods(fps,arr_length,clock,screen,smallfont,draw_bars)
    
    head1 = medfont.render("Enter Sorting Type:",True,(255,255,255))
    head2 = medfont.render("Types:",True,(255,255,255))
    head3 = medfont.render("Array:",True,(255,255,255))

    show = Show_array(arr_length,(300,200))
    typelist = [[labels.render(i,True,(255,255,255)),[120,240+(p*20)]] for p,i in enumerate([
        "Bubble Sort: 'b'",
        "Quick Sort: 'q'",
        "Selection Sort: 's'",
        "Cocktail Shaker Sort: 'c'",
        "Bogo Sort: 'j'",
        "Odd-Even Sort: 'o'",
        "Shell Sort: 'k'",
        "Comb Sort: 'l'",
        "Insertion Sort: 'i'",
        "Merge (TD) Sort: 'm'",
        "Radix (LSD) Sort: 'r'",
        "Counting Sort: 'x'",
        "Cycle Sort: 'y'",
        "Heap Sort: 'h'",
        "Circle Sort: 'w'",
        "Gnome Sort: 'g'",
        "Binary Insertion Sort: 'u'",
        "Pancake Sort: 'p'",
        "Permutation Sort: 'd'",
        "Strand Sort: 'n'"
    ])]

    keys = {"q":M.quicksort,
            "b":M.bubble,
            "s":M.selection,
            "c":M.cocktail,
            "j":M.bogo,
            "o":M.oddeven,
            "k":M.shell,
            "l":M.comb,
            "i":M.insertion,
            "m":M.mergetd,
            "r":M.radixlsd,
            "x":M.counting,
            "y":M.cycle,
            "h":M.heap,
            "w":M.circle,
            "g":M.gnome,
            "u":M.binaryinsertion,
            "p":M.pancake,
            "d":M.permutation,
            "n":M.strand}

    current = ""

    while True:
        # Frame Rate
        clock.tick(15)

        # Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:                    
                    for name,func in keys.items():
                        if current == name:
                            M.setup(s[0]/arr_length,s)
                            func()
                            pygame.time.wait(500)
                    
                else:
                    current = chr(event.key)

        # User changes array length
        # UP: +10
        # DOWN: -10
        # RIGHT: +1
        # LEFT: -1
        if pygame.key.get_pressed()[pygame.K_UP] or pygame.key.get_pressed()[pygame.K_DOWN] or pygame.key.get_pressed()[pygame.K_RIGHT] or pygame.key.get_pressed()[pygame.K_LEFT]:

            # Change array length
            events = pygame.key.get_pressed()
            arr_length += (10 if events[pygame.K_UP] else (1 if events[pygame.K_RIGHT] else (-10 if events[pygame.K_DOWN] else (-1 if events[pygame.K_LEFT] else 0))))

            if arr_length < 2:
                arr_length = 2

            # Re-initialise
            M = methods(fps,arr_length,clock,screen,smallfont,draw_bars)
            keys = {"q":M.quicksort,"b":M.bubble,"s":M.selection,"c":M.cocktail,"j":M.bogo,"o":M.oddeven,"k":M.shell,"l":M.comb,"i":M.insertion,"m":M.mergetd,"r":M.radixlsd,"x":M.counting,"y":M.cycle,"h":M.heap,"w":M.circle,"g":M.gnome,"u":M.binaryinsertion,"p":M.pancake,"d":M.permutation,"n":M.strand}
            
            show = Show_array(arr_length,(300,200))

        # Drawing
        screen.fill((0,0,0))

        screen.blit(head1,(50,50))
        screen.blit(head2,(50,200))
        screen.blit(head3,(750,140))

        show.draw(screen,[640,200],[740,440],labels)

        for i in typelist:
            screen.blit(i[0],i[1])

        letter = bigfont.render(str(current),True,(0,255,0))
        screen.blit(letter,letter.get_rect(center=[i/2 for i in s]))

        pygame.display.flip()

if __name__ == "__main__":
    main()
