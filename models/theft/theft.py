from peewee import *

from server import BaseModel
from models.user.user import User
from models.card.card import Card

class Theft(BaseModel):
    '''
    La classe Theft permet de contenir toutes les données d'un vol de carte.

        Attributs:
                | thief_id (User): id du voleur
                | victim_id (User): id de la victime du vol
                | card_id (Card): id de la carte vole
    '''
    thief_id = ForeignKeyField(User)
    victim_id = ForeignKeyField(User)
    card_id = ForeignKeyField(Card)

    def toDict(self):
        '''
        Retourne un dictionnaire contenant les données d'un objet Theft.

            Return(s):
                    | data ({}): Dictionnaire contenant tous les attributs de l'objet Theft

        '''
        data = {
            'thief_id':self.thief_id,
            'victim_id':self.victim_id,
            'card_id':self.card_id
        }

        return data