import streamlit as st


pg = st.navigation([
    st.Page("streamlit_pages/habits_list.py", title="Habits List"), 
    st.Page("streamlit_pages/complete_habit.py", title="Complete Habit"),
    st.Page("streamlit_pages/create_habit.py", title="Create Habit"),
    st.Page("streamlit_pages/delete_habit.py", title="Delete Habit")
])

pg.run()