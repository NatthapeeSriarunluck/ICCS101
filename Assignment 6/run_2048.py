# ICCS101 - Intro to Programming
# Author: Sunsern Cheamanunkul
# Date: Feb 25, 2015

from tkinter import Tk, Canvas
import random
from tkinter import messagebox as tkMessageBox
import t2048

class Tile(Canvas):
    """ UI for each tile """
    def __init__(self, master, width=0, height=0, **kwargs):
        self.width = width
        self.height = height
        Canvas.__init__(self, master, width=self.width, height=self.height)
        self.create_rectangle(0, 0, width, height, width=5)
        self.textObj = self.create_text(width/2, 
                                        height/2, 
                                        font=kwargs['font'],
                                        text=" ")

    def setText(self, s):
        self.itemconfigure(self.textObj, text=s)

    def getText(self):
        return self.itemcget(self.textObj, 'text')

    def pack(self, *args, **kwargs):
        Canvas.pack(self, *args, **kwargs)
        self.pack_propagate(False)

    def grid(self, *args, **kwargs):
        Canvas.grid(self, *args, **kwargs)
        self.grid_propagate(False)

class Game2048:
    def __init__(self, master, num_rows, num_cols):
        self.tiles = {}
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.master = master
        w = int(root.winfo_width() / num_cols)
        h = int(root.winfo_height() / num_rows)
        for i in range(num_rows):
            for j in range(num_cols):
                self.tiles[(i,j)] = Tile(master,
                                         width=w,
                                         height=h,
                                         padx=40,
                                         pady=40,
                                         font=("Helvetica", 32))
                self.tiles[(i,j)].grid(row=i, column=j)
        self.reset()

    def _setBoard(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.tiles[(i,j)].setText(board[i][j])
        self.master.update()

    def _getBoard(self):
        board = []
        for i in range(self.num_rows):
            temp = []
            for j in range(self.num_cols):
                temp.append(self.tiles[(i,j)].getText())
            board.append(temp)
        return board

    def _gen_number(self, board):
        ''' Generates a new number. 
        If there is still a space on the board, return
          { 
            num: the new number,
            row: row number,
            col: col number
          } 
        Otherwise, return None 
        '''
        num = random.randint(0,10)
        # Custom distribution
        if num < 8: num = 2
        else: num = 4
        # find an empty space to spawn
        potential = t2048.emptyPos(board)
        # no more move
        if len(potential) == 0:
            print("No potential locations")
            return None
        # sample a location from the potential positions
        loc = random.choice(potential)
        return {'num': str(num), 'row': loc[0], 'col': loc[1]}

    def reset(self):
        # create an empty board
        board = []
        for i in range(self.num_rows):
            board.append([' '] * self.num_cols)
        # add one number
        c = self._gen_number(board)
        if c is not None:
            board[c['row']][c['col']] = c['num']
        self._setBoard(board)

    def keypress(self, event):
        k = event.char.lower()
        if k in ['w','a','s','d']:
            board = self._getBoard()
            if k == 'w': 
                changed, board = t2048.doKeyUp(board)
            elif k == 'a':
                changed, board = t2048.doKeyLeft(board)
            elif k == 's':
                changed, board = t2048.doKeyDown(board)
            elif k == 'd':
                changed, board = t2048.doKeyRight(board)
            if changed:
                c = self._gen_number(board)
                # Add new number if possible
                if c is not None:
                    board[c['row']][c['col']] = c['num']
                    self._setBoard(board)
            # Check game over
            if t2048.isGameOver(board):
                self.gameOver()
        elif k == 'r':
            self.reset()

    def gameOver(self):
        tkMessageBox.showinfo("Game Over", "Game Over!")
        self.reset()

#####

root = Tk()

# Main UI config
root.title = "2048"
root.minsize(width=400, height=400)
root.resizable(width=False, height=False)
root.update()

num_rows = 4
num_cols = 4
main = Game2048(root, num_rows, num_cols)

# keybinding
root.bind("<Key>", main.keypress)

print("Use 'w','a','s','d' to play. Press 'r' to reset")

root.mainloop()
