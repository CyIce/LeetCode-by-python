# Bulls and Cows
#AC

secret="3928"
guess="5137"

secret=list(secret)
guess=list(guess)

a=0
b=0





lens=len(secret)

i=0
while i<lens:
    if secret[i]==guess[i]:
        a+=1
        lens-=1
        secret.pop(i)
        guess.pop(i)
        i-=1
    i+=1

secret=sorted(secret)
guess=sorted(guess)

lens=len(secret)

j=0
k=0

print(secret)
print(guess)

while j<lens and k<lens:
    while j<lens and secret[j]<guess[k]:
        j+=1
    while j<lens and secret[j]>guess[k]:
        k+=1
        if k>=lens:
            break
    if j>=lens or k>=lens:
        break
    if secret[j] == guess[k]:
        b += 1
    if secret[j]<guess[k]:
        j+=1
    elif guess[k]<secret[j]:
        k+=1
    else:
        j+=1
        k+=1

'''
lens=len(secret)

for i in secret:
    if i in guess:
        b+=1
        for j in range(len(guess)):
            if guess[j]==i:
                guess.pop(j)
                break

'''
ans=str(a)+"A"+str(b)+"B"

print(ans)
