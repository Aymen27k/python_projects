class Book:
    def __init__(self, title, author, page_count):
        self.title = title
        self.author = author
        self.page_count = page_count

    def read_page(self):
        print(f"Reading pages from the book {self.title}, wrote by {self.author}")


book1 = Book("Python", "Eric Matthews", 544)
book1.read_page()


