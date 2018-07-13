import pygame

class Display:
    def __init__(self,bar_thickness,windowsize,surface):
        self.base_colour = (255,255,255)
        self.sorting_colour = (255,0,0)
        self.thickness = bar_thickness
        self.s = windowsize
        self.screen = surface

    def draw(self,array,*highlighted,background=(0,0,0)):
        self.surface.fill(background)

        for index,item in enumerate(array):
            if not index in highlighted:
                pygame.draw.rect(self.surface,self.base_colour,(index*self.thickness,self.s[1]-(item/len(array)*self.s[1]),self.thickness,item/len(array)*self.s[1]),0)
            else:
                pygame.draw.rect(self.surface,self.sorting_colour,(index*self.thickness,self.s[1]-(item/len(array)*self.s[1]),self.thickness,item/len(array)*self.s[1]),0)
                
    def draw_other(self,font,accesses,comparisons):
        a = font.render("Array Accesses: %s" % accesses,True,(255,0,0))
        c = font.render("Array Comparisions: %s" % comparisons,True,(255,0,0))

        self.surface.blit(a,a.get_rect(topleft=[10,10]))
        self.surface.blit(c,c.get_rect(topleft=[10,30]))

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
