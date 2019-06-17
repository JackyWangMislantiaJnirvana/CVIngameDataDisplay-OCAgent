from flask import *

from server import auth
from server import dashboard_manager
from server import users
from server.database import close_database

app = Flask(__name__)
app.config.from_pyfile('config.py')

print(app.config['DATABASE'])

# blueprint
app.register_blueprint(auth.bp)
app.register_blueprint(users.bp)
app.register_blueprint(dashboard_manager.bp)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.teardown_appcontext(close_database)
    app.run(debug=True)  # TODO: DELETE BEFORE DEPLOYMENT
