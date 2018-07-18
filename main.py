from algs import methods

import pygame
import random
import sys

arr_length = 200
fps = 20

s = [1000,700]
bar_thickness = s[0]/arr_length

pygame.init()
screen = pygame.display.set_mode(s,0,32)
clock = pygame.time.Clock()
pygame.display.set_caption("Sorting Algorithms by NIP")

bigfont = pygame.font.SysFont("Garamond MS",140)
medfont = pygame.font.SysFont("Garamond MS",40)
smallfont = pygame.font.SysFont("Garamond MS",20)

def main():
    M = methods(fps,arr_length,clock,screen,smallfont,draw_bars)
    
    head1 = medfont.render("Enter Sorting Type:",True,(255,255,255))
    head2 = medfont.render("Types:",True,(255,255,255))

    typelist = [[smallfont.render(i,True,(255,255,255)),[80,340+(p*15)]] for p,i in enumerate([
        "Bubble Sort: 'b'",
        "Quick Sort: 'q'",
        "Insertion Sort: 'i'",
        "Cocktail Shaker Sort: 'c'",
        "Bogo Sort: 'j'",
        "Odd-Even Sort: 'o'",
        "Shell Sort: 's'",
        "Comb Sort: 'l'",
        "Gnome Sort: 'g'",
        "Merge (TD) Sort: 'm'",
        "Radix (LSD) Sort: 'r'"
    ])]
    
    keys = {
        "q":M.quicksort,
        "b":M.bubble,
        "i":M.insertion,
        "c":M.cocktail,
        "j":M.bogo,
        "o":M.oddeven,
        "s":M.shell,
        "l":M.comb,
        "g":M.gnome,
        "m":M.mergetd,
        'r':M.radixlsd
    }

    current = ""

    while True:
        screen.fill((0,0,0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:

                    M.setup(bar_thickness,s)
                    
                    for name,func in keys.items():
                        if current == name:
                            func()
                        
                else:
                    current = chr(event.key)

        screen.blit(head1,(50,50))
        screen.blit(head2,(50,300))

        for i in typelist:
            screen.blit(i[0],i[1])

        letter = bigfont.render(str(current),True,(0,255,0))
        screen.blit(letter,letter.get_rect(center=[i/2 for i in s]))

        pygame.display.flip()

if __name__ == "__main__":
    main()
