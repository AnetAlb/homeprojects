'''
Napiš program, který vypíše „tabulku“ s násobilkou:

0 0 0 0 0
0 1 2 3 4
0 2 4 6 8
0 3 6 9 12
0 4 8 12 16
'''
for radek in range(0,5):
    print('') #vytvori novy radek

    for cislo in range(0,5):
        nasobek=cislo*radek
        print(nasobek, end=' ') #vypisuje do radku
