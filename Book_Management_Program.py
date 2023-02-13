############################# Capstone Project V ###############################

#################################### START #####################################

import sqlite3
from tabulate import tabulate

def create_table():
    """ Creates the books table in the books database. 
    If the table already exists, this function does nothing. 
    If the table is empty, the function inserts five default books.

        Keyword arguments: None
    """
    try:
        # Connects to the database
        database = sqlite3.connect("books.db")
        cursor = database.cursor()
        # Creates the books table if it doesn't exist
        # Sets 'id' as primary key and autoincrements it
        # for new rows
        cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT,
                        author TEXT,
                        qty INTEGER)''')
        # Check if the table is empty                
        cursor.execute("SELECT * FROM books")
        books = cursor.fetchall()
        if len(books) == 0:
            # If the table is empty, insert five sample books
            id = [3001, 3002, 3003, 3004, 3005]
            title = ['A Tale of Two Cities', 
                        'Harry Potter and the Philosopher\'s Stone', 
                        'The Lion, the Witch and the Wardrobe', 
                        'The Lord of the Rings', 
                        'Alice in Wonderland']
            author = ['Charles Dickens', 
                        'J.K Rowling', 
                        'C.S Lewis', 
                        'J.R.R Tolkien', 
                        'Lewis Carroll' ]
            qty = [30, 40, 25, 37, 12]
            for i in range(len(id)):
                # Inserts the new books into the database
                cursor.execute('''INSERT INTO books (id, title, author, qty) 
                                    VALUES (?, ?, ?, ?)''', 
                                    (id[i], title[i], author[i], qty[i]))
        else:
            pass
        # Updates database
        database.commit()
    # Catches database exeption 
    except sqlite3.ProgrammingError as error:
        print(f"Programming Error occured, "
                f"please contact IT support", error)
    except sqlite3.OperationalError as error:
        print(f"Unexpected Error in the database, "
                f"please contact IT support", error)
    except sqlite3.DataError as error: 
        print(f"Data processing error",
                f"please contact IT support", error)
    finally:
        # Disconnects database
        database.close()

def add_book(title, author, qty):
    """ Adds a new row into the books table

        Keyword arguments:
            title   --str, - Book title
            author  --str, - Book author
            qty     --int, - Quantity
    """
    try:
        # Connects to the database
        database = sqlite3.connect("books.db")
        cursor = database.cursor()
        # Inserts the new book into the database
        cursor.execute('''INSERT INTO books (title, author, qty) 
                            VALUES (?, ?, ?)''', 
                            (title, author, qty))
        # Updates database
        database.commit()
        # Retrieves and displays a newly added book from the database
        cursor.execute('''SELECT * FROM books 
                            ORDER BY id 
                            DESC LIMIT 1''')
        result = cursor.fetchall()
        print("Book added successfully.\n")
        print(tabulate(result, 
                        headers=['ID', 'Title', 'Author', 'Qty'], 
                        tablefmt='fancy_grid'))
    # Catches database exeption 
    except sqlite3.ProgrammingError as error:
        print(f"Programming Error occured, "
                f"please contact IT support", error)
    except sqlite3.OperationalError as error:
        print(f"Unexpected Error in the database, "
                f"please contact IT support", error)
    except sqlite3.DataError as error: 
        print(f"Data processing error",
                f"please contact IT support", error)
    finally:
        # Disconnects database
        database.close()

def update_book(id, qty):
    """Updates book's quantity in the database
    
        Keyword arguments:
            id      --int, - Unique book ID
            qty     --int, - Quantity

    """
    try: 
        # Connects to the database
        database = sqlite3.connect("books.db")
        cursor = database.cursor()
        # Inserts new quanity value into the database
        cursor.execute('''UPDATE books
                            SET qty=?
                            WHERE id=?''', 
                            (qty, id))
        # Updates database
        database.commit()
        print("Book updated successfully.\n")
        # Retrieves and displays the updated row from the database
        cursor.execute('''SELECT * FROM books 
                            WHERE id=?''', (id,))
        result = cursor.fetchone()
        if result:
            print(tabulate([result], 
                            headers=['ID', 'Title', 'Author', 'Qty'], 
                            tablefmt='fancy_grid'))
    # Catches database exeption 
    except sqlite3.ProgrammingError as error:
        print(f"Programming Error occured, "
                f"please contact IT support", error)
    except sqlite3.OperationalError as error:
        print(f"Unexpected Error in the database, "
                f"please contact IT support", error)
    except sqlite3.DataError as error: 
        print(f"Data processing error",
                f"please contact IT support", error)
    finally:
        # Disconnects database
        database.close()

def remove_book(id):
    """Removes book from the table
    
        Keyword arguments:
            id      --int, - Unique book ID

    """
    try:
        # Connects to the database
        database = sqlite3.connect("books.db")
        cursor = database.cursor()
        # Deletes specific row in database table
        cursor.execute("DELETE FROM books WHERE id=?", (id,))
        database.commit()
        print("Book removed successfully.\n")
        # Disconnects database
    # Catches database exeption 
    except sqlite3.ProgrammingError as error:
        print(f"Programming Error occured, "
                f"please contact IT support", error)
    except sqlite3.OperationalError as error:
        print(f"Unexpected Error in the database, "
                f"please contact IT support", error)
    except sqlite3.DataError as error: 
        print(f"Data processing error",
                f"please contact IT support", error)
    finally:
        # Disconnects database
        database.close()

def search_book(id):
    """Finds specific book in database table
    
        Keyword arguments:
            id      --int, - Unique book ID

    """
    try:
        # Connects to the database
        database = sqlite3.connect("books.db")
        cursor = database.cursor()
        # Retrieves and displays a book from the database
        cursor.execute('''SELECT * FROM books 
                            WHERE id=?''', (id,))
        result = cursor.fetchone()
        if result:
            print(tabulate([result], 
                            headers=['ID', 'Title', 'Author', 'Qty'], 
                            tablefmt='fancy_grid'))
        else:
            print("Book not found.\n")
    # Catches database exeption 
    except sqlite3.ProgrammingError as error:
        print(f"Programming Error occured, "
                f"please contact IT support", error)
    except sqlite3.OperationalError as error:
        print(f"Unexpected Error in the database, "
                f"please contact IT support", error)
    except sqlite3.DataError as error: 
        print(f"Data processing error",
                f"please contact IT support", error)
    finally:
        # Disconnects database
        database.close()

def list_all_books():
    """ Finds and displays all books stored in 
        the database table

        Keyword arguments: None
    """
    try: 
        # Connects to the database
        database = sqlite3.connect("books.db")
        cursor = database.cursor()
        # Retrieves and displays all rows from the database table
        cursor.execute("SELECT * FROM books")
        result = cursor.fetchall()
        if result:
            print(tabulate(result, 
                            headers=['ID', 'Title', 'Author', 'Qty'], 
                            tablefmt='fancy_grid'))
        else:
            print("Books not found. Please contact IT support\n")
    # Catches database exeption 
    except sqlite3.ProgrammingError as error:
        print(f"Programming Error occured, "
                f"please contact IT support", error)
    except sqlite3.OperationalError as error:
        print(f"Unexpected Error in the database, "
                f"please contact IT support", error)
    except sqlite3.DataError as error: 
        print(f"Data processing error",
                f"please contact IT support", error)
    finally:
        # Disconnects database
        database.close()

def menu():
    """ Displays user navigation menu, reads user input
        and calls one of the functions:

            1 = add_book(title, author, qty),
            2 = update_book(id, qty),
            3 = remove_book(id),
            4 = search_book(id),
            5 = list_all_books()

        Keyword arguments: None
    """
    while True:
        try:
            # Displays menu
            print(f"\nHyperonDev - Software Enigneering Bootcamp "
                    f"\nCapstone Project - Task 48 \n"
                    f"\nBook Management Program (Alex Pelsis, 2023 ©)\n"
                    f"\n1. Add book"
                    f"\n2. Update book"
                    f"\n3. Remove book"
                    f"\n4. Search book"
                    f"\n5. List all books"
                    f"\n0. Exit")
            # Declares user input into a variable and 
            # perfroms conditional & inapropriate arguments checks
            choice = int(input("\nEnter your choice: "))
            if choice == 1:
                title = input("Enter title: ")
                author = input("Enter author: ").title()
                qty = input("Enter quantity: ")
                try:
                    qty = int(qty)
                # Checks for datatype mismatch
                except ValueError:
                    print(f"Quantity must be an integer. "
                            f"Please enter a valid quantity.")
                    continue
                # Calls the function to add a new row 
                # into database table
                add_book(title, author, qty)
            elif choice == 2:
                id = input("Enter ID: ")
                try:
                    id = int(id)
                # Checks for datatype mismatch
                except ValueError:
                    print(f"ID must be an integer. "
                            f"Please enter a valid ID.")
                    continue
                qty = input("Enter quantity: ")
                try:
                    qty = int(qty)
                # Checks for datatype mismatch
                except ValueError:
                    print(f"Quantity must be an integer. "
                            f"Please enter a valid quantity.")
                    continue
                # Calls the function amend the row
                # in the database table
                update_book(id, qty)
            elif choice == 3:
                id = input("Enter ID: ")
                try:
                    id = int(id)
                # Checks for datatype mismatch
                except ValueError:
                    print(f"ID must be an integer. "
                            f"Please enter a valid ID.")
                    continue
                # Calls the function delete the row
                # in the database table
                remove_book(id)
            elif choice == 4:
                id = input("Enter ID: ")
                try:
                    id = int(id)
                # Checks for datatype mismatch
                except ValueError:
                    print(f"ID must be an integer. "
                            f"Please enter a valid ID.")
                    continue
                # Calls the function to look and retrun
                # a specifc row from the database table
                search_book(id)
            elif choice == 5: 
                # Calls the function to look and retrun
                # all rows from the database table
                list_all_books()
                continue
            # Exits program
            elif choice == 0:
                break
            else:
                print(f"Invalid choice. "
                        f"Please enter a valid choice.")
        # Checks for hard escape 'Ctrl + C'
        except KeyboardInterrupt:
            print(f"\nInvalid input, "
                    f"please select option \'0\'to exit the program")
# Calls function to create/check table
create_table()
# Calls user menu
menu()

##################################### END ######################################
