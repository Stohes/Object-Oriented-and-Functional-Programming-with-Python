from dataclasses import dataclass
from datetime import datetime


@dataclass
class Habit:
    name: str
    periodicity: str
    created_at: datetime
    completion_dates: list
    
    
    def complete_task(self):
        pass
    
    
    def is_broken(self):
        pass
    
    
    def streak(self):
        pass