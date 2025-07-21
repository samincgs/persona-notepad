import customtkinter as ctk
import pygame
from persona_notepad.menus import Menu, FileMenu, EditMenu, FormatMenu, DarkModeMenu, PersonaMenu
from persona_notepad.config import *


class App(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color='black')
        
        pygame.init()
        pygame.mixer.init()
        
        music = pygame.mixer.Sound('data/music/Heaven.mp3')
        music.set_volume(0.1)
        
        music.play()
        
        self.title('Notepad')
        self.geometry('800x600')
        self.minsize(800, 600)
        # self.iconbitmap('empty.ico')
                            
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        # image = ctk.CTkImage(light_image=Image.open('joker.png'), size=(250, 420))
        
        # main menu
        menu = Menu(self) #TODO Change the color of the menu so it looks better

        # main textarea
        self.textarea = ctk.CTkTextbox(self, wrap='word', corner_radius=CORNER_RADIUS, font=(DEFAULT_FONT, DEFAULT_FONT_SIZE), spacing2=DEFAULT_LINE_HEIGHT, bg_color=BACKGROUND_COLORS['WHITE'])
        # submenus
        self.file_menu = FileMenu(menu, textarea=self.textarea) # filemenu
        self.edit_menu = EditMenu(menu, textarea=self.textarea) # edit menu
        self.format_menu = FormatMenu(menu, textarea=self.textarea) # format menu
        self.darkmode_menu = DarkModeMenu(menu, textarea=self.textarea) # color menu
        self.persona_menu = PersonaMenu(menu, textarea=self.textarea) # color menu
        
        # img_label = ctk.CTkLabel(master=self.textarea, image=image, text='')
        
        # add submenus to the main menu
        menu.add_cascade(label='File', menu=self.file_menu)
        menu.add_cascade(label='Edit', menu=self.edit_menu)
        menu.add_cascade(label='Format', menu=self.format_menu)
        menu.add_cascade(label='Dark Mode', menu=self.darkmode_menu)
        menu.add_cascade(label='Persona 4', menu=self.persona_menu)
        
        # add keybinds
        # Always add event keybinds to main application
        self.configure_keybinds()
        
        # img_label.grid(row=0, column=0, sticky='se')
        
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
        
        