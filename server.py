from flask import Flask,render_template,request,redirect,url_for,Response
from main import *
import jinja2
from fileinput import filename
import os 
from werkzeug.utils import secure_filename
# import shutil

# source = '/Users/aditya/Documents/Documents - Ravindra’s MacBook Pro/SEM-6/IS/Info-Sec-Project/'
destination = '/Users/aditya/Documents/Documents - Ravindra’s MacBook Pro/SEM-6/IS/Info-Sec-Project/data'

app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = "data/"



@app.route("/", methods=['GET','POST'])
def index():
    
    if request.method == 'POST':
        dropdown_id = request.form.get('encryption')
        if dropdown_id == 'encryptId':
            f = request.files['fileName']
            fn = f.filename
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(fn)))  
            return redirect(url_for('func1')) 
        else:
            f = request.files['fileName']
            fn = f.filename
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(fn)))  
            return redirect(url_for('func2'))   
    elif request.method == 'GET':
        return render_template('index.html')

    return render_template("index.html")




@app.route("/encrypt")
def func1():
    encrypt()
    return render_template("acknoweldgment.html")

@app.route("/decrypt")
def func2():
    decrypt()
    return render_template("acknoweldgment.html")

if __name__ == "__main__":
    app.run(debug=True)


