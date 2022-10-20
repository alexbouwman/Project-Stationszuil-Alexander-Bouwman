import tkinter as tk
from datetime import datetime
import psycopg2 as pg
from PIL import ImageTk, Image
import requests


conn = pg.connect(
    host="localhost",
    user="postgres",
    password="0000",
    database="stationszuil"
)

# -------------------------------------------------------------------------------------------------------------------- #
window = tk.Tk()
window.geometry('800x450')
window.title('NS Meningen')
window.iconbitmap('C:/Users/bouwm/downloads/favicon.ico')
window.configure(bg='#212b5c')
# -------------------------------------------------------------------------------------------------------------------- #
window.grid_columnconfigure(0, weight=200)
window.grid_columnconfigure(1, weight=100)

window.grid_rowconfigure(0, weight=40)
window.grid_rowconfigure(1, weight=100)
window.grid_rowconfigure(2, weight=100)
# -------------------------------------------------------------------------------------------------------------------- #
berichten = tk.Frame(window, bg='white')
faciliteiten = tk.Frame(window, bg='green')
tijd = tk.Frame(window, bg='gray')
weer = tk.Frame(window, bg='yellow')
# -------------------------------------------------------------------------------------------------------------------- #

curs_bericht = conn.cursor()
bericht_display = f"SELECT bericht FROM meningen"
curs_bericht.execute(bericht_display)

inlezen_berichten = curs_bericht.fetchall()


counter = 0


# -------------------------------------------------------------------------------------------------------------------- #

def bericht_vernieuwen(teller):
    varbericht.set(str(inlezen_berichten[teller][0]))
    teller += 1
    window.after(5000, bericht_vernieuwen, teller)


window.after(0, bericht_vernieuwen, counter)

varbericht = tk.StringVar()

berichten_label = tk.Label(berichten, textvariable=varbericht, bg='white')
berichten_label.pack()

# -------------------------------------------------------------------------------------------------------------------- #

tijd_var = tk.StringVar()


def tijd_vernieuwen():
    time = datetime.today()
    current = datetime.strftime(time, '%H:%M:%S')
    tijd_var.set(current)
    tijd.after(1000, tijd_vernieuwen)


tijd.after(0, tijd_vernieuwen)

tijd_label = tk.Label(tijd, textvariable=tijd_var, fg='white', bg='gray', font=('', 35))
tijd_label.place(relx=0.5, rely=0.5, anchor='center')

# -------------------------------------------------------------------------------------------------------------------- #

img_lift = ImageTk.PhotoImage(
    Image.open("D:/GitHub/Project-Stationszuil/Module 3 Stationshalscherm/faciliteiten/img_lift.png").resize(
        (110, 110)))
img_lift_label = tk.Label(faciliteiten, image=img_lift)
img_lift_label.place(relx=0.25, rely=0.18, anchor='center')

img_ovfiets = ImageTk.PhotoImage(
    Image.open("D:/GitHub/Project-Stationszuil/Module 3 Stationshalscherm/faciliteiten/img_ovfiets.png").resize(
        (110, 110)))
img_ovfiets_label = tk.Label(faciliteiten, image=img_ovfiets)
img_ovfiets_label.place(relx=0.748, rely=0.18, anchor='center')

img_pr = ImageTk.PhotoImage(
    Image.open("D:/GitHub/Project-Stationszuil/Module 3 Stationshalscherm/faciliteiten/img_pr.png").resize((110, 110)))
img_pr_label = tk.Label(faciliteiten, image=img_pr)
img_pr_label.place(relx=0.25, rely=0.53, anchor='center')

img_toilet = ImageTk.PhotoImage(
    Image.open("D:/GitHub/Project-Stationszuil/Module 3 Stationshalscherm/faciliteiten/img_toilet.png").resize(
        (110, 110)))
img_toilet_label = tk.Label(faciliteiten, image=img_toilet)
img_toilet_label.place(relx=0.748, rely=0.53, anchor='center')

# -------------------------------------------------------------------------------------------------------------------- #

resource_uri = 'https://api.openweathermap.org/data/2.5/weather?q=Hilversum,' \
               'NL&appid=899abec4310dcd6f4bb871df89a7dfb1&units=metric '
weer_data = requests.get(resource_uri).json()

# -------------------------------------------------------------------------------------------------------------------- #

berichten.grid(column=0, row=0, rowspan=2, sticky='news', padx=(10, 5), pady=(10, 5))
weer.grid(column=0, row=2, sticky='news', padx=(10, 5), pady=(5, 10))
faciliteiten.grid(column=1, row=1, rowspan=2, sticky='news', padx=(5, 10), pady=(5, 10))
tijd.grid(column=1, row=0, sticky='news', padx=(5, 10), pady=(10, 5))

conn.close()
tk.mainloop()
