from flask import Flask, send_from_directory, jsonify
import os
from werkzeug.utils import secure_filename
import time

app = Flask(__name__)
image_folder = '/home/ivrl/Fooocus/outputs'
latest_image = None

def get_latest_image():
    # Get the list of files in the directory, their full paths, and their modified times
    files = [(f, os.path.getmtime(os.path.join(image_folder, f))) for f in os.listdir(image_folder) if f.endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    # Sort the list of files by modified time in descending order
    files.sort(key=lambda x: x[1], reverse=True)
    # Return the name of the latest file, or None if there are no files
    return files[0][0] if files else None

@app.route('/')
def index():
    return send_from_directory('templates', 'index_latest.html')

@app.route('/latest-image')
def latest_image():
    return jsonify(image=get_latest_image())

@app.route('/image/<filename>')
def image(filename):
    return send_from_directory(image_folder, secure_filename(filename))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)
