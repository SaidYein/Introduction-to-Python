def pow(x,y):
    if y > 0:
        return x * pow(x, y-1)
    else:
        return 1

