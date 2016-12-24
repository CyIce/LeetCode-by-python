# Remove Element
#AC

l=[3,2,2,3]

val=3

def remove(nums,val):
    list=range(len(nums))[::-1]
    for i in list:
        if nums[i]==val:
            nums.pop(i)


remove(l,val)
print(l)