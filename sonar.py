# Poszukiwanie skarbu sonarem

import random
import sys
import math

def utwórzNowąPlanszę():
    # Tworzymy nową strukturę danych z planszą 60x15.
    plansza = []
    for x in range(60): # Główna lista zawiera 60 list.
        plansza.append([])
        for y in range(15): # Każda lista na liście głównej zawiera 15 jednoznakowych łańcuchów.
            # Użyj różnych znaków na fale oceanu, aby uzyskać lepszy efekt.
            if random.randint(0, 1) == 0:
                plansza[x].append('~')
            else:
                plansza[x].append('`')
    return plansza

def narysujPlanszę(plansza):
    # Narysuj strukturę danych z planszą.
    wierszCyfryDziesiętne = '    ' # Początkowy odstęp dla liczb po lewej stronie planszy.
    for i in range(1, 6):
        wierszCyfryDziesiętne += (' ' * 9) + str(i)

    # Wyświetl liczby wzdłuż górnej krawędzi planszy.
    print(wierszCyfryDziesiętne)
    print('   ' + ('0123456789' * 6))
    print()

    # Wyświetl każdy z 15 wierszy.
    for wiersz in range(15):
        # Liczby jednocyfrowe wymagają uzupełnienia dodatkową spacją.
        if wiersz < 10:
            dodatkowaSpacja = ' '
        else:
            dodatkowaSpacja = ''

        # Utwórz łańcuch dla tego wiersza na planszy.
        wierszPlanszy = ''
        for kolumna in range(60):
            wierszPlanszy += plansza[kolumna][wiersz]

        print('%s%s %s %s' % (dodatkowaSpacja, wiersz, wierszPlanszy, wiersz))

    # Wyświetl liczby wzdłuż dolnej krawędzi.
    print()
    print('   ' + ('0123456789' * 6))
    print(wierszCyfryDziesiętne)

def ukryjLosowoSkrzynie(liczbaSkrzyń):
    # Utwórz listę ze strukturami danych ze skrzyniami (dwuelementowe listy z całkowitoliczbowymi współrzędnymi x, y).
    skrzynie = []
    while len(skrzynie) < liczbaSkrzyń:
        nowaSkrzynia = [random.randint(0, 59), random.randint(0, 14)]
        if nowaSkrzynia not in skrzynie: # Upewnij się, że nie ma w tym miejscu skrzyni.
            skrzynie.append(nowaSkrzynia)
    return skrzynie

def jestNaPlanszy(x, y):
    # Zwróć True, jeśli te współrzędne są na planszy. W przeciwnym wypadku zwróć False.
    return x >= 0 and x <= 59 and y >= 0 and y <= 14

def wykonajRuch(plansza, skrzynie, x, y):
    # Zmień strukturę danych z planszą, wprowadzając znak reprezentujący sonar. Usuwaj znajdowane skrzynie ze skarbami
    # z listy skrzynie. Zwróć False, jeśli ruch ten jest nieprawidłowy.
    # W przeciwnym razie zwróć łańcuch z wynikiem tego ruchu.
    najmniejszaOdległość = 100 # wszystkie skrzynie będą w odległości mniejszej niż 100.
    for cx, cy in skrzynie:
        odległość = math.sqrt((cx - x) * (cx - x) + (cy - y) * (cy - y))

        if odległość < najmniejszaOdległość: # Interesuje nas najbliższa skrzynia ze skarbami.
            najmniejszaOdległość = odległość

    najmniejszaOdległość = round(najmniejszaOdległość)

    if najmniejszaOdległość == 0:
        # Punkt xy jest bezpośrednio nad skrzynią ze skarbem!
        skrzynie.remove([x, y])
        return 'Znaleziono skrzynię ze skarbami!'
    else:
        if najmniejszaOdległość < 10:
            plansza[x][y] = str(najmniejszaOdległość)
            return 'Skarb wykryty w odległości %s od sonara.' % (najmniejszaOdległość)
        else:
            plansza[x][y] = 'X'
            return 'Sonar niczego nie wykrył. Wszystkie skrzynie ze skarbami poza zasięgiem.'

def wczytajRuchGracza(poprzednieRuchy):
    # Pozwól graczowi podać ruch. Zwróć dwuelementową listę z całkowitoliczbowymi współrzędnymi xy.
    print('Gdzie chcesz zanurzyć następny sonar? (0-59 0-14) (albo wpisz koniec)')
    while True:
        ruch = input()
        if ruch.lower() == 'koniec':
            print('Dzięki za grę!')
            sys.exit()

        ruch = ruch.split()
        if len(ruch) == 2 and ruch[0].isdigit() and ruch[1].isdigit() and jestNaPlanszy(int(ruch[0]), int(ruch[1])):
            if [int(ruch[0]), int(ruch[1])] in poprzednieRuchy:
                print('Tutaj ruch już był wykonywany.')
                continue
            return [int(ruch[0]), int(ruch[1])]

        print('Wpisz liczbę od 0 do 59, spację, a następnie liczbę od 0 do 14.')

def wyświetlInstrukcję():
    print('''Instrukcja:
Jesteś kapitanem na okręcie poszukiwaczy skarbów Simon. Twoja misja polega
na znalezieniu za pomocą sonarów trzech skrzyń zatopionych na dnie oceanu. Ale
twoje sonary to proste urządzenia, które podają odległość, lecz nie kierunek.

Wpisz współrzędne, gdzie chcesz zanurzyć sonar. Na mapie pojawi się informacja
o odległości do najbliższej skrzyni, albo X, jeśli skarb jest poza zasięgiem.
Na przykład C oznacza miejsce, w którym jest skrzynia. Sonar pokazuje 3,
ponieważ najbliższa skrzynia znajduje się w odległości 3 jednostek.

                    1         2         3
          012345678901234567890123456789012

        0 ~~~~`~```~`~``~~~``~`~~``~~~``~`~ 0
        1 ~`~`~``~~`~```~~~```~~`~`~~~`~~~~ 1
        2 `~`C``3`~~~~`C`~~~~`````~~``~~~`` 2
        3 ````````~~~`````~~~`~`````~`~``~` 3
        4 ~`~~~~`~~`~~`C`~``~~`~~~`~```~``~ 4

          012345678901234567890123456789012
                    1         2         3
(W prawdziwej grze skrzynie są niewidoczne.)

Naciśnij ENTER, żeby kontynuować...''')
    input()

    print('''Gdy sonar znajdzie się bezpośrednio nad skrzynią, wyciągasz ją,
a pozostałe sonary aktualizują dane o położeniu względem kolejnej skrzyni.
Skrzynie są poza zasięgiem sonaru z lewej, więc na planszy pojawia się X.

                    1         2         3
          012345678901234567890123456789012

        0 ~~~~`~```~`~``~~~``~`~~``~~~``~`~ 0
        1 ~`~`~``~~`~```~~~```~~`~`~~~`~~~~ 1
        2 `~`X``7`~~~~`C`~~~~`````~~``~~~`` 2
        3 ````````~~~`````~~~`~`````~`~``~` 3
        4 ~`~~~~`~~`~~`C`~``~~`~~~`~```~``~ 4

          012345678901234567890123456789012
                    1         2         3

Skrzynie ze skarbami nie zmieniają miejsca. Sonary wykrywają skrzynie
znajdujące się w odległości do 9 jednostek. Spróbuj znaleźć wszystkie
3 skrzynie, zanim skończą ci się sonary. Powodzenia!

Naciśnij ENTER, aby kontynuować...''')
    input()



print('S O N A R !')
print()
print('Czy chcesz przeczytać instrukcję? (tak/nie)')
if input().lower().startswith('t'):
    wyświetlInstrukcję()

while True:
    # Konfiguracja gry
    liczbaSonarów = 20
    taPlansza = utwórzNowąPlanszę()
    teSkrzynie = ukryjLosowoSkrzynie(3)
    narysujPlanszę(taPlansza)
    poprzednieRuchy = []

    while liczbaSonarów > 0:
        # Pokaż informację o liczbie sonarów i skrzyń.
        print('Zostało ci %s sonarów. Pozostały jeszcze %s skrzynie ze skarbami.' % (liczbaSonarów, len(teSkrzynie)))

        x, y = wczytajRuchGracza(poprzednieRuchy)
        poprzednieRuchy.append([x, y]) # Musimy śledzić wszystkie ruchy, aby sonary można było aktualizować.

        skutekRuchu = wykonajRuch(taPlansza, teSkrzynie, x, y)
        if skutekRuchu == False:
            continue
        else:
            if skutekRuchu == 'Znaleziono skrzynię ze skarbami!':
                # Aktualizuje wszystkie sonary znajdujące się obecnie na mapie.
                for x, y in poprzednieRuchy:
                    wykonajRuch(taPlansza, teSkrzynie, x, y)
            narysujPlanszę(taPlansza)
            print(skutekRuchu)

        if len(teSkrzynie) == 0:
            print('Wszystkie skrzynie ze skarbami znalezione! Gratulacje!')
            break

        liczbaSonarów -= 1

    if liczbaSonarów == 0:
        print('Nie masz już więcej sonarów! Trzeba zawrócić i popłynąć')
        print('do portu pozostawiając skarby! Koniec gry.')
        print('    Pozostałe skrzynie znajdowały się tu:')
        for x, y in teSkrzynie:
            print('    %s, %s' % (x, y))

    print('Czy chcesz zagrać ponownie? (tak lub nie)')
    if not input().lower().startswith('t'):
        sys.exit()
