from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/api_value")
def return_x():
    x={'key1':[0,1,1,0,0]}
    return jsonify(x)


if __name__ == "__main__":
    app.run()