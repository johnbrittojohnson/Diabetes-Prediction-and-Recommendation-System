from flask import Flask, request, render_template
from dxt1 import cm, ac, test
import ter


app = Flask(__name__, template_folder='template')
@app.route('/')
def form():
    return render_template('index.html')


@app.route('/x')
def my_form():
    return render_template('details.html')

@app.route('/getfile', methods=['POST'])
def my_form_post():
    gender = str(request.form['gender'])
    age = int(request.form['age'])
    pregnancycount=int(request.form['pregnancycount'])
    glucose = int(request.form['glucose'])
    bloodpressure = int(request.form['bloodpressure'])
    skinthickness = int(request.form['skinthickness'])
    insulin = int(request.form['insulin'])
    bmi = float(request.form['bmi'])
    pedigree = float(request.form['diabetespedigreefunction'])
    test_output= [ pregnancycount, glucose , bloodpressure , skinthickness , insulin , bmi , pedigree, age ]
    result = test(test_output)
    ter.term(result, age, glucose, bmi)
    return render_template("result.html",age = age,test_output = result,bmi = bmi,glucose = glucose)
    
    
    

if __name__ == '__main__':
 app.run(host='127.0.0.1',debug=True,port=8080)
