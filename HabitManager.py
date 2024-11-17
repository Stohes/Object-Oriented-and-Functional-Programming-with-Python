from dataclasses import dataclass, field
from Habit import Habit
import pickle


@dataclass
class HabitManager:
    habits: list[Habit] = field(default_factory=list)
    
    
    def __post_init__(self):
        self.load_habits()
    
    
    def create_habit(self, name, periodicity):
        new_habit = Habit(name, periodicity)
        self.habits.append(new_habit)
        self.save_habits()
        
    
    def delete_habit(self, name):
        habit = self.find_habit(name)
        self.habits.remove(habit)
        self.save_habits()
        

    def complete_habit(self, name):
        habit = self.find_habit(name)
        
        if habit.is_broken():
            habit.reset_streak()
        
        habit.complete_task()
        habit.increase_streak()
        self.save_habits()
    
    
    def find_habit(self, name):
        for habit in self.habits:
            if habit.name == name:
                return habit
            
    
    def save_habits(self):
        with open("Code/data.pkl", "wb") as file:
            pickle.dump(self.habits, file)
    
    
    def load_habits(self):
        with open("Code/data.pkl", "rb") as file:
            self.habits = pickle.load(file)
            