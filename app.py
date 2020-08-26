import os

from flask import Flask, render_template, url_for, request, redirect

from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_PATH'] = 'uploads'

@app.route('/', methods=['GET','POST'])
def index():
	if request.method == 'GET':
		return render_template('index.html')
	else:
		f = request.files['file']
		filename = secure_filename(f.filename)
		f.save(os.path.join(app.config['UPLOAD_PATH'], filename))
		return 'uploaded successfully!'

app.run(debug=True)