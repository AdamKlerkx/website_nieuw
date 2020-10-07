#Adam •™

```hier onder staat de code, je moet het runnen in een python editor```

import random #Adam •™

woord = ["hallo", "fijn", "apen","jij","ons","uil","kat","vis","adam"]
#Adam •™
geheim_woord = random.choice(woord)#Adam •™

#Adam •™
def galg (aantal_fout):
    if aantal_fout == 0:#Adam •™
        return '''========='''
    if aantal_fout == 1:
        return ''' |/
 |
 |
 |
 |
========='''
    if aantal_fout == 2:#Adam •™
        return '''_______
 |/
 |
 |
 |
 |
========='''
    if aantal_fout == 3:
        return '''_______
 |/   |
 |
 |
 |
 |
========='''
    if aantal_fout == 4:
        return '''_______
 |/   |
 |    @
 |
 |
 |
========='''
    if aantal_fout == 5:
        return '''_______
 |/   |
 |    @
 |   -+-
 |   /\\
 |
========='''

aantal_fout = 0
aantal_goed = 0
geraaden_letter = ""

while True:
#Adam •™

    het_woord = ""
    for letter in geheim_woord:
        if letter in geraaden_letter:
            het_woord += letter
        else:
            het_woord += "_ "

    if het_woord == geheim_woord:
        print("••• goed •••")
        print(" ")#Adam •™
        print("letters goed " + str(aantal_goed))
        print("letters fout " + str(aantal_fout))
        print("gemaakt door Adam")
        break

    print(het_woord)
    letter = input("schijf je letter: ")

    #print(geheim_woord)

    if not letter.isalpha():
        print ("doe alleen maar letters in AUB")
        aantal_fout = aantal_fout + 1
    elif letter in geheim_woord:
        print(letter)#Adam •™
        aantal_goed = aantal_goed + 1
        print(galg(aantal_fout))#Adam •™
        geraaden_letter += letter
    else:#Adam •™#Adam •™
        print(letter)
        aantal_fout = aantal_fout + 1
        print(galg(aantal_fout))

    if aantal_fout == 5:
        print(galg(aantal_fout))
        print("•••fout•••")
        print(" ")
        print("letters goed " + str(aantal_goed))
        print("letters fout " + str(aantal_fout))
        print(str(geheim_woord))
        print("gemaakt door Adam")
        break#Adam •™





