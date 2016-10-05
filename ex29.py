states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a baisc set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detriot',
    'FL': 'Jacksonville'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print
print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

#dot it by using the state then cities dict
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

#print every state abbreviation
print('-' * 10)
for state, abbrev in states.items():
    print("{} is abbreviated {}".format(state,abbrev))

# print every city in state
print('-' * 10)
for abbrev, city in cities.items():
    print("{} has the city {}".format(abbrev, city))

print('-' * 10)
for state, abbrev in states.items():
    print("{} state is abbreviated {} and has city {}".format(state, abbrev, cities[abbrev]))

print('-' * 10)
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")

city = cities.get('TX', 'Does not Exist')
print("The city for the state 'TX' is: {}".format(city))
