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
    print "test"
    return cells.getCells()
    # return "Hello"

if __name__ == "__main__":
    app.run()
