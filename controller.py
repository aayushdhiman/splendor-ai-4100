import game

def play(self):
                userAction = input().split()
                mainCommand = userAction[0]

                match mainCommand:
                        case "take_3":
                                try:
                                    color1 = userAction[1]  
                                    color2 = userAction[2]  
                                    color3 = userAction[3]  
                                except:
                                    print("Invalid action")  
                                self.ParseAction(self.getGameState, 
                                                 {'type': 'take_3', 
                                                  'params': (color1, color2, color3)})
                        case "take_2":
                                try:
                                    color = userAction[1]
                                except:
                                    print("Invalid action")
                                self.ParseAction(self.getGameState, 
                                                 {'type': 'take_2', 
                                                  'params': color})
                        case 'purchase':
                                try:
                                    tier = userAction[1] - 1
                                    cardNum = userAction[2] - 1
                                except:
                                    print("Invalid action")
                                self.ParseAction(self.getGameState, {'type': 'purchase',
                                                  'params': ['from_table', (tier, cardNum)]})
                                    