# Import pygame
import pygame
from state import state
from game import game

# Import any controls 
from pygame.locals import(
    K_ESCAPE,
    QUIT,
    KEYDOWN,
)

class graphics:
    def __init__(self, game, state):
        self.game = game
        self.state = state
    
    def showScreen(self):
        pygame.init()

        # Constants for the screen
        SCREEN_WIDTH = 1280
        SCREEN_HEIGHT = 720

        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        # Run until terminal state
        running = True
        while running:

            # Check for ESC or Quit
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                elif event.type == QUIT:
                    running = False

            # White background
            screen.fill((255, 255, 255))


            # Computer Tokens
            # Represent tokens as multiple ovals of different colors, with a number on each one determining how much you have
            pygame.draw.ellipse(screen, (0, 0, 0), (50, 20, 160, 100))
            pygame.draw.ellipse(screen, (7, 3, 252), (50, 140, 160, 100))
            pygame.draw.ellipse(screen, (252, 3, 15), (50, 260, 160, 100))
            pygame.draw.ellipse(screen, (38, 166, 51), (50, 380, 160, 100))
            pygame.draw.ellipse(screen, (0, 0, 0), (50, 500, 160, 100), 5)

            # Add text on each of the cards from card metadata
            
            # Include a counter that has how many prestige points you have
            # Deck 1
            pygame.draw.rect(screen, (128, 111, 64), pygame.Rect(250, 70, 70, 100))
            pygame.draw.rect(screen, (128, 111, 64), pygame.Rect(350, 40, 120, 170))
            pygame.draw.rect(screen, (128, 111, 64), pygame.Rect(500, 40, 120, 170))
            pygame.draw.rect(screen, (128, 111, 64), pygame.Rect(650, 40, 120, 170))

            tier1 = " ".join([(str(card) + " ") for card in state.table[0]])
            tier1 = tier1.split(" ");
            cardFont = pygame.font.SysFont(None, 24);
            cardText = cardFont.render(tier1[0], True, (0, 0, 0))
            screen.blit(cardText, (240, 70))
            # Deck 2
            pygame.draw.rect(screen, (128, 111, 64), pygame.Rect(250, 270, 70, 100))
            pygame.draw.rect(screen, (128, 111, 64), pygame.Rect(350, 240, 120, 170))
            pygame.draw.rect(screen, (128, 111, 64), pygame.Rect(500, 240, 120, 170))
            pygame.draw.rect(screen, (128, 111, 64), pygame.Rect(650, 240, 120, 170))
            # Deck 3
            pygame.draw.rect(screen, (128, 111, 64), pygame.Rect(250, 470, 70, 100))
            pygame.draw.rect(screen, (128, 111, 64), pygame.Rect(350, 440, 120, 170))
            pygame.draw.rect(screen, (128, 111, 64), pygame.Rect(500, 440, 120, 170))
            pygame.draw.rect(screen, (128, 111, 64), pygame.Rect(650, 440, 120, 170))
            # Player tokens
            pygame.draw.ellipse(screen, (0, 0, 0), (860, 20, 160, 100))
            pygame.draw.ellipse(screen, (7, 3, 252), (860, 140, 160, 100))
            pygame.draw.ellipse(screen, (252, 3, 15), (860, 260, 160, 100))
            pygame.draw.ellipse(screen, (38, 166, 51), (860, 380, 160, 100))
            pygame.draw.ellipse(screen, (0, 0, 0), (860, 500, 160, 100), 5)
            # Prestige counter
            font = pygame.font.SysFont(None, 48)
            # These counts need to be updated with information from the cards + player metadata
            prestigeComputer = font.render('0', True, (0, 0, 0))
            screen.blit(prestigeComputer, (113, 645))

            prestigePlayer = font.render('0', True, (0, 0, 0))
            screen.blit(prestigePlayer, (923, 645))
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(85, 620, 80, 80), 5)
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(895, 620, 80, 80), 5)

            # Flip the display
            pygame.display.flip()

        pygame.quit()