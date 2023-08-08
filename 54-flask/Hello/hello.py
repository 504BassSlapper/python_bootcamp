from flask import Flask

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

if __name__ =="__main__":
    app.run(debug=True)