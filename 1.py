def foo(x,y):
    #...
    yield x
    #...
    yield y

print(type(foo))
x = foo(1,2)
print(x.__next__()) #to, chto otdaet yield statement
print(x.__next__())
a = list(foo(1,2))
print(a)

def N(n):
    while True:
        yield n
        n += 1

print(list(zip('abc', N(0))))

#def N2():
    #some gen
    #for x in some_gen:
        #yield x
    #OR
    #yield from N()

def prime():
    yield 1
    a = [2]
    yield 2
    for n in N(3):
        if any(n%y == 0 for y in a):
            continue    
        a.append(n)
        yield n


a = list(zip(prime(),range(100)))
print(a[-1])

def fib():
    yield 1
    yield 1
    a = [1,1]
    while True:
        a.append(a[-1]+a[-2])
        yield a[-1]

b = list(zip(fib(),range(1000)))
print(b[-1])

            
    