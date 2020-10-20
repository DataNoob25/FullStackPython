def fib(n):
        a, b=0, 1
        i=0

        while i<n:
            a, b = b, a+b
            i+=1
        return a
        

print(fib(2))

def funcion1(a=2,b=5):
    return a+b

print(funcion1(2))