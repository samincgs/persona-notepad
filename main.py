import customtkinter as ctk
from menus import Menu, FileMenu, EditMenu, FormatMenu, ColorMenu
from settings import *


class App(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color='black')
        ctk.set_appearance_mode('light')
        self.title('Notepad')
        self.geometry('800x600')
        self.minsize(300, 200)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        # main menu
        menu = Menu(self) #TODO Change the color of the menu so it looks better

        # main textarea
        self.textarea = ctk.CTkTextbox(self, wrap='word', corner_radius=CORNER_RADIUS, font=(DEFAULT_FONT, DEFAULT_FONT_SIZE), spacing2=DEFAULT_LINE_HEIGHT, bg_color=BACKGROUND_COLORS['WHITE'])
        
        # submenus
        self.filemenu = FileMenu(menu, textarea=self.textarea) # filemenu
        self.editmenu = EditMenu(menu, textarea=self.textarea) # edit menu
        self.formatmenu = FormatMenu(menu, textarea=self.textarea) # format menu
        self.colormenu = ColorMenu(menu, textarea=self.textarea) # color menu
        
        # add keybinds
        # Always add event keybinds to main application
        self.configure_keybinds()
        
        # add submenus to the main menu
        menu.add_cascade(label='File', menu=self.filemenu)
        menu.add_cascade(label='Edit', menu=self.editmenu)
        menu.add_cascade(label='Format', menu=self.formatmenu)
        menu.add_cascade(label='Color', menu=self.colormenu)
        
        # add main menu to root App
        self.config(menu=menu)
        self.textarea.grid(row=0, column=0, sticky='nsew')
    
    def configure_keybinds(self):
        # for saving functionality
        self.bind('<Control-s>', self.filemenu.save)
     
if __name__ == '__main__':
    app = App()
    app.mainloop()
        
        