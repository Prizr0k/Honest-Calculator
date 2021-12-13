# put your python code here
n1 = float(input())
n2 = float(input())
s = input()
if s == '+':
    print(n1 + n2)
elif s == '-':
    print(n1 - n2)
elif s == '/':
    if n2 != 0:
        print(n1 / n2)
    else:
        print('Division by 0!')
elif s == '*':
    print(n1 * n2)
elif s == 'mod':
    if n2 != 0:
        print(n1 % n2)
    else:
        print('Division by 0!')
elif s == 'pow':
    print(n1 ** n2)
elif s == 'div':
    if n2 != 0:
        print(n1 // n2)
    else:
        print('Division by 0!')
