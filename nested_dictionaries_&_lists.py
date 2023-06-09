# 1. Update Values in Dictionaries and Lists
#   1. Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
#   2. Change the last_name of the first student from 'Jordan' to 'Bryant'
#   3. In the sports_directory, change 'Messi' to 'Andres'
#   4. Change the value 20 in z to 30
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
# 1.1
x[1][0] = 15
# 1.2
students[0]['last_name']='Bryant'
# 1.3
sports_directory['soccer'][0] = 'Andres'
# 1.4
z[0]['y'] = 30


# 2. Iterate Through a List of Dictionaries
# Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:
def iterateDictionary(list):
    for person in list:
        # first solution, hard code the first/last name into the print
        # print('first_name -', person['first_name'] + ', last_name -', person['last_name'])

        # second solution, allow print to be modular to input data
        result = ''
        for key, val in person.items():
            # added conditional to add a comma and spacing before new entries
            if result != '': result += ', '
            result += key + ' - ' + val
        print(result)

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(students)
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel


# 3. Get Values From a List of Dictionaries
# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary.
def iterateDictionary2(key_name, some_list):
    for person in some_list:
        # talking to Ben, he unintentionally added this conditional to check if key_name was available. I liked that, so I'm adding it in.
        if key_name in person:
            print(person[key_name]) # my original solution only had this print, not the surrounding if-statement
        else:
            print('cannot find ' + key_name)
iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)
# For example, iterateDictionary2('first_name', students) should output:
# Michael
# John
# Mark
# KB
# And iterateDictionary2('last_name', students) should output:
# Jordan
# Rosales
# Guillen
# Tonel

# edgecase testing
# iterateDictionary2('middle_name', students)

# 4. Iterate Through a Dictionary with List Values
# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example:
def printInfo(some_dict):
    for key, val in some_dict.items():
        print(len(val), key.upper())
        for i in val:
            print(i)

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)
# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon