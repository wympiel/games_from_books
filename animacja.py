import pygame, sys, time
from pygame.locals import *

# Skonfiguruj pygame.
pygame.init()

# Skonfiguruj okno.
SZEROKOŚĆOKNA = 400
WYSOKOŚĆOKNA = 400
powierzchniaOkna = pygame.display.set_mode((SZEROKOŚĆOKNA, WYSOKOŚĆOKNA), 0, 32)
pygame.display.set_caption('Animacja')

# Skonfiguruj zmienne związane z kierunkami.
LEWADÓŁ = 'lewaDół'
PRAWADÓŁ = 'prawaDół'
LEWAGÓRA = 'lewaGóra'
PRAWAGÓRA = 'prawaGóra'

SZYBKOŚĆRUCHU = 4

# Skonfiguruj kolory.
BIAŁY = (255, 255, 255)
CZERWONY = (255, 0, 0)
ZIELONY = (0, 255, 0)
NIEBIESKI = (0, 0, 255)

# Skonfiguruj struktury danych z ramkami.
r1 = {'rect':pygame.Rect(300, 80, 50, 100), 'kolor':CZERWONY, 'kier':PRAWAGÓRA}
r2 = {'rect':pygame.Rect(200, 200, 20, 20), 'kolor':ZIELONY, 'kier':LEWAGÓRA}
r3 = {'rect':pygame.Rect(100, 150, 60, 60), 'kolor':NIEBIESKI, 'kier':LEWADÓŁ}
ramki = [r1, r2, r3]

# Wykonuj główną pętlę gry.
while True:
    # Sprawdź, czy zaszło zdarzenie QUIT.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Narysuj na powierzchni białe tło.
    powierzchniaOkna.fill(BIAŁY)

    for r in ramki:
        # Przemieść strukturę danych z ramką.
        if r['kier'] == LEWADÓŁ:
            r['rect'].left -= SZYBKOŚĆRUCHU
            r['rect'].top += SZYBKOŚĆRUCHU
        if r['kier'] == PRAWADÓŁ:
            r['rect'].left += SZYBKOŚĆRUCHU
            r['rect'].top += SZYBKOŚĆRUCHU
        if r['kier'] == LEWAGÓRA:
            r['rect'].left -= SZYBKOŚĆRUCHU
            r['rect'].top -= SZYBKOŚĆRUCHU
        if r['kier'] == PRAWAGÓRA:
            r['rect'].left += SZYBKOŚĆRUCHU
            r['rect'].top -= SZYBKOŚĆRUCHU

        # Sprawdź, czy ramka nie wyszła za okno.
        if r['rect'].top < 0:
            # Ramka wyszła za górną krawędź.
            if r['kier'] == LEWAGÓRA:
                r['kier'] = LEWADÓŁ
            if r['kier'] == PRAWAGÓRA:
                r['kier'] = PRAWADÓŁ
        if r['rect'].bottom > WYSOKOŚĆOKNA:
            # Ramka wyszła za dolną krawędź.
            if r['kier'] == LEWADÓŁ:
                r['kier'] = LEWAGÓRA
            if r['kier'] == PRAWADÓŁ:
                r['kier'] = PRAWAGÓRA
        if r['rect'].left < 0:
            # Ramka wyszła za lewą krawędź.
            if r['kier'] == LEWADÓŁ:
                r['kier'] = PRAWADÓŁ
            if r['kier'] == LEWAGÓRA:
                r['kier'] = PRAWAGÓRA
        if r['rect'].right > SZEROKOŚĆOKNA:
            # Ramka wyszła za prawą krawędź.
            if r['kier'] == PRAWADÓŁ:
                r['kier'] = LEWADÓŁ
            if r['kier'] == PRAWAGÓRA:
                r['kier'] = LEWAGÓRA

        # Narysuj ramkę na powierzchni.
        pygame.draw.rect(powierzchniaOkna, r['kolor'], r['rect'])

    # Narysuj okno na ekranie.
    pygame.display.update()
    time.sleep(0.02)
