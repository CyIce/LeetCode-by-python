# ZigZag Conversion

s="0123456"

ans=[]

lens=len(s)

numRows=3

#记录每一行字符的个个数；
row=(lens-1)//2
#记录每两个字符的最大间隔；
gap=numRows-1
#记录两行之间的下标差；
index=2*gap

if lens<numRows:
    numRows=lens

def zig():
    i=0
    while i<numRows:
        k=i
        j=0
        while k<lens and j<=row:
            if i==0 or i==numRows-1:
                ans.append(s[k])
                k+=index
            else:
                ans.append(s[k])
                k+=(index-i*2)
                if k>=lens:
                    break
                ans.append(s[k])
                k+=2*i
            j+=1

        i+=1

if numRows==1:
    ans="".join(s)
else:
    zig()
    #将ans转换为字符串；
    ans="".join(ans)





print(ans)
