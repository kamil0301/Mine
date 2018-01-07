x = -3
print(x == 3)
if x >= 0:
    print("x jest dodatni")
y = 0
if x > 0 and y == 0:
    print("x>0 i y=0")
elif x == 3:
    print("x = 3")
else:
    print("coś spartoliłeś")

i = 0
while i < 5:
    print("mniej niż 5")
    print(i)
    i += 1
    #print(i)

list = [0, 4, 123, 7, 432, 24, 2235, 987, 54, 43]
archive = []
for i in list:
    print(i,"_",list.index(i))

for e in range(7):
    print(e,list[e])
    if e >= 3:
        break

for i in range(2,101,2):
    print(i)
i=0
pierwsze=[]
for i in range(2,101):
    for dz in range(2,i):
        if i % dz == 0:
            pierwsze.append(i)
    if pierwsze.count(i) == 0:
        print(i)




