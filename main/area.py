def area(length, width=''):
    try:
        if width == '':
            width = length
        length = int(length)
        width = int(width)
    except:
        print("Must supply integers")
        raise ValueError
    if (length < 0) or (width < 0):
        print("length must not be negative")
        raise ValueError
    return length * width
