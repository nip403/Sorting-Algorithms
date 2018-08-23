import pygame

class mode_selector:
    def __init__(self,topleft_pos,dimensions,font):
        self.pos = topleft_pos
        self.dimensions = dimensions
        self.font = font

        self.modes = [
            "Random",
            "Ascending",
            "Descending",
            "Nearly Sorted"
        ]

        self.mode = "Random"
        self.text = self.font.render(self.mode,True,(0,0,0))
        
        self.rect = pygame.Rect(self.pos,self.dimensions)
        self.surf = pygame.Surface(self.dimensions)
        self.draw_in()

    def draw_in(self):
        self.surf.fill((30,144,255))
        pygame.draw.rect(self.surf,(148,0,211),(0,0,*self.dimensions),5)
        self.surf.blit(self.text,self.text.get_rect(center=[i/2 for i in self.dimensions]))

    def change_mode(self,mouse):
        changed = False
        
        if pygame.Rect(mouse[0]-1,mouse[1]-1,2,2).colliderect(self.rect):
            self.mode = self.modes[self.modes.index(self.mode)+1 if self.modes.index(self.mode)+1 < len(self.modes) else 0]
            changed = True
            
        self.text = self.font.render(self.mode,True,(0,0,0))
        self.draw_in()

        return changed

    def draw(self,surf):
        surf.blit(self.surf,(self.pos))

    @property
    def state(self):
        return self.modes.index(self.mode)

    @state.setter
    def state(self,new):
        if isinstance(new,int) and 0 <= new < 4:
            self.mode = self.modes[new]
        elif new in self.modes:
            self.mode = new

    @state.deleter
    def state(self):
        self.mode = self.modes[0]
