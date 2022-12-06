import game
import state
import random
from gameTree import expectimax


class main():

        def __init__(self, game, state) -> None:
                self.game = game
                self.state = state



        def playGame(self, state):

                while not state.isOver():

                        if state.turns:
                                action = expectimax.getAction()
                                state = state.ParseAction(action, state.turns)
                        else:
                                random_actions = state.get_possible_actions()
                                action = random.choice(random_actions)
                                state = state.ParseAction(action, state.turn)

                
                        


        
        