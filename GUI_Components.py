import tkinter as tk
from tkinter.filedialog import askopenfilename


class MainWindow:
    def __init__(self, size: tuple, is_resizeable: bool, icon, title, bg:str):
        self.window = tk.Tk()
        self.window.geometry(f'{size[0]}x{size[1]}')
        self.window.resizable(width=is_resizeable, height=is_resizeable)
        self.window.iconbitmap(icon)
        self.window.title(title)
        self.window.config(bg=bg)


class Title:
    def __init__(self, master, text:str, color:str, font:tuple, pos:tuple, bg:str):
        self.title = tk.Label(master, text=text, fg=color, font=font, bg=bg)
        self.title.place(x=pos[0], y=pos[1], anchor=tk.CENTER)


class OutputFolder:
    def __init__(self, master, width: int, font: tuple, pos: tuple, bg: str):
        self.entry = tk.Entry(master, width=width, font=font)
        self.entry.place(x=pos[0], y=pos[1], anchor=tk.SW)

        self.button = tk.Button(master, font=font, text='...')
        self.button.place(anchor=tk.SW, x=pos[0] + 340, y=pos[1], width=70, height=30)
        self.button.bind('<Button-1>', lambda e: self.pick_folder())

        self.label = tk.Label(master, font=font, text='Output Dir:', fg='white', bg=bg)
        self.label.place(anchor=tk.SW, x=pos[0] - 130, y=pos[1])

    def pick_folder(self):
        path = askopenfilename()
        self.entry.delete(0, 'end')
        self.entry.insert(0, path)


class Timeout:
    def __init__(self, master, bg, width, pos: tuple):
        self.label = tk.Label(master=master, font=('default', 17), text='Timeout (MS):', bg=bg, fg='white')
        self.label.place(anchor=tk.SW, x=pos[0] - 130, y=pos[1])

        self.slider = tk.Scale(master, bg=bg, from_=0, to=5000, orient=tk.HORIZONTAL, length=width, highlightthickness=0, fg='white', troughcolor='white', width=20)
        self.slider.place(anchor=tk.SW, x=pos[0] + 50, y=pos[1])
        self.slider.set(2500)


class MaxThreads:
    def __init__(self, master, bg, width, pos: tuple):
        self.label = tk.Label(master=master, font=('default', 17), text='Max Threads:', bg=bg, fg='white')
        self.label.place(anchor=tk.SW, x=pos[0] - 130, y=pos[1])

        self.slider = tk.Scale(master, bg=bg, from_=0, to=300, orient=tk.HORIZONTAL, length=width, highlightthickness=0, fg='white', troughcolor='white', width=20)
        self.slider.place(anchor=tk.SW, x=pos[0] + 50, y=pos[1])
        self.slider.set(150)


class ProxyTypes:
    def __init__(self, master, http_pos: tuple, bg_color):
        http_label = tk.Label(master, font=('default', 17), text='HTTP:', bg=bg_color, fg='white')
        http_label.place(x= http_pos[0] - 130, y= http_pos[1], anchor=tk.SW)
