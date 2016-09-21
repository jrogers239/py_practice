# reading and writing files

from sys import argv

script, filename = argv

print("We're going to erase {}".format(filename))
print("If you don't want that, hit CTRL-C (^C)")
print("If you do wan that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file.")
target.truncate()

print("Now I'm going to ask you for three lines")

line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("I'm going to write these to the file")

lines = line1 + "\n" + line2 + "\n" + line3 + "\n"
print(lines)
target.write(lines)

print("Closing")
target.close()
