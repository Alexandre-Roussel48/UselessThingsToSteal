from peewee import *

from server import BaseModel
from datetime import date

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
    next_card = DateField(default=date.today())
    next_theft = DateField(default=date.today())

    def toDict(self):
        '''
        Retourne un dictionnaire contenant les données d'un objet User.

            Return(s):
                    | data ({}): Dictionnaire contenant tous les attributs de l'objet User

        '''
        data = {
            'id':self.id,
            'username':self.username,
            'next_card':self.next_card,
            'next_theft':self.next_theft
        }

        return data