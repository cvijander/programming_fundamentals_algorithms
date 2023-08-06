# searchin for an item in an ordered list
# this tehnique uses a binary search

items = [6, 8, 19, 20, 23, 41, 49, 53, 56, 87]

def binarysearch(item, itemlist):
    #get the list size
    listsize = len(itemlist) - 1
    #start at two ends of the list
    lowerIdx = 0
    upperIdx = listsize

    while lowerIdx <= upperIdx:
        pass
    #todo calculate the middle point

        midPt = (lowerIdx + upperIdx) //2

    #todo if item is found, return the index
        if itemlist[midPt] == item:
           return midPt
    #todo otherwise get the next midpoint
        if item > itemlist[midPt]:
            lowerIdx = midPt + 1
        else :
           upperIdx = midPt -1

    if lowerIdx > upperIdx:
        return None
    



print(binarysearch(23,items))
print(binarysearch(87,items))
print(binarysearch(250,items))
