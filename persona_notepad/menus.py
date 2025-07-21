import tkinter as tk
import customtkinter as ctk
from tkinter import filedialog
from PIL import Image
from persona_notepad.config import *

IGNORE_KEYS = {
'Shift_L', 'Shift_R',
'Control_L', 'Control_R',
'Alt_L', 'Alt_R',
'Caps_Lock',
'Meta_L', 'Meta_R', 'Super_L', 'Super_R', 'Win_L', 'Win_R',
'Left', 'Right', 'Up', 'Down',
'Home', 'end-1c',
'Page_Up', 'Page_Down',
'Insert',
'Num_Lock', 'Scroll_Lock', 'Pause',
'Print',
'Menu',
'Escape',
'Tab'  
}
        

class Menu(tk.Menu):
    def __init__(self, parent):
        super().__init__(parent, tearoff=0) 
        
    def delete_text(self):
        self.textarea.delete("1.0", 'end-1c') # use "1.0" because this is how you indicate the first line (1 -> first line, 0 -> position of character)
        
    def retrieve_text(self):
        return self.textarea.get("1.0", 'end-1c')
      
class FileMenu(Menu):
    def __init__(self, parent, textarea):
        super().__init__(parent)
        self.parent = parent # main menu
        self.textarea = textarea
        self.current_file = None

        self.add_command(label='New', command=self.new)
        self.add_command(label='Open', command=self.open)
        self.add_command(label='Save', command=self.save)
        self.add_command(label='Save As', command=self.save_as)
        self.add_command(label='Exit', command=self.exit)
        
    def new(self):
        self.delete_text()
        
    def exit(self):
        self.parent.master.quit()
        
    def open(self):
        opened_file = filedialog.askopenfilename(defaultextension='.txt',filetypes=[('Text Files', '*.txt')])
        if opened_file:
            self.current_file = opened_file
            f = open(opened_file, mode='r')
            self.new()
            file_data = f.read()
            self.textarea.insert(text=file_data, index="1.0")
            f.close()
    
    def save(self, event=None):
        if self.current_file:
            f = open(self.current_file, 'w')
            text = self.retrieve_text()
            f.write(text)
            f.close()
        else:
            self.save_as()
     
    def save_as(self):
        save_file = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[('Text Files', '.txt')])
        if save_file:
            self.current_file = save_file
            f = open(save_file, 'w')
            f.write(self.retrieve_text())
            f.close()
        
class EditMenu(Menu): #TODO: ADD REDO AND UNDO Functionality
    def __init__(self, parent, textarea):
        super().__init__(parent)
        self.textarea = textarea
        
        self.undo_stack = []
        self.redo_stack = []
        
        self.add_command(label='Undo', command=self.undo)
        self.add_command(label='Redo', command=self.redo)
        
    def undo(self, event=None):
        if len(self.undo_stack) > 1:
            current_text = self.retrieve_text()
            self.redo_stack.append(current_text)
            
            self.undo_stack.pop()
            text = self.undo_stack[-1]
            
            self.delete_text()
            self.textarea.insert(index="1.0", text=text)
        else:
            self.delete_text()
        
        
    def redo(self, event=None):
        if self.redo_stack:
            current_text = self.retrieve_text()
            self.undo_stack.append(current_text)
            text = self.redo_stack.pop()
            self.delete_text()
            self.textarea.insert(index="1.0", text=text)
        
        
    def track(self, event=None):
        if event.keysym not in IGNORE_KEYS:
            text = self.retrieve_text()
            self.undo_stack.append(text)
            self.redo_stack.clear()
        
        
class FormatMenu(Menu):
    def __init__(self, parent, textarea):
        super().__init__(parent)
        self.textarea = textarea
        self.word_wrap = 'word'
        self.word_wrap_str = 'On'
        self.fonts = FONTS
        self.font_sizes = FONT_SIZES
        self.line_heights = LINE_HEIGHTS
        
        self.current_font = DEFAULT_FONT
        self.current_size = DEFAULT_FONT_SIZE
        self.current_line_height = DEFAULT_LINE_HEIGHT
        
        # additional submenus
        self.font_menu = Menu(self)
        self.font_size_menu = Menu(self)
        self.line_height_menu = Menu(self)
        
        # format menu
        self.add_command(label=f'Word Wrap: {self.word_wrap_str}', command=self.word_wrap_toggle) # TODO add a variable controlling on and off
        
        # font menu TODO use a for loop to simplify
        self.font_menu.add_command(label=f'{self.fonts[0]}', command=lambda f=self.fonts[0]: self.change_font(f)) # Arial
        self.font_menu.add_command(label=f'{self.fonts[1]}', command=lambda f=self.fonts[1]: self.change_font(f)) # Comic Sans MS
        self.font_menu.add_command(label=f'{self.fonts[2]}', command=lambda f=self.fonts[2]: self.change_font(f)) # Times New Roman
        self.font_menu.add_command(label=f'{self.fonts[3]}', command=lambda f=self.fonts[3]: self.change_font(f) ) # MS Gothic
         
        # font size menu TODO use a for loop to simplify
        self.font_size_menu.add_command(label=f'{self.font_sizes[0]}', command=lambda fs=self.font_sizes[0]: self.change_size(fs)) # 12
        self.font_size_menu.add_command(label=f'{self.font_sizes[1]}', command=lambda fs=self.font_sizes[1]: self.change_size(fs)) # 16
        self.font_size_menu.add_command(label=f'{self.font_sizes[2]}', command=lambda fs=self.font_sizes[2]: self.change_size(fs)) # 20
        self.font_size_menu.add_command(label=f'{self.font_sizes[3]}', command=lambda fs=self.font_sizes[3]: self.change_size(fs)) # 24
        self.font_size_menu.add_command(label=f'{self.font_sizes[4]}', command=lambda fs=self.font_sizes[4]: self.change_size(fs)) # 28
        self.font_size_menu.add_command(label=f'{self.font_sizes[5]}', command=lambda fs=self.font_sizes[5]: self.change_size(fs)) # 32
        
        # line height menu
        self.line_height_menu.add_command(label=f'{self.line_heights[0]}', command=lambda lh=self.line_heights[0]: self.change_line_height(lh))
        self.line_height_menu.add_command(label=f'{self.line_heights[1]}', command=lambda lh=self.line_heights[1]: self.change_line_height(lh))
        self.line_height_menu.add_command(label=f'{self.line_heights[2]}', command=lambda lh=self.line_heights[2]: self.change_line_height(lh))
        
        self.add_cascade(label='Font', menu=self.font_menu)
        self.add_cascade(label='Font Size', menu=self.font_size_menu)
        self.add_cascade(label='Line Height', menu=self.line_height_menu)
        
    # pass through each individual font if button is pressed and change the font
    def change_font(self, font):
        self.current_font = font
        self.textarea.configure(font=(self.current_font, self.current_size))
        
    def change_size(self, size):
        self.current_size = size
        self.textarea.configure(font=(self.current_font, self.current_size))
    
    def change_line_height(self, line_height):
        self.current_line_height = line_height
        self.textarea.configure(spacing2=self.current_line_height)
        
    def word_wrap_toggle(self):
        # change word wrap
        self.word_wrap = 'none' if self.word_wrap == 'word' else 'word'
        # change the word wrap string
        self.word_wrap_str = 'On' if self.word_wrap == 'word' else 'Off'
        
        # configure it in the GUI
        self.textarea.configure(wrap=self.word_wrap)
        self.entryconfig(0, label=f'Word Wrap: {self.word_wrap_str}') # configure the menu item at a certain index
        
class DarkModeMenu(Menu):
    def __init__(self, parent, textarea):
        super().__init__(parent)
        self.textarea = textarea
        self.color_mode = DEFAULT_COLOR_MODE
        ctk.set_appearance_mode(self.color_mode)
        
        self.add_command(label='System', command=self.turn_system)
        self.add_command(label='Dark', command=self.turn_dark)
        self.add_command(label='Light', command=self.turn_light)
    
    def turn_system(self):
        self.color_mode = 'system'
        ctk.set_appearance_mode(self.color_mode)
        
    def turn_dark(self):
        self.color_mode = 'dark'
        ctk.set_appearance_mode(self.color_mode)
        
    def turn_light(self):
        self.color_mode = 'light'
        ctk.set_appearance_mode(self.color_mode)
        
class PersonaMenu(Menu):
    def __init__(self, parent, textarea):
        super().__init__(parent)
        self.textarea = textarea
        self.current_image = 'mc'
        
        self.image = ctk.CTkImage(light_image=Image.open(f'data/images/{self.current_image}.png'), dark_image=Image.open(f'data/images/{self.current_image}.png'), size=(200, 420))
        self.img_label = ctk.CTkLabel(master=self.textarea, image=self.image, text='')
        
        self.img_label.grid(row=0, column=0, sticky='se', pady=20, padx=40)
        
        self.add_command(label='Joker', command=lambda: self.set_current_image('joker'))
        self.add_command(label='Ann', command=lambda: self.set_current_image('ann'))
        self.add_command(label='Ryuji', command=lambda: self.set_current_image('ryuji'))
        
    def set_current_image(self, character):
        self.current_image = character
        self.set_image()
        
    def set_image(self):
        img = Image.open(f'data/images/{self.current_image}.png')
        img.thumbnail((200, 420))  # Keeps aspect ratio, fits box
        self.image = ctk.CTkImage(light_image=img, dark_image=img, size=img.size)
        self.img_label.configure(image=self.image)
        