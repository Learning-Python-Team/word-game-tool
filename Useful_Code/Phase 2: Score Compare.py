#The user gives 2 words and the program indicates which is the better scorer based on the letter values only.

# function to convert a word to the base point value using the letter

# does not account for value modifications based on a board


def score_compare(word1, word2):
    # Convert word passed in to uppercase so it can find
    # keys in dictionary
    word1 = word1.upper()
    word2 = word2.upper()

    # dictionary of letters and their point values
    charDict = {
        ' ': 0,
        'A': 1,
        'B': 3,
        'C': 3,
        'D': 2,
        'E': 1,
        'F': 4,
        'G': 2,
        'H': 4,
        'I': 1,
        'J': 8,
        'K': 5,
        'L': 1,
        'M': 3,
        'N': 1,
        'O': 1,
        'P': 3,
        'Q': 10,
        'R': 1,
        'S': 1,
        'T': 1,
        'U': 1,
        'V': 4,
        'W': 4,
        'X': 8,
        'Y': 4,
        'Z': 10,
    }
    # Refactored for loop with list comprehension
    # Basically grabs the number value that correlates with the
    # letter in the word and creates a list. Returns the sum of the list
    # Example: 'Dog' -> sum([2, 1, 2]) = 5
    word1_score = sum([charDict[char] for char in word1])
    word2_score = sum([charDict[char] for char in word2])

    print('{} is worth {} points'.format(word1, word1_score))
    print('{} is worth {} points'.format(word2, word2_score))

    if word1_score > word2_score:
        better_by = word1_score - word2_score
        print('{} is better by {} points'.format(word1, better_by))
    elif word1_score < word2_score:
        better_by = word2_score - word1_score
        print('{} is better by {} points'.format(word2, better_by))
    elif word1_score == word2_score:
        print('{} and {} have the same score'.format(word1, word2))

score_compare('need','coffee')
