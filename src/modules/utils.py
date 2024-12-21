import os
import sys
import argparse

def get_quotes_dir_path():
    quotes_dir_path = os.environ.get('bookquotes')
    if quotes_dir_path is None:
        print('bookquotes env var not configured.')
        sys.exit(1)
    return quotes_dir_path

def get_args():
    parser = argparse.ArgumentParser(prog='book_quotes', description='Manage your book quotes')
    parser.add_argument('-b', '-books', metavar='', dest='show_books', help='search books by book id, book name, author, tag or reading year ("all" to show all books / "favs" to show favorites) [query]')
    parser.add_argument('-q', '-quotes', metavar='', dest='search_quotes', help='search quotes by a query word [query]')
    parser.add_argument('-a', '-authors', action='store_true', dest='show_authors', help='show authors table')
    parser.add_argument('-t', '-tags', action='store_true', dest='show_tags', help='show tags table')
    parser.add_argument('-f', '-format', action='store_true', dest='show_format', help='show md files format')
    args = parser.parse_args()
    if args.show_format:
        print_format_help()
        sys.exit()
    if not any([args.show_books, args.search_quotes, args.show_authors, args.show_tags]):
        parser.print_help()
        sys.exit()
    return args

def print_format_help():
    print(
    '''Each year should have a different markdown file, with the YYYY.md format.
The .md files have to have the following format:

    #Book Name/Book Author
    [tag1,tag2,tag3,...,tagn]

    * Quote 1.
      Here you can write your quote.
      You can use more than one line per quote, a new quote only begins with "*"
    * Quote 2. You can write as many quotes as you want.

Book tags are optional.
To mark a book as favorite, write an * at the end of the title line.

    #Favorite Book Name/Book Author*

If a book has multiple authors, use & to separate them.

    #Book Name/Author 1 & Author 2
    '''
    )
