class list2D():
  def __init__(self,container,*lists):
    self.container = container
    self.container.extend(lists)
  
  def pPrint(self):
    containerStr = str(self.container)
    minPoint = 0
    maxPoint = 0
    for i in range(len(containerStr)):
      try:
        if containerStr[i] == ']' and containerStr[i+1] == ',':
          maxPoint = i+2
          print(containerStr[minPoint:maxPoint])
          minPoint = i+2
      except IndexError:
        print(containerStr[minPoint:])
        
        
  def sort(self):
    firstItems = {}
    for i in range(len(self.container)):
      self.container.insert(i+1,sorted(self.container[i]))
      del(self.container[i])
      firstItems.update({i:self.container[i][0]})
      
    firstItems = [(k, firstItems[k]) for k in sorted(firstItems, key=firstItems.get, reverse=False)]
    tempContainer = []
    for i in firstItems:
      tempContainer.append(self.container[i[0]])
    self.container = tempContainer
    

