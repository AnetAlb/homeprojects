'''
Pomocí cyklů for a příkazu if napiš program, který z jednotlivých 'X' a mezer vypíše:

X X X X X X
X         X
X         X
X         X
X         X
X X X X X X
'''
def xctverec():
    velikost=int(input("Pocet X: "))
    for radek in range(0,velikost):
        print('') #vytvori novy radek
        if radek > 0 and radek < velikost-1 :
                mezery=(' '*((velikost-2)*2-1))
                print('X',mezery ,'X', end=' ')
        else:
            print('X '*velikost, end=' ')


xctverec()
