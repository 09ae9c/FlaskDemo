from flask import Flask
from . import main

@main.route('/',methods=['GET','POST'])
def index():
    return 'hello flask'
