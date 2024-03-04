# Initializing emty lists, set, and dictionary
books_list = []
authors_set = set()
books_dict = {}

# Add books
books_list.append("Python Programming")
authors_set.add("John Smith")
books_dict["Python Programming"] = "Jhon Smith"

books_list.append("Data Structure and Algorithms")
authors_set.add("Jane Doe")
books_dict["Data Structure and Algorithms"] = "Jane Doe"

books_list.append("Machine Learning and Bisics")
authors_set.add("Alice Jhonson")
books_dict["Machine learning and basics"] = "Alice Jhonson"

# Search for a book
search_title = input("Enter the title of the book to search: ")
if search_title in books_list:
    print(f"Book found! Author: {books_dict[search_title]}")
else:
    print("Book not found")
    
# Display all books
print("List of Books:")
for book in books_list:
    print(book)
    
# Removing a book
remove_title = input("Enter the title of the book to remove or else enter to skip: ")
if remove_title in books_list:
    remove_author = books_dict[remove_title]
    books_list.remove(remove_title)
    authors_set.remove(remove_author)
    del books_dict[remove_title]
    print("Books removed successfully!")
    print("Books available: ", books_list)
    
else:
    print("Books not found!")