n=1111
res=''
while n>0:
    rem=n%10
    n=n//10
    res+=str(rem)
print(res)
if res==str(n):
    print(1)
else:
    print(0)