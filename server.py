from flask import Flask, render_template, request, json, jsonify
from main import access

app = Flask(__name__)
app.static_folder = 'ui'


@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/signIn.html')
def signIn():
    return render_template('signIn.html')


@app.route('/register.html')
def register():
    return render_template('register.html')

@app.route('/main_menu.html')
def menu():
    return render_template('main_menu.html')


@app.route('/signIn.html', methods=['POST'])
def submit_data():
    if request.method == 'POST':
        user = request.form.get('user')
        password = request.form.get('pass')
        # Process the data (e.g., save to a database)
        credentials = [user, password]
        access(credentials[0], credentials[1])

        # Return a response (if needed)
        response_data = {'message': 'Data received successfully'}
        # = [user, password]
        # return json.dumps(credentials)
        return credentials

    else:
        return 'Invalid request method'


if __name__ == '__main__':
    app.run(debug=True, port=8080)
