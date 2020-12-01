import numpy as np
import pandas as pd
from datetime import datetime


def add_dates_start_end_inplace(data):
    data['DATE_START'] = data['WEEK'].apply(lambda idx: DATES_FROM_WEEK_IDX[idx][0])
    data['DATE_END']   = data['WEEK'].apply(lambda idx: DATES_FROM_WEEK_IDX[idx][1])

def add_age_inplace(data):
    data['AGE'] = datetime.now().year - data['TBIRTH_YEAR']

def replace_codes_with_nan_inplace(data):
    data.replace(-88, np.nan, inplace=True)
    data.replace(-99, np.nan, inplace=True)