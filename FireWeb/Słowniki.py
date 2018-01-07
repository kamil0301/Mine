#jak i tablica jest zbiorem danych
#tablica - nieuporządkowane
#key:value
#key - int/str/tupla(para danych)
foo = {'Ania': 534}

#print(foo)
foo2 = dict([('Jacek', 640), ('Gustaw',666), ('Ania',534)])
print(foo2)
print(sorted(foo2))

x = foo2.keys()
#print(x)

y = list(x)
print(y)

print(foo['Ania'])

print(foo2['Gustaw'])
del (foo2['Gustaw'])
#print(foo2['Gustaw']) #już nie działą
print(foo2)
print('Ania' in foo2)
print('Gustaw' in foo2)
print('Gustaw' not in foo2)

for i in foo2.keys():
    print(foo2[i])

for k, v in foo2.items():
    print(k,v)

foo3 = dict(Jacek=640, Gustaw=666, Ania=534)
print(foo3)

foo3['Jacek'] = 774
print(foo3['Jacek'])

foo3['Ola'] = 998
print(foo3)

print(foo3.values())