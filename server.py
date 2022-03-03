# the next two lines always need to be atop this server.py file 
from flask import Flask, render_template, session, request, redirect
from env import KEY

app = Flask(__name__)    # Create a new instance of the Flask class called "app"
# all the @ stuff below will (later) be moved into separate files.  These will be replaced with controller import lines. 

@app.route('/')
def index(): 
    return render_template('index.html')

@app.route('/createUser/', methods=['POST'])
def createUser():
    print('Form submission was good')
    print('Here is the data', request.form)
    session['name'] = request.form['name']

@app.route('/movies/')
def movies():
    return render_template('movies.html')

"""DON'T TOUCH BELOW :-) below always needs to be at the bottom of the script, yes!"""
# below is stuff you oughta have, per TA Cameron Smith, from Coding Dojo: 

@app.route('/', defaults={'cookies': ''})
@app.route('/<path:cookies>')
def catch_all(cookies):
    return 'Sorry! No response here. Try url again.'

# below is flask boiler plate; exclude it and stuff won't work    
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

