path = ['A','B','C','D','E','F','G','H','I','J','K','L']
path1 = []
def iteratePath():
    x = len(path)
    print x
    if x > 1:
        print path[x-1]
        path.pop(x-1)
        x -= 1
        iteratePath()
    elif x == 1:
        endpos = path[0]
        print endpos
    

iteratePath()
