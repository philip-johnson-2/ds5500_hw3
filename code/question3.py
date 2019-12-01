import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import plotly.graph_objects as go

# read the base dataset
ed_data = pd.read_csv(os.path.expanduser('~/Desktop/Sdf16_1a.txt'), sep='\t', low_memory=False)
math_data = pd.read_csv(os.path.expanduser('~/Desktop/math-achievement-lea-sy2015-16.csv'), low_memory=False)


# function for cleaning data
def clean_data(field):
    """ 
    Function to take a column and covert non-numeric values into numeric values to account 
    for range values in the data as well as account for greater than and less than 
    symbols in the data. For ranges, I take the average numeric value within the range. 
    For greater then and less then strings I use 0 or 100 to determin average value.
    Other values that do not have a numeric definition get converted to NA.
    """
    num = field

    for i in range(len(num)):
        if num[i] == '.': # convert to NA
            value = np.nan
        
        elif num[i] == 'PS': # convert to NA
            value = np.nan

        elif num[i] == ' ': # convert to NA
            value = np.nan
        
        elif num[i].count('-') > 0: # get range values
            y = num[i].split("-")
            value = np.mean([int(y[0]),int(y[1])])
        
        elif num[i][0:2] == 'LE': # less than or equal to
            x = float(num[i].lstrip('LE'))
            value = np.mean([0,int(x)])
        elif num[i][0:2] == 'GE': # greater than or equal to
            x = float(num[i].lstrip('GE'))
            value = np.mean([int(x),100])
        elif num[i][0:2] == 'LT': # less than
            x = float(num[i].lstrip('LT'))
            value = np.mean([0,int(x)])
        elif num[i][0:2] == 'GT': # greater than
            x = float(num[i].lstrip('GT'))
            value = np.mean([int(x),100])
           
        else:
            value = int(num[i])
        
        num[i] = value

        
    return num
        



math_scores = clean_data(math_data['ALL_MTH00PCTPROF_1516'])
print(math_scores)
plt.hist(math_scores.values, bins=20)
plt.xlabel("% of Students Scoring Proficient in Math")
plt.ylabel("Count of Districts")
plt.show()

