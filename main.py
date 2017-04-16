from flask import Flask
import os

app = Flask(__name__, static_url_path='')

@app.route('/', methods=['GET', 'POST'])
def root():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run()
