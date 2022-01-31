def bezout(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcdVal, x, y = bezout(b % a, a)
        return gcdVal, y - (b // a) * x, x 

def totient(a):
    count =0
    for index in range(1,a):
        if isCoprime(index, a):
            count+=1
    return count

def isCoprime(a,b):
    return gcd(a,b, False) ==1
    
# Printmode = False silences working out
def gcd(a,b, printmode):
    quot, mod = divmod(a,b)
    if printmode:
        print(f'{a} = {quot} * {b} r-{mod}')
    while mod:
        a=b
        b=mod
        x = a
        quot, mod = divmod(a,b)
        if printmode:
            print(f'{a} = {quot} * {b} r-{mod}')
    return b

if __name__ == '__main__':
    inp = str(input("G\tGCD\nC\tCoprime\nT\tEuler's Totient\nB\tBezout Coefficients\n~ ")).lower()
    if inp == 'g':
        a = int(input("What's the first number? "))
        b = int(input("What's the second number? ")) 
        print(f'GCD is {gcd(a,b, True)}')
    if inp == 'c':
        a = int(input("What's the first number? "))
        b = int(input("What's the second number? ")) 
        if isCoprime(a,b):
            print(f'{a} and {b} are coprime')
        else:
            print(f'{a} and {b} are not coprime')
    if inp == 't':
        a = int(input("What's the number? "))
        print(f'The totient of {a} is {totient(a)}')
    if inp == 'b':
        a = int(input("What's the first number? "))
        b = int(input("What's the second number? "))
        gcdVal, x, y = bezout(a,b) 
        print(f'gcd({a},{b})\n\t= {gcdVal}\n\t= {a}*{x} + {b}*{y}')