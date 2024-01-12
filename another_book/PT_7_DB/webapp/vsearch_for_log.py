from flask import Flask, render_template, request, escape
from vsearch import search_for_letters
import mariadb

app = Flask(__name__)


def log_request(req: 'flask_request', res: str) -> None:
    """Журналирует веб-запрос и возвращает результаты"""
    dbconfig = {
        'host': '127.0.0.1',
        'user': 'vsrch',
        'password': 'pswd',
        'database': 'vsearchlogDB'
    }

    conn = mariadb.connect(**dbconfig)
    cursor = conn.cursor()

    _SQL = """insert into log (phrase, letters, ip, browser_string, results) values (%s, %s, %s, %s, %s)"""
    cursor.execute(_SQL,
                   (req.form['phrase'],
                    req.form['letters'],
                    req.remote_addr,
                    req.user_agent.browser,
                    res,))

    conn.commit()

    # _SQL = """select * from log"""
    #
    # cursor.execute(_SQL)
    #
    # for row in cursor.fetchall():
    #     print(row)

    cursor.close()
    conn.close()


@app.route('/search_for', methods=['POST'])
def do_search() -> 'hmtl':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Ваши результаты: '
    results = str(search_for_letters(phrase, letters))
    log_request(request, results)
    return render_template('results.html',
                           the_phrase=phrase,
                           the_title=title,
                           the_letters=letters,
                           the_results=results, )


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Поиск букв в слове', )


@app.route('/viewlog')
def view_the_log() -> 'html':
    contents = []
    with open('vsearch.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles = ('Form Data', 'Remote addr', 'User agent', 'Results')
    return render_template('viewlog.html',
                           the_title='View log',
                           the_row_titles=titles,
                           the_data=contents)


if __name__ == '__main__':
    app.run(port=80, host='localhost', debug=True)
