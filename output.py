import json
import datetime
from dateutil import relativedelta
from dateutil import parser

with open ("test.json") as json_data:
    data = json.load(json_data)

def demeFactor(years):
    if years >= 0.25 and years < 0.5:
        return 7
    if years >= 0.5 and years < 1:
        return 14
    if years >= 1 and years < 1.5:
        return 19.5
    if years >= 1.5 and years < 2:
        return 2* 19.5
    if years >= 2 and years <2.5:
        return 2 *20
    if years >= 2.5 and years <3:
        return 3*20
    if years >= 3 and years <3.5:
        return 3*20.5
    if years >= 3.5 and years <4:
        return 4 *20.5
    if years >= 4 and years < 4.5:
        return 4 *21
    if years >= 4.5 and years < 5:
        return 5* 21
    if years>= 5 and years < 5.5:
        return 5* 21.24
    if years >= 5.5 and years < 6:
        return 6*21.24
    if years >= 6 and years < 6.5:
        return 6*21.5
    if years >= 6.5 and years < 7:
        return 7* 21.5
    if years >= 7 and years < 7.5:
        return 7*22
    if years >= 7.5 and years <8:
        return 8*22
    if years >= 8:
        return 22 *8

def calculotiempo(tiempoInicio):
    hoy = datetime.date.today()
    tiempo= parser.parse (tiempoInicio,dayfirst = True)
    delta = relativedelta.relativedelta(hoy,tiempo)
    years = delta.years + (delta.months/12) + (delta.days/365)
    return years


salarios = list(data["salarios"])
tiempodeallan = data["tiempoInicio"]
tiempodetrabajoallan = calculotiempo(tiempodeallan)
otraforma = demeFactor(tiempodetrabajoallan)

cesantia = (sum(salarios)/180) * otraforma
print cesantia
