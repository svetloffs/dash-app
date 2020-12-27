# %%
import pandas as pd
from pandas_datareader import data as web

from datetime import datetime as dt
import datetime
import time

import numpy as np

# %%
np.random.seed(0)
# установим начальную дату наблюдения (сегодня) 
# установим период наблюедния =365 дней
# вычислим начальную точку наблюдения start_date
Time_view = 10
end_date = dt.today()
delta = datetime.timedelta(days = 365 * Time_view)
start_date = end_date - delta
# print('Start_date:', start_date)
# print('End_date:', end_date)
# datetime.strptime("2015-08-10 19:33:27.653", "%Y-%m-%d %H:%M:%S.%f")
# str_today = str(dt.today().year) + '-' + str(dt.today().month) + '-' + str(dt.today().day)
rng = pd.date_range(start_date, periods = int(delta.days) // 30, freq = 'm')
data = pd.DataFrame({'date': rng, 'Sales': np.random.randint(0, 100, len(rng))})
data

# %%
