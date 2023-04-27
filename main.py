import plotly.graph_objs as go
import streamlit as st

from core.search import GridSearchProblem, breadth_first_search

st.title("Breadth-first search")
st.write(
    "This type of search is complete, but a bit brute-force. However, for small maps, breadth-first search "
    + "provides quick enough performance.")
problem = GridSearchProblem()
st.sidebar.title("Parameters")
label_col1, label_col2 = st.sidebar.columns(2, gap="small")
label_col1.caption("Start")
label_col2.caption("Goal")
col1, col2, col3, col4 = st.sidebar.columns(4, gap="small")
txt_start_x = col1.text_input("X:", value=problem.start[0])
txt_start_y = col2.text_input("Y:", value=problem.start[1])
txt_goal_x = col3.text_input("X:", value=problem.goal[0])
txt_goal_y = col4.text_input("Y:", value=problem.goal[1])

new_start = int(txt_start_x), int(txt_start_y)
new_goal = int(txt_goal_x), int(txt_goal_y)
problem = GridSearchProblem(start=new_start, goal=new_goal)
soln = breadth_first_search(problem)
# st.text(problem.plotSolution(path))
island = problem.getGridPoints()
xs = [x for x, _ in island]
ys = [y for _, y in island]
land = go.Scatter(name="Terrain",
                  x=xs,
                  y=ys,
                  mode='markers',
                  marker=dict(showscale=False,
                              color='green',
                              size=20,
                              line=dict(width=0)))
xs = [x for x, _ in soln[::-1]]
ys = [y for _, y in soln[::-1]]
path = go.Scatter(name="Solution path",
                  x=xs,
                  y=ys,
                  mode='markers',
                  marker=dict(showscale=False,
                              color='mediumslateblue',
                              size=20,
                              line=dict(width=0)))
start = go.Scatter(name="Start",
                   x=[int(txt_start_x)],
                   y=[int(txt_start_y)],
                   text='S',
                   textposition='middle center',
                   mode='markers+text',
                   marker=dict(showscale=False,
                               color='blue',
                               size=20,
                               line=dict(width=0)))
goal = go.Scatter(name="Goal",
                  x=[int(txt_goal_x)],
                  y=[int(txt_goal_y)],
                  text='G',
                  textposition='middle center',
                  mode='markers+text',
                  marker=dict(showscale=False,
                              color='purple',
                              size=20,
                              line=dict(width=0)))
fig = go.Figure(data=[land, path, start, goal],
                layout=go.Layout(hovermode='closest',
                                 xaxis=dict(showgrid=False,
                                            zeroline=False,
                                            showticklabels=False),
                                 yaxis=dict(showgrid=False,
                                            zeroline=False,
                                            autorange='reversed',
                                            showticklabels=False)))
st.plotly_chart(fig, use_container_width=True)
st.write(f"Path: {soln}")
