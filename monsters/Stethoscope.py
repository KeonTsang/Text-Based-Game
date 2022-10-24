from monsters import Monster


class stethoscope(Monster):

    def __init__(self):
        Monster.__init__(self, "Stephy", 20, 7)

    def phase1(self):
        command = input(f"ATTACK {self.name}\nTALK to {self.name}\nSPARE {self.name}")

        return True

