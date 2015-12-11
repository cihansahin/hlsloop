from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    print "I am in hello..",
    return "Hello 2 World!!"


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
