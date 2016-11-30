#BinaryWatch

n=int(input())

#分别代表上下两种LED灯亮的个数；
arr1=[]
arr2=[]

#储存分钟数；
minute=[]
#储存答案；
ans=[]
#将输入的数字进行拆分；
for i in range(n+1):
    if i<=4 and n-i<=6:
        arr1.append(i)
        arr2.append(n-i)

def one(num):
    ans=0
    while num!=0:
        if num%2==1:
            ans+=1
        num//=2

    return ans


for i in range(len(arr1)):
    for j in range(arr2[i],60):
        if one(j)==arr2[i]:

            if j<10:
                j="0"+str(j)
            else:
                j=str(j)
            minute.append(j)

    for k in range(arr1[i],12):
        if one(k)==arr1[i]:
            for l in range(0,len(minute)):
                ans.append(str(k)+":"+minute[l])
    del minute[:]


print(ans)

