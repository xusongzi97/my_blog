from flask import Flask, render_template
# from flask_admin import Admin
from controller.user import user

app = Flask(__name__)
app.register_blueprint(user)
# admin = Admin(app)


@app.route('/')
def hello_world():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')