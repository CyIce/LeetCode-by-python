# ZigZag Conversion

s="A"

ans=[]

lens=len(s)

numRows=2

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
        k=i-index
        j=0
        while j<=row:
            if j%gap==0:
                k+=index
                if k>=lens:
                    ans.append("\n")
                    break
                ans.append(s[k])
            elif (j+1)%gap==0 and i!=0 and i!=numRows-1:
                t=k
                k+=(index-i*2)
                if k>=lens:
                    ans.append("\n")
                    break
                print(k)
                ans.append(s[k])
                k=t
            else:
                ans.append(" ")

            if j!=row:
                ans.append(" ")
            else:
                ans.append("\n")

            j+=1

        i+=1

if numRows==1:
    ans=" ".join(s)
else:
    zig()
    #将ans转换为字符串；
    ans="".join(ans)





print(ans)
