# lists and shit
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# first kind of loop
for number in the_count:
    print("This is count {}".format(number))

#same as above

for fruit in fruits:
    print("This is a type of fruit: {}".format(fruit))

#also we can mix lists
for i in change:
    print("I got {}".format(i))

elements = []

#the use a range function to do 0 to 5

for i in range(6):
    print("Adding {} to the list.".format(i))
    elements.append(i)

for i in elements:
    print("Element was: {}".format(i))
