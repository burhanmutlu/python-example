import os
from flask import Flask, render_template, request, flash, redirect, url_for
from moduleFile import ResimSifreleme
from werkzeug.utils import secure_filename
from moduleFile import ResimSifreleme
 
UPLOAD_FOLDER = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Pictures')
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__, template_folder='template')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)

            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            process = int(request.args.get('process'))

            p = ResimSifreleme(os.path.join(app.config['UPLOAD_FOLDER'], filename), 0)
            print("--------------------------",process)
            if(process == 1):
                img = p.imageEncryption()
            if(process == 2):
                img = p.imageDecryption()

            p.saveImage(os.path.join(app.config['UPLOAD_FOLDER'], filename),img)
 
            return redirect(url_for('uploaded_file', filename=filename))
    return render_template('/upload.html')

from flask import send_from_directory

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

from werkzeug.middleware.shared_data import SharedDataMiddleware
app.add_url_rule('/uploads/<filename>', 'uploaded_file', build_only=True)
app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
    '/uploads':  app.config['UPLOAD_FOLDER']
})

if __name__ == '__main__':
   app.run(debug = True)
