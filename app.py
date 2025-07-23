from flask import render_template

@app.route('/')
def todo_form():
    return render_template('index.html')
