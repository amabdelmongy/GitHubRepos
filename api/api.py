import flask
from flask import request, jsonify, Flask
import lorem
import random
from flask_cors import CORS

app = flask.Flask(__name__)
app.config["DEBUG"] = True
CORS(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Api</h1>
<p>Mock https://api.github.com/users/torvalds/repos</p>'''


# A route to return all of the available entries in our catalog.
@app.route('/users/<username>/repos', methods=['GET'])
def api_all(username):
    books = []
    length  = random.randrange(3, 12)
    for x in range(length):
        books.extend([
        {'id': x+1,
         'name': lorem.sentence(),
         'html_url': "https://www.google.com/search?q="+lorem.sentence(),
         'description': lorem.paragraph()
         }])
    return jsonify(books)

app.run()
