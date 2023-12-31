# syntax
st = set()
st = {'item1', 'item2', 'item3', 'item4'}


# Examples
st = {'item1', 'item2', 'item3', 'item4'}
print(len(st))

fruits = {'banana', 'orange', 'mango', 'lemon'}
print(len(fruits))


# Checking an item
st = {'item1', 'item2', 'item3', 'item4'}
print("Does set st contain item3? ", 'item3' in st) # Does set st contain item3? True

fruits = {'banana', 'orange', 'mango', 'lemon'}
print('mango' in fruits ) # True


# Adding items to a set
st = {'item1', 'item2', 'item3', 'item4'}
st.add('item5')
print(st)

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.add('lime')
print(fruits)

st = {'item1', 'item2', 'item3', 'item4'}
st.update(['item5','item6','item7']) #Adding multiple items
print(st)

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)
print(fruits)


# Removing items from a set
st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item2')
print(st)

fruits = {'banana', 'orange', 'mango', 'lemon'}
print(fruits.pop())  # removes a random item from the set
print(fruits)

fruits = {'banana', 'orange', 'mango', 'lemon'}
removed_item = fruits.pop() 
print(removed_item)
print(fruits)


# Clearing items in a set
st = {'item1', 'item2', 'item3', 'item4'}
st.clear()
print(st)

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear()
print(fruits) # set()


# Deleting a set
st = {'item1', 'item2', 'item3', 'item4'}
del st
#print(st) #ERROR

fruits = {'banana', 'orange', 'mango', 'lemon'}
del fruits
#print(fruits) #ERROR


# Converting list to set
lst = ['item1', 'item2', 'item3', 'item4', 'item1']
st = set(lst)  # {'item2', 'item4', 'item1', 'item3'} - the order is random, because sets in general are unordered
print(st)

fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
fruits = set(fruits) # {'mango', 'lemon', 'banana', 'orange'}
print(fruits)


# Joining sets
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)
print(st3)

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
print(fruits.union(vegetables)) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st1.update(st2) # st2 contents are added to st1
print(st1)

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
fruits.update(vegetables)
print(fruits) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}


# Finding intersections items
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
print(st1.intersection(st2)) # {'item3', 'item2'}

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers.intersection(even_numbers)) # {0, 2, 4, 6, 8, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.intersection(dragon))    # {'o', 'n'}


# Checking subset and superset
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print(st2.issubset(st1)) # True
print(st1.issuperset(st2)) # True


whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers.issubset(even_numbers))# False, because it is a super set
print(whole_numbers.issuperset(even_numbers)) # True

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.issubset(dragon))   # False


# Checking the difference between two sets
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print(st2.difference(st1)) # set()
print(st1.difference(st2)) # {'item1', 'item4'} => st1\st2


whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers.difference(even_numbers)) # {1, 3, 5, 7, 9}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.difference(dragon))    # {'p', 'y', 't'}  - the result is unordered (characteristic of sets)
print(dragon.difference(python))    # {'d', 'r', 'a', 'g'}


# Finding simetric differences between two sets
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
# it means (A\B)∪(B\A)
print(st2.symmetric_difference(st1)) # {'item1', 'item4'}

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
print(whole_numbers.symmetric_difference(some_numbers)) # {0, 6, 7, 8, 9, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.symmetric_difference(dragon))  # {'r', 't', 'p', 'y', 'g', 'a', 'd', 'h'}


# Disjoint sets
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print(st2.isdisjoint(st1)) # False

even_numbers = {0, 2, 4 ,6, 8}
odd_numbers = {1, 3, 5, 7, 9}
print(even_numbers.isdisjoint(odd_numbers)) # True, because no common item

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.isdisjoint(dragon)) # False, there are common items {'o', 'n'}