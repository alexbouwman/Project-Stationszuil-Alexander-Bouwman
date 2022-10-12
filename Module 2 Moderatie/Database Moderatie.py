import psycopg2 as pg

conn = pg.connect(
    host="localhost",
    user="postgres",
    password="0000",
    database="stationszuil"
)


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

with open('../berichten.csv', 'w') as leeghalen:
    pass
