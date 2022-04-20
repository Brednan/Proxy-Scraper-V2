from GUI_Components import *

bg_color = '#343434'

window = MainWindow(size=(600, 700), is_resizeable=False, icon='./images/app_icon.ico', title='Proxy Scraper V2', bg=bg_color)

title = Title(window.window, 'Proxy Scraper V2', 'white', font=('default', 30), pos=(300, 50), bg=bg_color)

output_dir = OutputFolder(window.window, 25, ('default', 17), (150, 150), bg=bg_color)

timeout = Timeout(window.window, bg_color, width=350, pos=(150, 250))
max_threads = MaxThreads(window.window, bg_color, width=350, pos=(150, 320))

http_proxies = ProxyTypes(window.window, http_pos=(150, 400), bg_color= bg_color)

window.window.mainloop()
