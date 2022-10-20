from datetime import datetime
import psycopg2 as pg

conn = pg.connect(
    host="localhost",
    user="postgres",
    password="0000",
    database="stationszuil"
)


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
        x.append(moderatortijd)
        x.append(moderatoremail)
    return beoordeeld


with open('../berichten.csv') as meningen:
    onbeoordeeld = meningen.readlines()

vandaag = datetime.today()
moderatornaam = input('Moderator naam: ')
moderatortijd = vandaag.strftime('%d/%m/%Y %H:%M:%S')
moderatoremail = input('Moderator E-mail: ')

meningen_toevoegen = open('../berichten.csv', 'w')
for x in beoordeling():
    meningen_toevoegen.write(f'{x[0]};{x[1]};{x[2]};{x[3]};{x[4]};{x[5]};{x[6]};{x[7]}\n')
meningen_toevoegen.close()

with open('../berichten.csv') as meningen:
    inlezen = meningen.readlines()
    importeren = []
    for mening in inlezen:
        importeren.append(mening.strip().split(';'))

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
    insert_naam = f"INSERT INTO meningen(naam_gebruiker, datum, bericht, station, " \
                  f"status, moderator, tijdmod, emailmod)" \
                  f" VALUES ('{naam}', '{datum}', '{bericht}', '{station}', '{status}', " \
                  f"'{moderator}', '{tijd_mod}', '{email_mod}')"
    curs.execute(insert_naam)
    conn.commit()
conn.close()

with open('../berichten.csv', 'w') as leeghalen:
    pass

conn.close()
