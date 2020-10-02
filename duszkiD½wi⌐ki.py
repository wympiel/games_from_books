import pygame, sys, time, random
from pygame.locals import *

# Skonfiguruj pygame.
pygame.init()
głównyZegar = pygame.time.Clock()

# Skonfiguruj okno.
SZEROKOŚĆOKNA = 400
WYSOKOŚĆOKNA = 400
powierzchniaOkna = pygame.display.set_mode((SZEROKOŚĆOKNA, WYSOKOŚĆOKNA), 0, 32)
pygame.display.set_caption('Duszki i dźwięki')

# Skonfiguruj kolory.
BIAŁY = (255, 255, 255)

# Skonfiguruj strukturę danych z blokiem.
gracz = pygame.Rect(300, 100, 40, 40)
obrazekGracza = pygame.image.load('gracz.png')
rozciągniętyObrazekGracza = pygame.transform.scale(obrazekGracza, (40, 40))
obrazekJedzonka = pygame.image.load('jedzonko.png')
jedzonka = []
for i in range(20):
    jedzonka.append(pygame.Rect(random.randint(0, SZEROKOŚĆOKNA - 20), random.randint(0, WYSOKOŚĆOKNA - 20), 20, 20))

licznikJedzonek = 0
NOWEJEDZONKO = 40

# Skonfiguruj zmienne związane z klawiszami.
ruchLewa = False
ruchPrawa = False
ruchGóra = False
ruchDół = False

SZYBKOŚĆRUCHU = 6

# Skonfiguruj muzykę.
odgłosZjadania = pygame.mixer.Sound('mniam.wav')
pygame.mixer.music.load('muzyczka.mid')
pygame.mixer.music.play(-1, 0.0)
graMuzyka = True

# Wykonuj główną pętlę gry.
while True:
    # Sprawdź, czy zaszło zdarzenie QUIT.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            # Zmień wartości zmiennych związanych z klawiszami.
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
            if event.key == K_m:
                if graMuzyka:
                    pygame.mixer.music.stop()
                else:
                    pygame.mixer.music.play(-1, 0.0)
                graMuzyka = not graMuzyka

        if event.type == MOUSEBUTTONUP:
            jedzonka.append(pygame.Rect(event.pos[0] - 10, event.pos[1] - 10, 20, 20))

    licznikJedzonek += 1
    if licznikJedzonek >= NOWEJEDZONKO:
        # Dodaj nowe jedzonko.
        licznikJedzonek = 0
        jedzonka.append(pygame.Rect(random.randint(0, SZEROKOŚĆOKNA - 20), random.randint(0, WYSOKOŚĆOKNA - 20), 20, 20))

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


    # Narysuj blok na powierzchni.
    powierzchniaOkna.blit(rozciągniętyObrazekGracza, gracz)

    # Sprawdź, czy doszło do kolizji bloku z którymś z kwadracików z jedzonkiem.
    for jedzonko in jedzonka[:]:
        if gracz.colliderect(jedzonko):
            jedzonka.remove(jedzonko)
            gracz = pygame.Rect(gracz.left, gracz.top, gracz.width + 2, gracz.height + 2)
            rozciągniętyObrazekGracza = pygame.transform.scale(obrazekGracza, (gracz.width, gracz.height))
            if graMuzyka:
                odgłosZjadania.play()

    # Narysuj jedzonko.
    for jedzonko in jedzonka:
        powierzchniaOkna.blit(obrazekJedzonka, jedzonko)

    # Narysuj okno na ekranie.
    pygame.display.update()
    głównyZegar.tick(40 )
