from flask import Flask
from nltk import word_tokenize
app = Flask(__name__)

@app.route('/')
def hello_world():
  a = word_tokenize("somthing is awesome")
  return a[0]

if __name__ == '__main__':
  app.run(debug=True)
