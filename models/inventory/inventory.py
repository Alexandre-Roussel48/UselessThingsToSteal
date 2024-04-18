from peewee import *

from server import BaseModel
from models.user.user import User
from models.card.card import Card

class Inventory(BaseModel):
    '''
    La classe Inventory permet de contenir les cartes appartenants aux users.

        Attributs:
                | user_id (User): id de l'utilisateur
                | card_id (Card): id de la carte
    '''
    user_id = ForeignKeyField(User)
    card_id = ForeignKeyField(Card)

    def toDict(self):
        '''
        Retourne un dictionnaire contenant les données d'un objet Inventory.

            Return(s):
                    | data ({}): Dictionnaire contenant tous les attributs de l'objet Inventory

        '''
        data = {
            'user_id':self.user_id,
            'card_id':self.card_id
        }

        return data