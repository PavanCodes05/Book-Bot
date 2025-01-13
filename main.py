# Open the book
with open("./books/frankenstein.txt", "r") as file:
    file_contents = file.read()

# Analysis
"""
1. Count the number of words
2. Count occurances of each characters
"""

words = len(file_contents.split(" "))

letters = dict()

joined_words = file_contents.strip()
lowercase = joined_words.lower()

for letter in lowercase:
    letters[letter] = 1 + letters.get(letter, 0)

# Report
with open("report.txt", "w") as file:
    file.write("____________________Beginning of the report_____________________\n\n")

    file.write(f"Total Number of words: {words}\n\n")

    for val, occ in letters.items():
        file.write(f"The letter '{val}' has occured {str(letters[val])} times.\n")

    file.write("\n\n____________________End of the report___________________________")
