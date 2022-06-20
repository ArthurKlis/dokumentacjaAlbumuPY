# dokumentacjaAlbumu.py
# wersja 1
#2022-06-20

import uuid
import os

nazwaAlbum=input('Podaj nazwę albumu: ')
iloscZdjecDotychczas=int(input('Podaj ilość zdjęć dotychczas zindeksowanych: '))
nowaKarta=''
kartaNumer=0
while nowaKarta != 'n':
      print('obecny numer karty: ' + str(kartaNumer))
      kartaNumer=input('Podaj numer karty, z którą będziesz pracował: ')
      nowaStrona=''
      stronaNumer=0
      while nowaStrona != 'n':
            print('obecny numer strony: ' + str(stronaNumer))
            stronaNumer=input('Podaj numer strony, z którą będziesz pracował: ')
            wierszeCzyKolumny=input('Podaj sposób adresacji na stronie (wiersze/kolumny): ')
            noweZdjecie=''
            while noweZdjecie != 'n':
                  zdjecieNumer=iloscZdjecDotychczas+1
                  adresZdjecie=input('Podaj adres zdjęcia, obie cyfry adresu jedna po drugiej: ')
                  szerokosc=input('Podaj szerokosc w mm: ')
                  wysokosc=input('Podaj wysokosc w mm: ')
                  iloscOsob=input('Podaj ilość osób na zdjęciu: ')
                  orientacja=input('Podaj orientację zdjęcia w albumie (pionowa/pozioma): ')
                  opisNaStronie=input('Podaj opis zdjęcia ze strony karty albumu lub wpisz brak, jeśli nie ma: ')
                  opisZtylu=input('Podaj opis zdjęcia z tyłu zdjęcia lub słowo brak, jeśli nie ma: ')
                  opisZawartosc=input('Podaj opis zawartosci zdjęcia (taki, jaki osoba, która nic nie wie o zdjęciu i widzi je po raz pierwszy): ')
                  opisNaZdjeciu=input('Podaj opis znajdujący się na zdjęciu: ')
                  identyfikator=str(nazwaAlbum)+'.k'+str(kartaNumer)+'.str'+str(stronaNumer)+'.'+str(zdjecieNumer)+'.'+str(adresZdjecie[:1])+str(wierszeCzyKolumny[:1])+'.'+str(adresZdjecie[1:2])+'z'
                  uuidValue = uuid.uuid5(uuid.NAMESPACE_X500, identyfikator)
                  file=open('album_'+str(nazwaAlbum)+'.txt', 'a')
                  file.write(str(uuidValue)+' '+str(identyfikator)+'\n')
                  file.write('szerokość: '+str(szerokosc)+'mm'+' '+'wysokość: '+str(wysokosc)+'mm'+' '+'ilość osób: '+str(iloscOsob)+' '+'orientacja: '+str(orientacja)+' '+'opis na stronie karty przy zdjęciu: '+str(opisNaStronie)+' '+'opis z tyłu zdjęcia: '+str(opisZtylu)+' '+'Opis zawartości: '+str(opisZawartosc)+' '+'opis na zdjęciu: '+str(opisNaZdjeciu)+'\n\n\n')
                  file.close()
                  iloscZdjecDotychczas += 1
                  noweZdjecie=input('Czy nowe zdjęcie? (t/n): ')
            nowaStrona=input('Czy nowa strona karty? (t/n): ')
      nowaKarta=input('Czy kolejna karta albumu? (t/n): ')
