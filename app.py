from flask import Flask
from getcode import Cells
app = Flask(__name__)

@app.route("/")
def hello():
    cells = Cells()
    print "test"
    return cells.getCells()
    # return "Hello"

if __name__ == "__main__":
    app.run()
