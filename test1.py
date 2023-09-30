a = int(input('Enter a number :- '))
b = str(input('Enter a number :- '))
if b > a:
    print(b , ' is greater than ', a , '.')
elif b < a:
    print(a , ' is greater than ', b , '.')
elif b == a:
    print(a , ' is equal to ', b , '.')
else:
    print("These values can't be compared as one is string and the other an integer.")