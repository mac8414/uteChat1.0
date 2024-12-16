from flask import Flask, render_template, request
from flask_socketio import SocketIO, send
from methods import parse_input, display_answers
from models import KeyWord, Sport
from crud import get_db, get_keywords, get_sports
from dataBase import init_db

app = Flask(__name__)

@app.before_request
def setup_database():
    init_db()

@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/query")
def query():
    search_query = request.args.get('search')
    keyword = parse_input(search_query)
    answers = display_answers(keyword)
    return render_template("query.html", query=search_query, answers=answers)

@app.route("/account-reps")
def accountrep():
    return render_template("account_reps.html")
