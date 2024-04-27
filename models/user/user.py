from peewee import *

from server import BaseModel
from datetime import datetime
from models.card.card import Card

class User(BaseModel):
    '''
    La classe User permet de contenir toutes les données d'un utilisateur.

        Attributs:
                | id (str): id de l'utilisateur
                | username (str): nom de l'utilisateur
                | password_hash (str): hash du mot de passe de l'utilisateur
                | password_salt (str): salt du mot de passe de l'utilisateur
                | next_card (date): prochaine date d'attribution d'une carte commune a l'utilisateur
                | next_theft (date): prochaine date de vol d'une carte par l'utilisateur
    '''
    id = CharField(max_length=40, primary_key=True)
    username = CharField(max_length=100)
    password_hash = CharField(max_length=200)
    password_salt = CharField(max_length=100)
    connection_count = IntegerField()
    next_card = DateTimeField(default=datetime.utcnow(), formats='%Y-%m-%d %H:%M:%S')
    next_theft = DateTimeField(default=datetime.utcnow(), formats='%Y-%m-%d %H:%M:%S')

    def toDict(self):
        '''
        Retourne un dictionnaire contenant les données d'un objet User.

            Return(s):
                    | data ({}): Dictionnaire contenant tous les attributs de l'objet User

        '''
        data = {
            'id':self.id,
            'username':self.username,
            'connection_count':self.connection_count,
            'next_card':self.next_card.isoformat() + 'Z',
            'next_theft':self.next_theft.isoformat() + 'Z'
        }

        return data

class Inventory(BaseModel):
    id = AutoField(primary_key=True)
    user_id = ForeignKeyField(User)
    card_id = ForeignKeyField(Card)