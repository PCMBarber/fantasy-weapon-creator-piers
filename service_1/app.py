from flask import Flask
import requests, json

app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def index():
    weapon = requests.get('http://service-2:5000/get/weapon').text
    damage = requests.get('http://service-3:5000/get/damage').json()

    content = {'weapon': weapon, 'damage': damage}
    status = requests.post('http://service-4:5000/post/status', json=content).json()

    return f"You generated a {weapon} with a damage multiplier of {damage} and the status effect of {status['effect']}.\n \
        It is called the {status['level']} {status['name']} {weapon} of {status['effect']}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
