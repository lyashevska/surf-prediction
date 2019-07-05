import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from erddapy import ERDDAP
import pandas as pd
import seaborn as sns
sns.set(rc={'figure.figsize': (11, 4)})


e = ERDDAP(
    server='https://erddap.marine.ie/erddap',
    protocol='tabledap',
)

e.dataset_id = 'IWBNetwork'

e.constraints = {
    'time>=': '2015-06-28T00:00:00Z',
    'station_id=': 'M3'
}

e.variables = [
    'time',
    'AtmosphericPressure',
    'WindDirection',
    'WindSpeed',
    'WaveHeight',
    'WavePeriod',
    'MeanWaveDirection',
    # 'Hmax',
    # 'AirTemperature',
    'SeaTemperature'
]


url = e.get_download_url()

print(url)

df = e.to_pandas(
    index_col='time (UTC)',
    parse_dates=True).dropna()

df.shape

df.columns

cols = ['AtmosphericPressure', 'WindDirection', 'WindSpeed',
        'WaveHeight', 'WavePeriod', 'MeanWaveDirection', 'SeaTemperature']

# rename columns
df.columns = cols

df.dtypes

df.index

plt.scatter(df.WaveHeight, df.WavePeriod, marker='.')


df['Year'] = df.index.year
df['Month'] = df.index.month
df['Day'] = df.index.day

df.head()

# today
df.loc['2019-07-05']

cols_plot = ['WindDirection', 'WaveHeight', 'WavePeriod', 'SeaTemperature']
axes = df[cols_plot].loc['2019'].plot(
    marker='.', alpha=0.5, linestyle='None', figsize=(11, 9), subplots=True)
for ax in axes:
    ax.set_ylabel('')


df.columns
# indicator variables
# WindDirection Easterly 60-120
# WaveHeight if 0.5-3 -> 1, otherwise 0
# MeanWaveDirection SW - NW


cols_plot = ['SeaTemperature']
axes = df[cols_plot].plot(
    marker='.', alpha=0.5, linestyle='None', figsize=(11, 9), subplots=True)
for ax in axes:
    ax.set_ylabel('')
