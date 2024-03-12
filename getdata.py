from data.users import User
from data.jobs import Jobs
from data.db_session import global_init, create_session
import argparse
from data import db_session
from flask import Flask, render_template

app = Flask(__name__)




if __name__ == '__main__':
    global_init("db/blogs.db")
    app.run(host='127.0.0.1', port=8080, debug=Flask)
