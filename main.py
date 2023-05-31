from tkinter import *


def on_click(event):
    x = event.x // pixel_size
    y = event.y // pixel_size
    canvas.create_rectangle((x * pixel_size, y * pixel_size),
                            ((x + 1) * pixel_size, (y + 1) * pixel_size),
                            fill=current_color,
                            outline="")


def select_color(color):
    global current_color
    current_color = color


root = Tk()
root.title("Pixel Art Editor")

canvas_width = 400
canvas_height = 400
pixel_size = 10
current_color = "black"

canvas = Canvas(root, 
                width=canvas_width, 
                height=canvas_height, 
                bg="white")
canvas.pack()

canvas.bind("<Button-1>", on_click)

color_pallette = Frame(root)
color_pallette.pack()

colors_list = ["black", "white", "red", "green", "blue", "yellow"]

for color in colors_list:
    button = Button(
        color_pallette, 
        bg=color,
        width=2,
        command=lambda c=color: select_color(c))
    button.pack(side=LEFT)


root.mainloop()
