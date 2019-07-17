from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet

import sys
sys.path.insert(0, '../')

import actions

import tmdbsimple as tmdb
tmdb.API_KEY = '4e451d47079417d82742022a3cf54988'

