from flask import Flask, render_template
import os,requests
app = Flask(__name__)	


@app.route('/',methods=["GET"])
def inicio():
    noserver=False
    datos=""
    
    try:
        server=os.environ["CITAS_SERVER"]
        url="http://"+server+"/quotes/random"
        r=requests.get(url, timeout=1)
        datos=r.json()
    except:
        noserver=True
 
    return render_template("inicio.html",noserver=noserver,datos=datos)


app.run('0.0.0.0',5000,debug=True)
