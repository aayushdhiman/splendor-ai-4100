import game
import ActionUtil

class node:

    def __init__(self, game : game, value : float, children : list, isMaxNode: bool):
        self.game = game
        self.value = value
        self.children = children
        self.isMaxNode = isMaxNode

        
        # if self.state.getTurns == True:
        #     self.isMaxNode = True
        #     for action in ActionUtil.get_possible_actions(self.getGame.getGameState.getComputerHand):
                
        # else:
        #     self.isMaxNode = False

        # if depth == 3:
        #     self.value = game.newGame.eval
        # else:
        #     if self.state.getTurns == True:
        #         self.value = self.getMaxChild.getValue
        #     else:
        #         self.value = self.getMinChild.getValue
        

        

        

    def getGame(self):
        return self.game

    def getChildren(self):
        return self.children

    def getValue(self):
        return self.value

    def getIsMaxNode(self):
        return self.isMaxNode

    def getMaxChild(self):
        ans = float('-inf')
        for child in self.getChildren:
            if child.getValue >= ans:
                ans = child.getValue
        return ans

    def getMinChild(self):
        ans = float('inf')
        for child in self.getChildren:
            if child.getValue <= ans:
                ans = child.getValue
        return ans
    


    def setValue(self, num):
        self.value = num

rootNode = node(
    game.newGame,
    None,
    [],
    game.newGame.
)
    
