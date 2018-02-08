from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'

@app.route('/sign',methods=['GET'])
def sign_form():
    return '''<form action="/signin" method="GET">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''


@app.route('/sign',methods=["POST"])
def signin():
    # 需要从 request 对象读取表单内容
    if( request.form['username'] == 'admin' and request.form['password'] == 'password'):
        return '<h3>Hello, admin </h3>'
    return '<h3>Bad username or password</h3>'


if(__name__=='__main__'):
    app.run()
