# Minimum Size Subarray Sum
#AC

nums=[2,3,1,2,4,3]

ans=len(nums)

s=7


l=0
r=0
tot=0
nowL=0

for i in nums:
    tot+=i
    r+=1
    nowL+=1
    if tot>=s:
        while tot-nums[l]>=s:
            tot-=nums[l]
            l+=1
            nowL-=1
        if ans>nowL:
            ans=nowL
if tot<s:
    print(0)
else:
    print(ans)












