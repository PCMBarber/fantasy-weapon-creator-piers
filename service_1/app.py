from flask import Flask
import requests, json

app = Flask(__name__)

@app.route('/')
def index():
    weapon = requests.get('http://34.105.171.115:80/get/weapon').text
    damage = requests.get('http://34.105.171.115:80/get/damage').json()

    content = {'weapon': weapon, 'damage': damage}
    status = requests.post('http://34.105.171.115:80/post/status', json=content).json()

    return f"You generated a {weapon} with a damage multiplier of {damage} and the status effect of {status['effect']}.\n \
        It is called the {status['level']} {status['name']} {weapon} of {status['effect']}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
