from flask import Flask
from flask import render_template, request, redirect, session, flash, abort
import config
import os

app = Flask(__name__)
app.secret_key = config.SECRET_KEY

