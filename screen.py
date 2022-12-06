# Import pygame
import pygame
from state import state
from gameTree import expectimax
import random
from game import game
import csv

# Import any controls 
from pygame.locals import(
    K_ESCAPE,
    QUIT,
    KEYDOWN,
    K_SPACE,
    K_q,
)

class graphics:
    def __init__(self, auto : bool):
        testGame = game()
        self.state = testGame.getStartingState()
        self.expectimax = expectimax()
        self.wasNothing = False
        self.auto = auto
        
    
    def showScreen(self):
        pygame.init()

        # Constants for the screen
        SCREEN_WIDTH = 1280
        SCREEN_HEIGHT = 720

        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        # Run until terminal state
        self.running = not self.state.isOver()[0]

        while self.running:

            if self.state.isOver()[0]:
                print("GAME OVER! " + self.state.isOver()[1] + " Wins!")
                break
            # Check for ESC or Quit
            
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    elif event.key == K_SPACE:
                        self.GenerateTurn()
                        

                    if event.key == K_q:
                        print(self.state.getPlayerHand().deckTokens)
                     

                elif event.type == QUIT:
                    running = False

            if(self.auto):
                self.GenerateTurn()

            # Update state
            # self.updateState();

            # White background
            screen.fill((255, 255, 255))


            # Computer Tokens
            # Represent tokens as multiple ovals of different colors, with a number on each one determining how much you have
            pygame.draw.ellipse(screen, (0, 0, 0), (50, 20, 160, 100))
            pygame.draw.ellipse(screen, (7, 3, 252), (50, 140, 160, 100))
            pygame.draw.ellipse(screen, (252, 3, 15), (50, 260, 160, 100))
            pygame.draw.ellipse(screen, (38, 166, 51), (50, 380, 160, 100))
            pygame.draw.ellipse(screen, (0, 0, 0), (50, 500, 160, 100), 5)

            tokenFont = pygame.font.SysFont(None, 100)

            computer_black = tokenFont.render(str(self.state.getComputerHand().getTokens().get('black')), True, (255, 255, 255))
            screen.blit(computer_black, (112, 40))

            computer_blue = tokenFont.render(str(self.state.getComputerHand().getTokens().get('blue')), True, (255, 255, 255))
            screen.blit(computer_blue, (112, 160))

            computer_red = tokenFont.render(str(self.state.getComputerHand().getTokens().get('red')), True, (255, 255, 255))
            screen.blit(computer_red, (112, 280))

            computer_green = tokenFont.render(str(self.state.getComputerHand().getTokens().get('green')), True, (255, 255, 255))
            screen.blit(computer_green, (112, 400))

            computer_white = tokenFont.render(str(self.state.getComputerHand().getTokens().get('white')), True, (0, 0, 0))
            screen.blit(computer_white, (112, 520))
            
            # Add text on each of the cards from card metadata
            
            # Include a counter that has how many prestige points you have
            # Deck 1
            pygame.draw.rect(screen, (128, 111, 64), pygame.Rect(250, 70, 70, 100))
            pygame.draw.rect(screen, (128, 111, 64), pygame.Rect(350, 40, 120, 170))
            pygame.draw.rect(screen, (128, 111, 64), pygame.Rect(500, 40, 120, 170))
            pygame.draw.rect(screen, (128, 111, 64), pygame.Rect(650, 40, 120, 170))

            deckFont = pygame.font.SysFont(None, 24)
            cardFont = pygame.font.SysFont(None, 20)

            deck_text = deckFont.render("Tier 1", True, (0, 0, 0))
            screen.blit(deck_text, (262, 100))

            tier1card1 = self.state.GetCardAtTableLocation([0, 0])

            if tier1card1 is not None:

                cardText = cardFont.render(str(tier1card1), True, (0, 0, 0))
                screen.blit(cardText, (360, 70))

                tier1card1_prestige = self.state.table[0][0].prestige
                cardPrestige = cardFont.render("Prestige: " + str(tier1card1_prestige), True, (0, 0, 0))
                screen.blit(cardPrestige, (375, 100))
            
            tier1card2 = self.state.GetCardAtTableLocation([0, 1])

            if tier1card2 is not None:

                cardText = cardFont.render(str(tier1card2), True, (0, 0, 0))
                screen.blit(cardText, (510, 70))

                tier1card2_prestige = self.state.table[0][1].prestige
                cardPrestige = cardFont.render("Prestige: " + str(tier1card2_prestige), True, (0, 0, 0))
                screen.blit(cardPrestige, (525, 100))

            tier1card3 = self.state.GetCardAtTableLocation([0, 2])
            if tier1card3 is not None:

                
                cardText = cardFont.render(str(tier1card3), True, (0, 0, 0))
                screen.blit(cardText, (660, 70))
                tier1card3_prestige = tier1card3.prestige
                cardPrestige = cardFont.render("Prestige: " + str(tier1card3_prestige), True, (0, 0, 0))
                screen.blit(cardPrestige, (675, 100))
            # Deck 2
            pygame.draw.rect(screen, (128, 111, 64), pygame.Rect(250, 270, 70, 100))
            pygame.draw.rect(screen, (128, 111, 64), pygame.Rect(350, 240, 120, 170))
            pygame.draw.rect(screen, (128, 111, 64), pygame.Rect(500, 240, 120, 170))
            pygame.draw.rect(screen, (128, 111, 64), pygame.Rect(650, 240, 120, 170))
            
            deck_text = deckFont.render("Tier 2", True, (0, 0, 0))
            screen.blit(deck_text, (262, 300))

            tier2card1 = self.state.GetCardAtTableLocation([1, 0])
            if type(tier2card1)is not None:
                cardText = cardFont.render(str(tier2card1), True, (0, 0, 0))
                screen.blit(cardText, (360, 270))
                tier2card1_prestige = self.state.table[1][0].prestige
                cardPrestige = cardFont.render("Prestige: " + str(tier2card1_prestige), True, (0, 0, 0))
                screen.blit(cardPrestige, (375, 300))
            
            tier2card2 = self.state.GetCardAtTableLocation([1, 1])

            if tier2card2 is not None:

                cardText = cardFont.render(str(tier2card2), True, (0, 0, 0))
                screen.blit(cardText, (510, 270))

                tier2card2_prestige = self.state.table[1][1].prestige
                cardPrestige = cardFont.render("Prestige: " + str(tier2card2_prestige), True, (0, 0, 0))
                screen.blit(cardPrestige, (525, 300))
            
            tier2card3 = self.state.GetCardAtTableLocation([1, 2])
            if tier2card3 is not None:

            
                cardText = cardFont.render(str(tier2card3), True, (0, 0, 0))
                screen.blit(cardText, (660, 270))

                tier2card3_prestige = self.state.table[1][2].prestige
                cardPrestige = cardFont.render("Prestige: " + str(tier2card3_prestige), True, (0, 0, 0))
                screen.blit(cardPrestige, (675, 300))
            # Deck 3
            pygame.draw.rect(screen, (128, 111, 64), pygame.Rect(250, 470, 70, 100))
            pygame.draw.rect(screen, (128, 111, 64), pygame.Rect(350, 440, 120, 170))
            pygame.draw.rect(screen, (128, 111, 64), pygame.Rect(500, 440, 120, 170))
            pygame.draw.rect(screen, (128, 111, 64), pygame.Rect(650, 440, 120, 170))
                        
            deck_text = deckFont.render("Tier 3", True, (0, 0, 0))
            screen.blit(deck_text, (262, 500))

            tier3card1 = self.state.GetCardAtTableLocation([2, 0])
            if tier3card1 is not None:

                
                cardText = cardFont.render(str(tier3card1), True, (0, 0, 0))
                screen.blit(cardText, (360, 470))


                tier3card1_prestige = self.state.table[2][0].prestige
                cardPrestige = cardFont.render("Prestige: " + str(tier3card1_prestige), True, (0, 0, 0))
                screen.blit(cardPrestige, (375, 500))

            tier3card2 = self.state.GetCardAtTableLocation([2, 1])
            if tier3card2 is not None:

                
                cardText = cardFont.render(str(tier3card2), True, (0, 0, 0))
                screen.blit(cardText, (510, 470))

                tier3card2_prestige = self.state.table[2][1].prestige
                cardPrestige = cardFont.render("Prestige: " + str(tier3card2_prestige), True, (0, 0, 0))
                screen.blit(cardPrestige, (525, 500))

            tier3card3 = self.state.GetCardAtTableLocation([2, 2])
            if tier3card3 is not None:

                
                cardText = cardFont.render(str(tier3card3), True, (0, 0, 0))
                screen.blit(cardText, (660, 470))

                tier3card3_prestige = self.state.table[2][2].prestige
                cardPrestige = cardFont.render("Prestige: " + str(tier3card3_prestige), True, (0, 0, 0))
                screen.blit(cardPrestige, (675, 500))
            # Player tokens
            pygame.draw.ellipse(screen, (0, 0, 0), (860, 20, 160, 100))
            pygame.draw.ellipse(screen, (7, 3, 252), (860, 140, 160, 100))
            pygame.draw.ellipse(screen, (252, 3, 15), (860, 260, 160, 100))
            pygame.draw.ellipse(screen, (38, 166, 51), (860, 380, 160, 100))
            pygame.draw.ellipse(screen, (0, 0, 0), (860, 500, 160, 100), 5)

            tokenFont = pygame.font.SysFont(None, 100)

            computer_black = tokenFont.render(str(self.state.getPlayerHand().getTokens().get('black')), True, (255, 255, 255))
            screen.blit(computer_black, (920, 40))

            computer_blue = tokenFont.render(str(self.state.getPlayerHand().getTokens().get('blue')), True, (255, 255, 255))
            screen.blit(computer_blue, (920, 160))

            computer_red = tokenFont.render(str(self.state.getPlayerHand().getTokens().get('red')), True, (255, 255, 255))
            screen.blit(computer_red, (920, 280))

            computer_green = tokenFont.render(str(self.state.getPlayerHand().getTokens().get('green')), True, (255, 255, 255))
            screen.blit(computer_green, (920, 400))

            computer_white = tokenFont.render(str(self.state.getPlayerHand().getTokens().get('white')), True, (0, 0, 0))
            screen.blit(computer_white, (920, 520))
            
            # Prestige counter
            font = pygame.font.SysFont(None, 48)
            # These counts need to be updated with information from the cards + player metadata
            prestigeComputer = font.render(str(self.state.getComputerHand().getPrestige()), True, (0, 0, 0))
            screen.blit(prestigeComputer, (114, 645))

            prestigePlayer = font.render(str(self.state.getPlayerHand().getPrestige()), True, (0, 0, 0))
            screen.blit(prestigePlayer, (924, 645))
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(85, 620, 80, 80), 5)
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(895, 620, 80, 80), 5)

            # Token pool
            pygame.draw.ellipse(screen, (0, 0, 0), (300, 625, 80, 80))
            pygame.draw.ellipse(screen, (7, 3, 252), (400, 625, 80, 80))
            pygame.draw.ellipse(screen, (252, 3, 15), (500, 625, 80, 80))
            pygame.draw.ellipse(screen, (38, 166, 51), (600, 625, 80, 80))
            pygame.draw.ellipse(screen, (0, 0, 0), (700, 625, 80, 80), 5)

            poolFont = pygame.font.SysFont(None, 20)
            black_pool = font.render(str(self.state.getPool()['black']), True, (255, 255, 255))
            screen.blit(black_pool, (330, 650))

            blue_pool = font.render(str(self.state.getPool()['blue']), True, (255, 255, 255))
            screen.blit(blue_pool, (430, 650))

            red_pool = font.render(str(self.state.getPool()['red']), True, (255, 255, 255))
            screen.blit(red_pool, (530, 650))

            green_pool = font.render(str(self.state.getPool()['green']), True, (255, 255, 255))
            screen.blit(green_pool, (630, 650))

            white_pool = font.render(str(self.state.getPool()['white']), True, (0, 0, 0))
            screen.blit(white_pool, (730, 650))

            # Flip the display
            pygame.display.flip()

        pygame.quit()
      
        return self.state

        # def updateState(newState : state):
        #     self.state = newState
    def GenerateTurn(self):
        if self.state.isPlayerTurn:
            action = self.expectimax.getAction(self.state)
            if(action['type'] == 'do_nothing'):
                if(self.wasNothing):
                    #print("GAME OVER! STALEMATE!")
                    #print(self.state.GetWinner() + " WINS!")
                    if not self.state.RefreshCards():
                        print("GAME OVER! STALEMATE!")
                        self.running = False
                    #running = False
                    self.wasNothing = False
                    
                else:
                    self.wasNothing = True
                    self.state = self.state.ParseAction(action)

            else:
                self.state = self.state.ParseAction(action)
        else:

            random_actions = self.state.get_possible_actions()
            action = random.choice(random_actions)
            if(action['type'] == 'do_nothing'):
                if(self.wasNothing):
                    if not self.state.RefreshCards():
                        print("GAME OVER! STALEMATE!")
                        self.running = False
                    self.wasNothing = False
                else:
                    self.wasNothing = True
                    self.state = self.state.ParseAction(action)
            else:
                self.state = self.state.ParseAction(action)


winner = {"Player":0, "Random Agent":0, "None" : 0};
record = []
for i in range(1):
    display = graphics(True)
    result = display.showScreen()
    winner[result.GetWinner()] += 1
    record.append([result.GetWinner(), result.playerHand.getPrestige(), result.computerHand.getPrestige()])
    
with open('record.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for i in range(len(record)):

        spamwriter.writerow(record[i])
    spamwriter.writerow(winner.items())
    
print(winner)