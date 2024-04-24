import uuid
import random
from werkzeug.security import generate_password_hash, check_password_hash

from models.user.user import User
from models.card.card import Card

#====================User====================#

def create_or_update_user(data):
    '''
    Crée ou met à jour un objet user à partir des données
    passées en paramètre.

        Param(s):
                | data ({}): Dictionnaire contenant les attributs de l'objet

        Return(s):
                | id_user (str): Id de l'objet user créé ou mis à jour

    '''
    salt = uuid.uuid4().hex
    if not data.get('id', False):
        user = User.create(
            id = uuid.uuid4().hex,
            username = data['username'],
            connection_count = -1,
            password_hash = generate_password_hash(data['password'] + salt),
            password_salt = salt)
        starter = random.choices(Card.select().where(Card.rarity=='common')[:], k=5)
        user.inventory.clear()
        for card in starter:
            try:
                user.inventory.add(card)
            except Exception:
                pass
    else:
        user = User.get(id=data['id'])
        user.username = data['username']
        user.password_hash = generate_password_hash(data['password'] + salt)
        user.password_salt = salt
        user.save()

    return user.id

def check_user(data):
    '''
    Renvoie l'objet User dont l'username a été passé en paramètre.

        Param(s):
                | data ({}): Dictionnaire contenant les attributs de l'user

        Return(s):
                | user (User): objet User à partir de l'username
    '''
    matching_users = User.select().where(User.username==data['username'])[:]
    for user in matching_users:
        if check_password_hash(user.password_hash, data['password'] + user.password_salt):
            user.connection_count += 1
            return user.toDict()
    return None

def get_inventory(user_id):
    '''
    Renvoie l'inventaire de l'objet User dont l'username a été passé en paramètre.

        Param(s):
                | user_id (uuid): id de l'user

        Return(s):
                | inventory (Card[]): objets Card à partir de l'username
    '''
    return User.get(id=user_id).inventory[:]