from flask import Flask, render_template
import requests
from post import Post

response = requests.get("https://jsonplaceholder.typicode.com/posts")
response.raise_for_status()
all_posts = response.json()
posts_obj = []
for post in all_posts:
    post_obj = Post(post['id'], post['title'], post['body'])
    posts_obj.append(post_obj)


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", posts=posts_obj)

@app.route("/post/<int:index>")
def get_post(index):
    requested_post = None
    for post in posts_obj:
        if post.id == index:
            requested_post = post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
