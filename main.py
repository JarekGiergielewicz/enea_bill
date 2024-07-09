from kalkulator_zuzycia import CalcuEnea

def init_setup():
    wynik = CalcuEnea()
    kw = ''
    while True:
        wynik.data = []
        do = input('Podaj datę odzytu: ')
        # zs = input('podaj zuzycie szczytowe: ')
        # zps = input('podaj zuzycie pozaszczytowe: ')
        if do.lower() == 'q':
            break
        else:
            zs = input('podaj zuzycie szczytowe: ')
            zps = input('podaj zuzycie pozaszczytowe: ')
            wynik.data_kw(int(zs))

            wynik.data_kw(int(zps))
            wynik.base_kw(do)
            print(wynik.base)

    print(wynik.data_cal())
    sd = input('podaj za jaki rok: ')
    wynik.save_data(sd)


init_setup()