def sum(a,b):
    result = a + b
    print('+++++++++++++++++++++++')
    print("The sum is:-", result)
    print('+++++++++++++++++++++++')
def sub(a,b):
    diff = a - b
    print('+++++++++++++++++++++++')
    print("The diff is:-", diff)
    print('+++++++++++++++++++++++')
def mul(a,b):
    mul = a*b
    print('+++++++++++++++++++++++')
    print("The multiplication is:-", mul)
    print('+++++++++++++++++++++++')
def div(a,b):
    div = a/b
    print('+++++++++++++++++++++++')
    print("The division is:-", div)
    print('+++++++++++++++++++++++')
print('++++++++++++++CALCULATOR++++++++++++')
a = int(input ("Enter 1st intiger:-"))
print("You have entered:- ", a)
b = int(input ("Enter 2nd intiger:-"))
print("2nd intiger is:- ", b)
choice = int(input ("For Addition press 1, subtraction press 2, multiplication press 3, division press 4"))

if (choice == 1):
    sum(a,b)
elif (choice == 2):
    sub(a,b)
elif (choice == 3):
    mul(a,b)
else:
    div(a,b)

