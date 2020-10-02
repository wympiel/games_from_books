import pygame, random, sys
from pygame.locals import *

SZEROKOŚĆOKNA = 600
WYSOKOŚĆOKNA = 600
KOLORTEKSTU = (0, 0, 0)
KOLORTŁA = (255, 255, 255)
FPS = 60
MINROZMIARPASKUDY = 10
MAXROZMIARPASKUDY = 40
MINSZYBKOŚĆPASKUDY = 1
MAXSZYBKOŚĆPASKUDY = 8
SZYBKOŚĆDODAWANIAPASKUD = 6
SZYBKOŚĆGRACZA = 5

def zakończ():
    pygame.quit()
    sys.exit()

def czekajAżGraczNaciśnieKlawisz():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                zakończ()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: # Naciśnięcie klawisza ESC zamyka program.
                    zakończ()
                return

def graczTrafiłPaskudę(postaćGracza, paskudy):
    for b in paskudy:
        if postaćGracza.colliderect(b['rect']):
            return True
    return False

def narysujTekst(tekst, czcionka, powierzchnia, x, y):
    tekstObiekt = czcionka.render(tekst, 1, KOLORTEKSTU)
    tekstProstokąt = tekstObiekt.get_rect()
    tekstProstokąt.topleft = (x, y)
    powierzchnia.blit(tekstObiekt, tekstProstokąt)

# Skonfiguruj pygame, okno i wskaźnik myszy.
pygame.init()
głównyZegar = pygame.time.Clock()
powierzchniaOkna = pygame.display.set_mode((SZEROKOŚĆOKNA, WYSOKOŚĆOKNA))
pygame.display.set_caption('Dodger')
pygame.mouse.set_visible(False)

# Skonfiguruj czcionki.
czcionka = pygame.font.SysFont(None, 48)

# Skonfiguruj dźwięki.
dźwiękKoniecGry = pygame.mixer.Sound('koniecGry.wav')
pygame.mixer.music.load('muzyczka.mid')

# Skonfiguruj obrazy.
obrazekGracza = pygame.image.load('gracz.png')
postaćGracza = obrazekGracza.get_rect()
obrazekPaskudy = pygame.image.load('paskuda.png')

# Wyświetl ekran "startowy".
powierzchniaOkna.fill(KOLORTŁA)
narysujTekst('Dodger', czcionka, powierzchniaOkna, (SZEROKOŚĆOKNA / 3), (WYSOKOŚĆOKNA / 3))
narysujTekst('Naciśnij jakiś klawisz.', czcionka, powierzchniaOkna, (SZEROKOŚĆOKNA / 3) - 30, (WYSOKOŚĆOKNA / 3) + 50)
pygame.display.update()
czekajAżGraczNaciśnieKlawisz()

najlepszyWynik = 0
while True:
    # Skonfiguruj początek gry.
    paskudy = []
    punkty = 0
    postaćGracza.topleft = (SZEROKOŚĆOKNA / 2, WYSOKOŚĆOKNA - 50)
    ruchLewa = ruchPrawa = ruchGóra = ruchDół = False
    cheatZmianaKierunku = cheatSpowalnianie = False
    licznikDodawaniaPaskud = 0
    pygame.mixer.music.play(-1, 0.0)

    while True: # Główna pętla gry jest wykonywana dopóki trwa gra.
        punkty += 1 # Zwiększ wynik.

        for event in pygame.event.get():
            if event.type == QUIT:
                zakończ()

            if event.type == KEYDOWN:
                if event.key == K_z:
                    cheatZmianaKierunku = True
                if event.key == K_x:
                    cheatSpowalnianie = True
                if event.key == K_LEFT or event.key == K_a:
                    ruchPrawa = False
                    ruchLewa = True
                if event.key == K_RIGHT or event.key == K_d:
                    ruchLewa = False
                    ruchPrawa = True
                if event.key == K_UP or event.key == K_w:
                    ruchDół = False
                    ruchGóra = True
                if event.key == K_DOWN or event.key == K_s:
                    ruchGóra = False
                    ruchDół = True

            if event.type == KEYUP:
                if event.key == K_z:
                    cheatZmianaKierunku = False
                    punkty = 0
                if event.key == K_x:
                    cheatSpowalnianie = False
                    punkty = 0
                if event.key == K_ESCAPE:
                        zakończ()

                if event.key == K_LEFT or event.key == K_a:
                    ruchLewa = False
                if event.key == K_RIGHT or event.key == K_d:
                    ruchPrawa = False
                if event.key == K_UP or event.key == K_w:
                    ruchGóra = False
                if event.key == K_DOWN or event.key == K_s:
                    ruchDół = False

            if event.type == MOUSEMOTION:
                # Jeśli mysz się poruszy, przenieś gracza tam, gdzie jerst kursor.
                postaćGracza.centerx = event.pos[0]
                postaćGracza.centery = event.pos[1]
        # Jeśli trzeba, dodawaj nowe paskudy na górze ekranu.
        if not cheatZmianaKierunku and not cheatSpowalnianie:
            licznikDodawaniaPaskud += 1
        if licznikDodawaniaPaskud == SZYBKOŚĆDODAWANIAPASKUD:
            licznikDodawaniaPaskud = 0
            rozmiarPaskudy = random.randint(MINROZMIARPASKUDY, MAXROZMIARPASKUDY)
            nowaPaskuda = {'rect': pygame.Rect(random.randint(0, SZEROKOŚĆOKNA - rozmiarPaskudy), 0 - rozmiarPaskudy, rozmiarPaskudy, rozmiarPaskudy),
                        'szybkość': random.randint(MINSZYBKOŚĆPASKUDY, MAXSZYBKOŚĆPASKUDY),
                        'powierzchnia':pygame.transform.scale(obrazekPaskudy, (rozmiarPaskudy, rozmiarPaskudy)),
                        }

            paskudy.append(nowaPaskuda)

        # Przemieszczaj postać gracza.
        if ruchLewa and postaćGracza.left > 0:
            postaćGracza.move_ip(-1 * SZYBKOŚĆGRACZA, 0)
        if ruchPrawa and postaćGracza.right < SZEROKOŚĆOKNA:
            postaćGracza.move_ip(SZYBKOŚĆGRACZA, 0)
        if ruchGóra and postaćGracza.top > 0:
            postaćGracza.move_ip(0, -1 * SZYBKOŚĆGRACZA)
        if ruchDół and postaćGracza.bottom < WYSOKOŚĆOKNA:
            postaćGracza.move_ip(0, SZYBKOŚĆGRACZA)

        # Przemieszczaj paskudy w dół ekranu.
        for p in paskudy:
            if not cheatZmianaKierunku and not cheatSpowalnianie:
                p['rect'].move_ip(0, p['szybkość'])
            elif cheatZmianaKierunku:
                p['rect'].move_ip(0, -5)
            elif cheatSpowalnianie:
                p['rect'].move_ip(0, 1)

        # Usuwaj paskudy, które przekroczyły dolną krawędź.
        for p in paskudy[:]:
            if p['rect'].top > WYSOKOŚĆOKNA:
                paskudy.remove(p)

        # Narysuj w oknie świat gry.
        powierzchniaOkna.fill(KOLORTŁA)

        # Narysuj wynik bieżący i najlepszy.
        narysujTekst('Wynik: %s' % (punkty), czcionka, powierzchniaOkna, 10, 0)
        narysujTekst('Najlepszy wynik: %s' % (najlepszyWynik), czcionka, powierzchniaOkna, 10, 40)

        # Narysuj prostokątną postać gracza.
        powierzchniaOkna.blit(obrazekGracza, postaćGracza)

        # Narysuj każdą paskudę.
        for p in paskudy:
            powierzchniaOkna.blit(p['powierzchnia'], p['rect'])

        pygame.display.update()

        # Sprawdź, czy żadna z paskud nie trafiła gracza.
        if graczTrafiłPaskudę(postaćGracza, paskudy):
            if punkty > najlepszyWynik:
                najlepszyWynik = punkty # ustaw nowy najlepszy wynik
            break

        głównyZegar.tick(FPS)

    # Zatrzymaj grę i wyświetl ekran "Game Over".
    pygame.mixer.music.stop()
    dźwiękKoniecGry.play()

    narysujTekst('GAME OVER', czcionka, powierzchniaOkna, (SZEROKOŚĆOKNA / 3), (WYSOKOŚĆOKNA / 3))
    narysujTekst('Naciśnij klawisz, aby zagrać ponownie.', czcionka, powierzchniaOkna, (SZEROKOŚĆOKNA / 3) - 80, (WYSOKOŚĆOKNA / 3) + 50)
    pygame.display.update()
    czekajAżGraczNaciśnieKlawisz()

    dźwiękKoniecGry.stop()
