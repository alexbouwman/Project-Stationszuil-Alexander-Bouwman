import tkinter as tk

window = tk.Tk()
window.geometry('500x400')
window.title('NS Meningen')
window.iconbitmap('C:/Users/bouwm/downloads/favicon.ico')
window.configure(bg='#212b5c')

window.grid_columnconfigure(0, weight=200)
window.grid_columnconfigure(1, weight=100)

window.grid_rowconfigure(0, weight=200)
window.grid_rowconfigure(1, weight=100)

berichten = tk.Frame(window, bg='red')
faciliteiten = tk.Frame(window, bg='green')

label = tk.Label(berichten, text='hello')
label.pack()

berichten.grid(column=0, row=0, sticky='news')
faciliteiten.grid(column=1, row=0, sticky='news')

tk.mainloop()
