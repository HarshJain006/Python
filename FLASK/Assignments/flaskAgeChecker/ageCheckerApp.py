from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    # Render the home page with a button to start age checking
    return render_template('home.html')

@app.route('/check_age')
def age_form():
    # Render the form to input name and age
    return render_template('age_form.html')

@app.route('/result', methods=['POST'])
def result():
    # Get name and age from the form
    name = request.form['name']
    age = int(request.form['age'])

    # Determine if the user is an adult or minor
    if age >= 18:
        message = f"Hello {name}, you are an adult."
    else:
        message = f"Hello {name}, you are a minor."

    # Render the result page with the message
    return render_template('result.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
