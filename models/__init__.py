'''
Fichier contenant les fonctions utiles à la manipulation du thesaurus.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Fonctions:

   | create_db()
   | pop_cards()
'''

import peewee

from server import db
from .card.card import Card
from .theft.theft import Theft
from .user.user import User
from .vault.vault import Vault

def create_db():
    '''
    Crée les tables au niveau de la base de données.   
    '''
    db.create_tables([
        Theft,
        Vault,
        Card,
        User,
        User.inventory.get_through_model()
        ])

def pop_cards():
    """
    initialise les cartes
    attention, ne plus toucher une fois défini
    ne pas corriger les index
    si nouvelle reference, ajouter sur le tas
    """
    
    for idx, name, rarity in [
            (1, 'barriere_chantier', 'common'),
            (2, 'cable_iphone_casse', 'common'),
            (3, 'chat_mignon', 'common'),
            (4, 'esc_key', 'common'),
            (5, 'extincteur', 'common'),
            (6, 'latte_lit', 'common'),
            (7, 'mcdo_toy', 'common'),
            (8, 'panneau_routier', 'common'),
            (9, 'plot_de_chantier', 'common'),
            (10, 'pot_a_eau', 'common'),
            (11, 'ressort', 'common'),
            (12, 'rj45', 'common'),
            (13, 'vaisselle_mcdo', 'common'),
            (14, 'vis_chaise', 'common')]:
        try:
            Card.create(id=idx, name=name, rarity=rarity)
        except peewee.IntegrityError:
            print ('%s - %s déja existant' % (idx, name))