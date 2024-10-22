a = int(input('papa: '))
b = int(input('mama: '))
c = input('vvedite: ')
match c:
    case '+':
        print(a+b)
    case '*':
        print(a*b)
    case '-':
        print(a-b)
    case '/':
        if b== 0:
            print('oshibka')
        else:
            print(a / b)
    case _:
        print('error')





# if c =='+':
#     print(a + b)
# elif c =='*':
#     print(a * b)
# elif c=='-':
#     print(a - b)
# elif c=='/':
#     if b== 0:
#         print('oshibka')
#     else:
#         print(a / b)
# else:
#     print('Error')

