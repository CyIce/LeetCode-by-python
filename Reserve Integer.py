# Reserve Integer

#AC

x=0

ans=0


def resever(num):
    ans=[]
    num=abs(num)

    s=num//10
    y=num%10

    while num!=0:
        y=num%10
        ans.append(y)
        num//=10
    return ans

num=resever(x)

p=pow(10,len(num)-1)

for i in num:
    ans+=(p*i)
    p//=10

if x<0:
    ans*=-1

print(ans)