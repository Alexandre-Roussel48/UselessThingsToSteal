from peewee import *

from server import BaseModel
from models.user.user import User
from models.card.card import Card

class Vault(BaseModel):
    '''
    La classe Vault permet de contenir toutes les données du coffre fort appartenants aux users.

        Attributs:
                | user_id (str): id de l'animation
                | card_id (str): titre de l'animation
                | rarity (str): statut de l'animation (3=En cours, 2=Terminée, 1=Validée)
    '''
    user_id = ForeignKeyField(User)
    card_id = ForeignKeyField(Card)
    rarity = CharField(max_length=10, constraints=[Check('rarity IN ("common", "uncommon", "rare", "epic", "legendary")')])

    class Meta:
        indexes = (
            (('user_id','card_id','rarity'), True),
        )

    def toDict(self):
        '''
        Retourne un dictionnaire contenant les données d'un objet Vault.

            Return(s):
                    | data ({}): Dictionnaire contenant tous les attributs de l'objet Vault

        '''
        data = {
            'user_id':self.user_id,
            'card_id':self.card_id,
            'rarity':self.rarity
        }

        return data