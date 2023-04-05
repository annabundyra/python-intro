from flask import Flask, jsonify, request

app = Flask(__name__)


@app.get("/books")
# @app.route('/books', methods=["GET"]) # same as above
def get_books():
    return jsonify(books), 200


@app.get("/books/<string:isbn>")
# @app.route('/books/<string:isbn>', methods=["GET"]) # same as above
def get_a_book(isbn):
    index = find_book_index_by_isbn(isbn)
    if index != -1:
        print(f"index {index}")
        return jsonify({"message": "success", "book": books[index]})

    return jsonify({"message": "book does not exist"}), 404


@app.post("/books")
# @app.route('/books', methods=["POST"]) # same as above
def add_book():
    book = request.get_json()
    books.append(book)
    return jsonify({"message": "success", "book": book}), 201


@app.put("/books/<string:isbn>")
# @app.route('/books/<string:isbn>', methods=["PUT"])# the above is the same as this
def update_book(isbn):
    new_book = request.get_json()
    index = find_book_index_by_isbn(isbn)
    if index != -1:
        books[index]["title"] = new_book["title"]
        books[index]["year"] = new_book["year"]
        books[index]["author"] = new_book["author"]

        return jsonify({"message": "Success", "book": books[index]}), 200
    return jsonify({"message": "Error Invalid book isbn"}), 400


# @app.route('/books/<string:isbn>', methods=['DELETE'])
@app.delete("/books/<string:isbn>")
# @app.route('/books/<string:isbn>', methods=["DELETE"]) the above is the same as this
def delete_book(isbn):
    index = find_book_index_by_isbn(isbn)
    if index != -1:
        book = books.pop(index)
        return jsonify({"message": "Success", "book": book}), 200
    return jsonify({"message": "Book does not exist"}), 404


def find_book_index_by_isbn(isbn):
    for index, book in enumerate(books):
        if book["isbn"] == isbn:
            return index
    return -1


books = [
    {
        "author": "Chinua Achebe",
        "title": "Things Fall Apart",
        "year": 1958,
        "isbn": "9780435272463",
    },
    {
        "author": "Jane Austen",
        "title": "Pride and Prejudice",
        "year": 1813,
        "isbn": "9786589711452",
    },
]
if __name__ == "__main__":
    app.run(debug=True, port=5000)
