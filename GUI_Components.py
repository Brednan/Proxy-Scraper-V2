import sys
import tkinter as tk
from tkinter.filedialog import askopenfilename
from test import loop_func
import threading
from scraper import Scraper

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
    def __init__(self, master, http_pos: tuple, bg_color, socks4_pos: tuple):
        self.http_checked = tk.IntVar(value=1)
        self.http_checkbox = tk.Checkbutton(master, text='HTTPS', font=('default', 17), bg=bg_color, fg='white', bd=0, selectcolor='darkgrey', variable=self.http_checked)
        self.http_checkbox.place(anchor=tk.SW, x=http_pos[0] - 125, y=http_pos[1])

        self.socks4_checked = tk.IntVar()
        self.socks4_checkbox = tk.Checkbutton(master, font=('default', 17), text='SOCKS4', bg=bg_color, fg='white', bd=0, selectcolor='darkgrey', variable=self.socks4_checked)
        self.socks4_checkbox.place(x=socks4_pos[0] - 100, y=socks4_pos[1], anchor=tk.SW)


class Status:
    def __init__(self, master, bg_color, pos):
        self.master = master
        self.status_var = tk.StringVar(master, 'Status: None')

        self.status_display = tk.Label(master, textvariable=self.status_var, font=('default', 15), fg='white', bg=bg_color)
        self.status_display.place(anchor=tk.SW, x=pos[0], y=pos[1])

    def status_none(self):
        self.status_var.set('Status: None')

    def status_scraping(self):
        self.status_var.set('Status: Scraping')


class StartButton:
    def __init__(self, master, pos: tuple, status, output, types, timeout, threads):
        self.status = status
        self.output = output
        self.types = types
        self.timeout = timeout
        self.threads = threads

        self.button = tk.Button(master, text='START', fg='white', bg='#00BD03', font=('Arial TUR', 20), relief=tk.FLAT, width=8, command=lambda: self.submit())
        self.button.place(anchor=tk.SW, x=pos[0], y=pos[1])

    def submit(self):
        error_message = ErrorMessage('./images/error_logo.ico')

        if len(self.output.entry.get().strip()) < 1:
            threading.Thread(target=error_message.custom_error, args=((400, 70), ('default', 17), 'Please select an output file!')).start()

        else:
            self.status.status_var.set('Status: Scraping')
            threading.Thread(target=self.bot_sequence).start()

    def bot_sequence(self):
        error_message = ErrorMessage('./images/error_logo.ico')

        try:
            scraper = Scraper(self.types)
            scraper.scrape_proxies()
        except:
            threading.Thread(target=error_message.error_scraping, args=((250, 50), ('default', 15))).start()
        
        self.status.status_var.set('Status: None')


class StopButton:
    def __init__(self, master, pos: tuple, status):
        self.status = status
        self.button = tk.Button(master, text='STOP', fg='white', bg='#D50000', font=('Arial TUR', 20), relief=tk.FLAT, width=8, command=lambda: self.stop_process())
        self.button.place(anchor=tk.SE, x=pos[0], y=pos[1])

    def stop_process(self):
        self.status.status_var.set('Status: None')

class ErrorMessage:
    def __init__(self, icon):
        self.icon = icon

    def error_scraping(self, size:tuple, font):
        window = tk.Tk()
        window.geometry(f'{size[0]}x{size[1]}')
        window.resizable(width=False, height=False)
        window.iconbitmap(self.icon)
        window.title('Error')

        message = tk.Label(window, fg='red', font=font, text='Error Scraping!')
        message.place(x=int(size[0]/2), y=int(size[1]/2), anchor=tk.CENTER)

        window.mainloop()
    
    def custom_error(self, size:tuple, font, text):
        window = tk.Tk()
        window.geometry(f'{size[0]}x{size[1]}')
        window.resizable(width=False, height=False)
        window.iconbitmap(self.icon)
        window.title('Error')

        message = tk.Label(window, fg='red', font=font, text=text)
        message.place(x=int(size[0]/2), y=int(size[1]/2), anchor=tk.CENTER)
        window.mainloop()
