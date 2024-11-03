import streamlit as st


pg = st.navigation([
    st.Page("streamlit_pages/habits_list.py", title="Habits List"), 
    st.Page("streamlit_pages/create_habit.py", title="Create Habit")
])

pg.run()