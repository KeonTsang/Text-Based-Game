
from colorama import Fore, Style

there_are_enemies = Style.BRIGHT + Fore.LIGHTRED_EX + "(!) " + Fore.RESET + "There are " + Fore.RED + "ENEMIES " + Fore.RESET + "here!"


battle_screen_dim = Fore.RED + Style.DIM + """

                                                                       
_______                                                                
\  ___ `'.                _..._                 __.....__              
 ' |--.\  \             .'     '.   .--./)  .-''         '.            
 | |    \  '           .   .-.   . /.''\\  /     .-''"'-.  `. .-,.--.  
 | |     |  '    __    |  '   '  || |  | |/     /________\   \|  .-. | 
 | |     |  | .:--.'.  |  |   |  | \`-' / |                  || |  | | 
 | |     ' .'/ |   \ | |  |   |  | /("'`  \    .-------------'| |  | | 
 | |___.' /' `" __ | | |  |   |  | \ '---. \    '-.____...---.| |  '-  
/_______.'/   .'.''| | |  |   |  |  /'""'.\ `.             .' | |      
\_______|/   / /   | |_|  |   |  | ||     ||  `''-...... -'   | |      
             \ \._,\ '/|  |   |  | \'. __//                   |_|      
              `--'  `" '--'   '--'  `'---'                             

""" + Fore.YELLOW + Style.DIM + """                               __
                              /  \        
                             / || \  
                            /  ||  \  
                           /   ||   \  
                          /          \ 
                         /     ()     \ 
                        /______________\ """ + Fore.RESET + Style.RESET_ALL + """ 
"""

battle_screen_bright = Style.NORMAL + Fore.RED + """

                                                                       
_______                                                                
\  ___ `'.                _..._                 __.....__              
 ' |--.\  \             .'     '.   .--./)  .-''         '.            
 | |    \  '           .   .-.   . /.''\\  /     .-''"'-.  `. .-,.--.  
 | |     |  '    __    |  '   '  || |  | |/     /________\   \|  .-. | 
 | |     |  | .:--.'.  |  |   |  | \`-' / |                  || |  | | 
 | |     ' .'/ |   \ | |  |   |  | /("'`  \    .-------------'| |  | | 
 | |___.' /' `" __ | | |  |   |  | \ '---. \    '-.____...---.| |  '-  
/_______.'/   .'.''| | |  |   |  |  /'""'.\ `.             .' | |      
\_______|/   / /   | |_|  |   |  | ||     ||  `''-...... -'   | |      
             \ \._,\ '/|  |   |  | \'. __//                   |_|      
              `--'  `" '--'   '--'  `'---'                             

""" + Style.NORMAL + Fore.YELLOW + """                               __
                              /  \        
                             / || \  
                            /  ||  \  
                           /   ||   \  
                          /          \ 
                         /     ()     \ 
                        /______________\ """ + Fore.RESET  + Style.RESET_ALL + """
"""

bad_ending = """
You black out onto the floor, swallowed by the ooze....


Confused, you awake from a slumber, bruised and battered.
Your name is unknown to you, but you know that you are someone of importance.
You find yourself in a room, with an odd sense of familiarity.

The gentle ring of a PA system chimes:
"Good morning sir, at your service."

The PA system chimes once more - it's a slogan:
"A helping hand - for a better tomorrow." . . .
"""

good_ending = """
You walk out of the lab through the fire exit.

Ah! sunlight, so warm, so healing!

Stephy comes over to you and asks you what your going to do now.

You take a moment to think about it, what are you going to do?
After a long while, you finally decide.

You may not know who you were, where you came from or anything, but you do know you want to start again.
You tell Stephy that you will start a new life, with all of your new friends.
Stephy seems to like this plan, as does everyone else.

And altogether you walk off into the horizon . . .
"""

true_ending1 = """
'Let me tell you everything...

You were the lead scientists here at the lab, you conducted experiements,
awful experiments on people.
See all your new 'friends'? - Every single one of them is an experiment of yours.
But I can see you have changed now, and become friends with us instead of treating us
like lab rats.'"""

true_ending2 = """
After hearing the story Stephy comes over to you and asks you what to do next?
You pause for a moment to take it all in and think.
After a while you come up with an answer.

You decide to stay here at the lab, re build with help from your new friends,
to further the research of humanity in a more humane way.

You hope all the good you can do will make up for the wrong you have done.
You and your new friends began work at once, to build for bigger things . . .
"""

the_end = """
▄▄▄█████▓  ██░ ██  ▓█████    ▓█████   ███▄    █  ▓█████▄ 
▓  ██▒ ▓▒ ▓██░ ██▒ ▓█   ▀    ▓█   ▀   ██ ▀█   █  ▒██▀ ██▌
▒ ▓██░ ▒░ ▒██▀▀██░ ▒███      ▒███    ▓██  ▀█ ██▒ ░██   █▌
░ ▓██▓ ░  ░▓█ ░██  ▒▓█  ▄    ▒▓█  ▄  ▓██▒  ▐▌██▒ ░▓█▄   ▌
  ▒██▒ ░  ░▓█▒░██▓ ░▒████▒   ░▒████▒ ▒██░   ▓██░ ░▒████▓ 
  ▒ ░░     ▒ ░░▒░▒ ░░ ▒░ ░   ░░ ▒░ ░ ▓ ▒░   ▒ ▒   ▒▒▓  ▒ 
    ░      ▒ ░▒░ ░  ░ ░  ░    ░ ░  ░ ░ ░░   ░ ▒░  ░ ▒  ▒ 
  ░        ░  ░░ ░    ░         ░      ░   ░ ░   ░ ░  ░ 
           ░  ░  ░    ░  ░      ░   ░         ░     ░    
                                               ░      
"""

the_end_question = """
▄▄▄█████ ▓ ██░ ██  ▓█████    ▓█████   ███▄    █  ▓█████▄   ▄████████▓ 
▓  ██▒ ▓ ▒▓██░ ██▒ ▓█   ▀    ▓█   ▀   ██ ▀█   █  ▒██▀ ██▌ ░▓▀▓░  ░▓██░
▒ ▓██░ ▒ ░▒██▀▀██░ ▒███      ▒███    ▓██  ▀█ ██▒ ░██   █▌   ░ ▄████▓▒░
░ ▓██▓ ░  ░▓█ ░██  ▒▓█  ▄    ▒▓█  ▄  ▓██▒  ▐▌██▒ ░▓█▄   ▌    ░▓▓░   ░
  ▒██▒ ░  ░▓█▒░██▓ ░▒████▒   ░▒████▒ ▒██░   ▓██░ ░▒████▓    ░▓██░░
  ▒ ░░     ▒ ░░▒░▒ ░░ ▒░ ░   ░░ ▒░ ░ ▓ ▒░   ▒ ▒   ▒▒▓  ▒    ▒░░▓░▒
    ░      ▒ ░▒░ ░  ░ ░  ░    ░ ░  ░ ░ ░░   ░ ▒░  ░ ▒  ▒    ░  ▒  ░
  ░        ░  ░░ ░    ░         ░       ░   ░ ░   ░ ░  ░   ░  ░   ░
           ░  ░  ░    ░  ░      ░  ░          ░     ░          ░
                                              ░      
"""

you_died = """
▓██   ██▓  ▒█████    █    ██    ▓█████▄   ██▓ ▓█████  ▓█████▄  ▐██▌
 ▒██  ██▒ ▒██▒  ██▒  ██  ▓██▒   ▒██▀ ██▌ ▓██▒ ▓█   ▀  ▒██▀ ██▌ ▐██▌
  ▒██ ██░ ▒██░  ██▒ ▓██  ▒██░   ░██   █▌ ▒██▒ ▒███    ░██   █▌ ▐██▌
  ░ ▐██▓░ ▒██   ██░ ▓▓█  ░██░   ░▓█▄   ▌ ░██░ ▒▓█  ▄  ░▓█▄   ▌ ▓██▒
  ░ ██▒▓░ ░ ████▓▒░ ▒▒█████▓    ░▒████▓  ░██░ ░▒████▒ ░▒████▓  ▒▄▄ 
   ██▒▒▒  ░ ▒░▒░▒░  ░▒▓▒ ▒ ▒     ▒▒▓  ▒  ░▓   ░░ ▒░ ░  ▒▒▓  ▒  ░▀▀▒
 ▓██ ░▒░    ░ ▒ ▒░  ░░▒░ ░ ░     ░ ▒  ▒   ▒ ░  ░ ░  ░  ░ ▒  ▒  ░  ░
 ▒ ▒ ░░   ░ ░ ░ ▒    ░░░ ░ ░     ░ ░  ░   ▒ ░    ░     ░ ░  ░     ░
 ░ ░          ░ ░      ░           ░      ░      ░  ░    ░     ░
 ░ ░                             ░                     ░      
"""

game_over = """
  ▄████   ▄▄▄        ███▄ ▄███▓ ▓█████     ▒█████    ██▒   █▓ ▓█████   ██▀███  
 ██▒ ▀█▒ ▒████▄     ▓██▒▀█▀ ██▒ ▓█   ▀    ▒██▒  ██▒ ▓██░   █▒ ▓█   ▀  ▓██ ▒ ██▒
▒██░▄▄▄░ ▒██  ▀█▄   ▓██    ▓██░ ▒███      ▒██░  ██▒  ▓██  █▒░ ▒███    ▓██ ░▄█ ▒
░▓█  ██▓ ░██▄▄▄▄██  ▒██    ▒██  ▒▓█  ▄    ▒██   ██░   ▒██ █░░ ▒▓█  ▄  ▒██▀▀█▄  
░▒▓███▀▒  ▓█   ▓██▒ ▒██▒   ░██▒ ░▒████▒   ░ ████▓▒░    ▒▀█░   ░▒████▒ ░██▓ ▒██▒
 ░▒   ▒   ▒▒   ▓▒█░ ░ ▒░   ░  ░ ░░ ▒░ ░   ░ ▒░▒░▒░     ░ ▐░   ░░ ▒░ ░ ░ ▒▓ ░▒▓░
  ░   ░    ▒   ▒▒ ░ ░  ░      ░  ░ ░  ░     ░ ▒ ▒░     ░ ░░    ░ ░  ░   ░▒ ░ ▒░
░ ░   ░    ░   ▒    ░      ░       ░      ░ ░ ░ ▒        ░░      ░      ░░   ░ 
      ░        ░  ░        ░       ░  ░       ░ ░         ░      ░  ░    ░     
                                                         ░                     
"""