from datetime import datetime
import psycopg2 as pg

# Het verbinden met mijn PostgreSQL database.
conn = pg.connect(
    host="localhost",
    user="postgres",
    password="0000",
    database="stationszuil"
)


# Functie die onbeoordeelde meningen ophaalt, deze vervolgens laat zien aan de moderator die de mening kan goedkeuren
# of afkeuren, hierna worden de naam, tijd en email van de moderator toegevoegd en apart neergezet.
def beoordeling():
    beoordeeld = []
    for beo in onbeoordeeld:
        beoordeeld.append(beo.strip().split(';'))
    for x in beoordeeld:
        print(f'{x[0]} {x[1]} {x[3]}: {x[2]}')
        beoordeling2 = input('Is dit bericht toegestaan? Ja/Nee: ').lower()
        if beoordeling2 == 'ja':
            x.append('Goedgekeurd')
        elif beoordeling2 == 'nee':
            x.append('Afgekeurd')
        x.append(moderatornaam)
        x.append(tijd_halen())
        x.append(moderatoremail)
    return beoordeeld


# Het inlezen van de onbeoordeelde meningen
with open('../berichten.csv') as meningen:
    onbeoordeeld = meningen.readlines()

moderatornaam = input('Moderator naam: ')
moderatoremail = input('Moderator E-mail: ')


# Een functie voor het ophalen van de tijd zodat de tijd van moderatie terug te traceren is.
def tijd_halen():
    vandaag = datetime.today()
    moderatortijd = vandaag.strftime('%d/%m/%Y %H:%M:%S')
    return moderatortijd


# Beoordeelde meningen schrijven naar het csv-bestand. Deze meningen zijn klaar om naar de database verstuurd te worden.
meningen_toevoegen = open('../berichten.csv', 'w')
for x in beoordeling():
    meningen_toevoegen.write(f'{x[0]};{x[1]};{x[2]};{x[3]};{x[4]};{x[5]};{x[6]};{x[7]}\n')
meningen_toevoegen.close()

# Het importeren van de meningen uit het csv-bestand en deze splitsen voor de database.
with open('../berichten.csv') as meningen:
    inlezen = meningen.readlines()
    importeren = []
    for mening in inlezen:
        importeren.append(mening.strip().split(';'))

# Hier maak ik alle variabelen aan voor de database en zet ik ze ook daadwerkelijk in de database. Dit doe ik apart voor
# de meningen en de moderatie.
for record in range(len(importeren)):
    naam = importeren[record][0]
    datum = importeren[record][1]
    bericht = importeren[record][2]
    station = importeren[record][3]
    status = importeren[record][4]
    moderator = importeren[record][5]
    tijd_mod = importeren[record][6]
    email_mod = importeren[record][7]
    curs = conn.cursor()
    insert_meningen = f"INSERT INTO meningen(mening, datum, naam, station, status)" \
                      f"VALUES ('{bericht}', '{datum}', '{naam}', '{station}', '{status}')"
    insert_moderator = f"INSERT INTO moderatie(datum, mod_naam, mod_email)" \
                       f"VALUES ('{tijd_mod}', '{moderator}', '{email_mod}')"
    curs.execute(insert_meningen)
    curs.execute(insert_moderator)
    conn.commit()
conn.close()

# Nadat de data in de database is gezet, haal ik het hele csv-bestand leeg.
with open('../berichten.csv', 'w') as leeghalen:
    pass

# Hier sluit ik de connectie met de database.
conn.close()
