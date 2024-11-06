import streamlit as st
from HabitManager import HabitManager


st.title("Complete Habit")


habitManager = HabitManager()
                
habit_list = habitManager.habits
for habit in habit_list:
    
    habit_name = habit.name
    complete_button = st.button(label=habit_name)
    
    if complete_button:
        habitManager.complete_habit(habit_name)
        st.write(f"Habit {habit.name} Successfully Completed")