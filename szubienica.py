import random
SZUBIENICA_OBRAZKI = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
     ===''']
słowa = 'baran bocian borsuk bóbr foka fretka gęś gołąb indyk jastrząb jaszczurka jeleń kaczka kobra kojot kot koza kret królik kruk lama leniwiec lew lis łabędź łasica łosoś łoś małpa małż mrówka muł mysz niedźwiedź nietoperz nosorożec orzeł osioł owca pająk panda papuga pawian pies pstrąg puma pyton rekin ropucha skunks sowa szczur traszka tygrys wąż wielbłąd wieloryb wilk wombat wrona wydra zebra żaba żółw'.split()

def wylosujSłowo(listaSłów):
    # Ta funkcja zwraca losowy łańcuch z przesłanej do niej listy łańcuchów.
    indeksSłowa = random.randint(0, len(listaSłów) - 1)
    return listaSłów[indeksSłowa]

def wyświetlPlanszę(strzałyNiecelne, strzałyCelne, tajneSłowo):
    print(SZUBIENICA_OBRAZKI[len(strzałyNiecelne)])
    print()

    print('Strzały niecelne:', end=' ')
    for litera in strzałyNiecelne:
        print(litera, end=' ')
    print()

    pusteMiejsca = '_' * len(tajneSłowo)

    for i in range(len(tajneSłowo)): # Zamieniaj puste miejsca na odgadnięte litery
        if tajneSłowo[i] in strzałyCelne:
            pusteMiejsca = pusteMiejsca[:i] + tajneSłowo[i] + pusteMiejsca[i+1:]

    for litera in pusteMiejsca: # Wyświetl tajne słowo, oddzielając litery spacjami
        print(litera, end=' ')
    print()

def wczytajStrzał(jużPodawane):
    # Zwraca literę podaną przez gracza. Funkcja ta sprawdza, czy gracz podał jedną literę, a nie coś innego.
    while True:
        print('Podaj literę.')
        strzał = input()
        strzał = strzał.lower()
        if len(strzał) != 1:
            print('Proszę podaj jedną literę.')
        elif strzał in jużPodawane:
            print('Ta litera już była. Spróbuj ponownie.')
        elif strzał not in 'aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż':
            print('Proszę podać LITERĘ.')
        else:
            return strzał

def zagrajPonownie():
    # Funkcja ta zwraca True, jeśli gracz chce zagrać ponownie; w przeciwnym wypadku zwraca False.
    print('Chcesz zagrać ponownie? (tak lub nie)')
    return input().lower().startswith('t')


print('S Z U B I E N I C A')
strzałyNiecelne = ''
strzałyCelne = ''
tajneSłowo = wylosujSłowo(słowa)
koniecGry = False

while True:
    wyświetlPlanszę(strzałyNiecelne, strzałyCelne, tajneSłowo)

    # Pozwól graczowi podać literę.
    strzał = wczytajStrzał(strzałyNiecelne + strzałyCelne)

    if strzał in tajneSłowo:
        strzałyCelne = strzałyCelne + strzał

        # Sprawdź, czy gracz wygrał.
        wszystkieLiteryOdgadnięte = True
        for i in range(len(tajneSłowo)):
            if tajneSłowo[i] not in strzałyCelne:
                wszystkieLiteryOdgadnięte = False
                break
        if wszystkieLiteryOdgadnięte:
            print('Tak! Tajne słowo to "' + tajneSłowo + '"! Zwycięstwo!')
            koniecGry = True
    else:
        strzałyNiecelne = strzałyNiecelne + strzał

        # Sprawdź, czy gracz wykonał zbyt wiele prób i przegrał.
        if len(strzałyNiecelne) == len(SZUBIENICA_OBRAZKI) - 1:
            wyświetlPlanszę(strzałyNiecelne, strzałyCelne, tajneSłowo)
            print('Nie masz już więcej strzałów!\nPo ' + str(len(strzałyNiecelne)) + ' strzałach niecelnych i ' + str(len(strzałyCelne)) + ' strzałach celnych, tajne słowo to "' + tajneSłowo + '"')
            koniecGry = True

    # Zapytaj gracza, czy chce zagrać ponownie (ale tylko jeśli gra się skończyła).
    if koniecGry:
        if zagrajPonownie():
            strzałyNiecelne = ''
            strzałyCelne = ''
            koniecGry = False
            tajneSłowo = wylosujSłowo(słowa)
        else:
            break
