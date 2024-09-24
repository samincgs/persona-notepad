import tkinter as tk
from tkinter import filedialog

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
        
        # additional submenus
        self.font_menu = Menu(self)
        self.font_size_menu = Menu(self)
        
        self.add_command(label='Word Wrap: On') # TODO add a variable controlling on and off
        
        self.add_cascade(label='Font', menu=self.font_menu)
        self.add_cascade(label='Font Size', menu=self.font_size_menu)
        
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