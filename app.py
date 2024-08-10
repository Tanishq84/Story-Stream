from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

blogs = [
    ["Combustion", "Types of different combustion techniques", "Tanishq Som", "Aug 10, 2024"],
    ["Combustion", "Types of different combustion techniques", "Tanishq Som", "Aug 10, 2024"]
]

@app.route("/")
def home():
    return render_template("home.html", blogs=blogs)


@app.route('/add_blog', methods=['GET', 'POST'])
def add_blog():
    if request.method == 'POST':
        title = request.form['title']
        headline = request.form['headline']
        author = request.form['author']
        date = request.form['date']
        blogs.append([title, headline, author, date])
        return redirect(url_for('home'))
    return render_template('add_blog.html')


if __name__ == "__main__":
    app.run(debug=True)