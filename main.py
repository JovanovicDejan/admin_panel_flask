from flask import Flask, redirect, url_for
from blueprints.employee_blueprint import employee_services
from blueprints.user_blueprint import user_services
from initialization import create_folder

app = Flask(__name__, static_url_path="")
app.config['MAX_CONTENT_LENGTH'] = 50 * 1000 * 1000
app.secret_key = "*"
app.register_blueprint(user_services, url_prefix="/users")
app.register_blueprint(employee_services, url_prefix="/employees")
create_folder()

@app.route('/')
def home():
    return redirect(url_for('user_services.login_page'))



if __name__ == "__main__":
    app.run(debug=True)
