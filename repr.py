class MyClass:
    def __init__(self,title):
        self.title=title
    def __repr__(self):
        return f"Book:{self.title}"
book=MyClass("Book 1")
print(book)