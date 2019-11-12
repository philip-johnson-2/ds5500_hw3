import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import plotly.graph_objects as go

# read the base dataset
ed_data = pd.read_csv(os.path.expanduser('~/Desktop/Sdf16_1a.txt'), sep='\t')


# get total fed spending 
total = sum(ed_data['TFEDREV'])
percent_15_total = float(total) * .15
print(total)
print(percent_15_total)


data = ed_data[['LEAID','STNAME','TFEDREV']]
data['Updated Funding'] = data['TFEDREV'] *  .85
df = pd.DataFrame((data[['LEAID','STNAME','Updated Funding']].sort_values('Updated Funding', ascending=False).head(15).reset_index(drop=True)))
df.columns = ['LEAID','State','Updated_Funding_Amount']

fig = go.Figure(data=[go.Table(
    header=dict(values=list(df.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[df.LEAID,df.State,df.Updated_Funding_Amount],
               fill_color='lavender',
               align='left'))
])

fig.update_layout(
    autosize=False,
    width=500,
    height=500
)

fig.show()