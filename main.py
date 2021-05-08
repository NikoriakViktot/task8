
# Task1

def oops():
    raise IndexError


def doomed():
    try:
        oops()
    except IndexError:
        print('caught an index error!')
    else:
        print('no error caught...')


if __name__ == '__main__':
    doomed()


# Task2
def c (c: int):
for True:
    try:
        a = int(input('Enter a:'))
        b = int(input('Enter b:'))
        c = a**2/b
        #print("a**2/b = %d" % c)
        
    except ValueError:
        print('No valid integer! Please try again ...')
    except Exception:
        print("can't divide by zero")
        print(Exception)
    else:
        print('Hi I am else block')
exit(0)        
print(c)
