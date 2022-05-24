from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Hello World from Flask!!!</h1>"

@app.route('/second')
def second():
    return "<h2>Hello from Second!!!</h2>"

@app.route("/third/subthird")
def third():
    return "<h3>This is the subpath of third page</h3>"

@app.route('/forth/<string:id>')
def forth(id):
    return f'Id number of this page is {id}'

if __name__=="__main__":
    app.run(debug=True)