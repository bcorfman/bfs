import streamlit as st

from core.search import GridSearchProblem, breadth_first_search

st.title("Breadth-first search")
problem = GridSearchProblem()
st.sidebar.title("Parameters")
label_col1, label_col2 = st.sidebar.columns(2, gap="small")
label_col1.caption("Start")
label_col2.caption("Goal")
col1, col2, col3, col4 = st.sidebar.columns(4, gap="small")
txt_start_x = col1.text_input("X:", value=problem.start[1])
txt_start_y = col2.text_input("Y:", value=problem.start[0])
txt_goal_x = col3.text_input("X:", value=problem.goal[1])
txt_goal_y = col4.text_input("Y:", value=problem.goal[0])

new_start = int(txt_start_y), int(txt_start_x)
new_goal = int(txt_goal_y), int(txt_goal_x)
problem = GridSearchProblem(start=new_start, goal=new_goal)
path = breadth_first_search(problem)
st.text(problem.plotSolution(path))
st.write(f"Path: {path}")
