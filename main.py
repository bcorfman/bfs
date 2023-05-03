import plotly.graph_objs as go
import streamlit as st

from core.parser import MAX_GRID_WIDTH
from core.search import GridSearchProblem, breadth_first_search

st.set_page_config(page_title='Breadth-first search app')
st.title("Breadth-first search")
st.write(
    "This type of search always finds the shortest path to the goal, but it's a brute-force, uninformed search. "
    +
    "Compared to an informed heuristic search like A-star, breadth-first search is a slower performer, but on "
    + "small maps, it does just fine.")
problem = GridSearchProblem()
st.sidebar.title("Parameters")
label_col1, label_col2 = st.sidebar.columns(2, gap="small")
label_col1.caption("Start")
label_col2.caption("Goal")
col1, col2, col3, col4 = st.sidebar.columns(4, gap="small")
txt_start_x = col1.number_input("X:",
                                format="%d",
                                min_value=1,
                                max_value=MAX_GRID_WIDTH,
                                value=problem.start[0])
txt_start_y = col2.number_input("Y:",
                                format="%d",
                                min_value=1,
                                max_value=MAX_GRID_WIDTH,
                                value=problem.start[1])
txt_goal_x = col3.number_input("X:",
                               format="%d",
                               min_value=1,
                               max_value=MAX_GRID_WIDTH,
                               value=problem.goal[0])
txt_goal_y = col4.number_input("Y:",
                               format="%d",
                               min_value=1,
                               max_value=MAX_GRID_WIDTH,
                               value=problem.goal[1])

new_start = int(txt_start_x), int(txt_start_y)
new_goal = int(txt_goal_x), int(txt_goal_y)
problem = GridSearchProblem(start=new_start, goal=new_goal)
soln = breadth_first_search(problem)
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
if soln is not None:
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
else:
    path = go.Scatter(x=[], y=[])
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
if soln is not None:
    st.write(f"Path: {soln}")
else:
    st.write("Path: No solution found. Outside map boundary.")
