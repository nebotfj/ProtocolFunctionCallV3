"""DEX Protocols Package"""

from .pancakeswap import PANCAKESWAP_FUNCTIONS
from .raydium import RAYDIUM_FUNCTIONS
from .orca import ORCA_FUNCTIONS
from .apeswap import APESWAP_FUNCTIONS
from .biswap import BISWAP_FUNCTIONS

# Update DEX_PROTOCOLS dictionary with new protocols
DEX_PROTOCOLS.update({
    'PANCAKESWAP': PANCAKESWAP_FUNCTIONS,
    'RAYDIUM': RAYDIUM_FUNCTIONS,
    'ORCA': ORCA_FUNCTIONS,
    'APESWAP': APESWAP_FUNCTIONS,
    'BISWAP': BISWAP_FUNCTIONS
})