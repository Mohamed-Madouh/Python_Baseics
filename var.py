'''m={'f':[1,2,3],'d':[4,5,6],'g':[7,8]}
for x,y in m.items():
    for i in y :
        print(i)


m={'f':[1,2,3],'d':[4,5,6],'g':[7,8]}
for x in m.values():
    for i in x:
        print(i)
        

x=0
while x< 5 :
    y=0
    while y<3:
        print(y)
        y+=1
    print(x)
    x+=1



for x in range(10):
    if x==6:
        break
    print(x)

mysum = lambda x,y : x+y

print(mysum(2,3))

start=int(input('Enter Frist Number :'))
end=int(input('Enter end Number :'))
print('Nomber\tSquare')
print('-----------------')
for x in range(start,end+1):
    print(x,'\t',x*x)
'''











