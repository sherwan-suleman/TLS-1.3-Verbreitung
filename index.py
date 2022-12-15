from flask import Flask , request , render_template
from flask_cors import CORS
from classes.tls import tls
import sqlite3
connexion = sqlite3.connect("hosts.db", check_same_thread=False)
tlsInstance = tls()
app = Flask(__name__, template_folder='frontend/build', static_folder='frontend/build',static_url_path='')
CORS(app)
@app.get('/')
def index_get():
    return render_template("index.html")
@app.get("/clearhosts")
def clear_hosts():
    tlsInstance.clear(connexion)
    return ""
@app.get("/checkhosts")
def check_hosts():
    args = request.args
    tlsInstance.check( args['host'], 443, connexion )
    return ""
@app.get("/stat/getbytls")
def getByTls():
    data = tlsInstance.getbytls(connexion)
    return data
@app.get("/stat/getbyorganisation")
def getByOrganisation():
    data = tlsInstance.getbyorganisation(connexion)
    return data
@app.get("/stat/getbycyfer")
def getByCyfer():
    data = tlsInstance.getbycyfer(connexion)
    return data