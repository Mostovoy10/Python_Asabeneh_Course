# Variables in Python
f_n = 'Alex'
last_name = 'Sánchez'
country = 'Spain'
city = 'Ávila'
age = 29
is_married = False
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
   'firstname':'ALEX',
   'lastname':'SANCHEZ',
   'country':'SPAIN',
   'city':'AVILA'
   }

print('Hello, World!') # The text Hello, World! is an argument
print('Hello',',','World','!') # it can take multiple arguments, four arguments have been passed
print(len('Hello, World!')) # it takes only one argument

print('First name:', f_n)
print('First name length:', len(f_n))
print('Last name:', last_name)
print('Last name length:', len(last_name))
print('Country:',country)
print('City:',city)
print('Age:',age)
print('Married:', is_married)
print('Skills:', skills)
print('Person information:', person_info)


f_n, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

print(f_n, last_name, country, age, is_married)
print('First name:', f_n)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)


# Different python data types
# Let's declare variables with various data types

f_n = 'Asa'     # str
last_name = 'Yeta'       # str
country = 'Finland'         # str
city= 'Helsinki'            # str
age = 150                   # int, it is not my real age, don't worry about it

# Printing out types
print(type('Asabeneh'))     # str
print(type(f_n))     # str
print(type(10))             # int
print(type(3.14))           # float
print(type(1 + 1j))         # complex
print(type(True))           # bool
print(type([1, 2, 3, 4]))     # list
print(type({'name':'Asabeneh','age':250, 'is_married':250}))    # dict
print(type((1,2)))                                              # tuple
print(type(zip([1,2],[3,4])))                                   # set


# int to float
num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0

# float to int
gravity = 9.81
print(int(gravity))             # 9

# int to str
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'

# str to int or float

num_str = '7.6' 

"""
print('num_int', int(num_str))      # 10 """

print('num_float', float(num_str))  # 10.6 

# str to list
f_n = 'Asabeneh'
print(f_n)               # 'Asabeneh'
first_name_to_list = list(f_n)
print(first_name_to_list)            # ['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']