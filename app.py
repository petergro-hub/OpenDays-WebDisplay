import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# Change this to the path of your custom image folder
IMAGE_FOLDER = '/home/peter/OpenDays/otherApp/static/images'

class ImageHandler(FileSystemEventHandler):
    def __init__(self, app):
        self.app = app
    def on_any_event(self, event):
        if event.is_directory:
            return None
        elif event.event_type == 'created':
            self.update_image_list()
        elif event.event_type == 'deleted':
            self.update_image_list()
        elif event.event_type == 'modified':
            self.update_image_list()
    def update_image_list(self):
        images = sorted(os.listdir(IMAGE_FOLDER))
        self.app.jinja_env.globals['images'] = images

@app.route('/')
def index():
    images = sorted(os.listdir(IMAGE_FOLDER))
    return render_template('index.html', images=images)

@app.route('/image/<filename>')
def get_image(filename):
    return send_from_directory(IMAGE_FOLDER, filename)

if __name__ == '__main__':
    event_handler = ImageHandler(app)
    observer = Observer()
    observer.schedule(event_handler, path=IMAGE_FOLDER)
    observer.start()
    app.jinja_env.globals['images'] = []
    app.run(debug=False, port=8000)
