def power(x,n):
    if n==0:
        return 1
    flag=power(x,int(n/2))
    if(int(n%2)==0):
        return (flag*flag)
    else:
        return (x*flag*flag)
    
x = 5
n = 5
print(power(x,n))