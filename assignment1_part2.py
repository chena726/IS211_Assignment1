class Book:
    author = ""
    title = ""

    def __init__(self, title, author):        
        self.title = title
        self.author = author

    def display(self):        
        return  self.title+", written by "+self.author

book1 = Book("'Of Mice and Men'","John Steinbeck")
book2 = Book("'To Kill a Mockingbird'","Harper Lee")

print(book1.display())
print(book2.display())    
