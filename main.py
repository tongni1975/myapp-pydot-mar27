from flask import Flask

#create flask app

app = Flask(__name__, static_folder='./static')

#loading from static resource

@app.route('/', methods=['GET'])
def index():
    return app.send_static_file('index.html')

@app.route('/<path:mypath>', methods=['GET'])
def resources(mypath):
    print('mypath:',mypath)
    return app.send_static_file(mypath)

#run flask

if '__main__' == __name__:
    app.run(port=3000, debug=True, host='0.0.0.0')