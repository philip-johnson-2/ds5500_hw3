import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import plotly.graph_objects as go


# read the base dataset
ed_data = pd.read_csv(os.path.expanduser('~/Desktop/Sdf16_1a.txt'), sep='\t')


data = ed_data[["STNAME", "TFEDREV"]].query('TFEDREV>0')
data = data.groupby(["STNAME"]).sum().reset_index()
data = data.sort_values(by="TFEDREV", ascending=False)
df = pd.DataFrame(data.sort_values(by="TFEDREV", ascending=False))
df.columns = [['State','Sum_Federal_Funding']]

fig = go.Figure(data=[go.Table(
    header=dict(values=list(df.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[df.State,df.Sum_Federal_Funding],
               fill_color='lavender',
               align='left'))
])

fig.update_layout(
    autosize=True,
    width=500,
    height=2000
)

fig.show()



states = data['STNAME'].values
revs = data['TFEDREV'].values
plt.bar(np.arange(len(states)), revs)
plt.xlabel("State Rank")
plt.ylabel("Total Funding Received in Dollars")
plt.show()




data = ed_data[["STNAME", "TOTALEXP", "V33"]].groupby(['STNAME']).sum().reset_index()
data['spend_per_student'] = round(data['TOTALEXP'] / data['V33'])
data = data.sort_values(by='spend_per_student', ascending=False)[['STNAME', 'spend_per_student']]
df = pd.DataFrame(data.sort_values(by='spend_per_student', ascending=False)[['STNAME', 'spend_per_student']])
df.columns = [['State','Spending_Per_Student']]


fig = go.Figure(data=[go.Table(
    header=dict(values=list(df.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[df.State,df.Spending_Per_Student],
               fill_color='lavender',
               align='left'))
])

fig.update_layout(
    autosize=False,
    width=500,
    height=500
)

fig.show()
