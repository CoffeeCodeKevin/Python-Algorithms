def cookie(x):
    name = 'Zach' if (type(x) is str) else ('Monica' if (type(x) is float or type(x) is int) else 'the dog')
    return 'Who ate the last cookie? It was %s!' % name
