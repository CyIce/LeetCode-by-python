#Two Sum

import sys
sys.setrecursionlimit(1000000)

nums=[3,2,4]

target=6
lens=len(nums)-1

arr=sorted(nums)

print(arr)

flag=False

def find(head,tail,value):
    global  flag
    mid=(head+tail)//2
    if value==arr[mid]:
        flag=arr[mid]
        return
    if tail-head==1:
        for i in range(2):
            if value==arr[head+i]:
                flag=arr[head+i]
                return
    if value>arr[tail] or value<arr[head]:
        return
    if mid>head and mid<tail and value<arr[mid]:
        find(head,mid,value)
    if mid<tail and mid>head and value>arr[mid]:
        find(mid,tail,value)

for i in range(lens):
    find(0,i-1,target-arr[i])
    if flag==False:
        find(i+1,lens,target-arr[i])
    else:
        ans=[arr[i],flag]
        break

ans[0]=nums.index(ans[0])
ans[1]=nums.index(ans[1])

if ans[0]>ans[1]:
    temp=ans[0]
    ans[0]=ans[1]
    ans[1]=temp

print(ans)