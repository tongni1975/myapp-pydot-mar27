from flask import Flask

app=Flask(__name__, static_folder='./static')

@app.route('/', methods=['GET'])
def index():
    return app.send_static_file('index.html')

@app.route('/,path:mypath>', methods=['GET'])
def resources(mypath):
    return app.send_static_file(mypath)

if '__main__'==__name__:
    app.run(port=3000, debug=True, host='0.0.0.0')

    