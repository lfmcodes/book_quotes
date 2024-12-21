from classes.Quote import Quote

def get_quotes(books, query):
    quotes = [Quote(book.book_name, book.authors, quote) for book in books for quote in book.quotes if query in quote.quote]
    return quotes
