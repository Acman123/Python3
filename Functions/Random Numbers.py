def randomInt(len,base):
  import random
  import string
  digits = [str(i) for i in list(range(0, 10))]
  digits.extend(list(string.ascii_uppercase))
  digits.extend(list(string.ascii_lowercase))
  digits.extend(['+', '/'])
  return eval(str('str(digits[random.randint(0,{})])+'.format(base-2)*len)[:-1])
