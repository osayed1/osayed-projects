from flask import Flask , request 
from flask import render_template_string as render

app = Flask(__name__)
temp = "0"

@app.route('/')
def home():
    return render("<h> {{temperature}}</h>", temperature = temp)

@app.route('/update', methods=['POST'])
def update():
    global temp

    temp = request.form.get('temperature', '0')

    return "ok", 200

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000)