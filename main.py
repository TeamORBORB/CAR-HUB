# import threading

# # import "packages" from flask
# from flask import render_template  # import render_template from "public" flask libraries

# # import "packages" from "this" project
# from __init__ import app  # Definitions initialization

# # setup APIs
# from api.cars import cars_api

# # register URIs
# # app.register_blueprint(joke_api) # register api routes
# app.register_blueprint(cars_api) # register api routes


# @app.errorhandler(404)  # catch for URL not found
# def page_not_found(e):
#     # note that we set the 404 status explicitly
#     return render_template('404.html'), 404

# @app.route('/')  # connects default URL to index() function
# def index():
#     return render_template("index.html")

# @app.route('/stub/')  # connects /stub/ URL to stub() function
# def stub():
#     return render_template("stub.html")

# # this runs the application on the development server
# if __name__ == "__main__":
#     # change name for testing
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///volumes/sqlite.db'
#     app.run(debug=True, host="0.0.0.0", port="8054")