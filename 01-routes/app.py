import json

from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__) 

postsDatastore =  {
    "posts": [
    {
      "id": 0,
      "upvotes": 1,
      "title": "My cat is the cutest!",
      "link": "https://i.imgur.com/jseZqNK.jpg",
      "username": "alicia98",
    },
    {
      "id": 1,
      "upvotes": 3,
      "title": "Cat loaf",
      "link": "https://i.imgur.com/TJ46wX4.jpg",
      "username": "alicia98",
    },
    ]
}

idGenerator = 2



@app.route('/')
def index():
    return "Hello, world!"

@app.route("/api/posts/")
def getPosts():
    """
        Retrieve all posts.
    """
    return jsonify(postsDatastore)

@app.route("/api/posts/<int:id>/")
def getPostById(id):
    """
        Get a single post by id.
    """
    posts = [*filter(lambda x: x['id'] == id, postsDatastore['posts'])]
    return jsonify(posts[0])

@app.route("/api/posts/", methods=["POST"])
def createPost():
    """
        Create a new post.
    """
    data = json.loads(request.data)
    post_id = postsDatastore["posts"][-1]["id"] +  1
    post = {"id": post_id, **data}
    postsDatastore['posts'].append(post)
    return jsonify(post)








if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8889, debug=True)
