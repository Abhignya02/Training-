s="PAYPALISHIRING"
numRows=3

def rec_fun(s,i,l):
    print(i,l)
    if i>=len(s):
        return ""
    print(s[i])
    k=0
    if l[0]==0:
        k=1
    return s[i]+rec_fun(s,i+l[k],l[::-1])
res=""
l=[(2*(numRows-1)),0]
for i in range(numRows):
    res+=rec_fun(s,i,l)
    l[0]-=2
    l[1]+=2
    print(l)
print(res)
#return res