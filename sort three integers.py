x=int(input("Input 1st Number : "))
y=int(input("Input 2nd Number : "))
z=int(input("Input 3rd Number : "))
 
a1=min(x,y,z)
a3=max(x,y,z)
a2=(x+y+z)-a1-a3
print("Number in sorted order: ", a1 , a2 , a3)
