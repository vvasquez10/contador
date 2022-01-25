from flask import Flask, render_template, session, redirect,request

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/', methods=['GET'])
def paginaInicial():    
    if 'visitas' in session:
        session['visitas'] += 1
        return render_template("index.html")
    else:
        session['visitas'] = 1
        return render_template("index.html")  

@app.route('/destroy_session', methods=['GET'])
def destruyeSesion():    
    session.clear()  
    return redirect("/")  

@app.route('/reset', methods=['POST'])
def reset():    
    return redirect("/destroy_session")  

@app.route('/addTwo', methods=['POST'])
def addTwo():    
    session['visitas'] += 1
    return redirect("/")  


@app.route('/addX', methods=['POST'])
def addX():    
    num = request.form['addX']
    session['visitas'] += int(num)-1
    return redirect("/")  

if __name__ == "__main__":
    app.run(debug = True)