from dataclasses import dataclass
from Habit import Habit
import json


@dataclass
class Habit_Manager:
    
    
    def create_habit(self, name, periodicity):
        pass
    
    
    def delete_habit(self, name):
        pass
    
    
    def list_habits(self):
        pass
    
    
    def list_habits_by_periodicity(self):
        pass


    def complete_habit(self, name):
        pass
    
    
    def load_habits(self):
        pass