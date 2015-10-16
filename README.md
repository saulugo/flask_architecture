#Flask Applications Architecture

A Flask App is structured the following way:

1) Application Instance: All Flask applications must create an application instance. The web server
passes all requests it receives from clients to this object for handling using a protocol called 
Web Server Gateway Interface (WSGI)