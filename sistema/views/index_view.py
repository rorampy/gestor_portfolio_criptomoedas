from flask import render_template
from sistema import app


@app.route('/')
def principal():
    return render_template('index.html')