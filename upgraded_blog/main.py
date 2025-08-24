import json
from flask import Flask
from flask import render_template, request
import smtplib
import os
from dotenv import load_dotenv

load_dotenv("./.env")

EMAIL = os.getenv("BOT_MAIL")
PASSWORD = os.getenv("PASSWORD")

app = Flask(__name__)


with open("./static/blog_posts.json", 'r') as file:
        posts = json.load(file)

@app.route("/")
def home():
    return render_template("index.html", posts = posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=['GET','POST'])
def contact():
    if request.method == "POST":
        feedback_name = request.form['name']
        feedback_mail = request.form['mail']
        feedback_phone = request.form['phone']
        feedback_message = request.form['message']
        #Sending the data in mail
        subject = "New Message from Your Website"
        email_content = f"Subject: {subject}\n\nName: {feedback_name}\n\nEmail: {feedback_mail}\n\nPhone: {feedback_phone}\n\nMessage: {feedback_message}"
        try:
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=EMAIL, password=PASSWORD)
                connection.sendmail(
                    from_addr=EMAIL,
                    to_addrs="aymen27k@gmail.com",
                    msg=email_content.encode('utf-8')
                )
            print("Mail sent to => aymen27k@gmail.com")
        except Exception as e:
            print(f"An error occurred while sending the email: {e}")
        return render_template('contact.html')
        
    return render_template("contact.html")

@app.route("/post/<int:index>")
def show_post(index):
    for post in posts:
        if post['id'] == index:
            return render_template("post.html", post=post)
    return render_template('notfound.html')


if __name__ == "__main__":
    app.run(debug=True)