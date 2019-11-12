import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import plotly.graph_objects as go

# read the base dataset
ed_data = pd.read_csv(os.path.expanduser('~/Desktop/Sdf16_1a.txt'), sep='\t')


data = ed_data[['LEAID', 'TOTALREV', 'TOTALEXP']].query('TOTALREV>0')
plt.plot(data['TOTALREV'],data['TOTALEXP'],'o')
plt.xlabel("Revenue")
plt.ylabel("Expense")
plt.show()


data = ed_data[['STNAME','TOTALREV','TOTALEXP','V33']].copy()
data = data.groupby(['STNAME']).sum().reset_index()
data['total_debt'] = data['TOTALREV'] - data['TOTALEXP']
data['debt_per_student'] = round(data['total_debt'] / data['V33']).fillna(0)
data = data.sort_values(by='debt_per_student', ascending=False)[['STNAME', 'debt_per_student']]
df = pd.DataFrame(data.sort_values(by='debt_per_student', ascending=False)[['STNAME', 'debt_per_student']])
df.columns = [['State','Debt_per_Student']]

fig = go.Figure(data=[go.Table(
    header=dict(values=list(df.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[df.State,df.Debt_per_Student],
               fill_color='lavender',
               align='left'))
])

fig.update_layout(
    autosize=False,
    width=500,
    height=500
)

fig.show()
