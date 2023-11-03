from flask import Flask, send_from_directory, jsonify
import os
from threading import Timer
import time

app = Flask(__name__)
image_folder = '/path/to/your/image/folder'
image_list = []

def update_image_list():
    global image_list
    # List all image files in the folder
    image_list = [f for f in os.listdir(image_folder) if f.endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    Timer(5.0, update_image_list).start()

@app.route('/')
def index():
    return send_from_directory('templates', 'index2.html')

@app.route('/images')
def images():
    return jsonify(images=image_list)

@app.route('/image/<filename>')
def image(filename):
    return send_from_directory(image_folder, filename)

if __name__ == '__main__':
    update_image_list()  # Start the image list update loop
    app.run(host='0.0.0.0', port=8000)
