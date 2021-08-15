from . import app, db
from .models import Weapon
from flask import render_template, redirect, url_for, request
import requests, json


@app.route('/', methods=["POST", "GET"])
def index():
    weapon = requests.get('http://service-2:5000/get/weapon').text
    damage = requests.get('http://service-3:5000/get/damage').json()

    content = {'weapon': weapon, 'damage': damage}
    status = requests.post('http://service-4:5000/post/status', json=content).json()

    new_weapon = Weapon(name=status['name'], weapon_type=weapon, damage=damage, status=status['effect'], level=status['level'])

    if new_weapon:
        db.session.add(new_weapon)
        db.session.commit()

    context = Weapon.query.limit(1).all()

    statement = f"You generated a {weapon} with a damage multiplier of {damage} and the status effect of {status['effect']}.\n \
        It is called the {status['level']} {status['name']} {weapon} of {status['effect']}"

    return render_template('index.html', statement=statement, context=context)


