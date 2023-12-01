from flask import Flask,request
from controllers import result
app = Flask(__name__)

@app.route('/')
def root():
    return "hello from arnab"

@app.route('/api/predict', methods=['POST'])
def predictRoute():
    request_data = request.get_json()

    return result(request_data)



if __name__ == '__main__':
    app.debug = True
    app.run()
