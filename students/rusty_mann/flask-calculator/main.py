import os
import base64

from flask import Flask, render_template, request, redirect, url_for, session

from model import SavedTotal

app = Flask(__name__)
app.secret_key = b'\\\xf1A\x88f\x1a@6\x1d\xa2\xc8J\xfc\x9e\x9c1\x86p\x04\xc1\xc7\xc7\x03\xfd\xbd'

@app.route('/add', methods=['GET', 'POST'])
def add():
    # session['total']

    if 'total' not in session:
        session['total'] = 0

    if request.method == 'POST':
        number = int(request.form['number'])
        session['total'] += number

    return render_template('add.jinja2', session=session)

@app.route('/save', methods=['POST'])
def save():
    total = session.get('total', 0)
    code = base64.b32encode(os.urandom(8)).decode().strip("=")
#    print(total)
#    print(code)
    saved_total = SavedTotal(value=total, code=code)
    print(saved_total.value)
    print(saved_total.code)
    saved_total.save()

    return render_template('save.jinja2')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
#    app.debug = True
    app.run(host='0.0.0.0', port=port)
