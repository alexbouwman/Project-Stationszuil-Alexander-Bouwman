# Het importeren van alle modules die ik nodig heb.
from datetime import datetime
from random import randint


# Hier heb ik een functie gemaakt die een random station kiest uit een lijst met 3 stations in een apart bestand.
def random_station():
    stations_lijst = open('stations.txt', 'r')
    stations = stations_lijst.readlines()
    station = stations[randint(0, 2)]
    stations_lijst.close()
    return station


# Het ophalen van de tijd door middel van een functie zodat elk bericht een unieke tijd heeft.
def tijd_halen():
    vandaag = datetime.today()
    tijd = vandaag.strftime('%d/%m/%Y %H:%M:%S')
    return tijd


# Het geven van een naam en mening over het betreffende station, ook kijken of het bericht geschikt is en het schrijven
# van het bericht met naam, datum en bericht zelf naar het csv-bestand.
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


# Een functie om het csv-bestand leeg te halen, op het moment dat iemand als naam: 'clear' heeft ingevuld.
def clear():
    with open('../berichten.csv', 'w'):
        pass


# Een loop om ervoor te zorgen dat een onbeperkt aantal mensen een mening over het station kan geven.
while True:
    mening()
