from datetime import datetime
from random import randint


def random_station():
    stations_lijst = open('stations.txt', 'r')
    stations = stations_lijst.readlines()
    station = stations[randint(0, 2)]
    stations_lijst.close()
    return station


def tijd_halen():
    vandaag = datetime.today()
    tijd = vandaag.strftime('%d/%m/%Y %H:%M:%S')
    return tijd


def mening():
    berichten = open('../berichten.csv', 'a')
    naam = input("Voer uw naam in: ").strip().split(' ')[0]
    if len(naam) <= 0:
        naam = "Anoniem"
    bericht = input("Geef uw mening over dit station: ")
    if len(bericht) > 140:
        print("Bericht is te lang, probeer opnieuw.")
    if naam == 'clear':
        clear()
    elif len(bericht) < 140:
        berichten.write(f'{naam};{tijd_halen()};{bericht};{random_station()}')
        print("Bericht opgeslagen, dank voor uw mening!")


def clear():
    with open('../berichten.csv', 'w'):
        pass


while True:
    mening()
