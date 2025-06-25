# Create a dictionary
student = {'name': 'Sanu', 'age': 21, 'college': 'Cosmos'}

print(student.keys())          # dict_keys(['name', 'age', 'college'])
print(student.values())        # dict_values(['Sanu', 21, 'Cosmos'])
print(student.items())         # dict_items([('name', 'Sanu'), ('age', 21), ('college', 'Cosmos')])

print(student.get('name'))     # Sanu
print(student.get('dept', 'N/A'))  # N/A (default)

student['age'] = 22            # Update value
student.update({'dept': 'Computer'})  # Add new key

print(student.pop('college'))  # Removes and returns 'Cosmos'
print(student)                 # {'name': 'Sanu', 'age': 22, 'dept': 'Computer'}

copy_dict = student.copy()     # Shallow copy
student.clear()                # Removes all items

# Create sets
a = {1, 2, 3}
b = {3, 4, 5}

a.add(6)                       # Add single element
a.remove(1)                   # Remove element (error if not found)
a.discard(10)                 # Safe remove (no error)
a.pop()                       # Removes random element

# Set operations
print(a.union(b))             # {2, 3, 4, 5, 6}
print(a.intersection(b))      # {3}
print(a.difference(b))        # {2, 6}
print(a.symmetric_difference(b))  # {2, 4, 5, 6}

# Checks
print(a.issubset(b))          # False
print(a.issuperset(b))        # False
print(a.isdisjoint(b))        # False
