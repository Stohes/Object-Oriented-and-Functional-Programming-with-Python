import streamlit as st


pg = st.navigation([
    st.Page("streamlit_pages/home.py", title="Home"), 
    st.Page("streamlit_pages/create_habit.py", title="Create Habit")
])

pg.run()