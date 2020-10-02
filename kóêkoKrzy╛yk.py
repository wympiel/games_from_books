# Kółko i krzyżyk

import random

def narysujPlanszę(plansza):
    # Ta funkcja wyświetla przekazany do niej argument plansza.

    # "plansza" to lista zawierająca 10 łańcuchów, reprezentujących planszę (ignorujemy indeks 0)
    print(plansza[7] + '|' + plansza[8] + '|' + plansza[9])
    print('-+-+-')
    print(plansza[4] + '|' + plansza[5] + '|' + plansza[6])
    print('-+-+-')
    print(plansza[1] + '|' + plansza[2] + '|' + plansza[3])

def wczytajLiteręGracza():
    # Niech gracz wybierze swoją literę.
    # Zwraca listę, na której pierwszym elementem jest litera gracza, a drugim – litera komputera.
    litera = ''
    while not (litera == 'X' or litera == 'O'):
        print('Chcesz używać znaku X czy O?')
        litera = input().upper()

    # Pierwszym elementem na liście jest litera gracza, a drugim – litera komputera.
    if litera == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def ktoZaczyna():
    # Losowo wybierz gracza, który wykona pierwszy ruch.
    if random.randint(0, 1) == 0:
        return 'komputer'
    else:
        return 'gracz'

def wykonajRuch(plansza, litera, ruch):
    plansza[ruch] = litera

def czyJestZwycięstwo(pl, li):
    # Znając stan planszy i literę gracza, funkcja ta zwraca True, jeśli gracz wygrał.
    # Używamy pl zamiast plansza i li zamiast litera, aby mieć mniej do wpisywania.
    return ((pl[7] == li and pl[8] == li and pl[9] == li) or # górny wiersz
    (pl[4] == li and pl[5] == li and pl[6] == li) or # środkowy wiersz
    (pl[1] == li and pl[2] == li and pl[3] == li) or # dolny wiersz
    (pl[7] == li and pl[4] == li and pl[1] == li) or # lewa kolumna
    (pl[8] == li and pl[5] == li and pl[2] == li) or # środkowa kolumna
    (pl[9] == li and pl[6] == li and pl[3] == li) or # prawa kolumna
    (pl[7] == li and pl[5] == li and pl[3] == li) or # przekątna
    (pl[9] == li and pl[5] == li and pl[1] == li)) # przekątna

def wykonajKopięPlanszy(plansza):
    # Wykonaj kopię listy z planszą i zwróć ją.
    kopiaPlanszy = []
    for i in plansza:
        kopiaPlanszy.append(i)
    return kopiaPlanszy

def czyPoleJestWolne(plansza, ruch):
    # Zwróć True, jeśli przesłany ruch można wykonać na przesłanej planszy.
    return plansza[ruch] == ' '

def wczytajRuchGracza(plansza):
    # Pozwól graczowi podać ruch.
    ruch = ' '
    while ruch not in '1 2 3 4 5 6 7 8 9'.split() or not czyPoleJestWolne(plansza, int(ruch)):
        print('Jaki jest twój następny ruch? (1-9)')
        ruch = input()
    return int(ruch)

def wylosujRuchZlisty(plansza, listaRuchów):
    # Zwraca prawidłowy ruch z przesłanej listy na przesłanej planszy.
    # Zwraca None, jeśli nie można wykonać ruchu.
    możliweRuchy = []
    for i in listaRuchów:
        if czyPoleJestWolne(plansza, i):
            możliweRuchy.append(i)

    if len(możliweRuchy) != 0:
        return random.choice(możliweRuchy)
    else:
        return None

def ustalRuchKomputera(plansza, literaKomputera):
    # Znając planszę i literę komputera, ustal gdzie wykonać ruch i zwróć ten ruch.
    if literaKomputera == 'X':
        literaGracza = 'O'
    else:
        literaGracza = 'X'

    # Oto algorytm naszej SI do gry Kółko i krzyżyk:
    # Najpierw sprawdzamy, czy możemy wygrać w kolejnym ruchu
    for i in range(1, 10):
        kopiaPlanszy = wykonajKopięPlanszy(plansza)
        if czyPoleJestWolne(kopiaPlanszy, i):
            wykonajRuch(kopiaPlanszy, literaKomputera, i)
            if czyJestZwycięstwo(kopiaPlanszy, literaKomputera):
                return i

    # Sprawdź czy gracz może wygrać w kolejnym ruchu i zablokuj go.
    for i in range(1, 10):
        kopiaPlanszy = wykonajKopięPlanszy(plansza)
        if czyPoleJestWolne(kopiaPlanszy, i):
            wykonajRuch(kopiaPlanszy, literaGracza, i)
            if czyJestZwycięstwo(kopiaPlanszy, literaGracza):
                return i

    # Spróbuj zająć jedno z pól narożnych, jeśli są wolne.
    ruch = wylosujRuchZlisty(plansza, [1, 3, 7, 9])
    if ruch != None:
        return ruch

    # Spróbuj zająć pole centralne, jeśli jest wolne.
    if czyPoleJestWolne(plansza, 5):
        return 5

    # Wykonaj ruch na jednym z pól bocznych.
    return wylosujRuchZlisty(plansza, [2, 4, 6, 8])

def czyPlanszaJestPełna(plansza):
    # Zwróć True, jeśli wszystkie pola na planszy są zajęte. W przeciwnym wypadku zwróć False.
    for i in range(1, 10):
        if czyPoleJestWolne(plansza, i):
            return False
    return True


print('Witaj w grze Kółko i krzyżyk!')

while True:
    # Zresetuj planszę
    taPlansza = [' '] * 10
    literaGracza, literaKomputera = wczytajLiteręGracza()
    tura = ktoZaczyna()
    print('To ' + tura + ' zaczyna grę.')
    graTrwa = True

    while graTrwa:
        if tura == 'gracz':
            # Tura gracza.
            narysujPlanszę(taPlansza)
            ruch = wczytajRuchGracza(taPlansza)
            wykonajRuch(taPlansza, literaGracza, ruch)

            if czyJestZwycięstwo(taPlansza, literaGracza):
                narysujPlanszę(taPlansza)
                print('Hura! Zwycięstwo!')
                graTrwa = False
            else:
                if czyPlanszaJestPełna(taPlansza):
                    narysujPlanszę(taPlansza)
                    print('Gra zakończyła się remisem!')
                    break
                else:
                    tura = 'komputer'

        else:
            # Tura komputera.
            ruch = ustalRuchKomputera(taPlansza, literaKomputera)
            wykonajRuch(taPlansza, literaKomputera, ruch)

            if czyJestZwycięstwo(taPlansza, literaKomputera):
                narysujPlanszę(taPlansza)
                print('Komputer cię pokonał! Przegrywasz.')
                graTrwa = False
            else:
                if czyPlanszaJestPełna(taPlansza):
                    narysujPlanszę(taPlansza)
                    print('Gra zakończyła się remisem!')
                    break
                else:
                    tura = 'gracz'

    print('Chcesz zagrać ponownie? (tak lub nie)')
    if not input().lower().startswith('t'):
        break
