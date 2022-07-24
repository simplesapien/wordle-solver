from operator import indexOf
import string

# Dictionary of words courtesy: https://github.com/dwyl/english-words
# I had another script just go through and pull all the 5-letter words into a separate text file
textfile = open("words.txt", "r")

# Load each of those 5-letter words into an array
words = []
for word in textfile:
    word = word.rstrip("\n")
    words.append(word)

# Initialize a dictionary with every letter of the alphabet, set their values to zero
alphabet = list(string.ascii_lowercase)
letters = {}
for letter in alphabet:
    letters[letter] = 0

# Count the occurrence of every letter in the alphabet among the list of 5 letter words, and count the total number of letters
totalLetters = 0
for word in words:
    for letter in word:
        letters[letter] += 1
        totalLetters += 1

# Calculate percentage occurence of each letter in the list of words
for key, value in letters.items():
    letters[key] = round((value / totalLetters) * 100, 4)

# Give score to word based on percentage
scores = {}
for word in words:
    scores[word] = 0

    # Create a set to avoid double counting repeating characters
    unique = "".join(set(word))
    for letter in unique:
        scores[word] += letters[letter]


# Only guess words that meet certain conditions
grayLetters = ""

# Figure out a case for yellow that accounts for a letter being guessed wrong in certain positions a couple of times
yellowLetters = ["", "", "", "", ""]
greenLetters = ["", "", "", "", ""]

# Gray letters
for key in list(scores.keys()):
    for letter in grayLetters:
        if letter in key:
            del scores[key]
            break

# Green letters
for key in list(scores.keys()):

    # Loop through letters in the green array
    for letter in greenLetters:

        # if a letter exists
        if letter:

            # store the index of that letter
            index = greenLetters.index(letter)

            # if the letter isn't equal to the equivalent position in the key, remove that key
            if letter != key[index]:
                del scores[key]
                break


# Yellow letters
for key in list(scores.keys()):

    # Go through each letter in yellow array
    for letter in yellowLetters:

        # If a letter exists
        if letter:

            # Grab its index
            index = yellowLetters.index(letter)

            # If the letter exists in key, but NOT at key[index], continue, else delete that item
            if letter in key and letter != key[index]:
                continue
            else:
                del scores[key]

        else:
            break

sortedScores = dict(sorted(scores.items(), key=lambda item: item[1], reverse=True))
top = list(sortedScores.items())[:30]
print(top)
