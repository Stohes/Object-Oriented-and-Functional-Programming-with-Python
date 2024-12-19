import pytest
from unittest.mock import mock_open, patch
from datetime import datetime, timedelta
from Habit import Habit
from HabitManager import HabitManager
from Analytics import longest_streak, most_struggled_habits, current_habits


# Helper function for creating a habit with completion dates
def create_habit_with_dates(name, periodicity, completion_dates):
    habit = Habit(name=name, periodicity_string=periodicity)
    habit.completion_dates = completion_dates
    habit.current_streak = len(completion_dates)
    habit.max_streak = len(completion_dates)
    return habit


@pytest.fixture
def habit_manager():
    # Setup a fresh instance of HabitManager for each test
    manager = HabitManager()
    manager.habits = []  # Clear any loaded habits for testing
    return manager


@pytest.fixture
def mock_file_operations():
    with patch("builtins.open", mock_open()) as mocked_file:
        yield mocked_file


# Test cases for Habit class
def test_habit_complete_task():
    habit = Habit(name="Test Habit", periodicity_string="Daily")
    initial_streak = habit.current_streak

    habit.complete_task()

    assert len(habit.completion_dates) == 1
    assert habit.completion_dates[-1].date() == datetime.now().date()
    assert habit.current_streak == initial_streak


def test_habit_is_broken():
    habit = Habit(name="Test Habit", periodicity_string="Daily")
    habit.completion_dates.append(datetime.now() - timedelta(days=3))

    assert habit.is_broken() is True

    habit.completion_dates.append(datetime.now())
    assert habit.is_broken() is False


def test_habit_reset_streak():
    habit = Habit(name="Test Habit", periodicity_string="Daily", current_streak=5)

    habit.reset_streak()

    assert habit.current_streak == 0


def test_habit_increase_streak():
    habit = Habit(name="Test Habit", periodicity_string="Daily", current_streak=2, max_streak=3)

    habit.increase_streak()

    assert habit.current_streak == 3
    assert habit.max_streak == 3


# Test cases for HabitManager
def test_create_habit(habit_manager, mock_file_operations):
    habit_manager.create_habit(name="Test Habit", periodicity="Daily")

    assert len(habit_manager.habits) == 1
    assert habit_manager.habits[0].name == "Test Habit"
    assert habit_manager.habits[0].periodicity_string == "Daily"


def test_delete_habit(habit_manager, mock_file_operations):
    habit_manager.create_habit(name="Test Habit", periodicity="Daily")

    habit_manager.delete_habit("Test Habit")

    assert len(habit_manager.habits) == 0


def test_complete_habit(habit_manager, mock_file_operations):
    habit_manager.create_habit(name="Test Habit", periodicity="Daily")
    habit_manager.complete_habit("Test Habit")

    habit = habit_manager.habits[0]
    assert len(habit.completion_dates) == 1
    assert habit.current_streak == 1
    assert habit.max_streak == 1


# Test cases for Analytics
def test_longest_streak():
    habits = [
        create_habit_with_dates("Habit 1", "Daily", [datetime.now() - timedelta(days=i) for i in range(5)]),
        create_habit_with_dates("Habit 2", "Weekly", [datetime.now() - timedelta(weeks=i) for i in range(3)])
    ]

    assert longest_streak(habits) == 5


def test_most_struggled_habits():
    habits = [
        create_habit_with_dates("Habit 1", "Daily", [
            datetime.now() - timedelta(days=0),
            datetime.now() - timedelta(days=4),
            datetime.now() - timedelta(days=8)
        ]),
        create_habit_with_dates("Habit 2", "Weekly", [
            datetime.now() - timedelta(weeks=0),
            datetime.now() - timedelta(weeks=3)
        ])
    ]

    assert most_struggled_habits(habits) == ["Habit 1", "Habit 2"]


def test_current_habits():
    habits = [
        create_habit_with_dates("Habit 1", "Daily", [datetime.now() - timedelta(days=i) for i in range(5)]),
        create_habit_with_dates("Habit 2", "Weekly", []),
    ]

    assert current_habits(habits) == ["Habit 1"]
