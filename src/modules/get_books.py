import os
import sys
from classes.Book import Book

def get_book_name_authors(line, md_file_path):
    is_favorite = line.strip().endswith('*')
    try:
        book_name, authors = line.strip('*#\n').split('/')
        authors = [author.strip() for author in authors.split('&')]
    except ValueError:
        print(f'Wrong format in book header -> {line.strip()} in {md_file_path}')
        print('The format should be book_name/author1 & author2 & authorn')
        sys.exit(1)
    return book_name, authors, is_favorite

def get_md_file_content(md_file_path):
    year = md_file_path.split('/')[-1].split('.')[0] # md name: year.md
    if len(year) != 4 or not year.isdigit():
        sys.exit(f'{md_file_path} file name is in the wrong format')
    with open(md_file_path, 'r', encoding="utf-8") as fhandle:
        lines = [line for line in fhandle if line.strip()]
    assert lines, (f'{md_file_path} is empty')
    return lines, year

def read_md_file(md_file_path):
    books = []
    lines, year = get_md_file_content(md_file_path)
    in_code_block = False
    for line in lines:
        line = line.rstrip()
        if line.lstrip().startswith('```'):
            in_code_block = not in_code_block
        if in_code_block:
            books[-1].add_text_to_last_quote(line)
            continue
        if line.startswith('#'): # book title
            book_id = f'{year[-2:]}-{len(books)+1}'
            book_name, authors, is_favorite = get_book_name_authors(line, md_file_path)
            books.append(Book(book_id, book_name, authors, year, is_favorite))
        elif line.startswith('[') and line.endswith(']') and line != '[]':
            books[-1].add_tags(line)
        elif line.startswith('*'): # new quote starts
            books[-1].add_quote(line.lstrip('* '))
        else:
            books[-1].add_text_to_last_quote(line)
    return books

def get_books(quotes_dir_path):
    quotes_files_paths = sorted([os.path.join(quotes_dir_path, xfile) for xfile in os.listdir(quotes_dir_path) if xfile.endswith('.md')])
    books = [book for md_file_path in quotes_files_paths for book in read_md_file(md_file_path)]
    if not books:
        sys.exit('No quotes found')
    return books
