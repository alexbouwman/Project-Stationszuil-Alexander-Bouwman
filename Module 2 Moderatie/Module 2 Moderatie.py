from datetime import datetime


def beoordeling():
    beoordeeld = []
    for x in onbeoordeeld:
        beoordeeld.append(x.strip().split(';'))
    for x in beoordeeld:
        print(f'{x[0]} {x[1]} {x[3]}: {x[2]}')
        beoordeling = input('Is dit bericht toegestaan? Ja/Nee: ').lower()
        if beoordeling == 'ja':
            x.append('Goedgekeurd')
            print(beoordeeld)
        elif beoordeling == 'nee':
            x.append('Afgekeurd')
        x.append(moderatornaam)
        x.append(moderatortijd)
        x.append(moderatoremail)
    return beoordeeld


with open('../berichten.csv') as meningen:
    onbeoordeeld = meningen.readlines()
    onbeoordeeld.remove('Naam;Datum/Tijd;Bericht;Station\n')

vandaag = datetime.today()
moderatornaam = input('Moderator naam: ')
moderatortijd = vandaag.strftime('%d/%m/%Y %H:%M:%S')
moderatoremail = input('Moderator E-mail: ')

meningen_toevoegen = open('../berichten.csv', 'w')
meningen_toevoegen.write('Naam;Datum/Tijd;Bericht;Station;Status;Moderator;Datum/Tijd-MOD;Email-MOD\n')
for x in beoordeling():
    meningen_toevoegen.write(f'{x[0]};{x[1]};{x[2]};{x[3]};{x[4]};{x[5]};{x[6]};{x[7]}\n')
