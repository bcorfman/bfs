import streamlit as st

from core.search import GridSearchProblem, breadth_first_search

st.title("Breadth-first search")
problem = GridSearchProblem()
st.write(f"Start: {problem.start}")
st.write(f"Goal: {problem.goal}")
path = breadth_first_search(problem)
st.write(f"Path: {path}")
st.write(problem.plotSolution(path))
