from algs import methods
from showarr import Show_array
import pygame
import sys

# Options
arr_length = 200
fps = 0
draw_bars = True

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

# User Instructions
print("\n |----                                                    ----| \n")
print("  To download the code: go to:")
print("\thttps://github.com/nip403/Sorting-Algorithms\n")
print("  To select the sorting mode, press the letters under \"Types\".")
print("  To run, press ENTER.")
print("  To toggle between drawing bars and dots, press BACKSPACE.")
print("\n  To change the list size, use either:")
print("\tUP and DOWN arrows (these change the size by 10).")
print("\tLEFT and RIGHT arrows (these change the size by 1).")
print("\n |----                                                    ----| \n")

def main():
    global arr_length,draw_bars

    # Initialisations
    M = methods(fps,clock,screen,smallfont,draw_bars,s)

    all_sorts = {
        "b":["Bubble",M.bubble],
        "q":["Quick",M.quicksort],
        "s":["Selection",M.selection],
        "c":["Cocktail Shaker",M.cocktail],
        "j":["Bogo",M.bogo],
        "o":["Odd-Even",M.oddeven],
        "k":["Shell",M.shell],
        "l":["Comb",M.comb],
        "i":["Insertion",M.insertion],
        "m":["Merge (TopDown)",M.mergetd],
        "r":["Radix (LSD)",M.radixlsd],
        "x":["Counting",M.counting],
        "y":["Cycle",M.cycle],
        "h":["Heap",M.heap],
        "w":["Circle",M.circle],
        "g":["Gnome",M.gnome],
        "u":["Binary Insertion",M.binaryinsertion],
        "p":["Pancake",M.pancake],
        "d":["Permutation",M.permutation],
        "n":["Strand",M.strand],
        "v":["Bucket",M.bucket],
        "e":["MinMax",M.minmax],
        "t":["Merge (BottomUp)",M.mergebu]
    }
    
    head1 = medfont.render("Enter Sorting Type:",True,(140,140,255))
    head2 = medfont.render("Types:",True,(255,255,140))
    head3 = medfont.render("Array:",True,(255,255,255))

    show = Show_array(arr_length,(300,200),draw_bars)
    typelist = [[labels.render(f"{all_sorts[i][0]} Sort: '{i}'",True,(255,145,140)),[120,130+(p*23)]] for p,i in enumerate(all_sorts.keys())]

    current = "b"

    while True:
        # Frame Rate
        clock.tick(15)

        # Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:                    
                    for name,data in all_sorts.items():
                        if current == name:
                            pygame.display.set_caption(f"Sorting Algorithms by NIP |||| List size: {arr_length} |||| Sorting method: {data[0]} Sort")
                            M.setup(arr_length)
                            
                            data[1]()
                            pygame.time.wait(500)
                            pygame.display.set_caption("Sorting Algorithms by NIP")

                elif event.key == pygame.K_BACKSPACE:
                    draw_bars = not draw_bars
                    setattr(M,"bars",not getattr(M,"bars"))
                    setattr(show,"bars",not getattr(show,"bars"))
                    
                else:
                    current = chr(event.key) if chr(event.key) in "abcdefghijklmnopqrstuvwxyz1234567890" else current
                    
        # User changes array length
        if pygame.key.get_pressed()[pygame.K_UP] or pygame.key.get_pressed()[pygame.K_DOWN] or pygame.key.get_pressed()[pygame.K_RIGHT] or pygame.key.get_pressed()[pygame.K_LEFT]:

            # Change array length
            events = pygame.key.get_pressed()
            arr_length += (10 if events[pygame.K_UP] else (1 if events[pygame.K_RIGHT] else (-10 if events[pygame.K_DOWN] else (-1 if events[pygame.K_LEFT] else 0))))

            if arr_length < 4:
                arr_length = 4

            # Re-initialise
            M.setup(arr_length)
            show = Show_array(arr_length,(300,200),draw_bars)

        # Drawing
        screen.fill((0,0,0))

        pygame.draw.rect(screen,(140,140,140),(s[0]/2-100,s[1]/2-100,200,200),10)
        pygame.draw.rect(screen,(100,100,100),(s[0]/2-90,s[1]/2-90,180,180),0)

        for i in [[100,100],[-100,-100],[100,-100],[-100,100]]:
            pygame.draw.circle(screen,(140,140,140),list(map(int,(s[0]/2+i[0],s[1]/2+i[1]))),4,0)

        screen.blit(head1,(40,40))
        screen.blit(head2,(60,90))
        screen.blit(head3,(750,140))

        show.draw(screen,[640,200],[740,440],labels)

        for i in typelist:
            screen.blit(i[0],i[1])

        letter = bigfont.render(str(current),True,(0,255,0))
        screen.blit(letter,letter.get_rect(center=[i/2 for i in s]))

        pygame.display.flip()

if __name__ == "__main__":
    main()
