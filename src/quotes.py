#!/usr/bin/python3
import sys
from modules import print_entries
from modules import utils
from modules import backup
from modules.get_books import get_books
from modules.get_authors import get_authors
from modules.filter_books import filter_books
from modules.get_quotes import get_quotes
from modules.get_tags import get_tags

def main():
    args = utils.get_args()
    quotes_dir_path = utils.get_quotes_dir_path()
    backup.check_file_integrity(quotes_dir_path)
    books = get_books(quotes_dir_path)

    #! SEARCH BOOKS
    if args.show_books:
        query = args.show_books.casefold()
        filtered_books = filter_books(books, query)
        if len(filtered_books) == 1:
            print_entries.print_book_quotes_markdown(filtered_books[0])
        elif len(filtered_books) > 1:
            print_entries.print_books_table(filtered_books)
        else:
            sys.exit('No books found.')

    #! SEARCH QUOTES
    elif args.search_quotes:
        query = args.search_quotes.casefold()
        quotes = get_quotes(books, query)
        if not quotes:
            sys.exit('No quotes found.')
        print_entries.print_quotes_markdown(quotes)

    #! PRINT AUTHORS TABLE
    elif args.show_authors:
        authors = get_authors(books)
        print_entries.print_authors_table(authors)

    #! PRINT TAGS TABLE
    elif args.show_tags:
        tags = get_tags(books)
        print_entries.print_tags_table(tags)

if __name__ == '__main__':
    main()
