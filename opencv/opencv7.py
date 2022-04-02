from cProfile import label
from curses import window
import tkinter as tk
from click import command
import cv2 as cv

class App:
    def __init__(self,window,window_title):
        self.window=window
        self.window.title(window_title)
        self.window.geometry('1000x600')
        self.window.mainloop()
        self.main_menu=tk.Menu(window)
        self.file_menu=tk.Menu(self.main_menu,tearoff=0)
        self.file_menu.add_command(label="開啟檔案",command=self.open_file)
        self.file_menu.add_command(lable="儲存檔案",command=self.save_file)
        self.main_menu.add_cascade(label="檔案",menu=self.file_menu)
        self.window.config(menu=self.main_menu)
        self.window.mainloop()
    def open_file(self):
        pass
App(tk.Tk(),"OpenCv with Tkinter GUI")

