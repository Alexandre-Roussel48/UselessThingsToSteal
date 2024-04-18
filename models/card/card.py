from peewee import *

from server import BaseModel

class Card(BaseModel):
    '''
    La classe Card permet de contenir les données relatives a une carte.

        Attributs:
                | id (str): id de la carte
                | name (str): nom de la carte
                | rarity (str): rarete de la carte (common, uncommon, rare, epic, legendary)
    '''
    id = CharField(max_length=40, primary_key=True)
    name = CharField(max_length=100)
    rarity = CharField(max_length=10, constraints=[Check('rarity IN ("common", "uncommon", "rare", "epic", "legendary")')])

    def toDict(self):
        '''
        Retourne un dictionnaire contenant les données d'un objet Card.

            Return(s):
                    | data ({}): Dictionnaire contenant tous les attributs de l'objet Card

        '''
        data = {
            'id':self.id,
            'name':self.name,
            'rarity':self.rarity
        }

        return data