import streamlit as st
from HabitManager import HabitManager


st.title("Habits List")


habitManager = HabitManager()

habit_list = habitManager.habits
for habit in habit_list:
    st.code(
        f"""
        Name: {habit.name}
        Periodicity: {habit.periodicity_string}
        Current Streak: {habit.current_streak}
        Max Streak: {habit.max_streak}
        Completion Dates: {habit.completion_dates}
        """
    )