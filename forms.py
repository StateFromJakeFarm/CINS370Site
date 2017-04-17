from flask import Flask, request, render_template
from wtforms import Form, BooleanField, TextField, StringField, PasswordField, validators

class QueryForm(Form):
    query = TextField('Query', [validators.Required()])
