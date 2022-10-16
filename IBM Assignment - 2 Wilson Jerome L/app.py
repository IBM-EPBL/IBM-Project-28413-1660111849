from flask import Flask,redirect,url_for

app=Flask(__name__)

@app.route('/hello/<name>')
def hello_name(name):
    return render_template('hello.html',name=name)

@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s!' %name

@app.route('/page/<int:postID>')
def show_page(postID):
    return render_template('page.html',pageno=postID)

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('user/<nam>')
def hello_user(name):
    if name=='admin':
        return redirect(url_for('hello_name'),name=name)
    else:
        return redirect(url_for('hello_name'),name=name)

@app.route('/')
def hello_world():
    return 'Hello world'

@app.route('/login')
def login():
    return 'Login Page'

@app.route('/home')
def home():
    return 'home Page'

@app.route('/register')
def register():
    return 'register Page'

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8880,debug=True)
