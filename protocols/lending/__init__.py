"""Update Lending Protocols Package"""

from .euler import EULER_FUNCTIONS
from .benqi import BENQI_FUNCTIONS
from .venus import VENUS_FUNCTIONS
from .cream import CREAM_FUNCTIONS
from .iron_bank import IRON_BANK_FUNCTIONS
from .maple import MAPLE_FUNCTIONS
from .morpho import MORPHO_FUNCTIONS

LENDING_PROTOCOLS = {
    'EULER': EULER_FUNCTIONS,
    'BENQI': BENQI_FUNCTIONS,
    'VENUS': VENUS_FUNCTIONS,
    'CREAM': CREAM_FUNCTIONS,
    'IRON_BANK': IRON_BANK_FUNCTIONS,
    'MAPLE': MAPLE_FUNCTIONS,
    'MORPHO': MORPHO_FUNCTIONS
}