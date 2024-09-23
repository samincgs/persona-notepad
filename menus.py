import tkinter as tk


class Menu(tk.Menu):
    def __init__(self, parent):
        super().__init__(parent, tearoff=0) # add tearoff
      
class FileMenu(Menu):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.add_command(label='New', command='')
        self.add_command(label='Open', command='')
        self.add_command(label='Save', command='')
        self.add_command(label='Save As', command='')
        self.add_command(label='Exit', command='')
        
class EditMenu(Menu):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.add_command(label='Undo', command='')
        self.add_command(label='Redo', command='')
        
        
class FormatMenu(Menu):
    def __init__(self, parent):
        super().__init__(parent)
        
        # additional submenus
        self.font_menu = Menu(self)
        self.font_size_menu = Menu(self)
        
        self.add_command(label='Word Wrap: On') # TODO add a variable controlling on and off
        
        self.add_cascade(label='Font', menu=self.font_menu)
        self.add_cascade(label='Font Size', menu=self.font_size_menu)
        
class ColorMenu(Menu):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.add_command(label='White', command='')
        self.add_command(label='Black', command='')
        self.add_command(label='Red', command='')