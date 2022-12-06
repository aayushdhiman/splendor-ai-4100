import game
import state
import random
from gameTree import expectimax


class main():

        def __init__(self, game, state, turns = True) -> None:
                self.game = game
                self.state = state
                self.turns = turns


        def playGame(self, game, state, turns):

                while not state.isOver():
                        if turns:
                                action = expectimax.getAction()
                                state.ParseAction(action)
                        else:
                                random_actions = state.get_possible_actions()
                                action = 
                                state.ParseAction

                        


        
        