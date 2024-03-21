from flask import Flask,request,render_template
import pickle
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction.text import CountVectorizer

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/predict',methods=['POST'])
@app.route('/predict',methods=['POST'])
def predict():
    text = request.form.get('text')
    vector = pickle.load(open(r"C:\Users\ravin\Downloads\cv.pkl",'rb'))
    num= vector.transform([text]).toarray()
    model = pickle.load(open(r"C:\Users\ravin\Downloads\logistic.pkl",'rb'))
    prediction = model.predict(num)
    return render_template('home.html',prediction=prediction)



if __name__ =='__main__':
        app.run(debug=True, port=5000, host='0.0.0.0')