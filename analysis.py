
file = 'Book.txt'

with open(file,'r') as f:
    for line in f:
        print (line[:-1])



