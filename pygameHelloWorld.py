import pygame, sys
from pygame.locals import *

# Skonfiguruj pygame.
pygame.init()

# Skonfiguruj okno.
powierzchniaOkna = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('Hello world!')

# Skonfiguruj kolory.
CZARNY = (0, 0, 0)
BIAŁY = (255, 255, 255)
CZERWONY = (255, 0, 0)
ZIELONY = (0, 255, 0)
NIEBIESKI = (0, 0, 255)

# Skonfiguruj czcionki.
podstawowaCzcionka = pygame.font.SysFont(None, 48)

# Skonfiguruj tekst.
tekst = podstawowaCzcionka.render('Hello world!', True, BIAŁY, NIEBIESKI)
prostTekst = tekst.get_rect()
prostTekst.centerx = powierzchniaOkna.get_rect().centerx
prostTekst.centery = powierzchniaOkna.get_rect().centery

# Narysuj na powierzchni białe tło.
powierzchniaOkna.fill(BIAŁY)

# Narysuj na powierzchni zielony wielokąt.
pygame.draw.polygon(powierzchniaOkna, ZIELONY, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))

# Narysuj na powierzchni kilka niebieskich odcinków.
pygame.draw.line(powierzchniaOkna, NIEBIESKI, (60, 60), (120, 60), 4)
pygame.draw.line(powierzchniaOkna, NIEBIESKI, (120, 60), (60, 120))
pygame.draw.line(powierzchniaOkna, NIEBIESKI, (60, 120), (120, 120), 4)

# Narysuj na powierzchni niebieski okrąg.
pygame.draw.circle(powierzchniaOkna, NIEBIESKI, (300, 50), 20, 0)

# Narysuj na powierzchni czerwoną elipsę.
pygame.draw.ellipse(powierzchniaOkna, CZERWONY, (300, 250, 40, 80), 1)

# Narysuj na powierzchni prostokątne tło tekstu.
pygame.draw.rect(powierzchniaOkna, CZERWONY, (prostTekst.left - 20, prostTekst.top - 20, prostTekst.width + 40, prostTekst.height + 40))

# Uzyskaj tablicę z pikselami powierzchni.
tablicaPikseli = pygame.PixelArray(powierzchniaOkna)
tablicaPikseli[480][380] = CZARNY
del tablicaPikseli

# Narysuj tekst na powierzchni.
powierzchniaOkna.blit(tekst, prostTekst)

# Narysuj okno na ekranie.
pygame.display.update()

# Wykonuj główną pętlę gry.
while True:
    for zdarzenie in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
