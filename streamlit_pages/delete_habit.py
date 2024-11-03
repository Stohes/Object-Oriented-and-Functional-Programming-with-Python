import streamlit as st
from HabitManager import HabitManager


st.title("Delete Habit")


habitManager = HabitManager()

with st.form("Delete Habit"):
    name = st.text_input(label="Name")

    submitted = st.form_submit_button(label="Delete")
    
    if submitted:
        habitManager.delete_habit(name=name)
        st.write(f"Habit Successfully Deleted")