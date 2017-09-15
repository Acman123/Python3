def ceasar(phrase,shift): #Ceasar Cipher
    import string
    new = ''
    for i in phrase:
        if i in string.ascii_lowercase:
            new += string.ascii_lowercase[(string.ascii_lowercase.index(i)+2)%len(string.ascii_lowercase)]
        elif i in string.ascii_uppercase:
            new += string.ascii_uppercase[(string.ascii_uppercase.index(i)+2)%len(string.ascii_uppercase)]
        else:
            new += i
    return new

def kwCipher(phrase,kw): #Keyword Cipher
    import string
    alphabet = ''.join([i for i in string.ascii_lowercase if i not in kw])
    key = kw + alphabet
    new = ''
    for i in phrase:
        if i in string.ascii_lowercase:
            new += key[string.ascii_lowercase.index(i)]
        elif i in string.ascii_uppercase:
            new+= key.upper()[string.ascii_uppercase.index(i)]

        else:
            new += i
    return new
