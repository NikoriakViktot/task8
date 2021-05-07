

    # Task1
def oops():
    raise KeyError
def doomed():
    try:
       oops()
    except IndexError:
        print('caught an  index    error!')
    else:
        print('no    error    caught.')




