from flask import Flask
from markupsafe import escape

app = Flask(__name__)
print(app)

@app.route('/')
def hello():
    return "hello"

@app.route("/bye/<user>")
def bye(user):
    return f"bye {user}"

@app.route("/username/<string:name>/<int:number>")
def description(name, number ):
    if number > 2:
        return f"hello {name} you are the  {number} th client "
    elif number == 2:
        return f"hello {name} you are the {number} nd client "
    elif number == 1:
        return f"hello {name} you are the {number} st client <3"
    else: 
        return f"hello {name}"

@app.route("/path/<path:link>")
def where_is_your_workspace(link):
    return f" workspace located at {escape(link)}"

if __name__ =="__main__":
    app.run(debug=True)