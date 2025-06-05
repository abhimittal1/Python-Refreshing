#Find the name starting from the S
 
list = ["Happy" , "Abhishek" , "Suraj" , "Sujal" , "Sameer"]

for name in list:
    if(name.startswith("S")):
        print(f"{name}, You are most Welcome!")

#pattern printing

n = 5
for i in range( 1 , n+1):
    print(" "*(n-i),end = "")
    print("*"*((2*i)-1) , end = "")
    print("") 
                
print("")

#reverse table 
for i in range(10, 0 , -1):
    print(f"5 X {i} = {5 * i}" )

        