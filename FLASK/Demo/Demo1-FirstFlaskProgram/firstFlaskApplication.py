from flask import Flask

app = Flask(__name__)

@app.route('/')  # This route will handle requests to the root URL "/"
def homePage():
    return "Welcome to the homepage!"

if __name__ == '__main__':
    app.run(debug=True)