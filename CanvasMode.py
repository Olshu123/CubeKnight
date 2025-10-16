import tkinter as tk

class CanvasMode:
    def __init__(self, root, text_bg, terminal_mode):
        self.root = root
        self.terminal_mode = terminal_mode
        
        self.canvas = tk.Canvas(root, bg=text_bg, highlightthickness=0)
        self.canvas.bind('<Button-1>', self.switch_to_terminal)
    
    def switch_to_terminal(self, event):
        self.hide()
        self.terminal_mode.show()
        self.terminal_mode.clear_console()
    
    def draw_shapes(self):
        self.canvas.delete("all")
        self.canvas.create_rectangle(50, 50, 150, 100, fill='lightblue', outline='blue', width=2)
        self.canvas.create_oval(200, 50, 300, 100, fill='lightgreen', outline='green', width=2)
        self.canvas.create_line(50, 120, 350, 120, fill='red', width=3)
        self.canvas.create_polygon([50, 150, 100, 180, 50, 180], fill='yellow', outline='orange', width=2)
    
    def hide(self):
        self.canvas.pack_forget()
    
    def show(self):
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.draw_shapes()