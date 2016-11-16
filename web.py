from flask import Flask,redirect,render_template,request
import db
import dynamics

app = Flask(__name__)

PUB_DYNAMICS_AVAILABLE = dynamics.pub_sources.keys()
PRIV_DYNAMICS_AVAILABLE = dynamics.priv_sources.keys()

@app.route('/pub')
def root():
  if "index" in PUB_DYNAMICS_AVAILABLE:
    return render_template("pub/index.html", **dynamics.pub_sources["index"]())
  else:
    return render_template("pub/index.html")

@app.route('/pub/<path:patha>')
def send_pub(patha):
  path = patha.replace("..", ".")
  dyn = path.split('.')[0]
  if dyn in PUB_DYNAMICS_AVAILABLE:
    return render_template("pub/"+path, **dynamics.pub_sources[dyn]())
  else:
    return render_template("pub/"+path)

@app.route('/login')
def login():
  if "login" in PUB_DYNAMICS_AVAILABLE:
    return render_template("pub/login.html", **dynamics.pub_sources["login"]())
  else:
    return render_template("pub/login.html")

@app.route('/do_login', methods=['POST'])
def do_login():
  usrr = db.User.query.filter_by(username=request.form.get('username'))
  if usrr.count <1:
    return redirect('/login?error=fail')
  usr=usrr.first()
  k=usr.login(request.form.get('password'), request.environ['REMOTE_ADDR'], request.headers.get('User-Agent'))
  if k=="logout":
    return redirect('/login?error=fail')
  resp = redirect('/priv')
  resp.set_cookie('soda', k)
  return resp

@app.route('/priv')
def privroot():
  usr=db.User.query.filter_by(sessionhash=request.cookies.get('soda'))
  if usr.count() < 1:
    return redirect('/pub')
  userobj = usr.first()
  if "index" in PRIV_DYNAMICS_AVAILABLE:
    return render_template("priv/index.html", **dynamics.priv_sources["index"]())
  else:
    return render_template("priv/index.html")

@app.route('/priv/<path:patha>')
def send_priv(patha):
  usr=db.User.query.filter_by(sessionhash=request.cookies.get('soda'))
  if usr.count() < 1:
    return redirect('/pub')
  userobj = usr.first()
  path = patha.replace("..", ".")
  dyn = path.split('.')[0]
  if dyn in PRIV_DYNAMICS_AVAILABLE:
    return render_template("priv/"+path, **dynamics.priv_sources[dyn]())
  else:
    return render_template("priv/"+path)

if __name__ == '__main__':
    app.run()
