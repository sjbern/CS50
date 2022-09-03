import sys
import random
from pyfiglet import Figlet

if len(sys.argv) == 1:
    randomFont = True
    font_r = random.choice(list)

elif len(sys.argv)== 3 and sys.argv[1] == '-f' or sys.argv[1] == '--font': 
    randomFont = False
    font_r = sys.argv[2]

else:
    sys.exit("Invalid Usage")

if randomFont == False:
    try:
        figlet = Figlet()
        list = figlet.getFonts()
        figlet.setFont(font=font_r)
        print(figlet.renderText(input("")))
    except:
        print("Invalid Usage")
        sys.exit(1)