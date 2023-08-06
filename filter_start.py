#use a hashtable to fileter out duplicate items

#define a set of items that we want to reduce duplicates

items=["apple","pear","orange","banana","apple",
       "orange","apple","pear","banana","orange",
       "apple","kiwi","paer","apple","orange"]


#todo  create a hastable to perfrom a filter 

filter = dict()

#todo loop over each item and add to the hashtable 

for key in items:
    filter[key] = 0


#todo create a set from the resulting keys in the hashtable 
result = set(filter.keys())
print(result)

