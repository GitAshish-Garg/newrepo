#List


li=[1,4,5,6,7,5]                                          #here we declare a list name li with some elements
print(li)
lis=[1,5,9,8]

print(li[2])                                                        #if we want to access the elements of list then we use a index to access

li[4]=8                                                  #here i am include a new element on index 4 and assign in variable d

print("list after modified",li)

#import copy from copy
#g=li.copy(lis)                                             #if we want to copy a list(li) into another list(lis) then we use copy function before use we want
                                                                #   import copy statement from copy

g=li.pop(1)                                                 #here i am use pop function for delete a index of element and we use delete element in another variable                                                                
print(g)                                                           #if we not give any value then it pop from last
print("list after pop" ,li)

print(li.remove(5))                                               #in remove function we use element value to delete a element from list
print("list after remove",li)

del (li[2] )                                              #here we use delete command to delete element from list using  index value
print("list after deleete",li)

#list can be traversed

print("list is traversed here")
for x in li:
    print(x )
    print("\n")


print(li*2)                                               #this is used to repetation a list

print(max(li))                                                   #this is used to know the maximum value present in list

print(min(li))                                            #this is used to know to know the minimum valve present in the list

print(len(li))                                                     #this is used to know the length of the list
print("after max,min ,length of list")
print("list is ",li)
li.insert(2,8)
print(li)

print(li.index(8))                                         #this is used to know the index of the element present in the list

#it has no find function to find index of list elment

li.insert(3,5)                                       #insert is used to another way to insert the element in the list in first we give index and given value
print("list after modified and insert function ",li)

li.count(5)                                                   #count is used to know the element how many times it come or repeate
print("list after count",li)

li.sort()                                               #sort is used to sorting or arranging inassendiinig and descinding order
print("list after the sorting",li)

li.append(4)                                                   #append function is used to add element in last index of list
print("list after the append",li)

print(4 in li)                                          #it is used to know this is the element of list or not
print(4 not in li)

tup=(1,'d',4,4.5,'g')                                         #here i am declaring a tuple in tup variable
print(tup)                                                         #print(tuple)
print(list(tup))                                        #list(tuple name);this function is used to convert a list into tuple


print("here we contatenate a list")
print("li",li)
print("lis =",lis)
print(li+lis)                                                  #if we want to add two list and store in one list then we use (+) for this

li.extend(lis)                                                      #it also perform same operation it is used to join the listand another listand give output in list
print"list after the extend",li

print("li",li)
print("lis",lis)

print(cmp (li,lis))                                               #it is used to compare a two list it compare lis with li if lis have less element then it give -1
print(cmp(lis,li))                                                 #if li have more value then funtion give +1 value means second compare first

print("Thank you")

