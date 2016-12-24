# Palindrome Number
# AC

x=1000101

def palindrome(num):
    remainder=0
    num2=0
    while num2<=num:
        remainder=num%10
        num//=10

        if num==num2:
            return True
        num2=num2*10+remainder

        if num==num2:
            return True
    return False


if (x!=0 and x%10==0) or x<0:
    print(False)
else:
    print(palindrome(x))