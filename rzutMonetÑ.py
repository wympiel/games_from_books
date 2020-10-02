import random
print('Rzucę monetą 1000 razy. Zgadnij ile razy wypadnie reszka. (Naciśnij ENTER, aby rozpocząć)')
input()
rzuty = 0
reszka = 0
while rzuty < 1000:
    if random.randint(0, 1) == 1:
        reszka = reszka + 1
    rzuty = rzuty + 1

    if rzuty == 900:
        print('900 rzutów i ' + str(reszka) + ' razy wypadła reszka.')
    if rzuty == 100:
        print('Na 100 rzutów reszka wypadła ' + str(reszka) + ' razy.')
    if rzuty == 500:
        print('Połowa za nami, a reszka wypadła ' + str(reszka) + ' razy.')

print()
print('Na 1000 rzutów monetą, reszka wypadła ' + str(reszka) + ' razy!')
print('Było blisko?')
