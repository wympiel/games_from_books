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
     ===''', '''
  +---+
 [O   |
 /|\  |
 / \  |
     ===''', '''
  +---+
 [O]  |
 /|\  |
 / \  |
     ===''']
słowa = {'Kolory':'czerwony pomarańczowy żółty zielony niebieski granatowy fioletowy biały czarny brązowy'.split(),
'Figury geometryczne':'kwadrat trójkąt prostokąt okrąg elipsa romb trapez deltoid pięciokąt sześciokąt siedmiokąt ośmiokąt'.split(),
'Owoce':'jabłko pomarańcza cytryna limona gruszka arbuz winogrono grejpfrut czereśnia banan kantalupa mango truskawka pomidor'.split(),
'Zwierzęta':'nietoperz niedźwiedź bóbr kot puma krab jeleń pies osioł kaczka orzeł ryba żaba koza pijawka lew jaszczurka małpa łoś mysz wydra sowa panda pyton królik szczur rekin owca skunks kalmar tygrys indyk żółw łasica wieloryb wilk wombat zebra'.split()}

def wylosujSłowo(słownikSłów):
    # Ta funkcja zwraca losowy łańcuch z przesłanego do niej słownika zawierającego listy łańcuchów, oraz klucz.
    # Najpierw, wybierz losowy klucz ze słownika:
    kluczSłowa = random.choice(list(słownikSłów.keys()))

    # Następnie, losowo wybierz słowo z listy znajdującej się pod tym kluczem w słowniku:
    indeksSłowa = random.randint(0, len(słownikSłów[kluczSłowa]) - 1)

    return [słownikSłów[kluczSłowa][indeksSłowa], kluczSłowa]

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

trudność = 'z'
while trudność not in 'NPW':
    print('Wybierz poziom trudnośći: N - Niski, P - Przeciętny, W - Wysoki')
    trudność = input().upper()
if trudność == 'P':
    del SZUBIENICA_OBRAZKI[8]
    del SZUBIENICA_OBRAZKI[7]
if trudność == 'W':
    del SZUBIENICA_OBRAZKI[8]
    del SZUBIENICA_OBRAZKI[7]
    del SZUBIENICA_OBRAZKI[5]
    del SZUBIENICA_OBRAZKI[3]

strzałyNiecelne = ''
strzałyCelne = ''
tajneSłowo, tajnaKategoria = wylosujSłowo(słowa)
koniecGry = False

while True:
    print('Tajne słowo należy do kategorii: ' + tajnaKategoria)
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
            tajneSłowo, tajnaKategoria = wylosujSłowo(słowa)
        else:
            break
