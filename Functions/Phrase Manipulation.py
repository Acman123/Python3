def phraseWaveForm(phrase,n):
    [[print(phrase[:j]) if j <= len(phrase) else print(phrase[:2*len(phrase)-j]) for j in range(1,2*len(phrase)-1)] for i in range(n)]
    print(phrase[0])

def reorderPhrase(phrase, caps=False):
    if caps == True:
        phrase = phrase.upper()
    for i in range(len(phrase),0,-1):
        tempPhrase = phrase[i:] + phrase[:i]
        [print(tempPhrase[j],end=" ") for j in range(len(phrase))]
        print()


