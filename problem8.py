# If languages of two friends are same; what will happen to the program in problem 6?
# create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.
d= {}
name=input("Enter friends name:")
lang=input("enter language name:")
d.update({name:lang})
name=input("Enter friends name:")
lang=input("enter language name:")
d.update({name:lang})
name=input("Enter friends name:")
lang=input("enter language name:")
d.update({name:lang})
name=input("Enter friends name:")
lang=input("enter language name:")
d.update({name:lang})
print(d)

# output 
#Enter friends name:garima
#enter language name:python
#Enter friends name:rabina
#enter language name:python
#Enter friends name:harry
#enter language name:c++
#Enter friends name:abi
#enter language name:C#     
#{'garima': 'python', 'rabina': 'python', 'harry': 'c++', 'abi': 'C#'}