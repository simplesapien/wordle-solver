import string

# Dictionary of words courtesy: https://github.com/dwyl/english-words
# I had another script just go through and pull all the 5-letter words into a separate text file
textfile = open("words.txt", "r")

# Load each of those 5-letter words into an array
words = []
for word in textfile:
    word = word.rstrip("\n")
    words.append(word)

# Initialize a dictionary with every letter of the alphabet, set their values to zero, then create an array of letters to be used for guesses
alphabet = list(string.ascii_lowercase)
remainingLetters = []
letters = {}
for letter in alphabet:
    letters[letter] = 0
    remainingLetters.append(letter)

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

# Sort scores in descending order from most used to least used
sortedScores = dict(sorted(scores.items(), key=lambda item: item[1], reverse=True))

# See the top 50 scoring words
top = list(sortedScores.items())[:50]
print(top)


# Randomly use one of the highest scoring words as first word
# Find way to interact with page to know if correct letters selected
# Adjust 5 letter word dictionary and repeat
