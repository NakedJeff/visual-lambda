

# Some common functions


def toInt( x ):
    return int( round( x ) )




def mix( k, a, b ):
    return a*(1-k) + b*k



def first( generator ):
    "Get first value of generator  or  None"
    for value in generator:
        return value
    return None


def last( generator ):
    "Get last value of generator  or  None"
    last = None
    for value in generator:
        last = value
    return last




