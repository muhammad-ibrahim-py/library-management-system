import json
from pathlib import Path

# ============================================================
# CLASS 1: Book
# ============================================================

class Book:
    def __init__(self, title: str, book_number: int, author: str) -> None:
        self.title = title
        self.book_number = book_number
        self.author = author
    
    def info(self) -> None:
        print(f"Title: {self.title}")
        print(f"Book Number: {self.book_number}")
        print(f"Author: {self.author}")


# ============================================================
# CLASS 2: Library
# ============================================================

class Library:
    def __init__(self) -> None:
        self.books: list = []
    
    def add_book(self, book: Book) -> None:
        self.books.append(book)
    
    def show_all(self) -> None:
        for book in self.books:
            book.info()
            print()
    
    def total_books(self) -> int:
        return len(self.books)
    
    def number_exists(self, book_number: int) -> bool:
        for book in self.books:
            if book.book_number == book_number:
                return True
        return False
    
    def search_by_number(self, book_number: int) -> Book | None:
        for book in self.books:
            if book.book_number == book_number:
                return book
        return None
    
    def update_book(self, title: str, book_number: int, author: str) -> bool:
        book: Book | None = self.search_by_number(book_number)
        if book is not None:
            book.title = title
            book.author = author
            return True
        return False
    
    def delete_book(self, book_number: int) -> bool:
        book: Book | None = self.search_by_number(book_number)
        if book is not None:
            self.books.remove(book)
            return True
        return False
    
    def save_to_file(self) -> None:
        data: list = []
        for book in self.books:
            data.append({
                "title": book.title,
                "book_number": book.book_number,
                "author": book.author
            })
        with open("library.json", "w") as file:
            json.dump(data, file, indent=4)
    
    def load_from_file(self) -> None:
        if Path("library.json").exists():
            with open("library.json", "r") as file:
                data: list = json.load(file)
                for item in data:
                    book: Book = Book(
                        item["title"],
                        item["book_number"],
                        item["author"]
                    )
                    self.books.append(book)


# ============================================================
# INPUT VALIDATION FUNCTIONS
# ============================================================

def get_int_input(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


# ============================================================
# MENU FUNCTION
# ============================================================

def show_menu() -> None:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. View All Books")
    print("3. Search Book")
    print("4. Update Book")
    print("5. Delete Book")
    print("6. Total Books")
    print("7. Save & Exit")
    print("=====================================")


# ============================================================
# MAIN FUNCTION
# ============================================================

def main() -> None:
    library: Library = Library()
    library.load_from_file()
    
    while True:
        show_menu()
        choice: int = get_int_input("Enter your choice (1-7): ")
        
        # ---------- Choice 1: Add Book ----------
        if choice == 1:
            title: str = input("Enter book title: ")
            book_number: int = get_int_input("Enter book number: ")
            author: str = input("Enter author name: ")
            
            if library.number_exists(book_number):
                print("Error: Book number already exists.")
            else:
                book: Book = Book(title, book_number, author)
                library.add_book(book)
                print("Book added successfully.")
        
        # ---------- Choice 2: View All ----------
        elif choice == 2:
            if library.total_books() == 0:
                print("No books found.")
            else:
                library.show_all()
        
        # ---------- Choice 3: Search ----------
        elif choice == 3:
            book_number: int = get_int_input("Enter book number to search: ")
            book: Book | None = library.search_by_number(book_number)
            if book is not None:
                book.info()
            else:
                print("Book not found.")
        
        # ---------- Choice 4: Update ----------
        elif choice == 4:
            book_number: int = get_int_input("Enter book number to update: ")
            if library.number_exists(book_number):
                title: str = input("Enter new title: ")
                author: str = input("Enter new author: ")
                library.update_book(title, book_number, author)
                print("Book updated successfully.")
            else:
                print("Book not found.")
        
        # ---------- Choice 5: Delete ----------
        elif choice == 5:
            book_number: int = get_int_input("Enter book number to delete: ")
            if library.delete_book(book_number):
                print("Book deleted successfully.")
            else:
                print("Book not found.")
        
        # ---------- Choice 6: Total ----------
        elif choice == 6:
            print(f"Total books: {library.total_books()}")
        
        # ---------- Choice 7: Save & Exit ----------
        elif choice == 7:
            library.save_to_file()
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice.")


# ============================================================
# ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()