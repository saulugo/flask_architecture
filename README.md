#Flask Applications Architecture

A Flask App is structured the following way:

1) **Application Instance:** All Flask applications must create an application instance. The web server
passes all requests it receives from clients to this object for handling using a protocol called 
Web Server Gateway Interface (WSGI)

The **app instance is** an object of the Class Flask. It is usually created as follow:

from flask import Flask
app = Flask(__name__)

2)**Routes and View Functions:** the client sends requests to the web server, who in turn sends them to
the **app instance**. The app instance keeps a map of URLs (received from the web server - clients requests)
and Python functions to be run for each URL. This association between a URL and a Python function is
called a **Route**.
