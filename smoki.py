import random
import time

def wyświetlIntro():
    print('''Znajdujesz się w krainie smoków. Przed sobą
widzisz dwie jaskinie. W jednej mieszka przyjazny smok,
który podzieli się z tobą swoim skarbem. Drugi smok jest 
chciwy i głodny, więc pożre cię bez zmrużenia oka.''')
    print()

def wybierzJaskinię():
    jaskinia = ''
    while jaskinia != '1' and jaskinia != '2':
        print('Do której jaskini chcesz wejść? (1 lub 2)')
        jaskinia = input()

    return jaskinia

def zbadajJaskinię(wybranaJaskinia):
    print('Zbliżasz się do mrocznej jaskini...')
    time.sleep(2)
    print('Wtem! Nagle! Raptem!')
    time.sleep(2)
    print('Pojawia się straszliwy smok... Otwiera swoją paszczę i...')
    print()
    time.sleep(2)

    przyjaznaJaskinia = random.randint(1, 2)

    if wybranaJaskinia == str(przyjaznaJaskinia):
         print('Oddaje ci swój skarb!')
    else:
         print('Mniam, mniam! Pożera cię w całości!')

zagrajPonownie = 'tak'
while zagrajPonownie == 'tak' or zagrajPonownie == 't':
    wyświetlIntro()
    numerJaskini = wybierzJaskinię()
    zbadajJaskinię(numerJaskini)

    print('Chcesz zagrać ponownie? (tak lub nie)')
    zagrajPonownie = input()
