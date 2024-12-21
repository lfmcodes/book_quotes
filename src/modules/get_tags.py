def get_tags(books):
    tag_list = [tag for book in books for tag in book.tags]
    tags = {tag: tag_list.count(tag) for tag in set(tag_list)}
    return tags
