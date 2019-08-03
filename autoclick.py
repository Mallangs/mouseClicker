from tkinter import *
from tkinter import ttk
from pynput.mouse import Controller

import pyautogui as pag
class MyApp:
        def __init__(self, parent):
                self.myparent = parent
                #--------Main Frame-------#
                self.mainframe = Frame(self.myparent)
                self.mainframe.pack()
                #--------   Label --------#
                self.xlabel = Label(self.mainframe,
                                    text = 'x 좌표',
                                    width = 10)
                self.xlabel.grid(row=1, column=1)

                self.ylabel = Label(self.mainframe,
                                    text = 'y 좌표',
                                    width = 10)
                self.ylabel.grid(row=2, column=1)

                self.countlabel = Label(self.mainframe,
                                        text = '카운터',
                                        width = 10)
                self.countlabel.grid(row=3, column =1)
                
                #--------   Entry --------#
                self.entry = Entry(self.mainframe,
                                   width = 15)
                self.entry.grid(row=1, column=2)

                self.entry2 = Entry(self.mainframe,
                                    width = 15)
                self.entry2.grid(row=2, column =2)
                
                self.entry3 = Entry(self.mainframe,
                                    width = 15)
                self.entry3.grid(row=3, column =2)              
                #--------   Button -------#
                self.button = Button(self.mainframe,
                                     text = 'set',
                                     command = self.setpointer)
                self.button.grid(row=1, column = 3)
                self.button2 = Button(self.mainframe,
                                      text = 'start',
                                      command = clicked)
                self.button2.grid(row=3, column = 3)
                
        def setpointer(self):
                #-------- Get mouse position------#
                global x1, y1, count
                x1 = Controller().position[0]
                y1 = Controller().position[1]
                self.entry.delete(0,"end")
                self.entry2.delete(0,"end")
                
                #-------- Set mouse position------#
                self.entry.insert(0,str(x1))
                self.entry2.insert(0,str(y1))
                count = self.entry3.get()
                if count == '':
                        self.entry3.insert(0,100)
                print(type(count),+int(count))
               
                
def clicked():
        print(x1, y1, count)

        #-------Click time--------#
        for i in range(int(count)):
                pag.moveTo(x1, y1)
                pag.click()
                print(i)
        
if __name__ == '__main__':
        root = Tk()
        myapp = MyApp(root)
        root.mainloop()
