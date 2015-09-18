from flask import Flask
# from flask.ext.cors import CORS
from getcode import Cells
from xml_to_json import XTJ
from cors_decorator import crossdomain

app = Flask(__name__)
# CORS(app)

@app.route("/squad")
@crossdomain(origin='*')
def squad():
    cells = Cells()
    content = cells.getCells()
    xtj = XTJ()
    tree = xtj(xtj.CRITERIA_SQUAD, content)
    return tree.render_json()
@app.route("/chapter")
@crossdomain(origin='*')
def chapter():
    cells = Cells()
    content = cells.getCells()
    xtj = XTJ()
    tree =  xtj(xtj.CRITERIA_CHAPTER, content)
    return tree.render_json()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
