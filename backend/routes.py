from flask import Flask , request, render_template
from controllers import result
app = Flask(__name__)

@app.route('/')
def root():
    return "hello from arnab"

@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == "GET":
        return render_template('utils/input.html')
    if request.method == "POST":
        request_data = request.get_json()
        print(request_data)
        response = result(request_data)
        return render_template('utils/result.html', value=response)



if __name__ == '__main__':
    app.debug = True
    app.run()
