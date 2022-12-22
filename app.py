from flask import Flask,render_template,request
from artifacts.utils import solar

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('solar.html')

@app.route('/predict',methods=['POST'])
def predict():
    data = request.form
    solar_obj = solar(data)
    result = solar_obj.predict()

    return render_template('solar.html',pred=result)

if __name__ == "__main__":
    app.run(host='localhost',port=5000,debug=True)


    