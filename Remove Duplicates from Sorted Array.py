# Remove Duplicates from Sorted Array
#AC
nums=[1,1,2,2,3,4,4,4,5]

i=0
j=0

lens=len(nums)

while i<lens:
    nums[j]=nums[i]
    i+=1
    j+=1
    if i>=lens:
        break
    while nums[i]==nums[i-1]:
        i+=1
        if i>=lens:
            break


nums=nums[0:j]

ans=len(nums)
print(nums)
print(ans)
