# TUTAJ JEST ROZWIĄZANIE ZADANIA
suma = 1
n = 1
liczby_doskonale = []
dot = 10
ile = 1
b = 3  # nasza liczba nieparzysta po której sprawdzamy
a = 0  # gdy a = 0 to liczba suma jest l. pierwszą, jeśli a=1 to suma nie jest l.pierwszą
while True:
    suma += 2 ** n
    if suma > dot:  # to jest pętla, która nam pokazuje rząd wielkości sprawdzanej liczby,
        print("10^", ile)  # gdy sprawdzana liczba jest większa od aktualnie wyświetlonego rzędu wielkości,
        dot *= 10  # pętla działa i zwiększa rząd o jedną potęgę więcej.
        ile += 1
    while True:

        if suma != 2:  # gdy suma =/= 2, zadziała funkcja:
            if (suma % 2) == 0:  # sprawdza czy podzielne przez 2
                a = 1
            else:
                while b <= (suma / 2):  # sprawdza czy podzielne przez kolejne liczby nieparzyste aż do połowy sprawdzanej
                    if suma % b == 0:
                        a = 1
                    b += 2  # zwiększenie nieparzystej o dwa
        if a == 1:  # gdy suma nie jest l pierwszą pętla sprawdzania
            break
        else:
            liczby_doskonale.append(suma * (2 ** n))  # dodanie nowej liczby doskonałej do tablicy liczb doskonalych
            print(liczby_doskonale)  # nie mów mi że tutaj też potrzebujesz wyjaśnienia na tym poziomie
            break
    n += 1

# W RAZIE POTRZEBY JAKICHKOLWIEK DODATKOWYCH WYJAŚNIEŃ PISAĆ DO JACKA SUDERA.