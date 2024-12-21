from classes.Quote import Quote

class Book:
    def __init__(self, book_id, book_name, authors, reading_year, is_favorite):
        self.book_id = book_id
        self.book_name = book_name
        self.authors = authors
        self.str_authors = (' & ').join(self.authors)
        self.reading_year = reading_year
        self.is_favorite = is_favorite
        self.quotes = []
        self.tags = []

    def add_quote(self, text):
        self.quotes.append(Quote(self.book_name, self.authors, text))

    def add_text_to_last_quote(self, text):
        self.quotes[-1].add_text(text)

    def add_tags(self, tags_line):
        self.tags = [tag.strip() for tag in tags_line.lower().strip('[]\n').split(',')]

    def __repr__(self):
        return f'{self.book_id} {self.book_name} {self.str_authors}'
