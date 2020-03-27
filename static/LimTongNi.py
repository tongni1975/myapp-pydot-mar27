import numpy as np                               # vectors and matrices
import pandas as pd                              # tables and data manipulations
import matplotlib.pyplot as plt                  # plots
import seaborn as sns                            # more plots
import statsmodels

import statsmodels.formula.api as smf            # statistics and econometrics
import statsmodels.tsa.api as smt
import statsmodels.api as sm
import scipy.stats as scs

import warnings                                  # `do not disturbe` mode
warnings.filterwarnings('ignore')

df = pd.read_csv('Parmesan Cheese.csv')
df.head()

df.dtypes

df['Month'] = pd.to_datetime(df['Month'])
df.dtypes

#set datetime object as the index of the dataframe

df = df.set_index('Month')
df.head()

plt.show()