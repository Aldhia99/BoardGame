import pygame, sys 

class Game():
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((600,600))
    
    def input(self,event):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    def main(self):
        while True:
            for event in pygame.event.get():
                self.input(event)
    
            self.screen.fill(0)
            pygame.display.update()

if __name__=="__main__":
    game = Game()
    game.main()