# To jest gra "Zgadnij jaka to liczba".
import random

wykonanePróby = 0

print('Cześć! Jak masz na imię?')
mojeImię = input()

liczba = random.randint(1, 20)
print('Słuchaj, ' + mojeImię + ', myślę o liczbie z przedziału od 1 do 20.')

for wykonanePróby in range(6):
    print('Spróbuj odgadnąć.') # Cztery spacje przed "print".
    próbaOdgadnięcia = input()
    próbaOdgadnięcia = int(próbaOdgadnięcia)

    if próbaOdgadnięcia < liczba:
        print('Twoja liczba jest za mała.') # Osiem spacji przed "print"

    if próbaOdgadnięcia > liczba:
        print('Twoja liczba jest za duża.')

    if próbaOdgadnięcia == liczba:
        break

if próbaOdgadnięcia == liczba:
    wykonanePróby = str(wykonanePróby + 1)
    print('Świetna robota, ' + mojeImię + '! Udało ci się odgadnąć w ' + wykonanePróby + ' próbach!')

if próbaOdgadnięcia != liczba:
    liczba = str(liczba)
    print('Niestety nie. Liczba, którą miałem na myśli, to ' + liczba + '.')
