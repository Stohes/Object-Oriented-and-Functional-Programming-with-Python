import streamlit as st
from HabitManager import HabitManager


st.title("Complete Habit")


habitManager = HabitManager()

with st.form("Complete Habit"):
    name = st.text_input(label="Name")

    submitted = st.form_submit_button(label="Complete")
    
    if submitted:
        habitManager.complete_habit(name=name)
        st.write(f"Habit Successfully Completed")