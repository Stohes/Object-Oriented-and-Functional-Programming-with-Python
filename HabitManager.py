from dataclasses import dataclass, field
from Habit import Habit
import pickle


@dataclass
class HabitManager:
    habits: list = field(default_factory=list)
    
    
    def __post_init__(self):
        self.load_habits()
    
    
    def create_habit(self, name, periodicity):
        new_habit = Habit(name, periodicity)
        self.habits.append(new_habit)
        
    
    def delete_habit(self, name):
        for habit in self.habits:
            if habit.name == name:
                del habit
                return  # maybe add confirmation message
    
    
    def list_habits(self):
        for habit in self.habits:
            print(habit)
    
    
    def list_habits_by_periodicity(self):
        print(self.get_daily_habits())
        print(self.get_weekly_habits())
        print(self.get_monthly_habits())
            
        
    def get_daily_habits(self):
        return [habit for habit in self.habits if habit.periodicity_string == "Daily"]


    def get_weekly_habits(self):
        return [habit for habit in self.habits if habit.periodicity_string == "Weekly"]


    def get_monthly_habits(self):
        return [habit for habit in self.habits if habit.periodicity_string == "Monthly"]
        

    def complete_habit(self, name):
        pass
    
    
    def save_habits(self):
        with open("data.pkl", "wb") as file:
            pickle.dump(self.habits, file)
    
    
    def load_habits(self):
        with open("data.pkl", "rb") as file:
            self.habits = pickle.load(file)
            