sum=0

for x in range(1,1000100000000000000):## tu wybieramy w jakim przedziale szukamy liczb
    for y in range(1,x):
        if x%y==0:
            sum=sum+y
    if(x==sum):
        print(x)
sum=0