import json
from pprint import pprint

import requests

address = "http://127.0.0.1:5000"
headers = {"content-type": "application/json"}


def get_books():
    return requests.get(f"{address}/books", headers=headers).json()


def get_book_by_isbn(isbn):
    return requests.get(url=f"{address}/books/{isbn}", headers=headers).json()


def add_book(isbn, author, title, year):
    book = {"isbn": isbn, "author": author, "title": title, "year": year}
    return requests.post(
        url=f"{address}/books", headers=headers, data=json.dumps(book)
    ).json()


def edit_a_book(isbn, author, title, year):
    book = {"author": author, "title": title, "year": year}
    return requests.put(
        url=f"{address}/books/{isbn}", headers=headers, data=json.dumps(book)
    ).json()


def delete_a_book(isbn):
    return requests.delete(url=f"{address}/books/{isbn}", headers=headers).json()


if __name__ == "__main__":
    pprint("All books")
    pprint(get_books())

    print()
    pprint("Get a specific book by isbn")
    pprint(get_book_by_isbn("9786589711452"))

    print()
    pprint("Add a book")
    isbn = "21232"
    new_book = add_book(
        isbn=isbn, author="Arthur", title="How to learn code", year=2023
    )
    pprint(new_book)

    pprint("Edit a book")  # let us edit the book above
    edited_book = edit_a_book(
        isbn=isbn, author="Arthur Kalule", title="API simplified", year=2022
    )
    pprint(edited_book)

    pprint("Delete a book")  # we can delete Things fall apart isbn 9780435272463
    isbn = "9780435272463"
    pprint(delete_a_book("9780435272463"))

    # Let's confirm by fetching a deleted book, we expect an empty response
    book = get_book_by_isbn(isbn)
    pprint(book)
