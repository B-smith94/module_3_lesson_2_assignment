#Task 1
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

while True:
    new_book = input("Please enter the book you wish to add: "),
    new_book_author = input("Please enter the author of the book you wish to add: "),
    book_and_author = (new_book + new_book_author)
    if book_and_author in library:
        print("That book is already in the Library.")
    else:
        library.append(book_and_author)
        print(library)
        print("Book successfully added.")
    while True:
        another_book = input("Would you like to add another book? (yes/no): ")
        if another_book.lower() == 'yes':
            break
        elif another_book.lower() != 'yes':
            if another_book.lower() == 'no':
                break
            else:
                print("Invalid input, please try again.")
    if another_book.lower() == 'yes':
        continue
    else:
        print(library)
        break
