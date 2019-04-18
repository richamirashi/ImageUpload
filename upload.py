from flask import Flask, render_template, request
from werkzeug import secure_filename
import os
UPLOAD_FOLDER = 'static/images'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def upload():
   return render_template('index.html')

@app.route('/img', methods = ['GET', 'POST'])
def upload_image():
   if request.method == 'POST':
      image = request.files['file']
      image_name = secure_filename(image.filename)
      image.save(os.path.join(app.config['UPLOAD_FOLDER'], image_name))
      return render_template("view.html", uploaded_image = image_name)

if __name__ == '__main__':
   app.run(debug = True)
