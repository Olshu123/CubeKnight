import tkinter as tk

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