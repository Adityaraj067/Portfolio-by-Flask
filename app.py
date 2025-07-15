from flask import Flask, render_template, request, redirect, url_for
import json
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    with open('data/experience.json') as f:
        experience = json.load(f)
    return render_template('index.html', experience=experience)

@app.route('/projects')
def projects():
    with open('data/projects.json') as f:
        projects = json.load(f)
    return render_template('projects.html', projects=projects)
@app.route('/certifications')
def certifications():
    return render_template('certifications.html')

@app.route("/skills")
def skills():
    return render_template("skills.html")

@app.route('/education')
def education():
    return render_template('education.html')


@app.route('/blog')
def blog():
    with open('data/blog.json') as f:
        blog_posts = json.load(f)
    return render_template('blog.html', posts=blog_posts)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        with open("contact_submissions.txt", "a") as f:
            f.write(f"{datetime.now()} | {name} | {email} | {message}\n")
        return redirect(url_for('contact'))
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
