from flask import Flask
from flask.ext.cors import CORS
from getcode import Cells
from cors_decorator import crossdomain

app = Flask(__name__)
# CORS(app)

@app.route("/")
@crossdomain(origin='*')
def hello():
    cells = Cells()
    return cells.getCells()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
