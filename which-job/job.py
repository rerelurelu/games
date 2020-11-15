import tkinter as tk


job = ["TANK", "HEALER", "DPS"]


def click_btn():
    pts = 0
    for i in range(7):
        if bvar[i].get():
            pts += 1
        text.delete("1.0", tk.END)

        if pts < 3:
            text.insert("1.0", f"<診断結果>\nあなたの適正ジョブは{job[0]}です。")
        elif pts < 6:
            text.insert("1.0", f"<診断結果>\nあなたの適正ジョブは{job[1]}です。")
        else:
            text.insert("1.0", f"<診断結果>\nあなたの適正ジョブは{job[2]}です。")


root = tk.Tk()
root.title("Which job?")
root.resizable(False, False)

canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()

image = tk.PhotoImage(file="./images/sumire.png")
canvas.create_image(400, 300, image=image)

button = tk.Button(text="診断する", font=(None, 32), bg="lightgreen", command=click_btn)
button.place(x=400, y=480)

text = tk.Text(width=40, height=5, font=(None, 16))
text.place(x=320, y=30)

bvar = [None] * 7
cbtn = [None] * 7
item = [
    "みんなを引っ張っていくのが好き",
    "みんなを支えるのが好き",
    "自分で決着をつけたい",
    "かっこいいのが好き",
    "可愛いのが好き",
    "攻撃したい",
    "回復したい",
]

for i in range(7):
    bvar[i] = tk.BooleanVar()
    bvar[i].set(False)
    cbtn[i] = tk.Checkbutton(text=item[i], font=(None, 12), variable=bvar[i], bg="#dfe")
    cbtn[i].place(x=400, y=160 + 40 * i)

root.mainloop()
