def betterIndex(list1,val):
    locs = []
    for i in range(len(list1)):
        if list1[i] == val:
            locs.append(i)
    return locs
