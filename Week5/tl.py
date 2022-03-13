
list = [1,2,3,4,5]

print (len(list))
print (list[1:3])
print(list [1:])
print (list [:3])
print (list [::2])
print (list [::-1])

sum = 0 

for x in list:
    sum += x 
    print (sum)

for i in range (0,len(list)):
    print ("value of index", i, "is", list[i])

t = (1,2,3)
x, y, z =t

print (y)