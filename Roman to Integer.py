# Roman to Integer
# AC

s="IV"



def convert(str):
    d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

    lens=len(str)
    ans=d[str[lens-1]]
    l=range(lens)[::-1]

    for i in l:
        if i>0 and d[str[i]]<=d[str[i-1]]:
            ans+=d[str[i-1]]
        elif i>0 and d[str[i]]>d[str[i-1]]:
            ans-=d[str[i-1]]
    return ans

print(convert(s))