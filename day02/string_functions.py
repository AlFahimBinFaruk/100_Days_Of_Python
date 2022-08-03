story="lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

# count length
print(len(story))
# see what the string endwith
print(story.endswith("laborum."))
# count the number of word and character in a string
print(story.count("lorem"))
print(story.count("o"))
# capitalize the first word of a string
print(story.capitalize())
# find the first occureance of a word or character in a string
print(story.find("Ipsum"))
print(story.find("l"))
# replace all the occurance of a word or character in a string
print(story.replace("lorem","Fahim"))
print(story.replace("o","Fahim"))