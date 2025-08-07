import customtkinter as ctk
import pygame
from menus import Menu, FileMenu, EditMenu, FormatMenu, DarkModeMenu, PersonaMenu
from config import *

class App(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color=('#f8f9fb', '#2b2b2b'))
        
        pygame.mixer.init()
        
        self.title('Notepad')
        self.geometry(f'{SCREEN_SIZE[0]}x{SCREEN_SIZE[1]}')
        self.minsize(*SCREEN_SIZE)
                            
        self.grid_columnconfigure(0, weight=5)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        # main menu
        menu = Menu(self)

        # main textarea
        self.textarea = ctk.CTkTextbox(self, wrap='word', fg_color=BACKGROUND_COLORS, corner_radius=CORNER_RADIUS, font=(DEFAULT_FONT, DEFAULT_FONT_SIZE), spacing2=DEFAULT_LINE_HEIGHT, bg_color=BACKGROUND_COLORS, border_width=0)
   
        # submenus
        self.file_menu = FileMenu(menu, textarea=self.textarea) # filemenu
        self.edit_menu = EditMenu(menu, textarea=self.textarea) # edit menu
        self.format_menu = FormatMenu(menu, textarea=self.textarea) # format menu
        self.darkmode_menu = DarkModeMenu(menu, textarea=self.textarea, app=self) # color menu
        self.persona_menu = PersonaMenu(menu, textarea=self.textarea, app=self) # persona menu
        
        # add submenus to the main menu
        menu.add_cascade(label='File', menu=self.file_menu)
        menu.add_cascade(label='Edit', menu=self.edit_menu)
        menu.add_cascade(label='Format', menu=self.format_menu)
        menu.add_cascade(label='Dark Mode', menu=self.darkmode_menu)
        menu.add_cascade(label='Persona 5', menu=self.persona_menu)
        
        # Add all event keybinds to main application
        self.configure_keybinds()
        
        
        # add main menu to root App
        self.config(menu=menu)
        self.textarea.grid(row=0, column=0, sticky='nsew')
    
    def configure_keybinds(self):
        # for saving functionality
        self.bind('<Control-s>', self.file_menu.save)
        # for undo and redo functionality
        self.bind('<Control-z>', self.edit_menu.undo)
        self.bind('<Control-y>', self.edit_menu.redo)
        self.bind('<Key>', self.edit_menu.track)
       
if __name__ == '__main__':
    app = App()
    app.mainloop()
        
        