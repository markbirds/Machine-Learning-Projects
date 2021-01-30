from flask import Flask, request, render_template, jsonify
from server.util import classify_email

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/classify',methods=['POST','GET'])
def classify():
   if request.method == 'POST':
      email = request.form['email']
      prediction = classify_email(email)
      return jsonify({'prediction':str(prediction[0])})

if __name__ == '__main__':
   app.run()