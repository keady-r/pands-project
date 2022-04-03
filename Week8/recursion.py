#def reverse(str):
 #if str == " " or len(str)==1:
  #return str
 #else:
  #return reverse (str[1:]) + "|" + str [0]

#print(reverse("dominic"))
#print(reverse("GMIT"))
#print(reverse("recursion is hard"))

#def merge(string, string2):
 #if string2 == "":
    #return string 
 #else:
     #return (string[0:]) + (string2[:])
 

#print(merge("dmnc", "oii"))

def merge(string, string2):
 if len(string < string2):
    return string 
 else:
    return merge(string[0] + string2 [0])

print(merge("dmnc", "oii"))
print(merge ("What is Love", "LOL"))

#def substrings(string):
    #if string == '' or len(string) ==1:
        #return string 
    #else:
       # return substrings(string [0:3])

#print(substrings("We are in isolation"))