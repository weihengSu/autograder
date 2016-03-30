#This is a flask app for cs4740 cloud class
# The app is to grade students' assignments and give them a score
#Weiheng Su (No external sources were used)
#Assignment 4

import os
import subprocess

from flask import Flask, render_template,json, request, redirect, url_for, request, get_flashed_messages,send_from_directory

from werkzeug import secure_filename
app = Flask(__name__)





# This is the path to the upload directory
app.config['UPLOAD_FOLDER'] = 'uploads/'
# These are the extension that we are accepting to be uploaded
app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','cc','cpp','c'])

# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
	return '.' in filename and \
		   filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']





@app.route("/")
def main():
	return render_template('index.html')

#@app.route('/showUpload')
#def showUpload():
#	return redirect(url_for('viewUpload'))

@app.route('/showUpload')
def showUpload():
	return redirect(url_for('viewUpload'))

					
	
@app.route('/viewUpload')
def viewUpload():
	return render_template('upload.html')





@app.route('/gradeUpload', methods=['GET', 'POST'])
def gradeUpload():
	file = request.files['file']
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		return redirect(url_for('viewUpload'))


@app.route('/viewResult',methods=['GET', 'POST'])
def viewResult():
	subprocess.call("rm -f ./a.out", shell=True)
	retcode = subprocess.call("/usr/bin/g++ uploads/walk.cc", shell=True)
	data = {}
	data[0] = ""
	data[1] = ""
	if retcode:
		data[0] += "failed to compile walk.cc\n"
	subprocess.call("rm -f ./output", shell=True)
	retcode = subprocess.call("./test.sh", shell=True)
	data[0] += "Score: " + str(retcode) + " out of 2 correct."
	data[1] += "*************Original submission*************\n"
	with open('uploads/walk.cc','r') as fs:
		data[1] += fs.read()
		data[1] += "\n"
	return render_template('upload.html', data=data)






#@app.route('/gradeUpload',methods=['GET','POST'])

#def gradeUpload():

	
if __name__ == "__main__":
	app.run(debug=True)
