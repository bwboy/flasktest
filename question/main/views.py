from flask import render_template,session,redirect,url_for,request
from . import main


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/post',methods=['get','POST'])
def post():
    return request.get_data()