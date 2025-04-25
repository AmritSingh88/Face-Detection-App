from flask import Flask, render_template, request, redirect, url_for
import face_recognition
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    # Load the uploaded image
    uploaded_image = face_recognition.load_image_file(file_path)
    face_locations = face_recognition.face_locations(uploaded_image)

    return render_template('index.html', face_locations=face_locations, filename=file.filename)

if __name__ == '__main__':
    app.run(debug=True)