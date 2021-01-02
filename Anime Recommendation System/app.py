from flask import Flask, request, render_template, jsonify
from server.util import return_anime_list, recommend_pearson

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/api')
def api():
  return jsonify({'anime_list':return_anime_list()})

@app.route('/recommend',methods=['POST','GET'])
def recommend():
  if request.method == 'POST':
    anime = request.form['anime']
    filter = request.form['filter']
    return jsonify(recommend_pearson(anime,filter))

if __name__ == '__main__':
   app.run()