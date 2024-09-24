import tkinter as tk
from tkinter import filedialog
from settings import *


class Menu(tk.Menu):
    def __init__(self, parent):
        super().__init__(parent, tearoff=0) # add tearoff
      
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
        self.textarea.delete(1.0, tk.END) # use 1.0 because this is how you indicate the first line (1 -> first line, 0 -> position of character)
        
    def exit(self):
        self.parent.master.quit()
        
    def open(self):
        opened_file = filedialog.askopenfilename(defaultextension='.txt',filetypes=[('Text Files', '*.txt')])
        self.current_file = opened_file
        if opened_file:
            f = open(opened_file, mode='r')
            self.new()
            file_data = f.read()
            self.textarea.insert(text=file_data, index=1.0)
            f.close()
    
    def save(self):
        if self.current_file:
            f = open(self.current_file, 'w')
            f.write(self.textarea.get(1.0, tk.END))
            f.close()
        else:
            self.save_as()
     
    def save_as(self):
        save_file = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[('Text Files', '.txt')])
        if save_file:
            self.current_file = save_file
            f = open(save_file, 'w')
            f.write(self.textarea.get(1.0, tk.END))
            f.close()
        
class EditMenu(Menu):
    def __init__(self, parent, textarea):
        super().__init__(parent)
        self.textarea = textarea
        
        self.add_command(label='Undo', command='')
        self.add_command(label='Redo', command='')
        
        
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
        self.entryconfig(0, label=f'Word Wrap: {self.word_wrap_str}')
        
class ColorMenu(Menu):
    def __init__(self, parent, textarea):
        super().__init__(parent)
        self.textarea = textarea
        
        self.add_command(label='White', command=self.turn_white)
        self.add_command(label='Black', command=self.turn_black)
        self.add_command(label='Red', command=self.turn_red)
        
    def turn_white(self):
        self.textarea.configure(text_color='black', fg_color='white')
        
    def turn_black(self):
        self.textarea.configure(text_color='white', fg_color='black')
        
    def turn_red(self):
       self.textarea.configure(text_color='white', fg_color='red')