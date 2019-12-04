from flask import Flask,render_template,request,redirect,url_for
app = Flask(__name__)



@app.route('/')
def index():
	x = 'hello world!'
	return render_template("index.html",show=x)

@app.route('/hello/<user>')
def hello(user):
   return render_template('hello.html', name = user)


#build a URL dynamically, by adding variable parts to the route parameter

@app.route('/<name>')
def hello_name(name):
   return 'Hello %s!' % name

@app.route('/<int:postID>')
def show_Post(postID):
   return 'Post Number %d' % postID

@app.route('/<float:revNo>')
def revision(revNo):
   return 'Revision Number %f' % revNo




@app.route('/admin')
def hello_admin():
   return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest

@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest',guest = name))


if __name__ == '__main__':
	app.debug = True
	app.run()