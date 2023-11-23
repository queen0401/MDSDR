from flask import Flask
from flask_bootstrap import Bootstrap
from flask import render_template
from settings import config

from Index import app_Index
from Search import app_Search
# from Browse import app_Browser
# from Document import app_Document
# from Contact import app_Contact
# from Download import app_Download

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config.from_object(config['base'])

# Define a custom filter function for 'max'
def custom_max(value, arg):
    return max(value, arg)

# Add the custom filter to the Jinja2 environment of the Flask app
app.jinja_env.filters['max'] = custom_max

app.register_blueprint(app_Index, url_prefix="")
app.register_blueprint(app_Search, url_prefix="")
# app.register_blueprint(app_Browser, url_prefix="/Browse")
# app.register_blueprint(app_Document, url_prefix="/Document")
# app.register_blueprint(app_Contact, url_prefix="/Contact")
# app.register_blueprint(app_Download, url_prefix="/Download")

# @app.errorhandler(500)
# def page_not_found(e):
# 	return render_template('500.html')

# @app.errorhandler(404)
# def page_not_found(e):
# 	return render_template('404.html')

if __name__ == '__main__':
	app.run(debug=True, threaded=True, port = 5001)
