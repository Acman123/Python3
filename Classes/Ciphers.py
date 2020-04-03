import string

class Shift:
    def __init__(self, key):
        self.key = key
        self.alpha = string.ascii_uppercase

    def encrypt(self, word):
        w = word.upper().strip()
        chars = list(w)
        charsNum = [self.alpha.index(chars[i]) for i in range(len(w))]
        newNum = [(charsNum[i] + self.key) % 26 for i in range(len(w))]
        newChars = [self.alpha[i] for i in newNum]
        newWord = ''.join(newChars)
        return newWord

    def decrypt(self, word):
        w = word.upper().strip()
        chars = list(w)
        charsNum = [self.alpha.index(chars[i]) for i in range(len(w))]
        newNum = [(charsNum[i] - self.key) % 26 for i in range(len(w))]
        newChars = [self.alpha[i] for i in newNum]
        newWord = ''.join(newChars)
        return newWord
    

class keyWord(self, key):
    def __init__:
        self.key = key.upper().strip()
        self.alpha = string.ascii_uppercase

    def encrypt(self,word)
        w = word.upper().strip()
        chars = list(w)
        transChars = list(key)
        for i in range(26 - len(key)):
            skip = 0
            if not self.alpha[i + skip] not in transChars:
                skip += 1
            transChars.append(self.alpha[i + skip])
        charsNum = [self.alpha.index(chars[i]) for i in range(len(w))]
        newChars = [transChars[i] for i in charsNum]
        newWord = ''.join(newChars)
        return newWord

    def decrypt(self,word)
        w = word.upper().strip()
        chars = list(w)
        transChars = list(key)
        for i in range(26 - len(key)):
            skip = 0
            if not self.alpha[i + skip] not in transChars:
                skip += 1
            transChars.append(self.alpha[i + skip])
        charsNum = [transChars.index(chars[i]) for i in range(len(w))]
        newChars = [self.alpha[i] for i in charsNum]
        newWord = ''.join(newChars)
        return newWord


class Vigenere:
    def __init__(self, key):
        self.key = key.upper().strip()
        self.alpha = string.ascii_uppercase

    def encrypt(self, word):
        w = word.upper().strip()
        chars = list(w)
        shiftChars = [self.key[i % len(self.key)] for i in range(len(w))]
        charsNum = [self.alpha.index(chars[i]) for i in range(len(w))]
        shiftNum = [self.alpha.index(shiftChars[i]) for i in range(len(w))]
        newNum = [(charsNum[i] + shiftNum[i]) % 26 for i in range(len(w))]
        newChars = [self.alpha[i] for i in newNum]
        newWord = ''.join(newChars)
        return newWord

    def decrypt(self, word):
        w = word.upper().strip()
        chars = list(w)
        shiftChars = [self.key[i % len(self.key)] for i in range(len(w))]
        charsNum = [self.alpha.index(chars[i]) for i in range(len(w))]
        shiftNum = [self.alpha.index(shiftChars[i]) for i in range(len(w))]
        newNum = [(charsNum[i] - shiftNum[i]) % 26 for i in range(len(w))]
        newChars = [self.alpha[i] for i in newNum]
        newWord = ''.join(newChars)
        return newWord
