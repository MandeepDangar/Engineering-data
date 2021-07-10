X=int(input("Enter number 1 : "))
Y=int(input("Enter number 2 : "))

#Divide and conquer

def karatsuba(X,Y):
    #Base case
    if X<10 or Y<10:
        return X*Y
    m=max(len(str(X)),len(str(Y)))
    if m%2!=0:
        m-=1
    a,b=divmod(X,10**int(m/2))
    c,d=divmod(Y,10**int(m/2))
        
    ac=karatsuba(a,c)
    bd=karatsuba(b,d)
    ad_bc=karatsuba((a+b),(c+d))-ac-bd
    
    return ((ac*(10**m))+((ad_bc)*(10**int(m/2)))+bd) #karatsuba eqn


s=karatsuba(X,Y)
print(s)