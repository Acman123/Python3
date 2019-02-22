def cast(value,dataType):
    if not dataType in ['int','str','list','chr','ord']:
        print('Invalid data type to cast to, please select from:')
        for i in ['int','str','list','chr','ord']:
            print(i)
        dType = input("Please enter a new data type.\n")
        return cast(value,dType)
    try:
        x = eval(dataType + '(' + str(value) + ')')
    except:
        print("Unable to perform cast.")
        return -1
    return x


def printClass(class1):
    for obj in gc.get_objects():
        if isinstance(obj, class1):
            print(obj)
            print(obj.__dict__)

            
def positions(n):
    a = str(n)[-1]
    if a == "1":
        return n + 'st'
    elif a == "2":
        return n + 'nd'
    elif a == "3":
        return n + 'rd'
    else:
        return n + 'th'

def comma(n): #Inserts commas into a number, i.e. 1000000 --> 1,000,000
    temp = list(str(n))
    for i in range(len(temp),0,-3):
        temp.insert(i,',')
    return ''.join(temp[:-1])

def uniqueValues(arr):
    unique = []
    for item in arr:
        if item not in unique:
            unique.append(item)

    return unique
