# implement a merge sort with recursion


items = [6,20,8,19,56,23,87,41,59,49,53]


def mergesort(dataset):
    if len(dataset)>1:
       mid = len(dataset) //2
       leftarr =dataset[:mid]
       rigtharr = dataset[mid:]


     # todo recursively break down the arrays    
       mergesort(leftarr)
       mergesort(rigtharr)



     #todo now perform the merging

    i =0   # index int the left array
    j = 0  # index into the rigth array
    k = 0  # index int merged array

    #todo while both arrays have content

    while i <len (leftarr) and j < len(rigtharr):
        if leftarr[i]<rigtharr[j]:
            dataset[k] = leftarr[i]
            i +=1
        else:
           dataset[k] = rigtharr[j]
           j +=1
        k +=1  

    #todo if the left array  still has values, add them

    while i <len(leftarr):
        dataset[k] =leftarr[i]
        i +=1
        k +=1


     #todo if the right array still has values, add them

        while j< len(rigtharr):
         dataset[k] = rigtharr[j]
         j +=1
         k +=1   
        

       # test the merge sort with data
       # 
       # 
    print(items)
    mergesort(items)
    print(items)
      