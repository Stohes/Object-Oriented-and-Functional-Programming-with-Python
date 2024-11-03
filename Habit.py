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
        
        if delta > periodicity_int:
            return True
        else:
            return False
        
    
    def get_current_streak(self):
        return self.current_streak
    
    
    def get_max_streak(self):
        return self.max_streak
    
    
    def increase_streak(self):
        self.current_streak += 1
        
    
    def reset_streak(self):
        self.max_streak = max(self.current_streak, self.max_streak)
        self.current_streak = 0
        
        
    def get_periodicity_int(self, periodicity_string):
        periodicity_dictionary = {
            "daily": 1,
            "weekly": 7,
            "monthly": 30,
        }
        
        return periodicity_dictionary[periodicity_string]