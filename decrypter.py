a=input('Enter string:- ')
b=int(input('Enter no.'))
c=('zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba')
d=('ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ')
e=''
for i in range(0,len(a)):
    z=a[i]
    y=c.find(z)
    e=e+c[y+b]
print(e)
