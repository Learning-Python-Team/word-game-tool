# function to convert a word to the base point value using the letter

# does not account for value modifications based on a board

def point_conversion(word):
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
    score = 0
    for char in word:
        score += charDict[char]
    return score

# example
# print(point_conversion('EXAMPLE'))

