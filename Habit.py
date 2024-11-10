from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Habit:
    name: str
    periodicity_string: str
    created_at: datetime = datetime.now()
    completion_dates: list = field(default_factory=list)
    current_streak: int = 0
    max_streak: int = 0
    
    
    def complete_task(self):
        current_date = datetime.now()
        self.completion_dates.append(current_date)
        
    
    def is_broken(self):
        if len(self.completion_dates) == 0:
            return False
        
        last_completion = self.completion_dates[-1]
        current_date = datetime.now()
        
        delta = current_date - last_completion
        
        periodicity_int = self.get_periodicity_int(self.periodicity_string)
        
        return delta.days > periodicity_int
            
    
    def increase_streak(self):
        self.current_streak += 1
        self.max_streak = max(self.current_streak, self.max_streak)
        
    
    def reset_streak(self):
        self.current_streak = 0
        
        
    def get_periodicity_int(self, periodicity_string):
        periodicity_dictionary = {
            "Daily": 1,
            "Weekly": 7,
            "Monthly": 30,
        }
        
        return periodicity_dictionary[periodicity_string]