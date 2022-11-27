class card:

        def __init__(self, prestige, cost, color, tier):
                """
                """
                self._prestige = prestige
                self._cost = cost
                self._color = color
                self._tier = tier

        @property
        def prestige(self):
                return self._prestige
        @property
        def cost(self):
                return self._cost
        @property
        def color(self):
                return self._color
        @property
        def tier(self):
                return self._tier

        def __repr__(self) -> str:
                return "Tier " + str(self.tier) + " " + self.color + " card "

