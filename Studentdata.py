import pandas as pd
import sqlite3

import logging
logger = logging.getLogger()

logging.basicConfig(
    filename=r'C:\Users\chr08\Documents\Notebook\logfile1.log',
    format='[%(asctime)s][%(levelname)s] %(message)s',
    level=logging.DEBUG,
    datefmt= '%Y-%m-%d %H:%M:%S')

logger.debug('This is a debug-level log record.')
logger.info('This is an info-level log record.')
logger.warning('I have a bad feeling about this...')

con = sqlite3.connect('studentlife.db')

df = pd.read_csv(r'C:\Users\chr08\anaconda3\student_lifestyle_dataset.csv', index_col=False)

df['Sleep_Hours_Per_Day'] = 10

