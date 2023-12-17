from Stack import StackGame
from time import sleep

stack = StackGame()

def is_key_pressed():
    if input('') == 't':
        stack.handleClick()


while(True):
    stack.display()
    is_key_pressed()
    stack.moveBlocks()
    sleep(1)
