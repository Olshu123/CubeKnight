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
        
        # Заголовок
        tk.Label(title_bar, text="Терминал Windows", bg=self.title_bg, fg='white', font=('Segoe UI', 10)).pack(side=tk.LEFT, padx=10)
        tk.Label(title_bar, bg=self.title_bg).pack(side=tk.LEFT, expand=True)
        
        # Кнопка закрытия
        buttons_frame = tk.Frame(title_bar, bg=self.title_bg)
        buttons_frame.pack(side=tk.RIGHT)
        
        close_btn = tk.Label(buttons_frame, text="x", bg=self.title_bg, fg='white', font=('Segoe UI', 14), cursor='hand2', padx=12)
        close_btn.pack()
        close_btn.bind('<Button-1>', lambda e: self.root.quit())
        close_btn.bind('<Enter>', lambda e: close_btn.config(bg='#E81123'))
        close_btn.bind('<Leave>', lambda e: close_btn.config(bg=self.title_bg))
        
        # Перемещение окна
        title_bar.bind('<Button-1>', self.start_move)
        title_bar.bind('<B1-Motion>', self.on_move)
    
    def start_move(self, event):
        self.start_x = event.x
        self.start_y = event.y
    
    def on_move(self, event):
        x = self.root.winfo_x() + event.x - self.start_x
        y = self.root.winfo_y() + event.y - self.start_y
        self.root.geometry(f"+{x}+{y}")


class TerminalMode:
    def __init__(self, root, text_bg, text_fg, canvas_mode):
        self.root = root
        self.text_bg = text_bg
        self.text_fg = text_fg
        self.canvas_mode = canvas_mode
        self.current_output = None
        
        self.text_area = tk.Text(
            root,
            wrap=tk.WORD,
            bg=text_bg,
            fg=text_fg,
            insertbackground='white',
            selectbackground='#404040',
            font=('Consolas', 10),
            borderwidth=0,
            highlightthickness=0
        )
        self.text_area.pack(fill=tk.BOTH, expand=True)
        
        self.text_area.bind('<Return>', self.on_enter)
        self.text_area.bind('<Key>', self.on_key_press)
        self.text_area.focus_set()
    
    def on_enter(self, event):
        command = self.get_current_command()
        self.execute_command(command)
        return "break"
    
    def on_key_press(self, event):
        if self.current_output and event.keysym not in ['Shift_L', 'Shift_R', 'Control_L', 'Control_R', 'Alt_L', 'Alt_R']:
            self.clear_console()
    
    def get_current_command(self):
        text = self.text_area.get('1.0', tk.END).strip()
        return text.split('\n')[-1] if text else ""
    
    def clear_console(self):
        self.text_area.delete('1.0', tk.END)
        self.current_output = None
    
    def execute_command(self, command):
        command = command.lower().strip()
        
        if command == "help":
            self.show_output("Доступные команды:\nhelp - показать справку\nclear - очистить экран\nexit - выйти\ncanvas - перейти в режим холста")
        elif command == "clear":
            self.clear_console()
        elif command == "exit":
            self.root.quit()
        elif command == "canvas":
            self.hide()
            self.canvas_mode.show()
        elif command == "":
            self.clear_console()
        else:
            self.show_output(f"'{command}' не является командой")
    
    def show_output(self, text):
        self.text_area.delete('1.0', tk.END)
        self.text_area.insert(tk.END, text)
        self.current_output = text
    
    def hide(self):
        self.text_area.pack_forget()
    
    def show(self):
        self.text_area.pack(fill=tk.BOTH, expand=True)
        self.text_area.focus_set()


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


if __name__ == "__main__":
    TerminalTextEditor().run()