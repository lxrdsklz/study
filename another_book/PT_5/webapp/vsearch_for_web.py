from flask import Flask, render_template, request
from vsearch import search_for_letters

app = Flask(__name__)


@app.route('/search_for', methods=['POST'])
def do_search() -> 'hmtl':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Ваши результаты: '
    results = str(search_for_letters(phrase,
                                     letters))
    return render_template('results.html',
                           the_phrase=phrase,
                           the_title=title,
                           the_letters=letters,
                           the_results=results,)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Поиск букв в слове',)

if __name__ == '__main__':
    app.run(port=80, host='localhost', debug=True)