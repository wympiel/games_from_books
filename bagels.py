import random

ILE_CYFR = 3
ILE_PRÓB = 10

def uzyskajTajnąLiczbę():
    # Zwraca łańcuch zbudowany z niepowtarzających się losowych cyfr o długości ILE_CYFR.
    liczby = list(range(10))
    random.shuffle(liczby)
    tajnaLiczba = ''
    for i in range(ILE_CYFR):
        tajnaLiczba += str(liczby[i])
    return tajnaLiczba

def uzyskajPodpowiedzi(strzał, tajnaLiczba):
    # Zwraca łańcuch z wyświetlanymi użytkownikowi podpowiedziami Pico, Fermi i Bagels.
    if strzał == tajnaLiczba:
        return 'Zgadza się!'

    podpowiedzi = []
    for i in range(len(strzał)):
        if strzał[i] == tajnaLiczba[i]:
            podpowiedzi.append('Fermi')
        elif strzał[i] in tajnaLiczba:
            podpowiedzi.append('Pico')
    if len(podpowiedzi) == 0:
        return 'Bagels'

    podpowiedzi.sort()
    return ' '.join(podpowiedzi)

def zawieraTylkoCyfry(licz):
    # Zwraca True, jeśli wartością zmiennej licz jest łańcuch zawierający tylko cyfry. W przeciwnym wypadku zwraca False.
    if licz == '':
        return False

    for i in licz:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False

    return True


print('Myślę o %s-cyfrowej liczbie. Spróbuj ją odgadnąć.' % (ILE_CYFR))
print('Moje podpowiedzi to...')
print('Gdy mówię:     To oznacza:')
print('  Bagels       Żadna z cyfr nie jest prawidłowa.')
print('  Pico         Jedna z cyfr jest zgadza, ale nie jest na swoim miejscu.')
print('  Fermi        Jedna z cyfr się zgadza i jest na swoim miejscu.')

while True:
    tajnaLiczba = uzyskajTajnąLiczbę()
    print('Wybrałem liczbę. Masz %s prób, aby ją odgadnąć.' % (ILE_PRÓB))

    wykonanePróby = 1
    while wykonanePróby <= ILE_PRÓB:
        strzał = ''
        while len(strzał) != ILE_CYFR or not zawieraTylkoCyfry(strzał):
            print('Próba #%s: ' % (wykonanePróby))
            strzał = input()

        print(uzyskajPodpowiedzi(strzał, tajnaLiczba))
        wykonanePróby += 1

        if strzał == tajnaLiczba:
            break
        if wykonanePróby > ILE_PRÓB:
            print('Nie masz już więcej prób. Odpowiedź to %s.' % (tajnaLiczba))

    print('Chcesz zagrać ponownie? (tak lub nie)')
    if not input().lower().startswith('t'):
        break
