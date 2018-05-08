def findSubStr(string,sub):
  for i in range(len(string)):
    try:
      condition = eval('string[i:i+len(sub)] == sub')
    except IndexError:
      break
    
    if condition:
      return i
  return None
