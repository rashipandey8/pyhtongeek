#Even and odd numbers in list

l = list()
print(type(l))
l = [10,22,4,5,8,9,23,0,89]
for i in l:
    if i%2 == 0:
       print("Number in list is even")
    else:
        print("Number in list is odd")
l.append(2) #Adding new item ot the list
print(l)
l.pop(1)
print(l) #Removing item at specified index
l.remove(9) # removing specified item from the list
print(l)
l.copy()
print(l)