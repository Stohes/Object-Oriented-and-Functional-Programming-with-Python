def longest_streak(habits):
    return max((habit.max_streak for habit in habits), default=0)


def most_struggled_habits(habits):
    def missed_completions(habit):
        missed = 0
        periodicity_int = habit.get_periodicity_int(habit.periodicity_string)
        for i in range(1, len(habit.completion_dates)):
            delta = (habit.completion_dates[i] - habit.completion_dates[i - 1]).days
            missed += max(0, delta // periodicity_int - 1)
        return missed
    
    struggled_habits = sorted(habits, key=missed_completions, reverse=True)
    return [habit.name for habit in struggled_habits if missed_completions(habit) > 0]


def current_habits(habits):
    return [habit.name for habit in habits if habit.current_streak > 0]
