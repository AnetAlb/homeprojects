'''Pomocí cyklů for a parametru end pro print napiš program, který postupně z jednotlivých 'X' vypíše:

X X X X X
X X X X X
X X X X X
X X X X X
X X X X X
„Z jednotlivých 'X'“ znamená, že nepoužiješ např. print('X X X X X').

Jak pojmenuješ proměnnou cyklu? A tu druhou?'''

'''

for i in range(0,5):
    print("X X X X X \n")

for i in range(0,5):
    print("X X X X X", end=' ')
'''


for radek in range(0,5):
    print('') #vytvori novy radek
    for pismeno in range(0,5):
        print('x', end=' ') #vypisuje do radku
