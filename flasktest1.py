# 1. import Flask
from flask import Flask, render_template

# 2. Create an app, being sure to pass __name__
app = Flask(__name__, template_folder='.')

# 3. Define what to do when a user hits the index route
@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return "Welcome to my 'Home' page!"

# 4. Define what to do when a user hits the /about route
@app.route("/about")
def thisrouteabout():
    print("Server received request for 'About' page...")
    return "Welcome to my 'About' page!"

@app.route("/well_work")
def about():
    print("Server received request for 'About' page...")
    return render_template('20190322 Well Work Analysis.html')


if __name__ == "__main__":
  app.run(debug=True)
