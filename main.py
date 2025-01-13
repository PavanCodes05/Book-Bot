# Reads the book content and returns a array of words
def read_book(book_path):
    with open(book_path, "r") as book:
        book_contents = book.read()
    return book_contents

# Reads the book content and return the number of words
def count_words(book_contents):
    words = len(book_contents.split(" "))
    return words

# Reads the book content and converts uppercase to lowercase 
def convert_lowercase(book_contents):
    lowercase_contents = book_contents.strip().lower()
    return lowercase_contents

# Reads the lowercase contents and returns the dictionary with each letter occurances
def count_letter(lowercase_contents):
    letter_count = dict()
    for letter in lowercase_contents:
        letter_count[letter] = 1 + letter_count.get(letter, 0)
    return letter_count

# Generates Report.txt file 
def generate_report(word_count, letter_count):
    with open("report.txt", "w") as file:
        file.write("____________________Beginning of the report_____________________\n\n")

        file.write(f"Total Number of words: {word_count}\n\n")

        for val, occ in letter_count.items():
            file.write(f"The letter '{val}' has occured {str(letter_count[val])} times.\n")

        file.write("\n\n____________________End of the report___________________________")

# Main function that organizes all of the code (Functional Programming)  
def main():
    book_path = "./books/frankenstein.txt"
    
    book_contents = read_book(book_path)
    
    word_count = count_words(book_contents)
    lowercase_contents = convert_lowercase(book_contents)

    letter_count = count_letter(lowercase_contents)
    
    generate_report(word_count, letter_count)

# Calls the main function
main()