def baseConvert(num, base1, base2):
    import math
    import string

    accepted = True
    base10Nums = []
    baseStr = ""

    digits = [str(i) for i in list(range(0, 10))]
    digits.extend(list(string.ascii_uppercase))
    digits.extend(list(string.ascii_lowercase))
    digits.extend(['+', '/'])

    if any(num not in digits for num in list(str(num))):
        numRedo = input(
            'Unsupported characters in inputted number. The allowed characters are:\n' + str(digits).replace('\'','').replace(
                '[', '').replace(']', '') + '\nPlease enter a new number.\n')
        accepted = False

    if any(x > 64 and x < 2 for x in [base1,base2]):
        base1Redo, base2Redo = input(
            'Base(s) inputted invalid, the largest accepted base is base 64, and the smallest is base 2. Please input your two bases again, space separated. ({Base1} {Base2})\n').split()
        accepted = False

    if not accepted:
        baseConvert(numRedo, base1Redo, base2Redo)

    for i in range(len(str(num))):
        base10Nums.append((base1 ** (len(str(num)) - (i + 1))) * digits.index(str(num)[i]))

    newNum = sum(base10Nums)

    if base2 == 10:
        return newNum

    a = math.floor(math.log(newNum, base2))

    for i in range(a, -1, -1):

        if newNum // base2 ** i <= base2 - 1:
            baseStr += str(newNum // base2 ** i)
            newNum -= (newNum // base2 ** i) * (base2 ** i)

        else:
            baseStr += "0"

    return baseStr
