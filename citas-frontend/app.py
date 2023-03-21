from flask import Flask, render_template
import os,requests
app = Flask(__name__)	


@app.route('/',methods=["GET"])
def inicio():
    noserver=False
    datos=""
    version=""
    try:
        server=os.environ["CITAS_SERVER"]
        url="http://"+server+"/quotes/random"
        r=requests.get(url, timeout=1)
        datos=r.json()
        url="http://"+server+"/version"
        r=requests.get(url, timeout=1)
        print(r.text)
        version=r.text
    except:
        noserver=True
 
    return render_template("inicio.html",noserver=noserver,datos=datos,version=version)


app.run('0.0.0.0',5000,debug=True)
