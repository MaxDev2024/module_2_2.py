first = int(input('Первое: '))
second = int(input('Второе: '))
third = int(input('Третье: '))

if (first == second
    and second ==third
    and third == first):
    print('3')
elif (first == second
    or second ==third
    or third == first):
    print('2')
else:
    print('0')