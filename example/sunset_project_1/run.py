"""
created by seven 2018/11/01
"""

from flask import Flask

app = Flask(__name__)

@app.route('')
def index():
    return '1'

if __name__ == '__main__':
    app.run(debug=True)
