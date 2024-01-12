from flask import Flask, render_template, request, escape, session, copy_current_request_context
from vsearch import search_for_letters
from DBcm import UseDatabase, ConnectionError, CredentialsError, SQLError
import checker
from threading import Thread

app = Flask(__name__)
app.secret_key = 'YouWillNeverGuessMySecretKey'

app.config['dbconfig'] = {
        'host': '127.0.0.1',
        'user': 'vsrch',
        'password': 'pswd',
        'database': 'vsearchlogDB'
    }


@app.route('/search_for', methods=['POST'])
def do_search() -> 'hmtl':
    @copy_current_request_context
    def log_request(req: 'flask_request', res: str) -> None:
        """Журналирует веб-запрос и возвращает результаты"""
        with UseDatabase(app.config['dbconfig']) as cursor:
            _SQL = """
            insert into log
            (phrase, letters, ip, browser_string, results)
            values
            (%s, %s, %s, %s, %s)"""
            cursor.execute(_SQL, (req.form['phrase'],
                                  req.form['letters'],
                                  req.remote_addr,
                                  req.user_agent.browser,
                                  res,))

    """Извлекает данные из веб-запроса; выполняет поиск; возвращает результаты"""
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Ваши результаты: '
    results = str(search_for_letters(phrase, letters))
    try:
        t = Thread(target=log_request, args=(request, results))
        t.start()
    except Exception as err:
        print('***** Logging failed with this error: ', str(err))
    return render_template('results.html',
                           the_phrase=phrase,
                           the_title=title,
                           the_letters=letters,
                           the_results=results, )


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    """Выводит HTML-форму"""
    return render_template('entry.html',
                           the_title='Поиск букв в слове', )


@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'You are now logged in!'


@app.route('/logout')
def do_logout() -> str:
    session.pop('logged_in')
    return 'You are now logged out'


@app.route('/viewlog')
@checker.check_logged_in
def view_the_log() -> 'html':
    """Выводит содержимое файла журнала в виде HTML-таблицы"""
    try:
        with UseDatabase(app.config['dbconfig']) as cursor:
            _SQL = """select
            phrase, letters, ip, browser_string, results
            from
            log"""
            cursor.execute(_SQL)
            contents = cursor.fetchall()
        titles = ('Phrase', 'Letters', 'Remote addr', 'User agent', 'Results')
        return render_template('viewlog.html',
                               the_title='View log',
                               the_row_titles=titles,
                               the_data=contents)
    except ConnectionError as err:
        print('Connection error: ', str(err))
    except CredentialsError as err:
        print('User-id/Password issues. Error: ', str(err))
    except SQLError as err:
        print('Is your query correct? Error: ', str(err))
    except Exception as err:
        print('Something went wrong: ', str(err))


if __name__ == '__main__':
    app.run(port=80, host='localhost', debug=True)
