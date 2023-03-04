dict = {"Rashi" : 234534, "Shail" : 34567 , "Anvay": 654787, "Nysa":9876543}
print("Phone number and names are: ")
count = 0
for i,j in dict.items():
    count = count+1
    print(count, i, "=" , j)
