WARUNKI
składnia:
if x == 2:
    print('foo')
/wydrukuj 'foo' gdy x ma wartość 2/
operatory:
== - równe
!= - różne
< - mniejsze
> - większe
<= - mniejsze równe
>= - większe równe
PĘTLA while
i = 0
while i < 3:
    print(i)
    i += 1
/wydrukuj wartość i gdy i jest mniejsze od 3
i zwiększa się o 1 po każdym przejściu pętli, więc wydrukowane będzie:
0
1
2
komputer wraca za każdym przejściem na początek pętli dopóki warunek po while zwraca wartość True/
PĘTLA for
list = ['a', 'b', 'c']
for i in list:
    print(i)
/dla każdego przejścia pętli i przyjmuje kolejne wartości z tablicy list
wydrukuje się:
'a'
'b'
'c'
pętla kończy się gdy osiągnięty zostanie koniec tablicy/
for i in range(3):
    print(i)
/funkcja range zwraca trzyelementową tablicę [0, 1, 2]
wydrukuje się:
0
1
2
range(1, 10, 3) zwróci tablicę o pierwszym elemencie 1, ostatnim mniejszym niż 10 i kroku 3, czyli [1, 4, 7]/
BREAK
i = 0
while i < 10:
    if i == 8:
        break
    print(i)
    i += 1
/pętla jest wykonywana normalnie dopóki nie spełni się warunek
wtedy komputer opuszcza pętlę i idzie dalej z kodem/
CONTINUE
for i in range(10):
    if i == 8:
        continue
    print(i)
/pętla jest wykonywana normalnie dopóki nie spełni się warunek
wtedy komputer pomija jedno "okrążenie" pętli i kontynuuje ją dla następnego i/
Let's code!