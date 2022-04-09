import tkinter as tk


class MainWindow:
    def __init__(self, size: tuple, is_resizeable: bool, icon, title):
        self.window = tk.Tk()
        self.window.geometry(f'{size[0]}x{size[1]}')
        self.window.resizable(width=is_resizeable, height=is_resizeable)
        self.window.iconbitmap(icon)
        self.window.title(title)


