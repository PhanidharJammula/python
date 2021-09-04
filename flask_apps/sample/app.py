import json                                                                     
from flask import Flask, jsonify, request, Response, redirect, url_for, render_template
#from flask_cors import CORS                                                     
                                                                                
app = Flask(__name__)                                                           
#CORS(app)                                                                       
                                                                                
                                                                                
@app.route('/home', methods=['GET', 'POST'], defaults={'name': 'default'})                                
@app.route('/home/<string:name>', methods=['GET', 'POST'])                                
def first(name):                                                                    
    return "<h3>Hello {}</h3>".format(name)
                                                                                
@app.route('/json', methods=['GET', 'POST'])                                
def json():                                                                    
    return jsonify({"key1": 1, "key2": [1, 2, 3]})


@app.route('/details', methods=['GET', 'POST'])                                
def details():
    name = request.args.get('name')
    location = request.args.get('location')
    return "<h3>Hello {}, you are from {}.You are on the detaila page</h3>".format(name, location)

@app.route('/theform', methods=['GET', 'POST'], defaults={'name': 'default'})
@app.route('/theform/<name>', methods=['GET', 'POST'])                                
def form(name):
    if request.method == 'GET':
        return render_template('form.html', name=name, display=True, mylist=[1, 2])
    else:
        #name=request.form['name']
        #location=request.form['location']

        #return "Hi {}, your are from {}".format(name, location)
        
        return redirect(url_for('first'))
                                                                                
if __name__ == "__main__":                                                      
    app.run(host='localhost', port=8080, debug=True)

#name = request.args.get('name')
#data = request.get_json()
