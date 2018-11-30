# Test Web File
from bottle import route, run, template, get, post, Bottle
from bottle import request, error, static_file, PasteServer
from paste import httpserver

Webapp = Bottle()

@Webapp.route('/')
def index():
    return( static_file("/index.html",root='C:/Users/Joe Stanley/Desktop'))

@Webapp.route('/hello/<name>')
def nmdisp(name):
    return(template('<b>Hello {{name}}</b>!', name=name))

@Webapp.route('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

@Webapp.post('/login') # or @route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if True: #check_login(username, password):
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"

@Webapp.error(404)
def error404(error):
    return("Sorry, that link or page seems to be unavailable.")

@Webapp.route('/upload')
def upload():
    return('''<form action="/upload" method="post" enctype="multipart/form-data">
      Category:      <input type="text" name="category" />
      Select a file: <input type="file" name="upload" />
      <input type="submit" value="Start upload" />
    </form>''')

@Webapp.post('/upload')
def do_upload():
    category   = request.forms.get('category')
    upload     = request.files.get('upload')
    name, ext = os.path.splitext(upload.filename)
    print("I made it")
    if ext not in ('.png','.jpg','.jpeg'):
        return 'File extension not allowed.'

    save_path = get_save_path_for_category(category)
    upload.save(save_path) # appends upload.filename automatically
    return 'OK'

Webapp.run(host='localhost', port=80)
