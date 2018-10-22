'''
Napiš program, který postupně z jednotlivých 'X' vypíše:
X
X X
X X X
X X X X

for radek in range(0,5):
    print('') #vytvori novy radek

    for cislo in range(0,5):
        nasobek=cislo*radek
        print('X'*nasobek, end=' ') #vypisuje do radku
'''
for cislo in range(0,5):
    print('X'*cislo)
