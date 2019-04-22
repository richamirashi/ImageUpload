from flask import Flask, render_template, request, send_file, abort
from io import StringIO, BytesIO
from werkzeug import secure_filename
app = Flask(__name__)

@app.route('/')
def upload():
   return render_template('index.html')

@app.route('/img', methods = ['GET', 'POST'])
def upload_image():
   error = None
   if request.method == 'GET':
       abort(405)
   if request.method == 'POST':
      image = request.files['file']
      image_name = secure_filename(image.filename)
      if image_name == '':
          error = 'The file is not chosen. Please select an image to upload.'
          return render_template('index.html', error = error), 400
      # Reads and returns the binary data-stream
      data = image.read()
      # BytesIO object is created
      strIO = BytesIO()
      strIO.write(data)
      strIO.seek(0)
      return send_file(strIO, attachment_filename=image_name, as_attachment=False)

if __name__ == '__main__':
   app.run(debug = True)
