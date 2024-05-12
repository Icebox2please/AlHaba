# import plotly.express as px
# df = px.data.gapminder()
# fig = px.scatter_geo(df, locations='iso_alpha', color = 'continent'
#     ,hover_name = 'country', size = 'pop', animation_frame= 'year', projection ='natural earth')
# fig.show()

# import numpy as np
# import plotly.figure_factory as ff
# x1, y1 = np.meshgrid(np.arange(0, 54, .99), np.arange(0, 54, .99))

# u1 = np.cos(x1) * y1
# v1 = np.sin(x1) * y1

# fig = ff.create_quiver(x1, y1, u1, v1)

# fig.show()

from plotly.subplots import make_subplots

fig = make_subplots(rows=1, cols=2)

fig.add_scatter(y=[4, 2, 3.5], mode="markers",

marker = dict(size=20, color="LightSeaGreen"), name="a", row=1, col=1)

fig.add_bar(y =[4, 2, 3.5], marker = dict(color="MediumPurple"), name="b", row=1, col=1)

fig.add_scatter(y =[4, 2, 3.5], mode="markers",

marker = dict(size=20, color="MediumPurple"), name="c", row=1, col=1)

fig.add_bar(y =[4, 2, 3.5],

marker = dict(color="LightSeaGreen"),

name="d", row=1, col=1)

fig.show()