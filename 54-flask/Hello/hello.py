from flask import Flask

app = Flask(__name__)
print(app)

@app.route('/')
def hello():
    return "hello"

@app.route("/bye/<user>")
def bye(user):
    return f"bye {user}"

if __name__ =="__main__":
    app.run(debug=True)