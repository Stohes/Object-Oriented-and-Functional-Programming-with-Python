import streamlit as st
from HabitManager import HabitManager


st.title("Create Habit")


habitManager = HabitManager()

with st.form("Create Habit"):
    name = st.text_input(label="Name")
    periodicity = st.selectbox(label="Periodicity", options=["Daily", "Weekly", "Monthly"])

    submitted = st.form_submit_button(label="Create")
    
    if submitted:
        habitManager.create_habit(
            name=name,
            periodicity=periodicity
        )
        st.write(f"New Habit Successfully Created")