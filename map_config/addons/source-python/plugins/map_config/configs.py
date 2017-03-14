## IMPORTS

from config.manager import ConfigManager
from filters.weapons import WeaponClassIter
from paths import CFG_PATH
from translations.strings import LangStrings

from .info import info

## ALL DECLARATION

__all__ = (
    '_weapons',
    '_all_weapons',
    'CONFIG_PATH',
    'g_configs',
    'g_configs_map',
)

## GLOBALS

_weapons = [
    item.name.split('_')[1] for item in WeaponClassIter(not_filters= ['knife','objective'])
]

_all_weapons = set(weapon.name for weapon in WeaponClassIter())

CONFIG_PATH = CFG_PATH / 'map_config'
g_configs = dict()
g_configs_map = dict()



with ConfigManager(info.name) as _config:
    #
    #   Displaying informations
    #
    _config.section('Restrictions')

    for weapon in _weapons:
        g_configs['restrict_' + weapon + '_ct'] = _config.cvar(
            'restrict_' + weapon + '_ct', 0,
            '1 - Restricted | 0 - Not restricted', 0) 

        g_configs['restrict_' + weapon + '_t'] = _config.cvar(
            'restrict_' + weapon + '_t', 0,
            '1 - Restricted | 0 - Not restricted', 0) 
