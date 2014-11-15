from flask import Flask, request
app = Flask(__name__)

@app.route('/hello/')
def hello_world():
    return 'Hello World!'

@app.route('/page')
def page():
    print request.method
    print request.args.get('name', 'gyc')
    return 'you are in'

if __name__ == '__main__':
    app.debug = True
    app.run()
