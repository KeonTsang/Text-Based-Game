
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