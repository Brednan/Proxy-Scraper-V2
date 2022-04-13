from GUI_Components import *

background_color = '#343434'

window = MainWindow(size=(600, 700), is_resizeable=False, icon='./images/app_icon.ico', title='Proxy Scraper V2', bg=background_color)

title = Title(window.window, 'Proxy Scraper V2', 'white', font=('default', 30), pos=(300, 50), bg=background_color)

output_dir = OutputFolder(window.window, 25, ('default', 17), (150, 150), bg=background_color)

window.window.mainloop()
