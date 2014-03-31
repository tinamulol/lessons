#f = open('','w')
#f.write(...)
#with open('...', 'w') as f:
    #f.write()

#class X:
    #def __open__(self):
        #pass
    #def __close__(self, exc_cl, st_tr, exc_iwg): #sys.exc_info()
        #pass
from contextlib import contextmanager
@contextmanager
def foo():
    print('Before')
    yield
    print('After')
with foo() as x:
    print('Inside')
    print('x is', x)

@contextmanager
def bar():
    try:
        yield
    except ValueError:
        print('12')
    finally:
        pass
    
@contextmanager
def acc():
    lst = []
    yield lst
    for x in lst:
        print(x)
with acc() as a:
    a.append(1)
    a.append(2)
    a.append('the room full of people who...')
    
