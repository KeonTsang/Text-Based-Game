from monsters import Monster


class stethoscope(Monster):

    def __init__(self, name):
        Monster.__init__(self, name, 20)
