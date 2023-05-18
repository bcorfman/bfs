import plotly.graph_objs as go
import streamlit as st

from core.parser import MAX_GRID_HEIGHT, MAX_GRID_WIDTH
from core.search import GridSearchProblem, breadth_first_search

st.set_page_config(page_title='Breadth-first search app')
st.title("Grid map search")
st.write(
    "Breadth-first search (BFS) is always complete and finds the shortest path to the goal, but it's also uninformed. "
    +
    "Compared to an informed heuristic search like A*, BFS can be a slower performer, but on "
    + "small maps it does just fine.")
problem = GridSearchProblem()
st.sidebar.title("Parameters")
label_col11, label_col12 = st.sidebar.columns(2, gap="small")
label_col11.caption("Start")
col11, col12 = st.sidebar.columns(2, gap="small")
# create a placeholder so we can redefine the Y input later once
# the map height is known
start_x_placeholder = col11.empty()
start_y_placeholder = col12.empty()

label_col21, label_col22 = st.sidebar.columns(2, gap="small")
label_col21.caption("Goal")
col21, col22 = st.sidebar.columns(2, gap="small")
# create a placeholder so we can redefine the Y input later once
# the map height is known
goal_x_placeholder = col21.empty()
goal_y_placeholder = col22.empty()

# pulling start and goal coordinates from the text boxes since the
# number widgets prevent input errors from occurring
new_start = int(problem.start[0]), int(problem.start[1])
new_goal = int(problem.goal[0]), int(problem.goal[1])
problem = GridSearchProblem(start=new_start, goal=new_goal)
soln = breadth_first_search(problem)
# revise max Y inputs to actual grid height once it's been read in
grid_height = problem.getGridHeight()
txt_start_x = col11.number_input("X:",
                                 format="%d",
                                 min_value=1,
                                 max_value=MAX_GRID_WIDTH,
                                 value=problem.start[0])
txt_start_y = start_y_placeholder.number_input("Y:",
                                               format="%d",
                                               min_value=1,
                                               max_value=grid_height + 1,
                                               value=problem.start[1])
txt_goal_x = goal_x_placeholder.number_input("X:",
                                             format="%d",
                                             min_value=1,
                                             max_value=MAX_GRID_WIDTH,
                                             value=problem.goal[0])
txt_goal_y = goal_y_placeholder.number_input("Y:",
                                             format="%d",
                                             min_value=1,
                                             max_value=grid_height + 1,
                                             value=problem.goal[1])
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
