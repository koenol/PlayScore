"""Web application initialization"""

from flask import Flask, render_template, request, redirect, session, flash, abort
import config

app = Flask(__name__)
app.secret_key = config.SECRET_KEY
