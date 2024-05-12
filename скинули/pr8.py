# import plotly.graph_objects as go
# import numpy as np
# N = 1000000
# fig = go.Figure(data = go.Scattergl(
#     x = np.random.randn(N),
#     y = np.random.randn(N),
#     mode = 'markers',
    
#     marker = dict(
#         color = np.random.randn(N),
#         #colorscale = 'Viridis',
#         #colorscale = 'Reds',
#         colorscale = 'gnbu',
#         line_width = 1
#     )
#     )
#     )
# fig.show()



import plotly.graph_objects as go
import numpy as np
np.random.seed(1)
y0 = np.random.randn(50)
y1 = np.random.randn(50)
y2 = np.random.randn(50)
y3 = np.random.randn(50)
y4 = np.random.randn(50)

fig = go.Figure()
fig.add_trace(go.Box(y=y0))
fig.add_trace(go.Box(x=y1))
fig.add_trace(go.Box(y=y1))
fig.add_trace(go.Box(y=y2))
# fig.add_trace(go.Box(x=y3))
# fig.add_trace(go.Box(y=y3))
# fig.add_trace(go.Box(y=y4))


fig.show()