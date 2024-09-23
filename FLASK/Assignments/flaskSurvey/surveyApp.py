from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    # Render the home page
    return render_template('home.html')

@app.route('/survey')
def survey():
    # Render the survey page with questions
    return render_template('survey.html')

@app.route('/results', methods=['POST'])
def results():
    name = request.form['name']
    favoriteColor = request.form['favorite_color']
    feedback = request.form['feedback']
    return render_template('results.html', name=name, favorite_color=favoriteColor, feedback=feedback)


if __name__ == '__main__':
    app.run(debug=True)
