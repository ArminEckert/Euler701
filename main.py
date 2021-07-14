import random
import time


class Zelle:
    def __init__(self, x, y):
        self.wert = random.randint(0, 1)
        self.besucht = False
        self.x = x
        self.y = y


def anzahlBesetzt(akt):
    if akt.besucht is True: return 0
    akt.besucht = True
    if akt.wert == 0: return 0
    if akt.x > 0:
        w1 = anzahlBesetzt(matrix[akt.x - 1][akt.y])
    else:
        w1 = 0
    if akt.y > 0:
        w2 = anzahlBesetzt(matrix[akt.x][akt.y - 1])
    else:
        w2 = 0
    if akt.x < w - 1:
        w3 = anzahlBesetzt(matrix[akt.x + 1][akt.y])
    else:
        w3 = 0
    if akt.y < h - 1:
        w4 = anzahlBesetzt(matrix[akt.x][akt.y + 1])
    else:
        w4 = 0
    return 1 + w1 + w2 + w3 + w4


def testBit(wert, bitNr):
    mask = 1 << bitNr
    return wert & mask


def matrixNeuErstellen(versuch):
    i=0
    for a in matrix:
        for b in a:
            b.wert = testBit(versuch,i)
            i=i+1
            b.besucht = False


anfang = time.time()
ergebnisse = []
w, h = 7, 7
anzahl=2 ** (w * h)
summe=0
matrix = [[Zelle(x, y) for y in range(w)] for x in range(h)]
for versuch in range(anzahl):
    matrixNeuErstellen(versuch)
    maximum = 0
    for spalte in matrix:
        for zelle in spalte:
            bes = anzahlBesetzt(zelle)
            if bes > maximum:
                maximum = bes
    summe+=maximum;

print()
print(summe / anzahl)
print(time.time() - anfang)
