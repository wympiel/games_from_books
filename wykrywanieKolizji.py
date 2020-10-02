import pygame, sys, random
from pygame.locals import *

# Skonfiguruj pygame.
pygame.init()
głównyZegar = pygame.time.Clock()

# Skonfiguruj okno.
SZEROKOŚĆOKNA = 400
WYSOKOŚĆOKNA = 400
powierzchniaOkna = pygame.display.set_mode((SZEROKOŚĆOKNA, WYSOKOŚĆOKNA), 0, 32)
pygame.display.set_caption('Wykrywanie kolizji')

# Skonfiguruj kolory.
CZARNY = (0, 0, 0)
ZIELONY = (0, 255, 0)
BIAŁY = (255, 255, 255)

# Skonfiguruj struktury danych z graczem i jedzonkiem.
licznikJedzonek = 0
NOWEJEDZONKO = 40
ROZMIARJEDZONKA = 20
gracz = pygame.Rect(300, 100, 50, 50)
jedzonka = []
for i in range(20):
    jedzonka.append(pygame.Rect(random.randint(0, SZEROKOŚĆOKNA - ROZMIARJEDZONKA), random.randint(0, WYSOKOŚĆOKNA - ROZMIARJEDZONKA), ROZMIARJEDZONKA, ROZMIARJEDZONKA))

# Skonfiguruj zmienne związane z ruchem.
ruchLewa = False
ruchPrawa = False
ruchGóra = False
ruchDół = False

SZYBKOŚĆRUCHU = 6


# Wykonuj główną pętlę gry.
while True:
    # Sprawdź, czy zaszły jakieś zdarzenia.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            # Zmień wartość zmiennych związanych z klawiszami.
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
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT or event.key == K_a:
                ruchLewa = False
            if event.key == K_RIGHT or event.key == K_d:
                ruchPrawa = False
            if event.key == K_UP or event.key == K_w:
                ruchGóra = False
            if event.key == K_DOWN or event.key == K_s:
                ruchDół = False
            if event.key == K_x:
                gracz.top = random.randint(0, WYSOKOŚĆOKNA - gracz.height)
                gracz.left = random.randint(0, SZEROKOŚĆOKNA - gracz.width)

        if event.type == MOUSEBUTTONUP:
            jedzonka.append(pygame.Rect(event.pos[0], event.pos[1], ROZMIARJEDZONKA, ROZMIARJEDZONKA))

    licznikJedzonek += 1
    if licznikJedzonek >= NOWEJEDZONKO:
        # Dodaj nowe jedzonko.
        licznikJedzonek = 0
        jedzonka.append(pygame.Rect(random.randint(0, SZEROKOŚĆOKNA - ROZMIARJEDZONKA), random.randint(0, WYSOKOŚĆOKNA - ROZMIARJEDZONKA), ROZMIARJEDZONKA, ROZMIARJEDZONKA))

    # Narysuj białe tło na powierzchni.
    powierzchniaOkna.fill(BIAŁY)

    # Przemieść postać gracza.
    if ruchDół and gracz.bottom < WYSOKOŚĆOKNA:
        gracz.top += SZYBKOŚĆRUCHU
    if ruchGóra and gracz.top > 0:
        gracz.top -= SZYBKOŚĆRUCHU
    if ruchLewa and gracz.left > 0:
        gracz.left -= SZYBKOŚĆRUCHU
    if ruchPrawa and gracz.right < SZEROKOŚĆOKNA:
        gracz.right += SZYBKOŚĆRUCHU

    # Narysuj postać gracza na powierzchni.
    pygame.draw.rect(powierzchniaOkna, CZARNY, gracz)

    # Sprawdź, czy doszło do kolizji gracza z jakimś kwadracikiem pożywienia.
    for jedzonko in jedzonka[:]:
        if gracz.colliderect(jedzonko):
            jedzonka.remove(jedzonko)

    # Narysuj jedzonko.
    for i in range(len(jedzonka)):
        pygame.draw.rect(powierzchniaOkna, ZIELONY, jedzonka[i])

    # Narysuj okno na ekranie.
    pygame.display.update()
    głównyZegar.tick(40 )
