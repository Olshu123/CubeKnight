import tkinter as tk

SIZEX = 1080
SIZEY = 640

root = tk.Tk()
root.title("CubeKnight")
root.resizable(False, False)
root.geometry(str(SIZEX)+'x'+str(SIZEY))
canvas = tk.Canvas(root, width=SIZEX, height=SIZEY, bg="black")
canvas.pack(pady=0)

def say(text, size, brightness=250): 
    text_id = canvas.create_text(SIZEX-SIZEX*0.95, SIZEY-SIZEY*0.06, text=text, font=("Times New Roman", size), fill=f'#{brightness:02x}{brightness:02x}{brightness:02x}', anchor="sw")
    def animate(brightness):
        canvas.itemconfig(text_id, fill=f'#{brightness:02x}{brightness:02x}{brightness:02x}')
        brightness -= 2
        if brightness >= 0:
            root.after(20, lambda: animate(brightness))    
    root.after(2000, lambda: animate(brightness))

# Прямоугольник
canvas.create_rectangle(50, 30, 150, 80, fill="red", outline="black")
# Овал
canvas.create_oval(50, 100, 150, 150, fill="green", outline="black")
# Линия
canvas.create_line(50, 180, 150, 230, width=3, fill="blue")
# Многоугольник (треугольник)
canvas.create_polygon(200, 50, 170, 100, 230, 100, fill="orange", outline="black")


#Анимация
d = canvas.create_rectangle(50, 50, 100, 100, fill="red")


def move_figure_step():
    canvas.move(d, 8, 8)
    root.after(8, move_figure_step)



# Текст
say('Великий Математик', 65)
move_figure_step()
root.mainloop()