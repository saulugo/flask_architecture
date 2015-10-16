from flask import Flask
app = Flask(__name__)

@app.route('/<username>')
def user(username):
	return '<h1>Hello Mr. %s</h1>' % username
	
@app.route('/portfolios/<int:p_id>')
def portfolios(p_id):
	return '<p>Your portfolio id: %d is ready</p>' %p_id
	
	
if __name__ == '__main__':
	app.run(debug=True)
	