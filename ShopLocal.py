import flask, csv

app = flask.Flask(__name__)

businesses_file = open('./data/business.licences.csv', encoding="latin1")
businesses = csv.DictReader(businesses_file)
    

@app.route('/')
def index():
    return flask.render_template("index.html", businesses=businesses)
    businesses_file.close()
