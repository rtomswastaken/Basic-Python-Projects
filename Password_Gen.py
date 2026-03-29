import random

def GenPass(Len):
    chars="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*()_+=-;:',.></?{]}[|\]"
    pwd=""
    for i in range(Len):
        p=random.choice(chars)
        pwd+=p
    return pwd

n=int(input("Enter the length of the password: "))
print(GenPass(n))
