monsters = {
    'pythachu': {
        'name': 'Pythachu',
        'attacks': ['tonnerre', 'charge'],
    },
    'pythard': {
        'name': 'Pythard',
        'attacks': ['jet-de-flotte', 'charge'],
    },
    'ponytha': {
        'name': 'Ponytha',
        'attacks': ['brûlure', 'charge'],
    },
}

attacks = {
    'charge': {'damages': 20},
    'tonnerre': {'damages': 50},
    'jet-de-flotte': {'damages': 40},
    'brûlure': {'damages': 40},
}


def get_choice_input(choices, error_message):
    entry = input('> ').lower()
    while entry not in choices:
        print(error_message)
        entry = input('> ').lower()
    return choices[entry]


def get_monster_choice(monsters, error_message):
    entry = input('> ').lower()
    for key, value in monsters.items():
        if entry == key or entry == value['name'].lower():
            return monsters[key]
    print(error_message)
    return get_monster_choice(monsters, error_message)


def get_player(player_id):
    print('Joueur', player_id, 'quel monstre choisissez-vous ?')
    monster = get_monster_choice(monsters, 'Monstre invalide')
    while True:
        try:
            pv = int(input('Quel est son nombre de PV ? '))
            break
        except ValueError:
            print("Veuillez entrer un nombre valide pour les PV.")
    return {'id': player_id, 'monster': monster, 'pv': pv}


def get_players():
    print('Monstres disponibles :')
    for monster in monsters.values():
        print('-', monster['name'])
    return get_player(1), get_player(2)


def apply_attack(attack, opponent):
    opponent['pv'] -= attack['damages']
    if opponent['pv'] < 0:
        opponent['pv'] = 0


def game_turn(player, opponent):
    if player['pv'] <= 0:
        return

    monster_attacks = {}

    print('Joueur', player['id'], 'quelle attaque utilisez-vous ?')
    for name in player['monster']['attacks']:
        monster_attacks[name] = attacks[name]
        print('-', name.capitalize(), '-', attacks[name]['damages'], 'PV')

    attack = get_choice_input(monster_attacks, 'Attaque invalide')
    apply_attack(monster_attacks[attack], opponent)

    print(
        player['monster']['name'],
        'attaque',
        opponent['monster']['name'],
        'qui perd',
        monster_attacks[attack]['damages'],
        'PV, il lui en reste',
        opponent['pv'],
    )


def get_winner(player1, player2):
    if player1['pv'] > player2['pv']:
        return player1
    else:
        return player2


player1, player2 = get_players()

print()
print(player1['monster']['name'], 'affronte', player2['monster']['name'])
print()

while player1['pv'] > 0 and player2['pv'] > 0:
    game_turn(player1, player2)
    game_turn(player2, player1)

winner = get_winner(player1, player2)
print('Le joueur', winner['id'], 'remporte le combat avec', winner['monster']['name'])


def test_apply_attack():
    player = {'id': 0, 'monster': monsters['pythachu'], 'pv': 100}

    apply_attack(attacks['brûlure'], player)
    assert player['pv'] == 60

    apply_attack(attacks['tonnerre'], player)
    assert player['pv'] == 10

    apply_attack(attacks['charge'], player)
    assert player['pv'] == 0


def test_get_winner():
    player1 = {'id': 0, 'monster': monsters['pythachu'], 'pv': 100}
    player2 = {'id': 0, 'monster': monsters['pythard'], 'pv': 0}
    assert get_winner(player1, player2) == player1
    assert get_winner(player2, player1) == player1

    player2['pv'] = 120
    assert get_winner(player1, player2) == player2
    assert get_winner(player2, player1) == player2

    player1['pv'] = player2['pv'] = 0
    assert get_winner(player1, player2) == player2
    assert get_winner(player2, player1) == player1
