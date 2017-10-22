# MVA "Introduction to Programming with Python" video 3

#Collect name from the user
name = input("what is your name?  ")
country = input("What country do you live in?  ")
country = country.upper()

#Display the name
#print(name)

#Creat a friendly output
print("\nHello, " + name + ".  You live in " + country)


#Update the value
#name = "Gary"
#print(name)

#Variables also allow you to manipulate the contents of the variable
message = "hello world"
#print(message.lower())
#print(message.upper())
#print(message.swapcase())

#What do you think these functions will do?

print(message.find("world")) #tells number position of first letter of the string 'world'
print(message.count("o"))   #counts appearances of the letter 'o' in the message string.
print(message.capitalize()) 
print(message.replace("Hello", "Hi")) #replaces first word with another.