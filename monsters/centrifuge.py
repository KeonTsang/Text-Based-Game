import player
from monsters.monster import Monster
from colorama import Fore


class Centrifuge(Monster):

    def __init__(self):
        super(Centrifuge, self).__init__("C3ntri", 40, 15, 10, 0.01, Fore.LIGHTYELLOW_EX)

    def execute_spare(self):
        if self.getPhase() == 3:
            self.spare()
        else:
            print(f"You cannot spare {self.name} yet!")

    def execute_talk(self):
        if self.getPhase() == 1:
            print("\nYou say: " + Fore.LIGHTWHITE_EX +
                  f"Sup {self.name}, your rhymes are sick, how did you get so good, what's your trick?" + Fore.RESET)
            print(f"{self.name}: " + self.colour +
                  "'Thanks dude, though there is no trick, you just gotta poor your heart out to be sick!'" + Fore.RESET)
            self.setPhase(2)
        elif self.getPhase() == 2:
            print(f"\nYou offer the word 'game' to {self.name}!")
            print(f"{self.name}: " + self.colour + "'HELL YEAH!\n'" +
                  "I told you last year that I burned you in a flame, Now this year, I’m wreckin average in the game!" +
                  Fore.RESET)
            self.setPhase(3)

    def execute_action(self):
        print(f"\nYou try to take the mic from {self.name}!")
        print(f"{self.name}: " + self.colour +
              "'Yo Dawg, that wasn't cool! Get out of here with your drool!'" + Fore.RESET)

    def execute_attack(self):
        weapon = player.current_weapon
        damage = weapon.attack()
        print(f"\nYou dealt {damage} to {self.name} using your {weapon.name}!")
        print(f"{self.name}: " + self.colour +
              "'Come on man, That hurts real bad, you better stop it now or your gonna make me mad!'" + Fore.RESET)
        self.damage(damage)
        self.setPhase(1)

    def spare(self):
        print(f"\nYou spared {self.name}")
        print(f"{self.name}: " + self.colour +
              "'Cheers dawg, that was great, hope to see you soon my new mate!'" + Fore.RESET)
        self.setSpared()
        player.karma += 1

    def print_description(self):
        description = (f"\n{self.name} the Centrifuge appeared!\n\n{self.name}: " + self.colour +
                       "'My beats 'n' rhymes are fly, you better get outta here 'fore you die!'\n" + Fore.RESET)
        if (self.getPhase() == 2):
            description = (f"\n{self.name} the Centrifuge appeared!\n\n{self.name}: " + self.colour +
                           "'I told you last year that I burned you in a flame, " +
                           "Now this year, I’m wreckin the average in my ... - What should I say here?'\n" + Fore.RESET)
        image = """              
       ________   
      /       /\   
     /       /  \  
    /_______/  ^|  
   /        \ ^>|  
  /   ---    \  |  
  |  (   )   |_/|  
  |  (   )   |  /  
  |   ---    | /   
  |__________|/    
              """
        print(description, image)
        self.display_health()
        print("\nWhat will you do?")
