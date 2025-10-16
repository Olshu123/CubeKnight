import tkinter as tk

class WindowController:
    def __init__(self, root, bg_color, title_bg):
        self.root = root
        self.bg_color = bg_color
        self.title_bg = title_bg
        self.create_title_bar()
    
    def create_title_bar(self):
        title_bar = tk.Frame(self.root, bg=self.title_bg, height=30)
        title_bar.pack(fill=tk.X)
        
        tk.Label(title_bar, text="Терминал Windows", bg=self.title_bg, fg='white', font=('Segoe UI', 10)).pack(side=tk.LEFT, padx=10)
        tk.Label(title_bar, bg=self.title_bg).pack(side=tk.LEFT, expand=True)
        
        buttons_frame = tk.Frame(title_bar, bg=self.title_bg)
        buttons_frame.pack(side=tk.RIGHT)
        
        close_btn = tk.Label(buttons_frame, text="x", bg=self.title_bg, fg='white', font=('Segoe UI', 14), cursor='hand2', padx=12)
        close_btn.pack()
        close_btn.bind('<Button-1>', lambda e: self.root.quit())
        close_btn.bind('<Enter>', lambda e: close_btn.config(bg='#E81123'))
        close_btn.bind('<Leave>', lambda e: close_btn.config(bg=self.title_bg))
        
        title_bar.bind('<Button-1>', self.start_move)
        title_bar.bind('<B1-Motion>', self.on_move)
    
    def start_move(self, event):
        self.start_x = event.x
        self.start_y = event.y
    
    def on_move(self, event):
        x = self.root.winfo_x() + event.x - self.start_x
        y = self.root.winfo_y() + event.y - self.start_y
        self.root.geometry(f"+{x}+{y}")