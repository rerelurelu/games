import tkinter as tk
from PIL import ImageTk
import random


def click_btn():
    label['text'] = random.choice(['great fortune', 'lucky day', 'slightly good luck', 'bad luck'])
    label.update()


root = tk.Tk()
root.title('omikuji')
root.resizable(False, False)

canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()

image = ImageTk.PhotoImage(file='images/sky.jpg')
canvas.create_image(400, 300, image=image)

label = tk.Label(root, text='What\'s your fortune today?', font=(None, 200), bg='white')
label.place(x=320, y=100)

button = tk.Button(root, text='Fortune telling', font=(None, 36), fg='skyblue', command=click_btn)
button.place(x=340, y=400)

root.mainloop()
