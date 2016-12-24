# Verify Preorder Serialization of a Binary Tree
# AC

preorder="9,3,4,#,#,1,#,#,2,#,6,#,#"

"""
lens=len(preorder)
print(preorder)

def check(str):
    num=0
    for i in range(lens):
        if i==0 and str[i]!='#':
            num+=2
        elif str[i]==',' or str[i-1]!=',':
            continue
        elif num<=0:
            return False

        elif str[i]!='#':
            num+=1

        elif str[i]=='#':
            num-=1

    if num==0:
        return True
    else:
        return False
if lens==1 and preorder[0]=='#':
    print(True)
else:
    print(check(preorder))
"""

"""
def check(str):
    num=0
    comma=0
    if len(str)!=1 and str[0]=='#':
        return False
    for i in str:
        if comma>=1 and (num-1)*2>=comma:
            return False

        if i=='#':
            num+=1
        elif i==',':
            comma+=1
    if num==0:
        return False
    if comma==(num-1)*2:
        return True
    else:
        return False

print(check(preorder))
"""
