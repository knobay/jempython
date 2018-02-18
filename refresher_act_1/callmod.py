def convftoc(far):
    "Converting farenheit to centegrade"
    cent = (far-32) * (5/9)
    return cent

def convctof(cent):
    "Convert centegrade to faraenheit"
    far = (cent*(9/5)) + 32
    return far

def calcgross(hrs, rate):
    gross = hrs * rate
    return gross

def calctax(gross):
    tax = gross / 3
    net = gross - tax
    return net, tax

