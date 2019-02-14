''' Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------'''

inp=input()
l=inp.split()
n=int(l[0])
m=int(l[1])


pattern=''
for i in range(int(n/2)):
    pattern+=(('.|.'*(i*2+1)).center(m,'-'))
    pattern+='\n'
    
print(pattern,end='')

for z in range(m-6):
    if(z==((m-7)/2)):
        print('WELCOME',end='')
    else:
        print('-',end='')

print(pattern[::-1])    








    



