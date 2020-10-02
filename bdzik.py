import random
liczba1 = random.randint(1, 10)
liczba2 = random.randint(1, 10)
print('Ile to jest ' + str(liczba1) + ' + ' + str(liczba2) + '?')
odpowiedź = input()
if odpowiedź == liczba1 + liczba2:
    print('Zgadza się!')
else:
    print('Źle! Prawidłowa odpowiedź to ' + str(liczba1 + liczba2))
