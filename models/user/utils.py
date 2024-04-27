import uuid
import random
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta

from models.user.user import User
from models.user.user import Inventory
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
        for card in starter:
            Inventory.create(
                user_id=user.id,
                card_id=card.id)
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
            user.save()
            return user.toDict()
    return None

def get_inventory(user_id):
    '''
    Renvoie l'inventaire de l'objet User dont l'id a été passé en paramètre.

        Param(s):
                | user_id (uuid): id de l'user

        Return(s):
                | inventory (Card[]): objets Card à partir de l'id
    '''
    return [Card.get(id=inventory.card_id) for inventory in Inventory.select().where(Inventory.user_id==user_id)[:]]

def drop_card(user_id):
    '''
    Ajoute une carte aleatoire a l'inventaire de l'objet User dont l'id a été passé en paramètre.

        Param(s):
                | user_id (uuid): id de l'user

        Return(s):
                | card (Card): objet Card ajoute a l'inventaire
    '''
    user = User.get(id=user_id)
    if user.next_card > datetime.utcnow():
        return None
    user.next_card = datetime.utcnow() + timedelta(minutes=1)
    user.save()
    drop = random.choices(Card.select().where(Card.rarity=='common')[:], k=1)[0]
    Inventory.create(
        user_id=user_id,
        card_id=drop.id)
    return {'drop':drop.toDict(),'next_card':user.next_card.isoformat() + 'Z'}