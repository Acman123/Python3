def insertionSort(array):
  for i in range(1,len(array)):
    for j in range(0,i):
      if array[i] <= array[j]:
        temp = array[i]
        del array[i]
        array.insert(j,temp)
  return array
