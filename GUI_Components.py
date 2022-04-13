import tkinter as tk


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
    def __init__(self, master, width:int, font:tuple, pos:tuple, bg:str):
        self.entry = tk.Entry(master, width=width, font=font)
        self.entry.place(x=pos[0], y=pos[1], anchor=tk.SW)

        self.button = tk.Button(master, font=font, text='...')
        self.button.place(anchor=tk.SW, x=pos[0] + 340, y=pos[1], width=70, height=30)

        self.label = tk.Label(master, font=font, text='Output Dir:', fg='white', bg=bg)
        self.label.place(anchor=tk.SE, x=pos[0] - 10, y=pos[1])
