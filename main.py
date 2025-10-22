import tkinter as tk

root = tk.Tk()
root.title("Геометрические фигуры")
root.resizable(False, False)
root.geometry("300x300")

canvas = tk.Canvas(root, width=280, height=280, bg="white")
canvas.pack(pady=10)

# Прямоугольник
canvas.create_rectangle(50, 30, 150, 80, fill="red", outline="black")

# Овал
canvas.create_oval(50, 100, 150, 150, fill="green", outline="black")

# Линия
canvas.create_line(50, 180, 150, 230, width=3, fill="blue")

# Многоугольник (треугольник)
canvas.create_polygon(200, 50, 170, 100, 230, 100, fill="orange", outline="black")

# Текст
canvas.create_text(150, 250, text="Геометрические фигуры", font=("Arial", 12))

root.mainloop()