# Copyright (c) 2008 Simplistix Ltd
# See license.txt for license details.

def resolve(dotted):
    names = dotted.split('.')
    l_names = len(names)
    current = names[0]
    i = 0
    for name in names:
        i +=1
        try:
            o = __import__(current)
        except ImportError:
            if i==l_names:
                raise
        else:
            break
    for name in names[i:]:
        o = getattr(o,name)
    return o
