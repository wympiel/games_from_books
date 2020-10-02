# Reversegam: klon gry Othello/Reversi
import random
import sys
SZEROKOŚĆ = 8  # Plansza ma 8 spacji szerokości
WYSOKOŚĆ = 8 # Plansza ma 8 spacji wysokości
def narysujPlanszę(plansza):
    # Wyświetl planszę przesłaną do tej funkcji. Zwróć None.
    print('  12345678')
    print(' +--------+')
    for y in range(WYSOKOŚĆ):
        print('%s|' % (y+1), end='')
        for x in range(SZEROKOŚĆ):
            print(plansza[x][y], end='')
        print('|%s' % (y+1))
    print(' +--------+')
    print('  12345678')

def utwórzNowąPlanszę():
    # Tworzy zupełnie nową, pustą strukturę danych z planszą.
    plansza = []
    for i in range(SZEROKOŚĆ):
        plansza.append([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
    return plansza

def czyRuchJestDozwolony(plansza, pionek, xstart, ystart):
    # Zwraca False, jeśli ruch gracza w polu xstart, ystart jest niedozwolony.
    # Jeśli ruch jest możliwy, zwraca listę z polami, które gracz zdobyłby w wyniku tego ruchu.
    if plansza[xstart][ystart] != ' ' or not czyJestNaPlanszy(xstart, ystart):
        return False

    if pionek == 'X':
        pionekPrzeciwnika = 'O'
    else:
        pionekPrzeciwnika = 'X'

    pionkiDoOdwrócenia = []
    for kierunekX, kierunekY in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        x, y = xstart, ystart
        x += kierunekX # Pierwszy krok w kierunku x
        y += kierunekY # Pierwszy krok w kierunku y
        while czyJestNaPlanszy(x, y) and plansza[x][y] == pionekPrzeciwnika:
            # Kontynuuj ruch w tym kierunku xy.
            x += kierunekX
            y += kierunekY
            if czyJestNaPlanszy(x, y) and plansza[x][y] == pionek:
                # Są pionki, które można odwrócić. Idź w przeciwnym kierunku aż do początkowego pola, zapisując wszystkie pionki znajdujące się po drodze.
                while True:
                    x -= kierunekX
                    y -= kierunekY
                    if x == xstart and y == ystart:
                        break
                    pionkiDoOdwrócenia.append([x, y])

    if len(pionkiDoOdwrócenia) == 0: # Jeśli nie powoduje odwrócenia żadnych pionków, to nie jest prawidłowy ruch.
        return False
    return pionkiDoOdwrócenia

def czyJestNaPlanszy(x, y):
    # Zwraca True, jeśli współrzędne znajdują się na planszy.
    return x >= 0 and x <= SZEROKOŚĆ - 1 and y >= 0 and y <= WYSOKOŚĆ - 1

def utwórzPlanszęZPodpowiedziami(plansza, pionek):
    # Zwraca nową planszę z kropkami, które oznaczają pola, na które gracz może wykonać ruch.
    kopiaPlanszy = wykonajKopięPlanszy(plansza)

    for x, y in znajdźDozwoloneRuchy(kopiaPlanszy, pionek):
        kopiaPlanszy[x][y] = '.'
    return kopiaPlanszy

def znajdźDozwoloneRuchy(plansza, pionek):
    # Zwraca listę z listami [x,y], reprezentującymi prawidłowe ruchy dla danego gracza na danej planszy.
    dozwoloneRuchy = []
    for x in range(SZEROKOŚĆ):
        for y in range(WYSOKOŚĆ):
            if czyRuchJestDozwolony(plansza, pionek, x, y) != False:
                dozwoloneRuchy.append([x, y])
    return dozwoloneRuchy

def obliczWynikNaPlanszy(plansza):
    # Oblicza wynik zliczając pionki. Zwraca słownik z kluczami 'X' i 'O'.
    wynikX = 0
    wynikO = 0
    for x in range(SZEROKOŚĆ):
        for y in range(WYSOKOŚĆ):
            if plansza[x][y] == 'X':
                wynikX += 1
            if plansza[x][y] == 'O':
                wynikO += 1
    return {'X':wynikX, 'O':wynikO}

def graczWybieraKolor():
    # Pozwala graczowi wybrać kolor pionków.
    # Zwraca listę, na której pierwszym elementem jest pionek gracza, a drugim pionek komputera.
    pionek = ''
    while not (pionek == 'X' or pionek == 'O'):
        print('Chcesz używać X czy O?')
        pionek = input().upper()

    # Pierwszy element na liście to pionek gracza, a drugi to pionek komputera.
    if pionek == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def ktoZaczyna():
    # Losowanie rozpoczynającego grę.
    if random.randint(0, 1) == 0:
        return 'komputer'
    else:
        return 'gracz'

def wykonajRuch(plansza, pionek, xstart, ystart):
    # Postaw na planszy pionek w polu xstart, ystart i odwróć piony przeciwnika.
    # Zwraca False, jeśli ten ruch jest niedozwolony, a True, jeśli jest dozwolony.
    pionkiDoOdwrócenia = czyRuchJestDozwolony(plansza, pionek, xstart, ystart)

    if pionkiDoOdwrócenia == False:
        return False

    plansza[xstart][ystart] = pionek
    for x, y in pionkiDoOdwrócenia:
        plansza[x][y] = pionek
    return True

def wykonajKopięPlanszy(plansza):
    # Utwórz i zwróć kopię listy plansza.
    kopiaPlanszy = utwórzNowąPlanszę()

    for x in range(SZEROKOŚĆ):
        for y in range(WYSOKOŚĆ):
            kopiaPlanszy[x][y] = plansza[x][y]

    return kopiaPlanszy

def wolnePoleNarożne(x, y):
    # Zwraca True, jeśli pozycja znajduje się w jednym z czterech pól narożnych.
    return (x == 0 or x == SZEROKOŚĆ - 1) and (y == 0 or y == WYSOKOŚĆ - 1)

def wczytajRuchGracza(plansza, pionekGracza):
    # Pozwól graczowi podać ruch.
    # Zwraca ruch jako [x, y] (albo zwraca łańcuchy 'pomoc' lub 'koniec').
    CYFRY1DO8 = '1 2 3 4 5 6 7 8'.split()
    while True:
        print('Podaj swój ruch, wpisz "koniec" aby zakończyć grę, lub "pomoc" aby włączyć podpowiedzi.')
        ruch = input().lower()
        if ruch == 'koniec' or ruch == 'pomoc':
            return ruch

        if len(ruch) == 2 and ruch[0] in CYFRY1DO8 and ruch[1] in CYFRY1DO8:
            x = int(ruch[0]) - 1
            y = int(ruch[1]) - 1
            if czyRuchJestDozwolony(plansza, pionekGracza, x, y) == False:
                continue
            else:
                break
        else:
            print('Ten ruch jest niedozwolony. Podaj kolumnę (1-8), a następnie wiersz (1-8).')
            print('Na przykład 81 oznacza pole w prawym górnym rogu.')

    return [x, y]

def ustalRuchKomputera(plansza, pionekKomputera):
    # Znając planszę i pionek komputera, ustal gdzie
    # wykonać ruch i zwróć ten ruch jako listę [x, y].
    możliweRuchy = znajdźDozwoloneRuchy(plansza, pionekKomputera)
    random.shuffle(możliweRuchy) # zrandomizuj kolejność ruchów

    # Zawsze postaraj się postawić pionek w polu narożnym, jeśli masz taką możliwość.
    for x, y in możliweRuchy:
        if wolnePoleNarożne(x, y):
            return [x, y]

    # Znajdź ruch dający najwięcej punktów.
    najwięcejPunktów = -1
    for x, y in możliweRuchy:
        kopiaPlanszy = wykonajKopięPlanszy(plansza)
        wykonajRuch(kopiaPlanszy, pionekKomputera, x, y)
        punkty = obliczWynikNaPlanszy(kopiaPlanszy)[pionekKomputera]
        if punkty > najwięcejPunktów:
            najlepszyRuch = [x, y]
            najwięcejPunktów = punkty
    return najlepszyRuch

def wyświetlWynik(plansza, pionekGracza, pionekKomputera):
    wyniki = obliczWynikNaPlanszy(plansza)
    print('Ty: %s punktów. Komputer: %s punktów.' % (wyniki[pionekGracza], wyniki[pionekKomputera]))

def zacznijGrać(pionekGracza, pionekKomputera):
    pokażPodpowiedzi = False
    tura = ktoZaczyna()
    print('To ' + tura + ' zacznie grę.')

    # Wyczyść planszę i ustaw na niej początkowe pionki.
    plansza = utwórzNowąPlanszę()
    plansza[3][3] = 'X'
    plansza[3][4] = 'O'
    plansza[4][3] = 'O'
    plansza[4][4] = 'X'

    while True:
        możliweRuchyGracza = znajdźDozwoloneRuchy(plansza, pionekGracza)
        możliweRuchyKomputera = znajdźDozwoloneRuchy(plansza, pionekKomputera)

        if możliweRuchyGracza == [] and możliweRuchyKomputera == []:
            return plansza # Nikt nie może wykonać ruchu, więc zakończ grę.

        elif tura == 'gracz': # Tura gracza
            if możliweRuchyGracza != []:
                # if pokażPodpowiedzi:
                #    planszaZPodpowiedziami = utwórzPlanszęZPodpowiedziami(plansza, pionekGracza)
                #    narysujPlanszę(planszaZPodpowiedziami)
                #else:
                #    narysujPlanszę(plansza)
                #wyświetlWynik(plansza, pionekGracza, pionekKomputera)

                ruch = ustalRuchKomputera(plansza, pionekGracza)
                #if ruch == 'koniec':
                #    print('Dzięki za grę!')
                #    sys.exit() # Zakończ program.
                #elif ruch == 'pomoc':
                #    pokażPodpowiedzi = not pokażPodpowiedzi
                #    continue
                #else:
                wykonajRuch(plansza, pionekGracza, ruch[0], ruch[1])
            tura = 'komputer'

        elif tura == 'komputer': # Tura komputera
            if możliweRuchyKomputera != []:
                #narysujPlanszę(plansza)
                #wyświetlWynik(plansza, pionekGracza, pionekKomputera)

                #input('Naciśnij ENTER, żeby zobaczyć ruch komputera.')
                ruch = ustalRuchKomputera(plansza, pionekKomputera)
                wykonajRuch(plansza, pionekKomputera, ruch[0], ruch[1])
            tura = 'gracz'



print('Witaj w grze Reversegam!')

pionekGracza, pionekKomputera = ['X', 'O'] #graczWybieraKolor()

while True:
    ostatecznaPlansza = zacznijGrać(pionekGracza, pionekKomputera)

    # Wyświetl ostateczny wynik.
    narysujPlanszę(ostatecznaPlansza)
    wyniki = obliczWynikNaPlanszy(ostatecznaPlansza)
    print('X zdobywa %s punktów. O zdobywa %s punktów.' % (wyniki['X'], wyniki['O']))
    if wyniki[pionekGracza] > wyniki[pionekKomputera]:
        print('Komputer przegrał z tobą o %s punktów! Gratulacje!' % (wyniki[pionekGracza] - wyniki[pionekKomputera]))
    elif wyniki[pionekGracza] < wyniki[pionekKomputera]:
        print('Przegrywasz. Komputer wygrywa o %s punktów.' % (wyniki[pionekKomputera] - wyniki[pionekGracza]))
    else:
        print('Gra zakończyła się remisem!')

    print('Chcesz zagrać ponownie? (tak lub nie)')
    if not input().lower().startswith('t'):
        break
