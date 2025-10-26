from flask import Flask, render_template, request
import os 

app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def hello_world():
    return "Hello from Gunicorn on Railway! It's working!"

    # if request.method == 'GET':
    #     return render_template('index.html', message="Hello, World!")
    # else : 
    #     return request.form.get('url')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5005))
    app.run(host='0.0.0.0', port=port)