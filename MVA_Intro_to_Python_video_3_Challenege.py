#Write a program that allows a person to personalize a story.

#Take a page from a  book or make up a story.  Ask the user to enter information
#you can replace in the story such as their name, a place, or insert adjectives 
#or adverbs into the story.  Then display the personalized story to the user.

male = input("Enter a male name:  ")
male = male.capitalize()
location = input("Where is he from?  ")
location = location.capitalize()
female = input("Enter a female name:  ")
female = female.capitalize()
gift = input("Name something you'd give to someone you love:  ")
animal = input("Name a type of animal:  ")
animal = animal.capitalize()


print("\n\n\tA long time ago, there lived a fierce warrior named " + male + ", ")
print("who was the most talented fighter in all of " + location + ".  The only ")
print("thing that mattered to him was fighting.  That is, until " + female)
print("came along and stole his heart.  In an attempt to gain her ")
print("affection, he presented her with " + gift + ".  Her eyes widened ")
print("with joy. 'For me?  You shouldn't have!', " + female + " exclaimed.")
print("8.3 seconds later, they got married and rode into the sunset ")
print("on the back of a beautiful " + animal + "... ")
print("\nAnd they may, or may not have, lived happily ever after. \n\n\tThe End\n")