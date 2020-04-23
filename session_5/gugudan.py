print("실습 2번\n")

def gugudan_even():
    i = 2
    while i < 10:
        for j in range(1,10):
            print("%d * %d = %d" % (i,j,i*j))
        i += 2


def gugudan_odd():
    i = 1
    while i < 10:
        for j in range(1,10):
            print("%d * %d = %d" % (i,j,i*j))
        i += 2

def gugudan_odd_or_even(num1):
    if num1 % 2 == 0:
        gugudan_even()
    else:
        gugudan_odd()

print(gugudan_odd_or_even(3))

print("\n실습 3번\n")

def gugudan_input(num2):
    k=1
    while k <= num2: 
        for l in range(1,10):
            print("%d * %d = %d" % (k,l,k*l))
        k += 1

print(gugudan_input(6))
