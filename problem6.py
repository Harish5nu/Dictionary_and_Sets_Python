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
#Enter friends name:harry
#enter language name:python
#Enter friends name:abishek
#enter language name:java
#Enter friends name:garima
#enter language name:c++
#Enter friends name:rabina
#enter language name:c#     
#{'harry': 'python', 'abishek': 'java', 'garima': 'c++', 'rabina': 'c#'}