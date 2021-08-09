from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def index():
    weapon = requests.get('http://service-2:5000/get/weapon').text
    damage = requests.get('http://service-3:5000/get/damage').json()

    content = {'weapon': weapon, 'damage': damage}
    status = requests.post('http://service-4:5000/post/service-4', json=content)

    return f"You generated a {weapon} with a damage multiplier of {damage} and the status effect of {status.element}.\n It is called {status.name}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
