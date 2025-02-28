#string data type
myString = "This is a string."
print(myString)

#check type
print(type(myString))

#convertthe value of type to string
print(myString + " is of the data type " + str(type(myString)))


#concatenation(combine two strings to one)
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)


#input string
name = input("What is your name? ")

print(name)


#formatting output strings
color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")

print("{}, you like a {} {}!".format(name,color,animal))