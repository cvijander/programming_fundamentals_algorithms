#using a hashtable to count individual items

#define a set of items that we want to count

items=["apple","pear","orange","banana","apple",
       "orange","apple","pear","banana","orange",
       "apple","kiwi","paer","apple","orange"]

#todo create a hashtable object to hold the imtes and conts
counter= dict()


#todo iterate over each item and increment the count for each one 
for item in items:
    if(item in counter.keys()):
        counter[item] +=1
    else:
        counter[item]=1



#print the result
print(counter)


