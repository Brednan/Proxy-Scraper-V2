from GUI_Components import *
import time


bg_color = '#343434'

window = MainWindow(size=(600, 540), is_resizeable=False, icon='./images/app_icon.ico', title='Proxy Scraper V2', bg=bg_color)

title = Title(window.window, 'Proxy Scraper V2', 'white', font=('default', 30), pos=(300, 50), bg=bg_color)

output_dir = OutputFolder(window.window, 25, ('default', 17), (150, 150), bg=bg_color)

timeout = Timeout(window.window, bg_color, width=350, pos=(150, 250))
max_threads = MaxThreads(window.window, bg_color, width=350, pos=(150, 320))

proxy_types = ProxyTypes(window.window, http_pos=(250, 400), bg_color=bg_color, socks4_pos=(450, 400))

status = Status(window.window, bg_color, pos=(10, 530))

start = StartButton(window.window, (150, 475), status, output_dir, proxy_types, timeout, max_threads)
stop = StopButton(window.window, pos=(450, 475), status=status)

window.window.mainloop()

