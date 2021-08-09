from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def index():
    var1 = requests.get('http://service-2:5000/get/var1').text
    var2 = requests.get('http://service-3:5000/get/var2').text

    content = {'var1': var1, 'var2': var2}
    status = requests.post('http://service-4:5000/post/service-4', json=content)

    return f"You generated a {var1} with a damage multiplier of {var2} and the status effect of {status.element}.\n It is called {status.name}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')