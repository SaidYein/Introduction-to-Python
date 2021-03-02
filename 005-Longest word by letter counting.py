text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do \
eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad \
minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex \
ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate \
velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat \
cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id \
est laborum."

length = 0
word = ""

# initialize variables for storing the max. length and longest word
max_length = 0
longest_word = ""

# for all characters in the text ...
for character in text:
    
    # check if the character is a letter (part of a word).
    if character.isalpha():
        # if yes, increment the length counter and 
        # add the character to the word to remember
        length += 1
        word += character
    else:
        # reset running variables
        length = 0
        word = ""

    # check if the last word was longer then the previous longest word
    if length > max_length:
        # if yes, remember the new max. length and longest word
        max_length = length
        longest_word = word
        
# print result
print(f"The longest word in the text is \"{longest_word}\" " \
      f"({max_length} characters).")