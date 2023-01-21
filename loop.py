'''

for m in range(1,12+1):
    for n in range(1,12+1):
        print(f'{m} X {n}= {m*n} ')
    print('-----------------------------------------')
''' 

start=int(input('Emtar Start :'))
end = int(input('Enter End :'))


for m in range(start,end+1):
    for n in range(1,12+1):
        print(f'{m} X {n}= {m*n} ')
    print('-----------------------------------------')
