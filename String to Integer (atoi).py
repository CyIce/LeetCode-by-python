# String to Integer (atoi)
# AC

str="   - 321"

b=False

flag=0

ans=0

lens=len(str)

p=True

for i in range(lens):

    if str[i]=='-' and flag==0:
        b=True

    if (str[i]=='+' or str[i]=='-') and flag==0:
        flag+=1
        continue
    if flag>1:
        break
    if str[0].isalpha()==True:
        break

    if str[0].isdigit()==False and i==0:
        continue

    if str[i] == ' ' and p==False:
        break
    if str[i] == ' ':
        continue

    if str[i].isdigit()==False and i>=1:
         break
    ans*=10
    ans+=int(str[i])
    p=False


if b==True:
    ans*=-1



print(ans)