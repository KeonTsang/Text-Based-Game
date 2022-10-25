import player
from monsters.monster import Monster
from colorama import Fore
from items import item_init


class Stethoscope(Monster):

    def __init__(self):
        super(Stethoscope, self).__init__("Stephy", 15, 5, 1, 0.05, Fore.LIGHTMAGENTA_EX, item_init.stethoscope)

    def execute_talk(self):
        if self.getPhase() == 1:
            print(f"\nYou told {self.name} it is great at listening to hearts!")
            print(f"{self.name}: " + self.colour + " 'Thank you! Maybe I could try listening to yours!'" + Fore.RESET)
            self.setPhase(2)
        else:
            print(f"\nYou complement {self.name} again!")
            print(f"{self.name}: " + self.colour + "'Thanks friend!'" + Fore.RESET)

    def execute_action(self):
        if self.getPhase() == 1:
            print(f"\nYou try to get {self.name} to measure your heart beat!")
            print(f"{self.name}: " + self.colour + "'Woah I barely know you!'" + Fore.RESET)
        else:
            print(f"\nYou let the {self.name} measure your heart beat!")
            print(f"{self.name}: " + self.colour + "'You have a great beat partner!'" + Fore.RESET)
            self.setPhase(3)

    def execute_attack(self):
        weapon = player.current_weapon
        damage = weapon.attack()
        print(f"\nYou dealt {damage} to {self.name} using your {weapon.name}!")
        print(f"{self.name}: " + self.colour + "'Owww!!! That hurts!'" + Fore.RESET)
        self.damage(damage)
        self.setPhase(1)

    def spare(self):
        print(f"\nYou spared {self.name}")
        print(f"{self.name}: " + self.colour + "'That was fun! We should do this again sometime! Bye now!'" + Fore.RESET)
        self.setSpared()
        player.karma += 1

    def print_description(self):
        description = f"\n{self.name} the Stethoscope appeared!\n\n{self.name}: " + self.colour + "'Stephy is my name, measuring heart beats is my game!'\n" + Fore.RESET
        image = """                 
          (   )   (   )  
           | |     | |   
           \ \     / /   
            \ \   / /    
             \ \_/ /     
          ___ \   /      
         [: )]  \ \      
          | |    | |     
           \ \   | |     
            \ \_/ /      
             \___/       
                         """
        print(description, image)
        self.display_health()
        print("\nWhat will you do?")
