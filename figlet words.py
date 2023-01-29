import sys
from pyfiglet import Figlet
import random

fonts = ["3-d", "3x5", "5lineoblique", "slant",
"5lineoblique","alphabet", "banner3-D",
"doh", "isometric1", "letters",
"alligator", "bubble", "rectangles"]

f = Figlet()
try:
    if len(sys.argv) > 3:
        pass
    elif sys.argv[1] != "-f":
        sys.exit("Invalid Usage")
    elif sys.argv[2] not in fonts:
        sys.exit("Invalid Usage")
except IndexError:
    pass


if len(sys.argv) < 2:
    f = Figlet(font = random.choice(fonts))
    text = input("Input: ")
    print("Output: \n",f.renderText(text))
elif len(sys.argv) >= 2 and sys.argv[1] == "-f" or sys.argv[1] == "--font":
    f = Figlet(font = sys.argv[2])
    text = input("Input: ")
    print("Output: \n",f.renderText(text))
