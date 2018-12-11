import inspect,os,sys


#### next improvements
# 1. stop the errors when pressing other keys
# 2. include an 'exit' key to stop the script


def wait_key():
    ''' Wait for a key press on the console and return it. '''
    result = None
    if os.name == 'nt':
        import msvcrt
        result = msvcrt.getch()
    else:
        import termios
        fd = sys.stdin.fileno()

        oldterm = termios.tcgetattr(fd)
        newattr = termios.tcgetattr(fd)
        newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
        termios.tcsetattr(fd, termios.TCSANOW, newattr)

        try:
            result = sys.stdin.read(1)
        except IOError:
            pass
        finally:
            termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)

    return result

def printLines(lines):

	for line in lines:
		print(line[0] + ". " + line[1] + "\r")

#clear the screen
os.system("clear")

keys = "1234567890qwertyuiopasdfghjklzxcvbnm"
keyList = list(keys)

f = open(os.path.dirname(os.path.abspath(inspect.stack()[0][1])) + "/script.txt")
# will need to replace this with an argument, or perhaps not to keep command line simple

linePos = 0
lines = []
keysIndex = []

next = f.readline()
while next != "":
	next = next.strip()
	lines.append([])
	lines[linePos].append(keyList[linePos])
	keysIndex.append(keyList[linePos])
	lines[linePos].append(next)
	linePos = linePos + 1
	next = f.readline()

#should probably clean up empty array entries
lineTotal = len(lines)

print("Press the key to say the phrase:")
printLines(lines)

while True:
	choice = wait_key()
	keyItem = keysIndex.index(choice) 
	#need an if statement here to check if the keypress is in the range
	os.system("say -v Samantha \"" + lines[keyItem][1] + "\"")
