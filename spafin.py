from flask import Flask
app = Flask(__name__)

@app.route('/index')
def index():

        f = open('view/index.html', 'r').read()
        return f

@app.route('/page1')
def pag1():

        f = open('view/page1.html', 'r').read()
        return f

@app.route('/page2')
def pag3():

        f = open('view/page2.html', 'r').read()
        return f
                
        
#-------------------------------------------#
if __name__ == '__main__':
        app.run(host='0.0.0.0', port='5000')
