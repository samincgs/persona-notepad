import customtkinter as ctk
from menus import Menu, FileMenu, EditMenu, FormatMenu, ColorMenu


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode('light')
        self.title('Notepad')
        self.geometry('800x600')
        self.resizable(False, False)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        # main menu
        menu = Menu(self) #TODO Change the color of the menu so it looks better

        # main textarea
        self.textarea = ctk.CTkTextbox(self, wrap='word', corner_radius=0)
        
        # submenus
        filemenu = FileMenu(menu, textarea=self.textarea) # filemenu
        editmenu = EditMenu(menu, textarea=self.textarea) # edit menu
        formatmenu = FormatMenu(menu, textarea=self.textarea) # format menu
        colormenu = ColorMenu(menu, textarea=self.textarea)
        
        # add submenus to the main menu
        menu.add_cascade(label='File', menu=filemenu)
        menu.add_cascade(label='Edit', menu=editmenu)
        menu.add_cascade(label='Format', menu=formatmenu)
        menu.add_cascade(label='Color', menu=colormenu)
        
        # add main menu to root App
        self.config(menu=menu)
        self.textarea.grid(row=0, column=0, sticky='nsew')
     
if __name__ == '__main__':
    app = App()
    app.mainloop()
        
        