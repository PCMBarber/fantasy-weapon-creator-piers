from flask import Flask, request, jsonify
import random

app = Flask(__name__)

effects = {
    0: "Fire",
    1: "Ice",
    2: "Lightning",
    3: "Water",
    4: "Earth",
    5: "Light",
    6: "Dark"
}

swords = {
    "names": {
        0: "Sharp",
        1: "Slicing",
        2: "Piercing",
        3: "Fearsome",
        4: "Pathetic"
    }
}

axes = {
    "names": {
        0: "Heavy",
        1: "Wimpy",
        2: "Devastating",
        3: "Swift",
        4: "Slow"
    }
}

daggers = {
    "names": {
        0: "Swift",
        1: "Hidden",
        2: "Piercing",
        3: "Blunt",
        4: "Useless"
    }
}

crossbows = {
    "names": {
        0: "Swift",
        1: "Slow",
        2: "Piercing",
        3: "Slapdash",
        4: "Loud"
    }
}

bows = {
    "names": {
        0: "Heavy",
        1: "Long",
        2: "Stunted",
        3: "Silent",
        4: "Short"
    }
}

staves = {
    "names": {
        0: "Heavy",
        1: "Long",
        2: "Short",
        3: "Light",
        4: "Useless"
    }
}

@app.route('/post/status', methods=['POST'])
def post_status():
    weapon = request.json['weapon']
    damage = request.json['damage']

    if weapon == 'sword':
        name = random.choice(list(swords["names"].values()))
    elif weapon == 'axe':
        name = random.choice(list(axes["names"].values()))
    elif weapon == 'dagger':
        name = random.choice(list(daggers["names"].values()))
    elif weapon == 'crossbow':
        name = random.choice(list(crossbows["names"].values()))
    elif weapon == 'bow':
        name = random.choice(list(bows["names"].values()))
    else:
        name = random.choice(list(staves["names"].values()))

    if damage <= 10:
        level = "Beginner"
    elif damage <= 20:
        level = "Adept"
    elif damage <= 30:
        level = "Journeyman"
    elif damage <= 40:
        level = "Master"
    elif damage <= 50:
        level = "Hero"
    else:
        level = "Legend"

    effect = random.choice(list(effects.values()))

    status = {
        "level": level,
        "name": name,
        "effect": effect
    }
    
    return jsonify(status) 

if __name__ == '__main__':
    app.run(host='0.0.0.0')