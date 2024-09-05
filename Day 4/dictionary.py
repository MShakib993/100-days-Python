# Creating a dictionary 'a' with key-value pairs
a = {
    "Name": "Shakib",              # Key: 'Name', Value: 'Shakib'
    "Profession": "AI ML Engineer", # Key: 'Profession', Value: 'AI ML Engineer'
    "Package": "10 Crore CTC"       # Key: 'Package', Value: '10 Crore CTC'
}

# Printing the entire dictionary
print(a)  
# Output: {'Name': 'Shakib', 'Profession': 'AI ML Engineer', 'Package': '10 Crore CTC'}

# Accessing the value associated with the key "Name" using the get() method
print(a.get("Name"))  
# Output: 'Shakib'

# Updating the value for the key "Name" to 'Babul' using the update() method
a.update({"Name": "Babul"})  
# The value of "Name" is now updated to 'Babul'

# Printing the updated dictionary
print(a)  
# Output: {'Name': 'Babul', 'Profession': 'AI ML Engineer', 'Package': '10 Crore CTC'}

# Printing all the keys in the dictionary using the keys() method
print(a.keys())  
# Output: dict_keys(['Name', 'Profession', 'Package'])

# Printing all the key-value pairs in the dictionary using the items() method
print(a.items())  
# Output: dict_items([('Name', 'Babul'), ('Profession', 'AI ML Engineer'), ('Package', '10 Crore CTC')])
