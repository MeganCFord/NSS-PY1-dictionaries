my_family = {
    'sister': {
        'name': 'Emily',
        'age': 26
        },
    'mother': {
        'name': 'Kelly',
        'age': 56
        },
    'father': {
        'name': 'Steve',
        'age': 56
    },
    'brother': {
        'name': 'Evan',
        'age': 23
    }
}

# Using a dictionary comprehension, produce output that looks like the following example.

# Krista is my sister and is 42 years old
# Helpful hint: To convert an integer into a string in Python, it's str(integer_value)

family_descriptions = [info['name'] + ' is my ' + relationship + ' and is ' + str(info['age']) + ' years old.' for (relationship, info) in my_family.items()]
print(family_descriptions)
