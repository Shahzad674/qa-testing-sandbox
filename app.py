from flask import Flask, jsonify, request

app = Flask(__name__)

# Hardcoded data for testing
books = [
    {"id": 1, "title": "The Hobbit", "author": "J.R.R. Tolkien"},
    {"id": 2, "title": "1984", "author": "George Orwell"}
]

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books), 200

@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({"error": "Bad Request - Title is required"}), 400
        
    new_book = {
        "id": len(books) + 1,
        "title": data['title'],
        "author": data.get('author', 'Unknown')
    }
    books.append(new_book)
    return jsonify(new_book), 201

if __name__ == '__main__':
    app.run(debug=True)