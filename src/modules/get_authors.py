from classes.Author import Author

def get_authors(books):
    authors = {author: Author(author) for author in set(author for book in books for author in book.authors)}
    for book in books:
        for author in book.authors:
            authors[author].books.append(book)
            authors[author].tags.update(book.tags)

    return sorted(authors.values(), key=lambda author: author.name)
