import time
import string
import random

def betterIndex(list1,val):
    locs = []
    for i in range(len(list1)):
        if list1[i] == val:
            locs.append(i)
    return locs

def encrypt(phrase, const=0):
    highAlpha = list(string.ascii_uppercase)
    lowAlpha = list(string.ascii_lowercase)
    punctuation = list(string.punctuation)
    digits = []
    for i in range(len(punctuation)):
        digits.append(string.digits[i%len(string.digits)])

    lists1 = [highAlpha,lowAlpha]
    lists2 = [punctuation,digits]
    lists3 = []
    lists3.extend(lists1)
    lists3.extend(lists2)
    newPhrase = ""
    checkSums = []
    polarities = []
    polarities2 = []
    plusMinuses = []

    for j in range(len(phrase)):
        timeVar = time.time() + random.randint(0,1000)/1000
        while time.time() < timeVar:
            pass
        print('{}..'.format(len(phrase)-j))
    
        num = str(time.time())[-4:]
        checkSum = sum([int(i) for i in num])
        checkSums.append(checkSum)
        checkSum += const
        plusMinus = random.randint(0,1)
        plusMinuses.append(plusMinus)

        if any(phrase[j] in lists for lists in lists1):
            swapPolarity = random.randint(0,1)
            polarities.append(swapPolarity)

        elif phrase[j] in punctuation:
            swapPolarity2 = random.randint(0,1)
            if swapPolarity2 == 1:
                polarities2.append(punctuation.index(phrase[j])+1)
            else:
                polarities2.append(0)

        elif phrase[j] in digits:
            swapPolarity2 = random.randint(0,1)
            if swapPolarity2 == 1:
                polarities2.append(betterIndex(digits,phrase[j])[0]+1)
            else:
                polarities2.append(0)
    
        if phrase[j] in highAlpha:
            index = (highAlpha.index(phrase[j])+pow(-1,plusMinus)*checkSum)
            if not -26 <= index <= 25:
                index = index%26
            newPhrase += lists1[swapPolarity][index]
            
        elif phrase[j] in lowAlpha:
            index = (lowAlpha.index(phrase[j])+pow(-1,plusMinus)*checkSum)
            if not -26 <= index <= 25:
                index = index%26
            newPhrase += lists1[(1+swapPolarity)%2][index]
            
        elif phrase[j] in punctuation:
            index = (punctuation.index(phrase[j])+pow(-1,plusMinus)*checkSum)
            if not -32 <= index <= 31:
                index = index%32
                
            newPhrase += lists2[swapPolarity2][index]
        elif phrase[j] in digits:
            index = (digits.index(phrase[j])+pow(-1,plusMinus)*checkSum)
            if not -32 <= index <= 31:
                index = index%32
            newPhrase += lists2[(1+swapPolarity2)%2][index]
            
        else:
            newPhrase += phrase[j]
    
    print()

    noRandomLetters = random.randint(0,int(len(phrase)/5)) 

    if len(phrase) < 5:
        noRandomLetters = random.randint(0,1)

    newLetters = []
    newPhrase = list(newPhrase)
    for j in range(noRandomLetters):
        print('{}..'.format(noRandomLetters-j))
        letterType = random.randint(0,3)
        letter = random.randint(0,len(lists3[letterType])-1)
        letterIndex = random.randint(j*int(len(phrase)/noRandomLetters),(j+1)*int(len(phrase)/noRandomLetters)-1)
        newPhrase.insert(letterIndex,lists3[letterType][letter])
        newLetters.append(letterIndex)

    newPhrase = ''.join(newPhrase)
    return [newPhrase, checkSums, plusMinuses, polarities, polarities2, newLetters]


def decrypt(phrase, sums, plus, pol1,pol2, letters, const=0):
    highAlpha = list(string.ascii_uppercase)
    lowAlpha = list(string.ascii_lowercase)
    punctuation = list(string.punctuation)
    digits = []
    for i in range(len(punctuation)):
        digits.append(string.digits[i%len(string.digits)])
                      
    lists1 = [highAlpha,lowAlpha]
    lists2 = [punctuation,digits]
    lists3 = []
    lists3.extend(lists1)
    lists3.extend(lists2)
    newPhrase = ""
    checkSums = []
    polarities = []
    polarities2 = []
    plusMinuses = []

    for i in range(len(sums)):
        sums[i] += const

    newPhrase = list(phrase)
    for i in reversed(letters):
        del newPhrase[i]

    x = 0

    for i in range(len(newPhrase)):
        if newPhrase[i] in lowAlpha:
            if pol1[x] == 1:
                newPhrase[i] = newPhrase[i].upper()

        elif newPhrase[i] in highAlpha:
            if pol1[x] == 1:
                newPhrase[i] = newPhrase[i].lower()
            
        else:
            continue

        x += 1

    for i in range(len(newPhrase)):
        if newPhrase[i] in lowAlpha:
            index = (lowAlpha.index(newPhrase[i])+pow(-1,plus[i]+1)*sums[i])
            if not -26 <= index <= 25:
                index = index%26
            newPhrase[i] = lowAlpha[index]
            
        elif newPhrase[i] in highAlpha:
            index = (highAlpha.index(newPhrase[i])+pow(-1,plus[i]+1)*sums[i])
            if not -26 <= index <= 25:
                index = index%26
            newPhrase[i] = highAlpha[index]
            
        elif newPhrase[i] in punctuation:
            index = (punctuation.index(newPhrase[i])+pow(-1,plus[i]+1)*sums[i])
            if not -32 <= index <= 31:
                index = index%32
            newPhrase[i] = punctuation[index]
            
        elif newPhrase[i] in digits:
            index = (digits.index(newPhrase[i])+pow(-1,plus[i]+1)*(sums[i]+2))
            if not -32 <= index <= 31:
                index = index%32
            newPhrase[i] = digits[index]
            
        else:
            continue

    y = 0

    for i in range(len(newPhrase)):
        if newPhrase[i] in punctuation:
            if pol2[y] != 0:
                newPhrase[i] = digits[pol2[y]-1]

        elif newPhrase[i] in digits:
            if pol2[y] != 0:
                newPhrase[i] = punctuation[pol2[y]-1]

        else:
            continue
        y += 1
    
    newPhrase = ''.join(newPhrase)  
    return newPhrase
    
    
def main():
    inputPhrase = input("Please enter the word or phrase you wish to encrypt.\n")
    encryption = encrypt(inputPhrase)

    phrase, sums, plus, pol1, pol2, letters = encryption

    #"""
    [print(i) for i in encryption]
    print()
    #"""
    
    decryption = decrypt(phrase, sums, plus, pol1, pol2, letters)
    print(decryption)

main()
