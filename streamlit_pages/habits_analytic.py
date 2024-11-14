import streamlit as st
import Analytics
from HabitManager import HabitManager


st.title("Habits Analytic")


habitManager = HabitManager()
habit_list = habitManager.habits


st.write(
    f"Longest Streak: {Analytics.longest_streak(habit_list)}"
)


st.write(
    f"Most Struggled Habits: {Analytics.most_struggled_habits(habit_list)}"
)


st.write(
    f"Current Habits: {Analytics.current_habits(habit_list)}"
)