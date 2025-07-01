'''a=[1,2,2,4,5,5,6,6,7,8]
s=set(a)
print(s)
if 9 in s:
    print( "is present")
else:
    print("not presetn")'''
    
    
'''for i in range(1,12):    
    print(i)
    
for i in range(12):
    print(i)'''
    
    
'''i=1
while i<10:
    print(i,end=' ')
    i+=1'''
   
   
    
'''a=[1,2,3,4,1,2,3,1,4,5,6,7,7,8]
n=len(a)
traget = 9
for i in range(n):
    if a[i]==traget:
        print("true")
    else :
        print("fales")
        break'''
        
        
'''a=[1,1,1,2,3,4,1,4,5,3,5,6,7,8,9]
n=len(a)
target = 2 
count = 0
for i in range(n):
    if a[i]==target:
        count+=1
print(count)'''


a=[1,2,3,1,1,2,3,4,5,6,7,4,2,4,6,3,2]
maxi = a[0]
for i in a:
    if i>maxi:
        maxi =i
print(maxi)