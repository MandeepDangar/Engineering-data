text = "Python"
pattern='th'

X=len(text)
Y=len(pattern)
d=256  #positional base

#sum for pattern
sumP=0
for i in range(Y):
    sumP=sumP+(ord(pattern[i])*(d**(Y-i-1)))
print(sumP)

#sum of text
sumT=0
flag=0
for i in range(Y):
    sumT=sumT+(ord(text[i])*(d**(Y-i-1)))
if sumP==sumT:
    print("Pattern is present in the text at",Y)
    flag=1

#Rolling hash function
for i in range(Y,X):
    sumT=(sumT-(ord(text[i-Y])*(d**(Y-1))))*d+ord(text[i])
    if(sumP==sumT):
        print("Pattern is present in the text at",Y-i+1)
        flag=1
        
if flag==0:
    print("Pattern is not present in the text")
    