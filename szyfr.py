# Szyfr Cezara
SYMBOLE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
MAX_ROZMIAR_KLUCZA = len(SYMBOLE)

def ustawTryb():
    while True:
        print('Chcesz szyfrować czy deszyfrować komunikat?')
        tryb = input().lower()
        if tryb in ['szyfrowanie', 's', 'deszyfrowanie', 'd']:
            return tryb
        else:
            print('Wpisz "szyfrowanie" lub "s" lub "deszyfrowanie" lub "d".')

def wczytajKomunikat():
    print('Wpisz swój komunikat:')
    return input()

def wczytajKlucz():
    klucz = 0
    while True:
        print('Podaj liczbowy klucz (1-%s)' % (MAX_ROZMIAR_KLUCZA))
        klucz = int(input())
        if (klucz >= 1 and klucz <= MAX_ROZMIAR_KLUCZA):
            return klucz

def przekształćKomunikat(tryb, komunikat, klucz):
    if tryb[0] == 'd':
        klucz = -klucz
    poPrzekształceniu = ''

    for symbol in komunikat:
        indeksSymbolu = SYMBOLE.find(symbol)
        if indeksSymbolu == -1: # Symbol nie znajduje się w SYMBOLE.
            # Dodaj ten symbol bez żadnych zmian.
            poPrzekształceniu += symbol
        else:
            # Szyfrowanie lub deszyfrowanie
            indeksSymbolu += klucz

            if indeksSymbolu >= len(SYMBOLE):
                indeksSymbolu -= len(SYMBOLE)
            elif indeksSymbolu < 0:
                indeksSymbolu += len(SYMBOLE)

            poPrzekształceniu += SYMBOLE[indeksSymbolu]
    return poPrzekształceniu

tryb = ustawTryb()
komunikat = wczytajKomunikat()
klucz = wczytajKlucz()
print('Twój komunikat po przekształceniu brzmi:')
print(przekształćKomunikat(tryb, komunikat, klucz))
