from flask import Blueprint, jsonify

player_bp = Blueprint('players', __name__)


@player_bp.route('/players', methods=['GET'])
def get_players():
    '''Get a list of players'''
    return jsonify({'message': 'Get players'})


@player_bp.route('/players/<int:player_id>', methods=['GET'])
def get_player(player_id: int):
    '''Get a player'''
    return jsonify({'message': 'Get player'})


@player_bp.route('/players', methods=['POST'])
def add_player():
    '''Add a player'''
    return jsonify({'message': 'Add player'})


@player_bp.route('/players/<int:player_id>', methods=['PUT'])
def update_player(player_id: int):
    '''Update a player'''
    return jsonify({'message': 'Update player'})


@player_bp.route('/players/<int:player_id>', methods=['DELETE'])
def delete_player(player_id: int):
    '''Delete a player'''
    return jsonify({'message': 'Delete player'})
