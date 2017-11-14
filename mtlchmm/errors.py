import os
import logging


_FORMAT = '%(asctime)s:%(levelname)s:%(lineno)s:%(module)s.%(funcName)s:%(message)s'
_formatter = logging.Formatter(_FORMAT, '%H:%M:%S')
_handler = logging.StreamHandler()
_handler.setFormatter(_formatter)

logging.basicConfig(filename=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'mtlchmm.log'),
                    filemode='w',
                    level=logging.DEBUG)

logger = logging.getLogger(__name__)
logger.addHandler(_handler)
logger.setLevel(logging.INFO)
