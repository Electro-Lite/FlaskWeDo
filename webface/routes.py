from . import app
@app.route("/")

def index ():
    return "toto je Index"