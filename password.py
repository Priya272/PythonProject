import random
n=int(input("password length is: "))
c='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~`!@#$%^&*()_-+={[}]|\:;",?<>./'''
p=[]
for i in range(0,n):
    password=random.choice(c)
    
    p.append(password)
    password=''.join(p)

if(n<4):
    print("Password cannot be created \n")    


else:
 print(password)

