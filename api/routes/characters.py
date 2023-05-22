from flask import Blueprint, jsonify

character_bp = Blueprint('characters', __name__)


@character_bp.route('/characters', methods=['GET'])
def get_characters():
    '''Get a list of characters'''
    return jsonify({'message': 'Get characters'})


@character_bp.route('/characters/<int:character_id>', methods=['GET'])
def get_character(character_id: int):
    '''Get a character'''
    return jsonify({'message': 'Get character'})


@character_bp.route('/characters', methods=['POST'])
def add_character():
    '''Add a character'''
    return jsonify({'message': 'Add character'})


@character_bp.route('/characters/<int:character_id>', methods=['PUT'])
def update_character(character_id: int):
    '''Update a character'''
    return jsonify({'message': 'Update character'})


@character_bp.route('/characters/<int:character_id>', methods=['DELETE'])
def delete_character(character_id: int):
    '''Delete a character'''
    return jsonify({'message': 'Delete character'})
