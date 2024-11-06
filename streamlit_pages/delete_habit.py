import streamlit as st
from HabitManager import HabitManager


st.title("Delete Habit")


habitManager = HabitManager()

habit_list = habitManager.habits
for habit in habit_list:
    
    habit_name = habit.name
    delete_button = st.button(label=habit_name)
    
    if delete_button:
        habitManager.delete_habit(habit_name)
        st.rerun()