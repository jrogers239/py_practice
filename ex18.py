def cheese_and_crackers(cheese_count, boxes_of_crackers):
        print("You have {} cheeses!".format(cheese_count))
        print("You have {} boxes of crackers!".format(boxes_of_crackers))
        print("Man that's enough for a party!")
        print("Picnic time")

print("We can just give the function numbers directly")
cheese_and_crackers(20,30)

print("or we can use varaibles from out script:")

amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(10,50)

print("We can also do math")
cheese_and_crackers(10+20,5+6)
print("Combine it now!")
cheese_and_crackers(amount_of_cheese+100,amount_of_crackers+1000)
