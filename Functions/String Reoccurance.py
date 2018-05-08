#Requires "Find Substring.py"

def reoccurance(string,length,n=1):
  seen = []
  count = []
  for i in range(len(string)):
    
    try:
      currentSub = string[i:i+length]
    except IndexError:
      break
    
    currentVal = None
    
    try:
      currentVal = count[findSubStr(string,currentSub)]
    except IndexError:
      pass
    
    newStr = currentSub not in seen
    
    if newStr:
      seen.append(currentSub)
      count.append(1)
    
    elif currentVal == n:
      return currentSub
  
    else:
      count[findSubStr(string,currentSub)] += 1
  
  return None
