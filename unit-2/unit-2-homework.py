'''
def list_intersection(list1, list2):
    intersection = []
    for i in list1:
        for j in list2:
            if i == j:
                intersection.append(i)

    print('intersection is',intersection)

    return list_intersection
    
list_intersection([1,2,3],[3,4,5,1,6])
'''    
    
def item_count(thing,list1):
    num = 0
    for i in list1:
        if i == thing:
           num += 1

    print(f'we found {num} instances of {thing} in {list1}')
    #print(thing)
    #print(list1)
    #print(num)
    
    return
    
#item_count('a',['a','b','c','d','a','s','r','a','m'])   # works
#item_count(2,[34,67,2,9,100])

# better, simpler 
def list_intersection(list1, list2):
   intersection = []
   for i in list1:
       if i in list2:
           intersection.append(i)

   print('intersection is',intersection)

   return list_intersection
  
list_intersection([2,7],[3,4,5,1,6])
