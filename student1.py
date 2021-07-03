import plotly_express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np


data = pd.read_csv("student.csv")
print(data.groupby("student_id")["attempt"].mean())
# fig = px.scatter(data, x="student_id", y="student_id",color="attempt")
# fig.show()

# fig = go.Figure(go.Bar(x=['Level 1','Level 2', "Level 3","Level 4"],y=data.groupby("level")["attempt"].mean()))
# fig.show()

# fig = go.Figure(go.Bar(x=['TRL_123','TRL_987', "TRL_abc","TRL_imb","TRL_mda","TRL_mno","TRL_rst","TRL_xsl","TRL_xyz","TRL_zet","TRL_zny"],y=data.groupby("student_id")["attempt"].mean()))
# fig.show()


data123 = data.loc[data["student_id"]=="TRL_123"]
print(data123)

fig = go.Figure(go.Bar(x=['Level 1','Level 2', "Level 3","Level 4"],y=data123.groupby("level")["attempt"].mean()))
fig.show()