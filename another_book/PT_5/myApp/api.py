from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def entryPage():
    return render_template('base.html')


@app.route('/return', methods=['POST'])
def returnPage():
    return render_template('result.html')


app.run(debug=True, host='localhost', port=80)