from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/')
def index():
	
	L = [31,4,23,14,45,87,76,132]
	return render_template('index2.html',list=L)





@app.route('/form', methods=['GET','POST'])
def form():
	if request.method == 'POST':
		username = request.form['username']
		email =  request.form['email']
		return render_template('info.html',username=username)
	return render_template('form2.html')

if __name__ == '__main__':
	app.run(debug = True)