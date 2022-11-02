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
window.resizable(width=False, height=False)
window.title('NS Meningen')
window.iconbitmap('C:/Users/bouwm/downloads/favicon.ico')
window.configure(bg='#212b5c')

# -------------------------------------------------------------------------------------------------------------------- #

window.grid_columnconfigure(0, weight=67)
window.grid_columnconfigure(1, weight=33)

window.grid_rowconfigure(0, weight=16)
window.grid_rowconfigure(1, weight=42)
window.grid_rowconfigure(2, weight=42)

window.grid_propagate(False)

# -------------------------------------------------------------------------------------------------------------------- #

berichten = tk.Frame(window, bg='white')

berichten.grid_columnconfigure(0, weight=20)
berichten.grid_columnconfigure(1, weight=1)
berichten.grid_columnconfigure(2, weight=1)
berichten.grid_rowconfigure(1, weight=1)
berichten.grid_rowconfigure(2, weight=100)
berichten.grid_propagate(False)

faciliteiten = tk.Frame(window, bg='white')
faciliteiten.grid_columnconfigure(0, weight=1)
faciliteiten.grid_columnconfigure(1, weight=1)
faciliteiten.grid_rowconfigure(0, weight=1)
faciliteiten.grid_rowconfigure(1, weight=1)
faciliteiten.grid_rowconfigure(2, weight=1)
faciliteiten.grid_rowconfigure(3, weight=1)
faciliteiten.grid_propagate(False)

tijd = tk.Frame(window, bg='white')

# -------------------------------------------------------------------------------------------------------------------- #

curs_bericht = conn.cursor()
bericht_display = f"SELECT bericht FROM meningen WHERE status LIKE 'Goedgekeurd' ORDER BY datum DESC"
curs_bericht.execute(bericht_display)
inlezen_berichten = curs_bericht.fetchall()

curs_naam = conn.cursor()
naam_display = f"SELECT naam_gebruiker FROM meningen WHERE status LIKE 'Goedgekeurd' ORDER BY datum DESC"
curs_naam.execute(naam_display)
inlezen_naam = curs_naam.fetchall()

curs_infobericht = conn.cursor()
infobericht_display = f"SELECT datum, station FROM meningen ORDER BY datum DESC"
curs_infobericht.execute(infobericht_display)
inlezen_infobericht = curs_infobericht.fetchall()

counter = 0
counter2 = 0
counter3 = 0
counter4 = 0

# -------------------------------------------------------------------------------------------------------------------- #

img_lift = ImageTk.PhotoImage(
    Image.open("D:/GitHub/Project-Stationszuil/Module 3 Stationshalscherm"
               "/faciliteiten/img_lift.png").resize(
        (110, 110)))
img_ovfiets = ImageTk.PhotoImage(
    Image.open("D:/GitHub/Project-Stationszuil/Module 3 Stationshalscherm"
               "/faciliteiten/img_ovfiets.png").resize(
        (110, 110)))
img_pr = ImageTk.PhotoImage(
    Image.open("D:/GitHub/Project-Stationszuil/Module 3 Stationshalscherm"
               "/faciliteiten/img_pr.png").resize(
        (110, 110)))
img_toilet = ImageTk.PhotoImage(
    Image.open("D:/GitHub/Project-Stationszuil/Module 3 Stationshalscherm"
               "/faciliteiten/img_toilet.png").resize(
        (110, 110)))


def get_facilities():
    services_sql = f"select ov_bike, elevator, toilet, park_and_ride from station_service " \
                   f"where station_city like '{varstation.get()}'"
    service_cursor = conn.cursor()
    service_cursor.execute(services_sql)
    services = service_cursor.fetchone()
    facilities(services)


img_lift_label = tk.Label(faciliteiten, image=img_lift)
img_ovfiets_label = tk.Label(faciliteiten, image=img_ovfiets)
img_pr_label = tk.Label(faciliteiten, image=img_pr)
img_toilet_label = tk.Label(faciliteiten, image=img_toilet)


def facilities(services):
    ov_bike, elevator, toilet, park_and_ride = services
    if ov_bike:
        img_ovfiets_label.grid(column=0, row=0, sticky='w', padx=10, pady=10)
    else:
        img_ovfiets_label.grid_forget()
    if elevator:
        img_lift_label.grid(column=1, row=0, sticky='e', padx=10, pady=10)
    else:
        img_lift_label.grid_forget()
    if toilet:
        img_toilet_label.grid(column=0, row=1, sticky='w', padx=10, pady=5)
    else:
        img_toilet_label.grid_forget()
    if park_and_ride:
        img_pr_label.grid(column=1, row=1, sticky='e', padx=10, pady=5)
    else:
        img_pr_label.grid_forget()


# -------------------------------------------------------------------------------------------------------------------- #

def bericht_vernieuwen(teller):
    try:
        varbericht.set(str(inlezen_berichten[teller][0]))
    except IndexError:
        pass
    if teller < 4:
        teller += 1
    else:
        teller = 0
    window.after(5000, bericht_vernieuwen, teller)


window.after(0, bericht_vernieuwen, counter)

varbericht = tk.StringVar()

berichten_label = tk.Label(berichten, textvariable=varbericht, fg='#212b5c', bg='white', font=('', 18), wraplength=510,
                           justify='left')
berichten_label.grid(column=0, columnspan=3, row=2, sticky='nw', padx=3)


def naam_vernieuwen(teller2):
    try:
        varnaam.set(str(inlezen_naam[teller2][0]))
    except IndexError:
        pass
    if teller2 < 4:
        teller2 += 1
    else:
        teller2 = 0
    window.after(5000, naam_vernieuwen, teller2)


window.after(0, naam_vernieuwen, counter2)

varnaam = tk.StringVar()

naam_label = tk.Label(berichten, textvariable=varnaam, fg='#212b5c', bg='white', font=('', 25, 'bold'), wraplength=520,
                      justify='left')
naam_label.grid(column=0, row=0, sticky='nw')


def station_vernieuwen(teller4):
    try:
        varstation.set(str(inlezen_infobericht[teller4][1]))
    except IndexError:
        pass
    if teller4 < 4:
        teller4 += 1
    else:
        teller4 = 0
    window.after(5000, station_vernieuwen, teller4)
    get_facilities()


window.after(0, station_vernieuwen, counter4)

varstation = tk.StringVar()

text_label = tk.Label(faciliteiten, text='Gegeven op station:', fg='#212b5c', bg='white', font=('', 12, 'bold'))
text_label.place(relx=0.5, rely=0.75, anchor='center')

infostation_label = tk.Label(faciliteiten, textvariable=varstation, fg='#212b5c', bg='white', font=('', 30, 'bold'))
infostation_label.grid(column=0, columnspan=2, row=3, sticky='news', pady=30)


def infobericht_vernieuwen(teller3):
    try:
        vardatumbericht.set(
            datetime.strftime((datetime.strptime(str(inlezen_infobericht[teller3][0]), '%d/%m/%Y %H:%M:%S')),
                              '%d/%m/%Y'))
    except IndexError:
        pass
    if teller3 < 4:
        teller3 += 1
    else:
        teller3 = 0
    window.after(5000, infobericht_vernieuwen, teller3)


window.after(0, infobericht_vernieuwen, counter3)

vardatumbericht = tk.StringVar()

infobericht_label = tk.Label(berichten, textvariable=vardatumbericht, fg='#212b5c', bg='white', font=('', 15), wraplength=520,
                             justify='left')
infobericht_label.grid(column=2, row=0, sticky='e', padx=10)

# -------------------------------------------------------------------------------------------------------------------- #

tijd_var = tk.StringVar()


def tijd_vernieuwen():
    time = datetime.today()
    current = datetime.strftime(time, '%H:%M:%S')
    tijd_var.set(current)
    tijd.after(1000, tijd_vernieuwen)


tijd.after(0, tijd_vernieuwen)

tijd_label = tk.Label(tijd, textvariable=tijd_var, fg='#212b5c', bg='white', font=('', 35, 'bold'))
tijd_label.place(relx=0.5, rely=0.5, anchor='center')

# -------------------------------------------------------------------------------------------------------------------- #

resource_uri = 'https://api.openweathermap.org/data/2.5/weather?q=Hilversum,' \
               'NL&appid=899abec4310dcd6f4bb871df89a7dfb1&units=metric '
weer_data = requests.get(resource_uri).json()

# -------------------------------------------------------------------------------------------------------------------- #

topwindow = tk.Toplevel()
topwindow.geometry("270x400")
topwindow.title("Kies een station:")
topwindow.iconbitmap('C:/Users/bouwm/downloads/favicon.ico')
topwindow.configure(bg='#212b5c')

plaatsnaam = tk.StringVar()


def plaatsnaam1():
    plaatsnaam.set('Amsterdam')
    # print(plaatsnaam.get())
    topwindow.destroy()


def plaatsnaam2():
    plaatsnaam.set('Hilversum')
    # print(plaatsnaam.get())
    topwindow.destroy()


def plaatsnaam3():
    plaatsnaam.set('Utrecht')
    # print(plaatsnaam.get())
    topwindow.destroy()


knop_amsterdam = tk.Button(topwindow, text='Amsterdam', bg='#212b5c', fg='#ffc917', activebackground="#212b5c",
                           activeforeground='#ffc917',
                           font=('Calibri', 30, 'bold'), height=2, width=20, command=plaatsnaam1)
knop_hilversum = tk.Button(topwindow, text='Hilversum', bg='#212b5c', fg='#ffc917', activebackground="#212b5c",
                           activeforeground='#ffc917',
                           font=('Calibri', 30, 'bold'), height=2, width=20, command=plaatsnaam2)
knop_utrecht = tk.Button(topwindow, text='Utrecht', bg='#212b5c', fg='#ffc917', activebackground="#212b5c",
                         activeforeground='#ffc917',
                         font=('Calibri', 30, 'bold'), height=2, width=20, command=plaatsnaam3)

knop_amsterdam.pack(pady=0, padx=0)
knop_hilversum.pack(pady=0, padx=0)
knop_utrecht.pack(pady=0, padx=0)

# -------------------------------------------------------------------------------------------------------------------- #

weer = tk.Frame(window, bg='white',)
weer.grid_columnconfigure(0, weight=1)
weer.grid_columnconfigure(1, weight=1)
weer.grid_rowconfigure(0, weight=1)
weer.grid_rowconfigure(1, weight=1)
weer.grid_propagate(False)

weer_plaatsnaam = tk.Label(weer, textvariable=plaatsnaam, fg='#212b5c', bg='white', font=('', 20, 'bold'))
weer_plaatsnaam.grid(column=0, row=0, sticky='nw', padx=3)

# -------------------------------------------------------------------------------------------------------------------- #

berichten.grid(column=0, row=0, rowspan=2, sticky='news', padx=(10, 5), pady=(10, 5))
weer.grid(column=0, row=2, sticky='news', padx=(10, 5), pady=(5, 10))
faciliteiten.grid(column=1, row=1, rowspan=2, sticky='news', padx=(5, 10), pady=(5, 10))
tijd.grid(column=1, row=0, sticky='news', padx=(5, 10), pady=(10, 5))

# -------------------------------------------------------------------------------------------------------------------- #

tk.mainloop()
