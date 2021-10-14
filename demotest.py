def calc(x,y):
    try:
        return x/y
    except Exception as e:
        return e


print(calc(6,0))