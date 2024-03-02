from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    bd_sess = db_session.create_session()
    user = User(
        surname='Scott',
        name='Ridley',
        age=21,
        position='captain',
        speciality='research engineer',
        address='module_1',
        email='scott_chief@mars.org'
    )
    bd_sess.add(user)
    user = User(
        surname='LAlalalla',
        name='moorin',
        age=124,
        position='worker',
        speciality='kolonist',
        address='module_1',
        email='lallalalmoorin@mars.org'
    )
    bd_sess.add(user)
    user = User(
        surname='nolg',
        name='milinsky',
        age=98,
        position='worker',
        speciality='kolonist',
        address='module_1',
        email='noolg@mars.org'
    )
    bd_sess.add(user)
    user = User(
        surname='tt',
        name='y',
        age=21,
        position='worker',
        speciality='kolonist',
        address='module_1',
        email='tty@mars.org'
    )
    bd_sess.add(user)
    bd_sess.commit()
    app.run(host='127.0.0.1', port=8080, debug=True)


if __name__ == '__main__':
    main()
