#This is a flask app for cs4740 cloud class
# The app is to grade students' assignments and give them a score
#Weiheng Su (No external sources were used)
#Assignment 4

import os


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





@app.route('/gradeUpload', methods=['GET','POST'])
def gradeUpload():
	file = request.files['file']
	if file and allowed_file(file.filename):
		# Make the filename safe, remove unsupported chars
		filename = secure_filename(file.filename)
		# Move the file form the temporal folder to
		# the upload folder we setup
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		# Redirect the user to the uploaded_file route, which
		# will basicaly show on the browser the uploaded file
		#return redirect(url_for('uploaded_file', filename=filename))
		return redirect(url_for('viewUpload'))

# This route is expecting a parameter containing the name
# of a file. Then it will locate that file on the upload
# directory and show it on the browser, so if the user uploads
# an image, that image is going to be show after the upload
#@app.route('/uploads/<filename>')
#def uploaded_file(filename):
#	return send_from_directory(app.config['UPLOAD_FOLDER'], filename)







#@app.route('/gradeUpload',methods=['GET','POST'])

#def gradeUpload():

	
if __name__ == "__main__":
	app.run(debug=True)