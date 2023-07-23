from datetime import datetime
from flask import Blueprint, jsonify, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

from api import db
from api.models.player import Player

player_bp = Blueprint('players', __name__)

# region Forms

class AddPlayerForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired('First name is required.')])
    last_name = StringField('Last Name', validators=[DataRequired('Last name is required.')])
    email = StringField('Email', validators=[DataRequired('Email is required.'), Email('Email is invalid.')])

# endregion

# region Routes

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
    form = AddPlayerForm()
    if form.validate_on_submit():
        new_player = Player(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            is_active=True,
            is_admin=False,
            is_deleted=False,
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        db.session.add(new_player)
        db.session.commit()
        flash('Player added successfully!', 'success')

    # return redirect(url_for('player_bp.get_players'))
    return jsonify({'message': 'Add player'})


@player_bp.route('/players/<int:player_id>', methods=['PUT'])
def update_player(player_id: int):
    '''Update a player'''
    return jsonify({'message': 'Update player'})


@player_bp.route('/players/<int:player_id>', methods=['DELETE'])
def delete_player(player_id: int):
    '''Delete a player'''
    return jsonify({'message': 'Delete player'})

# endregion