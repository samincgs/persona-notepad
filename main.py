import customtkinter as ctk
import tkinter as tk
from menus import Menu, FileMenu, EditMenu, FormatMenu, ColorMenu


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode('light')
        self.title('Notepad')
        self.geometry('800x600')
        self.resizable(False, False)
        
        # main menu
        menu = Menu(self) #TODO Change the color of the menu so it looks better
        
        # submenus
        filemenu = FileMenu(menu) # filemenu
        editmenu = EditMenu(menu) # edit menu
        formatmenu = FormatMenu(menu) # format menu
        colormenu = ColorMenu(menu)
        
        # add submenus to the main menu
        menu.add_cascade(label='File', menu=filemenu)
        menu.add_cascade(label='Edit', menu=editmenu)
        menu.add_cascade(label='Format', menu=formatmenu)
        menu.add_cascade(label='Color', menu=colormenu)
        
        # add main menu to root App
        self.config(menu=menu)
     
if __name__ == '__main__':
    app = App()
    app.mainloop()
        
        