from flask import Flask
import random

app = Flask(__name__)

weapon = ['Sword', 'Axe', 'Dagger', 'Crossbow', 'Bow', 'Staff']

@app.route('/get/weapon')
def get_weapon():
    return random.choice(weapon)

if __name__ == '__main__':
    app.run(host='0.0.0.0')