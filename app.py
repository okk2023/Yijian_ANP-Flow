from flask import Flask, render_template
from backend import app_exploration, app_simulation, app_compilation

app = Flask(__name__)

app.register_blueprint(app_exploration.blueprint, url_prefix='/exploration')
app.register_blueprint(app_simulation.blueprint, url_prefix='/simulation')
app.register_blueprint(app_compilation.blueprint, url_prefix='/compilation')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chiselAsync')
def chisel_async_page():
    return render_template('chiselAsync.html')

@app.route('/help')
def help_page():
    return render_template('help.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
