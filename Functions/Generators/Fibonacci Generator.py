def fibGen():
    a = 0
    b = 1
    while True:
        c = a + b
        a, b = b, c
        yield c
