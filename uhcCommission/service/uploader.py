from flask import Flask, send_from_directory
import ngrok,logging,os,sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config.Config import Configs
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

class FileServer:
    def __init__(self, directory):
        self.directory = directory

    def get_files(self):
        return os.listdir(self.directory)

    def serve_file(self, filename):
        return send_from_directory(self.directory, filename)

app = Flask(__name__)

# Menggunakan class Configs untuk mendapatkan konfigurasi
conf = Configs()
DIRECTORY = os.path.join(os.path.abspath(os.path.join(os.getcwd(), os.pardir)), "document")

# Menggunakan class FileServer untuk menangani file
file_server = FileServer(DIRECTORY)

# Mengatur ngrok dengan token dari konfigurasi
ngrok.set_auth_token(conf.authtoken)
listener = ngrok.werkzeug_develop()
print("url: ",listener.url())

@app.route('/<path:filename>')
def serve_file(filename):
    return file_server.serve_file(filename)

@app.route('/file')
def index():
    files = file_server.get_files()
    links = [f"<a href='/{file}'>{file}</a>" for file in files]
    return "<br>".join(links)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
