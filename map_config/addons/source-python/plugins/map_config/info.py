## IMPORTS

from plugins.manager import plugin_manager

## ALL DECLARATION

__all__ = (
    'info',
)

info = plugin_manager.get_plugin_info(__name__)