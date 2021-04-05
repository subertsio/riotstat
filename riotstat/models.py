''' Data Models

Models are representing Data and/or
relation of Data, which can be used
for plotting in the bokeh library.
'''

from riotstat.dataloader import data_as_dataframe

try:
    from bokeh.plotting import figure, show
    from bokeh.models import ColumnDataSource
except ImportError:
    print('python3 -m pip install bokeh')


# Define imported Data Frame.
#
DATA = data_as_dataframe()

# More Variables:
#
ITEMS = len(DATA)
#FIRST_DATE = DATA['date'][0]
#LAST_DATE = DATA['date'][ITEMS]


class _Model:
    ''' Model for all Plots
    '''

    def __plot__(self):
        ...

    def __save__(self):
        ...


class FrequencyByMonth:
    ''' Frequency by Month
    '''
    ...        


class FrequencyTimeline:
    ''' Frequency of All
    '''
    ...


class FrequencyCity:
    ''' Frequency of Cities

    '''
    cities = DATA['location']
    dates = DATA['date']

    def plot(self) -> None:
        ''' Plot
        '''
        fig = figure()
        #fig.line(x, y)

