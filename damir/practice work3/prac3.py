l, u, p, d = 0, 0, 0, 0
s=input("Write your pasword:")
capitalalphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
smallalphabets="abcdefghijklmnopqrstuvwxyz"
specialchar="*-#"
digits="0123456789"
def pasword_cracker(s):
    if (len(s) == 8):
        for i in s:
            if (i in smallalphabets):
                l+=1
            if (i in capitalalphabets):
                u+=1
            if (i in digits):
                d+=1
            if(i in specialchar):
                p+=1       
if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(s)):
    print("The password is perfect")
else:
    print("Invalid Password")

pasword_cracker(s)