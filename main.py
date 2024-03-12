from flask import Flask
from data import db_session
from data.users import User
from data.jobs import Jobs
from data.db_session import create_session, global_init
from flask import Flask, render_template
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def add_users(bd_sess) -> None:
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
    a = User(
        surname='LAlalalla',
        name='moorin',
        age=124,
        position='worker',
        speciality='Colonist',
        address='module_1',
        email='lallalalmoorin@mars.org'
    )
    bd_sess.add(a)
    b = User(
        surname='nolg',
        name='milinsky',
        age=98,
        position='worker',
        speciality='Colonist',
        address='module_1',
        email='noolg@mars.org'
    )
    bd_sess.add(b)
    c = User(
        surname='tt',
        name='y',
        age=21,
        position='worker',
        speciality='Colonist',
        address='module_1',
        email='tty@mars.org'
    )
    bd_sess.add(c)


def add_jobs(bd_sess) -> None:
    job1 = Jobs(
        team_leader=1,
        job='deployment of residential modules 1 and 2',
        work_size=15,
        collaborators='2, 3',
        is_finished=False

    )
    bd_sess.add(job1)

@app.route("/")
def index():
    db_sess = create_session()
    works = db_sess.query(Jobs).all()
    return render_template(f"index.html", title="Журнал работ", works=works)

def main():
    db_session.global_init("db/blogs.db")
    bd_sess = db_session.create_session()
    #add_users(bd_sess)
    #add_jobs(bd_sess)
    works = bd_sess.query(Jobs).all()
    bd_sess.commit()
    app.run(host='127.0.0.1', port=8080, debug=True)


if __name__ == '__main__':
    main()
