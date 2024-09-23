from flask import Flask, render_template, request, redirect, url_for

# Step 1: Initialize Flask app
appLogin = Flask(__name__)
print(appLogin)

# Step 2: Create a route for the login page
@appLogin.route('/')
def login():
    return render_template('login.html')

# Step 3: Create a route to handle the login form submission
@appLogin.route('/login', methods=['POST'])
def handle_login():
    username = request.form['username']
    password = request.form['password']

    # Step 4: Simple username and password authentication
    if username == "admin" and password == "password":
        # return f"Welcome, {username}!"
        return redirect(url_for('show_dashboard'))
    else:
        return "Invalid credentials. Please try again."

@appLogin.route('/dashboard')
def show_dashboard():
    return render_template("dashboard.html")


# Step 5: Run the Flask app
if __name__ == '__main__':
    appLogin.run(debug=True)
