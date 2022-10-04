from datetime import datetime

def beoordeling():
    for x in onbeoordeeld:
        beoordeeld.append(x.strip().split(';'))
    for x in beoordeeld:
        print(f'{x[0]}: {x[2]}')
        beoordeling = input('Is dit bericht toegestaan? Ja/Nee: ').lower()
        if beoordeling == 'ja':
            x.append('Goedgekeurd')
            print(beoordeeld)
        elif beoordeling == 'nee':
            x.append('Afgekeurd')
    return beoordeeld


with open('../berichten.csv') as meningen:
    onbeoordeeld = meningen.readlines()
    beoordeeld = []
    onbeoordeeld.remove('Naam;Datum/Tijd;Bericht;Station\n')


vandaag = datetime.today()
moderatornaam = input('Moderator naam: ')
moderatortijd = vandaag.strftime('%d/%m/%Y %H:%M:%S')
moderatoremail = input('Moderator E-mail: ')


x.append(moderatornaam)
x.append(moderatortijd)
x.append(moderatoremail)
