''' Process Data for further modules.

This package will just work if
there is data available on your
filesystem provided by riotcrawlers.

Notes
-----
If you want to have a look at
riotcrawlers:
    .. _riotcrawlers Github Repository:
        https://github.com/rioterz/riotcrawlers


Attributes
----------
HOME : str
    Path to the
    Home Directory.
PATH : str
    Path to Data.
'''

import os
import json
from pathlib import Path

# Third Party Imports
#
try:
    import pandas as pd
except ImportError:
    print('python3 -m pip install pandas')

# Check that it is the same path
# as in the riotcrawlers package.
HOME = str(Path.home())
PATH = f'{HOME}/Riotz/'

if not os.path.exists(PATH):
    print('Did not found Path.')


def choose_file() -> str:
    ''' Choose the file to get Data.

    There will be more files in the
    directory, this function will
    provide the correct data.

    Returns
    -------
    str
        The File for further pro
        cessings.
    '''
    path_contains = os.listdir(PATH)
    for files in path_contains:
        if '.json' in files:
            return str(PATH + files)

def load_data() -> list[dict]:
    ''' Data Loader

    Loading the Data from the file.

    Returns
    -------
    data_dict_list : list[dict]
        List of all Data re-
        presented by dicts.
    '''
    data_file = choose_file()
    data = []

    with open(data_file, 'rb') as data_f:
        data_list = data_f.readlines()

    for item in data_list:
        data.append(json.loads(item))

    return data

def data_as_dataframe() -> pd.DataFrame:
    ''' Data as pd.DataFrame

    Returns
    -------
        : pd.DataFrame
        Returns the data as a pandas
        DataFrame.
    '''
    return pd.DataFrame.from_dict(load_data())
