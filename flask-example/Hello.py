from flask import Flask, render_template, request
from moduleFile import ResimSifreleme
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def isim_bastir():
   return 'Burhan Mutlu'

@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name

@app.route('/upload')
def upload_file():
   return render_template('/flask-example/upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file2():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return 'file uploaded successfully'


# p = ResimSifreleme("org.jpg", 0)

# sifreli = p.imageEncryption()
# p.PrintImage(sifreli, "sifreli")


# cozulmus = p.imageDecryption()
# p.PrintImage(cozulmus, "cozulmus")



if __name__ == '__main__':
   app.run()