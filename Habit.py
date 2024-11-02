from dataclasses import dataclass
from datetime import datetime


@dataclass
class Habit:
    id: int
    name: str
    periodicity_string: str
    periodicity_int: int
    created_at: datetime
    completion_dates: list
    current_streak: int
    max_streak: int
    
    
    def complete_task(self):
        current_date = datetime.now()
        self.completion_dates.append(current_date)
        
    
    def is_broken(self):
        last_completion = self.completion_dates[-1]
        current_date = datetime.now()
        
        delta = current_date - last_completion
        
        if delta > self.periodicity_int:
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