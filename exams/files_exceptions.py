'''
In this exercise, you will practice both File I/O as well as using Exceptions
in a real-world scenario.

You have a folder containing three text files of books from Project Gutenberg:
- war_and_peace.txt
- pride_and_prejudice.txt
- crime_and_punishment.txt

1) Open war_and_peace.txt, read the whole file content and store it in a variable

2) Open crime_and_punishment.txt and overwrite the whole content with an empty string

3) Loop over all three files and print out only the first character each. Your program
    should NEVER terminate with a Traceback.

    a) Which Exception can you expect to encounter? Why?

    b) How do you catch it to avoid the program from terminating with a Traceback?


BONUS CHALLENGE: write a custom Exception that inherits from Exception and raise it if the
first 100 characters of any of the files contain the string "Prince".

'''

# BONUS
class PrinceException(Exception):
    pass

# 1
with open("books/war_and_peace.txt", "r") as fin:
    content = fin.read()
print(f"TEST: {content[1000:1005]}")  # example test

# 2
with open("books/crime_and_punishment.txt", "w+") as fout:
    fout.write("")

# 3
books = [
    "war_and_peace.txt",
    "crime_and_punishment.txt",
    "pride_and_prejudice.txt"
    ]

for book in books:
    try:
        with open("books/" + book, "r") as fin:
            content = fin.read()
    except FileNotFoundError as fnf:
        print(f"ERROR in {book}: {fnf}")
    except PermissionError as err:
        print(f"ERROR in {book}: {err}")
    else:
        try:
            first_char = content[1]
        except IndexError as err:
            print(f"ERROR in {book}: {err}")
        else:
            # if "Prince" in content[:100]:
            #     raise PrinceException
            print(f"{book}: {first_char}")
