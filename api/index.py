from flask import *


app = Flask(__name__)



# Index Page
@app.route("/")
def index():
    return render_template("index.html")





if __name__ == "__main__":
    app.run(debug=True)



# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return 'Hello, World!'

# @app.route('/about')
# def about():
#     return 'About'
