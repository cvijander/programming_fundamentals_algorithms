# implement a quicksort

items = [20,6,8,53,56,23,87,41,49,19]


def quicksort(dataset,first, last):
    if first < last:
       #calculate the split point
       pivotIdx = partition(dataset,first,last)


       # now sort the two partitions

       quicksort(dataset, first, pivotIdx-1)
       quicksort(dataset,pivotIdx+1, last)


def partition(datavalues, first, last):
    # choose the first item as the pivot value
    pivotvalue = datavalues[first]
    #establish the upper and lower indexes

    lower = first +1
    upper = last
    
    # start searcing for the crossing point
    done = False
    while not done:
        #todo advance the lower index 

         while lower < upper and datavalues[lower]<= pivotvalue:
             lower +=1

        #todo advance the upper index 
         while datavalues[upper]>= pivotvalue and upper >= lower:
          upper =-1

        #todo if the two indexes cross, we have found the split point
          if upper < lower:
              done =True
          else:
              temp =datavalues[lower]
              datavalues[lower] =datavalues[upper]
              datavalues[upper]= temp

    # when the split point is found ,excange the pivot value

    temp = datavalues[first]
    datavalues[first] =datavalues[upper]
    datavalues[upper] = temp


    # return the split point index 
    return upper

# test the merge sprt with data

print(items)
quicksort(items, 0, len(items)-1)
print(items)

          