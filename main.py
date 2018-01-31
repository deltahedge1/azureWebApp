from flask import Flask
from nltk import word_tokenize
app = Flask(__name__)

@app.route('/')
def hello_world():
  word_tokenize("somthing is working")
  return "hello world"

if __name__ == '__main__':
  app.run(debug=True)
