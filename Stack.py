from enum import Enum

class Direction(Enum):
    RIGHT = 1
    LEFT = 2

class StackGame:
    def __init__(self):
        self.result = 0
        self.blocksInStack = [[2, 3, 4, 5], [2, 3, 4, 5], [2, 3, 4, 5], [2, 3, 4, 5]]
        self.movingBlocks = [0, 1, 2, 3]
        self.movingDirection = Direction.RIGHT

    def display(self):
        stack = []
        for emptyRows in range(3):
            stack.append(8*'_')

        row = []
        for movingBlock in range(8):
            if movingBlock in self.movingBlocks:
                row.append('+')
            else:
                row.append('_')
        stack.append(''.join(row))

        for baseRow in range(4):
            row = []
            for block in range(8):
                if block in self.blocksInStack[baseRow]:
                   row.append('*')
                else:
                   row.append('_')
            stack.append(''.join(row))

        print('Result: ', self.result)
        for row in stack:
            print(row)


    def moveBlocks(self):
        if self.movingDirection == Direction.RIGHT:
            if self.movingBlocks[-1] == 7:
                self.movingDirection = Direction.LEFT
        else:
            if self.movingBlocks[0] == 0:
                self.movingDirection = Direction.RIGHT

        if self.movingDirection == Direction.RIGHT:
            self.movingBlocks = [block + 1 for block in self.movingBlocks]
        else:
            self.movingBlocks = [block - 1 for block in self.movingBlocks]

    def handleClick(self):
        blocks_to_remove = []
        for movingBlock in self.movingBlocks:
            if movingBlock not in self.blocksInStack[0]:
                blocks_to_remove.append(movingBlock)
        for block_to_remove in blocks_to_remove:
            self.movingBlocks.remove(block_to_remove)
        if len(self.movingBlocks) == 0:
            self.endGame()

        self.blocksInStack.insert(0, self.movingBlocks)
        self.blocksInStack.pop()
        self.result += 1

    def endGame(self):
        print('Koniec gry. rezulat: ', self.result)
        exit()