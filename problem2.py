# write a program to input eight numbers from the user and display all the unique numbers(once).
s=set()

n=input("Enter number 1:")
s.add(int(n))
n=input("Enter number 2:")
s.add(int(n))
n=input("Enter number 3:")
s.add(int(n))
n=input("Enter number 4:")
s.add(int(n))
n=input("Enter number 5:")
s.add(int(n))
n=input("Enter number 6:")
s.add(int(n))
n=input("Enter number 7:")
s.add(int(n))
n=input("Enter number 8:")
s.add(int(n))

print(s)
# output Enter number 1:3
#Enter number 2:2
#Enter number 3:4
#Enter number 6:8
#Enter number 7:2
#Enter number 8:3
#{2, 3, 4, 5, 7, 8}