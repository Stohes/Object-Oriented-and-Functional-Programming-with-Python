import pickle
from datetime import datetime, timedelta
from Habit import Habit


# Pre-populated Habits
habits = [
    # Successful habits
    Habit(
        name="Meditation",
        periodicity_string="Daily",
        completion_dates=[
            datetime.now() - timedelta(days=i) for i in range(7)
        ],  # Completed for the past 7 days
        current_streak=7,
        max_streak=7
    ),
    Habit(
        name="Exercise",
        periodicity_string="Weekly",
        completion_dates=[
            datetime.now() - timedelta(weeks=i) for i in range(4)
        ],  # Completed for the past 4 weeks
        current_streak=4,
        max_streak=4
    ),
    # Struggled habits
    Habit(
        name="Journaling",
        periodicity_string="Daily",
        completion_dates=[
            datetime.now() - timedelta(days=i) for i in [0, 4, 8]
        ],  # Gaps of 4 days each, indicating missed completions
        current_streak=1,
        max_streak=2
    ),
    Habit(
        name="Reading",
        periodicity_string="Weekly",
        completion_dates=[
            datetime.now() - timedelta(weeks=i) for i in [0, 3, 6]
        ],  # Gaps of 3 weeks each, indicating missed completions
        current_streak=1,
        max_streak=2
    ),
    # New habit with no completions
    Habit(
        name="Cooking",
        periodicity_string="Monthly",
        completion_dates=[],
        current_streak=0,
        max_streak=0
    ),
]


with open("data.pkl", "wb") as file:
    pickle.dump(habits, file)

print("Habits pre-populated and saved to data.pkl!")
