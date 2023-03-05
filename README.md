# Flask

Flask is a web framework, it’s a Python module that lets you develop web applications easily. It’s has a small and easy-to-extend core: it’s a microframework that doesn’t include an ORM (Object Relational Manager) or such features.

It does have many cool features like url routing, template engine. It is a WSGI web app framework.

Why is Flask a good web framework choice? Unlike the Django framework, Flask is very Pythonic. It’s easy to get started with Flask, because it doesn’t have a huge learning curve.

On top of that it’s very explicit, which increases readability. To create the “Hello World” app, you only need a few lines of code.

This is a boilerplate code example.

from flask import Flask app = Flask(name)

@app.route('/') def hello_world(): return 'Hello World!'

if name == 'main': app.run() If you want to develop on your local computer, you can do so easily. Save this program as server.py and run it with python server.py.

$ python server.py

Serving Flask app "hello"
Running on http://127.0.0.1:5000/ (Press CTRL+C to quit) It then starts a web server which is available only on your computer. In a web browser open localhost on port 5000 (the url) and you’ll see “Hello World” show up. To host and develop online, you can use PythonAnywhere
Some example output:

flask

It’s a microframework, but that doesn’t mean your whole app should be inside one single Python file. You can and should use many files for larger programs, to handle complexity.

Micro means that the Flask framework is simple but extensible. You may all the decisions: which database to use, do you want an ORM etc, Flask doesn’t decide for you.

Flask is one of the most popular web frameworks, meaning it’s up-to-date and modern. You can easily extend it’s functionality. You can scale it up for complex applications.