import os


from flask import Flask, request, render_template, send_from_directory
from pathlib import Path

__author__ = 'ibininja'

app = Flask(__name__)



APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("upload.html")

@app.route("/upload", methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, 'images/')
    print('Target:' ,target)
    if not os.path.isdir(target):
            os.mkdir(target)
    else:
        print("Couldn't create upload directory: {}".format(target))
    print(request.files.getlist("file"))
    for upload in request.files.getlist("file"):
        print(upload)
        print("{} is the file name".format(upload.filename))
        filename = upload.filename
        destination = "/".join([target, filename])
        print ("Accept incoming file:", filename)
        print ("Save it to:", destination)
        upload.save(destination)

    # return send_from_directory("images", filename, as_attachment=True)
    return render_template("complete.html", image_name=filename)

@app.route('/upload/<path> <filename>')
def send_image(path, filename):
    print("path: ",path)
    return send_from_directory(path, filename)

@app.route('/gallery')
def get_gallery():

    ruta=os.getcwd()
    path = Path(ruta,"src\images")
    path.mkdir(parents=True, exist_ok=True)
    #print(ruta, "   ------    ", path)

    #image_names = os.listdir(path)
    image_names = ['1.png', '2.png', '3.jpg']
    path  = "images\CocaCola"
    print(image_names)
    return render_template("gallery.html", path = path, image_names=image_names)

if __name__ == "__main__":
    app.run(port=4555, debug=True)