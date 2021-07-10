def matrixchainmulti(d,n):
    m=[[0 for i in range(n)] for j in range(n)]
    for i in range(1,n):
        m[i][i]=0
    for D in range(1,n-1):
        for i in range(1,n-D):
            j=i+D
            m[i][j]=100000
            for k in range(i,j):
                q=m[i][k]+m[k+1][j]+d[i-1]*d[k]*d[j]
                if q<m[i][j]:
                    m[i][j]=q
    return m[1][n-1]
                    

d = [5,4,6,2,7]
size = len(d)
m=matrixchainmulti(d,size)
print(m)