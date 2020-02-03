from gpiozero import Robot
import gpiozero
from time import sleep
import curses


bobo = Robot(left=(4,14), right=(17,18))

# Get the curses window, turn off echoing of keyboard to screen, turn on
# instant (no waiting) key response, and use special values for cursor keys
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

try:
    while True:
        char = screen.getch()
        if char == ord('q'):
            break
        elif char == curses.KEY_UP:
           bobo.forward()
           sleep(1)
           bobo.stop()
           print("key: up", sep='\n')
        elif char == curses.KEY_RIGHT:
           bobo.right()
           sleep(1)
           bobo.stop()
           print("key: right", sep='\n')
        elif char == curses.KEY_LEFT:
           bobo.left()
           sleep(1)
           bobo.stop()
           print("key: left", sep='\n')
        elif char == curses.KEY_DOWN:
           bobo.backward()
           sleep(1)
           bobo.stop()
           print("key: down", sep='\n')
finally:
    #Close down curses properly, inc turn echo back on!
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()