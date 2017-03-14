## IMPORTS

import re

from config.manager import ConfigManager
from cvars import ConVar
from events import Event
from filters.players import PlayerIter
from filters.weapons import WeaponClassIter
from engines.server import global_vars
from listeners import OnServerActivate, OnLevelEnd, OnLevelInit
from messages import HintText
from messages import SayText2
from players.entity import Player
from weapons.restrictions import WeaponRestrictionHandler

from .configs import *
from .info import info


## GLOBALS

restrict_handler = WeaponRestrictionHandler()
weapon_restrict_ct = []
weapon_restrict_t = []
cvar_list = dict()


## UTILS

def load_map_config(map_name):
    map_config = CONFIG_PATH / map_name + '.cfg'
    g_configs_map.clear()
    with open(map_config) as f:
        for line in f:
            line = line.strip()

            if not line or line.startswith('//'):
                continue

            key, value = line.split(' ')
            g_configs_map[key] = value

    parse_config(g_configs_map)


def parse_config(config):
    for key in config:
        try:
            value = int(config[key])  
        except TypeError: 
            value = config[key].get_int()

        if key.find('restrict') != -1 and value == 1:
            useless, weapon, team = key.split('_')
            if team == 'ct' and weapon not in weapon_restrict_ct:
                weapon_restrict_ct.append(weapon) 
            elif team == 't' and weapon not in weapon_restrict_t:
                weapon_restrict_t.append(weapon)
        elif key.find('restrict') == -1:
            cvar_list[key] = config[key]


def set_cvar_value(cvar):
    value = cvar_list[cvar]
    if value.isdigit():
        ConVar(cvar).set_int(int(value))

    if re.match("^\d+?\.\d+?$", value) is not None:
        ConVar(cvar).set_float(float(value))

    if re.match("[^a-zA-Z]", value) is None:
        ConVar(cvar).set_string(value)

    return False


## GAME EVENT

@OnLevelInit
def _on_map_start(map_name):
    restrict_handler.remove_team_restrictions(3, *_all_weapons)
    restrict_handler.remove_team_restrictions(2, *_all_weapons)

    weapon_restrict_ct = []
    weapon_restrict_t = []
    g_configs_map.clear()
    cvar_list.clear()

    # Get default config
    parse_config(g_configs)

    # Get default config
    map_file = CONFIG_PATH / map_name + '.cfg'
    print(str(map_file.isfile()))
    if map_file.isfile():
        load_map_config(map_name)
        parse_config(g_configs_map)


@OnServerActivate
def on_server_activate(edicts, edict_count, max_clients):
    for cvar in cvar_list:
        set_cvar_value(cvar)

    # Add restriction
    if len(weapon_restrict_ct) != 0:
        restrict_handler.add_team_restrictions(3, *weapon_restrict_ct)

    if len(weapon_restrict_t) != 0:
        restrict_handler.add_team_restrictions(2, *weapon_restrict_t)


@OnLevelEnd
def _on_map_end():
    restrict_handler.remove_team_restrictions(3, *_all_weapons)
    restrict_handler.remove_team_restrictions(2, *_all_weapons)

