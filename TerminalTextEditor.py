import tkinter as tk
from WindowController import WindowController
from TerminalMode import TerminalMode
from CanvasMode import CanvasMode

class TerminalTextEditor:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Терминал Windows")
        
        self.bg_color = "#1A1917"
        self.title_bg = '#000000'
        self.text_bg = "#0F0F0D"
        self.text_fg = "#FFFFFF"
        
        self.root.configure(bg=self.bg_color)
        self.root.overrideredirect(True)
        self.root.geometry("800x600+100+100")
        
        WindowController(self.root, self.bg_color, self.title_bg)
        
        self.canvas_mode = CanvasMode(self.root, self.text_bg, None)
        self.terminal_mode = TerminalMode(self.root, self.text_bg, self.text_fg, self.canvas_mode)
        self.canvas_mode.terminal_mode = self.terminal_mode
        
        self.canvas_mode.hide()
        self.root.bind('<Control-q>', lambda e: self.root.quit())
    
    def run(self):
        self.root.mainloop()