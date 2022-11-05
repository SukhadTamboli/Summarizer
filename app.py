#from crypt import methods
#from cgitb import text
#from distutils import text_file
#from distutils.text_file import TextFile
from cgitb import text
from flask import Flask, render_template, request
from sklearn.metrics import classification_report

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')
#saving the file in local storge here 
@app.route('/Summarizer', methods=['POST'])
def predict():
    textfile= request.files['textfile']
    text_path= "./text/" + textfile.filename  # type: ignore
    textfile.save(text_path)  # type: ignore

     

    return render_template('index.html', prediction) 

if __name__ == '__main__':
    app.run(port=3000, debug=True)