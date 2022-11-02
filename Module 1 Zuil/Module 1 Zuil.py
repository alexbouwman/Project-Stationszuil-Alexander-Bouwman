from datetime import datetime
from random import randint

vandaag = datetime.today()


def random_station():
    stations_lijst = open('stations.txt', 'r')
    stations = stations_lijst.readlines()
    station = stations[randint(0, 2)]
    stations_lijst.close()
    return station


def mening():
    berichten = open('../berichten.csv', 'a')
    naam = input("Voer uw naam in: ").strip().split(' ')[0]
    tijd = vandaag.strftime('%d/%m/%Y %H:%M:%S')
    if len(naam) <= 0:
        naam = "Anoniem"
    bericht = input("Geef uw mening over dit station: ")
    if len(bericht) > 140:
        print("Bericht is te lang, probeer opnieuw.")
    if naam == 'clear':
        clear()
    elif len(bericht) < 140:
        berichten.write(f'{naam};{tijd};{bericht};{random_station()}')
        print("Bericht opgeslagen, dank voor uw mening!")


def clear():
    with open('../berichten.csv', 'w'):
        pass


while True:
    mening()
