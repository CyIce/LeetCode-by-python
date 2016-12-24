# Longest Common Prefix

strs=[]

def prefix(str):

    if len(str)==0:
        return ""
    ans=str[0]

    for i in str:
        flag=0
        lens1=len(ans)
        lens2=len(i)
        if lens1>lens2:
            lens1=lens2
        for j in range(lens1):
            if ans[j]==i[j]:
                flag+=1
            else:
                break
        ans=ans[0:flag]

    return ans

print(prefix(strs))